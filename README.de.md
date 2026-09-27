# Viersprachige Notizen · Polyglot Study Notes

[繁體中文](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md)

Lernnotizen für Englisch, Französisch, Deutsch und Japanisch, mit Grammatik, Wortschatz, Beispielsätzen, Audio und herunterladbaren Blättern. Die Oberfläche der Website ist auf Traditionellem Chinesisch. Die Beispielsätze stehen in der Sprache, die gerade gelernt wird.

Die erste Lektion in Englisch, Französisch und Deutsch ist eine A1-Vorstellung. Japanisch folgt dem JLPT von N5 bis N2. Jedes Beispiel zeigt Kanji, Kana und Romaji.

| Sprache | Lektion | Inhalt |
| --- | --- | --- |
| Englisch | [`en/`](en/) | Grammatik von A1 bis B2, beginnend mit be, have, be called |
| Französisch | [`fr/bonjour-verbes/`](fr/bonjour-verbes/) | être, avoir, s’appeler |
| Deutsch | [`de/`](de/) | Grammatik von A1 bis B2 nach dem GER, beginnend mit sein, haben, heißen |
| Japanisch | [`ja/`](ja/) | Grammatik von N5 bis N2, Beispiele mit Kanji, Kana und Romaji |

## Aufbau der Website

- `index.html`: Einstieg zu Englisch, Französisch, Deutsch und Japanisch
- `en/`: englische Grammatik von A1 bis B2
- `fr/bonjour-verbes/`: französisches A1-Blatt und `Bonjour-Verbes-A1.pdf`
- `de/`: deutsche Grammatik von A1 bis B2 nach dem GER
- `ja/`: japanische Grammatik von JLPT N5 bis N2
- `tools/generate_pdf.py`: Programm, das die PDFs erzeugt
- `tools/NotoSansTC.ttf`: chinesische Schrift für die PDFs

## Auf GitHub Pages veröffentlichen

Legen Sie die Dateien dieses Ordners ins **Veröffentlichungsverzeichnis** eines GitHub-Pages-Repositorys, sodass `index.html` dort zuoberst liegt. Liegt die Seite in einem Unterordner einer bestehenden persönlichen Website (zum Beispiel `study-notes/`), lautet die Adresse `https://<username>.github.io/study-notes/`. Die Links sind relativ, beide Varianten funktionieren.

GitHub-Repository-Name: `polyglot-study-notes`

GitHub About: `English, French, German, and Japanese study notes with grammar, vocabulary, examples, audio practice, and downloadable learning sheets.`

## Eine Lektion hinzufügen

Legen Sie den neuen Text in den Ordner der Sprache, tragen Sie ihn in die Liste der `index.html` dieser Sprache ein und verlinken Sie den Bereich von der Startseite. Die Beispiele werden über die Web Speech API des Browsers vorgelesen: Französisch `fr-FR`, Englisch `en-US`, Deutsch `de-DE`, Japanisch `ja-JP`. Die Aussprache hängt von den auf dem Gerät installierten Stimmen ab.

## PDFs erzeugen

PDFs für Englisch, Französisch und Deutsch erzeugt `python3 tools/generate_pdf.py`. Japanische Seiten und PDFs erzeugt `python3 tools/build_ja_grammar.py`. Beides braucht `reportlab`. Chinesisch nutzt `tools/NotoSansTC.ttf`. Japanische PDFs nutzen `tools/NotoSansJP.otf`, falls vorhanden, sonst Yu Gothic. Lateinische Buchstaben im französischen PDF nutzen DejaVu Sans (`/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`). Fehlt diese Schrift, bleibt das vorhandene französische PDF unverändert, und die PDFs für Englisch und Deutsch werden trotzdem erzeugt.
