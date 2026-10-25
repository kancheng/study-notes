"""Build alphabet / gojuon reference pages for en, de, fr, and ja.

Also generates printable PDFs and wires autoplay with configurable round count.
"""
import html
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


def japanese_font_path():
    if JP_OTF.exists():
        return JP_OTF, None
    if YU.exists():
        return YU, 0
    raise SystemExit('Japanese font not found. Place tools/NotoSansJP.otf or install Yu Gothic.')


def ensure_japanese_font():
    if 'Japanese' in pdfmetrics.getRegisteredFontNames():
        return
    path, index = japanese_font_path()
    if index is None:
        pdfmetrics.registerFont(TTFont('Japanese', str(path)))
    else:
        pdfmetrics.registerFont(TTFont('Japanese', str(path), subfontIndex=index))


SPEECH = """
const lessonLang = document.body.dataset.lang || 'en-US';
const rateInput = document.getElementById('rate');
const rateLabel = document.getElementById('rate-label');
const roundsInput = document.getElementById('rounds');
const statusEl = document.getElementById('play-status');
let queue = [];
let index = 0;
let round = 0;
let targetRounds = 1;
let playing = false;
let current = null;

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
  u.onend = () => { current = null; if (onend) onend(); };
  u.onerror = () => { current = null; if (onend) onend(); };
  current = u;
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
  document.querySelectorAll('.tile.active, .cell.active').forEach(el => el.classList.remove('active'));
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
  current = null;
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
      current = null;
      clearActive();
      setStatus('播放完畢（共 ' + targetRounds + ' 次）');
      return;
    }
  }
  const item = queue[index];
  clearActive();
  item.el.classList.add('active');
  item.el.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  setStatus('播放中：' + item.text + '（第 ' + (round + 1) + '/' + targetRounds + ' 次 · ' + (index + 1) + '/' + queue.length + '）');
  const rate = parseFloat(rateInput.value) || 0.9;
  speakOnce(item.text, item.lang, rate, () => {
    if (!playing) return;
    index += 1;
    setTimeout(playNext, 220);
  });
}

function startQueue(items) {
  if (!items.length) return;
  voicesReady(() => {
    playing = true;
    queue = items;
    index = 0;
    round = 0;
    targetRounds = readRounds();
    playNext();
  });
}

if (rateInput && rateLabel) {
  rateInput.addEventListener('input', () => {
    rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);
  });
  rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);
}

const playAll = document.getElementById('play-all');
const stopAllBtn = document.getElementById('stop-all');
if (playAll) playAll.addEventListener('click', () => startQueue(allItems()));
if (stopAllBtn) stopAllBtn.addEventListener('click', stopAll);

document.addEventListener('click', e => {
  const b = e.target.closest('[data-say]');
  if (!b) return;
  if (e.target.closest('.controls')) return;
  const rate = parseFloat(rateInput && rateInput.value) || 0.9;
  voicesReady(() => {
    playing = false;
    queue = [];
    clearActive();
    b.classList.add('active');
    setStatus('單字：' + b.dataset.say);
    speakOnce(b.dataset.say, b.dataset.lang || lessonLang, rate, () => {
      clearActive();
      setStatus('待命');
    });
  });
});

if ('speechSynthesis' in window) speechSynthesis.getVoices();
"""


def controls_html(pdf_name, accent):
    return f'''
<div class="toolbar">
  <a class="download" href="./{html.escape(pdf_name)}" download>下載完整 PDF</a>
  <span class="toolbar-note">發音使用裝置語音；可用性依瀏覽器與系統而異。</span>
</div>
<div class="controls" style="--accent:{accent}">
  <div class="controls-row">
    <button type="button" id="play-all" class="ctrl">▶ 全部播放</button>
    <button type="button" id="stop-all" class="ctrl stop">■ 停止</button>
    <label class="rate">語速
      <input id="rate" type="range" min="0.5" max="1.4" step="0.1" value="0.9">
      <span id="rate-label">0.9</span>
    </label>
    <label class="rounds">播放次數
      <input id="rounds" type="number" min="1" max="99" value="1" inputmode="numeric">
    </label>
  </div>
  <div id="play-status" class="status">待命</div>
</div>
'''


def page_shell(brand, title, h1, intro, accent, bg, border, body, speech_lang, pdf_name):
    tip = (
        '點選字母或假名可單獨朗讀。「全部播放」會依頁面順序朗讀；'
        '「播放次數」可設定整輪要播幾遍（1–99）。語速可用滑桿調整。'
        '也可下載 PDF 列印複習。'
    )
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(intro)}">
<title>{html.escape(title)}</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:{bg}}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{accent};color:white;padding:22px max(20px,calc((100vw - 1050px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1050px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.35rem;margin:36px 0 12px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 22px}}
.toolbar{{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:0 0 16px}}
.download{{display:inline-block;background:{accent};color:white;padding:12px 18px;border-radius:9px;text-decoration:none;font-weight:700}}
.download:hover,.download:focus-visible{{filter:brightness(.94);outline:2px solid {accent};outline-offset:2px}}
.toolbar-note{{font-size:.9rem;color:#627087}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid {border};border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{accent};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {accent};outline-offset:2px}}
.rate,.rounds{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input[type=range]{{width:140px}}
.rounds input{{width:64px;padding:6px 8px;border:1px solid {border};border-radius:8px;font:inherit}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:12px}}
.tile{{background:white;border:1px solid {border};border-radius:14px;padding:14px 10px;text-align:center;box-shadow:0 6px 18px #142f520c;cursor:pointer}}
.tile:hover,.tile:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.tile.active,.cell.active{{background:#fff4d8;outline:2px solid {accent};outline-offset:2px}}
.glyph{{font-size:1.85rem;font-weight:800;color:{accent};line-height:1.2}}
.pair{{font-size:1.05rem;color:#3d4d63;margin-top:4px}}
.roma,.name{{font-size:.88rem;color:#6a5870;margin-top:4px}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {border};border-left-width:4px;line-height:1.7;color:#52647a}}
.kana-wrap{{overflow-x:auto;margin:12px 0 8px}}
.kana{{border-collapse:collapse;width:100%;min-width:640px;background:white;border:1px solid {border};border-radius:12px;overflow:hidden}}
.kana th,.kana td{{border:1px solid {border};padding:10px 8px;text-align:center;vertical-align:middle}}
.kana th{{background:#f8eef2;font-size:.9rem;color:#5c3a46}}
.kana td.rowhead{{background:#f8eef2;font-weight:750;white-space:nowrap}}
.kana .empty{{background:#faf7f8;color:#b7a8ae}}
.cell{{cursor:pointer;border-radius:8px;background:transparent;border:0;width:100%;padding:4px;font:inherit}}
.cell:hover,.cell:focus-visible{{outline:2px solid {accent};outline-offset:-2px}}
.cell .hira{{font-size:1.45rem;font-weight:800;color:{accent};line-height:1.15}}
.cell .kata{{font-size:1.05rem;color:#3d4d63;margin-top:2px}}
.cell .roma{{font-size:.82rem;color:#6a5870;margin-top:2px}}
.accent-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.glyph{{font-size:1.55rem}}.rate input[type=range]{{width:100px}}}}
</style>
</head>
<body data-lang="{html.escape(speech_lang)}">
<header><div class="brand"><a href="../index.html">← {html.escape(brand)}</a>　/　{html.escape(title.split('｜')[0])}</div></header>
<main>
<h1>{html.escape(h1)}</h1>
<p class="note">{html.escape(intro)}</p>
{controls_html(pdf_name, accent)}
{body}
<div class="tip"><strong>用法提醒：</strong>{html.escape(tip)}</div>
</main>
<footer>{html.escape(title)}</footer>
<script>
{SPEECH}
</script>
</body>
</html>
'''


def latin_tile(upper, lower, name, say, lang):
    return (
        f'<button class="tile" type="button" data-say="{html.escape(say)}" data-lang="{lang}" '
        f'aria-label="播放 {html.escape(upper)}">'
        f'<div class="glyph">{html.escape(upper)}</div>'
        f'<div class="pair">{html.escape(lower)}</div>'
        f'<div class="name">{html.escape(name)}</div>'
        f'</button>'
    )


# --- letter data (shared by HTML + PDF) ---

EN_LETTERS = [
    ('A', 'a', 'ei'), ('B', 'b', 'bi'), ('C', 'c', 'si'), ('D', 'd', 'di'),
    ('E', 'e', 'i'), ('F', 'f', 'ef'), ('G', 'g', 'ji'), ('H', 'h', 'eich'),
    ('I', 'i', 'ai'), ('J', 'j', 'jei'), ('K', 'k', 'kei'), ('L', 'l', 'el'),
    ('M', 'm', 'em'), ('N', 'n', 'en'), ('O', 'o', 'ou'), ('P', 'p', 'pi'),
    ('Q', 'q', 'kiu'), ('R', 'r', 'ar'), ('S', 's', 'es'), ('T', 't', 'ti'),
    ('U', 'u', 'yu'), ('V', 'v', 'vi'), ('W', 'w', 'dabl yu'), ('X', 'x', 'eks'),
    ('Y', 'y', 'wai'), ('Z', 'z', 'zi / zed'),
]

DE_LETTERS = [
    ('A', 'a', 'ah'), ('B', 'b', 'be'), ('C', 'c', 'tse'), ('D', 'd', 'de'),
    ('E', 'e', 'eh'), ('F', 'f', 'ef'), ('G', 'g', 'ge'), ('H', 'h', 'ha'),
    ('I', 'i', 'i'), ('J', 'j', 'jot'), ('K', 'k', 'ka'), ('L', 'l', 'el'),
    ('M', 'm', 'em'), ('N', 'n', 'en'), ('O', 'o', 'oh'), ('P', 'p', 'pe'),
    ('Q', 'q', 'ku'), ('R', 'r', 'er'), ('S', 's', 'es'), ('T', 't', 'te'),
    ('U', 'u', 'u'), ('V', 'v', 'fau'), ('W', 'w', 've'), ('X', 'x', 'iks'),
    ('Y', 'y', 'üpsilon'), ('Z', 'z', 'tsett'),
]
DE_SPECIAL = [
    ('Ä', 'ä', 'a-umlaut'), ('Ö', 'ö', 'o-umlaut'), ('Ü', 'ü', 'u-umlaut'),
    ('ẞ', 'ß', 'Eszett / scharfes S'),
]

FR_LETTERS = [
    ('A', 'a', 'a'), ('B', 'b', 'bé'), ('C', 'c', 'cé'), ('D', 'd', 'dé'),
    ('E', 'e', 'e'), ('F', 'f', 'effe'), ('G', 'g', 'gé'), ('H', 'h', 'ache'),
    ('I', 'i', 'i'), ('J', 'j', 'ji'), ('K', 'k', 'ka'), ('L', 'l', 'elle'),
    ('M', 'm', 'emme'), ('N', 'n', 'enne'), ('O', 'o', 'o'), ('P', 'p', 'pé'),
    ('Q', 'q', 'ku'), ('R', 'r', 'erre'), ('S', 's', 'esse'), ('T', 't', 'té'),
    ('U', 'u', 'u'), ('V', 'v', 'vé'), ('W', 'w', 'double vé'), ('X', 'x', 'iks'),
    ('Y', 'y', 'i grec'), ('Z', 'z', 'zède'),
]
FR_ACCENTS = [
    ('É', 'é', 'e aigu'), ('È', 'è', 'e grave'), ('Ê', 'ê', 'e circonflexe'), ('Ë', 'ë', 'e tréma'),
    ('À', 'à', 'a grave'), ('Â', 'â', 'a circonflexe'),
    ('Ù', 'ù', 'u grave'), ('Û', 'û', 'u circonflexe'), ('Ü', 'ü', 'u tréma'),
    ('Ô', 'ô', 'o circonflexe'), ('Î', 'î', 'i circonflexe'), ('Ï', 'ï', 'i tréma'),
    ('Ç', 'ç', 'c cédille'), ('Œ', 'œ', 'e dans l’o'), ('Æ', 'æ', 'e dans l’a'),
]

JA_SEION = [
    ('あ行', [('あ', 'ア', 'a'), ('い', 'イ', 'i'), ('う', 'ウ', 'u'), ('え', 'エ', 'e'), ('お', 'オ', 'o')]),
    ('か行', [('か', 'カ', 'ka'), ('き', 'キ', 'ki'), ('く', 'ク', 'ku'), ('け', 'ケ', 'ke'), ('こ', 'コ', 'ko')]),
    ('さ行', [('さ', 'サ', 'sa'), ('し', 'シ', 'shi'), ('す', 'ス', 'su'), ('せ', 'セ', 'se'), ('そ', 'ソ', 'so')]),
    ('た行', [('た', 'タ', 'ta'), ('ち', 'チ', 'chi'), ('つ', 'ツ', 'tsu'), ('て', 'テ', 'te'), ('と', 'ト', 'to')]),
    ('な行', [('な', 'ナ', 'na'), ('に', 'ニ', 'ni'), ('ぬ', 'ヌ', 'nu'), ('ね', 'ネ', 'ne'), ('の', 'ノ', 'no')]),
    ('は行', [('は', 'ハ', 'ha'), ('ひ', 'ヒ', 'hi'), ('ふ', 'フ', 'fu'), ('へ', 'ヘ', 'he'), ('ほ', 'ホ', 'ho')]),
    ('ま行', [('ま', 'マ', 'ma'), ('み', 'ミ', 'mi'), ('む', 'ム', 'mu'), ('め', 'メ', 'me'), ('も', 'モ', 'mo')]),
    ('や行', [('や', 'ヤ', 'ya'), None, ('ゆ', 'ユ', 'yu'), None, ('よ', 'ヨ', 'yo')]),
    ('ら行', [('ら', 'ラ', 'ra'), ('り', 'リ', 'ri'), ('る', 'ル', 'ru'), ('れ', 'レ', 're'), ('ろ', 'ロ', 'ro')]),
    ('わ行', [('わ', 'ワ', 'wa'), None, None, None, ('を', 'ヲ', 'o')]),
    ('ん', [('ん', 'ン', 'n'), None, None, None, None]),
]
JA_DAKUON = [
    ('が行', [('が', 'ガ', 'ga'), ('ぎ', 'ギ', 'gi'), ('ぐ', 'グ', 'gu'), ('げ', 'ゲ', 'ge'), ('ご', 'ゴ', 'go')]),
    ('ざ行', [('ざ', 'ザ', 'za'), ('じ', 'ジ', 'ji'), ('ず', 'ズ', 'zu'), ('ぜ', 'ゼ', 'ze'), ('ぞ', 'ゾ', 'zo')]),
    ('だ行', [('だ', 'ダ', 'da'), ('ぢ', 'ヂ', 'ji'), ('づ', 'ヅ', 'zu'), ('で', 'デ', 'de'), ('ど', 'ド', 'do')]),
    ('ば行', [('ば', 'バ', 'ba'), ('び', 'ビ', 'bi'), ('ぶ', 'ブ', 'bu'), ('べ', 'ベ', 'be'), ('ぼ', 'ボ', 'bo')]),
]
JA_HANDAKU = [
    ('ぱ行', [('ぱ', 'パ', 'pa'), ('ぴ', 'ピ', 'pi'), ('ぷ', 'プ', 'pu'), ('ぺ', 'ペ', 'pe'), ('ぽ', 'ポ', 'po')]),
]
JA_YOUON = [
    ('きゃ行', [('きゃ', 'キャ', 'kya'), ('きゅ', 'キュ', 'kyu'), ('きょ', 'キョ', 'kyo')]),
    ('しゃ行', [('しゃ', 'シャ', 'sha'), ('しゅ', 'シュ', 'shu'), ('しょ', 'ショ', 'sho')]),
    ('ちゃ行', [('ちゃ', 'チャ', 'cha'), ('ちゅ', 'チュ', 'chu'), ('ちょ', 'チョ', 'cho')]),
    ('にゃ行', [('にゃ', 'ニャ', 'nya'), ('にゅ', 'ニュ', 'nyu'), ('にょ', 'ニョ', 'nyo')]),
    ('ひゃ行', [('ひゃ', 'ヒャ', 'hya'), ('ひゅ', 'ヒュ', 'hyu'), ('ひょ', 'ヒョ', 'hyo')]),
    ('みゃ行', [('みゃ', 'ミャ', 'mya'), ('みゅ', 'ミュ', 'myu'), ('みょ', 'ミョ', 'myo')]),
    ('りゃ行', [('りゃ', 'リャ', 'rya'), ('りゅ', 'リュ', 'ryu'), ('りょ', 'リョ', 'ryo')]),
    ('ぎゃ行', [('ぎゃ', 'ギャ', 'gya'), ('ぎゅ', 'ギュ', 'gyu'), ('ぎょ', 'ギョ', 'gyo')]),
    ('じゃ行', [('じゃ', 'ジャ', 'ja'), ('じゅ', 'ジュ', 'ju'), ('じょ', 'ジョ', 'jo')]),
    ('びゃ行', [('びゃ', 'ビャ', 'bya'), ('びゅ', 'ビュ', 'byu'), ('びょ', 'ビョ', 'byo')]),
    ('ぴゃ行', [('ぴゃ', 'ピャ', 'pya'), ('ぴゅ', 'ピュ', 'pyu'), ('ぴょ', 'ピョ', 'pyo')]),
]


def write_en():
    tiles = ''.join(latin_tile(u, l, n, u, 'en-US') for u, l, n in EN_LETTERS)
    body = f'''
<h2>26 個字母</h2>
<p class="note">大寫與小寫成對列出。名稱用常見的美式讀法；Z 在英式常讀作 zed。</p>
<div class="grid">{tiles}</div>
<div class="tip"><strong>補充：</strong>英文沒有獨立的變音字母。a / an 看的是後面的發音，不是字母本身：an hour、a university。</div>
'''
    page = page_shell(
        '英文筆記', 'Alphabet｜英文字母', '英文字母表',
        '英文字母共 26 個。點選可聽字母名稱；也可全部播放並設定次數。下面標的是常見的美式讀法。',
        '#17355d', '#f2f5fa', '#dce4ef', body, 'en-US', 'alphabet.pdf',
    )
    out = ROOT / 'en' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    write_latin_pdf(
        out / 'alphabet.pdf',
        'Alphabet｜英文字母',
        '26 個字母：大小寫與常見美式名稱',
        HexColor('#17355d'),
        [('26 個字母', EN_LETTERS)],
        '英文沒有獨立的變音字母。a / an 看的是後面的發音，不是字母本身。',
    )
    print(out / 'index.html')


def write_de():
    tiles = ''.join(latin_tile(u, l, n, u, 'de-DE') for u, l, n in DE_LETTERS)
    extra = ''.join(latin_tile(u, l, n, u if u != 'ẞ' else 'ß', 'de-DE') for u, l, n in DE_SPECIAL)
    body = f'''
<h2>基本字母</h2>
<p class="note">德文字母以拉丁字母為基礎。名稱依德文讀法標註。</p>
<div class="grid">{tiles}</div>
<h2>變音與 ß</h2>
<p class="note">Ä、Ö、Ü 是變音字母（Umlaut）。ß（Eszett）沒有對應的大寫傳統寫法時可寫成 SS；正式大寫也可用 ẞ。</p>
<div class="grid">{extra}</div>
<div class="tip"><strong>補充：</strong>名詞第一個字母要大寫。字典排序時，ä / ö / ü 常當作 a / o / u，ß 當作 ss。</div>
'''
    page = page_shell(
        '德文筆記', 'Alphabet｜德文字母', '德文字母表',
        '德文使用拉丁字母，另有 Ä、Ö、Ü 與 ß。點選可聽字母名稱；也可全部播放並設定次數。',
        '#1d6a4f', '#f2f5fa', '#dce4ef', body, 'de-DE', 'alphabet.pdf',
    )
    out = ROOT / 'de' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    write_latin_pdf(
        out / 'alphabet.pdf',
        'Alphabet｜德文字母',
        '基本字母與變音：Ä、Ö、Ü、ß',
        HexColor('#1d6a4f'),
        [('基本字母', DE_LETTERS), ('變音與 ß', DE_SPECIAL)],
        '名詞第一個字母要大寫。字典排序時，ä / ö / ü 常當作 a / o / u，ß 當作 ss。',
    )
    print(out / 'index.html')


def write_fr():
    tiles = ''.join(latin_tile(u, l, n, u, 'fr-FR') for u, l, n in FR_LETTERS)
    extra = ''.join(latin_tile(u, l, n, l, 'fr-FR') for u, l, n in FR_ACCENTS)
    body = f'''
<h2>基本字母</h2>
<p class="note">法文字母共 26 個。名稱依法文讀法標註。</p>
<div class="grid">{tiles}</div>
<h2>重音與特殊字母</h2>
<p class="note">重音改變發音或分辨詞義：é、è、ê、à、ù、ç 等。œ、æ 是合字，常出現在 cœur、curriculum vitæ。</p>
<div class="accent-grid">{extra}</div>
<div class="tip"><strong>補充：</strong>h 分為 mute h 與 aspirate h，會影響冠詞是否省音：l’homme，但 le haricot。大寫時重音仍建議保留：École。</div>
'''
    page = page_shell(
        '法文筆記', 'Alphabet｜法文字母', '法文字母表',
        '法文使用拉丁字母，並常搭配重音與合字。點選可聽名稱；也可全部播放並設定次數。',
        '#b3482f', '#f7f4f2', '#eadfd6', body, 'fr-FR', 'alphabet.pdf',
    )
    out = ROOT / 'fr' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    write_latin_pdf(
        out / 'alphabet.pdf',
        'Alphabet｜法文字母',
        '基本字母、重音與合字',
        HexColor('#b3482f'),
        [('基本字母', FR_LETTERS), ('重音與特殊字母', FR_ACCENTS)],
        'h 分為 mute h 與 aspirate h。大寫時重音仍建議保留：École。',
    )
    print(out / 'index.html')


def kana_cell(hira, kata, roma):
    if not hira:
        return '<td class="empty">—</td>'
    return (
        f'<td><button class="cell" type="button" data-say="{html.escape(hira)}" data-lang="ja-JP" '
        f'aria-label="播放 {html.escape(hira)}">'
        f'<div class="hira" lang="ja">{html.escape(hira)}</div>'
        f'<div class="kata" lang="ja">{html.escape(kata)}</div>'
        f'<div class="roma">{html.escape(roma)}</div>'
        f'</button></td>'
    )


def kana_table(headers, rows):
    head = ''.join(f'<th scope="col">{html.escape(h)}</th>' for h in headers)
    body_rows = []
    for label, cells in rows:
        tds = ''.join(kana_cell(*cell) if cell else kana_cell('', '', '') for cell in cells)
        body_rows.append(f'<tr><th scope="row" class="rowhead">{html.escape(label)}</th>{tds}</tr>')
    return (
        '<div class="kana-wrap"><table class="kana">'
        f'<thead><tr><th scope="col"></th>{head}</tr></thead>'
        f'<tbody>{"".join(body_rows)}</tbody></table></div>'
    )


def write_ja():
    vowels = ['a', 'i', 'u', 'e', 'o']
    youon_headers = ['ya', 'yu', 'yo']
    body = f'''
<h2>清音（五十音）</h2>
<p class="note">每一格由上到下是平假名、片假名、平文式羅馬拼音。を的羅馬拼音寫成 o；助詞を也讀 o。</p>
{kana_table(vowels, JA_SEION)}
<h2>濁音</h2>
<p class="note">在清音右上加濁點「゛」。ぢ、づ現在多半寫成 じ、ず；羅馬拼音同樣寫成 ji、zu。</p>
{kana_table(vowels, JA_DAKUON)}
<h2>半濁音</h2>
<p class="note">在は行右上加半濁點「゜」，讀成 p 音。</p>
{kana_table(vowels, JA_HANDAKU)}
<h2>拗音</h2>
<p class="note">い段假名加小寫ゃ／ゅ／ょ。片假名同理。羅馬拼音寫成 kya、sha、cha 等。</p>
{kana_table(youon_headers, JA_YOUON)}
<div class="tip"><strong>補充：</strong>促音「っ／ッ」讓後面子音拉長：きって = kitte。長音在平假名常寫成あ行母音，片假名多用「ー」。羅馬拼音長音照假名寫成 ou、oo、ei、ii、uu；片假名長音符號寫成雙母音。</div>
'''
    page = page_shell(
        '日文筆記', '五十音｜平假名・片假名', '日文五十音',
        '平假名、片假名對照，含清音、濁音、半濁音與拗音，並標平文式羅馬拼音。點選可朗讀；也可全部播放並設定次數。',
        '#8d3a55', '#f7f3f5', '#eadde2', body, 'ja-JP', 'gojuon.pdf',
    )
    out = ROOT / 'ja' / 'gojuon'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    write_gojuon_pdf(out / 'gojuon.pdf')
    print(out / 'index.html')


# --- PDF helpers ---

def write_latin_pdf(out, banner, subtitle, accent, sections, tip):
    """Grid PDF for Latin alphabets (en / de / fr)."""
    muted = HexColor('#53677c')
    pale = HexColor('#eaf0f9')
    line_color = HexColor('#dae2ed')
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    font = 'Chinese'
    cols = 4
    cell_w = (W - 84) / cols
    cell_h = 52
    margin_x = 42

    def heading(title, sub):
        c.setFillColor(accent)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont(font, 20)
        c.drawString(42, H - 49, title)
        c.setFont(font, 11)
        c.setFillColor(HexColor('#dde9ff'))
        c.drawString(43, H - 74, sub)
        return H - 120

    y = heading(banner, subtitle)
    for section_i, (section_title, letters) in enumerate(sections):
        if y < 120:
            c.showPage()
            y = heading(banner, subtitle)
        c.setFillColor(accent)
        c.setFont(font, 14)
        c.drawString(42, y, section_title)
        y -= 18
        for i, (upper, lower, name) in enumerate(letters):
            if y < 70:
                c.showPage()
                y = heading(banner, subtitle)
                c.setFillColor(accent)
                c.setFont(font, 14)
                c.drawString(42, y, section_title + '（續）')
                y -= 18
            col = i % cols
            if col == 0 and i:
                y -= cell_h + 8
            x = margin_x + col * cell_w
            c.setFillColor(pale)
            c.roundRect(x, y - cell_h + 8, cell_w - 8, cell_h, 6, fill=1, stroke=0)
            c.setStrokeColor(line_color)
            c.roundRect(x, y - cell_h + 8, cell_w - 8, cell_h, 6, fill=0, stroke=1)
            c.setFillColor(accent)
            c.setFont(font, 16)
            c.drawString(x + 10, y - 12, f'{upper}  {lower}')
            c.setFillColor(muted)
            c.setFont(font, 9)
            label = name
            while stringWidth(label, font, 9) > cell_w - 24 and len(label) > 3:
                label = label[:-2] + '…'
            c.drawString(x + 10, y - 30, label)
        y -= cell_h + 28

    if tip:
        if y < 80:
            c.showPage()
            y = heading(banner, subtitle)
        c.setFillColor(muted)
        c.setFont(font, 10)
        for line in _wrap(tip, font, 10, W - 84):
            c.drawString(42, y, line)
            y -= 14

    c.setFont(font, 8)
    c.setFillColor(muted)
    c.drawRightString(W - 42, 28, banner)
    c.save()
    print(out)


def _wrap(text, font, size, max_w):
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


def write_gojuon_pdf(out):
    ensure_japanese_font()
    accent = HexColor('#8d3a55')
    muted = HexColor('#53677c')
    pale = HexColor('#f8eef2')
    line_color = HexColor('#eadde2')
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    zh, jp = 'Chinese', 'Japanese'

    def heading(sub):
        c.setFillColor(accent)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont(zh, 20)
        c.drawString(42, H - 49, '五十音｜平假名・片假名')
        c.setFont(zh, 11)
        c.setFillColor(HexColor('#f6d5e0'))
        c.drawString(43, H - 74, sub)
        return H - 118

    def ensure_space(y, h):
        if y < h:
            c.showPage()
            return heading('平假名、片假名與羅馬拼音對照')
        return y

    def draw_table(y, title, headers, rows, note):
        y = ensure_space(y, 90)
        c.setFillColor(accent)
        c.setFont(zh, 14)
        c.drawString(42, y, title)
        y -= 16
        c.setFillColor(muted)
        c.setFont(zh, 9)
        for line in _wrap(note, zh, 9, W - 84):
            c.drawString(42, y, line)
            y -= 12
        y -= 4

        n_cols = len(headers)
        label_w = 48
        usable = W - 84 - label_w
        col_w = usable / n_cols
        row_h = 36
        x0 = 42

        y = ensure_space(y, row_h + 20)
        c.setFillColor(pale)
        c.rect(x0, y - row_h + 8, W - 84, row_h, fill=1, stroke=0)
        c.setStrokeColor(line_color)
        c.rect(x0, y - row_h + 8, W - 84, row_h, fill=0, stroke=1)
        c.setFillColor(accent)
        c.setFont(zh, 9)
        for i, h in enumerate(headers):
            c.drawCentredString(x0 + label_w + i * col_w + col_w / 2, y - 14, h)
        y -= row_h

        for label, cells in rows:
            y = ensure_space(y, row_h + 12)
            c.setStrokeColor(line_color)
            c.setFillColor(pale)
            c.rect(x0, y - row_h + 8, label_w, row_h, fill=1, stroke=1)
            c.setFillColor(white)
            c.rect(x0 + label_w, y - row_h + 8, usable, row_h, fill=1, stroke=1)
            c.setFillColor(accent)
            c.setFont(zh, 8)
            c.drawCentredString(x0 + label_w / 2, y - 14, label)
            for i, cell in enumerate(cells):
                cx = x0 + label_w + i * col_w + col_w / 2
                if not cell:
                    c.setFillColor(muted)
                    c.setFont(zh, 10)
                    c.drawCentredString(cx, y - 14, '—')
                    continue
                hira, kata, roma = cell
                c.setFillColor(accent)
                c.setFont(jp, 11)
                c.drawCentredString(cx, y - 6, hira)
                c.setFillColor(muted)
                c.setFont(jp, 8)
                c.drawCentredString(cx, y - 18, kata)
                c.setFont(zh, 7)
                c.drawCentredString(cx, y - 28, roma)
            y -= row_h
        return y - 16

    y = heading('平假名、片假名與羅馬拼音對照')
    y = draw_table(
        y, '清音（五十音）', ['a', 'i', 'u', 'e', 'o'], JA_SEION,
        '每一格：平假名、片假名、平文式羅馬拼音。を寫成 o。',
    )
    y = draw_table(
        y, '濁音', ['a', 'i', 'u', 'e', 'o'], JA_DAKUON,
        '右上加濁點。ぢ、づ多半寫成 じ、ず。',
    )
    y = draw_table(
        y, '半濁音', ['a', 'i', 'u', 'e', 'o'], JA_HANDAKU,
        'は行加半濁點，讀成 p 音。',
    )
    y = draw_table(
        y, '拗音', ['ya', 'yu', 'yo'], JA_YOUON,
        'い段假名加小寫ゃ／ゅ／ょ。',
    )
    tip = '促音「っ／ッ」讓後面子音拉長。片假名長音多用「ー」。'
    if y < 60:
        c.showPage()
        y = heading('平假名、片假名與羅馬拼音對照')
    c.setFillColor(muted)
    c.setFont(zh, 10)
    for line in _wrap(tip, zh, 10, W - 84):
        c.drawString(42, y, line)
        y -= 14
    c.setFont(zh, 8)
    c.drawRightString(W - 42, 28, '五十音｜平假名・片假名')
    c.save()
    print(out)


ALPHABET_CARDS = {
    'en': (
        'alphabet',
        '字母 · 跟讀',
        'Alphabet',
        '英文字母 A–Z：大小寫對照、字母名稱與朗讀。',
    ),
    'de': (
        'alphabet',
        '字母 · 跟讀',
        'Alphabet',
        '德文字母 A–Z，以及 Ä、Ö、Ü、ß：名稱與朗讀。',
    ),
    'fr': (
        'alphabet',
        '字母 · 跟讀',
        'Alphabet',
        '法文字母 A–Z，以及重音與合字：名稱與朗讀。',
    ),
    'ja': (
        'gojuon',
        '五十音 · 跟讀',
        '五十音',
        '平假名、片假名對照：清音、濁音、半濁音、拗音與羅馬拼音。',
    ),
}


def alphabet_card_html(lang):
    slug, meta, title, card = ALPHABET_CARDS[lang]
    lang_attr = ' lang="ja"' if lang == 'ja' else (' lang="fr"' if lang == 'fr' else '')
    return (
        '<h2>字母表</h2>'
        '<article class="item">'
        f'<div class="meta">{html.escape(meta)}</div>'
        f'<h3{lang_attr}>{html.escape(title)}</h3>'
        f'<p>{html.escape(card)}</p>'
        f'<a class="button" href="./{slug}/">進入 {html.escape(title)} →</a>'
        '</article>\n'
    )


def inject_index(lang, marker_html_before_levels):
    """Insert alphabet card before the first level heading if missing."""
    path = ROOT / lang / 'index.html'
    text = path.read_text(encoding='utf-8')
    slug = ALPHABET_CARDS[lang][0]
    if f'href="./{slug}/"' in text:
        return
    card = alphabet_card_html(lang)
    idx = text.find('<h2>')
    if idx < 0:
        raise SystemExit(f'no h2 in {path}')
    path.write_text(text[:idx] + card + text[idx:], encoding='utf-8')
    print('index', path)


def main():
    write_en()
    write_de()
    write_fr()
    write_ja()
    for lang in ('en', 'de', 'fr', 'ja'):
        inject_index(lang, None)


if __name__ == '__main__':
    main()
