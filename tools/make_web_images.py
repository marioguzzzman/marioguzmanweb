#!/usr/bin/env python3
"""Make web-sized images for the site.

For every image a page uses this writes, to images/web/<project>/:
    <name>.jpg        at most 1800 px wide, JPEG quality 80
    <name>-thumb.jpg  700 px wide
Originals are never touched or moved. Sources are either files under images/
(Mario's originals) or files under images/external/ (images that came from
other sites or were supplied separately, copied into the repo so the build
does not depend on the network).

Run from anywhere:  python tools/make_web_images.py
Needs Pillow.
"""
import os
import shutil
import sys
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
OUT = os.path.join(IMG, "web")
EXT = os.path.join(IMG, "external")

MAX_W, THUMB_W, QUALITY, MAX_BYTES = 1800, 700, 80, 500 * 1024

P = "projects/"
# project -> list of (name, source relative to images/ [, options])
# options: {"crop": (left, top, right, bottom) in pixels} or {"aspect": w/h centred crop}
MANIFEST = {
    "global": [
        ("mario-guzman-2026", "external/global/portrait-web.jpg"),
    ],
    "liminal": [
        ("lead", "home/liminalSanctuaryhome1.png"),
        ("01", P + "liminal/liminalSanctuary1.png"),
        ("02", P + "liminal/liminalSanctuary2.png"),
        ("03", P + "liminal/liminalSanctuary3.png"),
    ],
    "golem": [
        ("lead", P + "golem/golem_screen2.png"),
        ("main", "home/mario-guzman-golem_main_2023.png"),
        ("screen1", P + "golem/golem_screen1.png"),
        ("screen3", P + "golem/golem_screen3.png"),
        ("je-suis", P + "golem/golem_je_suis.png"),
        ("sitting", P + "golem/golem_sitting.jpeg"),
        ("closeup", P + "golem/golem_closeup1.jpg"),
        ("people-working", P + "golem/golem_people_working.jpg"),
        ("mini", P + "golem/golem_mini.jpg"),
    ],
    "seeds": [
        ("lead", "external/seeds/seed-original.png"),
    ],
    "conciencia": [
        ("lead", "home/mario-guzman-conciencia_main_2022.jpg"),
        ("01", P + "conciencia/consciousness1.png"),
        ("02", P + "conciencia/consciousness2.jpg"),
        ("03", P + "conciencia/consciousness3.png"),
    ],
    "cenote": [
        ("lead", P + "cenote/cenote_portal.jpg"),
        ("01", P + "cenote/cenote1.jpg"),
        ("02", P + "cenote/cenote2.png"),
        ("03", P + "cenote/cenote3.png"),
    ],
    "nierika": [
        ("lead", P + "combinatory-nierika/mario-guzman-combinatory-nierika-2020.jpg"),
    ],
    "learning": [
        ("lead", P + "lstm/lstm1.png"),
        ("01", P + "lstm/forest.png"),
        ("02", P + "lstm/networks.png"),
    ],
    "memory": [
        ("lead", "home/mario-guzman-memory-of-everywhere-2020.jpg"),
    ],
    "bitcelulle": [
        ("lead", P + "bitcelulle/bitcelulle3.png"),
        ("01", P + "bitcelulle/bitcelulle5.jpg"),
    ],
    "quetzabot": [
        ("lead", P + "quetzabot/quetzabot1.jpg"),
        ("01", P + "quetzabot/quetzabot3.jpg"),
        ("02", P + "quetzabot/quetzabot4.jpg"),
        ("03", P + "quetzabot/quetzabot10.jpg"),
    ],
    "temazcalli": [
        ("lead", P + "temazcalli/chamanportada.png"),
        ("01", P + "temazcalli/temazdomechaman.png"),
        ("02", P + "temazcalli/temazdome.png"),
        ("03", P + "temazcalli/temaztemaz.png"),
        ("04", P + "temazcalli/temazchaman.jpg"),
        ("05", P + "temazcalli/temazestrellas.jpg"),
        ("06", P + "temazcalli/temazgroovysmall.jpg"),
        ("07", P + "temazcalli/temazflor.png"),
        ("08", P + "temazcalli/temaziniciosmall.jpg"),
        ("codex1", P + "temazcalli/codice1.jpg"),
        ("codex2", P + "temazcalli/codice2.jpg"),
        ("long", P + "temazcalli/temazlong.jpg"),
        ("jaguar", P + "temazcalli/jaguar.jpg"),
        ("making-of", P + "temazcalli/makingOf.jpg"),
        ("rochelle", P + "temazcalli/rochelle.png"),
    ],
    "ped": [
        ("lead", "home/ped.jpg"),
        ("01", P + "ped/1ped.png"),
        ("03", P + "ped/3ped.png"),
        ("04", P + "ped/4ped.png"),
        ("cck", P + "ped/cck.png"),
    ],
    "oraculo": [
        ("lead", P + "oraculo/oraculo1.png"),
        ("02", P + "oraculo/oraculo2.png"),
        ("03", P + "oraculo/oraculo3.png"),
        ("05", P + "oraculo/oraculo5.png"),
        ("06", P + "oraculo/oraculo6.png"),
        ("portada", P + "oraculo/oraculoportada.jpg"),
    ],
    "lastagreement": [
        ("lead", "home/mario-guzman-last-agreement-video-dance-performance-vhs-2016.jpg"),
    ],
    "visionoros": [
        ("lead", "home/visionoros.png"),
        ("01", P + "visionoros/image01.jpg"),
        ("02", P + "visionoros/2.jpg"),
        ("03", P + "visionoros/1.png"),
        ("04", P + "visionoros/image00.jpg"),
        ("05", P + "visionoros/image02.jpg"),
        ("06", P + "visionoros/3.png"),
    ],
    "hiperstories": [
        ("lead", "home/mario-guzman-infinitud-infinita-hipertext-infinity-discrete.jpg"),
        ("01", P + "hiperstories/txt3.jpg"),
        ("02", P + "hiperstories/txt4.jpg"),
        ("03", P + "hiperstories/txt5.jpg"),
        ("04", P + "hiperstories/txt2.png"),
    ],
    "prepixel": [
        ("lead", "home/mario-guzman-prepixel-nosferatu-vhs-2014.jpg"),
    ],
    "ona": [
        ("lead", "external/ona/ona_1.jpg"),
        ("02", "external/ona/ona_2.jpg"),
    ],
    "she-tells": [
        ("lead", "external/she-tells/hero_image_shellphone.png"),
        ("kit-board-and-shell", "external/she-tells/kit-board-and-shell.jpg"),
        ("with-shell", "external/she-tells/19-with-shell.jpg"),
        ("board-in-box", "external/she-tells/kit-board-in-box.jpg"),
        ("transducer", "external/she-tells/21-transducer-in-shell.jpg"),
        ("complete", "external/she-tells/20-complete-with-power.jpg"),
        ("pcb-front", "external/she-tells/PCB_front_image_shellphone.png"),
    ],
    "robots": [
        ("desdemona-robot", "external/robots/desdemona-robot.jpg"),
        ("desdemona-phone", "external/robots/desdemona.jpg"),
        ("legible", "external/robots/legible.jpg"),
        # The Sophia stills: maxres is clean 16:9; the other is 4:3 with baked-in
        # black bars, so the bars (60 px top and bottom) are trimmed off.
        ("sophia-awakening", "external/robots/sophia-xuVYl2KzpHI.jpg"),
        ("sophia-nature", "external/robots/sophia-L0EFisbhwPs.jpg", {"crop": (0, 60, 640, 420)}),
    ],
    "mirar": [
        ("lead", "external/mirar/cielos4.png"),
        ("center", "external/mirar/cielos4.png", {"aspect": 1.11}),
    ],
}


def centre_crop(im, aspect):
    w, h = im.size
    if w / h > aspect:
        nw = round(h * aspect)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = round(w / aspect)
    y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def save(im, path, width):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    q = QUALITY
    while True:
        im.save(path, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(path) <= MAX_BYTES or q <= 55:
            break
        q -= 5
    return os.path.getsize(path)


def main():
    done = 0
    for project, items in MANIFEST.items():
        d = os.path.join(OUT, project)
        os.makedirs(d, exist_ok=True)
        for item in items:
            name, src = item[0], item[1]
            opts = item[2] if len(item) > 2 else {}
            path = os.path.join(IMG, src)
            if not os.path.exists(path):
                print("MISSING", src)
                sys.exit(1)
            im = ImageOps.exif_transpose(Image.open(path))
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGBA")
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[-1])
                im = bg
            else:
                im = im.convert("RGB")
            if "crop" in opts:
                im = im.crop(opts["crop"])
            if "aspect" in opts:
                im = centre_crop(im, opts["aspect"])
            a = save(im, os.path.join(d, name + ".jpg"), MAX_W)
            b = save(im, os.path.join(d, name + "-thumb.jpg"), THUMB_W)
            done += 1
            print("%-12s %-22s %4d KB  thumb %3d KB" % (project, name, a // 1024, b // 1024))
    # the Kanape chair is an SVG: copied as it is
    g = os.path.join(OUT, "global")
    shutil.copyfile(os.path.join(EXT, "global", "kanape-chair.svg"), os.path.join(g, "kanape-chair.svg"))
    print("done:", done, "images")


if __name__ == "__main__":
    main()
