# TODO-CONTENT: what Mario still has to supply or decide

Nothing here was guessed. Each gap is left visible on the site or left out.

## Open questions from the brief

- **Desdemona videos** are Mux streams. They open in the overlay player on the homepage (`player.mux.com`). If that player does not work for you, supply MP4 files or a public page to link to.
- **Recording or abstract links** for the texts and talks that point nowhere yet: Reconstitution (Routledge, forthcoming) has no link.
- **Venue lines** still missing: Pre-pixel Symphony in Major Fractal I (no venue in the homepage row; its page lists one exhibition, Paco Urondo Cultural Center, 2016), Cenote Reflections (page has no venue line, see below), Visionoros Collective, Memory of Everywhere has no page.
- **Language versions:** ES and FR versions of each work page (work pages are English only for now).
- **Spanish and French text is a draft** for Mario to correct (interface text, section names, role line, opening statement, section leads, About bio). The Sophia and Desdemona blurbs and the row descriptions (venues, credits) are kept in English on purpose.

## Problems found in the old pages (decide, then I fix)

- `combinatory_nierika.html` was a copy of the Learning to Write page. The new page has only the title, 2020, "Taper #5", "POSVERSO 2026" and a link to the Taper #5 page (the old homepage linked there). Needs a text, credits and images (images exist in `images/projects/combinatory-nierika/`, not yet used).
- `cenotes.html` carried the Exhibitions and Press of Quetzalcóatl-bot (ZERO1 2017, Electronic November, 105º Salón Nacional, Poetic Hybrids, Inlets/Outlets, Malacara Press). They were left out. Please supply the real exhibitions and press for Cenote Reflections.
- `conciencia.html`: Press was a placeholder ("ACA poner lo de HOLO magazine"), left out. The body text still says "Consciousness is the foreknowledge of the universal mind"; the title now follows your choice, "Precooking". Decide whether the body text should change too.
- `ped.html` had a broken image (`2ped.JPG` does not exist). It is not on the page. Photos named `PED MARIO GUZMAN 1-5.jpg` exist in `images/projects/ped/` if you want more.
- `lastagreement.html` and `prepixel.html` have only one image each (low resolution, 765 px). Better photos would help.
- `aerodynamics-seeds.html`: the page uses only the seed image. The Works row links to the project site.
- `learningtowrite.html`: the exhibitions list uses your wording ("Game On! The Art in Videogames", ACUD MACHT NEU). Old press link kept.
- Old typos in your project texts were kept word for word (for example "instuments", "Natual", "adecuate", "OEtymologically", "glitchs"). Say if you want them corrected.
- Videos from the old pages: Vimeo links open in the overlay player (lead image or "Watch" link). YouTube videos on three pages are lazy embeds.
- Alt texts on work-page photos are short and generic. Please refine.
- The Creative technologist list has no pages in the brief for Legible Journey and Mirar al cielo, so two small pages were added (`project/legible-journey.html`, `project/mirar-al-cielo.html`) using only facts from the mockup. Years are missing there.
- ONA page: text and credits are from pleek.net as given, with the venue written as you asked. The spelling "Lights sinchronization" there was changed to your credit line.

## Not migrated

- `project/ai-seeds.html` and `project/ocean.html`: unfinished stubs with the old template's Xbox images. Replaced by a short "moved" page.
- `project/bio.html`, `exhibits.html`, `texts.html`, `writing.html`, `workshops.html`, `classes.html`, `experimental.html`: replaced by short pages pointing to the matching homepage section (workshops and classes point to About; there is no workshops section).
- `project/originales/`: the original template author's client pages. Ask Mario before deleting.
- Removed as unused leftovers of the old template: `bootstrap-4.4.1-dist/`, `photography.html` (Austin DeHaven's page), `index-boot.html`. All remain in git history (commit "Snapshot of old design before v2").
- `coming/`, `lstm/` and `images/projects/temazcalli/*.html` still mention jQuery or Typekit. They are protected by the brief and were not touched.

## Deployment (for Mario)

Not part of this build. Pushes to `master` since March 2025 have not reached the server. Check GitHub, Settings, Webhooks, and how files reach the server (SSH and `git pull`, or an upload).

## Other

- Profile photo: `images/web/global/mario-guzman-2026.jpg` is made from the 1200 px web copy. Replace `images/external/global/portrait-web.jpg` with the 3470 px original if you want a sharper file, then run `python tools/make_web_images.py`.
- Contact links: email, Instagram and GitHub use the addresses from the old site (`marioguzzzman`).
- Tools: `tools/make_web_images.py` (images), `tools/build_home.py` and `tools/build_work.py` (write the HTML pages from the text in `tools/work_content.py`), `tools/check_site.py` (browser check). The site itself needs no build step.
