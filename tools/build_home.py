#!/usr/bin/env python3
"""Writes index.html, es/index.html and fr/index.html (the three homepages).
Run:  python tools/build_home.py
ES and FR text is a draft for Mario to correct (see designs/TODO-CONTENT.md, which is not published)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_common import *  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = "images/web/"
NB = "&nbsp;"

# ---- text that changes with the language -------------------------------
L = {
    "en": dict(
        title="Mario Guzman · Artist-researcher and creative technologist",
        desc="Mario Guzman, artist-researcher and creative technologist. Installations, robots and texts on artificial voice and social robots. Former operator and writer for the humanoid robot Sophia.",
        nav=["works", "robots", "creative technologist", "workshops", "texts", "about"],
        role="Artist-researcher and<br>creative technologist",
        say='I make installations, robots, texts and open tools about artificial entities: <span class="ask" role="button" tabindex="0" title="click">who is speaking when a machine speaks?</span>',
        say_plain="I make installations, robots, texts and open tools about artificial entities: who is speaking when a machine speaks?",
        words=["Works", "Humanoid robots", "Creative tech", "Workshops", "Texts"],
        h2=["Works", "Humanoid robots", "Creative technologist", "Workshops", "Texts", "About"],
        also="Also",
        robots_lead="Interaction design for the humanoid robots Sophia and Desdemona, 2018–2026, across Hanson Robotics and SingularityNET: what they said, how they moved, how they were shown. Also the empirical core of my PhD.",
        tech_lead="Commissioned work where I designed and built the technology.",
        texts_lead='PhD thesis in progress at La Rochelle Université: <i>Voicing Artificial Entities: Semiotics and Cultural Narratives in the Development of AI and Robot Persona and Personalities</i>.',
        about=[
            "Mario Guzman is a Mexican creative technologist and PhD candidate at La Rochelle Université, where he researches the semiotics of artificial voice and machine personas. For eight years (2018–2026) he operated the Sophia and Desdemona robots across Hanson Robotics and SingularityNET, writing dialogue, programming gesture, and staging live demonstrations.",
            "He is a mentor at the <a href=\"https://www.schoolofma.org/people/mario-guzman\">School of Machines, Making &amp; Make-Believe</a> in Berlin, co-founded the Imagined Tech Studies collective, and is the Spanish i18n Steward for the Processing Foundation's p5.js. His work has been shown at Festival ZERO1, BIENALSUR, and the Dakar Biennale.",
        ],
        avail='Available for talks, workshops and commissioned work. <a class="link" href="%s">Write to me</a>' % EMAIL,
        skip="Skip to content",
        rot_alt="Works",
    ),
    "es": dict(
        title="Mario Guzman · Artista-investigador y tecnólogo creativo",
        desc="Mario Guzman, artista-investigador y tecnólogo creativo. Instalaciones, robots y textos sobre la voz artificial y los robots sociales. Antiguo operador y escritor del robot humanoide Sophia.",
        nav=["obras", "robots", "tecnólogo creativo", "talleres", "textos", "acerca"],
        role="Artista-investigador y<br>tecnólogo creativo",
        say='Hago instalaciones, robots, textos y herramientas abiertas sobre entidades artificiales: <span class="ask" role="button" tabindex="0" title="click">¿quién habla cuando habla una máquina?</span>',
        say_plain="",
        words=["Obras", "Robots humanoides", "Tecnología creativa", "Talleres", "Textos"],
        h2=["Obras", "Robots humanoides", "Tecnólogo creativo", "Talleres", "Textos", "Acerca"],
        also="También",
        robots_lead="Diseño de interacción para los robots humanoides Sophia y Desdemona, 2018–2026, en Hanson Robotics y SingularityNET: qué decían, cómo se movían, cómo se mostraban. También es el núcleo empírico de mi doctorado.",
        tech_lead="Trabajo por encargo en el que diseñé y construí la tecnología.",
        texts_lead='Tesis doctoral en curso en La Rochelle Université: <i>Voicing Artificial Entities: Semiotics and Cultural Narratives in the Development of AI and Robot Persona and Personalities</i>.',
        about=[
            "Mario Guzman es un tecnólogo creativo mexicano y doctorando en La Rochelle Université, donde investiga la semiótica de la voz artificial y las personalidades de las máquinas. Durante ocho años (2018–2026) operó los robots Sophia y Desdemona en Hanson Robotics y SingularityNET, escribiendo diálogos, programando gestos y poniendo en escena demostraciones en vivo.",
            "Es mentor en la <a href=\"https://www.schoolofma.org/people/mario-guzman\">School of Machines, Making &amp; Make-Believe</a> de Berlín, cofundó el colectivo Imagined Tech Studies y es Spanish i18n Steward de p5.js, de la Processing Foundation. Su trabajo se ha mostrado en el Festival ZERO1, BIENALSUR y la Bienal de Dakar.",
        ],
        avail='Disponible para charlas, talleres y trabajos por encargo. <a class="link" href="%s">Escríbeme</a>' % EMAIL,
        skip="Saltar al contenido",
    ),
    "fr": dict(
        title="Mario Guzman · Artiste-chercheur et technologue créatif",
        desc="Mario Guzman, artiste-chercheur et technologue créatif. Installations, robots et textes sur la voix artificielle et les robots sociaux. Ancien opérateur et auteur du robot humanoïde Sophia.",
        nav=["œuvres", "robots", "technologue créatif", "ateliers", "textes", "à propos"],
        role="Artiste-chercheur et<br>technologue créatif",
        say='Je crée des installations, des robots, des textes et des outils ouverts autour des entités artificielles' + NB + ': <span class="ask" role="button" tabindex="0" title="click">qui parle quand une machine parle' + NB + '?</span>',
        say_plain="",
        words=["Œuvres", "Robots humanoïdes", "Tech créative", "Ateliers", "Textes"],
        h2=["Œuvres", "Robots humanoïdes", "Technologue créatif", "Ateliers", "Textes", "À propos"],
        also="Aussi",
        robots_lead="Design d'interaction pour les robots humanoïdes Sophia et Desdemona, 2018–2026, chez Hanson Robotics et SingularityNET" + NB + ": ce qu'ils disaient, comment ils bougeaient, comment ils étaient montrés. C'est aussi le cœur empirique de ma thèse.",
        tech_lead="Travaux de commande pour lesquels j'ai conçu et construit la technologie.",
        texts_lead='Thèse de doctorat en cours à La Rochelle Université' + NB + ': <i>Voicing Artificial Entities: Semiotics and Cultural Narratives in the Development of AI and Robot Persona and Personalities</i>.',
        about=[
            "Mario Guzman est un technologue créatif mexicain et doctorant à La Rochelle Université, où il étudie la sémiotique de la voix artificielle et des personas de machines. Pendant huit ans (2018–2026), il a opéré les robots Sophia et Desdemona au sein de Hanson Robotics et de SingularityNET, en écrivant des dialogues, en programmant des gestes et en mettant en scène des démonstrations en direct.",
            "Il est mentor à la <a href=\"https://www.schoolofma.org/people/mario-guzman\">School of Machines, Making &amp; Make-Believe</a> à Berlin, a cofondé le collectif Imagined Tech Studies et est Spanish i18n Steward pour p5.js de la Processing Foundation. Son travail a été présenté au Festival ZERO1, à BIENALSUR et à la Biennale de Dakar.",
        ],
        avail='Disponible pour des conférences, des ateliers et des commandes. <a class="link" href="%s">Écrivez-moi</a>' % EMAIL,
        skip="Aller au contenu",
    ),
}

PROJ = "project/"
# ---- works -------------------------------------------------------------
WORKS = [
    ("2026", "she-tells/lead", "She Tells, Sea Shells", "with Helin Ulaş and Rita Eperjesi", "S+T+ARTS Aqua Motion showcase, UNESCO Venice Office", PROJ + "she-tells-sea-shells.html", "DIY Shell Phone"),
    ("2024", "liminal/03", "Liminal Sanctuary", "with Agustín Ramos Anzorena", "XV Biennale of Contemporary African Art, Dakar", PROJ + "liminal_sanctuary.html", "Liminal Sanctuary"),
    ("2023", "golem/lead", "Entangled Matter: AI, Humans and Golems", "", "Festival ZERO1, La Rochelle<br>NeurIPS 2026 Creative AI Track", PROJ + "entangled_matter.html", "Entangled Matter: AI, Humans and Golems"),
    ("2021–25", "seeds/lead", "AI Seeds / Aerodynamics of Seeds", "", "BIENALSUR, Ecuador<br>FACTO 11, Brazil", "https://aerodynamics-of-seeds.netlify.app/", "A flying seed from the AI Seeds project"),
    ("2022", "conciencia/lead", "Consciousness Is the Precooking of the Universal Mind", "", "Latin American Artificial Intelligence Biennial, Mexico", PROJ + "conciencia.html", "Consciousness Is the Precooking of the Universal Mind"),
    ("2015", "quetzabot/lead", "Quetzalcóatl-bot. Between Code and Codex", "", "Installation and New Media Award, 105º Salón Nacional, Buenos Aires", PROJ + "quetzabot.html", "Quetzalcóatl-bot"),
]
ALSO = [
    ("2023", "cenote/lead", "Cenote Reflections", "AI Robot Roadshow, AI for Good Global Summit 2023, Geneva", PROJ + "cenotes.html"),
    ("2020", "nierika/lead", "Combinatory Nierika", "Taper #5 · POSVERSO 2026", PROJ + "combinatory_nierika.html"),
    ("2020", "memory/lead", "Memory of Everywhere", "ELO (Un)Continuity, Orlando", PROJ + "memory-of-everywhere.html"),
    ("2019", "learning/lead", "Learning to Write", "Game On!, Centro Cultural San Martín · Mixed Feelings, School of Machines", PROJ + "learningtowrite.html"),
    ("2018", "bitcelulle/lead", "Machine de transcodage bit-cellule", "ZERO1, La Rochelle", PROJ + "bitcelulle.html"),
    ("2016", "ped/lead", "Ped. Deneoclassified Electromagnetic Poem", "Centro Cultural Kirchner", PROJ + "ped.html"),
    ("2016", "lastagreement/lead", "The Last Agreement", "Casa del Bicentenario", PROJ + "lastagreement.html"),
    ("2015–16", "temazcalli/lead", "Temazcalli-Dome", "Planetario Galileo Galilei · BIENALSUR", PROJ + "temazcalli.html"),
    ("2015", "hiperstories/lead", "Discrete Infinity", "Itaú Digital Story Award anthology", PROJ + "hiperstories.html"),
    ("2014", "oraculo/lead", "Generative Oracle. From the Pulse to the Letter", "Youth Art Biennial", PROJ + "oraculo.html"),
    ("2014", "prepixel/lead", "Pre-pixel Symphony in Major Fractal I", "", PROJ + "prepixel.html"),
    ("2013–", "visionoros/lead", "Visionoros Collective", "VHS and electronic music performance", PROJ + "visionoros.html"),
]
SOPHIA1 = "https://www.youtube.com/watch?v=xuVYl2KzpHI"
SOPHIA2 = "https://www.youtube.com/watch?v=L0EFisbhwPs"
MUX1 = "https://stream.mux.com/17W8LSIuJnBj4wSLKmiDPXee7xBvjlY4g59h02mU801mg.m3u8"
MUX2 = "https://stream.mux.com/G00vzb7lA7Fo01MA00DHaJeG5novzvzWHeztJ6SKDRlB4A.m3u8"
DESD = "Hypersensual Overclocking: Making Machines Feel"
MELLY = "https://www.kunstinstituutmelly.nl/en/programs/10471-clip-open-session-1-lecture-with-mario-guzman-who-am"
HACK = "https://www.youtube.com/watch?v=8722fTuH_fo"
SOMURL = "https://www.schoolofma.org/algorithmic-poetry"
AMAZE = "https://amazeberlin2023.sched.com/event/1LADM/what-are-robots-talking-about-behind-your-back-an-experimental-chatbot-writing-workshop"
ALGOPO = "https://imaginedtech.neocities.org/algopo_ficro"
KANAPE = "https://www.kanape.studio/events/robot-voice-beyond-language-workshop-2025-04-05"


def build(lang):
    t = L[lang]
    root = "" if lang == "en" else "../"
    pre = lambda p: p if p.startswith("http") else root + p  # noqa
    sec = t["h2"]
    out = []
    # hreflang
    alt = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">\n'
        for l, p in (("en", ""), ("es", "es/"), ("fr", "fr/"))
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE}">\n'
    canonical = {"en": "", "es": "es/", "fr": "fr/"}[lang]
    out.append(head(lang, t["title"], t["desc"], W + "liminal/lead.jpg", canonical, root, alt + person_ld()))
    hrefs = {"en": "index.html", "es": "index.html", "fr": "index.html"}
    lang_links = []
    for l in ("en", "es", "fr"):
        target = {"en": root + "index.html" if lang != "en" else "index.html",
                  "es": "es/index.html" if lang == "en" else ("index.html" if lang == "es" else "../es/index.html"),
                  "fr": "fr/index.html" if lang == "en" else ("../fr/index.html" if lang == "es" else "index.html")}[l]
        cur = ' class="on" aria-current="page"' if l == lang else ""
        lang_links.append(f'<a href="{target}" hreflang="{l}" lang="{l}"{cur}>{l}</a>')
    nav = t["nav"]
    out.append(f"""<body class="home" data-root="{root}">
<a class="skip" href="#works">{t['skip']}</a>
<header>
  <div class="wrap">
    <nav aria-label="Main">
    <a class="me" href="#top">mario guzman</a>
    <a href="#works">{nav[0]}</a>
    <a href="#robots">{nav[1]}</a>
    <a href="#tech">{nav[2]}</a>
    <a href="#workshops">{nav[3]}</a>
    <a href="#texts">{nav[4]}</a>
    <a href="#about">{nav[5]}</a>
    </nav>
    <span id="lang">{' '.join(lang_links)}</span>
  </div>
</header>

<main id="top" class="wrap">

  <div class="hero">
    <h1 id="me">Mario Guzman</h1>
    <div class="say">
      <p class="sm"><span id="role">{t['role']}</span><br><span class="soft">Berlin / La Rochelle</span></p>
      <p class="big" id="say">{t['say']}</p>
    </div>
    <a class="pic" id="rot" href="{root}project/liminal_sanctuary.html"><img id="rotA" alt="Liminal Sanctuary, 2024" width="1800" height="1012"><img id="rotB" class="off" alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" width="1800" height="1012"><noscript><img src="{root}{W}liminal/lead.jpg" alt="Liminal Sanctuary, 2024" width="1800" height="1012"></noscript></a>
    <div class="cap sm"><span id="rotT">Liminal Sanctuary, 2024</span><span class="soft" id="rotV">XV Biennale of Contemporary African Art, Dakar</span></div>
  </div>
""")

    def cell(img, name, href, extra_cls="", alt=None, contain=False, lazy=True):
        a = esc(alt if alt is not None else name)
        ic = ' class="contain"' if contain else ""
        ex = f' target="_blank" rel="noopener"' if href.startswith("http") and "youtube" not in href and "mux" not in href else ""
        return (f'<a class="c{extra_cls}" data-n="{esc(name)}" href="{pre(href)}"{ex}>'
                f'<img src="{root}{img}" alt="{a}"{ic} loading="lazy" decoding="async"></a>')

    def txt(label, href):
        ex = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return f'<a class="c txt" href="{pre(href)}"{ex}>{label}</a>'

    w = t["words"]
    ov = [
        (w[0], "#works", [
            cell(W + "golem/lead-thumb.jpg", "Entangled Matter: AI, Humans and Golems", PROJ + "entangled_matter.html", alt="Entangled Matter: a golem wandering in its virtual world", lazy=False),
            cell(W + "conciencia/lead-thumb.jpg", "Consciousness Is the Precooking of the Universal Mind", PROJ + "conciencia.html"),
            cell(W + "liminal/lead-thumb.jpg", "Liminal Sanctuary", PROJ + "liminal_sanctuary.html"),
        ]),
        (w[1], "#robots", [
            cell(W + "robots/sophia-awakening-thumb.jpg", "Sophia. Stream of Consciousness: Awakening", SOPHIA1, alt="Sophia the Robot: close-up of an eye"),
            cell(W + "robots/sophia-nature-thumb.jpg", "Sophia. A Stream of Consciousness About Nature", SOPHIA2, alt="Sophia the Robot: profile of the head with its transparent skull"),
            cell(W + "robots/desdemona-robot-thumb.jpg", DESD, MUX1, alt="Desdemona, a robot wearing a green mask"),
        ]),
        (w[2], "#tech", [
            cell(W + "she-tells/with-shell-thumb.jpg", "DIY Shell Phone toolkit", PROJ + "she-tells-sea-shells.html", alt="The DIY Shell Phone board next to a shell"),
            cell(W + "robots/legible-thumb.jpg", "Legible Journey", PROJ + "legible-journey.html", alt="Legible Journey: a visitor pedals a bicycle on a platform among 3D-printed letters"),
            cell(W + "mirar/center-thumb.jpg", "Mirar al cielo", PROJ + "mirar-al-cielo.html", alt="Mirar al cielo: skies with generated words"),
        ]),
        (w[3], "#workshops", [
            cell(W + "workshops/melly-thumb.jpg", "Who Am I Really Talking To? We All Know your chatbot is slowly changing you", MELLY, alt="Poster of the CLiP Open Session with Mario Guzman at Kunstinstituut Melly", contain=True),
            cell(W + "workshops/hackathon-thumb.jpg", "Making Machines Feel", HACK, alt="Making Machines Feel: hands attach electronics to a person's head"),
            cell(W + "workshops/som-thumb.jpg", "Algorithmic Poetry: Speculative Imagination, Machine Learning, and Code Studies", SOMURL, alt="School of Machines, Algorithmic Poetry: two vintage computers shaking hands"),
        ]),
        (w[4], "#texts", [
            txt("Voicing Artificial Entities", "#texts"),
            txt("Robot Memories Imagined from e-Waste", "#texts"),
            txt("Demo Culture", "https://onhumantrace.hypotheses.org/10634"),
        ]),
    ]
    out.append('  <nav class="over" aria-label="Overview">')
    for word, anchor, cells in ov:
        out.append(f'    <div class="r"><a class="w" href="{anchor}">{word}</a>{"".join(cells)}</div>')
    out.append("  </nav>\n")

    # works
    out.append(f'  <section id="works">\n    <h2>{sec[0]}</h2>\n    <div class="rows">')
    for yr, img, title, withs, venue, href, alt in WORKS:
        sub = f'<br><span class="sm soft" style="letter-spacing:0">{withs}</span>' if withs else ""
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        out.append(f'      <a class="row work" href="{pre(href)}"{ext}><span>{yr}</span><span class="th"><img src="{root}{W}{img}-thumb.jpg" alt="{esc(alt)}" loading="lazy" decoding="async"></span><span class="t">{esc(title)}{sub}</span><span class="sm">{venue}</span></a>')
    out.append(f'    </div>\n\n    <p class="earlier soft" id="also">{t["also"]}</p>\n    <div class="rows small">')
    for yr, img, title, venue, href in ALSO:
        tag = "a" if href else "div"
        h = f' href="{pre(href)}"' if href else ""
        out.append(f'      <{tag} class="row work"{h}><span>{yr}</span><span class="th"><img src="{root}{W}{img}-thumb.jpg" alt="{esc(title)}" loading="lazy" decoding="async"></span><span class="t">{esc(title)}</span><span class="sm soft">{venue}</span></{tag}>')
    out.append("    </div>\n  </section>\n")

    # robots
    out.append(f"""  <section id="robots">
    <h2>{sec[1]}</h2>
    <p class="lead">{t['robots_lead']}</p>
    <div class="bots">
      <div>
        <div class="vids">
          <a class="vid" href="{SOPHIA1}"><img src="{root}{W}robots/sophia-awakening.jpg" alt="Sophia the Robot: Stream of Consciousness: Awakening. Close-up of an eye." loading="lazy" decoding="async"></a>
          <a class="vid" href="{SOPHIA2}"><img src="{root}{W}robots/sophia-nature.jpg" alt="Sophia the Robot: A Stream of Consciousness About Nature. Profile of the head with its transparent skull." loading="lazy" decoding="async"></a>
        </div>
        <h3>Sophia</h3>
        <p class="sm">Hanson Robotics, Hong Kong, 2018–2022. Main operator. I developed her speeches and performances and did the art direction for many of her presentations.<br><span class="soft">Videos: Stream of Consciousness: Awakening · A Stream of Consciousness About Nature.</span></p>
      </div>
      <div>
        <div class="vids">
          <a class="vid" href="{MUX1}"><img src="{root}{W}robots/desdemona-robot.jpg" alt="{DESD}. Desdemona, a robot wearing a green mask." loading="lazy" decoding="async"></a>
          <a class="vid" href="{MUX2}" title="Desdemona at the Vatican"><img src="{root}{W}robots/desdemona-phone.jpg" alt="Desdemona at the Vatican, seen through a phone camera" loading="lazy" decoding="async"></a>
        </div>
        <h3>Desdemona</h3>
        <p class="sm">SingularityNET, 2021–2026. Dialogue writing and live operation.<br><span class="soft">Videos: {DESD} · Desdemona at the Vatican.</span></p>
      </div>
    </div>
  </section>
""")

    # creative technologist
    out.append(f"""  <section id="tech">
    <h2>{sec[2]}</h2>
    <p class="lead">{t['tech_lead']}</p>
    <div class="kit">
      <a data-n="DIY Shell Phone toolkit" href="{root}{PROJ}she-tells-sea-shells.html"><img src="{root}{W}she-tells/with-shell-thumb.jpg" alt="The DIY Shell Phone board next to a shell" loading="lazy" decoding="async"></a>
      <a data-n="Legible Journey" href="{root}{PROJ}legible-journey.html"><img src="{root}{W}robots/legible-thumb.jpg" alt="Legible Journey: a visitor pedals a bicycle on a platform among 3D-printed letters" loading="lazy" decoding="async"></a>
      <a data-n="Mirar al cielo" href="{root}{PROJ}mirar-al-cielo.html"><img src="{root}{W}mirar/center-thumb.jpg" alt="Mirar al cielo / 52 tonos de azul: skies with generated words" loading="lazy" decoding="async"></a>
      <a data-n="ONA" href="{root}{PROJ}ona.html"><img src="{root}{W}ona/lead-thumb.jpg" alt="ONA, light installation, Venice 2017" loading="lazy" decoding="async"></a>
    </div>
    <div class="rows">
      <div class="row four"><span class="t2 t"><a href="https://shetells.stream/toolkit/build/">DIY Shell Phone toolkit</a> <a class="link sm" href="https://github.com/marioguzzzman/diy-shell.phone">Code</a></span><span class="sm">with Helin Ulaş, Rita Eperjesi and Christian Kokott. S+T+ARTS Aqua Motion, Esposende</span><span class="sm soft">Custom audio board for a Raspberry Pi Zero, bone-conduction speaker, shell enclosure</span></div>
      <div class="row four"><span class="t2 t"><a href="{root}{PROJ}legible-journey.html">Legible Journey</a></span><span class="sm">by Colectivo Línea 60. Festival ZERO1, La Rochelle, and Espace Mendès France</span><span class="sm soft">Device concept, microcontroller system and programming. <a class="link" href="https://vimeo.com/1064248159/bf6588966a">Video</a></span></div>
      <div class="row four"><span class="t2 t"><a href="https://www.yayalabs.io/">Robot personalities and interaction devices</a></span><span class="sm">YayaLabs, London</span><span class="sm soft">Personality development, device design, voice research</span></div>
      <div class="row four"><span class="t2 t"><a href="{root}{PROJ}mirar-al-cielo.html">Mirar al cielo / 52 tonos de azul</a></span><span class="sm">by Gabriela Golder. Fundación Andreani, BIENALSUR 2021, Videoformes 2022</span><span class="sm soft">Neural network implementation</span></div>
      <div class="row four"><span class="t2 t"><a href="{root}{PROJ}ona.html">ONA</a></span><span class="sm">by Joaquín Gómez and Tomás Terzano. Open Borders, Palazzo Mora, European Cultural Centre, Venice</span><span class="sm soft">Light synchronisation and programming, with Agustín Ramos Anzorena</span></div>
    </div>
  </section>
""")

    # workshops
    def wrow(title, href, where, note=""):
        return (f'      <div class="row four"><span class="t2 t"><a href="{href}">{title}</a></span>'
                f'<span class="sm">{where}</span><span class="sm soft">{note}</span></div>')
    out.append(f"""  <section id="workshops">
    <h2>{sec[3]}</h2>
    <div class="kit k3">
      <a class="kc" data-n="Who Am I Really Talking To? We All Know your chatbot is slowly changing you" href="{MELLY}"><img class="contain" src="{root}{W}workshops/melly-thumb.jpg" alt="Poster of the CLiP Open Session with Mario Guzman at Kunstinstituut Melly" loading="lazy" decoding="async"></a>
      <a class="kc" data-n="Making Machines Feel" href="{HACK}"><img src="{root}{W}workshops/hackathon-thumb.jpg" alt="Making Machines Feel: hands attach electronics to a person's head" loading="lazy" decoding="async"></a>
      <a class="kc" data-n="Algorithmic Poetry: Speculative Imagination, Machine Learning, and Code Studies" href="{SOMURL}"><img src="{root}{W}workshops/som-thumb.jpg" alt="School of Machines, Algorithmic Poetry: two vintage computers shaking hands" loading="lazy" decoding="async"></a>
    </div>
    <div class="rows">""")
    out += [
        wrow("Who Am I Really Talking To? We All Know your chatbot is slowly changing you", MELLY, "CLiP Open Session, Kunstinstituut Melly, Rotterdam", "Lecture, and workshop: Building Chatbots with p5.js + RiveScript"),
        wrow("Robot Voice Beyond Language", KANAPE, "with Kit Kuksenok, Imagined Tech Studies. Kanapé", "Participants build a web-based soundboard and perform with robot voices beyond human language."),
        wrow("Making Machines Feel", HACK, "Yaya Labs &amp; Umanesimo Artificiale Hackathon"),
        wrow("What are robots talking about behind your back? An experimental chatbot writing workshop", AMAZE, "A MAZE. / Berlin 2023", "with Rita Eperjesi"),
        wrow("Algorithmic Poetry: Speculative Imagination, Machine Learning, and Code Studies", SOMURL, "School of Machines, Making &amp; Make-Believe"),
        wrow("Algorithmic Poetry of Fictional Robotics", ALGOPO, "Imagined Tech Studies"),
    ]
    out.append("    </div>\n  </section>\n")

    # texts
    def trow(yr, title, venue, href=None):
        ti = f'<a href="{href}">{title}</a>' if href else title
        cls = "t2 t" if href else "t2"
        return f'      <div class="row three"><span>{yr}</span><span class="{cls}">{ti}</span><span class="sm">{venue}</span></div>'
    out.append(f'  <section id="texts">\n    <h2>{sec[4]}</h2>\n    <p class="lead">{t["texts_lead"]}</p>\n    <div class="rows">')
    out += [
        trow("2027", "Reconstitution: Robot Memories Imagined from e-Waste", "Chapter with Kit Kuksenok. Routledge, forthcoming"),
        trow("2026", "Demo Culture, Artificial Voice, and the Staging of Artificial Presence", "Talk. InterGestes research group, On Human Trace", "https://onhumantrace.hypotheses.org/10634"),
        trow("2025", "Who Am I Really Talking To? Chatbots and Creative Computation", "Lecture and research presentation (<i>Voicing Artificial Entities</i>). Open Drafts colloquium, HfG Karlsruhe", "https://opendrafts.netlify.app/"),
        trow("2022", "How to code human bodies for devouring and mutual enlightenment", "Critical Coding Cookbook", "https://criticalcode.recipes/contributions/how-to-code-human-bodies-for-devouring-and-mutual-enlightenment"),
        trow("2020", "Interfaces and modes of writing at the intersection between digital literature and electronic arts", "INNOVA UNTREF", "https://revistas.untref.edu.ar/index.php/innova/article/view/612"),
        trow("2019", "Writing as interface: Robotics, pre-Hispanic mythology and creative code", "¡Cuerpo, Máquina, Acción!", "http://sedici.unlp.edu.ar/handle/10915/148725"),
    ]
    out.append("    </div>\n  </section>\n")

    # about
    out.append(f"""  <section id="about">
    <h2>{sec[5]}</h2>
    <div class="about">
      <div class="p"><img src="{root}{W}global/mario-guzman-2026.jpg" alt="Mario Guzman" loading="lazy" decoding="async"></div>
      <div>
        <p>{t['about'][0]}</p>
        <p>{t['about'][1]}</p>
      </div>
    </div>
    <p class="avail">{t['avail']}</p>
    {contact_row()}
  </section>

</main>
<script src="{root}js/site.js"></script>
</body>
</html>
""")
    return "\n".join(out)


def main():
    for lang, path in (("en", "index.html"), ("es", "es/index.html"), ("fr", "fr/index.html")):
        p = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(build(lang))
        print("wrote", path)


if __name__ == "__main__":
    main()
