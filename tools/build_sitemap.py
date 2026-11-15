#!/usr/bin/env python3
"""Writes sitemap.xml and robots.txt at the site root.
sitemap.xml lists the three homepages (with hreflang alternates) and every real work page under /project/.
Left out: the short "moved" stub pages, ARCHIVO/, backups/, tools/, lstm/, coming/ and images/.
lastmod is the date of the file's last git commit.
Run after build_home.py and build_work.py:  python tools/build_sitemap.py"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_work import STUBS  # noqa
import work_content as C  # noqa

ROOT = os.path.dirname(HERE)
SITE = "https://www.mario-guzman.com/"


def lastmod(path):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT, capture_output=True, encoding="utf-8").stdout.strip()
    return out or None


def url(loc, path, extra=""):
    lm = lastmod(path)
    return "  <url>\n    <loc>%s</loc>\n%s%s  </url>\n" % (loc, ("    <lastmod>%s</lastmod>\n" % lm) if lm else "", extra)


homes = [("", "index.html"), ("es/", "es/index.html"), ("fr/", "fr/index.html")]
alts = "".join('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>\n' % (l, SITE + p)
               for l, p in (("en", ""), ("es", "es/"), ("fr", "fr/"))) + \
       '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n' % SITE
xml = ['<?xml version="1.0" encoding="UTF-8"?>\n',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n']
for loc, path in homes:
    xml.append(url(SITE + loc, path, alts))
for p in C.PAGES:
    if p["slug"] in STUBS:
        continue
    f = "project/%s.html" % p["slug"]
    assert os.path.exists(os.path.join(ROOT, f)), f
    xml.append(url(SITE + f, f))
xml.append("</urlset>\n")
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(xml))
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write("User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /backups/\nDisallow: /ARCHIVO/\n\nSitemap: %ssitemap.xml\n" % SITE)
print("wrote sitemap.xml (%d urls) and robots.txt" % (len(homes) + sum(1 for p in C.PAGES if p["slug"] not in STUBS)))
