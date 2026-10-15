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

// Formulaire de contact : validation, puis envoi par e-mail via FormSubmit (adresse dans data-envoi)
const EN = document.documentElement.lang === "en";
const T = EN
  ? { consent: "Please tick the consent box.", requis: "Please fill in the required fields (*).",
      envoi: "Sending…", merci: "Thank you! Your message is on its way, we'll get back to you very soon.",
      erreur: "Sorry, the message could not be sent. Please email us directly at " }
  : { consent: "Merci de cocher la case de consentement.", requis: "Merci de remplir les champs obligatoires (*).",
      envoi: "Envoi en cours…", merci: "Merci ! Votre message est bien parti, on revient vers vous très vite.",
      erreur: "Désolé, le message n'a pas pu partir. Écrivez-nous directement à " };
const form = document.querySelector(".form");
if (form) {
  const besoin = new URLSearchParams(location.search).get("besoin");
  if (besoin) {
    const box = form.querySelector(`input[name="besoin"][value="${CSS.escape(besoin)}"]`);
    if (box) box.checked = true;
  }
  const status = form.querySelector(".form-status");
  const bouton = form.querySelector('button[type="submit"]');
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    let firstBad = null;
    form.querySelectorAll("[required]").forEach((el) => {
      const ok = el.type === "checkbox" ? el.checked : el.checkValidity() && el.value.trim() !== "";
      el.closest(".field")?.toggleAttribute("data-error", !ok);
      if (!ok && !firstBad) firstBad = el;
    });
    if (firstBad) {
      status.className = "form-status full err";
      status.textContent = firstBad.name === "consent" ? T.consent : T.requis;
      firstBad.focus();
      return;
    }
    const d = new FormData(form);
    if (d.get("_honey")) return; // champ invisible rempli : robot
    const besoins = d.getAll("besoin").map((v) => form.querySelector(`input[value="${v}"]`).nextElementSibling.textContent);
    const donnees = {
      Nom: d.get("nom"), Email: d.get("email"), "Téléphone": d.get("tel") || "—",
      Entreprise: d.get("entreprise") || "—", Besoin: besoins.join(", ") || "—", Message: d.get("message"),
      Langue: EN ? "anglais" : "français", Page: location.href,
      _subject: `Nouveau message du site — ${d.get("nom")}`, _replyto: d.get("email"), _template: "table",
    };
    status.className = "form-status full";
    status.textContent = T.envoi;
    bouton.disabled = true;
    try {
      const r = await fetch(form.dataset.envoi, {
        method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(donnees),
      });
      const rep = await r.json().catch(() => ({}));
      if (!r.ok || rep.success === false || rep.success === "false") throw new Error(rep.message || r.status);
      status.className = "form-status full ok";
      status.textContent = T.merci;
      form.reset();
    } catch (err) {
      console.warn("Formulaire non envoyé :", err.message); // ex. « This form needs Activation » (FormSubmit)
      const mail = form.dataset.envoi.split("/").pop();
      status.className = "form-status full err";
      status.textContent = T.erreur + mail + ".";
    } finally {
      bouton.disabled = false;
    }
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

// Visionneuse : glisser le doigt vers la gauche / la droite pour changer de photo
if (lightbox) {
  let x0 = null;
  lightbox.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  lightbox.addEventListener("touchend", (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) lightbox.querySelector(dx < 0 ? ".lb-next" : ".lb-prev").click();
    x0 = null;
  }, { passive: true });
}
