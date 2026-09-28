# 四言語ノート · Polyglot Study Notes

[English](README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

**対象について：** このプロジェクトは、いまのところ中国語圏の学習者を優先して作っています。説明・訳・サイト表示は中国語中心（公開サイトは繁体字）で、中国語を主な言語とする人が英語・フランス語・ドイツ語・日本語を学びやすいようにしています。

英語・フランス語・ドイツ語・日本語の学習ノートです。文法、語彙、例文、音声、ダウンロードできる教材をまとめています。例文は学習中の言語です。

英語・フランス語・ドイツ語は CEFR／GER の A1 から B2 までです。日本語は JLPT の N5 から N2 までで、例文には漢字、仮名、ローマ字が付きます。

| 言語 | 教材 | 内容 |
| --- | --- | --- |
| 英語 | [`en/`](en/) | A1 から B2 の基礎文法。最初は be、have、be called |
| フランス語 | [`fr/`](fr/) | A1 から B2 の基礎文法。CECRL に沿い、être、avoir、s’appeler から |
| ドイツ語 | [`de/`](de/) | A1 から B2 の基礎文法。GER に沿い、sein、haben、heißen から |
| 日本語 | [`ja/`](ja/) | N5 から N2 の基礎文法。例文に漢字、仮名、ローマ字 |

## サイト構成

- `index.html`：英・仏・独・日の入口
- `en/`：英語の基礎文法。A1、A2、B1、B2 の順
- `fr/`：フランス語の基礎文法。CECRL の A1、A2、B1、B2 の順
- `de/`：ドイツ語の基礎文法。GER の A1、A2、B1、B2 の順
- `ja/`：日本語の基礎文法。JLPT の N5、N4、N3、N2 の順
- `tables/`：多言語対照表
- `tools/`：ページと PDF の生成プログラム
- `tools/NotoSansTC.ttf`：PDF 用の中国語フォント

## GitHub Pages への公開

このディレクトリのファイルを GitHub Pages リポジトリの**公開ルート**に置き、`index.html` がその直下に来るようにします。既存サイトのサブディレクトリ（例：`study-notes/`）に置く場合、URL は `https://<username>.github.io/study-notes/` になります。リンクは相対パスなので、どちらでも使えます。

GitHub repository name：`polyglot-study-notes`

GitHub About：`Study notes for English, French, German, and Japanese—built first for Chinese-speaking learners—with grammar, vocabulary, examples, audio, and downloadable sheets.`

## 記事を追加する

新しい記事はその言語のフォルダに入れ、その言語の `index.html` の一覧を直し、トップページからその欄へリンクします。例文の読み上げはブラウザの Web Speech API です。フランス語は `fr-FR`、英語は `en-US`、ドイツ語は `de-DE`、日本語は `ja-JP`。音質は端末に入っている音声によります。

## PDF を作る

英語は `python3 tools/build_en_grammar.py`、ドイツ語は `python3 tools/build_de_grammar.py`、フランス語は `python3 tools/build_fr_grammar.py`、日本語は `python3 tools/build_ja_grammar.py` で作ります。どれも `reportlab` が必要です。中国語とフランス語は同梱の `tools/NotoSansTC.ttf` を使います。日本語の PDF は `tools/NotoSansJP.otf` があればそれを、なければ Yu Gothic を使います。
