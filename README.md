# Polyglot Study Notes

[English](README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

**Audience first:** This project is built primarily for Chinese-speaking learners. Explanations, translations, and the site UI are in Chinese (Traditional Chinese on the live site), so people who use Chinese as their main language can study English, French, German, and Japanese more easily.

Study notes for English, French, German, and Japanese, with grammar, vocabulary, examples, audio practice, and downloadable sheets. Example sentences are in the language being studied.

English, French, and German follow the CEFR from A1 through B2. Japanese follows the JLPT from N5 through N2, and every example shows kanji, kana, and romaji.

| Language | Lessons | Contents |
| --- | --- | --- |
| English | [`en/`](en/) | A1–B2 grammar, starting with be, have, be called |
| French | [`fr/`](fr/) | A1–B2 grammar on the CEFR scale, starting with être, avoir, s’appeler |
| German | [`de/`](de/) | A1–B2 grammar on the CEFR scale, starting with sein, haben, heißen |
| Japanese | [`ja/`](ja/) | N5–N2 grammar, with kanji, kana, and romaji on every example |

## Site layout

- `index.html`: entry point for English, French, German, and Japanese
- `en/`: English grammar from A1 through B2
- `fr/`: French grammar from CEFR A1 to B2
- `de/`: German grammar from A1 to B2, following the CEFR
- `ja/`: Japanese grammar from JLPT N5 to N2
- `tables/`: multilingual comparison tables
- `tools/`: page and PDF builders
- `tools/NotoSansTC.ttf`: Chinese font used in the PDFs

## Deploy to GitHub Pages

Put the files in this directory at the **publishing root** of a GitHub Pages repository, so `index.html` sits at the top of that directory. If the site lives in a subdirectory of an existing personal site (for example `study-notes/`), the URL is `https://<username>.github.io/study-notes/`. Links are relative, so both setups work.

GitHub repository name: `polyglot-study-notes`

GitHub About: `Study notes for English, French, German, and Japanese—built first for Chinese-speaking learners—with grammar, vocabulary, examples, audio, and downloadable sheets.`

## Add a lesson

Put a new article in that language’s folder, add it to the list in that language’s `index.html`, and link to the section from the home page. Example audio uses the browser Web Speech API: French `fr-FR`, English `en-US`, German `de-DE`, Japanese `ja-JP`. Pronunciation depends on the voices installed on the device.

## Generate the PDFs

English PDFs: `python3 tools/build_en_grammar.py`. German: `python3 tools/build_de_grammar.py`. French: `python3 tools/build_fr_grammar.py`. Japanese: `python3 tools/build_ja_grammar.py`. These need `reportlab`. Chinese and French use the bundled `tools/NotoSansTC.ttf`. Japanese PDFs use `tools/NotoSansJP.otf` when present, otherwise Yu Gothic.
