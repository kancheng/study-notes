"""Build the Japanese grammar track: one folder, page, and PDF per lesson."""
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

from ja_romaji import self_test, to_romaji
from ja_lessons_n5 import LESSONS as N5
from ja_lessons_n4 import LESSONS as N4
from ja_lessons_n3 import LESSONS as N3
from ja_lessons_n2 import LESSONS as N2

ROOT = Path(__file__).parent.parent
NOTO = Path(__file__).parent / 'NotoSansTC.ttf'
JP_OTF = Path(__file__).parent / 'NotoSansJP.otf'
YU = Path(r'C:\Windows\Fonts\YuGothR.ttc')

LEVELS = [
    ('N5', '能讀寫平假名、片假名與基本漢字，並在教室和日常生活裡理解簡單句子。'),
    ('N4', '能理解稍長的日常句子，並說明理由、許可和打算。'),
    ('N3', '能聽懂接近日常語速的說明，並說出連貫的理由與看法。'),
    ('N2', '能閱讀較長的文章，並用書面語和敬語處理一般事務。'),
]
COLS = ('用法', '漢字', '假名', '羅馬拼音')
LESSONS = [*N5, *N4, *N3, *N2]
GLUED = ('では', 'には', 'へは', 'とは', 'からは', 'までは', 'よりは', 'じゃありません')
PUNCT = '。、？！「」『』'

navy = HexColor('#17365e')
muted = HexColor('#53677c')
pale = HexColor('#f8eef2')
line_color = HexColor('#eadde2')
white = HexColor('#ffffff')
light = HexColor('#f6d5e0')
rose = HexColor('#8d3a55')


def japanese_font_path():
    if JP_OTF.exists():
        return JP_OTF, None
    if YU.exists():
        return YU, 0
    raise SystemExit('Japanese font not found. Place tools/NotoSansJP.otf or install Yu Gothic.')


def register_fonts():
    pdfmetrics.registerFont(TTFont('Chinese', str(NOTO)))
    path, index = japanese_font_path()
    if index is None:
        pdfmetrics.registerFont(TTFont('Japanese', str(path)))
    else:
        pdfmetrics.registerFont(TTFont('Japanese', str(path), subfontIndex=index))


def cmap_for(path, font_number):
    from fontTools.ttLib import TTFont
    if font_number is None:
        font = TTFont(str(path))
    else:
        font = TTFont(str(path), fontNumber=font_number)
    return font.getBestCmap()


def _core(token):
    return token.strip(PUNCT)


def validate(lessons):
    global NOTO_CMAP, JP_CMAP
    self_test()
    jp_path, jp_index = japanese_font_path()
    NOTO_CMAP = cmap_for(NOTO, None)
    JP_CMAP = cmap_for(jp_path, jp_index)
    problems = []

    def need(font_map, label, text, where):
        for ch in text:
            if ch.isspace() or ord(ch) < 32:
                continue
            if ord(ch) not in font_map:
                problems.append(f'{label} {where}: {ch} U+{ord(ch):04X}')

    def need_either(label, text, where):
        for ch in text:
            if ch.isspace() or ord(ch) < 32:
                continue
            if ord(ch) not in NOTO_CMAP and ord(ch) not in JP_CMAP:
                problems.append(f'{label} {where}: {ch} U+{ord(ch):04X}')

    for lesson in lessons:
        need(JP_CMAP, lesson['slug'], lesson['title'], 'title')
        for key in ('h1', 'intro', 'card', 'tip', 'pdf_sub'):
            need_either(lesson['slug'], lesson[key], key)
        for col in COLS:
            need_either(lesson['slug'], col, 'col')
        for group in lesson['groups']:
            need(JP_CMAP, lesson['slug'], group['name'], 'name')
            need_either(lesson['slug'], group['meaning'], 'meaning')
            if len(group['rows']) < 1 or len(group['examples']) < 1:
                problems.append(f"{lesson['slug']} empty group {group['name']}")
            for row in group['rows']:
                if len(row) != 3:
                    problems.append(f"{lesson['slug']} row is not 3 cells: {row}")
                    continue
                label, kanji, kana = row
                need_either(lesson['slug'], label, 'label')
                need(JP_CMAP, lesson['slug'], kanji, 'kanji')
                need(JP_CMAP, lesson['slug'], kana, 'kana')
                problems.extend(_kana_problems(lesson['slug'], kana))
                try:
                    to_romaji(kana)
                except ValueError as exc:
                    problems.append(f"{lesson['slug']} romaji: {exc}")
            for example in group['examples']:
                if len(example) != 3:
                    problems.append(f"{lesson['slug']} example is not 3 cells: {example}")
                    continue
                kanji, kana, zh = example
                need(JP_CMAP, lesson['slug'], kanji, 'example')
                need(JP_CMAP, lesson['slug'], kana, 'kana')
                need_either(lesson['slug'], zh, 'zh')
                problems.extend(_kana_problems(lesson['slug'], kana))
                try:
                    to_romaji(kana)
                except ValueError as exc:
                    problems.append(f"{lesson['slug']} romaji: {exc}")
    if problems:
        unique = list(dict.fromkeys(problems))
        raise SystemExit('Japanese lesson check failed:\n' + '\n'.join(unique[:80]))


def _kana_problems(slug, kana):
    found = []
    for ch in kana:
        if ch.isspace() or ch in PUNCT or ch in '0123456789':
            continue
        code = ord(ch)
        kana_range = (
            0x3040 <= code <= 0x30FF
            or ch == 'ー'
            or 'A' <= ch <= 'Z'
            or 'a' <= ch <= 'z'
            or ch in "-'"
        )
        if not kana_range:
            found.append(f'{slug} kana has {ch} U+{code:04X} in {kana}')
    for token in kana.split():
        core = _core(token)
        if any(core == item or core.startswith(item) for item in GLUED):
            found.append(f'{slug} split the particle in: {kana}')
    return found


def annotated(lesson):
    groups = []
    for group in lesson['groups']:
        rows = [[label, kanji, kana, to_romaji(kana)] for label, kanji, kana in group['rows']]
        examples = [[kanji, kana, to_romaji(kana), zh] for kanji, kana, zh in group['examples']]
        groups.append({'name': group['name'], 'meaning': group['meaning'], 'rows': rows, 'examples': examples})
    return groups


def render_pdf(lesson, groups):
    out = ROOT / 'ja' / lesson['slug'] / lesson['pdf']
    out.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    state = {'y': 0}
    xs = (40, 112, 250, 410)
    widths = (68, 132, 154, 145)

    def face(ch):
        if ord(ch) in NOTO_CMAP:
            return 'Chinese'
        return 'Japanese'

    def measure(s, size, font):
        if font == 'Japanese':
            return stringWidth(s, 'Japanese', size)
        return sum(stringWidth(ch, face(ch), size) for ch in s)

    def text(x, y, s, size=10, color=navy, font='Chinese'):
        c.setFillColor(color)
        if font == 'Japanese':
            c.setFont('Japanese', size)
            c.drawString(x, y, s)
            return
        cursor = x
        for ch in s:
            use = face(ch)
            c.setFont(use, size)
            c.drawString(cursor, y, ch)
            cursor += stringWidth(ch, use, size)

    def wrap(s, size, max_w, font):
        lines = []
        buf = ''
        for ch in s:
            trial = buf + ch
            if buf and measure(trial, size, font) > max_w:
                lines.append(buf)
                buf = ch
            else:
                buf = trial
        if buf:
            lines.append(buf)
        return lines or ['']

    def heading(sub):
        c.setFillColor(rose)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        text(40, H - 49, f"{lesson['title']} · 日本語 {lesson['level']}", 18, white, 'Japanese')
        text(40, H - 74, sub, 11, light, 'Chinese')
        state['y'] = H - 118

    def sync(y):
        state['y'] = y
        return y

    heading(lesson['pdf_sub'])
    total_groups = len(groups)
    for index, group in enumerate(groups):
        if index:
            c.showPage()
            heading('句型對照與跟讀例句')
        y = state['y']
        text(40, y, group['name'], 16, rose, 'Japanese')
        name_w = stringWidth(group['name'], 'Japanese', 16)
        text(40 + name_w + 12, y, group['meaning'], 12, muted, 'Chinese')
        y -= 26
        c.setFillColor(pale)
        c.roundRect(36, y - 6, W - 72, 24, 5, fill=1, stroke=0)
        for col, x in zip(COLS, xs):
            text(x, y + 1, col, 9, navy, 'Chinese')
        y = sync(y - 22)
        for label, kanji, kana, roma in group['rows']:
            parts = [
                wrap(label, 9, widths[0], 'Chinese'),
                wrap(kanji, 9, widths[1], 'Japanese'),
                wrap(kana, 8, widths[2], 'Japanese'),
                wrap(roma, 8, widths[3], 'Chinese'),
            ]
            line_count = max(len(part) for part in parts)
            if state['y'] < 48 + line_count * 12:
                c.showPage()
                heading('句型對照與跟讀例句')
            y = state['y']
            for n in range(line_count):
                if n < len(parts[0]):
                    text(xs[0], y, parts[0][n], 9, navy, 'Chinese')
                if n < len(parts[1]):
                    text(xs[1], y, parts[1][n], 9, rose, 'Japanese')
                if n < len(parts[2]):
                    text(xs[2], y, parts[2][n], 8, navy, 'Japanese')
                if n < len(parts[3]):
                    text(xs[3], y, parts[3][n], 8, muted, 'Chinese')
                y -= 12
            c.setStrokeColor(line_color)
            c.line(36, y + 4, W - 36, y + 4)
            y = sync(y - 8)
        y = sync(state['y'] - 8)
        if state['y'] < 80:
            c.showPage()
            heading('句型對照與跟讀例句')
        y = state['y']
        text(40, y, '例句與翻譯', 13, navy, 'Chinese')
        y = sync(y - 20)
        for kanji, kana, roma, zh in group['examples']:
            blocks = [
                (kanji, 11, rose, 'Japanese'),
                (kana, 9, navy, 'Japanese'),
                (roma, 9, muted, 'Chinese'),
                (zh, 10, muted, 'Chinese'),
            ]
            lines = []
            for value, size, color, font in blocks:
                for line in wrap(value, size, W - 96, font):
                    lines.append((line, size, color, font))
            if state['y'] < 48 + len(lines) * 14:
                c.showPage()
                heading('句型對照與跟讀例句')
            y = state['y']
            for line, size, color, font in lines:
                text(48, y, line, size, color, font)
                y -= 14
            y = sync(y - 6)
        if index == total_groups - 1:
            tip_lines = []
            for part in lesson['tip'].split('\n'):
                tip_lines.extend(wrap(part, 10, W - 80, 'Chinese'))
            if state['y'] < 48 + len(tip_lines) * 14:
                c.showPage()
                heading('用法提醒')
            y = state['y'] - 6
            for n, part in enumerate(tip_lines):
                text(40, y - n * 14, part, 10, muted, 'Chinese')
    c.save()
    print(out)


PAGE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}｜日文 {level}</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:#f7f3f5}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:#6e243c;color:white;padding:22px max(20px,calc((100vw - 1050px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1050px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.55rem;margin:0}}
p{{line-height:1.7}}
.intro{{margin-bottom:24px}}
.toolbar{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:20px 0 12px}}
.download,button{{cursor:pointer;border:0;border-radius:9px;font:inherit}}
.download{{display:inline-block;background:#8d3a55;color:white;padding:12px 18px;text-decoration:none;font-weight:700}}
.download:hover{{background:#64283c}}
.note{{font-size:.92rem;color:#52647d}}
.convention{{background:#f8eef2;border-radius:10px;padding:12px 16px;color:#5c3a46;font-size:.92rem;line-height:1.65;margin:0 0 22px}}
.card{{background:white;border:1px solid #eadde2;border-radius:16px;box-shadow:0 8px 24px #142f5210;margin:20px 0;padding:23px}}
.cardhead{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}
.meaning{{color:#52647d}}
.tablewrap{{overflow-x:auto;margin-top:18px}}
table{{border-collapse:collapse;width:100%;min-width:760px;text-align:left}}
th{{background:#f8eef2;font-size:.9rem}}
th,td{{padding:13px 14px;border-bottom:1px solid #f0e4e8}}
td:nth-child(2){{font-weight:750;color:#6e243c}}
td:nth-child(3),td:nth-child(4){{color:#3d4d63}}
.examples{{margin-top:22px}}
.examples h3{{font-size:1.07rem;margin:0 0 10px}}
.example{{display:grid;grid-template-columns:1fr auto;align-items:center;gap:12px;padding:12px 0;border-top:1px solid #f3e8ec}}
.kanji{{font-size:1.08rem;font-weight:750;color:#6e243c}}
.kana{{color:#243044;margin-top:3px}}
.roma{{color:#6a5870;margin-top:2px;font-size:.95rem}}
.zh{{color:#53637b;margin-top:3px}}
.speak{{background:#f6e8ee;color:#6b2740;padding:9px 12px;min-width:84px}}
.speak:hover,.speak:focus-visible{{background:#ecd3dc;outline:2px solid #8d3a55;outline-offset:2px}}
.tip{{background:#f8eef2;border-left:4px solid #8d3a55;padding:14px 18px;border-radius:8px;margin-top:20px}}
.pager{{display:flex;justify-content:space-between;gap:12px;margin-top:22px}}
.pager a{{color:#8d3a55;font-weight:750;text-decoration:none}}
.pager a:hover,.pager a:focus-visible{{text-decoration:underline}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.card{{padding:17px}}}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 日文筆記</a>　/　{title}</div></header>
<main>
<div class="intro">
<h1>{h1}</h1>
<p>{intro}</p>
<div class="toolbar">
<a class="download" href="./{pdf}" download>下載完整 PDF</a>
<span class="note">發音使用裝置的日語語音，朗讀的是漢字句。可用性依瀏覽器與系統而異。</span>
</div>
<p class="convention">假名依詞分開。羅馬拼音用平文式：助詞は、を、へ寫成 wa、o、e。長音照假名寫成 ou、oo、ei、ii、uu，片假名的長音符號寫成雙母音。</p>
</div>
<div id="content"></div>
<div class="tip"><strong>用法提醒：</strong>{tip}</div>
<nav class="pager">{pager}</nav>
</main>
<footer>{title} · 日文 {level}</footer>
<script id="lesson" type="application/json">{payload}</script>
<script>
const lesson = JSON.parse(document.getElementById('lesson').textContent);
const esc = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
document.querySelector('#content').innerHTML = lesson.groups.map(function (g) {{
  var head = lesson.cols.map(function (col) {{ return '<th scope="col">' + esc(col) + '</th>'; }}).join('');
  var rows = g.rows.map(function (r) {{ return '<tr><td>' + esc(r[0]) + '</td><td lang="ja">' + esc(r[1]) + '</td><td lang="ja">' + esc(r[2]) + '</td><td>' + esc(r[3]) + '</td></tr>'; }}).join('');
  var examples = g.examples.map(function (item) {{
    return '<div class="example"><div><div class="kanji" lang="ja">' + esc(item[0]) + '</div><div class="kana" lang="ja">' + esc(item[1]) + '</div><div class="roma">' + esc(item[2]) + '</div><div class="zh">' + esc(item[3]) + '</div></div><button class="speak" type="button" data-say="' + esc(item[0]) + '" aria-label="播放日語：' + esc(item[0]) + '">▶ 播放</button></div>';
  }}).join('');
  return '<section class="card"><div class="cardhead"><h2 lang="ja">' + esc(g.name) + '</h2><span class="meaning">' + esc(g.meaning) + '</span></div><div class="tablewrap"><table><thead><tr>' + head + '</tr></thead><tbody>' + rows + '</tbody></table></div><div class="examples"><h3>例句與翻譯</h3>' + examples + '</div></section>';
}}).join('');
function speak(text) {{
  if (!('speechSynthesis' in window)) {{ alert('此瀏覽器不支援語音播放。'); return; }}
  let started = false;
  const run = () => {{
    if (started) return;
    started = true;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ja-JP';
    u.rate = 0.82;
    const voice = speechSynthesis.getVoices().find(v => v.lang.toLowerCase().replace('_','-').startsWith('ja'));
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


def write_html(lesson, groups, prev_lesson, next_lesson):
    folder = ROOT / 'ja' / lesson['slug']
    folder.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({'cols': list(COLS), 'groups': groups}, ensure_ascii=False)
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
        payload=payload.replace('<', '\\u003c'),
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
                f'<h3 lang="ja">{html.escape(lesson["title"])}</h3>'
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
<meta name="description" content="日文基礎文法清單：依 JLPT 的 N5、N4、N3、N2 排列。例句附漢字、假名、羅馬拼音、朗讀與 PDF。">
<title>日文筆記｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#172b47;background:#f7f3f5}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:#17355d;padding:20px max(20px,calc((100vw - 920px)/2))}}
header a{{color:white;text-decoration:none;font-weight:700}}
main{{max-width:920px;margin:auto;padding:44px 20px 80px}}
.eyebrow{{font-size:.9rem;font-weight:750;letter-spacing:.06em;color:#8d3a55}}
h1{{font-size:clamp(2rem,5vw,3rem);margin:10px 0}}
p{{line-height:1.7;color:#53647c}}
h2{{font-size:1.35rem;margin:36px 0 6px}}
.level-note{{margin:0 0 14px}}
.item{{background:white;border:1px solid #eadde2;border-radius:16px;padding:26px;box-shadow:0 10px 25px #172b470c;margin:0 0 14px}}
.item h3{{font-size:1.55rem;margin:0 0 7px}}
.item p{{margin:0 0 20px}}
.meta{{font-size:.9rem;color:#776b5c;margin-bottom:12px}}
.button{{display:inline-block;padding:11px 18px;border-radius:9px;background:#8d3a55;color:white;text-decoration:none;font-weight:750}}
.button:hover,.button:focus-visible{{background:#64283c;outline:2px solid #64283c;outline-offset:2px}}
@media(max-width:600px){{main{{padding-top:30px}}.item{{padding:21px}}}}
</style>
</head>
<body>
<header><a href="../index.html">← 四語筆記首頁</a></header>
<main>
<div class="eyebrow">日本語 · 日文</div>
<h1>日文筆記</h1>
<p>基礎文法依日本語能力試驗（JLPT）排列，從 N5 到 N2。每一課都有對照表。例句寫出漢字、假名與平文式羅馬拼音，並可朗讀、下載 PDF。</p>
<p>假名依詞分開。助詞は、を、へ的羅馬拼音是 wa、o、e。長音照假名寫成 ou、oo、ei、ii、uu；片假名的長音符號寫成雙母音。</p>
{''.join(sections)}
</main>
</body>
</html>
'''
    (ROOT / 'ja' / 'index.html').write_text(body, encoding='utf-8')


def main():
    register_fonts()
    validate(LESSONS)
    old = ROOT / 'ja' / 'konnichiwa-doushi' / 'Konnichiwa-Doushi-A1.pdf'
    if old.exists():
        old.unlink()
    for index, lesson in enumerate(LESSONS):
        groups = annotated(lesson)
        prev_lesson = LESSONS[index - 1] if index else None
        next_lesson = LESSONS[index + 1] if index + 1 < len(LESSONS) else None
        write_html(lesson, groups, prev_lesson, next_lesson)
        render_pdf(lesson, groups)
    write_index()
    print(f'{len(LESSONS)} lessons')


if __name__ == '__main__':
    main()
