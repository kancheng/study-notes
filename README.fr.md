# Notes quadrilingues · Polyglot Study Notes

[English](README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

**Public prioritaire :** Ce projet est conçu en priorité pour les apprenants sinophones. Les explications, les traductions et l’interface du site sont en chinois (chinois traditionnel sur le site en ligne), afin que les personnes dont la langue principale est le chinois puissent plus facilement apprendre l’anglais, le français, l’allemand et le japonais.

Notes d’étude pour l’anglais, le français, l’allemand et le japonais : grammaire, vocabulaire, exemples, audio et fiches à télécharger. Les exemples sont dans la langue étudiée.

L’anglais, le français et l’allemand suivent le CECRL de A1 à B2. Le japonais suit le JLPT, de N5 à N2. Chaque exemple japonais montre les kanji, les kana et le rōmaji.

| Langue | Leçon | Contenu |
| --- | --- | --- |
| Anglais | [`en/`](en/) | Grammaire de A1 à B2, à partir de be, have, be called |
| Français | [`fr/`](fr/) | Grammaire de A1 à B2 selon le CECRL, à partir de être, avoir, s’appeler |
| Allemand | [`de/`](de/) | Grammaire de A1 à B2 selon le CECR, à partir de sein, haben, heißen |
| Japonais | [`ja/`](ja/) | Grammaire de N5 à N2, exemples avec kanji, kana et rōmaji |

## Structure du site

- `index.html` : entrée vers l’anglais, le français, l’allemand et le japonais
- `en/` : grammaire anglaise, de A1 à B2
- `fr/` : grammaire française de A1 à B2 selon le CECRL
- `de/` : grammaire allemande de A1 à B2, selon le CECR
- `ja/` : grammaire japonaise du JLPT N5 au N2
- `tables/` : tableaux de comparaison multilingues
- `tools/` : générateurs de pages et de PDF
- `tools/NotoSansTC.ttf` : police chinoise utilisée dans les PDF

## Publier sur GitHub Pages

Placez les fichiers de ce dossier à la **racine de publication** du dépôt GitHub Pages, de sorte que `index.html` soit au premier niveau. S’ils sont dans un sous-dossier d’un site personnel déjà en ligne (par exemple `study-notes/`), l’adresse sera `https://<username>.github.io/study-notes/`. Les liens sont relatifs : les deux dispositions fonctionnent.

Nom du dépôt GitHub : `polyglot-study-notes`

GitHub About : `Study notes for English, French, German, and Japanese—built first for Chinese-speaking learners—with grammar, vocabulary, examples, audio, and downloadable sheets.`

## Ajouter une leçon

Placez le nouvel article dans le dossier de la langue, ajoutez-le à la liste du `index.html` de cette langue, puis reliez cette section depuis la page d’accueil. La lecture des exemples utilise l’API Web Speech du navigateur : français `fr-FR`, anglais `en-US`, allemand `de-DE`, japonais `ja-JP`. La prononciation dépend des voix installées sur l’appareil.

## Produire les PDF

Anglais : `python3 tools/build_en_grammar.py`. Allemand : `python3 tools/build_de_grammar.py`. Français : `python3 tools/build_fr_grammar.py`. Japonais : `python3 tools/build_ja_grammar.py`. Ces programmes ont besoin de `reportlab`. Le chinois et le français utilisent `tools/NotoSansTC.ttf`. Les PDF de japonais utilisent `tools/NotoSansJP.otf` s’il est présent, sinon Yu Gothic.
