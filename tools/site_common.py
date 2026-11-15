"""Shared bits for the page generators (build_home.py, build_work.py).
The generators write plain, finished HTML files. They are authoring helpers only;
the site itself needs no build step."""
import html

SITE = "https://www.mario-guzman.com/"
EMAIL = "mailto:marioguzzzman@gmail.com"
INSTAGRAM = "https://instagram.com/marioguzzzman/"
GITHUB = "https://github.com/marioguzzzman"
ORCID = "https://orcid.org/0009-0002-6914-5825"


def esc(s):
    return html.escape(s, quote=True)


def head(lang, title, description, og_image, canonical_path, root, extra=""):
    """<head> shared by every page. root is '' or '../'."""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="canonical" href="{SITE}{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mario Guzman">
<meta property="og:url" content="{SITE}{canonical_path}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}{og_image}">
<meta name="twitter:card" content="summary_large_image">
{extra}<link rel="stylesheet" href="{root}css/site.css">
</head>
"""


def contact_row(label_email="email"):
    return f"""<div class="contact">
      <a class="link" href="{EMAIL}">{label_email}</a>
      <a class="link" href="{INSTAGRAM}">instagram</a>
      <a class="link" href="{GITHUB}">github</a>
      <a class="link" href="{ORCID}">orcid</a>
    </div>"""


PERSON_ID = SITE + "#mario-guzman"


def ld_script(data):
    import json
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/") + "</script>\n"


def person_ld():
    """The one Person block, on the homepages. Only these facts."""
    return ld_script({
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "Mario Guzman",
        "alternateName": "Mario Guzmán",
        "url": SITE,
        "image": SITE + "images/web/global/mario-guzman-2026.jpg",
        "jobTitle": "Artist-researcher and creative technologist",
        "affiliation": {"@type": "CollegeOrUniversity", "name": "La Rochelle Université"},
        "knowsAbout": ["artificial voice", "social robotics", "new media art", "electronic literature", "human-robot interaction"],
        "sameAs": ["https://orcid.org/0009-0002-6914-5825", "https://github.com/marioguzzzman", "https://instagram.com/marioguzzzman/"],
    })
