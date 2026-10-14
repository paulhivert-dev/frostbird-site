# frostbird.fr

Site de l'agence Frostbird — site statique généré par `build.py`.

- Contenu : `build.py` (pages, projets web et photo), `contenu_portfolio.py` (projets repris du
  portfolio), `contenu_prestations.py` (pages prestation).
- Styles et scripts : `public/assets/css/style.css`, `public/assets/js/site.js` (édités à la main).
- Images d'origine (JPG/PNG) dans `media/` : le build en tire des WebP et des vignettes 800 px
  dans `public/` (seules ces versions sont en ligne). Ajouter une image = la déposer dans `media/`.
- Générer : `python3 build.py` (Pillow requis) → met à jour `public/`.
- En ligne : Vercel publie `public/` tel quel à chaque push sur `main` (cf. `vercel.json`).
