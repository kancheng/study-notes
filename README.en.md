# Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

Study notes for English, French, German, and Japanese, with grammar, vocabulary, examples, audio, and downloadable sheets. The site interface is Traditional Chinese. Example sentences are in the language being studied.

The first lesson in each language is an A1 self-introduction: six persons, 18 examples, Chinese translations, a listen button, and a PDF.

| Language | Lesson | Contents |
| --- | --- | --- |
| English | [`en/`](en/) | A1–B2 grammar, starting with be, have, be called |
| French | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être, avoir, s’appeler |
| German | [`de/`](de/) | A1 to B2 grammar on the CEFR scale, starting with sein, haben, heißen |
| Japanese | [`ja/konnichiwa-doushi/`](ja/konnichiwa-doushi/) | です, あります／います, と言います |

## Site layout

- `index.html`: entry point for English, French, German, and Japanese
- `en/`: English grammar from A1 through B2
- `fr/bonjour-verbes/`: French A1 verb sheet and `Bonjour-Verbes-A1.pdf`
- `de/`: German grammar from A1 to B2, following the CEFR
- `ja/konnichiwa-doushi/`: Japanese A1 pattern sheet and `Konnichiwa-Doushi-A1.pdf`
- `tools/generate_pdf.py`: PDF generator
- `tools/NotoSansTC.ttf`: Chinese font used in the PDFs

## Deploy to GitHub Pages

Put the files in this directory at the **publishing root** of a GitHub Pages repository, so `index.html` sits at the top of that directory. If the site lives in a subdirectory of an existing personal site (for example `study-notes/`), the URL is `https://<username>.github.io/study-notes/`. Links are relative, so both setups work.

GitHub repository name: `polyglot-study-notes`

GitHub About: `English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## Add a lesson

Put a new article in that language’s folder, add it to the list in that language’s `index.html`, and link to the section from the home page. Example audio uses the browser Web Speech API: French `fr-FR`, English `en-US`, German `de-DE`, Japanese `ja-JP`. Pronunciation depends on the voices installed on the device.

## Generate the PDFs

Run `python3 tools/generate_pdf.py`. This requires `reportlab`. Chinese text, and the English, German, and Japanese sheets, use the bundled `tools/NotoSansTC.ttf` so Chinese does not disappear in the PDF. Latin text in the French PDF uses the system font DejaVu Sans (`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`). If that font is missing, the script leaves the existing French PDF in place and still writes the English, German, and Japanese PDFs.
