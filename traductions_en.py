"""Version anglaise du site : pages générées dans public/en/ à partir des pages françaises.

Chaque texte visible (et alt, aria-label, title, placeholder, meta description) est cherché ici
tel qu'il apparaît en français, espaces normalisés. Un texte absent est laissé tel quel (noms
propres, marques…) ; le build liste ceux qui manquent pour les compléter.

Les textes générés en série (« Raffiné — visuel 12 », « Gomu — Frostbird »…) sont traduits par
les règles de MOTIFS, en traduisant au passage la partie variable.
"""

MOTIFS = [
    # (expression régulière sur le texte français, modèle anglais ; {0} = partie variable traduite)
    (r"^(.+) — Frostbird$", "{0} — Frostbird"),
    (r"^(.+) — visuel (\d+)$", "{0} — visual {1}"),
    (r"^Agrandir le visuel (\d+)$", "Enlarge visual {0}"),
    (r"^(\d+) visuels$", "{0} visuals"),
    (r"^(\d+) photos$", "{0} photos"),
    (r"^(.+), capture d'écran$", "{0}, screenshot"),
    (r"^(.+), vue mobile$", "{0}, mobile view"),
    (r"^(.+), photographie$", "{0}, photography"),
    (r"^(.+), coulisses du shooting$", "{0}, behind the scenes of the shoot"),
    (r"^(.+) — ancien logo$", "{0} — former logo"),
    (r"^(.+) — nouveau logo$", "{0} — new logo"),
    (r"^(.+) — vidéo$", "{0} — video"),
    (r"^(.+) — film$", "{0} — film"),
    (r"^Test (\d) / 4$", "Test {0} / 4"),
]

EN = {
    # ------------------------------------------------------------------ navigation, pied de page
    "Accueil": "Home",
    "Prestations": "Services",
    "Contacts": "Contact",
    "Contact": "Contact",
    "Retour": "Back",
    "Ouvrir le menu": "Open menu",
    "Langue": "Language",
    "Frostbird — accueil": "Frostbird — home",
    "Frostbird — Agence créative": "Frostbird — Creative agency",
    "Frostbird, agence créative : branding, design graphique, web & apps, photographie.":
        "Frostbird, creative agency: branding, graphic design, web & apps, photography.",
    "Navigation": "Navigation",
    "Références": "Clients",
    "Légal": "Legal",
    "Mentions légales": "Legal notice",
    "Politique de confidentialité": "Privacy policy",
    "Gestion des cookies": "Cookie policy",
    "CGU": "Terms of use",
    "Éditeur": "Publisher",
    "Société en cours d'immatriculation": "Company being registered",
    "© 2026 Frostbird — Tous droits réservés.": "© 2026 Frostbird — All rights reserved.",

    # ------------------------------------------------------------------ métiers
    "Branding": "Branding",
    "Design graphique": "Graphic design",
    "Web & Apps": "Web & Apps",
    "Photographie": "Photography",
    "Logos, identités visuelles, chartes graphiques. Des marques qu'on reconnaît de loin.":
        "Logos, visual identities, brand guidelines. Brands you can spot from a mile away.",
    "Print, affiches, réseaux sociaux, packaging. Tout ce qui doit se voir.":
        "Print, posters, social media, packaging. Everything that needs to be seen.",
    "Sites vitrines, e-commerce, applications. Rapides, beaux, faciles à faire vivre.":
        "Showcase sites, e-commerce, apps. Fast, beautiful, easy to keep alive.",
    "Portraits, produits, reportages, événements. Des images qui racontent votre marque.":
        "Portraits, products, reportage, events. Images that tell your brand's story.",

    # ------------------------------------------------------------------ accueil
    "Agence créative pour marques qui veulent briller": "Creative agency for brands that want to shine",
    "Défiler vers les références": "Scroll to our clients",
    "Ils nous font confiance": "They trust us",
    "Ils ont confié leur image à Frostbird": "They trusted Frostbird with their image",
    "Nos projets": "Our work",
    "On en parle ?": "Shall we talk?",
    "Born to fly": "Born to fly",

    # ------------------------------------------------------------------ formulaire de contact
    "Nom *": "Name *",
    "Votre nom": "Your name",
    "Email *": "Email *",
    "vous@entreprise.com": "you@company.com",
    "Téléphone": "Phone",
    "Entreprise": "Company",
    "Nom de votre structure": "Your company name",
    "Votre besoin": "What you need",
    "Message *": "Message *",
    "Parlez-nous brièvement de votre projet": "Tell us briefly about your project",
    "J'accepte que Frostbird utilise ces informations pour me recontacter au sujet de ma demande.":
        "I agree that Frostbird may use this information to get back to me about my request.",
    "Envoyer": "Send",

    # ------------------------------------------------------------------ works
    "Works": "Works",
    "Tout": "All",
    "Filtrer par catégorie": "Filter by category",
    "En cours": "In progress",
    "Juillet 2026": "July 2026",
    "Septembre 2026": "September 2026",

    # ------------------------------------------------------------------ pages projet (commun)
    "Destiné à": "Client",
    "Réalisé par": "Made by",
    "Date": "Date",
    "Voir le site en ligne": "Visit the live site",
    "Défiler vers le processus": "Scroll to the process",
    "Le processus": "The process",
    "La série": "The series",
    "Le film": "The film",
    "Autres projets": "More projects",
    "← Tous les projets": "← All projects",
    "Un projet similaire ? Parlons-en →": "A similar project? Let's talk →",
    "Série complète, défilement horizontal": "Full series, horizontal scroll",
    "Visuels précédents": "Previous visuals",
    "Visuels suivants": "Next visuals",
    "Visionneuse": "Viewer",
    "Fermer": "Close",
    "Photo précédente": "Previous photo",
    "Photo suivante": "Next photo",
    "Avant": "Before",
    "Après": "After",
    "Comparer l'ancien et le nouveau logo": "Compare the former and the new logo",

    # étapes et prestations récurrentes
    "Brief": "Brief",
    "Recherches": "Research",
    "Création": "Design",
    "Déclinaisons": "Variations",
    "Déclinaisons couleur": "Colour variations",
    "Direction artistique": "Art direction",
    "Développement": "Development",
    "Mise en ligne": "Launch",
    "Comprendre": "Understanding",
    "Concept": "Concept",
    "Maquettes": "Mock-ups",
    "Tests": "Testing",
    "Idée": "Idea",
    "Message": "Message",
    "Composition": "Composition",
    "Finalisation": "Finishing",
    "Storyboard": "Storyboard",
    "Animation": "Animation",
    "Son": "Sound",
    "Diffusion": "Delivery",
    "Repérage": "Scouting",
    "Shooting": "Shoot",
    "Retouche": "Retouching",
    "Retouche & livraison": "Retouching & delivery",
    "Mise en scène": "Set design",
    "Shooting produit": "Product shoot",
    "Bord de terrain": "Pitchside",
    "Sélection & retouche": "Selection & retouching",
    "Photographie": "Photography",
    "Mise en page": "Layout",
    "Impression": "Printing",
    "Audit & reprise": "Audit & takeover",
    "Positionnement": "Positioning",
    "Logo & identité": "Logo & identity",
    "Affiche": "Poster",
    "Motion design": "Motion design",
    "Création de logo": "Logo design",
    "Refonte de logo": "Logo redesign",
    "Identité visuelle": "Visual identity",
    "Naming": "Naming",
    "Palette de couleurs": "Colour palette",
    "Illustration": "Illustration",
    "Mise en situation": "Mock-ups",
    "Lettrage sur mesure": "Custom lettering",
    "Webdesign": "Web design",
    "Hébergement": "Hosting",
    "Concept & UX": "Concept & UX",
    "UI design": "UI design",
    "Application iOS & Android": "iOS & Android app",
    "Back-end & hébergement": "Back-end & hosting",
    "Campagne d'affichage": "Poster campaign",
    "Campagnes d'affichage": "Poster campaigns",
    "Packaging": "Packaging",
    "Menu": "Menu",
    "Musique": "Music",
    "Photographie culinaire": "Food photography",
    "Photographie produit": "Product photography",
    "Photographie sportive": "Sports photography",
    "Stylisme culinaire": "Food styling",
    "Réseaux sociaux": "Social media",
    "Visuels réseaux sociaux": "Social media visuals",

    # ------------------------------------------------------------------ titres de projets
    "Application Cupidex": "Cupidex app",
    "Site de lancement Cupidex": "Cupidex launch site",
    "Portfolio de Paul Hivert": "Paul Hivert's portfolio",
    "Birdz — menu": "Birdz — menu",
    "Chikin Bang — affiches": "Chikin Bang — posters",
    "Chikin Bang — packaging": "Chikin Bang — packaging",
    "Gomu — affiches": "Gomu — posters",
    "Deezer — motion design": "Deezer — motion design",
    "Championnat de France": "French league",
    "Championnat National": "National league",
    "Coulisses d'un shooting": "Behind the scenes of a shoot",
    "Quelques affiches": "A few posters",

    # clients
    "Spike (projet de fin d'études)": "Spike (graduation project)",
    "Création personnelle": "Personal project",
    "Le Somar": "Le Somar",

    # ------------------------------------------------------------------ Cupidex (app)
    "Une application de rencontre où chaque rencontre rejoint une collection":
        "A dating app where every match joins a collection",
    "Cupidex reprend les codes des applications de swipe pour les détourner vers un objectif de collection : chaque rencontre remplit un Cupidex personnel, classé par la première lettre du prénom, avec des lettres rares, des badges qui évoluent et des séries à tenir. Frostbird conçoit l'application de bout en bout : concept, design, application iOS et Android, et le serveur qui la fait tourner. Le projet est en cours : l'application est en phase de tests avant sa sortie sur les stores.":
        "Cupidex takes the codes of swipe apps and turns them into a collection game: every match fills a personal Cupidex, sorted by the first letter of their first name, with rare letters, evolving badges and streaks to keep. Frostbird designs the app end to end: concept, design, iOS and Android app, and the server that runs it. The project is ongoing: the app is being tested before it hits the stores.",
    "Détourner le swipe vers la collection : une lettre par prénom, des lettres rares, des badges du match jusqu'à la relation.":
        "Turning the swipe into a collection: one letter per first name, rare letters, badges from the first match to a relationship.",
    "Un prototype cliquable de tous les écrans, puis une direction « verre liquide » en violet et rose.":
        "A clickable prototype of every screen, then a purple-and-pink “liquid glass” direction.",
    "Une application React Native pour iOS et Android, et une API Spring Boot : profils, matchs, messagerie, collection, modération.":
        "A React Native app for iOS and Android, and a Spring Boot API: profiles, matches, messaging, collection, moderation.",
    "Une nouvelle version testée chaque semaine sur un serveur de recette, jusqu'au lancement sur les stores.":
        "A new version tested every week on a staging server, all the way to the store launch.",
    "« Collectionne l'amour » : l'application donne le ton dès l'ouverture.":
        "“Collect love”: the app sets the tone from the very first screen.",
    "Le swipe, version Cupidex : l'essentiel d'un profil en un coup d'œil.":
        "The swipe, Cupidex style: the essentials of a profile at a glance.",
    "Le cœur de l'application : une collection de lettres, des plus courantes aux plus rares.":
        "The heart of the app: a collection of letters, from the most common to the rarest.",
    "L'historique : toutes les rencontres sur une frise, de la plus récente à la plus ancienne.":
        "The history: every match on a timeline, from the most recent to the oldest.",
    "Les badges : régularité, lettres, pays… tout ce qu'il reste à décrocher, avec l'avancée de chacun.":
        "The badges: streaks, letters, countries… everything left to unlock, with your progress on each.",
    "La carte des conquêtes : un globe où chaque pays rencontré s'allume.":
        "The conquest map: a globe where every country you've met lights up.",
    "Ceux qui t'ont liké, mis en avant selon les lettres qui te manquent.":
        "The people who liked you, ranked by the letters you're still missing.",

    # ------------------------------------------------------------------ Cupidex (site)
    "Une page d'attente pour faire monter l'envie avant la sortie de l'application":
        "A waiting page to build anticipation before the app comes out",
    "Cupidex est une application de rencontre qui transforme chaque rencontre en entrée d'une collection : une lettre par prénom, un badge qui évolue au fil de l'histoire. Avant la sortie sur les stores, il fallait une vitrine pour présenter le concept et recueillir les premiers inscrits.":
        "Cupidex is a dating app that turns every match into an entry in a collection: one letter per first name, a badge that evolves as the story unfolds. Before the store release, it needed a showcase to present the concept and gather its first sign-ups.",
    "À qui parle l'application, ce qui la rend différente, et ce qu'un visiteur doit retenir en dix secondes.":
        "Who the app speaks to, what makes it different, and what a visitor should remember in ten seconds.",
    "Prolongement de la charte Cupidex : dégradés violet-rose, titres italiques très gras, logo cœur-flèche. Un ton direct, en tutoiement.":
        "An extension of the Cupidex brand: purple-to-pink gradients, heavy italic headlines, the heart-and-arrow logo. A direct, friendly tone.",
    "Une page statique unique, sans aucune dépendance : très légère, rapide à charger, simple à faire évoluer jusqu'au lancement.":
        "A single static page with no dependencies: very light, fast to load, easy to evolve until launch.",
    "Nom de domaine cupidex.fr, hébergement sur un serveur dédié en HTTPS, publication en un clic depuis GitHub.":
        "The cupidex.fr domain, hosting on a dedicated server over HTTPS, one-click publishing from GitHub.",
    "Le message tient en une phrase : Cupidex arrive, et voilà pourquoi tu vas l'aimer.":
        "The message fits in one sentence: Cupidex is coming, and here's why you'll love it.",
    "Le concept expliqué en quatre cartes : lettres à collectionner, badges, séries, contrôle.":
        "The concept explained in four cards: letters to collect, badges, streaks, control.",
    "Pensé d'abord pour le téléphone, là où l'application vivra.":
        "Designed for the phone first, where the app will live.",

    # ------------------------------------------------------------------ Portfolio Paul Hivert
    "Un écrin sombre et sur mesure pour le portfolio d'un directeur artistique":
        "A dark, made-to-measure showcase for an art director's portfolio",
    "Paul Hivert est directeur artistique et chef de projets : logos, affiches, motion design, photographie, print. Son portfolio devait présenter une trentaine de projets sans jamais leur voler la vedette, et montrer son exigence graphique dès la première seconde.":
        "Paul Hivert is an art director and project manager: logos, posters, motion design, photography, print. His portfolio had to present some thirty projects without ever stealing their thunder, and show his design standards from the very first second.",
    "Récupération du code et du nom de domaine, puis inventaire complet des contenus : 6 catégories, 29 pages projets.":
        "Recovering the code and the domain name, then a full content inventory: 6 categories, 29 project pages.",
    "Une ambiance « brume » bleu-charbon avec du grain, et un lettrage géométrique dessiné sur mesure pour le titre.":
        "A blue-charcoal “mist” mood with grain, and custom geometric lettering for the title.",
    "Next.js et TypeScript : pages catégories, pages projets, visionneuse, vidéos, menu mobile. Rapide et entièrement responsive.":
        "Next.js and TypeScript: category pages, project pages, viewer, videos, mobile menu. Fast and fully responsive.",
    "Déploiement sur Vercel, reprise du domaine paulhivert.com, redirections et HTTPS.":
        "Deployment on Vercel, taking back the paulhivert.com domain, redirects and HTTPS.",
    "Un accueil sobre : un nom, un métier, et l'envie de faire défiler.":
        "A restrained home page: a name, a trade, and the urge to scroll.",
    "Chaque catégorie a sa page, avec les projets présentés en grand format.":
        "Each category has its own page, with projects shown large.",
    "Les visuels prennent toute la place : le site s'efface derrière le travail.":
        "The visuals take up all the space: the site steps back behind the work.",
    "Sur mobile, la même ambiance, sans compromis.": "On mobile, the same mood, no compromise.",

    # ------------------------------------------------------------------ Raffiné
    "Capturer l'ambiance d'un restaurant premium, de la cuisine jusqu'à l'assiette":
        "Capturing the atmosphere of a premium restaurant, from the kitchen to the plate",
    "Raffiné est un restaurant premium qui cuisine de très bons produits dans un lieu visuellement superbe. Les photos devaient représenter le restaurant tel qu'il est et nourrir la belle image qu'il s'est construite.":
        "Raffiné is a premium restaurant cooking excellent produce in a visually stunning space. The photos had to show the restaurant as it really is and feed the fine image it has built.",
    "Visite du restaurant pendant le service pour repérer les lumières, les matières et les plats signatures.":
        "Visiting the restaurant during service to scout the light, the textures and the signature dishes.",
    "Une image chaude et feutrée, fidèle au lieu : lumière basse, fonds sombres, reflets dorés.":
        "A warm, hushed look, true to the place: low light, dark backgrounds, golden glints.",
    "Une séance en plein service : plats, cocktails, cuisine et équipe, photographiés sur le vif.":
        "A shoot in the middle of service: dishes, cocktails, kitchen and team, captured on the fly.",
    "Sélection, étalonnage homogène de toute la série et exports pour le site, les réseaux et l'imprimé.":
        "Selection, consistent colour grading across the series, and exports for the website, social media and print.",
    "Lumière basse, flammes, matières : on photographie l'ambiance autant que l'assiette.":
        "Low light, flames, textures: we shoot the atmosphere as much as the plate.",
    "Le lieu fait partie du récit : marbre éclairé, lumière dorée, l'équipe prête pour le service.":
        "The place is part of the story: glowing marble, golden light, the team ready for service.",
    "Au bar aussi, chaque geste est mis en scène.": "At the bar too, every gesture is staged.",

    # ------------------------------------------------------------------ Birdz (photo)
    "Birdz Hot Chicken": "Birdz Hot Chicken",
    "Un shooting produit complet avant l'ouverture, pour les menus, les visuels et les réseaux":
        "A full product shoot before opening, for menus, visuals and social media",
    "Avant son ouverture, Birdz avait besoin de photos de toute sa gamme de poulet façon Nashville pour ses menus, ses visuels et ses réseaux sociaux. Voici une partie des images réalisées lors du shooting.":
        "Before opening, Birdz needed photos of its whole Nashville-style chicken range for its menus, visuals and social media. Here are some of the images from the shoot.",
    "Lister toute la gamme à photographier avant l'ouverture : tenders, burgers, sandwichs, accompagnements, menus.":
        "Listing the whole range to shoot before opening: tenders, burgers, sandwiches, sides, combos.",
    "Un décor aux couleurs de la marque : carrelage blanc, packagings bleus, et le rouge du poulet Nashville en vedette.":
        "A set in the brand's colours: white tiles, blue packaging, and the red of Nashville chicken in the spotlight.",
    "Chaque produit sous plusieurs angles, du plan d'ensemble au gros plan qui donne faim.":
        "Every product from several angles, from the wide shot to the close-up that makes you hungry.",
    "Des images prêtes pour les menus, l'affichage en boutique et les réseaux sociaux.":
        "Images ready for menus, in-store displays and social media.",
    "Toute la gamme réunie : une seule image pour présenter la carte.":
        "The whole range together: one image to present the menu.",
    "Le rouge Nashville en vedette, le bleu Birdz en écrin.":
        "Nashville red in the spotlight, Birdz blue as the setting.",
    "Des gros plans pensés pour donner faim, du menu jusqu'aux réseaux.":
        "Close-ups designed to make you hungry, from the menu to social media.",
    "L'envers du décor : la table dressée, les produits en place, juste avant le déclic.":
        "Behind the scenes: the table set, the products in place, just before the shutter clicks.",

    # ------------------------------------------------------------------ Championnat National (photo)
    "Aïman & Ilan": "Aïman & Ilan",
    "Photographier deux espoirs du football en bord de terrain, match après match":
        "Photographing two football prospects from the touchline, match after match",
    "Aïman et Ilan jouent tous les deux en U19 National. Avec la possibilité de signer un contrat professionnel, leur image doit être soignée, et cela commence par la photographie en bord de terrain : on les photographie pendant leurs matchs, puis on traite les images pour leurs réseaux.":
        "Aïman and Ilan both play in the U19 national league. With a professional contract within reach, their image has to be polished, and it starts with pitchside photography: we shoot them during their matches, then edit the images for their social media.",
    "Comprendre l'enjeu : deux joueurs U19 National qui doivent soigner leur image avant un possible contrat pro.":
        "Understanding what's at stake: two U19 national league players who need to polish their image before a possible pro contract.",
    "Présence à leurs matchs pour capter l'action, les gestes techniques et les moments de concentration.":
        "Being at their matches to catch the action, the technique and the moments of focus.",
    "Tri des meilleures images et retouche cohérente d'un match à l'autre, pour une image reconnaissable.":
        "Picking the best shots and retouching them consistently from one match to the next, for a recognisable look.",
    "Des formats prêts pour leurs réseaux, livrés rapidement après chaque rencontre.":
        "Formats ready for their social media, delivered quickly after each match.",
    "Le dos, le numéro, le ciel : une image qui raconte le joueur avant le match.":
        "The back, the number, the sky: an image that tells the player's story before the match.",
    "L'action saisie au bon moment, au ras du terrain.": "The action caught at the right moment, at pitch level.",
    "Des portraits épurés, pensés pour leurs réseaux.": "Clean portraits, designed for their social media.",

    # ------------------------------------------------------------------ Atlantic Bateaux
    "Atlantic Bateaux": "Atlantic Bateaux",
    "Remettre à neuf un logo vieux de quinze ans, sans perdre ce qui faisait son histoire":
        "Refreshing a fifteen-year-old logo without losing what made its story",
    "Atlantic Bateaux est une entreprise du nautisme installée à Piriac. Son logo avait quinze ans : il fallait le moderniser tout en gardant le dessin du bateau de l'ancienne version, repensé plus simplement et décliné sur plusieurs supports.":
        "Atlantic Bateaux is a boating company based in Piriac. Its logo was fifteen years old: it needed modernising while keeping the boat drawing from the old version, rethought more simply and rolled out across several media.",
    "Comprendre l'histoire de l'entreprise et ce que l'ancien logo représentait pour elle.":
        "Understanding the company's history and what the old logo meant to it.",
    "Garder le bateau comme fil conducteur et chercher une forme plus épurée, lisible de loin.":
        "Keeping the boat as the common thread and looking for a cleaner shape, readable from afar.",
    "Un pictogramme net associé à un nom en capitales solides, pensé pour la signalétique.":
        "A crisp pictogram paired with a name in solid capitals, designed for signage.",
    "Versions noir, blanc et argent pour tous les fonds et tous les supports.":
        "Black, white and silver versions for every background and every medium.",
    "Le bateau de l'ancien logo, redessiné en un seul geste.": "The boat from the old logo, redrawn in a single stroke.",
    "Une version argent pour les supports haut de gamme.": "A silver version for premium media.",
    "Quinze ans d'écart : le bateau est resté, tout le reste a été simplifié.":
        "Fifteen years apart: the boat stayed, everything else was simplified.",

    # ------------------------------------------------------------------ Spike
    "Une marque de football engagée, du logo à la campagne de lancement":
        "A committed football brand, from the logo to the launch campaign",
    "Spike est une marque créée de toutes pièces pour un projet de fin d'études en design graphique : un équipementier sportif, centré sur le football, qui fabrique ses produits à partir de plastique recyclé. Le projet couvre toute la marque : le nom, le logo, l'identité visuelle, puis une campagne de lancement avec une affiche et un motion design.":
        "Spike is a brand created from scratch for a graphic design graduation project: a sportswear maker, focused on football, that makes its products from recycled plastic. The project covers the whole brand: the name, the logo, the visual identity, then a launch campaign with a poster and a motion design film.",
    "Un équipementier de football qui donne une seconde vie au plastique retrouvé dans l'océan.":
        "A football kit maker giving a second life to plastic recovered from the ocean.",
    "Un S en deux courbes qui se répondent : le mouvement du jeu et la boucle du recyclage.":
        "An S made of two curves answering each other: the movement of the game and the recycling loop.",
    "Une chaussure qui se noie, pour faire ressentir le poids du plastique et le sens de la marque.":
        "A drowning boot, to make you feel the weight of plastic and what the brand stands for.",
    "Un film qui suit la matière, d'une bouteille dans la mer jusqu'à la chaussure finie.":
        "A film that follows the material, from a bottle in the sea to the finished boot.",
    "Un S en deux courbes : le mouvement du jeu et la boucle du recyclage.":
        "An S in two curves: the movement of the game and the recycling loop.",
    "La marque en situation, sur les produits.": "The brand in context, on the products.",
    "L'affiche de lancement : les dernières bulles d'air d'une chaussure qui se noie.":
        "The launch poster: the last air bubbles of a drowning boot.",
    "Le motion design : tout commence par une bouteille dans la mer.":
        "The motion design: it all starts with a bottle in the sea.",

    # ------------------------------------------------------------------ Rooster
    "Une marque de poulet braisé qui assume un virage à 180 degrés":
        "A rotisserie chicken brand that owns its U-turn",
    "Rooster est une marque de restaurants de poulet braisé. L'objectif : une identité visuelle forte, qui sorte des codes classiques du poulet (les couleurs chaudes) et assume pleinement ce changement de direction.":
        "Rooster is a rotisserie chicken restaurant brand. The goal: a strong visual identity that breaks away from the usual chicken codes (warm colours) and fully owns this change of direction.",
    "Repérer les codes du secteur, pour mieux s'en éloigner.": "Spotting the industry's codes, the better to move away from them.",
    "Un violet électrique à la place des rouges et des jaunes attendus.": "Electric purple instead of the expected reds and yellows.",
    "Un nom en capitales massives, avec un S en forme de flamme pour le braisé.":
        "A name in massive capitals, with a flame-shaped S for the grill.",
    "Logotype, pictogramme et versions ton sur ton pour tous les supports.":
        "Logotype, pictogram and tone-on-tone versions for every medium.",
    "Le violet remplace les couleurs chaudes : on ne confond pas Rooster.":
        "Purple replaces the warm colours: you can't mistake Rooster.",
    "Le S-flamme fonctionne aussi seul, comme pictogramme.": "The flame S also works on its own, as a pictogram.",

    # ------------------------------------------------------------------ Happy Propaganda
    "L'identité d'une agence de communication, avec un œil et un cœur dedans":
        "The identity of a communications agency, with an eye and a heart inside",
    "Happy Propaganda est une agence de communication qui voulait une identité visuelle forte et assumée. Sa demande tenait en une phrase : un œil, et un cœur dedans.":
        "Happy Propaganda is a communications agency that wanted a strong, confident visual identity. Its brief fitted in one sentence: an eye, with a heart inside.",
    "Partir de l'image voulue par l'agence : un œil qui regarde, un cœur qui ressent.":
        "Starting from the image the agency had in mind: an eye that looks, a heart that feels.",
    "Un trait volontairement brut, presque dessiné à la main, loin des logos trop lisses.":
        "A deliberately raw line, almost hand-drawn, far from overly polished logos.",
    "Un œil cornu qui abrite un cœur, et un mot « happy » au tracé libre.":
        "A horned eye sheltering a heart, and a free-hand “happy”.",
    "Rouge, sombre, blanc et monochrome : la même énergie sur chaque fond.":
        "Red, dark, white and monochrome: the same energy on every background.",
    "Un œil, un cœur dedans : la demande tenait en une phrase.": "An eye, a heart inside: the brief fitted in one sentence.",
    "Le rouge, couleur principale de l'agence.": "Red, the agency's main colour.",

    # ------------------------------------------------------------------ First Touch
    "Un logo stable et dynamique pour une agence de joueurs et joueuses de football":
        "A steady yet dynamic logo for an agency representing football players",
    "First Touch est une agence qui accompagne des joueurs et joueuses de football. Elle voulait un logo stable et dynamique, avec les codes d'un logo de sport, décliné en deux versions : une claire et simple, une plus travaillée.":
        "First Touch is an agency that represents football players, men and women. It wanted a steady yet dynamic logo with the codes of a sports logo, in two versions: one light and simple, one more elaborate.",
    "Comprendre le métier d'agent et les attentes des joueurs accompagnés.":
        "Understanding what an agent does and what the players they represent expect.",
    "Des initiales imbriquées et une inclinaison qui évoque la vitesse.": "Interlocking initials and a slant that suggests speed.",
    "Un monogramme FT géométrique, solide comme un écusson.": "A geometric FT monogram, as solid as a crest.",
    "Une version claire et sobre, une version en dégradé pour les réseaux.":
        "A light, understated version, and a gradient version for social media.",
    "La version travaillée, en dégradé, pour les réseaux.": "The elaborate gradient version, for social media.",
    "La version claire et simple, pour les documents de l'agence.": "The light, simple version, for the agency's documents.",

    # ------------------------------------------------------------------ Le Charles
    "Un cafard et une licorne pour le logo d'un nouveau bar-restaurant nantais":
        "A cockroach and a unicorn for the logo of a new bar-restaurant near Nantes",
    "Le Charles est un bar-restaurant situé en périphérie nantaise. Pour son ouverture, il fallait un logo qui le représente avec deux animaux inattendus : un cafard et une licorne.":
        "Le Charles is a bar-restaurant on the outskirts of Nantes. For its opening, it needed a logo featuring two unexpected animals: a cockroach and a unicorn.",
    "Comprendre l'humour du lieu et le sens de ce duo improbable.": "Getting the place's sense of humour and the meaning of this unlikely duo.",
    "Faire cohabiter les deux animaux dans une seule silhouette.": "Fitting both animals into a single silhouette.",
    "Une licorne enroulée, à l'allure d'emblème, avec son cafard bien caché.":
        "A coiled unicorn that looks like an emblem, with its cockroach well hidden.",
    "Mises en situation pour l'enseigne et les supports du bar.": "Mock-ups for the sign and the bar's materials.",
    "Une licorne en emblème… et un cafard pour qui sait regarder.": "A unicorn as an emblem… and a cockroach for those who look closely.",
    "Le logo en situation, prêt pour l'enseigne.": "The logo in context, ready for the sign.",

    # ------------------------------------------------------------------ Oh Damned
    "Une direction artistique douce et réconfortante pour une nouvelle marque de cookies parisienne":
        "A soft, comforting art direction for a new Parisian cookie brand",
    "Oh Damned est une nouvelle marque de cookies à Paris. Elle voulait une direction artistique simple, épurée et réconfortante, qui attire autant les plus jeunes que les gourmands plus âgés, avec un vrai effet de douceur et de confort.":
        "Oh Damned is a new cookie brand in Paris. It wanted a simple, clean and comforting art direction that appeals to younger customers as much as to older sweet tooths, with a real feeling of softness and comfort.",
    "Définir le ton : gourmand, doux, et accessible à tous les âges.": "Setting the tone: indulgent, soft, and welcoming to all ages.",
    "Des formes arrondies et des bruns chauds, comme une pâte à cookie.": "Rounded shapes and warm browns, like cookie dough.",
    "Un cookie dessiné simplement et un nom aux lettres généreuses.": "A simply drawn cookie and a name in generous letters.",
    "Brun, crème, sombre : une palette qui donne envie de croquer.": "Brown, cream, dark: a palette that makes you want to take a bite.",
    "Des lettres rondes et un cookie dessiné simplement.": "Round letters and a simply drawn cookie.",
    "Une palette de bruns et de crème, douce et gourmande.": "A palette of browns and cream, soft and indulgent.",

    # ------------------------------------------------------------------ Gomu Californian
    "Une gamme de burgers à l'américaine, mise en valeur avec un style rétro":
        "An American-style burger range, showcased with a retro look",
    "La gamme Californian de Gomu est un menu de burgers inspirés des États-Unis : des produits simples, économiques mais terriblement efficaces en bouche. Toute la campagne les met en valeur avec un style rétro et américain.":
        "Gomu's Californian range is a menu of US-inspired burgers: simple, affordable products that pack a serious punch. The whole campaign showcases them with a retro American style.",
    "Lancer une nouvelle gamme et la rendre désirable dès le premier regard.": "Launching a new range and making it desirable at first glance.",
    "Un univers rétro américain : typographies généreuses, couleurs franches.": "A retro American world: generous type, bold colours.",
    "Une affiche par burger, et une affiche collection pour toute la gamme.": "One poster per burger, and a collection poster for the whole range.",
    "Formats restaurant et réseaux sociaux pour toute la durée de la campagne.":
        "Restaurant and social media formats for the whole campaign.",
    "Toute la gamme réunie sur une seule affiche.": "The whole range on a single poster.",
    "Une affiche par burger, dans le même univers rétro.": "One poster per burger, in the same retro world.",

    # ------------------------------------------------------------------ Gomu affiches
    "Quatre campagnes d'affichage pour les restaurants Gomu, quatre univers":
        "Four poster campaigns for Gomu restaurants, four worlds",
    "Pour ses restaurants, Gomu enchaîne les temps forts : les 24 Heures du Mans, une nouvelle Bubble Waffle pour l'été, une campagne autour de la culture coréenne et une gamme relevée au jalapeño. À chaque fois, une affiche qui garde l'ADN asiatique de la marque tout en créant un univers propre à la campagne.":
        "Gomu's restaurants move from one highlight to the next: the 24 Hours of Le Mans, a new Bubble Waffle for summer, a campaign around Korean culture and a jalapeño-spiced range. Each time, a poster that keeps the brand's Asian DNA while creating a world of its own.",
    "Un temps fort, un produit ou un menu à mettre en avant, et une date de lancement.":
        "A highlight, a product or a menu to push, and a launch date.",
    "Un univers par campagne : Tokyo Drift, fraîcheur d'été, culture coréenne, piment.":
        "One world per campaign: Tokyo Drift, summer freshness, Korean culture, chilli.",
    "Les produits au premier plan, les offres lisibles, la marque toujours visible.":
        "Products up front, offers easy to read, the brand always visible.",
    "Retouche des produits, puis formats restaurant et réseaux sociaux.":
        "Product retouching, then restaurant and social media formats.",
    "Les 24 Heures du Mans, version Tokyo Drift.": "The 24 Hours of Le Mans, Tokyo Drift style.",
    "La Bubble Waffle : un produit d'été, des couleurs d'été.": "The Bubble Waffle: a summer product, summer colours.",
    "Korean Gomu : la culture coréenne autour des trois produits phares.":
        "Korean Gomu: Korean culture around the three flagship products.",
    "Jalapeño : de nouveaux parfums, une campagne relevée.": "Jalapeño: new flavours, a spicy campaign.",

    # ------------------------------------------------------------------ Chikin Bang
    "Des affiches colorées, pleines d'informations et de fantaisie":
        "Colourful posters, packed with information and fun",
    "Les affiches des dernières campagnes du restaurant Chikin Bang, sucrées comme salées. Une direction artistique colorée, des affiches remplies d'informations et beaucoup de fantaisie, fidèles à l'esprit pop coréen de la marque.":
        "Posters for Chikin Bang's latest campaigns, sweet and savoury. A colourful art direction, posters packed with information and plenty of fun, true to the brand's Korean pop spirit.",
    "Une campagne par temps fort : nouveaux burgers, Pâques, cheddar…": "One campaign per highlight: new burgers, Easter, cheddar…",
    "La pop coréenne de Chikin Bang : couleurs saturées et typographies joyeuses.":
        "Chikin Bang's Korean pop: saturated colours and cheerful type.",
    "Beaucoup d'informations, mais une lecture évidente : produit, offre, marque.":
        "Lots of information, but an obvious reading order: product, offer, brand.",
    "Formats restaurant et réseaux pour chaque campagne.": "Restaurant and social formats for every campaign.",
    "Les burgers coréens, en couleurs et en fantaisie.": "Korean burgers, in colour and full of fun.",
    "Une campagne sucrée pour Pâques.": "A sweet campaign for Easter.",
    "De nouveaux packagings pour les corndogs et les wings, en pop coréenne":
        "New packaging for corndogs and wings, in Korean pop style",
    "Chikin Bang, restaurant de street food coréenne, voulait de nouveaux packagings pour ses corndogs et ses wings, en gardant le style pop coréen de l'identité de ses restaurants.":
        "Chikin Bang, a Korean street food restaurant, wanted new packaging for its corndogs and wings, keeping the Korean pop style of its restaurants' identity.",
    "Renouveler les emballages sans trahir l'identité des restaurants.": "Renewing the packaging without betraying the restaurants' identity.",
    "Le style pop coréen de la marque, appliqué au packaging.": "The brand's Korean pop style, applied to packaging.",
    "Un motif commun pour les corndogs et les wings, facile à reconnaître.": "A shared pattern for corndogs and wings, easy to recognise.",
    "Quatre couleurs (jaune, rouge, bleu, violet) pour toute la gamme.": "Four colours (yellow, red, blue, purple) for the whole range.",
    "Le corndog, en version jaune.": "The corndog, in yellow.",
    "Les wings, avec le même motif décliné en violet.": "The wings, with the same pattern in purple.",

    # ------------------------------------------------------------------ Birdz menu
    "Un menu fidèle à l'univers des restaurants de poulet de Nashville":
        "A menu true to the world of Nashville chicken joints",
    "Le menu du restaurant Birdz devait coller à l'univers de la marque, inspirée des restaurants de poulet américains façon Nashville. L'objectif : un menu qui reprend tous les codes de la marque.":
        "The Birdz restaurant menu had to match the brand's world, inspired by Nashville-style American chicken joints. The goal: a menu that uses every one of the brand's codes.",
    "Présenter toute la carte de façon claire, avant l'ouverture du restaurant.": "Presenting the whole menu clearly, before the restaurant opens.",
    "Les codes Birdz : le bleu, le blanc, et l'esprit Nashville.": "The Birdz codes: blue, white and the Nashville spirit.",
    "Une lecture rapide au comptoir : catégories, prix, menus.": "Quick to read at the counter: categories, prices, combos.",
    "Fichiers prêts pour l'imprimeur, déclinés sur plusieurs supports.": "Print-ready files, adapted to several formats.",
    "Toute la carte, dans les codes de la marque.": "The whole menu, in the brand's codes.",
    "Une lecture rapide, pensée pour la commande au comptoir.": "Quick to read, designed for ordering at the counter.",

    # ------------------------------------------------------------------ Somar
    "Une carte refaite de zéro pour un restaurant de la mer sur la côte bauloise":
        "A menu redone from scratch for a seafood restaurant on the La Baule coast",
    "Le Somar est un restaurant de produits de la mer sur la côte bauloise. Sa carte était à refaire entièrement pour entrer dans un style plus moderne : des couleurs proches de la carte d'origine, mais une mise en page plus actuelle.":
        "Le Somar is a seafood restaurant on the La Baule coast. Its menu had to be completely redone in a more modern style: colours close to the original menu, but a more up-to-date layout.",
    "Moderniser la carte sans perdre les repères des habitués.": "Modernising the menu without losing the regulars' bearings.",
    "Garder les couleurs d'origine, mais les utiliser plus franchement.": "Keeping the original colours, but using them more boldly.",
    "Une carte complète, organisée pour une lecture facile à table.": "A complete menu, organised to be easy to read at the table.",
    "Fichiers prêts pour l'imprimeur et maquette de présentation.": "Print-ready files and a presentation mock-up.",
    "La nouvelle carte, fidèle aux couleurs d'origine.": "The new menu, true to the original colours.",
    "Une mise en page plus moderne, facile à lire à table.": "A more modern layout, easy to read at the table.",

    # ------------------------------------------------------------------ Deezer
    "Deezer Premium": "Deezer Premium",
    "Une animation haute en couleur, en mouvement et en profondeur":
        "A colourful animation, full of movement and depth",
    "Un motion design pour Deezer Premium : une animation haute en couleur, en mouvement et en profondeur, à l'image de ce que partage Deezer. Tout a été créé pour cette animation, y compris la musique.":
        "A motion design piece for Deezer Premium: a colourful animation full of movement and depth, just like what Deezer shares. Everything was created for this animation, including the music.",
    "Donner envie de passer à Premium, en quelques secondes.": "Making people want to go Premium, in a few seconds.",
    "Un enchaînement de scènes colorées, rythmées comme un morceau.": "A sequence of colourful scenes, paced like a track.",
    "Couleurs, mouvement et profondeur, créés de A à Z.": "Colour, movement and depth, created from A to Z.",
    "Une musique composée spécialement pour l'animation.": "Music composed specially for the animation.",
    "Des couleurs franches et du mouvement, à l'image de Deezer.": "Bold colours and movement, just like Deezer.",

    # ------------------------------------------------------------------ UEFA Youth League
    "Tom Mabon, Louis Leroux & Mathis Philippe (FC Nantes)": "Tom Mabon, Louis Leroux & Mathis Philippe (FC Nantes)",
    "Les visuels de match d'un parcours historique en coupe d'Europe":
        "Matchday visuals for a historic European cup run",
    "Tom Mabon, gardien de l'équipe jeunes du FC Nantes, a fait confiance à Frostbird pour ses visuels de match pendant leur parcours historique en coupe d'Europe, tout comme ses coéquipiers Louis Leroux et Mathis Philippe. Un visuel pour chaque rencontre.":
        "Tom Mabon, goalkeeper of FC Nantes' youth team, trusted Frostbird with his matchday visuals during their historic European cup run, as did his teammates Louis Leroux and Mathis Philippe. One visual for every match.",
    "Un visuel par match, publié avant chaque rencontre.": "One visual per match, published before kick-off.",
    "Chaque adversaire, chaque ville a sa propre ambiance.": "Every opponent, every city has its own mood.",
    "Le joueur en héros, entouré des références du match.": "The player as the hero, surrounded by references to the match.",
    "Formats stories et publications, livrés avant le coup d'envoi.": "Story and post formats, delivered before kick-off.",
    "Jusqu'à la finale : un visuel pour chaque étape du parcours.": "All the way to the final: one visual for every step of the run.",
    "Chaque adversaire a son ambiance.": "Every opponent has its own mood.",

    # ------------------------------------------------------------------ Championnat de France
    "Des visuels pour présenter la nouvelle saison de Ligue 1": "Visuals to present the new Ligue 1 season",
    "Ces visuels présentent la nouvelle saison de Ligue 1 McDonald's. On y retrouve l'identité des clubs et des villes à travers les couleurs, les joueurs et les références visuelles.":
        "These visuals present the new Ligue 1 McDonald's season. They capture the identity of the clubs and their cities through colours, players and visual references.",
    "Présenter la saison à travers ce qui fait l'identité de chaque club.": "Presenting the season through what makes each club unique.",
    "Couleurs, joueurs, monuments et références propres à chaque ville.": "Colours, players, landmarks and references specific to each city.",
    "Des compositions riches, où chaque détail renvoie au club.": "Rich compositions where every detail points back to the club.",
    "Une série cohérente, pensée pour les réseaux.": "A consistent series, designed for social media.",
    "Chaque club raconté par ses couleurs et ses références.": "Each club told through its colours and references.",
    "Des clins d'œil visuels à l'identité de chaque ville.": "Visual nods to each city's identity.",

    # ------------------------------------------------------------------ Ilan / Aïman
    "Photos et visuels de match pour un joueur U19 National": "Photos and matchday visuals for a U19 national league player",
    "Ilan joue en U19 National. Frostbird le photographie pendant ses matchs et réalise des visuels pour tous ses rendez-vous du week-end face à de gros clubs, notamment l'OL.":
        "Ilan plays in the U19 national league. Frostbird photographs him during his matches and creates visuals for all his weekend fixtures against big clubs, including OL.",
    "Aïman joue en U19 National. Frostbird le photographie pendant ses matchs et réalise des visuels pour tous ses rendez-vous du week-end face à de gros clubs, notamment le PSG.":
        "Aïman plays in the U19 national league. Frostbird photographs him during his matches and creates visuals for all his weekend fixtures against big clubs, including PSG.",
    "Accompagner l'image d'un joueur qui vise un contrat professionnel.": "Supporting the image of a player aiming for a professional contract.",
    "Des photos prises en match, la matière première des visuels.": "Photos taken during matches, the raw material of the visuals.",
    "Un visuel pour chaque affiche du week-end, dans une ligne reconnaissable.": "A visual for every weekend fixture, in a recognisable style.",
    "Formats prêts pour ses réseaux, livrés avant chaque rencontre.": "Formats ready for his social media, delivered before every match.",
    "Un visuel pour chaque rendez-vous du week-end.": "A visual for every weekend fixture.",
    "Une ligne graphique reconnaissable d'un match à l'autre.": "A recognisable visual style from one match to the next.",
    "Le joueur en héros, match après match.": "The player as the hero, match after match.",

    # ------------------------------------------------------------------ Europa League
    "Deux visuels de coupe d'Europe pour un joueur de l'Olympique de Marseille":
        "Two European cup visuals for an Olympique de Marseille player",
    "Quentin Merlin, alors joueur de l'Olympique de Marseille, a demandé deux visuels pour ses matchs de coupe d'Europe contre l'Atalanta Bergame et le Shakhtar Donetsk. Deux créations bien différentes, pour deux affiches européennes.":
        "Quentin Merlin, then an Olympique de Marseille player, asked for two visuals for his European cup matches against Atalanta and Shakhtar Donetsk. Two very different designs for two European nights.",
    "Deux matchs européens, deux visuels à publier avant chaque rencontre.": "Two European matches, two visuals to publish before each one.",
    "Une ambiance propre à chaque adversaire.": "A mood specific to each opponent.",
    "Le joueur au centre, mis en scène dans l'univers de la compétition.": "The player at the centre, staged in the world of the competition.",
    "Formats réseaux livrés avant le coup d'envoi.": "Social formats delivered before kick-off.",
    "Contre l'Atalanta Bergame.": "Against Atalanta.",
    "Contre le Shakhtar Donetsk : une tout autre ambiance.": "Against Shakhtar Donetsk: a whole different mood.",

    # ------------------------------------------------------------------ prestation : branding
    "Un logo, ça se teste.": "A logo has to be tested.",
    "Comme une voiture : au crash-test.": "Like a car: crash test included.",
    "En géant.": "Giant size.",
    "Sur une façade, un camion, un maillot. De près, il ne doit rien perdre.":
        "On a building, a truck, a jersey. Up close, it can't lose a thing.",
    "En minuscule.": "Tiny size.",
    "Seize pixels dans un onglet, deux centimètres sur une étiquette. Il doit rester lui-même.":
        "Sixteen pixels in a browser tab, two centimetres on a label. It has to stay itself.",
    "Sans couleur.": "No colour.",
    "Imprimé en noir sur un ticket de caisse, photocopié, tamponné. Aucune excuse.":
        "Printed in black on a receipt, photocopied, stamped. No excuses.",
    "En un éclair.": "In a flash.",
    "Aperçu à 110 km/h sur un panneau. On a moins d'une seconde pour le reconnaître.":
        "Glimpsed on a billboard at 70 mph. You have less than a second to recognise it.",
    "110 km/h": "70 mph",
    "16 px": "16 px",
    "TICKET N° 0042": "RECEIPT NO. 0042",
    "1 × IDENTITÉ VISUELLE": "1 × VISUAL IDENTITY",
    "MERCI DE VOTRE VISITE": "THANK YOU FOR YOUR VISIT",
    "Verdict :": "Verdict:",
    "les nôtres passent tous les tests.": "ours pass every test.",
    "Et le vôtre, il tiendrait le choc ?": "Would yours survive the crash?",
    "Faisons le test.": "Let's test it.",

    # ------------------------------------------------------------------ prestation : design
    "1,7 s": "1.7 s",
    "0,3 s": "0.3 s",
    "1 s": "1 s",
    "C'est le temps moyen qu'on accorde à un contenu en le faisant défiler sur son téléphone.":
        "That's the average time people give a piece of content while scrolling on their phone.",
    "Source : Facebook IQ, « Capturing Attention in Feed », 2016.":
        "Source: Facebook IQ, “Capturing Attention in Feed”, 2016.",
    "Une affiche, un menu, un visuel :": "A poster, a menu, a visual:",
    "tout se joue avant la fin du chrono.": "it all happens before the clock runs out.",
    "On vous voit.": "We see you.",
    "Une couleur, un contraste, une forme qui arrête le pouce.": "A colour, a contrast, a shape that stops the thumb.",
    "On vous comprend.": "We get you.",
    "Un seul message, une hiérarchie évidente : produit, offre, marque.": "One message, an obvious hierarchy: product, offer, brand.",
    "On a faim.": "We're hungry.",
    "L'envie est là. Le reste, c'est le chemin jusqu'au comptoir.": "The craving is there. The rest is the walk to the counter.",
    "Et vos visuels, ils tiennent combien de temps ?": "And your visuals, how long do they hold attention?",
    "Donnez-nous 1,7 seconde.": "Give us 1.7 seconds.",

    # ------------------------------------------------------------------ prestation : web
    "Quelqu'un cherche « restaurant ouvert près de moi ».": "Someone searches for “restaurant open near me”.",
    "Il tombe sur vous.": "They land on your site.",
    "Votre site commence à charger…": "Your site starts loading…",
    "s…": "s…",
    "des visites sur mobile sont abandonnées quand une page met plus de 3 secondes à s'afficher.":
        "of mobile visits are abandoned when a page takes more than 3 seconds to load.",
    "Source : Google / DoubleClick, « The Need for Mobile Speed », 2016.":
        "Source: Google / DoubleClick, “The Need for Mobile Speed”, 2016.",
    "Trois secondes plus tard,": "Three seconds later,",
    "il réserve chez le voisin.": "they book next door.",
    "On rembobine. Même soir, même recherche.": "Let's rewind. Same night, same search.",
    "Cette fois, tout s'affiche": "This time, everything loads",
    "avant qu'il ait cligné des yeux.": "before they can blink.",
    "Des écrans qu'on comprend sans réfléchir, qui s'affichent sans attendre.":
        "Screens you understand without thinking, that load without waiting.",
    "Et votre site, il garde ses visiteurs ?": "And your site, does it keep its visitors?",
    "On s'occupe du chrono.": "We'll handle the clock.",

    # ------------------------------------------------------------------ prestation : photo
    "Vous et nous,": "You and us,",
    "on ne regarde pas la même chose.": "we don't see the same thing.",
    "Vous voyez un burger.": "You see a burger.",
    "On voit une sauce qui coule au bon moment, sous une lumière qui vient de la gauche.":
        "We see sauce dripping at just the right moment, with light coming from the left.",
    "Vous voyez un match.": "You see a match.",
    "On voit l'instant exact où le ballon quitte le pied.": "We see the exact moment the ball leaves the foot.",
    "Vous voyez un bar.": "You see a bar.",
    "On voit le marbre qui s'allume quand la salle s'éteint.": "We see the marble light up as the room goes dark.",
    "Et derrière chaque image, il y a ça : une table, une lumière, et beaucoup de patience.":
        "And behind every image, there's this: a table, a light, and a lot of patience.",
    "Et chez vous, qu'est-ce qu'on verrait ?": "And at your place, what would we see?",
    "Venez, on vous montre.": "Come on, we'll show you.",

    # ------------------------------------------------------------------ prestations : communs
    "Parlons-en": "Let's talk",
    "Voir nos autres prestations": "See our other services",
    "Nos projets en branding": "Our branding work",
    "Nos projets en design graphique": "Our graphic design work",
    "Nos projets en web & apps": "Our web & apps work",
    "Nos projets en photographie": "Our photography work",

    # ------------------------------------------------------------------ légal
    "Éditeur du site : Frostbird, société en cours d'immatriculation. Contact : hello@frostbird.fr. Hébergeur : Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, États-Unis.":
        "Site publisher: Frostbird, company being registered. Contact: hello@frostbird.fr. Host: Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, United States.",
    "Les informations envoyées via le formulaire de contact servent uniquement à répondre à votre demande. Elles ne sont ni revendues ni transmises à des tiers. Texte à compléter.":
        "Information sent through the contact form is used only to answer your request. It is never sold or passed on to third parties. Text to be completed.",
    "Ce site n'utilise pas de cookies de suivi. Texte à compléter.": "This site does not use tracking cookies. Text to be completed.",
    "Conditions générales d'utilisation": "Terms of use",
    "Texte à compléter.": "Text to be completed.",
}
