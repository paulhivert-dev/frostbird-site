"""Pages prestation-<clé>.html : une histoire et une mise en scène propres à chaque métier.

Inspiré de l'esprit des pages prestations de makak-makak.com (une page = une idée, racontée en
chapitres plein écran), sans en reprendre les histoires. Les visuels sont les vrais projets Frostbird.

Chaque page est une liste de blocs ; types disponibles (rendus par build.py) :
  titre     : grande phrase sur une ou deux lignes (fond crème, rouge ou bordeaux)
  test      : une épreuve du crash-test de logo (visuel : geant, minuscule, ticket, eclair)
  mur       : mur de logos clients (fichiers de assets/img/clients)
  chiffre   : un chiffre géant, son explication et sa source
  temps     : un temps (« 0,3 s »), une phrase et une image de projet
  bande     : une bande d'images qui défile en continu
  horloge   : une heure en grand et une phrase (fond au choix)
  attente   : un téléphone qui charge… sans fin
  ecrans    : des écrans d'application dans des cadres de téléphone
  regard    : « Vous voyez… » / « On voit… » sur une grande photo
  video     : une vidéo muette en boucle et sa légende
  final     : la question, la réponse et le bouton de contact
"""

PAGES = {
    # ------------------------------------------------------------------ BRANDING : le crash-test
    "branding": [
        {"type": "titre", "l1": "Un logo, ça se teste.", "l2": "Comme une voiture : au crash-test.", "tag": True},
        {"type": "test", "n": 1, "titre": "En géant.",
         "texte": "Sur une façade, un camion, un maillot. De près, il ne doit rien perdre.", "visuel": "geant"},
        {"type": "test", "n": 2, "titre": "En minuscule.",
         "texte": "Seize pixels dans un onglet, deux centimètres sur une étiquette. Il doit rester lui-même.",
         "visuel": "minuscule"},
        {"type": "test", "n": 3, "titre": "Sans couleur.",
         "texte": "Imprimé en noir sur un ticket de caisse, photocopié, tamponné. Aucune excuse.",
         "visuel": "ticket"},
        {"type": "test", "n": 4, "titre": "En un éclair.",
         "texte": "Aperçu à 110 km/h sur un panneau. On a moins d'une seconde pour le reconnaître.",
         "visuel": "eclair"},
        {"type": "titre", "l1": "Verdict :", "l2": "les nôtres passent tous les tests.", "fond": "rouge"},
        {"type": "mur", "logos": [("atlantic.png", 1.907), ("rooster.png", 2.662), ("spike.png", 0.695),
                                  ("happy-propaganda.png", 1.393), ("first-touch.svg", 2.057),
                                  ("le-charles.png", 1.677), ("oh-damned.png", 2.591), ("gomu-burger.png", 1.551)]},
        {"type": "final", "question": "Et le vôtre, il tiendrait le choc ?", "reponse": "Faisons le test."},
    ],
    # ------------------------------------------------------------------ DESIGN GRAPHIQUE : le chrono
    "design": [
        {"type": "chiffre", "nombre": "1,7 s",
         "texte": "C'est le temps moyen qu'on accorde à un contenu en le faisant défiler sur son téléphone.",
         "source": "Facebook IQ, « Capturing Attention in Feed », 2016."},
        {"type": "titre", "l1": "Une affiche, un menu, un visuel :", "l2": "tout se joue avant la fin du chrono."},
        {"type": "temps", "t": "0,3 s", "texte": "On vous voit.",
         "detail": "Une couleur, un contraste, une forme qui arrête le pouce.",
         "img": "gomu-affiches/p17.jpg"},
        {"type": "temps", "t": "1 s", "texte": "On vous comprend.",
         "detail": "Un seul message, une hiérarchie évidente : produit, offre, marque.",
         "img": "chikin-bang-affiches/chikin-korean-burgers.jpg"},
        {"type": "temps", "t": "1,7 s", "texte": "On a faim.",
         "detail": "L'envie est là. Le reste, c'est le chemin jusqu'au comptoir.",
         "img": "gomu-californian/cal-jalapeno-1.jpg"},
        {"type": "bande", "images": ["gomu-affiches/gomu-waffle.jpg", "chikin-bang-affiches/chikin-paques.jpg",
                                     "gomu-affiches/p19.jpg", "gomu-californian/cal-cheese.jpg",
                                     "chikin-bang-affiches/chikin-cheddar.jpg", "gomu-affiches/p21.jpg",
                                     "gomu-californian/cal-californians.jpg", "gomu-affiches/p20.jpg"]},
        {"type": "final", "question": "Et vos visuels, ils tiennent combien de temps ?",
         "reponse": "Donnez-nous 1,7 seconde."},
    ],
    # ------------------------------------------------------------------ WEB & APPS : le visiteur pressé
    "web": [
        {"type": "horloge", "heure": "21:47", "texte": "Quelqu'un cherche « restaurant ouvert près de moi ».",
         "fond": "bordeaux"},
        {"type": "titre", "l1": "Il tombe sur vous.", "l2": "Votre site commence à charger…"},
        {"type": "attente"},
        {"type": "chiffre", "nombre": "53 %",
         "texte": "des visites sur mobile sont abandonnées quand une page met plus de 3 secondes à s'afficher.",
         "source": "Google / DoubleClick, « The Need for Mobile Speed », 2016."},
        {"type": "titre", "l1": "Trois secondes plus tard,", "l2": "il réserve chez le voisin.", "fond": "rouge"},
        {"type": "horloge", "heure": "21:47", "texte": "On rembobine. Même soir, même recherche.",
         "fond": "creme", "rembobine": True},
        {"type": "titre", "l1": "Cette fois, tout s'affiche", "l2": "avant qu'il ait cligné des yeux."},
        {"type": "ecrans", "texte": "Des écrans qu'on comprend sans réfléchir, qui s'affichent sans attendre.",
         "images": ["cx-mobile.jpg", "ph-mobile.jpg"]},
        {"type": "final", "question": "Et votre site, il garde ses visiteurs ?",
         "reponse": "On s'occupe du chrono."},
    ],
    # ------------------------------------------------------------------ PHOTOGRAPHIE : ce qu'on voit
    "photo": [
        {"type": "titre", "l1": "Vous et nous,", "l2": "on ne regarde pas la même chose.", "tag": True},
        {"type": "regard", "vous": "Vous voyez un burger.",
         "nous": "On voit une sauce qui coule au bon moment, sous une lumière qui vient de la gauche.",
         "img": "birdz/birdz-15.jpg"},
        {"type": "regard", "vous": "Vous voyez un match.",
         "nous": "On voit l'instant exact où le ballon quitte le pied.",
         "img": "national/national-08.jpg"},
        {"type": "regard", "vous": "Vous voyez un bar.",
         "nous": "On voit le marbre qui s'allume quand la salle s'éteint.",
         "img": "raffine/raffine-12.jpg"},
        {"type": "video", "src": "birdz/coulisses.mp4",
         "texte": "Et derrière chaque image, il y a ça : une table, une lumière, et beaucoup de patience."},
        {"type": "final", "question": "Et chez vous, qu'est-ce qu'on verrait ?", "reponse": "Venez, on vous montre."},
    ],
}
