#!/usr/bin/env python3
"""Browser check of every page, using headless Chrome over the DevTools protocol.
Needs Chrome or Edge, and aiohttp. Start `python -m http.server 8137` at the repo root first.

For each page, at 320, 360, 375, 390, 412 and 1280 px wide it reports: console errors, requests to hosts
other than the site and YouTube, horizontal overflow, broken images, and bytes transferred
on first load (without scrolling).

Run:  python tools/check_site.py [base_url]
"""
import asyncio
import glob
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

import aiohttp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8137"
PORT = 9333
WIDTHS = (320, 360, 375, 390, 412, 1280)
CHROME = next((p for p in (
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium") if os.path.exists(p)), None)
ALLOWED = ("localhost", "127.0.0.1", "youtube.com", "youtube-nocookie.com", "ytimg.com")


def pages():
    if len(sys.argv) > 2:
        return sys.argv[2:]
    out = ["index.html", "es/index.html", "fr/index.html"]
    out += sorted("project/" + os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "project", "*.html")))
    return out


class Cdp:
    def __init__(self, ws):
        self.ws, self.n, self.waiters, self.events = ws, 0, {}, []

    async def pump(self):
        async for msg in self.ws:
            d = json.loads(msg.data)
            if "id" in d and d["id"] in self.waiters:
                self.waiters.pop(d["id"]).set_result(d)
            else:
                self.events.append(d)

    async def call(self, method, **params):
        self.n += 1
        fut = asyncio.get_event_loop().create_future()
        self.waiters[self.n] = fut
        await self.ws.send_str(json.dumps({"id": self.n, "method": method, "params": params}))
        return (await fut).get("result", {})


async def check(cdp, url, width):
    cdp.events.clear()
    await cdp.call("Emulation.setDeviceMetricsOverride", width=width, height=900, deviceScaleFactor=1, mobile=width < 600)
    await cdp.call("Emulation.setTouchEmulationEnabled", enabled=width < 600, maxTouchPoints=5)
    await cdp.call("Page.navigate", url=url)
    await asyncio.sleep(0.3)
    # phones have no hover: emulate it so the touch-only styles are tested too
    await cdp.call("Emulation.setEmulatedMedia", features=[
        {"name": "hover", "value": "none" if width < 600 else "hover"},
        {"name": "pointer", "value": "coarse" if width < 600 else "fine"}])
    await asyncio.sleep(2.2)
    reqs, errs, size = {}, [], 0
    for e in cdp.events:
        m, p = e.get("method"), e.get("params", {})
        if m == "Network.requestWillBeSent":
            reqs[p["requestId"]] = p["request"]["url"]
        elif m == "Network.loadingFinished":
            size += p.get("encodedDataLength", 0)
        elif m == "Runtime.exceptionThrown":
            errs.append(p["exceptionDetails"].get("text", "exception"))
        elif m == "Runtime.consoleAPICalled" and p.get("type") == "error":
            errs.append("console.error")
        elif m == "Log.entryAdded" and p["entry"].get("level") == "error":
            errs.append(p["entry"].get("text", "") + " " + p["entry"].get("url", ""))
        elif m == "Network.loadingFailed":
            errs.append("failed: " + reqs.get(p["requestId"], "?"))
    hosts = sorted({u.split("/")[2] for u in reqs.values() if u.startswith("http")})
    bad_hosts = [h for h in hosts if not any(h == a or h.endswith("." + a) or h.startswith(a) for a in ALLOWED)]
    js = """(async()=>{[...document.images].forEach(i=>{i.loading='eager'});await new Promise(r=>setTimeout(r,1500));
      let mr=0,who='';document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.right>mr&&getComputedStyle(e).position!=='fixed'&&!e.closest('#box')){mr=r.right;who=e.tagName+'.'+(e.className||e.id||'')+' '+(e.textContent||'').trim().slice(0,20)}});
      return JSON.stringify({sw:Math.max(document.documentElement.scrollWidth,Math.ceil(mr)),iw:__W__,who:who,rowsok:[...document.querySelectorAll('.over .r')].every(r=>{const t=[...r.querySelectorAll('.c')].map(c=>Math.round(c.getBoundingClientRect().top));return t.every(x=>x===t[0])}),stills:[...document.querySelectorAll('.bots .vid')].map(v=>Math.round(v.getBoundingClientRect().width)).join('/'),nohover:matchMedia('(hover:none)').matches,
      bad:[...document.images].filter(i=>!(i.complete&&i.naturalWidth>0)).map(i=>i.src),
      h1:document.querySelectorAll('h1').length,noalt:[...document.images].filter(i=>!i.hasAttribute('alt')).length})})()"""
    r = await cdp.call("Runtime.evaluate", expression=js.replace("__W__", str(width)), awaitPromise=True, returnByValue=True)
    info = json.loads(r["result"]["value"])
    return dict(size=size, errs=errs, bad_hosts=bad_hosts, **info)


async def main():
    if not CHROME:
        sys.exit("no Chrome or Edge found")
    prof = tempfile.mkdtemp()
    proc = subprocess.Popen([CHROME, "--headless=new", f"--remote-debugging-port={PORT}", f"--user-data-dir={prof}",
                             "--no-first-run", "--disable-gpu", "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(40):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
                break
            except Exception:
                time.sleep(0.5)
        ws_url = next(t["webSocketDebuggerUrl"] for t in tabs if t["type"] == "page")
        async with aiohttp.ClientSession() as s, s.ws_connect(ws_url, max_msg_size=0) as ws:
            cdp = Cdp(ws)
            asyncio.ensure_future(cdp.pump())
            for d in ("Page", "Network", "Runtime", "Log"):
                await cdp.call(d + ".enable")
            await cdp.call("Network.setCacheDisabled", cacheDisabled=True)
            problems = 0
            for page in pages():
                for w in WIDTHS:
                    r = await check(cdp, f"{BASE}/{page}", w)
                    flags = []
                    if r["errs"]:
                        flags.append("ERRORS " + "; ".join(r["errs"][:3]))
                    if r["bad_hosts"]:
                        flags.append("HOSTS " + ",".join(r["bad_hosts"]))
                    if r["sw"] > r["iw"]:
                        flags.append(f"OVERFLOW {r['sw']}>{r['iw']} ({r['who']})")
                    if r["bad"]:
                        flags.append("BROKEN IMG " + ", ".join(r["bad"][:3]))
                    if w < 600 and not r["nohover"]:
                        flags.append("hover:none emulation not active")
                    if "rowsok" in r and r["rowsok"] is False and w < 600:
                        flags.append("overview cells not top-aligned")
                    st = r.get("stills", "").split("/")
                    if len(st) == 4 and len(set(st)) != 1:
                        flags.append("robot stills differ in size " + r["stills"])
                    if r["h1"] != 1:
                        flags.append(f"h1 x{r['h1']}")
                    if r["noalt"]:
                        flags.append(f"{r['noalt']} img without alt")
                    problems += bool(flags)
                    print("%-38s %4d px  %6d KB  %s" % (page, w, r["size"] // 1024, "OK" if not flags else " | ".join(flags)))
            print("pages with problems:", problems)
    finally:
        proc.terminate()


asyncio.run(main())
