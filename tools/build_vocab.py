"""Build shared vocabulary reference pages for en, de, fr, and ja."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Chinese gloss -> (en, de, fr, ja_kanji, ja_kana, ja_roma)
# Japanese follows Hepburn used elsewhere on the site.

SEASONS = [
    ('春天', 'spring', 'Frühling', 'printemps', '春', 'はる', 'haru'),
    ('夏天', 'summer', 'Sommer', 'été', '夏', 'なつ', 'natsu'),
    ('秋天', 'autumn', 'Herbst', 'automne', '秋', 'あき', 'aki'),
    ('冬天', 'winter', 'Winter', 'hiver', '冬', 'ふゆ', 'fuyu'),
]

MONTHS = [
    ('一月', 'January', 'Januar', 'janvier', '一月', 'いちがつ', 'ichigatsu'),
    ('二月', 'February', 'Februar', 'février', '二月', 'にがつ', 'nigatsu'),
    ('三月', 'March', 'März', 'mars', '三月', 'さんがつ', 'sangatsu'),
    ('四月', 'April', 'April', 'avril', '四月', 'しがつ', 'shigatsu'),
    ('五月', 'May', 'Mai', 'mai', '五月', 'ごがつ', 'gogatsu'),
    ('六月', 'June', 'Juni', 'juin', '六月', 'ろくがつ', 'rokugatsu'),
    ('七月', 'July', 'Juli', 'juillet', '七月', 'しちがつ', 'shichigatsu'),
    ('八月', 'August', 'August', 'août', '八月', 'はちがつ', 'hachigatsu'),
    ('九月', 'September', 'September', 'septembre', '九月', 'くがつ', 'kugatsu'),
    ('十月', 'October', 'Oktober', 'octobre', '十月', 'じゅうがつ', 'juugatsu'),
    ('十一月', 'November', 'November', 'novembre', '十一月', 'じゅういちがつ', 'juuichigatsu'),
    ('十二月', 'December', 'Dezember', 'décembre', '十二月', 'じゅうにがつ', 'juunigatsu'),
]

TIME_WORDS = [
    ('一周／一週', 'week', 'Woche', 'semaine', '週', 'しゅう', 'shuu'),
    ('周末', 'weekend', 'Wochenende', 'week-end', '週末', 'しゅうまつ', 'shuumatsu'),
    ('月', 'month', 'Monat', 'mois', '月', 'つき', 'tsuki'),
    ('年', 'year', 'Jahr', 'année', '年', 'とし', 'toshi'),
]

WEEKDAYS = [
    ('星期一', 'Monday', 'Montag', 'lundi', '月曜日', 'げつようび', 'getsuyoubi'),
    ('星期二', 'Tuesday', 'Dienstag', 'mardi', '火曜日', 'かようび', 'kayoubi'),
    ('星期三', 'Wednesday', 'Mittwoch', 'mercredi', '水曜日', 'すいようび', 'suiyoubi'),
    ('星期四', 'Thursday', 'Donnerstag', 'jeudi', '木曜日', 'もくようび', 'mokuyoubi'),
    ('星期五', 'Friday', 'Freitag', 'vendredi', '金曜日', 'きんようび', 'kinyoubi'),
    ('星期六', 'Saturday', 'Samstag', 'samedi', '土曜日', 'どようび', 'doyoubi'),
    ('星期日', 'Sunday', 'Sonntag', 'dimanche', '日曜日', 'にちようび', 'nichiyoubi'),
]

NUMBERS = [
    ('0', 'zero', 'null', 'zéro', '零', 'ゼロ', 'zero'),
    ('1', 'one', 'eins', 'un', '一', 'いち', 'ichi'),
    ('2', 'two', 'zwei', 'deux', '二', 'に', 'ni'),
    ('3', 'three', 'drei', 'trois', '三', 'さん', 'san'),
    ('4', 'four', 'vier', 'quatre', '四', 'よん', 'yon'),
    ('5', 'five', 'fünf', 'cinq', '五', 'ご', 'go'),
    ('6', 'six', 'sechs', 'six', '六', 'ろく', 'roku'),
    ('7', 'seven', 'sieben', 'sept', '七', 'なな', 'nana'),
    ('8', 'eight', 'acht', 'huit', '八', 'はち', 'hachi'),
    ('9', 'nine', 'neun', 'neuf', '九', 'きゅう', 'kyuu'),
    ('10', 'ten', 'zehn', 'dix', '十', 'じゅう', 'juu'),
    ('11', 'eleven', 'elf', 'onze', '十一', 'じゅういち', 'juuichi'),
    ('12', 'twelve', 'zwölf', 'douze', '十二', 'じゅうに', 'juuni'),
    ('13', 'thirteen', 'dreizehn', 'treize', '十三', 'じゅうさん', 'juusan'),
    ('14', 'fourteen', 'vierzehn', 'quatorze', '十四', 'じゅうよん', 'juuyon'),
    ('15', 'fifteen', 'fünfzehn', 'quinze', '十五', 'じゅうご', 'juugo'),
    ('16', 'sixteen', 'sechzehn', 'seize', '十六', 'じゅうろく', 'juuroku'),
    ('17', 'seventeen', 'siebzehn', 'dix-sept', '十七', 'じゅうなな', 'juunana'),
    ('18', 'eighteen', 'achtzehn', 'dix-huit', '十八', 'じゅうはち', 'juuhachi'),
    ('19', 'nineteen', 'neunzehn', 'dix-neuf', '十九', 'じゅうきゅう', 'juukyuu'),
    ('20', 'twenty', 'zwanzig', 'vingt', '二十', 'にじゅう', 'nijuu'),
    ('21', 'twenty-one', 'einundzwanzig', 'vingt et un', '二十一', 'にじゅういち', 'nijuuichi'),
    ('22', 'twenty-two', 'zweiundzwanzig', 'vingt-deux', '二十二', 'にじゅうに', 'nijuuni'),
    ('23', 'twenty-three', 'dreiundzwanzig', 'vingt-trois', '二十三', 'にじゅうさん', 'nijuusan'),
    ('24', 'twenty-four', 'vierundzwanzig', 'vingt-quatre', '二十四', 'にじゅうよん', 'nijuuyon'),
    ('25', 'twenty-five', 'fünfundzwanzig', 'vingt-cinq', '二十五', 'にじゅうご', 'nijuugo'),
    ('26', 'twenty-six', 'sechsundzwanzig', 'vingt-six', '二十六', 'にじゅうろく', 'nijuuroku'),
    ('27', 'twenty-seven', 'siebenundzwanzig', 'vingt-sept', '二十七', 'にじゅうなな', 'nijuunana'),
    ('28', 'twenty-eight', 'achtundzwanzig', 'vingt-huit', '二十八', 'にじゅうはち', 'nijuuhachi'),
    ('29', 'twenty-nine', 'neunundzwanzig', 'vingt-neuf', '二十九', 'にじゅうきゅう', 'nijuukyuu'),
    ('30', 'thirty', 'dreißig', 'trente', '三十', 'さんじゅう', 'sanjuu'),
]

# Place-value / large-number words (Chinese order requested by the user).
# 個 = ones place; East Asian 億 = 10^8, 兆 = 10^12.
SCALES = [
    ('個', 'ones', 'Einer', 'unité', '一', 'いち', 'ichi'),
    ('十', 'ten', 'Zehn', 'dix', '十', 'じゅう', 'juu'),
    ('百', 'hundred', 'Hundert', 'cent', '百', 'ひゃく', 'hyaku'),
    ('千', 'thousand', 'Tausend', 'mille', '千', 'せん', 'sen'),
    ('十萬', 'hundred thousand', 'hunderttausend', 'cent mille', '十万', 'じゅうまん', 'juuman'),
    ('百萬', 'million', 'Million', 'million', '百万', 'ひゃくまん', 'hyakuman'),
    ('千萬', 'ten million', 'zehn Millionen', 'dix millions', '千万', 'せんまん', 'senman'),
    ('億', 'hundred million', 'hundert Millionen', 'cent millions', '億', 'おく', 'oku'),
    ('兆', 'trillion', 'Billion', 'billion', '兆', 'ちょう', 'chou'),
]

SECTIONS = [
    ('季節', SEASONS),
    ('月份', MONTHS),
    ('時間單位', TIME_WORDS),
    ('星期', WEEKDAYS),
    ('數字 0–30', NUMBERS),
    ('數位與大數', SCALES),
]

THEMES = {
    'en': {
        'brand': '英文筆記',
        'title': 'Vocabulary｜英文單字',
        'h1': '英文單字表',
        'intro': '季節、月份、星期、數字與大數單位。點選單字可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#154a85',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'en-US',
        'slug': 'vocab',
        'card_title': 'Vocabulary',
        'card': '季節、月份、星期、數字與大數單位：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '單字 · 跟讀',
        'word_col': '英文',
    },
    'de': {
        'brand': '德文筆記',
        'title': 'Wortschatz｜德文單字',
        'h1': '德文單字表',
        'intro': '季節、月份、星期、數字與大數單位。點選單字可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#1d6a4f',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'de-DE',
        'slug': 'vocab',
        'card_title': 'Wortschatz',
        'card': '季節、月份、星期、數字與大數單位：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '單字 · 跟讀',
        'word_col': '德文',
    },
    'fr': {
        'brand': '法文筆記',
        'title': 'Vocabulaire｜法文單字',
        'h1': '法文單字表',
        'intro': '季節、月份、星期、數字與大數單位。點選單字可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#b3482f',
        'bg': '#f7f4f2',
        'border': '#eadfd6',
        'lang': 'fr-FR',
        'slug': 'vocab',
        'card_title': 'Vocabulaire',
        'card': '季節、月份、星期、數字與大數單位：可單字朗讀，也可全部循環播放並調語速。',
        'meta': '單字 · 跟讀',
        'word_col': '法文',
    },
    'ja': {
        'brand': '日文筆記',
        'title': '単語｜日文單字',
        'h1': '日文單字表',
        'intro': '季節、月份、星期、數字與大數單位。每一詞附漢字、假名與羅馬拼音。點選可朗讀；也可全部循環播放並調語速。',
        'accent': '#8d3a55',
        'bg': '#f7f3f5',
        'border': '#eadde2',
        'lang': 'ja-JP',
        'slug': 'vocab',
        'card_title': '単語',
        'card': '季節、月份、星期、數字與大數：漢字、平片假名、羅馬拼音；可單字朗讀或全部循環播放並調語速。',
        'meta': '單字 · 跟讀',
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
  current = null;
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
    setTimeout(playNext, 280);
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


def latin_rows(lang_key, col_index):
    blocks = []
    for title, rows in SECTIONS:
        items = []
        for row in rows:
            zh = row[0]
            word = row[col_index]
            items.append((zh, word, word))
        blocks.append((title, items))
    return blocks


def to_katakana(text):
    out = []
    for ch in text:
        code = ord(ch)
        if 0x3041 <= code <= 0x3096:
            out.append(chr(code + 0x60))
        else:
            out.append(ch)
    return ''.join(out)


def to_hiragana(text):
    out = []
    for ch in text:
        code = ord(ch)
        if 0x30A1 <= code <= 0x30F6:
            out.append(chr(code - 0x60))
        else:
            out.append(ch)
    return ''.join(out)


def ja_rows():
    blocks = []
    for title, rows in SECTIONS:
        items = []
        for row in rows:
            zh, _en, _de, _fr, kanji, kana, roma = row
            hira = to_hiragana(kana)
            kata = to_katakana(hira) if any('\u3040' <= ch <= '\u309f' for ch in hira) or any('\u30a0' <= ch <= '\u30ff' for ch in kana) else to_katakana(to_hiragana(kana))
            # Keep Latin/choonpu mixed tokens readable: ゼロ stays as katakana word
            if kana == 'ゼロ':
                hira = 'ぜろ'
                kata = 'ゼロ'
            items.append((zh, kanji, hira, kata, roma, kanji))
        blocks.append((title, items))
    return blocks


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


def page_for(lang):
    theme = THEMES[lang]
    accent = theme['accent']
    if lang == 'ja':
        body_parts = [controls_html(accent)]
        for title, items in ja_rows():
            rows_html = []
            for zh, kanji, hira, kata, roma, say in items:
                rows_html.append(
                    '<tr class="vocab-row">'
                    f'<td class="zh">{html.escape(zh)}</td>'
                    f'<td><button type="button" class="say" lang="ja" data-say="{html.escape(say)}" data-lang="ja-JP">'
                    f'<span class="kanji">{html.escape(kanji)}</span>'
                    f'<span class="kana"><span class="hira">{html.escape(hira)}</span>　<span class="kata">{html.escape(kata)}</span></span>'
                    f'<span class="roma">{html.escape(roma)}</span>'
                    f'</button></td>'
                    '</tr>'
                )
            body_parts.append(
                f'<h2>{html.escape(title)}</h2>'
                '<div class="tablewrap"><table>'
                '<thead><tr><th scope="col">中文</th><th scope="col">漢字 · 平假名 · 片假名 · 羅馬拼音</th></tr></thead>'
                f'<tbody>{"".join(rows_html)}</tbody></table></div>'
            )
    else:
        col = {'en': 1, 'de': 2, 'fr': 3}[lang]
        body_parts = [controls_html(accent)]
        for title, items in latin_rows(lang, col):
            rows_html = []
            for zh, word, say in items:
                rows_html.append(
                    '<tr class="vocab-row">'
                    f'<td class="zh">{html.escape(zh)}</td>'
                    f'<td><button type="button" class="say" lang="{lang}" data-say="{html.escape(say)}" data-lang="{theme["lang"]}">'
                    f'<span class="word">{html.escape(word)}</span>'
                    f'</button></td>'
                    '</tr>'
                )
            body_parts.append(
                f'<h2>{html.escape(title)}</h2>'
                '<div class="tablewrap"><table>'
                f'<thead><tr><th scope="col">中文</th><th scope="col">{html.escape(theme["word_col"])}</th></tr></thead>'
                f'<tbody>{"".join(rows_html)}</tbody></table></div>'
            )

    tip = (
        '點選單字可單獨朗讀。「全部循環播放」會依頁面順序朗讀；勾選「播完從頭再播」會一直循環，直到按停止。'
        '語速可用滑桿調整。日文朗讀的是漢字寫法。'
        if lang == 'ja'
        else '點選單字可單獨朗讀。「全部循環播放」會依頁面順序朗讀；勾選「播完從頭再播」會一直循環，直到按停止。語速可用滑桿調整。'
    )
    if lang == 'ja':
        tip += ' 每一詞列出漢字、平假名、片假名與羅馬拼音；濁音、半濁音直接寫在假名裡。數字四可讀よん或し；這裡標よん。七月標しちがつ。'

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
h2{{font-size:1.25rem;margin:28px 0 10px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid {theme['border']};border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{accent};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {accent};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid {theme['border']};border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:420px}}
th{{background:#f4f7fb;text-align:left;font-size:.9rem;padding:12px 14px}}
td{{padding:10px 14px;border-top:1px solid {theme['border']};vertical-align:middle}}
.zh{{color:#53647c;width:34%}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 0;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.word,.kanji{{font-size:1.15rem;font-weight:750;color:{accent}}}
.kana{{font-size:.98rem;color:#3d4d63}}
.hira{{margin-right:0}}
.kata{{color:#6a5870}}
.roma{{font-size:.88rem;color:#6a5870}}
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
{''.join(body_parts)}
<div class="tip"><strong>用法提醒：</strong>{html.escape(tip)}</div>
</main>
<footer>{html.escape(theme['title'])}</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def vocab_card_html(lang):
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
    card = vocab_card_html(lang)
    # Prefer inserting right after the alphabet / gojuon card block.
    markers = ('href="./alphabet/"', 'href="./gojuon/"')
    insert_at = None
    for marker in markers:
        pos = text.find(marker)
        if pos != -1:
            end = text.find('</article>', pos)
            if end != -1:
                insert_at = end + len('</article>')
                break
    if insert_at is None:
        h2 = text.find('<h2>')
        if h2 < 0:
            raise SystemExit(f'cannot inject vocab into {path}')
        # Before first level heading, after alphabet section if any
        insert_at = h2
        text = text[:insert_at] + '<h2>單字表</h2>\n' + card + text[insert_at:]
    else:
        # Same 字母表 section: append vocab card after alphabet card
        text = text[:insert_at] + '\n' + card + text[insert_at:]
        if '<h2>單字表</h2>' not in text and '<h2>字母表</h2>' in text:
            # Keep under 字母表 heading is odd; add 單字表 heading before vocab card
            text = text.replace(card, '<h2>單字表</h2>\n' + card, 1)
    path.write_text(text, encoding='utf-8')
    print('index', path)


def write_pages():
    for lang in ('en', 'de', 'fr', 'ja'):
        folder = ROOT / lang / THEMES[lang]['slug']
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / 'index.html'
        path.write_text(page_for(lang), encoding='utf-8')
        print(path)


def main():
    write_pages()
    for lang in ('en', 'de', 'fr', 'ja'):
        inject_index(lang)


if __name__ == '__main__':
    main()
