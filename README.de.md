# Viersprachige Notizen · Polyglot Study Notes

[English](README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

**Zielgruppe zuerst:** Dieses Projekt ist vorrangig für Lernende aus dem chinesischsprachigen Raum gedacht. Erklärungen, Übersetzungen und die Website-Oberfläche sind auf Chinesisch (auf der Live-Site Traditionelles Chinesisch), damit Menschen, deren Hauptsprache Chinesisch ist, Englisch, Französisch, Deutsch und Japanisch leichter lernen können.

Lernnotizen für Englisch, Französisch, Deutsch und Japanisch, mit Grammatik, Wortschatz, Beispielsätzen, Audio und herunterladbaren Blättern. Die Beispielsätze stehen in der Sprache, die gerade gelernt wird.

Englisch, Französisch und Deutsch folgen dem GER von A1 bis B2. Japanisch folgt dem JLPT von N5 bis N2. Jedes japanische Beispiel zeigt Kanji, Kana und Romaji.

| Sprache | Lektion | Inhalt |
| --- | --- | --- |
| Englisch | [`en/`](en/) | Grammatik von A1 bis B2, beginnend mit be, have, be called |
| Französisch | [`fr/`](fr/) | Grammatik von A1 bis B2 nach dem GER, beginnend mit être, avoir, s’appeler |
| Deutsch | [`de/`](de/) | Grammatik von A1 bis B2 nach dem GER, beginnend mit sein, haben, heißen |
| Japanisch | [`ja/`](ja/) | Grammatik von N5 bis N2, Beispiele mit Kanji, Kana und Romaji |

## Aufbau der Website

- `index.html`: Einstieg zu Englisch, Französisch, Deutsch und Japanisch
- `en/`: englische Grammatik von A1 bis B2
- `fr/`: französische Grammatik von A1 bis B2 nach dem GER
- `de/`: deutsche Grammatik von A1 bis B2 nach dem GER
- `ja/`: japanische Grammatik von JLPT N5 bis N2
- `tables/`: mehrsprachige Vergleichstabellen
- `tools/`: Programme für Seiten und PDFs
- `tools/NotoSansTC.ttf`: chinesische Schrift für die PDFs

## Auf GitHub Pages veröffentlichen

Legen Sie die Dateien dieses Ordners ins **Veröffentlichungsverzeichnis** eines GitHub-Pages-Repositorys, sodass `index.html` dort zuoberst liegt. Liegt die Seite in einem Unterordner einer bestehenden persönlichen Website (zum Beispiel `study-notes/`), lautet die Adresse `https://<username>.github.io/study-notes/`. Die Links sind relativ, beide Varianten funktionieren.

GitHub-Repository-Name: `polyglot-study-notes`

GitHub About: `Study notes for English, French, German, and Japanese—built first for Chinese-speaking learners—with grammar, vocabulary, examples, audio, and downloadable sheets.`

## Eine Lektion hinzufügen

Legen Sie den neuen Text in den Ordner der Sprache, tragen Sie ihn in die Liste der `index.html` dieser Sprache ein und verlinken Sie den Bereich von der Startseite. Die Beispiele werden über die Web Speech API des Browsers vorgelesen: Französisch `fr-FR`, Englisch `en-US`, Deutsch `de-DE`, Japanisch `ja-JP`. Die Aussprache hängt von den auf dem Gerät installierten Stimmen ab.

## PDFs erzeugen

Englisch: `python3 tools/build_en_grammar.py`. Deutsch: `python3 tools/build_de_grammar.py`. Französisch: `python3 tools/build_fr_grammar.py`. Japanisch: `python3 tools/build_ja_grammar.py`. Dafür wird `reportlab` benötigt. Chinesisch und Französisch nutzen `tools/NotoSansTC.ttf`. Japanische PDFs nutzen `tools/NotoSansJP.otf`, falls vorhanden, sonst Yu Gothic.
