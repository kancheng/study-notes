"""Build 0–2000 number reference pages for en, de, fr, and ja."""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

THEMES = {
    'en': {
        'brand': '英文筆記',
        'title': 'Numbers｜英文數字',
        'h1': '英文數字表',
        'intro': '數字 0 到 2000。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#17355d',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'en-US',
        'slug': 'numbers',
        'card_title': 'Numbers',
        'card': '數字 0–2000：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '數字 · 跟讀',
        'word_col': '英文',
    },
    'de': {
        'brand': '德文筆記',
        'title': 'Zahlen｜德文數字',
        'h1': '德文數字表',
        'intro': '數字 0 到 2000。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#1d6a4f',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'de-DE',
        'slug': 'numbers',
        'card_title': 'Zahlen',
        'card': '數字 0–2000：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '數字 · 跟讀',
        'word_col': '德文',
    },
    'fr': {
        'brand': '法文筆記',
        'title': 'Nombres｜法文數字',
        'h1': '法文數字表',
        'intro': '數字 0 到 2000。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#b3482f',
        'bg': '#f7f4f2',
        'border': '#eadfd6',
        'lang': 'fr-FR',
        'slug': 'numbers',
        'card_title': 'Nombres',
        'card': '數字 0–2000：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '數字 · 跟讀',
        'word_col': '法文',
    },
    'ja': {
        'brand': '日文筆記',
        'title': '数字｜日文數字',
        'h1': '日文數字表',
        'intro': '數字 0 到 2000。每一數附漢字、平假名、片假名與羅馬拼音（含濁音、半濁音讀法）。點選可朗讀；也可全部循環播放並調語速。',
        'accent': '#8d3a55',
        'bg': '#f7f3f5',
        'border': '#eadde2',
        'lang': 'ja-JP',
        'slug': 'numbers',
        'card_title': '数字',
        'card': '數字 0–2000：漢字、平片假名、羅馬拼音；可單字朗讀或全部循環播放並調語速。',
        'meta': '數字 · 跟讀',
        'word_col': '漢字',
    },
}

SPEECH_JS = r'''
const lessonLang = document.body.dataset.lang;
const rateInput = document.getElementById('rate');
const rateLabel = document.getElementById('rate-label');
const loopBox = document.getElementById('loop');
const statusEl = document.getElementById('play-status');
let queue = [];
let index = 0;
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

function stopAll() {
  playing = false;
  queue = [];
  index = 0;
  speechSynthesis.cancel();
  clearActive();
  setStatus('已停止');
}

function playNext() {
  if (!playing) return;
  if (index >= queue.length) {
    if (loopBox && loopBox.checked && queue.length) {
      index = 0;
    } else {
      stopAll();
      setStatus('播放完畢');
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
  setStatus('播放中：' + item.text + '（' + (index + 1) + ' / ' + queue.length + '）');
  const rate = parseFloat(rateInput.value) || 0.9;
  speakOnce(item.text, item.lang, rate, () => {
    if (!playing) return;
    index += 1;
    setTimeout(playNext, 220);
  });
}

function startQueue(items, startAt) {
  if (!items.length) return;
  voicesReady(() => {
    playing = true;
    queue = items;
    index = startAt || 0;
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
    setStatus('單字：' + b.dataset.say);
    speakOnce(b.dataset.say, b.dataset.lang || lessonLang, rate, () => {
      clearActive();
      setStatus('待命');
    });
  });
});

if ('speechSynthesis' in window) speechSynthesis.getVoices();
'''


# ---------- English ----------

_EN_ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen',
]
_EN_TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def en_under_100(n):
    if n < 20:
        return _EN_ONES[n]
    tens, ones = divmod(n, 10)
    if ones == 0:
        return _EN_TENS[tens]
    return f'{_EN_TENS[tens]}-{_EN_ONES[ones]}'


def en_word(n):
    if n < 100:
        return en_under_100(n)
    if n < 1000:
        h, r = divmod(n, 100)
        head = f'{_EN_ONES[h]} hundred'
        return head if r == 0 else f'{head} {en_under_100(r)}'
    # 1000–2000
    th, r = divmod(n, 1000)
    head = f'{_EN_ONES[th]} thousand'
    return head if r == 0 else f'{head} {en_word(r)}'


# ---------- German ----------

_DE_ONES = [
    'null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun',
    'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn',
    'siebzehn', 'achtzehn', 'neunzehn',
]
_DE_TENS = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']
_DE_ONES_COMPOUND = [
    '', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun',
]


def de_under_100(n, final=True):
    if n < 20:
        if n == 1 and not final:
            return 'ein'
        return _DE_ONES[n]
    tens, ones = divmod(n, 10)
    if ones == 0:
        return _DE_TENS[tens]
    return f'{_DE_ONES_COMPOUND[ones]}und{_DE_TENS[tens]}'


def de_word(n):
    if n < 100:
        return de_under_100(n, final=True)
    if n < 1000:
        h, r = divmod(n, 100)
        if h == 1:
            head = 'einhundert'
        else:
            head = f'{_DE_ONES_COMPOUND[h]}hundert'
        if r == 0:
            return head
        return head + de_under_100(r, final=True)
    th, r = divmod(n, 1000)
    if th == 1:
        head = 'eintausend'
    else:
        head = f'{_DE_ONES_COMPOUND[th]}tausend'
    if r == 0:
        return head
    return head + de_word(r)


# ---------- French ----------

_FR_ONES = [
    'zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf',
    'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize',
]
_FR_TENS = {
    20: 'vingt', 30: 'trente', 40: 'quarante', 50: 'cinquante', 60: 'soixante',
}


def fr_under_100(n):
    if n < 17:
        return _FR_ONES[n]
    if n < 20:
        return 'dix-' + _FR_ONES[n - 10]
    if n < 70:
        tens = (n // 10) * 10
        ones = n % 10
        base = _FR_TENS[tens]
        if ones == 0:
            return base
        if ones == 1:
            return f'{base} et un'
        return f'{base}-{_FR_ONES[ones]}'
    if n < 80:
        # 70–79 = soixante + 10–19
        rest = n - 60
        if rest == 11:
            return 'soixante et onze'
        return 'soixante-' + fr_under_100(rest)
    # 80–99
    rest = n - 80
    if rest == 0:
        return 'quatre-vingts'
    return 'quatre-vingt-' + fr_under_100(rest)


def fr_word(n):
    if n < 100:
        return fr_under_100(n)
    if n < 1000:
        h, r = divmod(n, 100)
        if h == 1:
            head = 'cent'
        elif r == 0:
            head = f'{_FR_ONES[h]} cents'
        else:
            head = f'{_FR_ONES[h]} cent'
        if r == 0:
            return head if h != 1 else 'cent'
        return f'{head} {fr_under_100(r)}'
    th, r = divmod(n, 1000)
    if th == 1:
        head = 'mille'
    else:
        head = f'{_FR_ONES[th]} mille'
    if r == 0:
        return head
    return f'{head} {fr_word(r)}'


# ---------- Japanese ----------

_JA_DIGIT_KANJI = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
_JA_DIGIT_HIRA = ['ぜろ', 'いち', 'に', 'さん', 'よん', 'ご', 'ろく', 'なな', 'はち', 'きゅう']
_JA_DIGIT_ROMA = ['zero', 'ichi', 'ni', 'san', 'yon', 'go', 'roku', 'nana', 'hachi', 'kyuu']


def to_katakana(text):
    out = []
    for ch in text:
        code = ord(ch)
        if 0x3041 <= code <= 0x3096:
            out.append(chr(code + 0x60))
        else:
            out.append(ch)
    return ''.join(out)


def hepburn_join(parts):
    """Join Hepburn syllables; insert apostrophe after n before vowel/y."""
    if not parts:
        return ''
    out = parts[0]
    for p in parts[1:]:
        if out.endswith('n') and p and p[0] in 'aiueoy':
            out += "'" + p
        else:
            out += p
    return out


def ja_under_100(n):
    """Return (kanji, hira, roma_parts) for 0–99."""
    if n == 0:
        return '零', 'ぜろ', ['zero']
    if n < 10:
        return _JA_DIGIT_KANJI[n], _JA_DIGIT_HIRA[n], [_JA_DIGIT_ROMA[n]]
    if n == 10:
        return '十', 'じゅう', ['juu']
    if n < 20:
        ones = n - 10
        return (
            '十' + _JA_DIGIT_KANJI[ones],
            'じゅう' + _JA_DIGIT_HIRA[ones],
            ['juu', _JA_DIGIT_ROMA[ones]],
        )
    tens, ones = divmod(n, 10)
    k = _JA_DIGIT_KANJI[tens] + '十'
    h = _JA_DIGIT_HIRA[tens] + 'じゅう'
    r = [_JA_DIGIT_ROMA[tens], 'juu']
    if ones:
        k += _JA_DIGIT_KANJI[ones]
        h += _JA_DIGIT_HIRA[ones]
        r.append(_JA_DIGIT_ROMA[ones])
    return k, h, r


def ja_hundreds_block(h):
    """Hundreds digit 1–9 → (kanji_prefix, hira, roma) for N百 with rendaku."""
    # 100 alone uses 百; 200=二百, 300=三百(びゃく), 600=六百(ぴゃく), 800=八百(ぴゃく)
    special = {
        1: ('百', 'ひゃく', 'hyaku'),
        2: ('二百', 'にひゃく', 'nihyaku'),
        3: ('三百', 'さんびゃく', 'sanbyaku'),
        4: ('四百', 'よんひゃく', 'yonhyaku'),
        5: ('五百', 'ごひゃく', 'gohyaku'),
        6: ('六百', 'ろっぴゃく', 'roppyaku'),
        7: ('七百', 'ななひゃく', 'nanahyaku'),
        8: ('八百', 'はっぴゃく', 'happyaku'),
        9: ('九百', 'きゅうひゃく', 'kyuuhyaku'),
    }
    return special[h]


def ja_word(n):
    """Return (kanji, hira, kata, roma, say_hira)."""
    if n == 0:
        return '零', 'ぜろ', 'ゼロ', 'zero', 'ぜろ'
    parts_k = []
    parts_h = []
    parts_r = []

    if n >= 1000:
        th, n = divmod(n, 1000)
        if th == 1:
            parts_k.append('千')
            parts_h.append('せん')
            parts_r.append('sen')
        elif th == 2:
            parts_k.append('二千')
            parts_h.append('にせん')
            parts_r.append('nisen')
        else:
            parts_k.append(_JA_DIGIT_KANJI[th] + '千')
            parts_h.append(_JA_DIGIT_HIRA[th] + 'せん')
            parts_r.append(_JA_DIGIT_ROMA[th] + 'sen')

    if n >= 100:
        h, n = divmod(n, 100)
        hk, hh, hr = ja_hundreds_block(h)
        parts_k.append(hk)
        parts_h.append(hh)
        parts_r.append(hr)

    if n > 0:
        uk, uh, ur = ja_under_100(n)
        parts_k.append(uk)
        parts_h.append(uh)
        parts_r.extend(ur)

    kanji = ''.join(parts_k)
    hira = ''.join(parts_h)
    # ゼロ stays katakana for zero only; others convert
    kata = to_katakana(hira)
    roma = hepburn_join(parts_r)
    return kanji, hira, kata, roma, hira


def build_entries():
    entries = []
    for n in range(0, 2001):
        entries.append({
            'n': n,
            'en': en_word(n),
            'de': de_word(n),
            'fr': fr_word(n),
            'ja': ja_word(n),
        })
    return entries


def controls_html(accent):
    return f'''
<div class="controls" style="--accent:{accent}">
  <div class="controls-row">
    <button type="button" id="play-all" class="ctrl">▶ 全部循環播放</button>
    <button type="button" id="stop-all" class="ctrl stop">■ 停止</button>
    <label class="rate">語速
      <input id="rate" type="range" min="0.5" max="1.4" step="0.1" value="0.9">
      <span id="rate-label">0.9</span>
    </label>
    <label class="loop"><input id="loop" type="checkbox" checked> 播完從頭再播</label>
  </div>
  <div id="play-status" class="status">待命</div>
</div>
'''


def toc_html(max_n=2000):
    links = []
    for start in range(0, max_n + 1, 100):
        end = min(start + 99, max_n)
        links.append(f'<a href="#n{start}">{start}–{end}</a>')
    return '<nav class="toc" aria-label="區間">' + ''.join(links) + '</nav>'


def page_for(lang, entries):
    theme = THEMES[lang]
    accent = theme['accent']
    parts = [controls_html(accent), toc_html()]

    for start in range(0, 2001, 100):
        end = min(start + 99, 2000)
        chunk = [e for e in entries if start <= e['n'] <= end]
        rows = []
        for e in chunk:
            n = e['n']
            if lang == 'ja':
                kanji, hira, kata, roma, say = e['ja']
                rows.append(
                    '<tr class="vocab-row">'
                    f'<td class="num">{n}</td>'
                    f'<td><button type="button" class="say" lang="ja" data-say="{html.escape(say)}" data-lang="ja-JP">'
                    f'<span class="kanji">{html.escape(kanji)}</span>'
                    f'<span class="kana"><span class="hira">{html.escape(hira)}</span>　'
                    f'<span class="kata">{html.escape(kata)}</span></span>'
                    f'<span class="roma">{html.escape(roma)}</span>'
                    f'</button></td></tr>'
                )
            else:
                word = e[lang]
                rows.append(
                    '<tr class="vocab-row">'
                    f'<td class="num">{n}</td>'
                    f'<td><button type="button" class="say" lang="{lang}" data-say="{html.escape(word)}" data-lang="{theme["lang"]}">'
                    f'<span class="word">{html.escape(word)}</span>'
                    f'</button></td></tr>'
                )
        head = (
            '<thead><tr><th scope="col">數字</th>'
            '<th scope="col">漢字 · 平假名 · 片假名 · 羅馬拼音</th></tr></thead>'
            if lang == 'ja'
            else f'<thead><tr><th scope="col">數字</th><th scope="col">{html.escape(theme["word_col"])}</th></tr></thead>'
        )
        parts.append(
            f'<section id="n{start}"><h2>{start}–{end}</h2>'
            f'<div class="tablewrap"><table>{head}<tbody>{"".join(rows)}</tbody></table></div></section>'
        )

    tip = (
        '點選數字可單獨朗讀。「全部循環播放」會依 0→2000 順序朗讀；勾選「播完從頭再播」會一直循環，直到按停止。語速可用滑桿調整。'
    )
    if lang == 'ja':
        tip += (
            ' 每一數列出漢字、平假名、片假名與羅馬拼音。'
            '百的連濁：三百＝さんびゃく、六百＝ろっぴゃく、八百＝はっぴゃく。'
            '四讀よん、七讀なな。零的片假名寫ゼロ。'
            'ん接母音或 y 時，羅馬拼音加撇號（如 千一＝sen\'ichi）。'
        )
    elif lang == 'fr':
        tip += ' 七十起為 soixante-dix 系統；八十為 quatre-vingts；整百複數加 s（deux cents），後面有數時不加。'
    elif lang == 'de':
        tip += ' 二十一寫成 einundzwanzig（個位在前）。100＝einhundert，1000＝eintausend。'

    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(theme['intro'])}">
<title>{html.escape(theme['title'])}</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:{theme['bg']}}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{accent};color:white;padding:22px max(20px,calc((100vw - 1050px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1050px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.15rem;margin:28px 0 10px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.toc{{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}}
.toc a{{display:inline-block;padding:5px 10px;border-radius:8px;background:white;border:1px solid {theme['border']};color:{accent};text-decoration:none;font-weight:650;font-size:.85rem}}
.toc a:hover,.toc a:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid {theme['border']};border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 18px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{accent};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {accent};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid {theme['border']};border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:420px}}
th{{background:#f4f7fb;text-align:left;font-size:.9rem;padding:10px 12px}}
td{{padding:8px 12px;border-top:1px solid {theme['border']};vertical-align:middle}}
.num{{color:#53647c;width:72px;font-variant-numeric:tabular-nums;font-weight:650}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:1px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:3px 0;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.word,.kanji{{font-size:1.08rem;font-weight:750;color:{accent}}}
.kana{{font-size:.95rem;color:#3d4d63}}
.kata{{color:#6a5870}}
.roma{{font-size:.85rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {theme['border']};border-left-width:4px;line-height:1.7;color:#52647a}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.rate input{{width:100px}}}}
</style>
</head>
<body data-lang="{theme['lang']}">
<header><div class="brand"><a href="../index.html">← {html.escape(theme['brand'])}</a>　/　{html.escape(theme['title'].split('｜')[0])}</div></header>
<main>
<h1>{html.escape(theme['h1'])}</h1>
<p class="note">{html.escape(theme['intro'])}</p>
{''.join(parts)}
<div class="tip"><strong>用法提醒：</strong>{html.escape(tip)}</div>
</main>
<footer>{html.escape(theme['title'])}</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def numbers_card_html(lang):
    theme = THEMES[lang]
    lang_attr = ''
    if lang == 'ja':
        lang_attr = ' lang="ja"'
    elif lang == 'fr':
        lang_attr = ' lang="fr"'
    elif lang == 'de':
        lang_attr = ' lang="de"'
    return (
        '<article class="item">'
        f'<div class="meta">{html.escape(theme["meta"])}</div>'
        f'<h3{lang_attr}>{html.escape(theme["card_title"])}</h3>'
        f'<p>{html.escape(theme["card"])}</p>'
        f'<a class="button" href="./{theme["slug"]}/">進入 {html.escape(theme["card_title"])} →</a>'
        '</article>\n'
    )


def inject_index(lang):
    path = ROOT / lang / 'index.html'
    text = path.read_text(encoding='utf-8')
    slug = THEMES[lang]['slug']
    if f'href="./{slug}/"' in text:
        return
    card = numbers_card_html(lang)
    # Insert after vocab card if present, else after alphabet/gojuon
    for marker in ('href="./vocab/"', 'href="./alphabet/"', 'href="./gojuon/"'):
        pos = text.find(marker)
        if pos != -1:
            end = text.find('</article>', pos)
            if end != -1:
                insert_at = end + len('</article>')
                text = text[:insert_at] + '\n' + card + text[insert_at:]
                path.write_text(text, encoding='utf-8')
                print('index', path)
                return
    raise SystemExit(f'cannot inject numbers into {path}')


def self_check():
    samples = {
        0: ('zero', 'null', 'zéro'),
        11: ('eleven', 'elf', 'onze'),
        21: ('twenty-one', 'einundzwanzig', 'vingt et un'),
        70: ('seventy', 'siebzig', 'soixante-dix'),
        80: ('eighty', 'achtzig', 'quatre-vingts'),
        91: ('ninety-one', 'einundneunzig', 'quatre-vingt-onze'),
        100: ('one hundred', 'einhundert', 'cent'),
        101: ('one hundred one', 'einhunderteins', 'cent un'),
        200: ('two hundred', 'zweihundert', 'deux cents'),
        201: ('two hundred one', 'zweihunderteins', 'deux cent un'),
        1000: ('one thousand', 'eintausend', 'mille'),
        1100: ('one thousand one hundred', 'eintausendeinhundert', 'mille cent'),
        2000: ('two thousand', 'zweitausend', 'deux mille'),
    }
    for n, (e, d, f) in samples.items():
        assert en_word(n) == e, (n, en_word(n), e)
        assert de_word(n) == d, (n, de_word(n), d)
        assert fr_word(n) == f, (n, fr_word(n), f)
    ja_samples = {
        0: ('零', 'ぜろ', 'ゼロ', 'zero'),
        4: ('四', 'よん', 'ヨン', 'yon'),
        10: ('十', 'じゅう', 'ジュウ', 'juu'),
        11: ('十一', 'じゅういち', 'ジュウイチ', 'juuichi'),
        20: ('二十', 'にじゅう', 'ニジュウ', 'nijuu'),
        100: ('百', 'ひゃく', 'ヒャク', 'hyaku'),
        300: ('三百', 'さんびゃく', 'サンビャク', 'sanbyaku'),
        600: ('六百', 'ろっぴゃく', 'ロッピャク', 'roppyaku'),
        800: ('八百', 'はっぴゃく', 'ハッピャク', 'happyaku'),
        1000: ('千', 'せん', 'セン', 'sen'),
        1001: ('千一', 'せんいち', 'センイチ', "sen'ichi"),
        1100: ('千百', 'せんひゃく', 'センヒャク', 'senhyaku'),
        2000: ('二千', 'にせん', 'ニセン', 'nisen'),
    }
    for n, expected in ja_samples.items():
        got = ja_word(n)[:4]
        assert got == expected, (n, got, expected)
    print('self_check ok')


def main():
    self_check()
    entries = build_entries()
    for lang in ('en', 'de', 'fr', 'ja'):
        folder = ROOT / lang / THEMES[lang]['slug']
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / 'index.html'
        path.write_text(page_for(lang, entries), encoding='utf-8')
        print(path, path.stat().st_size)
        inject_index(lang)


if __name__ == '__main__':
    main()
