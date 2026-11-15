/* mario-guzman.com v2. Vanilla JavaScript, no libraries.
   1. the main image rotates through the works (homepage only)
   2. click the question in the opening statement: the browser's synthetic voice asks it
   3. click the name: the letters scramble for a moment and settle back
   4. YouTube, Vimeo and Mux links open in an overlay; other outside links open in a new tab
   Pages set <body data-root="../"> when they sit one folder down. */
(function () {
  var root = document.body.getAttribute("data-root") || "";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // 1. rotation: random first slide, crossfade every 5 s, pause on hover or focus
  var rot = document.getElementById("rot");
  if (rot) {
    var W = "images/web/", P = "project/";
    var slides = [
      [W + "liminal/lead.jpg", "Liminal Sanctuary, 2024", "XV Biennale of Contemporary African Art, Dakar", P + "liminal_sanctuary.html"],
      [W + "golem/lead.jpg", "Entangled Matter: AI, Humans and Golems, 2023", "Festival ZERO1, La Rochelle", P + "entangled_matter.html"],
      [W + "conciencia/lead.jpg", "Consciousness Is the Precooking of the Universal Mind, 2022", "Latin American Artificial Intelligence Biennial", P + "conciencia.html"],
      [W + "she-tells/lead.jpg", "She Tells, Sea Shells, 2026", "S+T+ARTS Aqua Motion, UNESCO Venice Office", P + "she-tells-sea-shells.html"],
      [W + "cenote/lead.jpg", "Cenote Reflections, 2023", "", P + "cenotes.html"],
      [W + "nierika/lead.jpg", "Combinatory Nierika, 2020", "Taper #5", P + "combinatory_nierika.html"],
      [W + "golem/main.jpg", "Entangled Matter: AI, Humans and Golems, 2023", "Festival ZERO1, La Rochelle", P + "entangled_matter.html"],
      [W + "temazcalli/lead.jpg", "Temazcalli-Dome, 2015–2016", "Planetario Galileo Galilei, Buenos Aires", P + "temazcalli.html"]
    ];
    var a = document.getElementById("rotA"), b = document.getElementById("rotB");
    var t = document.getElementById("rotT"), v = document.getElementById("rotV");
    var i = Math.floor(Math.random() * slides.length), front = a, back = b, paused = false;
    var show = function (n, instant) {
      var s = slides[n];
      if (instant) { front.src = root + s[0]; front.alt = s[1]; }
      else {
        back.src = root + s[0]; back.alt = s[1];
        back.classList.remove("off"); front.classList.add("off");
        var x = front; front = back; back = x;
      }
      rot.href = root + s[3];
      t.textContent = s[1]; v.textContent = s[2];
    };
    show(i, true);
    rot.addEventListener("mouseenter", function () { paused = true; });
    rot.addEventListener("mouseleave", function () { paused = false; });
    rot.addEventListener("focus", function () { paused = true; });
    rot.addEventListener("blur", function () { paused = false; });
    if (!reduced) {
      setInterval(function () {
        if (paused || document.hidden) return;
        i = (i + 1) % slides.length;
        show(i);
      }, 5000);
    }
  }

  // 2. the question is spoken by a different installed voice on each click
  var say = document.getElementById("say");
  if (say && "speechSynthesis" in window) {
    var n = 0;
    var speak = function (el) {
      var lang = document.documentElement.lang || "en";
      var voices = speechSynthesis.getVoices().filter(function (x) { return x.lang.slice(0, 2) === lang; });
      var u = new SpeechSynthesisUtterance(el.textContent);
      u.lang = lang;
      if (voices.length) { u.voice = voices[n % voices.length]; n++; }
      u.onstart = function () { el.classList.add("on"); };
      u.onend = u.onerror = function () { el.classList.remove("on"); };
      speechSynthesis.cancel();
      speechSynthesis.speak(u);
    };
    speechSynthesis.getVoices();
    say.addEventListener("click", function (e) { var el = e.target.closest(".ask"); if (el) speak(el); });
    say.addEventListener("keydown", function (e) {
      var el = e.target.closest(".ask");
      if (el && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); speak(el); }
    });
  }

  // 3. the name scrambles for about 0.7 s (skipped when reduced motion is set)
  var me = document.getElementById("me");
  if (me) {
    var name = me.textContent, busy = false, pool = "abcdefghijklmnopqrstuvwxyz";
    var run = function () {
      if (busy || reduced) return;
      busy = true;
      var start = Date.now(), dur = 700;
      var timer = setInterval(function () {
        var k = (Date.now() - start) / dur, out = "";
        for (var j = 0; j < name.length; j++) {
          var c = name[j];
          if (c === " " || j / name.length < k) out += c;
          else { var r = pool[Math.floor(Math.random() * pool.length)]; out += (c === c.toUpperCase()) ? r.toUpperCase() : r; }
        }
        me.textContent = out;
        if (k >= 1) { clearInterval(timer); me.textContent = name; busy = false; }
      }, 45);
    };
    me.addEventListener("click", run);
    me.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); run(); } });
  }

  // 4. overlay player for YouTube, Vimeo and Mux; other outside links open in a new tab
  var box = document.createElement("div");
  box.id = "box";
  box.innerHTML = '<button type="button">close</button><iframe allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="video"></iframe>';
  document.body.appendChild(box);
  var frame = box.querySelector("iframe");
  var embed = function (url) {
    var m = url.match(/youtube(?:-nocookie)?\.com\/(?:watch\?v=|embed\/)([\w-]+)/);
    if (m) return "https://www.youtube-nocookie.com/embed/" + m[1] + "?autoplay=1";
    m = url.match(/stream\.mux\.com\/(\w+)/);
    if (m) return "https://player.mux.com/" + m[1] + "?autoplay=true";
    m = url.match(/vimeo\.com\/(?:video\/)?(\d+)(?:\/(\w+))?/);
    if (m) return "https://player.vimeo.com/video/" + m[1] + "?autoplay=1" + (m[2] ? "&h=" + m[2] : "");
    return null;
  };
  var closeBox = function () { box.classList.remove("open"); frame.src = "about:blank"; };
  var last = null;
  document.querySelectorAll('a[href^="http"]').forEach(function (l) {
    var e = embed(l.href);
    if (e) {
      l.addEventListener("click", function (ev) {
        ev.preventDefault(); last = l; frame.src = e; box.classList.add("open");
        box.querySelector("button").focus();
      });
    } else { l.target = "_blank"; l.rel = "noopener"; }
  });
  box.addEventListener("click", function (ev) { if (ev.target !== frame) { closeBox(); if (last) last.focus(); } });
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape" && box.classList.contains("open")) { closeBox(); if (last) last.focus(); } });
})();
