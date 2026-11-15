"""Content of the work pages. Text is Mario's, copied word for word from the old
pages (checked by build_work.py --verify against the snapshot commit).
Lists of exhibitions / press / credits come from work_lists.json, extracted from
the old pages, unless a page overrides them here.

Block types, in page order after the intro:
  ("t", heading, [paragraphs])        text under a subheading
  ("i", [images])                     grid of images; image = name or (name, alt, caption)
  ("v", url, label)                   text link that opens a video in the overlay
  ("yt", id)                          lazy youtube-nocookie embed
"""

# slug, file, title, year, venue (lines), people line, project folder in images/web
PAGES = []


def page(**kw):
    PAGES.append(kw)


page(
    slug="she-tells-sea-shells", folder="she-tells", title="She Tells, Sea Shells", year="2026",
    venue=["S+T+ARTS Aqua Motion showcase, UNESCO Venice Office"],
    people="with Helin Ulaş, Rita Eperjesi and Christian Kokott",
    lead_alt="She Tells, Sea Shells: a hand holds a shell above a glass sphere on a beach",
    intro=[
        "Sea Shells, She Tells, is an artistic research project in Esposende. It begins with the simple, almost childlike gesture of holding a shell to the ear and hearing the ocean. Through field recordings, performed voices, local stories and speculative futures, we extend a playful voice to the waters of Esposende, and invite the people who live alongside them to answer.",
    ],
    intro_html=['<a href="https://shetells.stream/">Sea Shells, She Tells</a>, is an artistic research project in Esposende. It begins with the simple, almost childlike gesture of holding a shell to the ear and hearing the ocean. Through field recordings, performed voices, local stories and speculative futures, we extend a playful voice to the waters of Esposende, and invite the people who live alongside them to answer.'],
    intro_link=("Visit the main project site: shetells.stream", "https://shetells.stream"),
    kind="", tech="",
    blocks=[
        ("t", "The Shellphone", [
            "The Shellphone is a shell you can listen to. Inside a shell sits a Raspberry Pi Zero W (or Zero 2 W) and a small custom audio board. When you hold the shell to your ear, it connects over WiFi to shetells.stream and plays its live stream - a flow of voices and memories that people have shared about water: the sea, rivers, drought, the things we are losing. It turns a familiar gesture - listening to a shell - into a way of listening to each other, and to the water.",
        ]),
        ("i", [
            ("kit-board-and-shell", "The snail-shaped audio board on a Raspberry Pi, next to a shell", ""),
            ("with-shell", "The DIY Shell Phone board next to a shell", ""),
            ("board-in-box", "The snail-shaped audio board in a box of green paper", ""),
        ]),
        ("t", "How it works", [
            "The Shellphone is three parts, hidden inside a shell:",
            "Raspberry Pi Zero W or Zero 2 W - a tiny WiFi computer. It connects to the internet and plays the live stream from shetells.stream.",
            "Custom audio board - a small PCB that plugs onto the Pi like a \"HAT\". It carries a MAX98357A I2S amplifier that turns the Pi's digital audio into a real signal, plus two LED \"antennas\" that light up whenever the Shellphone has power. The board is shaped like a snail.",
            "Bone-conduction transducer (8 Ω, 1 W) - instead of a normal speaker, a small transducer that makes whatever it touches vibrate. Glued inside the shell, it turns the shell itself into the speaker, so the sound seems to rise out of the shell in your hand.",
        ]),
        ("i", [
            ("transducer", "A bone-conduction transducer glued inside a shell", ""),
            ("complete", "The complete kit with its power supply", ""),
            ("pcb-front", "The audio board, front", ""),
        ]),
    ],
    links=[("shetells.stream", "https://shetells.stream/"), ("The DIY toolkit", "https://shetells.stream/toolkit/build/"),
           ("DIY Shell Phone on GitHub", "https://github.com/marioguzzzman/diy-shell.phone")],
    credits=[("Made by", "Helin Ulaş, Rita Eperjesi, Mario Guzman, Christian Kokott"),
             ("Funding and host", "Co-funded by the European Union within the S+T+ARTS Aqua Motion residency, hosted by Rio Neiva, Esposende.")],
    exhibitions=[], press=[], source="https://shetells.stream",
)

page(
    slug="liminal_sanctuary", folder="liminal", title="Liminal Sanctuary", year="2024",
    venue=["XV Biennale of Contemporary African Art, Dakar"], people="with Agustín Ramos Anzorena",
    lead_alt="Liminal Sanctuary: installation view",
    intro=[
        "Through symbolic elements such as Ghana-must-go bags and electronic candles animated with official migration data, Liminal Sanctuary builds an immersive space to safeguard oral memories that explore the notion of home and identity in the dynamics of the new contemporary micro-diasporas.",
        "Where does \"Home\" begin, and where does it end? How do the new displacements shaped by complex interconnectivity affect our notion of identity? How do we inhabit the in-between of unstable spaces? What does it mean to navigate the liminality between physical and virtual worlds, between the past and the future, and between the self and the other?",
        "The project includes a collection of stories from individuals who have navigated the challenges and emotions of displacement, building a collective emotional landscape that resonates with diverse audiences. The focus is on the emotional nuances of displacement journeys and how people cope with the sense of being \"in-between.\"",
    ],
    kind="", tech="",
    blocks=[
        ("t", "The Complexity of Displacement", [
            "In today's interconnected world, the experience of displacement extends beyond traditional geographical boundaries. The project explores how our digital connections, virtual identities, and emotional ties create new forms of belonging and displacement that coexist with physical migration.",
            "Liminal Sanctuary acknowledges that many individuals now navigate multiple forms of \"home\" simultaneously – the physical spaces they inhabit, the digital communities they belong to, and the emotional connections they maintain across distances. This complex layering of identity and belonging creates a new form of \"liminal\" existence – a state of being in-between, neither fully here nor there.",
        ]),
        ("i", ["01", "02", "03"]),
        ("t", "Emotional Landscape", [
            "The concept of an \"emotional landscape\" is central to Liminal Sanctuary. Rather than focusing solely on geographical or physical displacement, the project maps the emotional terrain that migrants, refugees, digital nomads, and other displaced individuals navigate.",
            "Our future homelands may also become an \"unreachable\" concept that will exist only in the realm of emotional landscapes, sustained by memory and nostalgia but inaccessible in physical reality. Governments, tech companies, and grassroots organizations, will shape these future diasporas alongside non-humans, machines and AI agents who will be maintaining cultural archives, facilitating virtual gatherings, or even participating as sentient entities in diasporic communities.",
            "Through the collected audio stories, visitors gain insight into how individuals create meaning and build identity in the midst of displacement, and how they develop resilience and new forms of belonging in unfamiliar contexts.",
        ]),
    ],
)

page(
    slug="entangled_matter", folder="golem", title="Entangled Matter: AI, Humans and Golems", year="2023",
    venue=["Festival ZERO1, La Rochelle", "NeurIPS 2026 Creative AI Track"], people="",
    lead_alt="Entangled Matter: a golem wandering in its virtual world",
    intro=[
        "Entangled Matter: AI, Humans and Golems begin with a desire to shift the focus from a racing technological anthropocentric pattern in which humans control and design creatures to a speculative place where we explore inspiration and cooperation between humans, virtual agents and AI within a feedback loop creation process.",
        "As prompts quickly become the primary interface for interacting with AI models. The piece attempts to create a reflexive digital analog workflow about prompt interpretation. Entangled Matter: AI, Humans and Golems is, therefore, an installation in which analog-manual sculpting and virtual worlds become part of a ritualistic feedback loop where Artificial Intelligence, Human Artistic interpretation, and the rudimentary but evolving speech of Virtual Golem-Agents become entangled.",
        "The piece is also a Workshop/installation in which analog-manual sculpting and virtual worlds become part of a ritualistic feedback loop where Artificial Intelligence, Human Artistic interpretation, and the rudimentary but evolving speech of Virtual Golem-Agents become entangled. This piece attempts to create a reflexive digital analog workflow about prompt interpretation.",
    ],
    kind="", tech="",
    blocks=[
        ("yt", "twu34-mAA3s", "Entangled Matter: AI, Humans and Golems, video"),
        ("t", "Golem as technological symbol", [
            "In Jewish folklore, a golem is a creature arisen from inanimate matter (usually clay or mud) and brought to life by ritual incantations and sequences of Hebrew letters. The Golem, brought into being by a human creator, first becomes a helper, a companion, or a rescuer but later runs amok and becomes a threat to its creator.",
            "We take the figure of the Golem as a metaphor for the current state of technology in the field of AI, in which a word or a text can bring an element to “life”. But contrary to the Jewish folklore story, our Golems can not be controlled; they begin as an AI creation living in a simulated space where they themselves post questions about their existence and create texts for us to be inspired and create more Golems, which in turn will be inserted in the simulation.",
        ]),
        ("i", [("sitting", "A clay golem sculpture", "Photo by Hugo Lafitte"), ("closeup", "Close-up of a clay golem sculpture", "")]),
        ("t", "Perceiving and acting", [
            "Generative language and generative sound are used to subvert the Golem's traditional narrative in which human written text and symbols control matter, often leading to the obliteration of a fragile emergent subjectivity.",
            "What degree of autonomy creates a \"living\" being? How can we program matter? How can matter program us? Can Golems reclaim their voice? Is the capability of interpreting reality a sign of consciousness, of identity? What does 'interpretation' mean for different agents?",
            "In Entangled Matter: AI, Humans and Golems, control over text is not an overpowering force, and neither humans nor Golems are in total control of each other. Humans, machines, and matter are influenced and moved by their own different forms of interpreting information. Each agent imprints its identity and distinct voice into the process of interpreting \"otherness.\"",
        ]),
        ("i", [("screen1", "A golem in its virtual world, render", ""), ("screen3", "Purple golems in a virtual space, render", ""), ("je-suis", "A golem in its virtual world, render, with the text Suis-je un Golem ?", "")]),
        ("t", "Virtuality as a possible realm", [
            "In this piece, different technologies bridging both realms (AI 3D generation, 3D rendering, handmade sculpting, text-to-image models, photogrammetry, generative language and generative sound) are used to subvert the Golem's traditional narrative in which human written text and symbols control matter, often leading to the obliteration of a fragile emergent subjectivity.",
            "After being sculpted, the scanned Golems become animated inside a virtual world built in Unreal Engine. They will perform several activities guided by rudimentary Artificial Intelligence behaviors. One of the most important is to develop a basic generative language out of simplified grammar to produce words, phrases and, finally, prompts that will be used for students to create more Golems.",
        ]),
        ("t", "Process", [
            "To develop the piece, a small workshop was designed for art students in which we reflected on the implications of programming matter, post-humanism, body in the digital age, and the use of natural language as an interface for producing several media assets such as images and 3D render in the field of Artificial Intelligence.",
            "Following the analogy of the Golem and the reflections stated above, the students developed prompts to create 3D images (on the Dreamfields-3D generation model modified by Shengyu Meng) and gain inspiration to sculpt their own Golems with clay and other materials.",
            "Software’s conceptual structure: Prompt from students after reflecting on technology → image on a text-to-3D image AI model → sculpture inspired by image → scan of sculpture → sculpture into virtual world → Golem create a prompt in virtual world → humans create a sculpture based on Golem's prompt.",
        ]),
        ("i", [("people-working", "Workshop participants working on golem sculptures", ""), ("mini", "Small golem sculptures", "Photo by Hugo Lafitte")]),
    ],
)

page(
    slug="aerodynamics-seeds", folder="seeds", title="AI Seeds / Aerodynamics of Seeds", year="2021–25",
    venue=["BIENALSUR, Ecuador", "FACTO 11, Brazil"], people="AI Seed Collective",
    lead_alt="A flying seed from the AI Seeds project", lead_contain=True,
    intro=[
        "Aerodynamics of seeds is an exploration that seeks to disarticulate and weave new imaginaries about the intelligence and evolution of the plant species by applying diverse methods of speculation and radical imagination offered by the field of artificial intelligence.",
        "This project seeks to generate a critical approach to the current and future problems in the behavior of ecosystems and their biodiversity in the face of the current environmental polycrisis, embracing as starting point different possible expressions of plant intelligence.",
    ],
    kind="", tech="",
    detail=[("Artists", "AI Seed Collective (Mario Guzman, Gabriela Munguía, Erika Torres, Guadalupe Chavez Pardo, Angel Salazar)"),
            ("Technology", "GPT-2 with a corpus of poetic nature explorations, philosophical and critical environmental perspectives, StyleGAN2")],
    blocks=[
        ("t", "Seeds in the wind.", [
            "The mechanism of the anemochory, the propagation of seeds by wind, is a type of propagule dissemination of great importance for the reproduction of many plant species. It allows a wider territorial dispersal, increasing the chances of preservation of species and their genetic variability.",
            "However, what are the new challenges in terms of cooperation and co-evolution between plant species and the environment? What aerodynamic, morphological and phylogenetic survival strategies will plants and their seeds have to develop in the face of the global climate crisis? How can we rewrite our anthropocentric imaginaries using artificial models?",
        ]),
        ("t", "Plant Intelligence and the Polycrisis.", [
            "The project embraces different possible expressions of plant intelligence as a starting point to generate a critical approach to the current and future problems in the behavior of ecosystems and their biodiversity in the face of the current environmental polycrisis.",
            "Through GPT-2 trained on a corpus of poetic nature explorations and philosophical and critical environmental perspectives, alongside visual generation using StyleGAN2, the work constructs speculative scenarios where plant agency, wind, and machine imagination converge.",
        ]),
        ("t", "About the Collective", [
            "AIseeds Project is a transdisciplinary artistic collective born at the beginning of 2021 integrated by a group of artists of renowned national and international trajectory from Argentina, Mexico, Ecuador and Colombia based in Buenos Aires.",
            "In our practice we are interested in disarticulating and weaving new perspectives on the notions of intelligence and co-evolution of plants by applying diverse methods of speculative technologies and radical imagination offered by the field of artificial intelligence, digital fabrication techniques and transmedia art.",
        ]),
    ],
    links=[("Visit the project", "https://aerodynamics-of-seeds.netlify.app/"), ("@aiseedsproject on Instagram", "https://www.instagram.com/aiseedsproject/")],
    credits=[("Concept and Direction", "AI Seed Collective"), ("", "Mario Guzman"), ("", "Gabriela Munguía"), ("", "Erika Torres"), ("", "Guadalupe Chavez Pardo"), ("", "Angel Salazar")],
    exhibitions=[], press=[],
)

page(
    slug="conciencia", folder="conciencia", title="Consciousness Is the Precooking of the Universal Mind", year="2022",
    venue=["Latin American Artificial Intelligence Biennial, Mexico"], people="",
    lead_alt="Consciousness Is the Precooking of the Universal Mind: ceramic skull and electronics",
    intro=[
        "Consciousness is the precooking of the universal mind, explores Resonance Theory through the integration of experimental lutherie, ceramics, electronics and neural networks trained on texts by Jacobo Grinberg and the history of shamanism in Mexico. It addresses the perception of consciousness concerning the body, sound and voice in the field of AI.",
    ],
    kind="Interactive Installation Ancestral AI / Experimental Lutherie / Techno-Shamanism / Sound Sculpture", tech="",
    blocks=[
        ("yt", "ASrmGYQaXNI", "Consciousness Is the Precooking of the Universal Mind, video"),
        ("t", "Resonance Theory", [
            "The Resonance Theory (Hunt, 2011) proposes that synchronization, harmonization, vibrations, or simply resonance have an integral relationship with consciousness itself. At the same time, this theory suggests that its method can address one of the \"Hard problems\" of consciousness: how matter (e.g., the human brain) is capable of having subjective experience? How do micro-conscious entities combine into a higher-level macro-consciousness?",
        ]),
        ("i", ["01", "02"]),
        ("t", "The mind-body problem", [
            "The piece aims to create a potential sonic space for two entities to achieve resonance and intuitively explore the \"mind-body\" problem. A skull-ceramic acting as a simple subject proposes an experience. At the same time, a human/complex responds to this experience by modifying the resonance conditions while being surrounded by voices depicting shamanic interpretations of consciousness and alternate descriptions of the mind created by AI.",
        ]),
        ("t", "Materiality", [
            "The piece addresses the “mind-body” problem (Chalmers, 1996) by juxtaposing corporeal entities that are self-complete in their mutual perception. The skull-ceramic as a simple subject that proposes an experience, responds to the presence of the skull-human/complex subject, and enables a space for the synchronization of frequencies that in their texture open a mutual reflection.",
            "Consciousness is the precooking of the universal mind is a space for the synchronization of frequencies that, in their texture, open a mutual reflection on the complex connections between matter and consciousness.",
        ]),
        ("i", [("03", "Diagram of the piece: microcontrollers, copper capacitive sensors, capacitive ink sensors, ceramic skull, contrabass strings, wooden wheel, motor", "")], "half"),
    ],
    drop_press=True,
)

page(
    slug="quetzabot", folder="quetzabot", title="Quetzalcóatl-bot. Between Code and Codex", year="2015",
    venue=["Installation and New Media Award, 105º Salón Nacional, Buenos Aires"], people="",
    lead_alt="Quetzalcóatl-bot, a mechanical feathered serpent", video="https://vimeo.com/189782745",
    intro=[
        "Quetzalcóatl-bot is a representation of the Mesoamerican deity of light, knowledge, and art. Through robotics, mapping and computer vision, this mechanic feathered serpent becomes a contemporary storyteller of ancient myths. It's also a counter-writing platform to experiment with the coexistence of codex and creative coding.",
    ],
    kind="Interactive Robotic Installation", tech="Robotics, computer vision, code, real-time image capture, interaction, projection mapping, generative writing, acrylic, paper, Arduino, PIR, Infrared light. Robot 72 cm x 22 cm x 16 cm / Projection 1.90m x 1.90m.",
    blocks=[
        ("t", "Storytelling through body movement.", [
            "The piece conceptually uses the link between word and image, movement of human and non-human bodies, and the cultural information contained in the Borgia's Codex, to articulate another method of storytelling and writing -a counter-writing, actually. During this process, we observe a new kind of mythical writing dynamic evolving within the techno-mythical scenario of the work: the narration of a cosmogonic episode, the implementation of a projection and a motion capture system, and the gestural behavior of a robot linked to the activity of the public.",
        ]),
        ("i", ["01", "02"]),
        ("t", "The Myth.", [
            "In the myth, the luminous and sonorous murmur of the god Quetzalcóatl tears apart the darkness and the primordial silence while rising from the underworld after having stolen the sacred bones that contain a life-giving material. During its ascent, it blows inside a snail and produces a sound that acquires the spiral shape of its instrument, simultaneously generating the first cultural configuration of the sound and the first formal graphic representation of the word: the voluta. An element that formalizes the link between verbal expression and image.",
        ]),
        ("i", ["03"]),
        ("t", "Writing as destruction.", [
            "Quetzalcoatl-bot’s serpentine activity acts as a writing method dynamically motivated by the viewer's circulation around the technical-symbolic system of the work. This movement becomes a dialogue framework between life forms to display and exchange signs that potentially can transform space.",
            "Etymologically, writing imposes a form, forces linearity and produces a regime of (in)formation on objects and materials. However, in this work, the surface is not passive against the destructive gesture of writing and creates a counter-writing.",
        ]),
        ("t", "Counter-writing.", [
            "The work displays a kind writing that accentuates the resistance of matter and abandons the conservation of information in favor of a fading movement of signs. Counter-writing thus performs against the traditional and social function of the codex - safeguarding information and preserving a mythological narrative - to impose on it the logic of the eternal beginning, the blank page or the eternal vacuum.",
            "If writing as technology supposes a state of conservation and, therefore, a triumph over the wear of materials and the loss of memory, this work proposes the inverse movement and bets for distortion, fragmentation, and fading.",
        ]),
    ],
)

page(
    slug="cenotes", folder="cenote", title="Cenote Reflections: A Prehispanic Science Fiction Journey", year="2023",
    venue=[], people="",
    lead_alt="Cenote Reflections: the installation in a darkened room",
    intro=[
        "Cenote Reflections explores an abstract cenote ritualistic space formed by a reflective patterned circle on the floor and a cross-shaped center surrounded by five screens, an important number in the Wirarika's shaman culture looking for the \"gift of seeing.\" It aims to create a narrative space and establish a larger work's basis on the prehispanic science fiction genre.",
    ],
    kind="Immersive Installation", tech="3D Ceramic Printing. AI Development. Animation Development. Computer for Unreal, TouchDesigner, and AI models. Video and Photography.",
    blocks=[
        ("yt", "cOqBUO5MqPQ", "Cenote Reflections, video"),
        ("t", "Cenotes", [
            "In this piece, fictional futures, hyperrealistic natural CGI environments, and AI latent spaces explore the notion of Cenote, a surface connection to subterranean water bodies derived from the Mayan word \"tz'onot\" (meaning \"well\" or \"abyss\"). Cenotes were also considered the entrance to the underworld and where the gods would visit. They became sacred sites where offerings and rituals were performed to please the gods. A Cenote is a passage, a throat, to communicate with other dimensions.",
        ]),
        ("i", ["01", "02"]),
        ("t", "The Space", [
            "In this symbolic space, one screen displays a generative text created by a machine learning model trained on pre-Hispanic heritage materials and current transcripts from the UN Permanent Forum on Indigenous Issues. The text is constantly evolving to prevent cultural stagnation.",
            "The floor contains a pattern with capacitive sensors that allow visitors to interact with the installation's images, the generative sound design of cenote field recordings, and the narrative. The pattern breaks the screen's visual impact allowing for a non-hierarchical reading of the piece.",
        ]),
        ("i", ["03"]),
        ("t", "New ways of observing.", [
            "Our general representation of the future is often clouded by visions derived from European and North American perspectives on progress. Through this lens, Latin America has been consumed as a homogenous and exotic space, unable to develop its own perspectives on a future derived from its roots.",
        ]),
        ("t", "Bigger picture", [
            "This piece is part of a larger project on expanded prehispanic science fiction that opens up a dialogue with the knowledge, myths and issues of indigenous communities where ancestral knowledge is reactivated through contemporary generative exploration to envision possible alternative futures. A definition that is inclusive and able to process identities and otherness as an ontological and political creative issue.",
        ]),
    ],
    exhibitions=[
        ("AI Robot Roadshow. AI for Good Global Summit 2023, Geneva, Switzerland", "Participating visual artist. Event concept: Jovanka v. Wilsdorf and David Hanson.", "https://jovanka-von-wilsdorf.de/en/project/ai-robot-roadshow"),
        ("AI Robot Roadshow, video", "", "https://www.youtube.com/watch?v=b4Zz6L9RjVs"),
    ],
    drop_press=True,
)

page(
    slug="combinatory_nierika", folder="nierika", title="Combinatory Nierika", year="2020",
    venue=["Taper #5", "POSVERSO 2026"], people="",
    lead_alt="Combinatory Nierika",
    intro=[
        "Following Taper's: Pent Up invitation to reflect on the significance of the number 5, the term \"Nierika\" relates to the quincunx structure, a geometric pattern consisting of four points forming a square and a fifth at its center. For the Huichols or Wixáritari, an indigenous culture located deep in the mountains of Mexico, it also represents a device crafted by their goddess mother to create the universe: a rhomboid embroidered with her hairs and two crossed arrows provided by her sons.",
        "Nierika also means the \"gift-of-seeing,\" an ability that shamans develop after practicing self-sacrifice, austerity, pilgrimage, fasting, and several other forms of vision searches.",
        "One of the most important of these activities is the ritual travel to Wirikuta, where they recreate the search for the mythical deer that transformed its heart into a peyote, a cactus with psychoactive properties.",
        "To become a shaman or a healer, an individual must participate in at least five pilgrimages to Wirikuta.",
        "The work \"Combinatory Nierika\" reimagines, in Spanish and Wixárika, the multiple visions that the Wixáritari may encounter while performing their ritual pilgrimage from the coastlines of Nayarit to Wirikuta, the northern part of San Luis Potosí, where the ritual ends and the sun rises for the first time.",
        "The background color performs a metaphorical passage from the ocean to the desert, and from day to night. By pressing the Wirikuta button, you can experience the minimalistic virtual pilgrimage's time on the scale of 24 hours or 24 seconds.",
    ],
    kind="", tech="",
    blocks=[("i", [("01", "Combinatory Nierika, screenshot", ""), ("02", "Combinatory Nierika, screenshot", ""), ("03", "Combinatory Nierika, screenshot", "")])],
    links=[("Combinatory Nierika in Taper #5", "https://taper.badquar.to/5/combinatory_nierika.html")],
    exhibitions=[], press=[], credits=[],
)

page(
    slug="learningtowrite", folder="learning", title="Learning to write: a machine learning experiment", year="2019",
    venue=["Game On! The Art in Videogames, Centro Cultural San Martín, Buenos Aires", "Mixed Feelings, School of Machines, ACUD MACHT NEU, Berlin"], people="",
    lead_alt="Learning to write: output of the neural network over a video still", video="https://vimeo.com/390603479",
    intro=[
        "Learning to write: a machine learning experiment is a textual artificial organism that performs a reading and writing exercise using video input from around the globe and a generative language model trained on 19th-century travel literature. The work focus on the notion of travel, journey, discovery, and cognition.",
    ],
    kind="Machine Learning / Experimental Literature / Installation", tech="Machine Learning, convolutional neural network, mobile vision, long short-term memory (LSTM), projection, XIX century travel literature corpus, travel videos.",
    blocks=[
        ("t", "Experimenting with narrative.", [
            "The work arises from a need to organize a series of chaotic experiences while traveling to more than 39 countries and 1,532 flight hours with a social robot.",
            "To make sense of the speed and heterogeneity of these episodes, I've designed a writing system that articulates two structures: a convolutional neural network using mobile vision and a long short-term memory (LSTM) architecture of recurrent neural network (RNN).",
        ]),
        ("i", ["01"]),
        ("t", "Writing with Neural Networks", [
            "A convolutional neural network using mobile vision interprets a set of audiovisual micro-narratives that represent personal waiting times or moments in which I feel present.",
            "Then, the objects and situations recognized by the machine are sent to a long short-term memory (LSTM) recurrent neural network (RNN) that has been trained on 19th-century travel literature, the RNN model then narrates what is happening -or what it thinks is happening- in the image.",
            "The work is also an experiment around an endless writing action that tries to understand a world constituted by limited objects and perceptions, perhaps a reflection of our own cognitive operations.",
        ]),
        ("i", ["02"]),
    ],
    exhibitions=[("Game On! The Art in Videogames.", "Centro Cultural San Martín, Buenos Aires.", ""),
                 ("Mixed Feelings.", "School of Machines, ACUD MACHT NEU, Berlin.", "https://www.schoolofma.org/algorithmic-poetry")],
)

page(
    slug="bitcelulle", folder="bitcelulle", title="Machine de transcodage bit-cellule", year="2018",
    venue=["Festival des arts et cultures numériques ZERO1, Maison Henri II, La Rochelle"], people="Mario Guzman, Agustín Ramos Anzorena",
    lead_alt="Machine de transcodage bit-cellule: mapping projection on the facade of the House of Henri II", video="https://vimeo.com/267137199",
    intro=[
        "The Machine de transcodage bit-cellule, is an audioVisual exploration of computation substrate and its evolution into ever-digitally-mediated organic cells. From binary light and logic gates that undergo the complexity of discrete agent simulation, to ASCII-defined cellular forms. This piece placed at the House of Henri II as the inauguration mapping of the Electronic Art Festival ZERO1 at La Rochelle, France.",
    ],
    kind="Mapping / ASCII art / Inauguration", tech="",
    blocks=[("i", ["01"], "half")],
)

page(
    slug="ped", folder="ped", title="Ped. Deneoclassified Electromagnetic Poem", year="2016",
    venue=["Centro Cultural Kirchner"], people="Mario Guzman, Paula Guersenzvaig",
    lead_alt="Ped, installation with fluorescent tubes", video="https://vimeo.com/201333283",
    intro=[
        "PED is an experiment in discursive feedback, an exploration of sound space, and a way of revealing the invisible forces that animate words. It is the articulation of a text affected by the electromagnetic waves that emanate from -and inhabit- architectural spaces.",
    ],
    kind="Interactive/ Algorithmic Literature / Electromagnetic", tech="Arduino, Fluorescent tubes, 3D printing, plaster molds, natural language processing. / 40cm x 40cm x 100cm",
    blocks=[
        ("t", "Architecture and speech.", [
            "We search in the ruins, in the distant origins, and in the architectural structures as recipients of discourses. We start from the neo-classicist space to think how their own philosophical assumptions (logic, clarity, universal validity) and social goals (morality, education) extend the foundations for their own deconstruction.",
            "Over there, where the electromagnetic waves subsist, between our bodies and within them, in the space between what is not seen and what is imagined, lays the uncertain meaning of this poem.",
        ]),
        ("i", ["01"]),
        ("t", "Writing with electromagnetic fields", [
            "The sound poem declared appropriately by the computational interface of the installation is generated from the sensing, in real time, of electromagnetic waves that recombine neo-classical texts and philosophical texts found within the installation space.",
        ]),
        ("i", ["03", "04", ("cck", "Ped at Centro Cultural Kirchner", "")]),
        ("i", ["p2", "p3", "p4", "p5"]),
    ],
)

page(
    slug="lastagreement", folder="lastagreement", title="The Last Agreement", year="2016",
    venue=["Casa del Bicentenario"], people="",
    lead_alt="The Last Agreement: video and dance performance with VHS", video="https://vimeo.com/181278197",
    intro=[
        "It is a piece built with obsolete remains of dance, music and video. The last agreement, immerses us in a fiction around disagreements, consensus, attempts, trials, errors and possible agreements, probably the last one, between music, dance and analog technology.",
    ],
    kind="Concert Installation / Performance / VHS", tech="VHS, Projection, VHS feedback, Electronic music, TV installation array.",
    blocks=[
        ("t", "About the performance.", [
            "The project recycles audiovisual materials from its rehearsals. While designing an inherent relationship between discarded images, music, and dance, the piece becomes closer to an art installation than to a dance production. It researches about the obsolete as a physical and choreographic strategy against the constant demand for updating: that absurd fiction of the future.",
        ]),
    ],
    exhibitions=[("Fase 8. Art, Science and Technology Fair.", "Bicentennial National House, Buenos Aires, 2016.", "")],
)

page(
    slug="temazcalli", folder="temazcalli", title="Temazcalli-Dome", year="2015–16",
    venue=["Planetario Galileo Galilei", "BIENALSUR"], people="Mario Guzmán, Agustín Ramos Anzorena",
    lead_alt="Temazcalli-Dome: a shaman figure in the dome projection", video="https://vimeo.com/199064724",
    intro=[
        "The Temazcalli Dome project is an audiovisual experience that transports the audience through an intense journey from within the medical and ritual practice of the temazcal towards the constellation of the Pleiades showing intricate patterns that emulate the cosmic and mythological visions of the Huichol people.",
    ],
    kind="FullDome Projection Mapping", tech="Projection mapping, Prehispanic instruments, 8K & 4K visuals, Custom Software, Surround 5.1, 4.1, and stereo high-bitrate sound / Duration 5\"",
    blocks=[
        ("i", ["01", "02"]),
        ("t", "The Aesthetics of Temazcalli-Dome", [
            "Temazcalli-Dome is an immersive voyage through the Huichol spiritual experience that honors the hypnotic patterns of Huichol's art, uses shamanic voices in surround spatiality, and recreates ritualistic music actually built with traditional prehispanic instruments.",
        ]),
        ("i", ["03", "05", "06", "07"]),
        ("t", "Prehispanic Temazcalli", [
            "Temazcalli (from the nahuatl temazcalli: ‘house where you sweat’. temaz, ‘sweat’ and calli, ‘House’) is a steam bath used in traditional medicine and everyday life by the people of central Mexico.",
        ]),
        ("i", ["codex1", "codex2"]),
        ("t", "Huichol Art", [
            "The word, Huichol, derived from Wirrarika, is the original name of these indigenous people. It means soothsayer or medicine man. The medicine man is the shaman who links the community with the \"other world\" from where their creativity pours forth as a gift from their deified ancestors to be given back as offerings to the gods.",
        ]),
        ("i", ["jaguar"]),
        ("t", "Making of", [
            "This project was completed thanks to the University of Tres de Febrero, and the “Understanding Visual Music” International Conference, during a two-year residency at the Galileo Galilei Planetarium. In order to create an accurate portrait of the Huichol culture and the ritual experience of the temazcalli, we assisted to ceremonies, researched on the Museum of Anthropology and Natural History in Mexico City and collaborated with Tozomoni, a prehispanic instrument developer.",
        ]),
        ("i", ["making-of", "rochelle"]),
        ("v", "https://vimeo.com/296226291", "Watch the second video"),
    ],
)

page(
    slug="hiperstories", folder="hiperstories", title="Discrete Infinity", year="2015",
    venue=["Itaú Digital Story Award anthology"], people="",
    lead_alt="Discrete Infinity: a page of the non-linear interactive text", video="https://vimeo.com/103773697",
    intro=[
        "Discrete infinity is a non-linear interactive text, a database and an experimental narrative that can be modified by its readers/users to articulate new routes.",
        "At the same time, it gathers the words written in a database that serves as content to other interactive texts. The project, therefore, configures itself as a kind of dynamic hypertext that simultaneously transforms another set of texts.",
    ],
    kind="Digital Literature / Non-linear", tech="Digital Literature, Non-linear Narrative, Database, Internet.",
    detail_links=[("Read story", [("Discrete Infinity Spanish Ed.", "hiperstories/infinitud_discreta/INFINITUD%20DISCRETA.html"),
                                  ("Discrete Infinity Portuguese Ed.", "hiperstories/infinitud_discreta/INFINITUD%20DISCRETA%20PORTUGUESE.html")])],
    blocks=[
        ("t", "Nonlinear Education", [
            "These stories were built as an integral part of a National Digital Literacy program funded by the Argentinian Library of Congress inside the Bibliomovil project: a double-decker bus which included technological equipment and a nearly 5,000 book library.",
        ]),
        ("i", ["01", "02", "03"]),
        ("t", "Bermuda Triangle. A story about pixels, glitches and the forces of nature (2014)", [
            "This interactive story raises an analogy between the forces of nature and the codifications of body and speech in the digital age.",
            "Much has been theorized about the famous Bermuda Triangle and the mysterious disappearances that surround it, however little is known about the open coordinates within its perimeter. This story tells precisely these discoveries.",
            "Digital Literature / Non-linear Digital Literature, Non-linear Narrative, Database, Internet.",
        ]),
        ("links", "Read story", [("Bermuda Triangle. A story about pixels, glitches and the forces of nature Spanish Ed.", "hiperstories/triangulo/triangulo_de_las_bermudas.html")]),
        ("i", ["04"], "half"),
    ],
    exhibitions=[("Digital storytelling week.", "Salvador de Bahía, Brasil, 2018.", "https://www.antologiaitau2015.org/infinitud-discreta"),
                 ("Digital Story Award Anthology.", "Itaú Bank, 2015.", "https://www.antologiaitau2015.org/infinitud-discreta")],
)

page(
    slug="oraculo", folder="oraculo", title="Generative Oracle. From the Pulse to the Letter", year="2014",
    venue=["Youth Art Biennial"], people="",
    lead_alt="Generative Oracle: front of the writing interface", video="https://vimeo.com/117094826",
    intro=[
        "The Generative Oracle. from pulse to letter is a technical-symbolic interface that operates as an abstraction of oracular practices to produce enigmatic texts destined to behave as contemporary omens. The work is part of an experimental writing project that focuses on the cooperation between human and machine to experiment with writing (as a process and as a product) as well as a visualization-enunciation performance.",
    ],
    kind="Interactive / Algorithmic Literature / Writing Interface", tech="Microcontroller, generative software, acrylic, infrared sensors. 100 x 90 x 50 cm",
    blocks=[
        ("t", "Body and text becomes one.", [
            "In the Generative Oracle's writing there is no pure present, but a deferred sprouting. The reader accesses a time of waiting where his body participates in the emergence of the text. The omen does not precede and does not exist without the individual, its existence is linked to the complete presence of the subject. In this scenario, text and body are inseparable.",
        ]),
        ("i", ["02", "03"]),
        ("t", "The design.", [
            "The user interface consists of a set of signs linked to the notion of future and writing: radiographs of hands lit intermittently by red leds that write in morse code the word destiny (- .... ... - .. -. -). Word that in Arabic maktub simultaneously means 'destiny' and 'inscription'.",
        ]),
        ("i", ["06", "05"]),
        ("t", "Writing contemporary omens.", [
            "In ancient times, oracular practice was considered a spiritual and intellectual activity of a religious nature that provided answers to logical and pragmatic dilemmas. Formulated as irrefutable facts, their omens were used to resolve moral, economic, war and territorial conflicts.",
            "Today we recognize the role of polysemy (the very word 'oracle' refers to both the physical space, the enunciator, the discourse and the interpreter) in the productive and enigmatic result of its propositions.",
            "To write these omens, the project received advice from the Department of Ancient Philology at the Faculty of Philosophy and Letters of the University of Buenos Aires to find adequate critical, literary and philosophical materials.",
        ]),
        ("i", ["portada"]),
    ],
)

page(
    slug="prepixel", folder="prepixel", title="Pre-pixel Symphony in Major Fractal I", year="2014",
    venue=[], people="",
    lead_alt="Pre-pixel Symphony in Major Fractal I: VHS feedback over a film still", video="https://vimeo.com/100402501",
    intro=[],
    kind="", tech="",
    blocks=[
        ("t", "Closed Circuit: Pre-pixel symphony in major fractal I (2014)", [
            "In closed circuits, vitality is a pathology, a chain reaction?",
            "\"Prepixel Symphony in Fractal Major I\", is part of a series of analog live interventions on classic films in VHS format.",
            "In this case about Nosferatu. Vampire of the Night (1979) by Werner Herzog, which in turn is a review of Nosferatu. A Symphony of Horror (1922) by F.W. Murnau",
            "Performance / VHS / Electronic Music VHS feedback, Found footage. Length 6,20\"",
        ]),
        ("t", "The song of the rooster: Pre-pixel symphony in major fractal I (2014)", [
            "What happens to the body when it is altered recursively, not as a form but as a formula?",
            "\"The song of the rooster\", is part of a series of analog live interventions on classic films in VHS format.",
            "Performance / VHS / Electronic Music VHS feedback, Found footage. Length 7,47\"",
        ]),
        ("vimg", "https://vimeo.com/100402508", "The song of the rooster: watch the video", "rooster"),
    ],
)

page(
    slug="visionoros", folder="visionoros", title="Visionoros Collective", year="2013–present",
    venue=[], people="",
    lead_alt="Visionoros: performance with VHS feedback", video="https://vimeo.com/147182332", credit_title="Credits, Visionoros Cosmic Ed.",
    intro=[
        "Visionoros is a shifting collective that designs audiovisual performances to defragment images and augment sound perceptions based on the experimentation/improvisation with analog-digital technologies. We are interested in is the hidden life of images and sounds.",
        "An essential part of the project is the inclusion of local artists or those willing to experiment collectively on mutable pieces and assemblies.",
    ],
    kind="Performance / VHS / Electronic Music", tech="Custom made guitars, homemade wooden projectors, VHS feedback, live-coding.",
    blocks=[
        ("i", ["01", "02", "03", "04", "05", "06"]),
        ("t", "Visionoros Cosmic Ed. (2016)", [
            "Mario Guzman, Agustín Ramos Anzorena",
            "Performance / Soundscapes / VHS feedback / Analog Visuals VHS feedback, Found footage, original music Length 30 min",
        ]),
        ("v", "https://vimeo.com/149999400", "Visionoros Cosmic Ed., video"),
    ],
)

page(
    slug="ona", folder="ona", title="ONA", year="2017",
    venue=["Open Borders, Palazzo Mora, European Cultural Centre, Venice"], people="by Joaquín Gómez and Tomás Terzano",
    lead_alt="ONA: blue LED strips around an Andean cross, with a lit acrylic box at its centre",
    intro=[
        "Ona is a luminous synchronisation device that create a quiet and mystical environment that allowed viewers to perceive the visual and sound subtleties present in the installation. It has a simple interface from where to regulate the intensity, speed and patterns of the led strips that surround the image of the Andean cross. At the same time this device had the function of pointing out the ideal space to perceive the sounds coming from a unidirectional speaker that reproduced voices of the Selknam Indians.",
    ],
    kind="Luminous synchronisation device for immersive audiovisual installation", tech="installation immersion audio-reactive",
    blocks=[("i", [("02", "ONA: a visitor stands in a dark corridor between lit panels, with blue light on the floor", "")])],
    credits=[("Main Project Direction and Sound Design", "Joaquín Gómez, Tomás Terzano"),
             ("Light synchronisation and programming", "Mario Guzman, with Agustín Ramos Anzorena"),
             ("Production", "Juana Carranza Vélez"), ("Film Footage", "Ben Sturgulewski")],
    exhibitions=[("Open Borders.", "Palazzo Mora, European Cultural Centre, Venice, 2017.", "")], press=[], source="https://www.pleek.net/projects/ona.html",
)

page(
    slug="legible-journey", folder="robots", lead="legible", title="Legible Journey", year="",
    venue=["Festival ZERO1, La Rochelle, 17 to 21 April 2025", "Espace Mendès France, 7 March 2025"], people="by Colectivo Línea 60",
    lead_alt="Legible Journey: a visitor pedals a bicycle on a platform among 3D-printed letters", video="https://vimeo.com/1064248159/bf6588966a",
    intro=[
        "Visitors pedal a bicycle mounted on a platform among 3D-printed letters, and their pedalling moves through a sound composition recorded on a bicycle journey from La Rochelle to Athens.",
        "The work reinterprets Jeffrey Shaw's Legible City (1988).",
    ],
    kind="", tech="", blocks=[],
    credits=[("Mario Guzman", "concept and programming"), ("Simon Breil", "programming and electronics"),
             ("Eléanor Faber", "traveller and sound capture"), ("João Garcia", "concept and graphics"),
             ("Diego Jarak", "artistic direction, concept, 3D, fabrication"), ("Maela Le Scouarnec", "traveller and sound capture"),
             ("Birgit Mollemelier", "fabrication and artistic advice"), ("Sarah Paixão", "distribution"),
             ("Jeanne Soccorsi", "coordination"), ("Julia Suero", "concept and sound design")],
    links=[("Legible Journey at Festival ZERO1", "https://www.festivalzero1.com/en/projets/legible-journey"),
           ("Video", "https://vimeo.com/1064248159/bf6588966a")],
    exhibitions=[("Festival ZERO1.", "La Rochelle, 17 to 21 April 2025.", ""), ("Espace Mendès France.", "7 March 2025.", "")], press=[], tech_section=True,
)

page(
    slug="mirar-al-cielo", folder="mirar", title="Mirar al cielo / 52 tonos de azul", year="",
    venue=["Fundación Andreani, BIENALSUR 2021, Videoformes 2022"], people="by Gabriela Golder",
    lead_alt="Mirar al cielo / 52 tonos de azul: four skies with generated words",
    intro=[
        "A neural network system reads videos of skies sent from different cities since March 2020 and answers them with fragments of scientific and poetic texts.",
        "The video installation version is called 52 tonos de azul.",
    ],
    kind="", tech="", blocks=[],
    credits=[("Idea and creation", "Gabriela Golder"), ("Neural network implementation", "Mario Guzmán"), ("Web development", "Lucas Medina"),
             ("General assistance", "Abel Cassanelli"), ("Translation", "Mariana Lombard"),
             ("Thanks for the skies to", "Paz Encina, Luciano Zubillaga, Hrair Sarkissian, Andres Hilarion, Claudia Joskowicz")],
    links=[("Link to the project", "http://gabrielagolder.com/cielos.html")],
    exhibitions=[("Fundación Andreani.", "Buenos Aires, Argentina, 2021.", ""), ("Jax District, BienalSur 2021.", "Riyadh, Saudi Arabia.", ""), ("Videoformes.", "Clermont-Ferrand, France, 2022.", "")], press=[], tech_section=True,
)

page(
    slug="memory-of-everywhere", folder="memory", title="Memory of Everywhere", year="2020",
    venue=["(Un)Continuity. Electronic Literature Organization. UCF Gallery, Orlando, USA, 2020"], people="",
    lead_alt="Memory of Everywhere: output of the neural network over a video still", old="lstm/index.html",
    intro=[
        "\"Memory of everywhere\" is a textual artificial organism that performs a reading and writing exercise using video input from around the globe and a generative language model trained on 19th-century travel literature. The work focuses on the notion of travel, journey, discovery, and cognition.",
        "The work arises from a need to comprehend a series of chaotic experiences while traveling to more than 45 countries and 1,723 flight hours with a social robot.",
        "To make sense of the speed and heterogeneity of these episodes, I trained a writing system to explain to me what it thought it was happening.",
        "The system articulates two structures: a convolutional neural network using mobile vision and a long short-term memory (LSTM) architecture of recurrent neural network (RNN).",
        "The work is also an experiment around an endless writing that tries to understand a world constituted by limited objects and perceptions, perhaps a reflection of our own cognitive operations.",
    ],
    kind="Machine Learning / Experimental Literature / Live Installation", tech="Machine Learning, convolutional neural network, mobile vision, long short-term memory (LSTM), projection, XIX century travel literature corpus, travel videos.",
    blocks=[],
    exhibitions=[("(Un)Continuity. Electronic Literature Organization.", "UCF Gallery, Orlando, USA, 2020.", "https://projects.cah.ucf.edu/mediaartsexhibits/uncontinuity/Guzman/guzman.html"),
                 ("Neologías Artificiales: arte con inteligencia artificial, Linne Magazine", "", "https://linnemagazine.com/2021/07/13/neologias-artificiales-arte-con-inteligencia-artificial/")],
    press=[], links=[], credits=[],
)

# Previous / next order on the pager (the Works list of the homepage)
ORDER = ["she-tells-sea-shells", "liminal_sanctuary", "entangled_matter", "aerodynamics-seeds", "conciencia",
         "quetzabot", "cenotes", "combinatory_nierika", "learningtowrite", "bitcelulle", "ped", "lastagreement",
         "temazcalli", "hiperstories", "oraculo", "prepixel", "visionoros"]
