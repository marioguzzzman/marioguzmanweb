# TODO-CONTENT: what Mario still has to supply or decide

Nothing here was guessed. Each gap is left visible on the site or left out.

## Open questions from the brief

- **Desdemona videos** are Mux streams. They open in the overlay player on the homepage (`player.mux.com`). If that player does not work for you, supply MP4 files or a public page to link to.
- **Recording or abstract links** for the texts and talks that point nowhere yet: Reconstitution (Routledge, forthcoming) has no link.
- **Venue lines** still missing: Pre-pixel Symphony in Major Fractal I (no venue in the homepage row; its page lists one exhibition, Paco Urondo Cultural Center, 2016), Cenote Reflections (the page has no venue line in the meta column), Visionoros Collective.
- **Language versions:** ES and FR versions of each work page (work pages are English only for now).
- **Spanish and French text is a draft** for Mario to correct (interface text, section names, role line, opening statement, section leads, About bio). The Sophia and Desdemona blurbs and the row descriptions (venues, credits) are kept in English on purpose.

## Problems found in the old pages (decide, then I fix)

- `cenotes.html` carried the Exhibitions and Press of Quetzalcóatl-bot; they were removed. Its only exhibition now is the AI Robot Roadshow. Supply any other exhibitions or press for Cenote Reflections.
- `lastagreement.html` and `prepixel.html` have only one image each (low resolution, 765 px). Better photos would help.
- `aerodynamics-seeds.html`: the page uses only the seed image. The Works row links to the project site.
- `learningtowrite.html`: the exhibitions list uses your wording ("Game On! The Art in Videogames", ACUD MACHT NEU). Old press link kept.
- Videos from the old pages: Vimeo links open in the overlay player (lead image or "Watch" link). YouTube videos on three pages are lazy embeds.
- Alt texts on work-page photos are short and generic. Please refine.
- ONA page: text and credits are from pleek.net as given, with the venue written as you asked. The spelling "Lights sinchronization" there was changed to your credit line.

- `conciencia.html`: the Press line was a placeholder ("ACA poner lo de HOLO magazine") and is left out. Supply real press if there is any.
- Memory of Everywhere: the page uses the text of the old `lstm/index.html`. The Linne Magazine article you named does not mention the piece or you, so the page links it without saying anything about it. Check it is the right link.
- Legible Journey and Mirar al cielo have no year yet.
- `legible-journey.html`: Mario to write a paragraph about his own contribution.
- `mirar-al-cielo.html`: Mario to write a paragraph about his own contribution.
- Spanish and French text lives in `tools/build_home.py` (dictionary `L`, keys "es" and "fr"), and in the generated `es/index.html` and `fr/index.html`. Edit `build_home.py` and run `python tools/build_home.py`, or edit the two HTML files directly.

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
