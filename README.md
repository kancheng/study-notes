# 四語筆記 · Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

英語、法語、德語、日語的學習筆記，含文法、詞彙、例句、朗讀與可下載講義。網站介面是繁體中文，例句是正在學的那種語言。

四種語言的第一篇都是 A1 自我介紹：六組人稱、18 個例句、中文翻譯、朗讀按鈕與 PDF。

| 語言 | 教材 | 內容 |
| --- | --- | --- |
| 英文 | [`en/`](en/) | A1 到 B2 基礎文法，從 be、have、be called 開始 |
| 法文 | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être、avoir、s’appeler |
| 德文 | [`de/`](de/) | A1 到 B2 基礎文法，依 GER，從 sein、haben、heißen 開始 |
| 日文 | [`ja/konnichiwa-doushi/`](ja/konnichiwa-doushi/) | です、あります／います、と言います |

## 網站結構

- `index.html`：英、法、德、日入口
- `en/`：英文基礎文法，依 A1、A2、B1、B2 排列
- `fr/bonjour-verbes/`：法文 A1 動詞教材與 `Bonjour-Verbes-A1.pdf`
- `de/`：德文基礎文法，依 GER 的 A1、A2、B1、B2 排列
- `ja/konnichiwa-doushi/`：日文 A1 說法教材與 `Konnichiwa-Doushi-A1.pdf`
- `tools/generate_pdf.py`：PDF 產生程式
- `tools/NotoSansTC.ttf`：PDF 用的中文字型

## 部署至 GitHub Pages

將本目錄中的檔案放到 GitHub Pages 儲存庫的**發佈根目錄**，讓 `index.html` 位於該目錄最上層。若放在既有個人網站的子目錄（例如 `study-notes/`），網址會是 `https://<username>.github.io/study-notes/`。網站使用相對路徑，兩種方式都能使用。

GitHub repository name：`polyglot-study-notes`

GitHub About：`English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## 新增文章

各語言的新文章可放入對應資料夾，修改該語言 `index.html` 的文章清單，再從首頁導向該區。例句朗讀使用瀏覽器的 Web Speech API：法文 `fr-FR`、英文 `en-US`、德文 `de-DE`、日文 `ja-JP`。發音品質依裝置內安裝的語音而異。

## 產生 PDF

執行 `python3 tools/generate_pdf.py`。需要 `reportlab`。中文與英、德、日內文使用專案內的 `tools/NotoSansTC.ttf`，避免中文在 PDF 裡消失。法文 PDF 的拉丁字母使用系統上的 DejaVu Sans（`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`）。找不到這套字型時，腳本會保留既有的法文 PDF，英、德、日 PDF 仍會產生。
