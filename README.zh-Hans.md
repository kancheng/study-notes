# 四语笔记 · Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

英语、法语、德语、日语的学习笔记，含语法、词汇、例句、朗读与可下载讲义。网站界面是繁体中文，例句是正在学的那种语言。

英文、法文、德文的第一篇是 A1 自我介绍。日文依 JLPT 从 N5 排到 N2，例句附汉字、假名与罗马拼音。

| 语言 | 教材 | 内容 |
| --- | --- | --- |
| 英文 | [`en/`](en/) | A1 到 B2 基础语法，从 be、have、be called 开始 |
| 法文 | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être、avoir、s’appeler |
| 德文 | [`de/`](de/) | A1 到 B2 基础语法，依 GER，从 sein、haben、heißen 开始 |
| 日文 | [`ja/`](ja/) | N5 到 N2 基础语法，例句附汉字、假名与罗马拼音 |

## 网站结构

- `index.html`：英、法、德、日入口
- `en/`：英文基础语法，按 A1、A2、B1、B2 排列
- `fr/bonjour-verbes/`：法文 A1 动词教材与 `Bonjour-Verbes-A1.pdf`
- `de/`：德文基础语法，依 GER 的 A1、A2、B1、B2 排列
- `ja/`：日文基础语法，依 JLPT 的 N5、N4、N3、N2 排列
- `tools/generate_pdf.py`：PDF 生成程序
- `tools/NotoSansTC.ttf`：PDF 用的中文字体

## 部署至 GitHub Pages

把本目录中的文件放到 GitHub Pages 仓库的**发布根目录**，让 `index.html` 位于该目录最上层。若放在已有个人网站的子目录（例如 `study-notes/`），网址会是 `https://<username>.github.io/study-notes/`。网站使用相对路径，两种方式都可以。

GitHub repository name：`polyglot-study-notes`

GitHub About：`English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## 新增文章

各语言的新文章可放入对应文件夹，修改该语言 `index.html` 的文章列表，再从首页导向该区。例句朗读使用浏览器的 Web Speech API：法文 `fr-FR`、英文 `en-US`、德文 `de-DE`、日文 `ja-JP`。发音质量取决于设备里安装的语音。

## 生成 PDF

英、法、德的 PDF 用 `python3 tools/generate_pdf.py`。日文页面与 PDF 用 `python3 tools/build_ja_grammar.py`。两者都需要 `reportlab`。中文使用项目内的 `tools/NotoSansTC.ttf`。日文 PDF 优先使用 `tools/NotoSansJP.otf`，否则使用系统的 Yu Gothic。法文 PDF 的拉丁字母使用系统上的 DejaVu Sans（`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`）。找不到这套字体时，脚本会保留已有的法文 PDF，英、德 PDF 仍会生成。
