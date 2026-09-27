# Notes quadrilingues · Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

Notes d’étude pour l’anglais, le français, l’allemand et le japonais : grammaire, vocabulaire, exemples, audio et fiches à télécharger. L’interface du site est en chinois traditionnel. Les exemples sont dans la langue étudiée.

La première leçon d’anglais, de français et d’allemand est une présentation A1. Le japonais suit le JLPT, de N5 à N2. Chaque exemple montre les kanji, les kana et le rōmaji.

| Langue | Leçon | Contenu |
| --- | --- | --- |
| Anglais | [`en/`](en/) | Grammaire de A1 à B2, à partir de be, have, be called |
| Français | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être, avoir, s’appeler |
| Allemand | [`de/`](de/) | Grammaire de A1 à B2 selon le CECR, à partir de sein, haben, heißen |
| Japonais | [`ja/`](ja/) | Grammaire de N5 à N2, exemples avec kanji, kana et rōmaji |

## Structure du site

- `index.html` : entrée vers l’anglais, le français, l’allemand et le japonais
- `en/` : grammaire anglaise, de A1 à B2
- `fr/bonjour-verbes/` : fiche A1 de français et `Bonjour-Verbes-A1.pdf`
- `de/` : grammaire allemande de A1 à B2, selon le CECR
- `ja/` : grammaire japonaise du JLPT N5 au N2
- `tools/generate_pdf.py` : programme qui produit les PDF
- `tools/NotoSansTC.ttf` : police chinoise utilisée dans les PDF

## Publier sur GitHub Pages

Placez les fichiers de ce dossier à la **racine de publication** du dépôt GitHub Pages, de sorte que `index.html` soit au premier niveau. S’ils sont dans un sous-dossier d’un site personnel déjà en ligne (par exemple `study-notes/`), l’adresse sera `https://<username>.github.io/study-notes/`. Les liens sont relatifs : les deux dispositions fonctionnent.

Nom du dépôt GitHub : `polyglot-study-notes`

GitHub About : `English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## Ajouter une leçon

Placez le nouvel article dans le dossier de la langue, ajoutez-le à la liste du `index.html` de cette langue, puis reliez cette section depuis la page d’accueil. La lecture des exemples utilise l’API Web Speech du navigateur : français `fr-FR`, anglais `en-US`, allemand `de-DE`, japonais `ja-JP`. La prononciation dépend des voix installées sur l’appareil.

## Produire les PDF

Les PDF d’anglais, de français et d’allemand viennent de `python3 tools/generate_pdf.py`. Les pages et PDF de japonais viennent de `python3 tools/build_ja_grammar.py`. Les deux ont besoin de `reportlab`. Le chinois utilise `tools/NotoSansTC.ttf`. Les PDF de japonais utilisent `tools/NotoSansJP.otf` s’il est présent, sinon Yu Gothic. Les lettres latines du PDF de français utilisent DejaVu Sans (`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`). Si cette police est absente, le script conserve le PDF de français déjà présent et génère quand même les PDF d’anglais et d’allemand.
