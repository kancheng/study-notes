# 四語筆記 · Polyglot Study Notes

English, French, German, and Japanese study notes with grammar, vocabulary, examples, and downloadable learning sheets. Starting with French A1.

四種語言的長期學習筆記網站。目前法文課優先；進入法文區後，從清單開啟第一篇是 **être、avoir、s’appeler 的現在式**，包含六組人稱、18 個例句、中文翻譯、法語朗讀按鈕與 PDF。

## 網站結構

- `index.html`：英、法、德、日入口
- `fr/index.html`：法文筆記清單
- `fr/bonjour-verbes/index.html`：法文 A1 動詞教材
- `fr/bonjour-verbes/Bonjour-Verbes-A1.pdf`：教材 PDF
- `en/`、`de/`、`ja/`：後續新增筆記的入口
- `tools/generate_pdf.py`：PDF 產生程式

## 部署至 GitHub Pages

將本目錄中的檔案放到 GitHub Pages 儲存庫的**發佈根目錄**，讓 `index.html` 位於該目錄最上層。若放在既有個人網站的子目錄（例如 `study-notes/`），網址會是 `https://<username>.github.io/study-notes/`。網站使用相對路徑，兩種方式都能使用。

GitHub repository name：`polyglot-study-notes`

GitHub About：`English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## 後續更新

各語言的新文章可放入對應資料夾；修改該語言 `index.html` 的文章清單，再從首頁導向該區。法語語音使用瀏覽器的 Web Speech API，發音品質依裝置內安裝的法語語音而異。

## 產生 PDF

執行 `python3 tools/generate_pdf.py`。需要 `reportlab`；字型檔 `tools/NotoSansTC.ttf` 已附於專案中，避免繁體中文在 PDF 裡消失。
