// Frostbird — comportements de la maquette

// Menu mobile
const burger = document.querySelector(".nav-burger");
const menu = document.getElementById("menu");
if (burger && menu) {
  const toggle = (open) => {
    burger.setAttribute("aria-expanded", open);
    burger.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
    menu.hidden = !open;
    document.body.style.overflow = open ? "hidden" : "";
  };
  burger.addEventListener("click", () => toggle(menu.hidden));
  document.addEventListener("keydown", (e) => e.key === "Escape" && !menu.hidden && toggle(false));
  matchMedia("(min-width: 761px)").addEventListener("change", (e) => e.matches && toggle(false));
}

// Slogan final : la ligne occupe toute la largeur
const fit = document.querySelector(".fit");
if (fit) {
  const resize = () => {
    fit.style.fontSize = "100px";
    const w = fit.parentElement.clientWidth - parseFloat(getComputedStyle(fit.parentElement).paddingLeft) * 2;
    fit.style.fontSize = (100 * w) / fit.scrollWidth + "px";
  };
  document.fonts.ready.then(resize);
  addEventListener("resize", resize);
}

// Works : filtres par catégorie
const filtres = document.querySelectorAll("[data-filtre]");
filtres.forEach((btn) =>
  btn.addEventListener("click", () => {
    const f = btn.dataset.filtre;
    filtres.forEach((b) => b.setAttribute("aria-pressed", b === btn));
    document.querySelectorAll(".work").forEach((w) => (w.hidden = f !== "tout" && w.dataset.cat !== f));
  })
);

// Formulaire de contact (pas encore branché : validation + message seulement)
const form = document.querySelector(".form");
if (form) {
  const besoin = new URLSearchParams(location.search).get("besoin");
  if (besoin) {
    const box = form.querySelector(`input[name="besoin"][value="${CSS.escape(besoin)}"]`);
    if (box) box.checked = true;
  }
  const status = form.querySelector(".form-status");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let firstBad = null;
    form.querySelectorAll("[required]").forEach((el) => {
      const ok = el.type === "checkbox" ? el.checked : el.checkValidity() && el.value.trim() !== "";
      el.closest(".field")?.toggleAttribute("data-error", !ok);
      if (!ok && !firstBad) firstBad = el;
    });
    if (firstBad) {
      status.className = "form-status full err";
      status.textContent = firstBad.name === "consent"
        ? "Merci de cocher la case de consentement."
        : "Merci de remplir les champs obligatoires (*).";
      firstBad.focus();
      return;
    }
    status.className = "form-status full ok";
    status.textContent = "Merci ! Votre message est bien parti, on revient vers vous très vite.";
    form.reset();
  });
}

// Visionneuse des galeries photo
const lightbox = document.querySelector(".lightbox");
if (lightbox) {
  const items = [...document.querySelectorAll(".gal-item")];
  const img = lightbox.querySelector("img");
  const count = lightbox.querySelector(".lb-count");
  let current = 0;
  const show = (i) => {
    current = (i + items.length) % items.length;
    img.src = items[current].dataset.src;
    img.alt = items[current].querySelector("img").alt;
    count.textContent = `${current + 1} / ${items.length}`;
  };
  items.forEach((btn, i) => btn.addEventListener("click", () => { show(i); lightbox.showModal(); }));
  lightbox.querySelector(".lb-close").addEventListener("click", () => lightbox.close());
  lightbox.querySelector(".lb-prev").addEventListener("click", () => show(current - 1));
  lightbox.querySelector(".lb-next").addEventListener("click", () => show(current + 1));
  lightbox.addEventListener("click", (e) => e.target === lightbox && lightbox.close());
  lightbox.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });
  lightbox.addEventListener("close", () => items[current].focus());
}

// Vidéos d'ambiance : pas de lecture automatique si l'utilisateur limite les animations
if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll("video[autoplay]").forEach((v) => { v.pause(); v.controls = true; });
}

// Comparateur avant / après
document.querySelectorAll(".compare").forEach((c) => {
  const range = c.querySelector(".compare-range");
  range.addEventListener("input", () => c.style.setProperty("--pos", range.value + "%"));
});

// Série sur une ligne : flèches de défilement (masquées en bout de ligne)
document.querySelectorAll(".gal-row-wrap").forEach((w) => {
  const row = w.querySelector(".gal-row");
  const prev = w.querySelector(".gal-nav-prev");
  const next = w.querySelector(".gal-nav-next");
  const pas = () => row.clientWidth * 0.8;
  const maj = () => {
    prev.disabled = row.scrollLeft <= 4;
    next.disabled = row.scrollLeft + row.clientWidth >= row.scrollWidth - 4;
  };
  prev.addEventListener("click", () => row.scrollBy({ left: -pas() }));
  next.addEventListener("click", () => row.scrollBy({ left: pas() }));
  row.addEventListener("scroll", maj, { passive: true });
  addEventListener("resize", maj);
  row.querySelectorAll("img").forEach((i) => i.addEventListener("load", maj));
  maj();
});
