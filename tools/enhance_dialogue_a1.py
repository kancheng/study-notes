"""Enhance dialogue-a1 pages: PDF download + autoplay with configurable rounds."""
from __future__ import annotations

import html as html_lib
import re
from html.parser import HTMLParser
from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).parent.parent
NOTO = Path(__file__).parent / 'NotoSansTC.ttf'
JP_OTF = Path(__file__).parent / 'NotoSansJP.otf'
YU = Path(r'C:\Windows\Fonts\YuGothR.ttc')

pdfmetrics.registerFont(TTFont('Chinese', str(NOTO)))

PAGES = {
    'en': {
        'path': ROOT / 'en' / 'dialogue-a1' / 'index.html',
        'pdf': 'dialogue-a1.pdf',
        'accent': HexColor('#17355d'),
        'banner': 'Dialogue A1｜英文自我介紹問答',
        'sub': '隨意／較客氣問法、Paul、範本與六類問答',
        'use_jp_font': False,
    },
    'de': {
        'path': ROOT / 'de' / 'dialogue-a1' / 'index.html',
        'pdf': 'dialogue-a1.pdf',
        'accent': HexColor('#1d6a4f'),
        'banner': 'Dialog A1｜德文自我介紹問答',
        'sub': 'du／Sie、Paul、範本與六類問答',
        'use_jp_font': False,
    },
    'fr': {
        'path': ROOT / 'fr' / 'dialogue-a1' / 'index.html',
        'pdf': 'dialogue-a1.pdf',
        'accent': HexColor('#b3482f'),
        'banner': 'Dialogue A1｜法文自我介紹問答',
        'sub': 'tu／vous、Paul、範本與六類問答',
        'use_jp_font': False,
    },
    'ja': {
        'path': ROOT / 'ja' / 'dialogue-a1' / 'index.html',
        'pdf': 'dialogue-a1.pdf',
        'accent': HexColor('#8d3a55'),
        'banner': '自己紹介の質問｜日文 A1 對話',
        'sub': '問句、丁寧形、範本與六類問答',
        'use_jp_font': True,
    },
}

ROUNDS_CONTROLS = '''  <div class="controls-row">
    <button type="button" id="play-all" class="ctrl">▶ 全部播放</button>
    <button type="button" id="stop-all" class="ctrl stop">■ 停止</button>
    <label class="rate">語速
      <input id="rate" type="range" min="0.5" max="1.4" step="0.1" value="0.9">
      <span id="rate-label">0.9</span>
    </label>
    <label class="rounds">播放次數
      <input id="rounds" type="number" min="1" max="99" value="1" inputmode="numeric">
    </label>
  </div>'''

SPEECH_JS = r'''
const lessonLang = document.body.dataset.lang;
const rateInput = document.getElementById('rate');
const rateLabel = document.getElementById('rate-label');
const roundsInput = document.getElementById('rounds');
const statusEl = document.getElementById('play-status');
let queue = [];
let index = 0;
let round = 0;
let targetRounds = 1;
let playing = false;

function voicesReady(cb) {
  if (!('speechSynthesis' in window)) { alert('此瀏覽器不支援語音播放。'); return; }
  if (speechSynthesis.getVoices().length) { cb(); return; }
  speechSynthesis.addEventListener('voiceschanged', () => cb(), { once: true });
  setTimeout(cb, 300);
}

function pickVoice(lang) {
  const prefix = lang.toLowerCase().replace('_', '-').slice(0, 2);
  return speechSynthesis.getVoices().find(v => v.lang.toLowerCase().replace('_', '-').startsWith(prefix));
}

function speakOnce(text, lang, rate, onend) {
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = lang;
  u.rate = rate;
  const voice = pickVoice(lang);
  if (voice) u.voice = voice;
  u.onend = () => { if (onend) onend(); };
  u.onerror = () => { if (onend) onend(); };
  speechSynthesis.speak(u);
}

function allItems() {
  return [...document.querySelectorAll('[data-say]')].map(el => ({
    text: el.dataset.say,
    lang: el.dataset.lang || lessonLang,
    el,
  }));
}

function clearActive() {
  document.querySelectorAll('.vocab-row.active').forEach(r => r.classList.remove('active'));
}

function setStatus(text) {
  if (statusEl) statusEl.textContent = text;
}

function readRounds() {
  const n = parseInt(roundsInput && roundsInput.value, 10);
  if (!Number.isFinite(n) || n < 1) return 1;
  return Math.min(n, 99);
}

function stopAll() {
  playing = false;
  queue = [];
  index = 0;
  round = 0;
  speechSynthesis.cancel();
  clearActive();
  setStatus('已停止');
}

function playNext() {
  if (!playing) return;
  if (index >= queue.length) {
    round += 1;
    if (round < targetRounds && queue.length) {
      index = 0;
    } else {
      playing = false;
      queue = [];
      index = 0;
      speechSynthesis.cancel();
      clearActive();
      setStatus('播放完畢（共 ' + targetRounds + ' 次）');
      return;
    }
  }
  const item = queue[index];
  clearActive();
  const row = item.el.closest('.vocab-row');
  if (row) {
    row.classList.add('active');
    row.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }
  setStatus('播放中：' + item.text + '（第 ' + (round + 1) + '/' + targetRounds + ' 次 · ' + (index + 1) + '/' + queue.length + '）');
  const rate = parseFloat(rateInput.value) || 0.9;
  speakOnce(item.text, item.lang, rate, () => {
    if (!playing) return;
    index += 1;
    setTimeout(playNext, 280);
  });
}

function startQueue(items, startAt) {
  if (!items.length) return;
  voicesReady(() => {
    playing = true;
    queue = items;
    index = startAt || 0;
    round = 0;
    targetRounds = readRounds();
    playNext();
  });
}

rateInput.addEventListener('input', () => {
  rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);
});
rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);

document.getElementById('play-all').addEventListener('click', () => {
  startQueue(allItems(), 0);
});
document.getElementById('stop-all').addEventListener('click', stopAll);

document.addEventListener('click', e => {
  const b = e.target.closest('[data-say]');
  if (!b) return;
  if (e.target.closest('.controls')) return;
  const rate = parseFloat(rateInput.value) || 0.9;
  voicesReady(() => {
    playing = false;
    queue = [];
    clearActive();
    const row = b.closest('.vocab-row');
    if (row) row.classList.add('active');
    setStatus('單句：' + b.dataset.say);
    speakOnce(b.dataset.say, b.dataset.lang || lessonLang, rate, () => {
      clearActive();
      setStatus('待命');
    });
  });
});

if ('speechSynthesis' in window) speechSynthesis.getVoices();
'''


def ensure_japanese_font():
    if 'Japanese' in pdfmetrics.getRegisteredFontNames():
        return
    if JP_OTF.exists():
        pdfmetrics.registerFont(TTFont('Japanese', str(JP_OTF)))
    elif YU.exists():
        pdfmetrics.registerFont(TTFont('Japanese', str(YU), subfontIndex=0))
    else:
        raise SystemExit('Japanese font not found')


def japanese_font_path():
    if JP_OTF.exists():
        return JP_OTF, None
    if YU.exists():
        return YU, 0
    raise SystemExit('Japanese font not found')


def patch_html(path: Path, pdf_name: str) -> None:
    text = path.read_text(encoding='utf-8')

    # CSS: loop -> rounds, add toolbar/download styles if missing
    if '.rounds' not in text:
        text = text.replace(
            '.rate,.loop{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}',
            '.rate,.rounds{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}\n'
            '.rounds input{width:64px;padding:6px 8px;border:1px solid #dce4ef;border-radius:8px;font:inherit}',
        )
    if '.toolbar{' not in text:
        # Insert toolbar CSS before .controls
        toolbar_css = (
            '.toolbar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:0 0 16px}'
            '.download{display:inline-block;background:var(--accent,currentColor);color:white;'
            'padding:12px 18px;border-radius:9px;text-decoration:none;font-weight:700}'
            '.download:hover,.download:focus-visible{filter:brightness(.94);outline:2px solid currentColor;outline-offset:2px}'
            '.toolbar-note{font-size:.9rem;color:#627087}\n'
        )
        text = text.replace('.controls{', toolbar_css + '.controls{', 1)
        # color download with page accent via inline style on the link instead

    # Replace controls row (loop -> rounds)
    text = re.sub(
        r'  <div class="controls-row">\s*'
        r'<button type="button" id="play-all"[^>]*>.*?</button>\s*'
        r'<button type="button" id="stop-all"[^>]*>.*?</button>\s*'
        r'<label class="rate">.*?</label>\s*'
        r'<label class="(?:loop|rounds)">.*?</label>\s*'
        r'</div>',
        ROUNDS_CONTROLS,
        text,
        count=1,
        flags=re.S,
    )

    # Inject PDF toolbar before controls if missing
    if f'href="./{pdf_name}"' not in text:
        # Match accent from controls style
        m = re.search(r'<div class="controls" style="--accent:([^"]+)">', text)
        accent = m.group(1) if m else '#17355d'
        toolbar = (
            f'<div class="toolbar">\n'
            f'  <a class="download" style="background:{accent}" href="./{html_lib.escape(pdf_name)}" download>'
            f'下載完整 PDF</a>\n'
            f'  <span class="toolbar-note">發音使用裝置語音；可用性依瀏覽器與系統而異。</span>\n'
            f'</div>\n'
        )
        text = text.replace(
            f'<div class="controls" style="--accent:{accent}">',
            toolbar + f'<div class="controls" style="--accent:{accent}">',
            1,
        )

    # Replace entire script block body (between <script> and </script> near end)
    text = re.sub(
        r'(<script>\s*)(.*?)(\s*</script>\s*</body>)',
        lambda m: m.group(1) + SPEECH_JS + m.group(3),
        text,
        count=1,
        flags=re.S,
    )

    # Soften copy that mentions infinite loop
    text = text.replace('全部循環播放', '全部播放')
    text = text.replace('也可用全部循環播放，並調整語速。', '也可全部播放並設定次數，並調整語速。')
    text = text.replace('也可用全部循環播放。', '也可全部播放並設定次數。')
    text = text.replace(
        '「全部循環播放」會依頁面順序朗讀；勾選「播完從頭再播」會一直循環，直到按停止。',
        '「全部播放」會依頁面順序朗讀；「播放次數」可設定整輪要播幾遍（1–99）。',
    )

    path.write_text(text, encoding='utf-8')
    print('patched', path)


class DialogueParser(HTMLParser):
    """Extract h2 sections and speakable lines with nearby Chinese for PDF."""

    def __init__(self):
        super().__init__()
        self.sections: list[tuple[str, list[tuple[str, str]]]] = []
        self._section: str | None = None
        self._rows: list[tuple[str, str]] = []
        self._capture = None  # 'h2' | 'say' | 'zh' | None
        self._buf = []
        self._in_say = False
        self._in_zh = False
        self._skip_depth = 0
        self._current_says: list[str] = []
        self._current_zh = ''
        self._in_row = False
        self._td_class = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' or tag == 'style':
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag == 'h2':
            self._flush_section()
            self._capture = 'h2'
            self._buf = []
        elif tag == 'tr' and 'vocab-row' in attrs.get('class', ''):
            self._in_row = True
            self._current_says = []
            self._current_zh = ''
        elif self._in_row and tag == 'button' and 'data-say' in attrs:
            self._current_says.append(attrs['data-say'])
            self._in_say = True
        elif self._in_row and tag == 'td':
            self._td_class = attrs.get('class', '')
            if 'zh' in self._td_class.split():
                self._in_zh = True
                self._buf = []

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag == 'h2' and self._capture == 'h2':
            title = ''.join(self._buf).strip()
            self._section = title
            self._rows = []
            self._capture = None
            self._buf = []
        elif tag == 'button' and self._in_say:
            self._in_say = False
        elif tag == 'td' and self._in_zh:
            text = ''.join(self._buf).strip()
            if text and not self._current_zh:
                self._current_zh = text
            self._in_zh = False
            self._buf = []
        elif tag == 'tr' and self._in_row:
            for say in self._current_says:
                zh = self._current_zh
                self._rows.append((say, zh))
            self._in_row = False
            self._current_says = []
            self._current_zh = ''

    def handle_data(self, data):
        if self._skip_depth:
            return
        if self._capture == 'h2' or self._in_zh:
            self._buf.append(data)

    def _flush_section(self):
        if self._section and self._rows:
            self.sections.append((self._section, self._rows))
            self._rows = []

    def close(self):
        self._flush_section()
        super().close()


def parse_dialogue(path: Path):
    parser = DialogueParser()
    parser.feed(path.read_text(encoding='utf-8'))
    parser.close()
    return parser.sections


def wrap(text, font, size, max_w):
    lines = []
    buf = ''
    for ch in text:
        trial = buf + ch
        if buf and stringWidth(trial, font, size) > max_w:
            lines.append(buf)
            buf = ch
        else:
            buf = trial
    if buf:
        lines.append(buf)
    return lines or ['']


def pick_font(text: str, prefer_jp: bool) -> str:
    if not prefer_jp:
        return 'Chinese'
    # Use Japanese font when kana/kanji present
    for ch in text:
        o = ord(ch)
        if (
            0x3040 <= o <= 0x30FF  # kana
            or 0x4E00 <= o <= 0x9FFF  # CJK
            or 0x3400 <= o <= 0x4DBF
            or 0xFF66 <= o <= 0xFF9D  # halfwidth kana
        ):
            return 'Japanese'
    return 'Chinese'


def write_pdf(out: Path, banner: str, sub: str, accent: HexColor, sections, use_jp: bool):
    if use_jp:
        ensure_japanese_font()
    muted = HexColor('#53677c')
    pale = HexColor('#eaf0f9')
    line_color = HexColor('#dae2ed')
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    zh_font = 'Chinese'

    def heading():
        c.setFillColor(accent)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont(zh_font, 18)
        c.drawString(42, H - 49, banner)
        c.setFont(zh_font, 10)
        c.setFillColor(HexColor('#dde9ff'))
        c.drawString(43, H - 74, sub)
        return H - 118

    y = heading()
    page = 1

    def new_page():
        nonlocal y, page
        c.setFont(zh_font, 8)
        c.setFillColor(muted)
        c.drawRightString(W - 42, 28, f'{page}')
        c.showPage()
        page += 1
        y = heading()

    for title, rows in sections:
        if not rows:
            continue
        if y < 100:
            new_page()
        c.setFillColor(accent)
        c.setFont(zh_font, 13)
        c.drawString(42, y, title)
        y -= 18
        for say, zh in rows:
            say_font = pick_font(say, use_jp)
            say_lines = wrap(say, say_font, 10, W - 100)
            zh_lines = wrap(zh, zh_font, 9, W - 100) if zh else []
            block_h = 8 + 13 * len(say_lines) + 12 * len(zh_lines)
            if y - block_h < 40:
                new_page()
            c.setFillColor(pale)
            c.roundRect(42, y - block_h + 4, W - 84, block_h, 5, fill=1, stroke=0)
            c.setStrokeColor(line_color)
            c.roundRect(42, y - block_h + 4, W - 84, block_h, 5, fill=0, stroke=1)
            ty = y - 12
            c.setFillColor(accent)
            c.setFont(say_font, 10)
            for line in say_lines:
                c.drawString(52, ty, line)
                ty -= 13
            if zh_lines:
                c.setFillColor(muted)
                c.setFont(zh_font, 9)
                for line in zh_lines:
                    c.drawString(52, ty, line)
                    ty -= 12
            y -= block_h + 8
        y -= 10

    c.setFont(zh_font, 8)
    c.setFillColor(muted)
    c.drawRightString(W - 42, 28, f'{page}')
    c.save()
    print(out, 'pages~', page)


def main():
    for lang, meta in PAGES.items():
        path = meta['path']
        if not path.exists():
            raise SystemExit(f'missing {path}')
        patch_html(path, meta['pdf'])
        sections = parse_dialogue(path)
        if not sections:
            raise SystemExit(f'no sections parsed from {path}')
        out = path.parent / meta['pdf']
        write_pdf(out, meta['banner'], meta['sub'], meta['accent'], sections, meta['use_jp_font'])
        n = sum(len(r) for _, r in sections)
        print(f'  {lang}: {len(sections)} sections, {n} lines')


if __name__ == '__main__':
    main()
