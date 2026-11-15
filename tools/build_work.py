#!/usr/bin/env python3
"""Writes project/*.html from tools/work_content.py (the shared work-page template).
Run:  python tools/build_work.py            (write the pages)
      python tools/build_work.py --verify   (check Mario's text against the old pages in git)
"""
import html
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from site_common import *  # noqa
import work_content as C  # noqa

ROOT = os.path.dirname(HERE)
SNAPSHOT = "8fb3430"  # commit "Snapshot of old design before v2"
W = "images/web/"
LISTS = json.load(open(os.path.join(HERE, "work_lists.json"), encoding="utf-8"))
BY = {p["slug"]: p for p in C.PAGES}
TECH = {"she-tells-sea-shells", "ona", "legible-journey", "mirar-al-cielo"}


def short(s, n=200):
    s = s.strip()
    if len(s) <= n:
        return s
    cut = s[:n]
    i = max(cut.rfind(". "), cut.rfind("? "))
    return (cut[: i + 1] if i > 60 else cut[: cut.rfind(" ")] + "...")


def img_tag(folder, name, alt, root="../", lazy=True):
    from PIL import Image
    path = os.path.join(ROOT, W, folder, name + ".jpg")
    w, h = Image.open(path).size
    la = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img src="{root}{W}{folder}/{name}.jpg" alt="{esc(alt)}" width="{w}" height="{h}"{la}>', w / h


def pack(ratios, width=1304, gap=12, target=290):
    """Split images into rows of 2 to 4 (a lone image only if it is the only one) so that every
    row is complete and row heights stay close to the target. Returns a list of index lists."""
    n = len(ratios)
    if n <= 1:
        return [list(range(n))]
    INF = float("inf")
    best = [0.0] + [INF] * n
    back = [0] * (n + 1)
    for j in range(1, n + 1):
        for k in (2, 3, 4):
            i = j - k
            if i < 0 or best[i] == INF:
                continue
            h = (width - gap * (k - 1)) / sum(ratios[i:j])
            cost = best[i] + (h - target) ** 2
            if cost < best[j]:
                best[j], back[j] = cost, i
    rows, j = [], n
    while j > 0:
        rows.append(list(range(back[j], j)))
        j = back[j]
    return rows[::-1]


def items_html(items):
    out = []
    for b, m, h in items:
        t = f'<a href="{esc(h)}">{esc(b)}</a>' if h else esc(b)
        if m:
            t += f' <span>{esc(m)}</span>'
        out.append(f"        <li>{t}</li>")
    return "\n".join(out)


def get_lists(p):
    slug = p["slug"]
    old = LISTS.get(slug, {})
    ex = [(i["b"], i["m"], i["h"]) for i in old.get("Exhibitions", [])]
    pr = [(i["b"], i["m"], i["h"]) for i in old.get("Press", [])]
    cr = [(i["b"], i["m"], "") for i in old.get("Full Credits", old.get("Credits", []))]
    if "exhibitions" in p:
        ex = p["exhibitions"]
    if "press" in p:
        pr = p["press"]
    if "credits" in p:
        cr = p["credits"]
    if p.get("drop_exhibitions"):
        ex = []
    if p.get("drop_press"):
        pr = []
    return ex, pr, cr


# works by other artists: Mario is a contributor, not the creator
CONTRIBUTOR = {"ona", "legible-journey", "mirar-al-cielo"}


def work_ld(p, og):
    data = {"@context": "https://schema.org", "@type": "CreativeWork", "name": p["title"],
            "url": f"{SITE}project/{p['slug']}.html", "image": SITE + og}
    if re.fullmatch(r"\d{4}", p["year"] or ""):
        data["dateCreated"] = p["year"]
    data["contributor" if p["slug"] in CONTRIBUTOR else "creator"] = {"@id": PERSON_ID}
    return ld_script(data)


def nav(root):
    return f"""<header>
  <div class="wrap">
    <nav aria-label="Main">
    <a class="me" href="{root}index.html">mario guzman</a>
    <a href="{root}index.html#works">works</a>
    <a href="{root}index.html#robots">robots</a>
    <a href="{root}index.html#tech">creative technologist</a>
    <a href="{root}index.html#workshops">workshops</a>
    <a href="{root}index.html#texts">texts</a>
    <a href="{root}index.html#about">about</a>
    </nav>
  </div>
</header>"""


def build(p):
    root = "../"
    slug, folder = p["slug"], p["folder"]
    lead = p.get("lead", "lead")
    title, year = p["title"], p["year"]
    desc = short(p["intro"][0]) if p["intro"] else (
        f"{title}" + (f", {year}" if year else "") + (f". {p['venue'][0]}" if p["venue"] else "") + ". A work by Mario Guzman.")
    og = f"{W}{folder}/{lead}.jpg"
    out = [head("en", f"{title} · Mario Guzman", desc, og, f"project/{slug}.html", root, work_ld(p, og))]
    out.append(f'<body data-root="{root}">\n<a class="skip" href="#content">Skip to content</a>\n{nav(root)}\n<main id="content" class="wrap">\n')
    out.append(f'  <article>\n  <div class="work-head">\n    <h1>{esc(title)}</h1>\n    <div class="meta">')
    out.append(f'      <p>{esc(year)}</p>')
    out.append(f'      <p>{"<br>".join(esc(v) for v in p["venue"])}</p>')
    out.append(f'      <p>{esc(p["people"])}</p>\n    </div>\n  </div>')
    tag, ratio = img_tag(folder, lead, p["lead_alt"], root, lazy=False)
    if p.get("video"):
        out.append(f'  <a class="work-lead" href="{p["video"]}">{tag}</a>')
    else:
        out.append(f'  <div class="work-lead">{tag}</div>')
    if p["intro"]:
        paras = p.get("intro_html") or [esc(t) for t in p["intro"]]
        out.append('  <div class="block nohead"><div class="prose">' + "".join(f"<p>{t}</p>" for t in paras) + "</div></div>")
    if p.get("intro_credit"):
        out.append(f'  <p class="sm soft prose" style="margin-top:10px">{esc(p["intro_credit"])}</p>')
    if p.get("intro_link"):
        out.append(f'  <p class="prose" style="margin-top:18px;font-size:24px"><a href="{p["intro_link"][1]}">{esc(p["intro_link"][0])}</a></p>')
    sub = [esc(x) for x in (p.get("kind"), p.get("tech")) if x]
    if sub:
        out.append('  <p class="sm soft prose" style="margin-top:14px">' + "<br>".join(sub) + "</p>")
    for k, v in p.get("detail", []):
        out.append(f'  <p class="sm prose" style="margin-top:10px"><b style="font-weight:400" class="soft">{esc(k)}</b> {esc(v)}</p>')
    for k, items in p.get("detail_links", []):
        links = " · ".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in items)
        out.append(f'  <p class="sm prose" style="margin-top:10px"><span class="soft">{esc(k)}:</span> {links}</p>')
    for blk in p["blocks"]:
        kind = blk[0]
        if kind == "t":
            out.append(f'  <section class="block">\n    <h2>{esc(blk[1])}</h2>\n    <div class="prose">' + "".join(f"<p>{esc(t)}</p>" for t in blk[2]) + "</div>\n  </section>")
        elif kind == "links":
            links = " · ".join(f'<a href="{esc(h)}">{esc(t)}</a>' for t, h in blk[2])
            out.append(f'  <p class="sm prose" style="margin-top:14px"><span class="soft">{esc(blk[1])}:</span> {links}</p>')
        elif kind == "i":
            figs, ratios = [], []
            for it in blk[1]:
                name, alt, cap = (it, f"{title}", "") if isinstance(it, str) else it
                tag, r = img_tag(folder, name, alt, root)
                c = f"<figcaption>{esc(cap)}</figcaption>" if cap else ""
                figs.append(f'<figure style="--r:{r:.4f}">{tag}{c}</figure>')
                ratios.append(r)
            rows = "\n".join('    <div class="gr">' + "".join(figs[i] for i in row) + "</div>" for row in pack(ratios))
            cls = "grid half" if len(blk) > 2 and blk[2] == "half" else "grid"
            out.append(f'  <div class="{cls}">\n' + rows + "\n  </div>")
        elif kind == "vimg":
            tag, r = img_tag(folder, blk[3] if len(blk) > 3 else lead, blk[2], root)
            out.append(f'  <a class="work-lead" style="margin-top:40px" href="{blk[1]}">{tag}</a>')
        elif kind == "v":
            out.append(f'  <p class="playlink"><a class="link" href="{blk[1]}">&#9654; {esc(blk[2])}</a></p>')
        elif kind == "yt":
            out.append(f'  <div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{blk[1]}" title="{esc(blk[2])}" loading="lazy" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>')
    # lists
    ex, pr, cr = get_lists(p)
    cols = []
    if ex:
        cols.append(("Exhibitions", ex))
    if pr:
        cols.append(("Press", pr))
    if p.get("links"):
        cols.append(("Links", [(t, "", h) for t, h in p["links"]]))
    if cr:
        cols.append((p.get("credit_title", "Credits"), [(c[0], c[1], "") for c in cr]))
    if cols:
        out.append(f'  <div class="lists n{min(3, len(cols))}">')
        for h, items in cols:
            out.append(f'    <div>\n      <h2>{h}</h2>\n      <ul>\n{items_html(items)}\n      </ul>\n    </div>')
        out.append("  </div>")
    if p.get("source"):
        out.append(f'  <p class="sm soft" style="margin-top:24px">Source: <a href="{p["source"]}">{p["source"].replace("https://", "")}</a></p>')
    # one link back to the section the page belongs to
    if slug in TECH:
        back = ("../index.html#tech", "Back to creative technologist")
    else:
        back = ("../index.html#works", "Back to works")
    out.append(f'  <nav class="pager" aria-label="Back"><a href="{back[0]}">{back[1]}</a></nav>')
    out.append("  </article>\n</main>\n<footer>\n  <div class=\"wrap\">\n    " + contact_row() + "\n  </div>\n</footer>")
    out.append(f'<script src="{root}js/site.js"></script>\n</body>\n</html>\n')
    return "\n".join(out)


# ---------------------------------------------------------------- verify
SKIP_VERIFY = {"she-tells-sea-shells", "ona", "legible-journey", "mirar-al-cielo", "combinatory_nierika"}
# spelling corrections made to Mario's old text (whitespace removed, as plain() does)
FIXES = [("OEtymologically", "Etymologically"), ("prehispanicinstuments", "prehispanicinstruments"), ("Natual", "Natural"),
         ("adecuate", "adequate"), ("glitchs", "glitches"), ("TrestheFebrero", "TresdeFebrero"), ("Luterie", "Lutherie"),
         ("Chamanism", "Shamanism"), ("theNNRmodel", "theRNNmodel"), ("AgustinRamos", "AgustínRamos"),
         ("foreknowledge", "precooking"), ("Prehispanicinstuments", "Prehispanicinstruments")]

def plain(src):
    src = re.sub(r"(?s)<!--.*?-->", "", src)
    src = re.sub(r"(?s)<(script|style)\b.*?</\1>", "", src)
    src = re.sub(r"<[^>]+>", " ", src)
    return re.sub(r"\s+", "", html.unescape(src))


def verify():
    bad = 0
    for p in C.PAGES:
        slug = p["slug"]
        if slug in SKIP_VERIFY:
            print(f"-- {slug}: text from the brief or another site, skipped")
            continue
        r = subprocess.run(["git", "show", f"{SNAPSHOT}:{p.get('old', 'project/' + slug + '.html')}"], cwd=ROOT, capture_output=True, encoding="utf-8")
        if r.returncode != 0:
            print(f"-- {slug}: no old page, skipped")
            continue
        old = plain(r.stdout)
        for a, b in FIXES:
            old = old.replace(a, b)
        strings = list(p["intro"]) + [x for x in (p.get("kind"), p.get("tech")) if x]
        for blk in p["blocks"]:
            if blk[0] == "t":
                strings.append(blk[1])
                strings += blk[2]
        strings += [v for _, v in p.get("detail", [])]
        n = 0
        for s in strings:
            variants = {s, s.replace(" / ", " "), s.replace(" / ", "")}
            ok = any(re.sub(r"\s+", "", v) in old for v in variants)
            if not ok:
                bad += 1
                print(f"  MISMATCH {slug}: {s[:90]}")
            n += 1
        print(f"-- {slug}: {n} strings checked")
    print("mismatches:", bad)
    return bad


# Old pages replaced by homepage sections: short pages that point to the matching section.
STUBS = {
    "bio": ("About", "index.html#about", "The biography is now the About section of the homepage."),
    "exhibits": ("Works", "index.html#works", "Exhibitions are now listed with each work on the homepage."),
    "texts": ("Texts", "index.html#texts", "Texts and talks are now a section of the homepage."),
    "writing": ("Texts", "index.html#texts", "Texts and talks are now a section of the homepage."),
    "workshops": ("About", "index.html#about", "This page has moved to the homepage."),
    "classes": ("About", "index.html#about", "This page has moved to the homepage."),
    "experimental": ("Works", "index.html#works", "This page has moved to the homepage."),
    "ai-seeds": ("AI Seeds / Aerodynamics of Seeds", "project/aerodynamics-seeds.html", "This page has moved."),
    "ocean": ("Works", "index.html#works", "This page has moved to the homepage."),
}


def stub(slug):
    label, target, msg = STUBS[slug]
    href = "../" + target if not target.startswith("project/") else target[len("project/"):]
    nl = chr(10)
    top = head("en", f"{label} · Mario Guzman", msg, W + "global/mario-guzman-2026.jpg", f"project/{slug}.html", "../",
               '<meta name="robots" content="noindex">' + nl)
    body = nl.join([
        '<body data-root="../">', nav("../"), '<main class="wrap">',
        f'  <div class="work-head"><h1>{esc(label)}</h1></div>',
        f'  <p class="lead">{esc(msg)} <a class="link" href="{href}">Go to {esc(label)}</a></p>',
        '</main>', '<script src="../js/site.js"></script>', '</body>', '</html>', ''])
    return top + body


def main():
    if "--verify" in sys.argv:
        sys.exit(1 if verify() else 0)
    for p in C.PAGES:
        path = os.path.join(ROOT, "project", p["slug"] + ".html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(build(p))
        print("wrote project/%s.html" % p["slug"])
    for slug in STUBS:
        with open(os.path.join(ROOT, "project", slug + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(stub(slug))
        print("wrote stub project/%s.html" % slug)


if __name__ == "__main__":
    main()
