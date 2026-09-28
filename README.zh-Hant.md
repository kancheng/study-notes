# 四語筆記 · Polyglot Study Notes

[English](README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

**讀者優先說明：** 本專案目前優先支持華語圈使用者學習。說明、翻譯與網站介面以中文為主（線上版為繁體中文），方便以中文為主要語言的人學習英文、法文、德文與日文。

英語、法語、德語、日語的學習筆記，含文法、詞彙、例句、朗讀與可下載講義。例句是正在學的那種語言。

英文、法文與德文依歐洲語言共同參考架構從 A1 排到 B2。日文依 JLPT 從 N5 排到 N2，例句附漢字、假名與羅馬拼音。

| 語言 | 教材 | 內容 |
| --- | --- | --- |
| 英文 | [`en/`](en/) | A1 到 B2 基礎文法，從 be、have、be called 開始 |
| 法文 | [`fr/`](fr/) | A1 到 B2 基礎文法，依 CECRL，從 être、avoir、s’appeler 開始 |
| 德文 | [`de/`](de/) | A1 到 B2 基礎文法，依 GER，從 sein、haben、heißen 開始 |
| 日文 | [`ja/`](ja/) | N5 到 N2 基礎文法，例句附漢字、假名與羅馬拼音 |

## 網站結構

- `index.html`：英、法、德、日入口
- `en/`：英文基礎文法，依 A1、A2、B1、B2 排列
- `fr/`：法文基礎文法，依 CECRL 的 A1、A2、B1、B2 排列
- `de/`：德文基礎文法，依 GER 的 A1、A2、B1、B2 排列
- `ja/`：日文基礎文法，依 JLPT 的 N5、N4、N3、N2 排列
- `tables/`：多語對照表
- `tools/`：頁面與 PDF 建置程式
- `tools/NotoSansTC.ttf`：PDF 用的中文字型

## 部署至 GitHub Pages

將本目錄中的檔案放到 GitHub Pages 儲存庫的**發佈根目錄**，讓 `index.html` 位於該目錄最上層。若放在既有個人網站的子目錄（例如 `study-notes/`），網址會是 `https://<username>.github.io/study-notes/`。網站使用相對路徑，兩種方式都能使用。

GitHub repository name：`polyglot-study-notes`

GitHub About：`Study notes for English, French, German, and Japanese—built first for Chinese-speaking learners—with grammar, vocabulary, examples, audio, and downloadable sheets.`

## 新增文章

各語言的新文章可放入對應資料夾，修改該語言 `index.html` 的文章清單，再從首頁導向該區。例句朗讀使用瀏覽器的 Web Speech API：法文 `fr-FR`、英文 `en-US`、德文 `de-DE`、日文 `ja-JP`。發音品質依裝置內安裝的語音而異。

## 產生 PDF

英文：`python3 tools/build_en_grammar.py`。德文：`python3 tools/build_de_grammar.py`。法文：`python3 tools/build_fr_grammar.py`。日文：`python3 tools/build_ja_grammar.py`。這些程式都需要 `reportlab`。中文與法文使用專案內的 `tools/NotoSansTC.ttf`。日文 PDF 優先使用 `tools/NotoSansJP.otf`，否則使用系統的 Yu Gothic。
