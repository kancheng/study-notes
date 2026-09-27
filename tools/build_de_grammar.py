"""Build the German grammar track: one folder, page, and PDF per lesson."""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).parent.parent
NOTO = Path(__file__).parent / 'NotoSansTC.ttf'
pdfmetrics.registerFont(TTFont('Chinese', str(NOTO)))

from de_lessons_a1 import LESSONS as A1
from de_lessons_a2 import LESSONS as A2
from de_lessons_b1 import LESSONS as B1
from de_lessons_b2 import LESSONS as B2

LEVELS = [
    ('A1', '能用簡單句子介紹自己、提問，並處理熟悉的日常需求'),
    ('A2', '能描述過去與身邊的事，比較事物，並用從句說明原因'),
    ('B1', '能連貫說明經驗、條件與看法，並處理旅行與工作中的大部分情況'),
    ('B2', '能讀寫較長的句子，轉述他人的話，並改寫句型'),
]
HELLO = {
    'slug': 'hallo-verben',
    'level': 'A1',
    'title': 'Hallo Verben',
    'meta': 'A1 · 動詞 · 例句跟讀',
    'card': 'sein、haben、heißen 的現在式：六組人稱對照、18 個德語例句、中文翻譯、發音與 PDF。',
    'skip': True,
}
LESSONS = [HELLO, *A1, *A2, *B1, *B2]

navy = HexColor('#17365e')
muted = HexColor('#53677c')
pale = HexColor('#eaf0f9')
line_color = HexColor('#dae2ed')
white = HexColor('#ffffff')
light = HexColor('#dde9ff')


def require_glyphs(lessons):
    from fontTools.ttLib import TTFont
    cmap = TTFont(str(NOTO)).getBestCmap()
    missing = []
    for lesson in lessons:
        if lesson.get('skip'):
            continue
        chunks = [lesson['title'], lesson['h1'], lesson['intro'], lesson['card'], lesson['tip'], *lesson['cols']]
        for group in lesson['groups']:
            chunks.extend([group['name'], group['meaning']])
            for row in group['rows']:
                if len(row) != 3:
                    raise SystemExit(f"{lesson['slug']} row is not 3 cells: {row}")
                chunks.extend(row)
            for example in group['examples']:
                if len(example) != 2:
                    raise SystemExit(f"{lesson['slug']} example is not a pair: {example}")
                chunks.extend(example)
        for chunk in chunks:
            for ch in chunk:
                if ch.isspace() or ord(ch) < 32:
                    continue
                if ord(ch) not in cmap:
                    missing.append(f"{lesson['slug']}:{ch} U+{ord(ch):04X}")
    if missing:
        unique = list(dict.fromkeys(missing))
        raise SystemExit('NotoSansTC missing glyphs:\n' + '\n'.join(unique[:80]))


def render_pdf(lesson):
    out = ROOT / 'de' / lesson['slug'] / lesson['pdf']
    out.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    font = 'Chinese'
    banner = f"{lesson['title']} - Deutsch {lesson['level']}"
    groups = lesson['groups']
    cols = lesson['cols']
    state = {'y': 0}

    def text(x, y, s, size=10, color=navy):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, y, s)

    def wrap(s, size, max_w):
        lines = []
        buf = ''
        for ch in s:
            trial = buf + ch
            if buf and stringWidth(trial, font, size) > max_w:
                lines.append(buf)
                buf = ch
            else:
                buf = trial
        if buf:
            lines.append(buf)
        return lines or ['']

    def heading(sub):
        c.setFillColor(navy)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        text(42, H - 49, banner, 18, white)
        text(43, H - 74, sub, 11, light)
        state['y'] = H - 123

    heading(lesson['pdf_sub'])
    total = len(groups)
    for i, group in enumerate(groups):
        if i:
            c.showPage()
            heading('句型對照與跟讀例句')
        y = state['y']
        text(42, y, group['name'], 16)
        text(42 + stringWidth(group['name'], font, 16) + 12, y, group['meaning'], 12, muted)
        y -= 28
        c.setFillColor(pale)
        c.roundRect(42, y - 5, W - 84, 25, 5, fill=1, stroke=0)
        text(55, y + 3, cols[0], 10)
        text(200, y + 3, cols[1], 10)
        text(400, y + 3, cols[2], 10)
        y -= 24
        for subject, form, zh in group['rows']:
            text(55, y, subject, 10)
            size = 10
            while size > 7 and stringWidth(form, font, size) > 185:
                size -= 1
            text(200, y, form, size)
            text(400, y, zh, 10)
            c.setStrokeColor(line_color)
            c.line(42, y - 8, W - 42, y - 8)
            y -= 26
        y -= 14
        text(42, y, '例句與翻譯', 13)
        y -= 22
        for line, zh in group['examples']:
            size = 10
            while size > 8 and stringWidth(line, font, size) > W - 110:
                size -= 1
            text(55, y, line, size)
            text(55, y - 16, zh, 10, muted)
            y -= 40
        if i == total - 1:
            y -= 4
            parts = []
            for part in lesson['tip'].split('\n'):
                parts.extend(wrap(part, 10, W - 84))
            for n, part in enumerate(parts):
                text(42, y - n * 14, part, 10, muted)
        c.setFont(font, 8)
        c.setFillColor(muted)
        c.drawRightString(W - 42, 28, f'{i + 1} / {total}')
    c.save()
    print(out)


PAGE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}｜德文 {level}</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC',sans-serif;color:#182a45;background:#f3f6fb}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:#132f55;color:white;padding:22px max(20px,calc((100vw - 1050px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1050px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.55rem;margin:0}}
p{{line-height:1.7}}
.intro{{margin-bottom:24px}}
.toolbar{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:20px 0 28px}}
.download,button{{cursor:pointer;border:0;border-radius:9px;font:inherit}}
.download{{display:inline-block;background:#df3349;color:white;padding:12px 18px;text-decoration:none;font-weight:700}}
.download:hover{{background:#b91f35}}
.note{{font-size:.92rem;color:#52647d}}
.card{{background:white;border:1px solid #dce4f0;border-radius:16px;box-shadow:0 8px 24px #142f5210;margin:20px 0;padding:23px}}
.cardhead{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}
.meaning{{color:#52647d}}
.tablewrap{{overflow-x:auto;margin-top:18px}}
table{{border-collapse:collapse;width:100%;min-width:680px;text-align:left}}
th{{background:#eaf0f9;font-size:.9rem}}
th,td{{padding:13px 14px;border-bottom:1px solid #e4e9f1}}
td:nth-child(2){{font-weight:750;color:#173e71}}
.examples{{margin-top:22px}}
.examples h3{{font-size:1.07rem;margin:0 0 10px}}
.example{{display:grid;grid-template-columns:1fr auto;align-items:center;gap:12px;padding:11px 0;border-top:1px solid #edf0f5}}
.line{{font-size:1.03rem;font-weight:700}}
.zh{{color:#53637b;margin-top:3px}}
.speak{{background:#e7f0fd;color:#163b6a;padding:9px 12px;min-width:84px}}
.speak:hover,.speak:focus-visible{{background:#cedffa;outline:2px solid #3769a9;outline-offset:2px}}
.tip{{background:#e9eff8;border-left:4px solid #5276aa;padding:14px 18px;border-radius:8px;margin-top:20px}}
.pager{{display:flex;justify-content:space-between;gap:12px;margin-top:22px}}
.pager a{{color:#1d6a4f;font-weight:750;text-decoration:none}}
.pager a:hover,.pager a:focus-visible{{text-decoration:underline}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.card{{padding:17px}}}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 德文筆記</a>　/　{title}</div></header>
<main>
<div class="intro">
<h1>{h1}</h1>
<p>{intro}</p>
<div class="toolbar">
<a class="download" href="./{pdf}" download>下載完整 PDF</a>
<span class="note">發音使用裝置的德語語音；可用性依瀏覽器與系統而異。</span>
</div>
</div>
<div id="content"></div>
<div class="tip"><strong>用法提醒：</strong>{tip}</div>
<nav class="pager">{pager}</nav>
</main>
<footer>{title} · 德文 {level}</footer>
<script id="lesson" type="application/json">{payload}</script>
<script>
const lesson = JSON.parse(document.getElementById('lesson').textContent);
const esc = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
document.querySelector('#content').innerHTML = lesson.groups.map(function (g) {{
  var head = lesson.cols.map(function (col) {{ return '<th scope="col">' + esc(col) + '</th>'; }}).join('');
  var rows = g.rows.map(function (r) {{ return '<tr><td>' + esc(r[0]) + '</td><td lang="de">' + esc(r[1]) + '</td><td>' + esc(r[2]) + '</td></tr>'; }}).join('');
  var examples = g.examples.map(function (pair) {{ return '<div class="example"><div><div class="line" lang="de">' + esc(pair[0]) + '</div><div class="zh">' + esc(pair[1]) + '</div></div><button class="speak" type="button" data-say="' + esc(pair[0]) + '" aria-label="播放德語：' + esc(pair[0]) + '">▶ 播放</button></div>'; }}).join('');
  return '<section class="card"><div class="cardhead"><h2>' + esc(g.name) + '</h2><span class="meaning">' + esc(g.meaning) + '</span></div><div class="tablewrap"><table><thead><tr>' + head + '</tr></thead><tbody>' + rows + '</tbody></table></div><div class="examples"><h3>例句與翻譯</h3>' + examples + '</div></section>';
}}).join('');
function speak(text) {{
  if (!('speechSynthesis' in window)) {{ alert('此瀏覽器不支援語音播放。'); return; }}
  let started = false;
  const run = () => {{
    if (started) return;
    started = true;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'de-DE';
    u.rate = 0.82;
    const voice = speechSynthesis.getVoices().find(v => v.lang.toLowerCase().replace('_','-').startsWith('de'));
    if (voice) u.voice = voice;
    speechSynthesis.speak(u);
  }};
  if (speechSynthesis.getVoices().length) run();
  else {{
    speechSynthesis.addEventListener('voiceschanged', run, {{ once: true }});
    setTimeout(run, 300);
  }}
}}
if ('speechSynthesis' in window) speechSynthesis.getVoices();
document.addEventListener('click', e => {{
  const b = e.target.closest('.speak');
  if (b) speak(b.dataset.say);
}});
</script>
</body>
</html>
"""


def pager(prev_lesson, next_lesson):
    parts = []
    if prev_lesson:
        parts.append(f'<a href="../{prev_lesson["slug"]}/">← {html.escape(prev_lesson["title"])}</a>')
    else:
        parts.append('<span></span>')
    if next_lesson:
        parts.append(f'<a href="../{next_lesson["slug"]}/">{html.escape(next_lesson["title"])} →</a>')
    else:
        parts.append('<span></span>')
    return ''.join(parts)


def write_html(lesson, prev_lesson, next_lesson):
    folder = ROOT / 'de' / lesson['slug']
    folder.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({'cols': lesson['cols'], 'groups': lesson['groups']}, ensure_ascii=False)
    tip = '<br>'.join(html.escape(part) for part in lesson['tip'].split('\n'))
    page = PAGE.format(
        desc=html.escape(lesson['card']),
        title=html.escape(lesson['title']),
        level=lesson['level'],
        h1=html.escape(lesson['h1']),
        intro=html.escape(lesson['intro']),
        pdf=html.escape(lesson['pdf']),
        tip=tip,
        pager=pager(prev_lesson, next_lesson),
        payload=payload,
    )
    (folder / 'index.html').write_text(page, encoding='utf-8')


def write_index():
    sections = []
    for level, blurb in LEVELS:
        items = []
        for lesson in LESSONS:
            if lesson['level'] != level:
                continue
            items.append(
                '<article class="item">'
                f'<div class="meta">{html.escape(lesson["meta"])}</div>'
                f'<h3>{html.escape(lesson["title"])}</h3>'
                f'<p>{html.escape(lesson["card"])}</p>'
                f'<a class="button" href="./{lesson["slug"]}/">進入 {html.escape(lesson["title"])} →</a>'
                '</article>'
            )
        sections.append(
            f'<h2>{level}</h2><p class="level-note">{html.escape(blurb)}</p>' + '\n'.join(items)
        )
    body = f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="德文基礎文法清單：依 GER 的 A1、A2、B1、B2 排列，含例句、中文翻譯、朗讀與 PDF。">
<title>德文筆記｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC',sans-serif;color:#172b47;background:#f2f5fa}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:#17355d;padding:20px max(20px,calc((100vw - 920px)/2))}}
header a{{color:white;text-decoration:none;font-weight:700}}
main{{max-width:920px;margin:auto;padding:44px 20px 80px}}
.eyebrow{{font-size:.9rem;font-weight:750;letter-spacing:.06em;color:#1d6a4f}}
h1{{font-size:clamp(2rem,5vw,3rem);margin:10px 0}}
p{{line-height:1.7;color:#53647c}}
h2{{font-size:1.35rem;margin:36px 0 6px}}
.level-note{{margin:0 0 14px}}
.item{{background:white;border:1px solid #dce4ef;border-radius:16px;padding:26px;box-shadow:0 10px 25px #172b470c;margin:0 0 14px}}
.item h3{{font-size:1.55rem;margin:0 0 7px}}
.item p{{margin:0 0 20px}}
.meta{{font-size:.9rem;color:#776b5c;margin-bottom:12px}}
.button{{display:inline-block;padding:11px 18px;border-radius:9px;background:#1d6a4f;color:white;text-decoration:none;font-weight:750}}
.button:hover,.button:focus-visible{{background:#124936;outline:2px solid #124936;outline-offset:2px}}
@media(max-width:600px){{main{{padding-top:30px}}.item{{padding:21px}}}}
</style>
</head>
<body>
<header><a href="../index.html">← 四語筆記首頁</a></header>
<main>
<div class="eyebrow">DEUTSCH · 德文</div>
<h1>德文筆記</h1>
<p>基礎文法依歐洲語言共同參考架構（GER）排列，對應歌德學院檢定 Start Deutsch 1（A1）、Start Deutsch 2（A2）、Goethe-Zertifikat B1 與 B2。每一課都有對照表、例句、中文翻譯、朗讀與 PDF。</p>
{''.join(sections)}
</main>
</body>
</html>
'''
    (ROOT / 'de' / 'index.html').write_text(body, encoding='utf-8')


def main():
    built = [lesson for lesson in LESSONS if not lesson.get('skip')]
    require_glyphs(built)
    for index, lesson in enumerate(LESSONS):
        if lesson.get('skip'):
            continue
        prev_lesson = LESSONS[index - 1] if index else None
        next_lesson = LESSONS[index + 1] if index + 1 < len(LESSONS) else None
        write_html(lesson, prev_lesson, next_lesson)
        render_pdf(lesson)
    write_index()
    print(f'{len(built)} lessons')


if __name__ == '__main__':
    main()
