# 四言語ノート · Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

英語・フランス語・ドイツ語・日本語の学習ノートです。文法、語彙、例文、音声、ダウンロードできる教材をまとめています。サイトの表示は繁体字中国語で、例文は学習中の言語です。

4言語とも最初の課は A1 の自己紹介です。人称6つ、例文18、中国語訳、再生ボタン、PDF が付きます。

| 言語 | 教材 | 内容 |
| --- | --- | --- |
| 英語 | [`en/`](en/) | A1 から B2 の基礎文法。最初は be、have、be called |
| フランス語 | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être、avoir、s’appeler |
| ドイツ語 | [`de/`](de/) | A1 から B2 の基礎文法。GER に沿い、sein、haben、heißen から |
| 日本語 | [`ja/konnichiwa-doushi/`](ja/konnichiwa-doushi/) | です、あります／います、と言います |

## サイト構成

- `index.html`：英・仏・独・日の入口
- `en/`：英語の基礎文法。A1、A2、B1、B2 の順
- `fr/bonjour-verbes/`：フランス語 A1 の動詞教材と `Bonjour-Verbes-A1.pdf`
- `de/`：ドイツ語の基礎文法。GER の A1、A2、B1、B2 の順
- `ja/konnichiwa-doushi/`：日本語 A1 の言い方教材と `Konnichiwa-Doushi-A1.pdf`
- `tools/generate_pdf.py`：PDF を作るプログラム
- `tools/NotoSansTC.ttf`：PDF 用の中国語フォント

## GitHub Pages への公開

このディレクトリのファイルを GitHub Pages リポジトリの**公開ルート**に置き、`index.html` がその直下に来るようにします。既存サイトのサブディレクトリ（例：`study-notes/`）に置く場合、URL は `https://<username>.github.io/study-notes/` になります。リンクは相対パスなので、どちらでも使えます。

GitHub repository name：`polyglot-study-notes`

GitHub About：`English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## 記事を追加する

新しい記事はその言語のフォルダに入れ、その言語の `index.html` の一覧を直し、トップページからその欄へリンクします。例文の読み上げはブラウザの Web Speech API です。フランス語は `fr-FR`、英語は `en-US`、ドイツ語は `de-DE`、日本語は `ja-JP`。音質は端末に入っている音声によります。

## PDF を作る

`python3 tools/generate_pdf.py` を実行します。`reportlab` が必要です。中国語と英・独・日の本文は、同梱の `tools/NotoSansTC.ttf` を使い、PDF で中国語が抜けないようにしています。フランス語 PDF のラテン文字は、システムの DejaVu Sans（`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`）を使います。このフォントが無い場合、既存のフランス語 PDF はそのまま残し、英・独・日の PDF は生成します。
