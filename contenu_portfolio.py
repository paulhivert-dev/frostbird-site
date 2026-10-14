"""Projets repris de paulhivert.com, rangés dans les catégories Frostbird.

Chaque entrée produit une carte dans Works et une page projet-<slug>.html (même modèle que les
autres études de cas). Images dans public/assets/img/works/<slug>/.

  logo     : (fichier dans assets/img/clients, ratio largeur/hauteur, fond de marque au survol)
             ou None → la carte montre la couverture teintée en attendant le logo
  captures : visuels mis en avant (image, légende) — orientation et proportions détectées au build
  galerie  : série complète en grille avec visionneuse ([] = pas de galerie)
  galerie_ligne : True → la série tient sur une ligne qui défile à l'horizontale
  video    : fichier .mp4 dans works/ (lu directement dans la page) ou lien YouTube
  avant_apres : (ancien visuel, nouveau visuel, légende) → comparateur à poignée

Textes rédigés à partir des descriptions du portfolio : à relire.
"""

PROCESSUS_LOGO = "Brief", "Recherches", "Création", "Déclinaisons"

PORTFOLIO = [
    # ------------------------------------------------------------------ Branding
    {
        "slug": "atlantic", "cat": "branding", "titre": "Atlantic Bateaux Piriac", "date": "2024",
        "cover": "atlantic/atlantic-noir-blanc.jpg", "logo": ("atlantic.png", 1.907, "#ffffff"),
        "client": "Atlantic Bateaux",
        "sous_titre": "Remettre à neuf un logo vieux de quinze ans, sans perdre ce qui faisait son histoire",
        "intro": "Atlantic Bateaux est une entreprise du nautisme installée à Piriac. Son logo avait quinze "
                 "ans : il fallait le moderniser tout en gardant le dessin du bateau de l'ancienne version, "
                 "repensé plus simplement et décliné sur plusieurs supports.",
        "services": ["Refonte de logo", "Identité visuelle", "Déclinaisons"],
        "processus": [
            ("Brief", "Comprendre l'histoire de l'entreprise et ce que l'ancien logo représentait pour elle."),
            ("Recherches", "Garder le bateau comme fil conducteur et chercher une forme plus épurée, lisible de loin."),
            ("Création", "Un pictogramme net associé à un nom en capitales solides, pensé pour la signalétique."),
            ("Déclinaisons", "Versions noir, blanc et argent pour tous les fonds et tous les supports."),
        ],
        "captures": [
            ("atlantic/logo-atlantic-u.jpg", "Le bateau de l'ancien logo, redessiné en un seul geste."),
            ("atlantic/atlantic-noir-argent.jpg", "Une version argent pour les supports haut de gamme."),
        ],
        "avant_apres": ("atlantic/ancien-logo.png", "atlantic/atlantic-noir-blanc.jpg",
                        "Quinze ans d'écart : le bateau est resté, tout le reste a été simplifié."),
        "galerie": ["atlantic/logo-atlantic-u.jpg", "atlantic/atlantic-noir-blanc.jpg", "atlantic/atlantic-blanc-noir.jpg", "atlantic/atlantic-noir-argent.jpg", "atlantic/atlantic-argent-noir.jpg"],
    },
    {
        "slug": "spike", "cat": "branding", "titre": "Spike", "date": "2021 – 2022",
        "cover": "spike/logo-spike-u.jpg", "logo": ("spike.png", 0.695, "#ffffff"),
        "client": "Spike (projet de fin d'études)",
        "sous_titre": "Une marque de football engagée, du logo à la campagne de lancement",
        "intro": "Spike est une marque créée de toutes pièces pour un projet de fin d'études en design "
                 "graphique : un équipementier sportif, centré sur le football, qui fabrique ses produits à "
                 "partir de plastique recyclé. Le projet couvre toute la marque : le nom, le logo, "
                 "l'identité visuelle, puis une campagne de lancement avec une affiche et un motion design.",
        "services": ["Naming", "Création de logo", "Identité visuelle", "Affiche", "Motion design"],
        "processus": [
            ("Positionnement", "Un équipementier de football qui donne une seconde vie au plastique retrouvé dans l'océan."),
            ("Logo & identité", "Un S en deux courbes qui se répondent : le mouvement du jeu et la boucle du recyclage."),
            ("Affiche", "Une chaussure qui se noie, pour faire ressentir le poids du plastique et le sens de la marque."),
            ("Motion design", "Un film qui suit la matière, d'une bouteille dans la mer jusqu'à la chaussure finie."),
        ],
        "captures": [
            ("spike/logo-spike-u.jpg", "Un S en deux courbes : le mouvement du jeu et la boucle du recyclage."),
            ("spike/spike-mockup.jpg", "La marque en situation, sur les produits."),
            ("spike/spike-affiche.jpg", "L'affiche de lancement : les dernières bulles d'air d'une chaussure qui se noie."),
            ("spike/spike-mer.jpg", "Le motion design : tout commence par une bouteille dans la mer."),
        ],
        "video": "spike/spike-motion.mp4",  # hébergée avec le site (aperçu : spike-motion-poster.jpg)
        "galerie": ["spike/logo-spike-u.jpg", "spike/spike-blanc-noir.jpg", "spike/spike-blanc-vert.jpg",
                    "spike/spike-vert-blanc.jpg", "spike/spike-mockup.jpg", "spike/spike-affiche.jpg",
                    "spike/p13.jpg", "spike/spike-mer.jpg", "spike/spike-warning.jpg"],
    },
    {
        "slug": "rooster", "cat": "branding", "titre": "Rooster", "date": "2026",
        "cover": "rooster/rooster-word-violet.jpg", "logo": ("rooster.png", 2.662, "#ffffff"),
        "client": "Rooster",
        "sous_titre": "Une marque de poulet braisé qui assume un virage à 180 degrés",
        "intro": "Rooster est une marque de restaurants de poulet braisé. L'objectif : une identité visuelle "
                 "forte, qui sorte des codes classiques du poulet (les couleurs chaudes) et assume "
                 "pleinement ce changement de direction.",
        "services": ["Création de logo", "Identité visuelle", "Palette de couleurs"],
        "processus": [
            ("Brief", "Repérer les codes du secteur, pour mieux s'en éloigner."),
            ("Recherches", "Un violet électrique à la place des rouges et des jaunes attendus."),
            ("Création", "Un nom en capitales massives, avec un S en forme de flamme pour le braisé."),
            ("Déclinaisons", "Logotype, pictogramme et versions ton sur ton pour tous les supports."),
        ],
        "captures": [
            ("rooster/rooster-word-violet.jpg", "Le violet remplace les couleurs chaudes : on ne confond pas Rooster."),
            ("rooster/rooster-icon-violet.jpg", "Le S-flamme fonctionne aussi seul, comme pictogramme."),
        ],
        "galerie": ["rooster/logo-rooster-u.jpg", "rooster/rooster-word-violet.jpg", "rooster/rooster-icon-ton.jpg", "rooster/rooster-word-blanc.jpg", "rooster/rooster-icon-violet.jpg", "rooster/rooster-word-ton.jpg"],
    },
    {
        "slug": "happy-propaganda", "cat": "branding", "titre": "Happy Propaganda", "date": "2026",
        "cover": "happy-propaganda/happy-rouge.jpg", "logo": ("happy-propaganda.png", 1.393, "#fe2c2b"),
        "client": "Happy Propaganda",
        "sous_titre": "L'identité d'une agence de communication, avec un œil et un cœur dedans",
        "intro": "Happy Propaganda est une agence de communication qui voulait une identité visuelle forte "
                 "et assumée. Sa demande tenait en une phrase : un œil, et un cœur dedans.",
        "services": ["Création de logo", "Identité visuelle", "Déclinaisons"],
        "processus": [
            ("Brief", "Partir de l'image voulue par l'agence : un œil qui regarde, un cœur qui ressent."),
            ("Recherches", "Un trait volontairement brut, presque dessiné à la main, loin des logos trop lisses."),
            ("Création", "Un œil cornu qui abrite un cœur, et un mot « happy » au tracé libre."),
            ("Déclinaisons", "Rouge, sombre, blanc et monochrome : la même énergie sur chaque fond."),
        ],
        "captures": [
            ("happy-propaganda/logo-happy-u.jpg", "Un œil, un cœur dedans : la demande tenait en une phrase."),
            ("happy-propaganda/happy-rouge.jpg", "Le rouge, couleur principale de l'agence."),
        ],
        "galerie": ["happy-propaganda/logo-happy-u.jpg", "happy-propaganda/happy-rouge.jpg", "happy-propaganda/happy-dark.jpg", "happy-propaganda/happy-blanc.jpg", "happy-propaganda/happy-dark-mono.jpg"],
    },
    {
        "slug": "first-touch", "cat": "branding", "titre": "First Touch", "date": "2025",
        "cover": "first-touch/ft-logo-agency.jpg", "logo": ("first-touch.svg", 2.057, "#f6eee3"),
        "client": "First Touch",
        "sous_titre": "Un logo stable et dynamique pour une agence de joueurs et joueuses de football",
        "intro": "First Touch est une agence qui accompagne des joueurs et joueuses de football. Elle voulait "
                 "un logo stable et dynamique, avec les codes d'un logo de sport, décliné en deux versions : "
                 "une claire et simple, une plus travaillée.",
        "services": ["Création de logo", "Identité visuelle", "Déclinaisons"],
        "processus": [
            ("Brief", "Comprendre le métier d'agent et les attentes des joueurs accompagnés."),
            ("Recherches", "Des initiales imbriquées et une inclinaison qui évoque la vitesse."),
            ("Création", "Un monogramme FT géométrique, solide comme un écusson."),
            ("Déclinaisons", "Une version claire et sobre, une version en dégradé pour les réseaux."),
        ],
        "captures": [
            ("first-touch/ft-gradient.jpg", "La version travaillée, en dégradé, pour les réseaux."),
            ("first-touch/ft-logo-agency.jpg", "La version claire et simple, pour les documents de l'agence."),
        ],
        "galerie": ["first-touch/ft-gradient.jpg", "first-touch/ft-logo-agency.jpg", "first-touch/ft-icon-light.jpg"],
    },
    {
        "slug": "le-charles", "cat": "branding", "titre": "Le Charles", "date": "2024",
        "cover": "le-charles/logo-le-charles-u.jpg", "logo": ("le-charles.png", 1.677, "#242424"),
        "client": "Le Charles",
        "sous_titre": "Un cafard et une licorne pour le logo d'un nouveau bar-restaurant nantais",
        "intro": "Le Charles est un bar-restaurant situé en périphérie nantaise. Pour son ouverture, il "
                 "fallait un logo qui le représente avec deux animaux inattendus : un cafard et une licorne.",
        "services": ["Création de logo", "Illustration", "Mise en situation"],
        "processus": [
            ("Brief", "Comprendre l'humour du lieu et le sens de ce duo improbable."),
            ("Recherches", "Faire cohabiter les deux animaux dans une seule silhouette."),
            ("Création", "Une licorne enroulée, à l'allure d'emblème, avec son cafard bien caché."),
            ("Déclinaisons", "Mises en situation pour l'enseigne et les supports du bar."),
        ],
        "captures": [
            ("le-charles/logo-le-charles-u.jpg", "Une licorne en emblème… et un cafard pour qui sait regarder."),
            ("le-charles/charles-mockup.jpg", "Le logo en situation, prêt pour l'enseigne."),
        ],
        "galerie": [],
    },
    {
        "slug": "oh-damned", "cat": "branding", "titre": "Oh Damned", "date": "2026",
        "cover": "oh-damned/od-dark.jpg", "logo": ("oh-damned.png", 2.591, "#474644"),
        "client": "Oh Damned",
        "sous_titre": "Une direction artistique douce et réconfortante pour une nouvelle marque de cookies parisienne",
        "intro": "Oh Damned est une nouvelle marque de cookies à Paris. Elle voulait une direction artistique "
                 "simple, épurée et réconfortante, qui attire autant les plus jeunes que les gourmands plus "
                 "âgés, avec un vrai effet de douceur et de confort.",
        "services": ["Création de logo", "Direction artistique", "Palette de couleurs"],
        "processus": [
            ("Brief", "Définir le ton : gourmand, doux, et accessible à tous les âges."),
            ("Recherches", "Des formes arrondies et des bruns chauds, comme une pâte à cookie."),
            ("Création", "Un cookie dessiné simplement et un nom aux lettres généreuses."),
            ("Déclinaisons", "Brun, crème, sombre : une palette qui donne envie de croquer."),
        ],
        "captures": [
            ("oh-damned/od-dark.jpg", "Des lettres rondes et un cookie dessiné simplement."),
            ("oh-damned/od-cream.jpg", "Une palette de bruns et de crème, douce et gourmande."),
        ],
        "galerie": ["oh-damned/logo-oh-damned-u.jpg", "oh-damned/od-dark.jpg", "oh-damned/od-brun.jpg", "oh-damned/od-cream.jpg", "oh-damned/od-dark-outline-big.jpg", "oh-damned/od-brun-fonce.jpg"],
    },
    # ------------------------------------------------------------------ Design graphique : affiches
    {
        "slug": "gomu-californian", "cat": "design", "titre": "Gomu Californian", "date": "2026",
        "cover": "gomu-californian/cal-collection.jpg", "logo": ("gomu-burger.png", 1.551, "#ffffff"),
        "client": "Gomu",
        "sous_titre": "Une gamme de burgers à l'américaine, mise en valeur avec un style rétro",
        "intro": "La gamme Californian de Gomu est un menu de burgers inspirés des États-Unis : des produits "
                 "simples, économiques mais terriblement efficaces en bouche. Toute la campagne les met en "
                 "valeur avec un style rétro et américain.",
        "services": ["Direction artistique", "Campagne d'affichage", "Déclinaisons"],
        "processus": [
            ("Brief", "Lancer une nouvelle gamme et la rendre désirable dès le premier regard."),
            ("Direction artistique", "Un univers rétro américain : typographies généreuses, couleurs franches."),
            ("Création", "Une affiche par burger, et une affiche collection pour toute la gamme."),
            ("Déclinaisons", "Formats restaurant et réseaux sociaux pour toute la durée de la campagne."),
        ],
        "captures": [
            ("gomu-californian/cal-collection.jpg", "Toute la gamme réunie sur une seule affiche."),
            ("gomu-californian/cal-jalapeno-1.jpg", "Une affiche par burger, dans le même univers rétro."),
        ],
        "galerie_ligne": True,
        "galerie": ["gomu-californian/cal-jalapeno-1.jpg", "gomu-californian/cal-collection.jpg", "gomu-californian/cal-cheese.jpg", "gomu-californian/cal-jalapeno-2.jpg", "gomu-californian/cal-californians.jpg", "gomu-californian/p16.jpg"],
    },
    {
        "slug": "gomu-affiches", "cat": "design", "titre": "Gomu — affiches", "date": "2025",
        "cover": "gomu-affiches/p17.jpg", "logo": ("gomu.png", 1.098, "#000000"),
        "client": "Gomu",
        "sous_titre": "Quatre campagnes d'affichage pour les restaurants Gomu, quatre univers",
        "intro": "Pour ses restaurants, Gomu enchaîne les temps forts : les 24 Heures du Mans, une "
                 "nouvelle Bubble Waffle pour l'été, une campagne autour de la culture coréenne et une "
                 "gamme relevée au jalapeño. À chaque fois, une affiche qui garde l'ADN asiatique de la "
                 "marque tout en créant un univers propre à la campagne.",
        "services": ["Direction artistique", "Campagnes d'affichage", "Retouche", "Déclinaisons"],
        "processus": [
            ("Brief", "Un temps fort, un produit ou un menu à mettre en avant, et une date de lancement."),
            ("Direction artistique", "Un univers par campagne : Tokyo Drift, fraîcheur d'été, culture coréenne, piment."),
            ("Composition", "Les produits au premier plan, les offres lisibles, la marque toujours visible."),
            ("Déclinaisons", "Retouche des produits, puis formats restaurant et réseaux sociaux."),
        ],
        "captures": [
            ("gomu-affiches/p17.jpg", "Les 24 Heures du Mans, version Tokyo Drift."),
            ("gomu-affiches/gomu-waffle.jpg", "La Bubble Waffle : un produit d'été, des couleurs d'été."),
            ("gomu-affiches/p19.jpg", "Korean Gomu : la culture coréenne autour des trois produits phares."),
            ("gomu-affiches/p21.jpg", "Jalapeño : de nouveaux parfums, une campagne relevée."),
        ],
        "galerie_ligne": True,
        "galerie": ["gomu-affiches/p17.jpg", "gomu-affiches/gomu-waffle.jpg", "gomu-affiches/p19.jpg",
                    "gomu-affiches/p20.jpg", "gomu-affiches/p21.jpg"],
    },
    {
        "slug": "chikin-bang-affiches", "cat": "design", "titre": "Chikin Bang — affiches", "date": "2026",
        "cover": "chikin-bang-affiches/chikin-korean-burgers.jpg", "logo": ("chikin-bang.png", 1.633, "#000000"),
        "client": "Chikin Bang",
        "sous_titre": "Des affiches colorées, pleines d'informations et de fantaisie",
        "intro": "Les affiches des dernières campagnes du restaurant Chikin Bang, sucrées comme salées. Une "
                 "direction artistique colorée, des affiches remplies d'informations et beaucoup de "
                 "fantaisie, fidèles à l'esprit pop coréen de la marque.",
        "services": ["Direction artistique", "Campagnes d'affichage", "Déclinaisons"],
        "processus": [
            ("Brief", "Une campagne par temps fort : nouveaux burgers, Pâques, cheddar…"),
            ("Direction artistique", "La pop coréenne de Chikin Bang : couleurs saturées et typographies joyeuses."),
            ("Composition", "Beaucoup d'informations, mais une lecture évidente : produit, offre, marque."),
            ("Déclinaisons", "Formats restaurant et réseaux pour chaque campagne."),
        ],
        "captures": [
            ("chikin-bang-affiches/chikin-korean-burgers.jpg", "Les burgers coréens, en couleurs et en fantaisie."),
            ("chikin-bang-affiches/chikin-paques.jpg", "Une campagne sucrée pour Pâques."),
        ],
        "galerie": ["chikin-bang-affiches/chikin-korean-burgers.jpg", "chikin-bang-affiches/chikin-paques.jpg", "chikin-bang-affiches/chikin-cheddar.jpg", "chikin-bang-affiches/p23.jpg"],
    },
    # ------------------------------------------------------------------ Design graphique : print
    {
        "slug": "birdz-menu", "cat": "design", "titre": "Birdz — menu", "date": "2025",
        "cover": "birdz-menu/birdz-menu-1.jpg", "logo": ("birdz.png", 1.0, "#ffffff"),
        "client": "Birdz Hot Chicken",
        "sous_titre": "Un menu fidèle à l'univers des restaurants de poulet de Nashville",
        "intro": "Le menu du restaurant Birdz devait coller à l'univers de la marque, inspirée des "
                 "restaurants de poulet américains façon Nashville. L'objectif : un menu qui reprend tous "
                 "les codes de la marque.",
        "services": ["Direction artistique", "Menu", "Mise en page"],
        "processus": [
            ("Brief", "Présenter toute la carte de façon claire, avant l'ouverture du restaurant."),
            ("Direction artistique", "Les codes Birdz : le bleu, le blanc, et l'esprit Nashville."),
            ("Mise en page", "Une lecture rapide au comptoir : catégories, prix, menus."),
            ("Impression", "Fichiers prêts pour l'imprimeur, déclinés sur plusieurs supports."),
        ],
        "captures": [
            ("birdz-menu/birdz-menu-1.jpg", "Toute la carte, dans les codes de la marque."),
            ("birdz-menu/birdz-menu-2.jpg", "Une lecture rapide, pensée pour la commande au comptoir."),
        ],
        "galerie": ["birdz-menu/birdz-menu-1.jpg", "birdz-menu/birdz-menu-2.jpg", "birdz-menu/birdz-menu-3.jpg", "birdz-menu/birdz-menu-4.jpg", "birdz-menu/birdz-menu-5.jpg", "birdz-menu/birdz-menu-6.jpg"],
    },
    {
        "slug": "chikin-bang-packaging", "cat": "design", "titre": "Chikin Bang — packaging", "date": "2025",
        "cover": "chikin-bang-packaging/cp-corndog-jaune.jpg", "logo": ("chikin-bang.png", 1.633, "#000000"),
        "client": "Chikin Bang",
        "sous_titre": "De nouveaux packagings pour les corndogs et les wings, en pop coréenne",
        "intro": "Chikin Bang, restaurant de street food coréenne, voulait de nouveaux packagings pour ses "
                 "corndogs et ses wings, en gardant le style pop coréen de l'identité de ses restaurants.",
        "services": ["Packaging", "Direction artistique", "Déclinaisons couleur"],
        "processus": [
            ("Brief", "Renouveler les emballages sans trahir l'identité des restaurants."),
            ("Direction artistique", "Le style pop coréen de la marque, appliqué au packaging."),
            ("Création", "Un motif commun pour les corndogs et les wings, facile à reconnaître."),
            ("Déclinaisons", "Quatre couleurs (jaune, rouge, bleu, violet) pour toute la gamme."),
        ],
        "captures": [
            ("chikin-bang-packaging/cp-corndog-jaune.jpg", "Le corndog, en version jaune."),
            ("chikin-bang-packaging/cp-wings-violet.jpg", "Les wings, avec le même motif décliné en violet."),
        ],
        "galerie": ["chikin-bang-packaging/cp-corndog-jaune.jpg", "chikin-bang-packaging/cp-wings-violet.jpg", "chikin-bang-packaging/cp-corndog-rouge.jpg", "chikin-bang-packaging/cp-wings-jaune.jpg", "chikin-bang-packaging/cp-corndog-bleu.jpg", "chikin-bang-packaging/cp-wings-rouge.jpg", "chikin-bang-packaging/cp-corndog-violet.jpg", "chikin-bang-packaging/cp-wings-bleu.jpg"],
    },
    {
        "slug": "somar", "cat": "design", "titre": "Somar", "date": "2026",
        "cover": "somar/somar-mockup.jpg", "logo": ("somar.png", 8.126, "#1b82c5"),
        "client": "Le Somar",
        "sous_titre": "Une carte refaite de zéro pour un restaurant de la mer sur la côte bauloise",
        "intro": "Le Somar est un restaurant de produits de la mer sur la côte bauloise. Sa carte était à "
                 "refaire entièrement pour entrer dans un style plus moderne : des couleurs proches de la "
                 "carte d'origine, mais une mise en page plus actuelle.",
        "services": ["Menu", "Mise en page", "Direction artistique"],
        "processus": [
            ("Brief", "Moderniser la carte sans perdre les repères des habitués."),
            ("Direction artistique", "Garder les couleurs d'origine, mais les utiliser plus franchement."),
            ("Mise en page", "Une carte complète, organisée pour une lecture facile à table."),
            ("Impression", "Fichiers prêts pour l'imprimeur et maquette de présentation."),
        ],
        "captures": [
            ("somar/somar-mockup.jpg", "La nouvelle carte, fidèle aux couleurs d'origine."),
            ("somar/somar-menu-1.jpg", "Une mise en page plus moderne, facile à lire à table."),
        ],
        "galerie": ["somar/somar-mockup.jpg", "somar/somar-menu-1.jpg", "somar/somar-menu-2.jpg"],
    },
    # ------------------------------------------------------------------ Design graphique : motion
    {
        "slug": "deezer", "cat": "design", "titre": "Deezer — motion design", "date": "2021",
        "cover": "deezer/motion-deezer-main.jpg", "logo": ("deezer.png", 1.006, "#080808"),
        "client": "Deezer Premium",
        "sous_titre": "Une animation haute en couleur, en mouvement et en profondeur",
        "intro": "Un motion design pour Deezer Premium : une animation haute en couleur, en mouvement et en "
                 "profondeur, à l'image de ce que partage Deezer. Tout a été créé pour cette animation, "
                 "y compris la musique.",
        "services": ["Motion design", "Direction artistique", "Musique"],
        "processus": [
            ("Brief", "Donner envie de passer à Premium, en quelques secondes."),
            ("Storyboard", "Un enchaînement de scènes colorées, rythmées comme un morceau."),
            ("Animation", "Couleurs, mouvement et profondeur, créés de A à Z."),
            ("Son", "Une musique composée spécialement pour l'animation."),
        ],
        "captures": [
            ("deezer/deezer-motion-1.jpg", "Des couleurs franches et du mouvement, à l'image de Deezer."),
        ],
        "galerie": [],
        "video": "https://youtu.be/RIjTaoSKWug",
    },
    # ------------------------------------------------------------------ Design graphique : réseaux sociaux
    {
        "slug": "uefa-youth-league", "cat": "design", "titre": "UEFA Youth League", "date": "2024",
        "cover": "uefa-youth-league/p25.jpg", "logo": ("youth-league.png", 1.0, "#2d2de5"),
        "client": "Tom Mabon, Louis Leroux & Mathis Philippe (FC Nantes)",
        "sous_titre": "Les visuels de match d'un parcours historique en coupe d'Europe",
        "intro": "Tom Mabon, gardien de l'équipe jeunes du FC Nantes, a fait confiance à Frostbird pour ses "
                 "visuels de match pendant leur parcours historique en coupe d'Europe, tout comme ses "
                 "coéquipiers Louis Leroux et Mathis Philippe. Un visuel pour chaque rencontre.",
        "services": ["Visuels réseaux sociaux", "Direction artistique", "Retouche"],
        "processus": [
            ("Brief", "Un visuel par match, publié avant chaque rencontre."),
            ("Direction artistique", "Chaque adversaire, chaque ville a sa propre ambiance."),
            ("Création", "Le joueur en héros, entouré des références du match."),
            ("Diffusion", "Formats stories et publications, livrés avant le coup d'envoi."),
        ],
        "captures": [
            ("uefa-youth-league/youth-finale.jpg", "Jusqu'à la finale : un visuel pour chaque étape du parcours."),
            ("uefa-youth-league/youth-olympiakos.jpg", "Chaque adversaire a son ambiance."),
        ],
        "galerie": ["uefa-youth-league/p25.jpg", "uefa-youth-league/youth-olympiakos.jpg", "uefa-youth-league/youth-finale.jpg", "uefa-youth-league/youth-eiffel.jpg"],
    },
    {
        "slug": "championnat-de-france", "cat": "design", "titre": "Championnat de France", "date": "2025",
        "cover": "championnat-de-france/p26.jpg", "logo": ("ligue-1.png", 0.791, "#085efc"),
        "client": "Création personnelle",
        "sous_titre": "Des visuels pour présenter la nouvelle saison de Ligue 1",
        "intro": "Ces visuels présentent la nouvelle saison de Ligue 1 McDonald's. On y retrouve l'identité "
                 "des clubs et des villes à travers les couleurs, les joueurs et les références visuelles.",
        "services": ["Visuels réseaux sociaux", "Direction artistique", "Retouche"],
        "processus": [
            ("Idée", "Présenter la saison à travers ce qui fait l'identité de chaque club."),
            ("Recherches", "Couleurs, joueurs, monuments et références propres à chaque ville."),
            ("Création", "Des compositions riches, où chaque détail renvoie au club."),
            ("Déclinaisons", "Une série cohérente, pensée pour les réseaux."),
        ],
        "captures": [
            ("championnat-de-france/p26.jpg", "Chaque club raconté par ses couleurs et ses références."),
            ("championnat-de-france/cdf-cowboy.jpg", "Des clins d'œil visuels à l'identité de chaque ville."),
        ],
        "galerie": ["championnat-de-france/p26.jpg", "championnat-de-france/cdf-greenwood.jpg", "championnat-de-france/cdf-cowboy.jpg", "championnat-de-france/cdf-saison.jpg"],
    },
    {
        "slug": "ilan-djadja", "cat": "design", "titre": "Ilan Djadja", "date": "2025 – 2026",
        "cover": "ilan-djadja/ilan-dfco.jpg", "logo": ("ilan-73.png", 1.013, "#000000"),
        "client": "Ilan Djadja",
        "sous_titre": "Photos et visuels de match pour un joueur U19 National",
        "intro": "Ilan joue en U19 National. Frostbird le photographie pendant ses matchs et réalise des "
                 "visuels pour tous ses rendez-vous du week-end face à de gros clubs, notamment l'OL.",
        "services": ["Visuels réseaux sociaux", "Photographie", "Retouche"],
        "processus": [
            ("Brief", "Accompagner l'image d'un joueur qui vise un contrat professionnel."),
            ("Photographie", "Des photos prises en match, la matière première des visuels."),
            ("Création", "Un visuel pour chaque affiche du week-end, dans une ligne reconnaissable."),
            ("Diffusion", "Formats prêts pour ses réseaux, livrés avant chaque rencontre."),
        ],
        "captures": [
            ("ilan-djadja/ilan-dfco.jpg", "Un visuel pour chaque rendez-vous du week-end."),
            ("ilan-djadja/ilan-metz.jpg", "Une ligne graphique reconnaissable d'un match à l'autre."),
        ],
        "galerie": ["ilan-djadja/ilan-dfco.jpg", "ilan-djadja/ilan-auxerre.jpg", "ilan-djadja/ilan-dijon-asptt.jpg", "ilan-djadja/p27.jpg", "ilan-djadja/ilan-saintpriest.jpg", "ilan-djadja/ilan-metz.jpg"],
    },
    {
        "slug": "europa-league", "cat": "design", "titre": "Europa League", "date": "2024",
        "cover": "europa-league/p28.jpg", "logo": ("europa-league.png", 0.704, "#111111"),
        "client": "Quentin Merlin",
        "sous_titre": "Deux visuels de coupe d'Europe pour un joueur de l'Olympique de Marseille",
        "intro": "Quentin Merlin, alors joueur de l'Olympique de Marseille, a demandé deux visuels pour ses "
                 "matchs de coupe d'Europe contre l'Atalanta Bergame et le Shakhtar Donetsk. Deux "
                 "créations bien différentes, pour deux affiches européennes.",
        "services": ["Visuels réseaux sociaux", "Direction artistique", "Retouche"],
        "processus": [
            ("Brief", "Deux matchs européens, deux visuels à publier avant chaque rencontre."),
            ("Direction artistique", "Une ambiance propre à chaque adversaire."),
            ("Création", "Le joueur au centre, mis en scène dans l'univers de la compétition."),
            ("Diffusion", "Formats réseaux livrés avant le coup d'envoi."),
        ],
        "captures": [
            ("europa-league/p28.jpg", "Contre l'Atalanta Bergame."),
            ("europa-league/europa-shakhtar.jpg", "Contre le Shakhtar Donetsk : une tout autre ambiance."),
        ],
        "galerie": [],
    },
    {
        "slug": "aiman", "cat": "design", "titre": "Aïman", "date": "2025 – 2026",
        "cover": "aiman/aiman-orleans.jpg", "logo": ("afc-creil.png", 0.88, "#ffffff"),
        "client": "Aïman",
        "sous_titre": "Photos et visuels de match pour un joueur U19 National",
        "intro": "Aïman joue en U19 National. Frostbird le photographie pendant ses matchs et réalise des "
                 "visuels pour tous ses rendez-vous du week-end face à de gros clubs, notamment le PSG.",
        "services": ["Visuels réseaux sociaux", "Photographie", "Retouche"],
        "processus": [
            ("Brief", "Accompagner l'image d'un joueur qui vise un contrat professionnel."),
            ("Photographie", "Des photos prises en match, la matière première des visuels."),
            ("Création", "Un visuel pour chaque affiche du week-end, dans une ligne reconnaissable."),
            ("Diffusion", "Formats prêts pour ses réseaux, livrés avant chaque rencontre."),
        ],
        "captures": [
            ("aiman/aiman-orleans.jpg", "Un visuel pour chaque rendez-vous du week-end."),
            ("aiman/aiman-racing.jpg", "Le joueur en héros, match après match."),
        ],
        "galerie": ["aiman/aiman-orleans.jpg", "aiman/aiman-amiens.jpg", "aiman/p29.jpg", "aiman/aiman-quevilly.jpg", "aiman/aiman-racing.jpg", "aiman/aiman-sarcelles.jpg"],
    },
]
