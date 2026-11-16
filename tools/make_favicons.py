#!/usr/bin/env python3
"""Writes favicon.svg, favicon.ico (32 px) and apple-touch-icon.png (180 px) at the site root:
the initials MG in white on the site's red-orange square. Needs Pillow and a bold sans-serif font
(Arial Bold on Windows, Liberation or DejaVu Sans Bold elsewhere).
Run:  python tools/make_favicons.py"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RED = (0xD9, 0x36, 0x1A)
FONTS = [r"C:\Windows\Fonts\arialbd.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/System/Library/Fonts/Helvetica.ttc"]

SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" fill="#d9361a"/>
<text x="32" y="43" text-anchor="middle" font-family="'Helvetica Neue',Helvetica,Arial,sans-serif" font-weight="700" font-size="30" letter-spacing="-1" fill="#fff">MG</text>
</svg>
"""


def render(size):
    font_path = next(p for p in FONTS if os.path.exists(p))
    im = Image.new("RGB", (size, size), RED)
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, round(size * 0.47))
    box = d.textbbox((0, 0), "MG", font=font)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((size - w) / 2 - box[0], (size - h) / 2 - box[1]), "MG", font=font, fill="white")
    return im


with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8", newline="\n") as f:
    f.write(SVG)
render(32).save(os.path.join(ROOT, "favicon.ico"), sizes=[(32, 32)])
render(180).save(os.path.join(ROOT, "apple-touch-icon.png"))
print("wrote favicon.svg, favicon.ico, apple-touch-icon.png")
