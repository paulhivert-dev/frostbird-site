#!/usr/bin/env python3
"""Génère la maquette statique du site Frostbird dans public/.

Architecture reprise de makak-makak.com :
  /                  hero · références · contact · slogan · footer (sections plein écran)
  /prestations       cartes métiers → /prestation-<clé> : une histoire et une mise en scène par métier
  /works             grille de projets filtrable
  /projet-<slug>     étude de cas (hero, processus, captures légendées, autres projets)
  /contact           formulaire seul
  /mentions-legales  pages légales

Ne pas éditer les HTML de public/ à la main : modifier ce fichier, puis
`python3 build.py`. Le CSS et le JS vivent directement dans public/assets/.
"""
from pathlib import Path

from contenu_portfolio import PORTFOLIO
from contenu_prestations import PAGES

OUT = Path(__file__).parent / "public"
# Images d'origine (JPG/PNG pleine qualité) : hors du dossier publié. Le build en tire des WebP
# dans public/ (cf. optimiser_medias) — seules les versions optimisées partent en ligne.
MEDIA = Path(__file__).parent / "media"

# --- Contenu (provisoire : à remplacer par les vrais textes) -----------------
AGENCE = "Frostbird"
BASELINE = "Agence créative"
SLOGAN = "Born to fly"
EMAIL = "hello@frostbird.fr"
METIERS = [
    # (clé, titre, description courte)
    ("branding", "Branding", "Logos, identités visuelles, chartes graphiques. Des marques qu'on reconnaît de loin."),
    ("design", "Design graphique", "Print, affiches, réseaux sociaux, packaging. Tout ce qui doit se voir."),
    ("web", "Web & Apps", "Sites vitrines, e-commerce, applications. Rapides, beaux, faciles à faire vivre."),
    ("photo", "Photographie", "Portraits, produits, reportages, événements. Des images qui racontent votre marque."),
]
CLIENTS = [
    # (nom, fichier dans assets/img/clients — logo monochrome utilisé en masque, ratio largeur/hauteur)
    ("Chikin Bang", "chikin-bang.png", 1.633),
    ("Cupidex", "cupidex.svg", 1.279),
    ("Gomu", "gomu.png", 1.093),
    ("Birdz Hot Chicken", "birdz.png", 1.0),
    ("First Touch", "first-touch.svg", 2.057),
]
PROJETS = [
    # (catégorie, titre, date[, image de couverture dans assets/img/works, slug de l'étude de cas])
    ("web", "Application Cupidex", "En cours", "cupidex-app/pokedex.jpg", "cupidex-app"),
    ("web", "Site de lancement Cupidex", "Juillet 2026", "cx-1.jpg", "cupidex"),
    ("web", "Portfolio de Paul Hivert", "Septembre 2026", "ph-1.jpg", "paulhivert"),
    ("photo", "Raffiné", "2025", "raffine/raffine-16.jpg", "raffine"),
    ("photo", "Birdz", "2025", "birdz/birdz-02.jpg", "birdz"),
    ("photo", "Championnat National", "2025 – 2026", "national/national-13.jpg", "national"),
] + [(e["cat"], e["titre"], e["date"], e["cover"], e["slug"]) for e in PORTFOLIO]  # branding puis design
# Logo du client posé sur la carte projet (fichier dans assets/img/clients, ratio largeur/hauteur).
# La carte montre le logo en crème sur bordeaux ; au survol, le même logo dans ses vraies couleurs
# (assets/img/clients/couleur) sur le fond de la marque. Aucun aperçu du travail.
LOGOS_PROJETS = {
    # slug: (logo monochrome, ratio, fond de marque au survol)
    "cupidex-app": ("cupidex.png", 1.899, "linear-gradient(135deg, #1f1168, #7655ca)"),
    "cupidex": ("cupidex.png", 1.899, "linear-gradient(135deg, #1f1168, #7655ca)"),  # mot en Poppins ExtraBold Italic, comme cupidex.fr
    "paulhivert": ("paulhivert.png", 5.193, "radial-gradient(circle at 60% 20%, #3c4952, #191a1e 70%)"),
    "birdz": ("birdz.png", 1.0, "#ffffff"),
    "raffine": ("raffine.png", 1.353, "#ffffff"),
    "national": ("national.png", 1.027, "#ffffff"),
}
LOGOS_PROJETS.update({e["slug"]: e["logo"] for e in PORTFOLIO if e["logo"]})

# Galeries photo complètes (ordre du portfolio paulhivert.com), images dans assets/img/works/<slug>/
def _serie(slug, noms):
    return [f"{slug}/{n}.jpg" for n in noms.split()]

GALERIES = {
    # raffine-01 (le cuisinier) a pris la place de raffine-06 (les deux cuisiniers masqués) ; raffine-36 retirée
    "raffine": _serie("raffine", "raffine-21 raffine-02 raffine-03 raffine-04 raffine-05 raffine-01 "
                      + " ".join(f"raffine-{i:02d}" for i in range(7, 21)) + " p33 "
                      + " ".join(f"raffine-{i:02d}" for i in range(22, 38) if i != 36)),  # 36 retirée
    "birdz": _serie("birdz", "birdz-13 birdz-01 birdz-02 birdz-03 birdz-04 birdz-05 birdz-06 birdz-07 birdz-08 "
                             "birdz-09 birdz-11 birdz-12 p35 birdz-14 birdz-15 birdz-16"),
    "national": _serie("national", "national-19 national-08 national-01 national-09 national-02 national-10 "
                                   "national-03 national-11 national-04 national-12 national-05 national-13 "
                                   "national-06 national-14 national-07 national-15 national-18 national-16 "
                                   "p31 national-17"),
}

# Études de cas : une page projet-<slug>.html par entrée.
# url : facultatif (bouton « Voir le site en ligne »)
# captures : (image ou vidéo .mp4, légende, "desktop" | "mobile" | "photo-h" | "photo-v")
# galerie : facultatif, série complète affichée en grille avec visionneuse
ETUDES = {
    "cupidex": {
        "client": "Cupidex",
        "url": "https://cupidex.fr/",
        "sous_titre": "Une page d'attente pour faire monter l'envie avant la sortie de l'application",
        "intro": "Cupidex est une application de rencontre qui transforme chaque rencontre en entrée "
                 "d'une collection : une lettre par prénom, un badge qui évolue au fil de l'histoire. "
                 "Avant la sortie sur les stores, il fallait une vitrine pour présenter le concept "
                 "et recueillir les premiers inscrits.",
        "services": ["Direction artistique", "Webdesign", "Développement", "Hébergement"],
        "processus": [
            ("Comprendre", "À qui parle l'application, ce qui la rend différente, et ce qu'un visiteur "
                           "doit retenir en dix secondes."),
            ("Direction artistique", "Prolongement de la charte Cupidex : dégradés violet-rose, titres "
                                     "italiques très gras, logo cœur-flèche. Un ton direct, en tutoiement."),
            ("Développement", "Une page statique unique, sans aucune dépendance : très légère, rapide "
                              "à charger, simple à faire évoluer jusqu'au lancement."),
            ("Mise en ligne", "Nom de domaine cupidex.fr, hébergement sur un serveur dédié en HTTPS, "
                              "publication en un clic depuis GitHub."),
        ],
        "captures": [
            ("cx-1.jpg", "Le message tient en une phrase : Cupidex arrive, et voilà pourquoi tu vas l'aimer.", "desktop"),
            ("cx-2.jpg", "Le concept expliqué en quatre cartes : lettres à collectionner, badges, séries, contrôle.", "desktop"),
            ("cx-mobile.jpg", "Pensé d'abord pour le téléphone, là où l'application vivra.", "mobile"),
        ],
    },
    "cupidex-app": {
        "client": "Cupidex",
        "sous_titre": "Une application de rencontre où chaque rencontre rejoint une collection",
        "intro": "Cupidex reprend les codes des applications de swipe pour les détourner vers un "
                 "objectif de collection : chaque rencontre remplit un Cupidex personnel, classé par la "
                 "première lettre du prénom, avec des lettres rares, des badges qui évoluent et des "
                 "séries à tenir. Frostbird conçoit l'application de bout en bout : concept, design, "
                 "application iOS et Android, et le serveur qui la fait tourner. Le projet est en cours : "
                 "l'application est en phase de tests avant sa sortie sur les stores.",
        "services": ["Concept & UX", "UI design", "Application iOS & Android", "Back-end & hébergement"],
        "processus": [
            ("Concept", "Détourner le swipe vers la collection : une lettre par prénom, des lettres rares, "
                        "des badges du match jusqu'à la relation."),
            ("Maquettes", "Un prototype cliquable de tous les écrans, puis une direction « verre liquide » "
                          "en violet et rose."),
            ("Développement", "Une application React Native pour iOS et Android, et une API Spring Boot : "
                              "profils, matchs, messagerie, collection, modération."),
            ("Tests", "Une nouvelle version testée chaque semaine sur un serveur de recette, jusqu'au "
                      "lancement sur les stores."),
        ],
        "captures": [
            ("cupidex-app/splash.jpg", "« Collectionne l'amour » : l'application donne le ton dès l'ouverture.", "mobile"),
            ("cupidex-app/home.jpg", "Le swipe, version Cupidex : l'essentiel d'un profil en un coup d'œil.", "mobile"),
            ("cupidex-app/pokedex.jpg", "Le cœur de l'application : une collection de lettres, des plus courantes aux plus rares.", "mobile"),
            ("cupidex-app/historique.jpg", "L'historique : toutes les rencontres sur une frise, de la plus récente à la plus ancienne.", "mobile"),
            ("cupidex-app/badges.jpg", "Les badges : régularité, lettres, pays… tout ce qu'il reste à décrocher, avec l'avancée de chacun.", "mobile"),
            ("cupidex-app/map.jpg", "La carte des conquêtes : un globe où chaque pays rencontré s'allume.", "mobile"),
            ("cupidex-app/likes.jpg", "Ceux qui t'ont liké, mis en avant selon les lettres qui te manquent.", "mobile"),
        ],
        "galerie": ["cupidex-app/splash.jpg", "cupidex-app/home.jpg", "cupidex-app/pokedex.jpg",
                    "cupidex-app/historique.jpg", "cupidex-app/badges.jpg", "cupidex-app/map.jpg",
                    "cupidex-app/likes.jpg", "cupidex-app/messages.jpg", "cupidex-app/chat.jpg",
                    "cupidex-app/profile.jpg"],
        "galerie_ligne": True,
    },
    "paulhivert": {
        "client": "Paul Hivert",
        "url": "https://www.paulhivert.com/",
        "sous_titre": "Un écrin sombre et sur mesure pour le portfolio d'un directeur artistique",
        "intro": "Paul Hivert est directeur artistique et chef de projets : logos, affiches, motion design, "
                 "photographie, print. Son portfolio devait présenter une trentaine de projets sans "
                 "jamais leur voler la vedette, et montrer son exigence graphique dès la première seconde.",
        "services": ["Direction artistique", "Lettrage sur mesure", "Développement", "Mise en ligne"],
        "processus": [
            ("Audit & reprise", "Récupération du code et du nom de domaine, puis inventaire complet des "
                                "contenus : 6 catégories, 29 pages projets."),
            ("Direction artistique", "Une ambiance « brume » bleu-charbon avec du grain, et un lettrage "
                                     "géométrique dessiné sur mesure pour le titre."),
            ("Développement", "Next.js et TypeScript : pages catégories, pages projets, visionneuse, "
                              "vidéos, menu mobile. Rapide et entièrement responsive."),
            ("Mise en ligne", "Déploiement sur Vercel, reprise du domaine paulhivert.com, "
                              "redirections et HTTPS."),
        ],
        "captures": [
            ("ph-1.jpg", "Un accueil sobre : un nom, un métier, et l'envie de faire défiler.", "desktop"),
            ("ph-2.jpg", "Chaque catégorie a sa page, avec les projets présentés en grand format.", "desktop"),
            ("ph-3.jpg", "Les visuels prennent toute la place : le site s'efface derrière le travail.", "desktop"),
            ("ph-mobile.jpg", "Sur mobile, la même ambiance, sans compromis.", "mobile"),
        ],
    },
}
ETUDES.update({
    "raffine": {
        "client": "Raffiné",
        "sous_titre": "Capturer l'ambiance d'un restaurant premium, de la cuisine jusqu'à l'assiette",
        "intro": "Raffiné est un restaurant premium qui cuisine de très bons produits dans un lieu "
                 "visuellement superbe. Les photos devaient représenter le restaurant tel qu'il est "
                 "et nourrir la belle image qu'il s'est construite.",
        "services": ["Direction artistique", "Photographie culinaire", "Retouche"],
        "processus": [
            ("Repérage", "Visite du restaurant pendant le service pour repérer les lumières, les matières "
                         "et les plats signatures."),
            ("Direction artistique", "Une image chaude et feutrée, fidèle au lieu : lumière basse, fonds "
                                     "sombres, reflets dorés."),
            ("Shooting", "Une séance en plein service : plats, cocktails, cuisine et équipe, "
                         "photographiés sur le vif."),
            ("Retouche & livraison", "Sélection, étalonnage homogène de toute la série et exports pour "
                                     "le site, les réseaux et l'imprimé."),
        ],
        "captures": [
            ("raffine/raffine-25.jpg", "Lumière basse, flammes, matières : on photographie l'ambiance autant que l'assiette.", "photo-v"),
            ("raffine/raffine-12.jpg", "Le lieu fait partie du récit : marbre éclairé, lumière dorée, l'équipe prête pour le service.", "photo-v"),
            ("raffine/raffine-05.jpg", "Au bar aussi, chaque geste est mis en scène.", "photo-v"),
        ],
        "galerie": GALERIES["raffine"],
    },
    "birdz": {
        "client": "Birdz Hot Chicken",
        "sous_titre": "Un shooting produit complet avant l'ouverture, pour les menus, les visuels et les réseaux",
        "intro": "Avant son ouverture, Birdz avait besoin de photos de toute sa gamme de poulet façon "
                 "Nashville pour ses menus, ses visuels et ses réseaux sociaux. Voici une partie des "
                 "images réalisées lors du shooting.",
        "services": ["Photographie produit", "Stylisme culinaire", "Retouche"],
        "processus": [
            ("Brief", "Lister toute la gamme à photographier avant l'ouverture : tenders, burgers, "
                      "sandwichs, accompagnements, menus."),
            ("Mise en scène", "Un décor aux couleurs de la marque : carrelage blanc, packagings bleus, "
                              "et le rouge du poulet Nashville en vedette."),
            ("Shooting produit", "Chaque produit sous plusieurs angles, du plan d'ensemble au gros plan "
                                 "qui donne faim."),
            ("Retouche & livraison", "Des images prêtes pour les menus, l'affichage en boutique et "
                                     "les réseaux sociaux."),
        ],
        "captures": [
            ("birdz/birdz-16.jpg", "Toute la gamme réunie : une seule image pour présenter la carte.", "photo-h"),
            ("birdz/birdz-03.jpg", "Le rouge Nashville en vedette, le bleu Birdz en écrin.", "photo-h"),
            ("birdz/birdz-15.jpg", "Des gros plans pensés pour donner faim, du menu jusqu'aux réseaux.", "photo-h"),
            ("birdz/coulisses.mp4", "L'envers du décor : la table dressée, les produits en place, juste avant le déclic.", "photo-v"),
        ],
        "galerie": GALERIES["birdz"],
    },
    "national": {
        "client": "Aïman & Ilan",
        "sous_titre": "Photographier deux espoirs du football en bord de terrain, match après match",
        "intro": "Aïman et Ilan jouent tous les deux en U19 National. Avec la possibilité de signer un "
                 "contrat professionnel, leur image doit être soignée, et cela commence par la "
                 "photographie en bord de terrain : on les photographie pendant leurs matchs, puis on "
                 "traite les images pour leurs réseaux.",
        "services": ["Photographie sportive", "Retouche", "Réseaux sociaux"],
        "processus": [
            ("Brief", "Comprendre l'enjeu : deux joueurs U19 National qui doivent soigner leur image "
                      "avant un possible contrat pro."),
            ("Bord de terrain", "Présence à leurs matchs pour capter l'action, les gestes techniques et "
                                "les moments de concentration."),
            ("Sélection & retouche", "Tri des meilleures images et retouche cohérente d'un match à "
                                     "l'autre, pour une image reconnaissable."),
            ("Diffusion", "Des formats prêts pour leurs réseaux, livrés rapidement après chaque rencontre."),
        ],
        "captures": [
            ("national/national-10.jpg", "Le dos, le numéro, le ciel : une image qui raconte le joueur avant le match.", "photo-v"),
            ("national/national-08.jpg", "L'action saisie au bon moment, au ras du terrain.", "photo-v"),
            ("national/national-19.jpg", "Des portraits épurés, pensés pour leurs réseaux.", "photo-v"),
        ],
        "galerie": GALERIES["national"],
    },
})

ETUDES.update({
    e["slug"]: {
        "client": e["client"], "sous_titre": e["sous_titre"], "intro": e["intro"],
        "services": e["services"], "processus": e["processus"],
        "captures": [(img, legende, "visuel") for img, legende in e["captures"]],
        "galerie": e["galerie"], "galerie_ligne": e.get("galerie_ligne", False),
        **({"video": e["video"]} if e.get("video") else {}),
        **({"avant_apres": e["avant_apres"]} if e.get("avant_apres") else {}),
    }
    for e in PORTFOLIO
})

RESEAUX = [("Instagram", "#"), ("LinkedIn", "#"), ("Behance", "#"), ("TikTok", "#")]

METIER_NOM = {k: t for k, t, _ in METIERS}


def logo(kind, cls=""):
    """Logo en masque CSS : prend la couleur `color` de son parent."""
    return f'<span class="logo-{kind} {cls}" role="img" aria-label="{AGENCE}"></span>'


def header(active, retour=None):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    nav = "".join([
        link("prestations.html", "Prestations", "prestations"),
        link("works.html", "Works", "works"),
        link("contact.html", "Contacts", "contact"),
    ])
    gauche = (f'<a class="nav-back" href="{retour}"><span aria-hidden="true">←</span> Retour</a>' if retour else
              '<div class="nav-lang" aria-label="Langue">'
              '<a href="#" aria-current="true">FR</a><span>/</span><a href="#" title="Version anglaise à venir">EN</a></div>')
    return f"""
<header class="nav">
  {gauche}
  <a class="nav-brand" href="index.html" aria-label="{AGENCE} — accueil">
    {logo("picto")}{logo("word")}
  </a>
  <nav class="nav-links">{nav}</nav>
  <button class="nav-burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
</header>
<div class="menu" id="menu" hidden>
  <nav>
    <a href="index.html">Accueil</a>
    <a href="prestations.html">Prestations</a>
    <a href="works.html">Works</a>
    <a href="contact.html">Contacts</a>
  </nav>
  <a class="menu-mail" href="mailto:{EMAIL}">{EMAIL}</a>
</div>"""


def footer():
    reseaux = "".join(f'<a href="{u}">{n}</a>' for n, u in RESEAUX)
    return f"""
<footer class="footer">
  <div class="footer-grid">
    <a class="footer-logo" href="index.html" aria-label="{AGENCE} — accueil">{logo("picto")}{logo("word")}</a>
    <div>
      <h4>Navigation</h4>
      <a href="prestations.html">Prestations</a>
      <a href="works.html">Works</a>
      <a href="index.html#references">Références</a>
      <a href="contact.html">Contact</a>
    </div>
    <div>
      <h4>Légal</h4>
      <a href="mentions-legales.html">Mentions légales</a>
      <a href="mentions-legales.html#confidentialite">Politique de confidentialité</a>
      <a href="mentions-legales.html#cookies">Gestion des cookies</a>
      <a href="mentions-legales.html#cgu">CGU</a>
    </div>
    <div>
      <h4>Éditeur</h4>
      <p>{AGENCE.upper()}<br>Société en cours d'immatriculation<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
  <div class="footer-social">{reseaux}</div>
  <p class="footer-copy">© 2026 {AGENCE} — Tous droits réservés.</p>
</footer>"""


def contact_section(titre_tag="h2"):
    besoins = "".join(
        f'<label class="chip"><input type="checkbox" name="besoin" value="{k}"><span>{t}</span></label>'
        for k, t, _ in METIERS
    )
    return f"""
<section class="chapter contact" id="contact">
  <div class="wrap">
    <{titre_tag} class="display contact-title">On en parle&nbsp;?</{titre_tag}>
    <a class="contact-mail display" href="mailto:{EMAIL}">{EMAIL}</a>
    <form class="form" novalidate>
      <div class="field"><label for="f-nom">Nom *</label><input id="f-nom" name="nom" placeholder="Votre nom" required autocomplete="name"></div>
      <div class="field"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" placeholder="vous@entreprise.com" required autocomplete="email"></div>
      <div class="field"><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" placeholder="06 00 00 00 00" autocomplete="tel"></div>
      <div class="field"><label for="f-ent">Entreprise</label><input id="f-ent" name="entreprise" placeholder="Nom de votre structure" autocomplete="organization"></div>
      <fieldset class="field full"><legend>Votre besoin</legend><div class="chips">{besoins}</div></fieldset>
      <div class="field full"><label for="f-msg">Message *</label><textarea id="f-msg" name="message" rows="5" placeholder="Parlez-nous brièvement de votre projet" required></textarea></div>
      <div class="form-foot full">
        <label class="consent"><input type="checkbox" name="consent" required><span>J'accepte que {AGENCE} utilise ces informations pour me recontacter au sujet de ma demande.</span></label>
        <button class="btn" type="submit">Envoyer</button>
      </div>
      <p class="form-status full" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>"""


def empreinte(fichier):
    """Empreinte courte du contenu : change à chaque modification, ce qui force les navigateurs
    à recharger le CSS / JS malgré la mise en cache d'une semaine (cf. vercel.json)."""
    import hashlib
    return hashlib.sha1((OUT / fichier).read_bytes()).hexdigest()[:8]


def vignette(im):
    """Nom de la vignette de galerie (800 px de large) ; générée par optimiser_medias."""
    return im.rsplit(".", 1)[0] + "-800.webp"


def _webp(src, dst, largeur=None):
    """Convertit une image de media/ en WebP dans public/ (seulement si elle a changé)."""
    from PIL import Image
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im = im.convert("RGBA") if im.mode in ("RGBA", "LA", "P") else im.convert("RGB")
        if largeur and im.width > largeur:
            im = im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS)
        im.save(dst, "WEBP", quality=80, method=5)


def optimiser_medias(html):
    """Remplace chaque image de media/ par sa version WebP (générée au besoin) ;
    vidéos et SVG sont copiés tels quels. Les vignettes « -800.webp » partent de l'original."""
    import re, shutil

    def copie(src, dst):
        if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    def remplace(m):
        dossier, chemin = m.group(1), m.group(2)
        public = OUT / "assets/img" / dossier
        if chemin.endswith("-800.webp"):
            base = chemin[: -len("-800.webp")]
            orig = next((MEDIA / dossier).glob(base.replace("[", "[[]") + ".*"))
            _webp(orig, public / chemin, 800)
            return f"assets/img/{dossier}/{chemin}"
        if chemin.endswith((".mp4", ".svg")):
            copie(MEDIA / dossier / chemin, public / chemin)
            return f"assets/img/{dossier}/{chemin}"
        webp = chemin.rsplit(".", 1)[0] + ".webp"
        _webp(MEDIA / dossier / chemin, public / webp, 2000)
        return f"assets/img/{dossier}/{webp}"

    motif = r'assets/img/(works|clients/couleur)/([^"\'\s)]+?(?:-800\.webp|\.jpe?g|\.png|\.mp4|\.svg))'
    html = re.sub(motif, remplace, html)
    return html.replace("<img ", '<img decoding="async" ')


def page(fichier, titre, body, active="", classe="", retour=None):
    full_title = f"{titre} — {AGENCE}" if titre else f"{AGENCE} — {BASELINE}"
    html = f"""<!doctype html>
<html lang="fr" class="{classe}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{AGENCE}, {BASELINE.lower()} : {', '.join(t.lower() for _, t, _ in METIERS)}.">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=Geist+Mono:wght@400;500&family=Geist:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={empreinte("assets/css/style.css")}">
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <!-- Monochromie bordeaux : sombres → bordeaux profond, moyens → bordeaux clair, clairs → crème -->
  <filter id="da-tritone" color-interpolation-filters="sRGB">
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer>
      <feFuncR type="table" tableValues="0.165 0.420 0.988"/>
      <feFuncG type="table" tableValues="0 0.165 0.886"/>
      <feFuncB type="table" tableValues="0.059 0.243 0.820"/>
    </feComponentTransfer>
  </filter>
</svg>
{header(active, retour)}
<main>
{body}
</main>
{footer()}
<script src="assets/js/site.js?v={empreinte("assets/js/site.js")}" defer></script>
</body>
</html>
"""
    (OUT / fichier).write_text(optimiser_medias(html), encoding="utf-8")


# --- Pages -------------------------------------------------------------------
def accueil():
    metiers = "".join(f'<li><a href="prestation-{k}.html">{t}</a></li>' for k, t, _ in METIERS)
    # surface égale pour tous les logos : largeur ∝ √ratio
    clients = "".join(
        f'<li class="client" style="--m: url(../img/clients/{f}); --w: {r ** .5:.3f}; aspect-ratio: {r}">'
        f'<span class="sr">{n}</span></li>'
        for n, f, r in CLIENTS
    )
    body = f"""
<section class="chapter hero">
  <div class="wrap hero-grid">
    <div class="hero-brand">
      <h1 class="hero-lockup">{logo("picto", "hero-picto")}{logo("word", "hero-word")}<span class="sr">{AGENCE}</span></h1>
      <p class="mono hero-baseline">{BASELINE} pour marques qui veulent briller</p>
    </div>
    <ul class="hero-metiers display">{metiers}</ul>
  </div>
  <a class="hero-down" href="#references" aria-label="Défiler vers les références">↓</a>
</section>

<section class="chapter references" id="references">
  <div class="wrap">
    <h2 class="display section-title">Ils nous font confiance</h2>
    <p class="mono section-sub">Ils ont confié leur image à {AGENCE}</p>
    <ul class="clients">{clients}</ul>
    <a class="big-link display" href="works.html">Nos projets <span aria-hidden="true">↗</span></a>
  </div>
</section>
{contact_section()}
<section class="slogan">
  <p class="display fit">{SLOGAN}</p>
</section>"""
    page("index.html", "", body, classe="snap")


def prestations():
    cartes = "".join(f"""
    <a class="card-metier" id="{k}" href="prestation-{k}.html">
      <div class="card-visual v{i}">{logo("picto")}</div>
      <div class="card-band">
        <h2 class="display">{t}</h2>
        <p>{d}</p>
      </div>
    </a>""" for i, (k, t, d) in enumerate(METIERS))
    body = f"""
<section class="page">
  <div class="wrap">
    <h1 class="display page-title">Prestations</h1>
    <div class="cards-metiers">{cartes}
    </div>
  </div>
</section>"""
    page("prestations.html", "Prestations", body, "prestations")


def bloc_prestation(b, k):
    """Un chapitre de page prestation (types décrits dans contenu_prestations.py)."""
    t = b["type"]
    W = "assets/img/works/"
    if t == "titre":
        fond = b.get("fond", "creme")
        tag = f'<span class="tag tag-static">{METIER_NOM[k]}</span>' if b.get("tag") else ""
        l1 = f'<{"h1" if b.get("tag") else "p"} class="display pr-l1">{b["l1"]}</{"h1" if b.get("tag") else "p"}>'
        return f"""
<section class="chapter pr pr-{fond}">
  <div class="wrap pr-centre">{tag}{l1}<p class="display pr-l2">{b["l2"]}</p></div>
</section>"""
    if t == "test":
        visuels = {
            "geant": f'<div class="pr-geant" aria-hidden="true">{logo("picto")}</div>',
            "minuscule": f'<div class="pr-mini" aria-hidden="true">{logo("picto")}<span class="mono">16 px</span></div>',
            "ticket": f"""<div class="pr-ticket" aria-hidden="true">{logo("picto")}{logo("word")}
              <p class="mono">TICKET N° 0042<br>1 × IDENTITÉ VISUELLE<br>────────────<br>MERCI DE VOTRE VISITE</p></div>""",
            "eclair": f'<div class="pr-eclair" aria-hidden="true">{logo("picto")}<span class="mono">110 km/h</span></div>',
        }
        return f"""
<section class="chapter pr pr-test pr-test-{b["visuel"]}">
  {visuels[b["visuel"]]}
  <div class="wrap pr-test-txt">
    <p class="mono pr-num">Test {b["n"]} / 4</p>
    <p class="display pr-l2">{b["titre"]}</p>
    <p class="pr-detail">{b["texte"]}</p>
  </div>
</section>"""
    if t == "mur":
        logos = "".join(f'<li class="client" style="--m: url(../img/clients/{f}); --w: {r ** .5:.3f}; '
                        f'aspect-ratio: {r}"></li>' for f, r in b["logos"])
        return f"""
<section class="chapter pr pr-bordeaux pr-mur">
  <div class="wrap"><ul class="clients">{logos}</ul></div>
</section>"""
    if t == "chiffre":
        return f"""
<section class="chapter pr pr-creme pr-chiffre">
  <div class="wrap pr-centre">
    <p class="display pr-nombre">{b["nombre"]}</p>
    <p class="display pr-l1">{b["texte"]}</p>
    <p class="mono pr-source">Source : {b["source"]}</p>
  </div>
</section>"""
    if t == "temps":
        w, h = dimensions(b["img"])
        return f"""
<section class="chapter pr pr-creme pr-temps">
  <div class="wrap pr-split">
    <div>
      <p class="display pr-chrono">{b["t"]}</p>
      <p class="display pr-l2">{b["texte"]}</p>
      <p class="pr-detail">{b["detail"]}</p>
    </div>
    <figure class="photo visuel" style="--r: {w / h:.4f}"><img src="{W}{vignette(b["img"])}" alt="" loading="lazy" width="{w}" height="{h}"></figure>
  </div>
</section>"""
    if t == "bande":
        imgs = "".join(f'<img src="{W}{vignette(im)}" alt="" loading="lazy" {taille(im)}>' for im in b["images"])
        return f"""
<section class="pr pr-bande" aria-label="Quelques affiches">
  <div class="pr-defile">{imgs}{imgs}</div>
</section>"""
    if t == "horloge":
        fond = b.get("fond", "bordeaux")
        icone = '<span class="pr-rembobine" aria-hidden="true">◀◀</span>' if b.get("rembobine") else ""
        return f"""
<section class="chapter pr pr-{fond} pr-horloge">
  <div class="wrap pr-centre">
    {icone}
    <p class="display pr-heure">{b["heure"]}</p>
    <p class="display pr-l1">{b["texte"]}</p>
  </div>
</section>"""
    if t == "attente":
        return """
<section class="chapter pr pr-creme pr-attente">
  <div class="wrap pr-centre">
    <div class="phone pr-phone-vide" aria-hidden="true"><span class="pr-spinner"></span></div>
    <p class="mono pr-compteur" aria-hidden="true"><span>1</span> s… <span>2</span> s… <span>3</span> s…</p>
  </div>
</section>"""
    if t == "ecrans":
        tels = "".join(f'<div class="phone"><img src="{W}{im}" alt="" loading="lazy"></div>' for im in b["images"])
        return f"""
<section class="chapter pr pr-creme pr-ecrans">
  <div class="wrap pr-centre">
    <div class="pr-tels">{tels}</div>
    <p class="pr-detail">{b["texte"]}</p>
  </div>
</section>"""
    if t == "regard":
        return f"""
<section class="chapter pr pr-regard">
  <img class="pr-regard-img" src="{W}{b["img"]}" alt="" loading="lazy">
  <div class="wrap pr-regard-txt">
    <p class="display pr-vous">{b["vous"]}</p>
    <p class="display pr-nous">{b["nous"]}</p>
  </div>
</section>"""
    if t == "video":
        src = b["src"]
        return f"""
<section class="chapter pr pr-creme pr-video">
  <div class="wrap pr-split">
    <figure class="photo pr-video-cadre"><video src="{W}{src}" poster="{W}{src[:-4]}-poster.jpg" autoplay muted loop
      playsinline preload="metadata" aria-label="Coulisses d'un shooting"></video></figure>
    <p class="display pr-l2">{b["texte"]}</p>
  </div>
</section>"""
    if t == "final":
        return f"""
<section class="chapter pr pr-bordeaux">
  <div class="wrap pr-centre">
    <p class="display pr-l1">{b["question"]}</p>
    <p class="display pr-l2 pr-accent">{b["reponse"]}</p>
    <a class="btn" href="contact.html?besoin={k}">Parlons-en</a>
  </div>
</section>"""
    raise ValueError(f"type de bloc inconnu : {t}")


def prestation(k):
    nom = METIER_NOM[k]
    ch = [bloc_prestation(b, k) for b in PAGES[k]]
    projets = [p for p in PROJETS if p[0] == k and len(p) == 5][:4]
    if projets:
        cartes = "".join(carte(j, *p, titre_tag="h3") for j, p in enumerate(projets))
        ch.append(f"""
<section class="page fable-projets">
  <div class="wrap">
    <h2 class="display others-title">Nos projets en {nom.lower()}</h2>
    <div class="works">{cartes}
    </div>
    <nav class="others-nav mono"><a href="works.html">← Tous les projets</a></nav>
  </div>
</section>""")
    autres = "".join(f'<li><a class="display" href="prestation-{k2}.html">{t2} <span aria-hidden="true">↗</span></a></li>'
                     for k2, t2, _ in METIERS if k2 != k)
    ch.append(f"""
<section class="page fable-autres">
  <div class="wrap">
    <p class="mono fable-autres-titre">Voir nos autres prestations</p>
    <ul class="fable-liste">{autres}</ul>
  </div>
</section>""")
    page(f"prestation-{k}.html", nom, "".join(ch), "prestations", classe="snap", retour="prestations.html")


def carte(i, c, t, d, img=None, slug=None, titre_tag="h2"):
    """Carte projet (grille Works et « Autres projets »)."""
    a_logo = slug in LOGOS_PROJETS
    if a_logo:
        f, r, fond = LOGOS_PROJETS[slug]
        # largeur ∝ √ratio : même surface visuelle quel que soit le format du logo
        taille_logo = f"--w: {r ** .5:.3f}; aspect-ratio: {r}"
        visuel = (f'<span class="work-brand" style="background: {fond}" aria-hidden="true"></span>'
                  f'<span class="work-logo" style="--m: url(../img/clients/{f}); {taille_logo}" aria-hidden="true"></span>'
                  f'<img class="work-logo work-logo-color" src="assets/img/clients/couleur/{f}" alt="" '
                  f'style="{taille_logo}" loading="lazy">')
        img = None
    elif img:
        # 2e copie teintée par-dessus : elle s'efface au survol (fondu vers les vraies couleurs)
        visuel = (f'<img src="assets/img/works/{img}" alt="" loading="lazy">'
                  f'<img class="tint" src="assets/img/works/{img}" alt="" loading="lazy">')
    else:
        visuel = logo("picto")
    titre = f'<a href="projet-{slug}.html">{t} <span aria-hidden="true">→</span></a>' if slug else t
    return f"""
      <article class="work" data-cat="{c}">
        <div class="work-visual v{i % 4}{' has-img' if img else ''}{' has-logo' if a_logo else ''}">
          <span class="tag">{METIER_NOM[c]}</span>
          {visuel}
        </div>
        <{titre_tag} class="display">{titre}</{titre_tag}>
        <p class="mono{' en-cours' if d == 'En cours' else ''}">{d}</p>
      </article>"""


def works():
    filtres = '<button class="chip-btn" aria-pressed="true" data-filtre="tout">Tout</button>' + "".join(
        f'<button class="chip-btn" aria-pressed="false" data-filtre="{k}">{t}</button>' for k, t, _ in METIERS
    )
    cartes = "".join(carte(i, *p) for i, p in enumerate(PROJETS))
    body = f"""
<section class="page">
  <div class="wrap">
    <h1 class="display page-title">Nos projets</h1>
    <div class="filtres" role="group" aria-label="Filtrer par catégorie">{filtres}</div>
    <div class="works">{cartes}
    </div>
  </div>
</section>"""
    page("works.html", "Works", body, "works")


def dimensions(im):
    from PIL import Image
    with Image.open(MEDIA / "works" / im) as i:
        return i.width, i.height


def avant_apres(paire, titre):
    """Comparateur avant / après : les deux visuels superposés, une poignée révèle le nouveau."""
    if not paire:
        return ""
    avant, apres, legende = paire
    return f"""
<section class="chapter shot shot-compare">
  <div class="wrap shot-inner">
    <figure class="compare" style="--pos: 50%">
      <div class="compare-pane compare-avant"><img src="assets/img/works/{avant}" alt="{titre} — ancien logo"></div>
      <div class="compare-pane compare-apres"><img src="assets/img/works/{apres}" alt="{titre} — nouveau logo"></div>
      <span class="compare-label mono compare-label-avant">Avant</span>
      <span class="compare-label mono compare-label-apres">Après</span>
      <span class="compare-handle" aria-hidden="true"></span>
      <input class="compare-range" type="range" min="0" max="100" value="50" aria-label="Comparer l'ancien et le nouveau logo">
    </figure>
    <p class="display shot-caption">{legende}</p>
  </div>
</section>"""


def video_youtube(url, titre):
    """Film en grand, dans un cadre 16:9 : fichier .mp4 hébergé avec le site, ou YouTube (sans cookies).
    En tête de page pour un motion design ; après les visuels pour un projet de branding."""
    if not url:
        return ""
    if url.endswith(".mp4"):
        # fichier hébergé avec le site : lecture à la demande (le film a du son), aperçu fixe
        lecteur = (f'<video src="assets/img/works/{url}" poster="assets/img/works/{url[:-4]}-poster.jpg" '
                   f'controls playsinline preload="none" aria-label="{titre} — film"></video>')
    else:
        vid = url.rstrip("/").split("/")[-1].split("v=")[-1]
        lecteur = (f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0" title="{titre} — vidéo" '
                   f'loading="lazy" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>')
    return f"""
<section class="chapter shot shot-video">
  <div class="wrap shot-inner">
    <figure class="photo yt">
      {lecteur}
    </figure>
    <p class="display shot-caption">Le film</p>
  </div>
</section>"""


def taille(im):
    """width/height réels : la place est réservée avant le chargement (pas de saut de mise en page)."""
    from PIL import Image
    with Image.open(MEDIA / "works" / im) as i:
        return f'width="{i.width}" height="{i.height}"'


def galerie(images, titre, ligne=False, unite="photos"):
    """Série complète : mosaïque, ou une seule ligne qui défile à l'horizontale (ligne=True)."""
    if not images:
        return ""
    vignettes = "".join(
        f'<li><button class="gal-item" data-src="assets/img/works/{im}" aria-label="Agrandir le visuel {n}">'
        f'<img src="assets/img/works/{vignette(im)}" alt="{titre} — visuel {n}" loading="lazy" {taille(im)}></button></li>'
        for n, im in enumerate(images, 1))
    if ligne:
        grille = f"""<div class="gal-row-wrap">
      <ul class="gal-row" tabindex="0" aria-label="Série complète, défilement horizontal">{vignettes}</ul>
      <button class="gal-nav gal-nav-prev" aria-label="Visuels précédents">←</button>
      <button class="gal-nav gal-nav-next" aria-label="Visuels suivants">→</button>
    </div>"""
    else:
        grille = f'<ul class="gal-grid">{vignettes}</ul>'
    return f"""
<section class="page gallery">
  <div class="wrap">
    <h2 class="display section-title">La série <span class="gal-count mono">{len(images)} {unite}</span></h2>
    {grille}
  </div>
  <dialog class="lightbox" aria-label="Visionneuse">
    <img alt="">
    <button class="lb-close" aria-label="Fermer">×</button>
    <button class="lb-prev" aria-label="Photo précédente">←</button>
    <button class="lb-next" aria-label="Photo suivante">→</button>
    <p class="lb-count mono"></p>
  </dialog>
</section>"""


def etude(slug):
    e = ETUDES[slug]
    i, (cat, titre, date, _, _) = next((i, p) for i, p in enumerate(PROJETS) if p[4:5] == (slug,))
    domaine = e["url"].split("//")[1].strip("/").removeprefix("www.") if "url" in e else ""
    bouton = (f'<a class="btn-outline" href="{e["url"]}" target="_blank" rel="noopener">'
              f'Voir le site en ligne <span aria-hidden="true">↗</span></a>') if "url" in e else ""
    services = "".join(f"<li>{x}</li>" for x in e["services"])
    etapes = "".join(f"""
      <li class="step">
        <span class="step-num mono">{n:02d}</span>
        <h3 class="display">{t}</h3>
        <p>{d}</p>
      </li>""" for n, (t, d) in enumerate(e["processus"], 1))

    def capture(img, legende, kind):
        if img.endswith(".mp4"):  # vidéo : même cadre que les photos (photo-v / photo-h)
            poster = img.replace(".mp4", "-poster.jpg")
            cadre = (f'<figure class="photo"><video src="assets/img/works/{img}" poster="assets/img/works/{poster}" '
                     f'autoplay muted loop playsinline preload="metadata" aria-label="{titre}, coulisses du shooting"></video></figure>')
        elif kind == "visuel":  # affiche, logo, visuel : proportions d'origine, jamais rogné
            w, h = dimensions(img)
            kind = "visuel-h" if w / h > 1.15 else "visuel-v"
            cadre = (f'<figure class="photo visuel" style="--r: {w / h:.4f}"><img src="assets/img/works/{img}" '
                     f'alt="{titre}" loading="lazy" width="{w}" height="{h}"></figure>')
        elif kind.startswith("photo"):
            cadre = f'<figure class="photo"><img src="assets/img/works/{img}" alt="{titre}, photographie" loading="lazy"></figure>'
        elif kind == "mobile":
            cadre = f'<div class="phone"><img src="assets/img/works/{img}" alt="{titre}, vue mobile" loading="lazy"></div>'
        else:
            cadre = f"""<div class="browser">
          <div class="browser-bar"><span></span><span></span><span></span><p class="mono">{domaine}</p></div>
          <img src="assets/img/works/{img}" alt="{titre}, capture d'écran" loading="lazy">
        </div>"""
        return f"""
<section class="chapter shot shot-{kind}">
  <div class="wrap shot-inner">
    {cadre}
    <p class="display shot-caption">{legende}</p>
  </div>
</section>"""

    # uniquement des projets qui ont leur propre étude de cas : même client d'abord, puis même catégorie
    autres = sorted((p for p in PROJETS if len(p) == 5 and p[4] != slug),
                    key=lambda p: (ETUDES[p[4]]["client"] != e["client"], p[0] != cat))[:2]
    autres_html = "".join(carte(j, *p, titre_tag="h3") for j, p in enumerate(autres, 1))
    body = f"""
<section class="chapter case-hero">
  {logo("picto", "case-bg")}
  <div class="wrap case-hero-inner">
    <span class="tag tag-static">{METIER_NOM[cat]}</span>
    <h1 class="display case-title">{titre}</h1>
    <p class="case-sub display">{e["sous_titre"]}</p>
    <p class="case-intro">{e["intro"]}</p>
    {bouton}
    <dl class="case-meta">
      <div><dt>Destiné à</dt><dd>{e["client"]}</dd></div>
      <div><dt>Réalisé par</dt><dd>{AGENCE}</dd></div>
      <div><dt>Date</dt><dd{' class="en-cours"' if date == 'En cours' else ''}>{date}</dd></div>
    </dl>
  </div>
  <a class="hero-down" href="#processus" aria-label="Défiler vers le processus">↓</a>
</section>

<section class="chapter process" id="processus">
  <div class="wrap">
    <h2 class="display section-title">Le processus</h2>
    <ul class="services">{services}</ul>
    <ol class="steps">{etapes}
    </ol>
  </div>
</section>
{avant_apres(e.get("avant_apres"), titre)}
{video_youtube(e.get("video"), titre) if cat != "branding" else ""}
{"".join(capture(*c) for c in e["captures"])}
{video_youtube(e.get("video"), titre) if cat == "branding" else ""}
{galerie(e.get("galerie"), titre, e.get("galerie_ligne", False), "photos" if cat == "photo" else "visuels")}
<section class="page others">
  <div class="wrap">
    <h2 class="display others-title">Autres projets</h2>
    <div class="works">{autres_html}
    </div>
    <nav class="others-nav mono">
      <a href="works.html">← Tous les projets</a>
      <a href="contact.html">Un projet similaire ? Parlons-en →</a>
    </nav>
  </div>
</section>"""
    page(f"projet-{slug}.html", titre, body, "works", retour="works.html")


def contact():
    page("contact.html", "Contact", contact_section("h1"), "contact")


def legal():
    blocs = [
        ("mentions", "Mentions légales", f"Éditeur du site : {AGENCE}, société en cours d'immatriculation. Contact : {EMAIL}. Hébergeur : Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis."),
        ("confidentialite", "Politique de confidentialité", "Les informations envoyées via le formulaire de contact servent uniquement à répondre à votre demande. Elles ne sont ni revendues ni transmises à des tiers. Texte à compléter."),
        ("cookies", "Gestion des cookies", "Ce site n'utilise pas de cookies de suivi. Texte à compléter."),
        ("cgu", "Conditions générales d'utilisation", "Texte à compléter."),
    ]
    contenu = "".join(f'<section id="{i}"><h2 class="display">{t}</h2><p>{p}</p></section>' for i, t, p in blocs)
    body = f"""
<section class="page legal">
  <div class="wrap narrow">
    <h1 class="display page-title">Légal</h1>
    {contenu}
  </div>
</section>"""
    page("mentions-legales.html", "Mentions légales", body)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    accueil(); prestations(); works(); contact(); legal()
    for k in PAGES:
        prestation(k)
    for slug in ETUDES:
        etude(slug)
    print("ok →", OUT)
