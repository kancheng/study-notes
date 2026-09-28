"""Build multilingual comparison tables under tables/."""
import html
import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent

spec = importlib.util.spec_from_file_location('build_vocab', Path(__file__).parent / 'build_vocab.py')
vocab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vocab)

ACCENT = '#445a7a'
EN = '#17355d'
DE = '#1d6a4f'
FR = '#b3482f'
JA = '#8d3a55'

# (zh, en, de, fr, ja_kanji, ja_kana, ja_roma)
WH_WORDS = [
    ('誰', 'who', 'wer', 'qui', 'だれ', 'だれ', 'dare'),
    ('什麼', 'what', 'was', 'que / qu’est-ce que', '何', 'なに', 'nani'),
    ('何時', 'when', 'wann', 'quand', 'いつ', 'いつ', 'itsu'),
    ('哪裡', 'where', 'wo', 'où', 'どこ', 'どこ', 'doko'),
    ('為什麼', 'why', 'warum', 'pourquoi', 'なぜ', 'なぜ', 'naze'),
    ('如何', 'how', 'wie', 'comment', 'どう', 'どう', 'dou'),
]

WH_EXAMPLES = [
    ('誰要來？', 'Who is coming?', 'Wer kommt?', 'Qui vient ?', '誰が来ますか。', 'だれ が きます か。', 'Dare ga kimasu ka.'),
    ('你在學什麼？', 'What are you studying?', 'Was lernst du?', 'Qu’est-ce que tu étudies ?', '何を勉強しますか。', 'なに を べんきょう します か。', 'Nani o benkyou shimasu ka.'),
    ('課幾點開始？', 'When does the class start?', 'Wann beginnt der Unterricht?', 'Quand commence le cours ?', '授業はいつ始まりますか。', 'じゅぎょう は いつ はじまります か。', 'Jugyou wa itsu hajimarimasu ka.'),
    ('你住哪裡？', 'Where do you live?', 'Wo wohnst du?', 'Où habites-tu ?', 'どこに住みますか。', 'どこ に すみます か。', 'Doko ni sumimasu ka.'),
    ('你為什麼學英文？', 'Why are you learning English?', 'Warum lernst du Englisch?', 'Pourquoi apprends-tu l’anglais ?', 'なぜ英語を勉強しますか。', 'なぜ えいご を べんきょう します か。', 'Naze eigo o benkyou shimasu ka.'),
    ('你怎麼練習？', 'How do you practice?', 'Wie übst du?', 'Comment est-ce que tu t’entraînes ?', 'どうやって練習しますか。', 'どうやって れんしゅう します か。', 'Douyatte renshuu shimasu ka.'),
]

WH_SECTIONS = [
    ('疑問詞', WH_WORDS),
    ('例句對照', WH_EXAMPLES),
]

SPEECH_JS = r'''
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
    lang: el.dataset.lang,
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
    speakOnce(b.dataset.say, b.dataset.lang, rate, () => {
      clearActive();
      setStatus('待命');
    });
  });
});

if ('speechSynthesis' in window) speechSynthesis.getVoices();
'''


def slugify(title):
    mapping = {
        '季節': 'seasons',
        '月份': 'months',
        '時間單位': 'time',
        '星期': 'weekdays',
        '數字 0–30': 'numbers',
        '數位與大數': 'scales',
        '疑問詞': 'wh-words',
        '例句對照': 'wh-examples',
    }
    return mapping.get(title, title)


def ja_cell(kanji, kana, roma):
    hira = vocab.to_hiragana(kana)
    if kana == 'ゼロ':
        hira = 'ぜろ'
        kata = 'ゼロ'
    else:
        kata = vocab.to_katakana(hira)
    return (
        f'<button type="button" class="say ja" lang="ja" data-say="{html.escape(kanji)}" data-lang="ja-JP">'
        f'<span class="word">{html.escape(kanji)}</span>'
        f'<span class="sub"><span class="hira">{html.escape(hira)}</span>　'
        f'<span class="kata">{html.escape(kata)}</span></span>'
        f'<span class="roma">{html.escape(roma)}</span>'
        f'</button>'
    )


def latin_cell(word, lang_code, css):
    return (
        f'<button type="button" class="say {css}" lang="{lang_code[:2]}" '
        f'data-say="{html.escape(word)}" data-lang="{lang_code}">'
        f'<span class="word">{html.escape(word)}</span>'
        f'</button>'
    )


def section_html(title, rows):
    sid = slugify(title)
    body = []
    for row in rows:
        zh, en, de, fr, kanji, kana, roma = row
        body.append(
            '<tr class="vocab-row">'
            f'<td class="zh">{html.escape(zh)}</td>'
            f'<td class="col-en">{latin_cell(en, "en-US", "en")}</td>'
            f'<td class="col-de">{latin_cell(de, "de-DE", "de")}</td>'
            f'<td class="col-fr">{latin_cell(fr, "fr-FR", "fr")}</td>'
            f'<td class="col-ja">{ja_cell(kanji, kana, roma)}</td>'
            '</tr>'
        )
    return f'''
<section id="{sid}">
<h2>{html.escape(title)}</h2>
<div class="tablewrap">
<table>
<thead>
<tr>
<th scope="col">中文</th>
<th scope="col" class="th-en">英文</th>
<th scope="col" class="th-de">德文</th>
<th scope="col" class="th-fr">法文</th>
<th scope="col" class="th-ja">日文</th>
</tr>
</thead>
<tbody>
{''.join(body)}
</tbody>
</table>
</div>
</section>
'''


def toc_html():
    links = []
    for title, _ in vocab.SECTIONS:
        links.append(f'<a href="#{slugify(title)}">{html.escape(title)}</a>')
    return '<nav class="toc" aria-label="章節">' + ''.join(links) + '</nav>'


def vocab_page():
    sections = ''.join(section_html(title, rows) for title, rows in vocab.SECTIONS)
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="英、德、法、日合併單字對照：季節、月份、星期、數字與大數單位。點選可朗讀。">
<title>單字對照｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:#f2f5fa}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{ACCENT};color:white;padding:22px max(20px,calc((100vw - 1180px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1180px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.25rem;margin:32px 0 12px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.toc{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}}
.toc a{{display:inline-block;padding:7px 12px;border-radius:9px;background:white;border:1px solid #dae3ef;color:{ACCENT};text-decoration:none;font-weight:650;font-size:.92rem}}
.toc a:hover,.toc a:focus-visible{{outline:2px solid {ACCENT};outline-offset:2px}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid #dae3ef;border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{ACCENT};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {ACCENT};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid #dae3ef;border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:920px}}
th{{background:#eef2f7;text-align:left;font-size:.9rem;padding:12px 12px;white-space:nowrap}}
.th-en{{color:{EN}}}
.th-de{{color:{DE}}}
.th-fr{{color:{FR}}}
.th-ja{{color:{JA}}}
td{{padding:10px 12px;border-top:1px solid #e6edf5;vertical-align:top}}
.zh{{color:#53647c;font-weight:650;white-space:nowrap}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 2px;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid currentColor;outline-offset:2px}}
.say .word{{font-size:1.05rem;font-weight:750}}
.say.en,.th-en,.say.en .word{{color:{EN}}}
.say.de,.th-de,.say.de .word{{color:{DE}}}
.say.fr,.th-fr,.say.fr .word{{color:{FR}}}
.say.ja,.th-ja,.say.ja .word{{color:{JA}}}
.sub{{font-size:.9rem;color:#3d4d63}}
.kata{{color:#6a5870}}
.roma{{font-size:.82rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {ACCENT};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid #dae3ef;border-left-width:4px;line-height:1.7;color:#52647a}}
.tip a{{color:{ACCENT};font-weight:650;text-decoration:none}}
.tip a:hover,.tip a:focus-visible{{text-decoration:underline}}
footer{{max-width:1180px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:700px){{main{{padding-top:25px}}.rate input{{width:100px}}}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 對表</a>　/　單字對照</div></header>
<main>
<h1>四語單字對照</h1>
<p class="note">春夏秋冬、一到十二月、一周／周末／月／年、星期一到日、數字 0–30，以及個到兆。點選任一格可朗讀；日文欄附漢字、平假名、片假名與羅馬拼音。</p>
{toc_html()}
<div class="controls">
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
{sections}
<div class="tip"><strong>用法提醒：</strong>點選單字可單獨朗讀；「全部循環播放」依英→德→法→日順序逐格朗讀。日文朗讀漢字寫法。德文「Billion」對應英文 trillion（10<sup>12</sup>）；東亞「億」是 10<sup>8</sup>、「兆」是 10<sup>12</sup>。五十音表見 <a href="../../ja/gojuon/">日文五十音</a>。</div>
</main>
<footer>單字對照｜四語筆記</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def index_page():
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="多語比較：英文、法文、德文、日文並排對照。">
<title>對表｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC',sans-serif;color:#172b47;background:#f2f5fa}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{ACCENT};padding:20px max(20px,calc((100vw - 920px)/2))}}
header a{{color:white;text-decoration:none;font-weight:700}}
main{{max-width:920px;margin:auto;padding:44px 20px 80px}}
.eyebrow{{font-size:.9rem;font-weight:750;letter-spacing:.06em;color:{ACCENT}}}
h1{{font-size:clamp(2rem,5vw,3rem);margin:10px 0}}
p{{line-height:1.7;color:#53647c}}
h2{{font-size:1.15rem;margin:36px 0 15px}}
.item{{background:white;border:1px solid #dce4ef;border-radius:16px;padding:26px;box-shadow:0 10px 25px #172b470c;margin:0 0 14px}}
.item h3{{font-size:1.45rem;margin:0 0 8px}}
.item p{{margin:0 0 18px}}
.meta{{font-size:.9rem;color:#776b5c;margin-bottom:10px}}
.button{{display:inline-block;padding:11px 18px;border-radius:9px;background:{ACCENT};color:white;text-decoration:none;font-weight:750}}
.button:hover,.button:focus-visible{{background:#334761;outline:2px solid #334761;outline-offset:2px}}
.langs{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px}}
.langs span{{font-size:.85rem;font-weight:750}}
.langs .en{{color:{EN}}}
.langs .de{{color:{DE}}}
.langs .fr{{color:{FR}}}
.langs .ja{{color:{JA}}}
@media(max-width:600px){{main{{padding-top:30px}}.item{{padding:21px}}}}
</style>
</head>
<body>
<header><a href="../index.html">← 四語筆記首頁</a></header>
<main>
<div class="eyebrow">COMPARE · 對表</div>
<h1>對表</h1>
<p>這一區獨立於英文、法文、德文、日文。多語比較表放在這裡，一張表並排四種語言。</p>
<h2>比較清單</h2>
<article class="item">
<div class="meta">單字 · 四語對照 · 跟讀</div>
<h3>單字對照</h3>
<div class="langs">
<span class="en">EN</span>
<span class="de">DE</span>
<span class="fr">FR</span>
<span class="ja">JA</span>
</div>
<p>春夏秋冬、一到十二月、一周／周末／月／年、星期一到日、數字 0–30、個到兆。日文欄附漢字、平假名、片假名與羅馬拼音。</p>
<a class="button" href="./vocab/">進入單字對照 →</a>
</article>
<article class="item">
<div class="meta">文法 · WH 疑問詞 · 跟讀</div>
<h3>疑問詞對照</h3>
<div class="langs">
<span class="en">EN</span>
<span class="de">DE</span>
<span class="fr">FR</span>
<span class="ja">JA</span>
</div>
<p>who／wer／qui／だれ，what／was／que／何，when／wann／quand／いつ，where／wo／où／どこ，why／warum／pourquoi／なぜ，how／wie／comment／どう。附例句對照。</p>
<a class="button" href="./wh-questions/">進入疑問詞對照 →</a>
</article>
<article class="item">
<div class="meta">五十音 · 平片假名 · 清濁半濁</div>
<h3 lang="ja">日文五十音</h3>
<div class="langs"><span class="ja">JA</span></div>
<p>平假名、片假名完整對照：清音、濁音、半濁音、拗音，並標平文式羅馬拼音。點選可朗讀。</p>
<a class="button" href="../ja/gojuon/">進入五十音 →</a>
</article>
</main>
</body>
</html>
'''


def wh_page():
    sections = ''.join(section_html(title, rows) for title, rows in WH_SECTIONS)
    toc = '<nav class="toc" aria-label="章節">' + ''.join(
        f'<a href="#{slugify(title)}">{html.escape(title)}</a>' for title, _ in WH_SECTIONS
    ) + '</nav>'
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="英、德、法、日疑問詞對照：who、what、when、where、why、how 與例句。點選可朗讀。">
<title>疑問詞對照｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:#f2f5fa}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{ACCENT};color:white;padding:22px max(20px,calc((100vw - 1180px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1180px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.25rem;margin:32px 0 12px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.toc{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}}
.toc a{{display:inline-block;padding:7px 12px;border-radius:9px;background:white;border:1px solid #dae3ef;color:{ACCENT};text-decoration:none;font-weight:650;font-size:.92rem}}
.toc a:hover,.toc a:focus-visible{{outline:2px solid {ACCENT};outline-offset:2px}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid #dae3ef;border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{ACCENT};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {ACCENT};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid #dae3ef;border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:920px}}
th{{background:#eef2f7;text-align:left;font-size:.9rem;padding:12px 12px;white-space:nowrap}}
.th-en{{color:{EN}}}
.th-de{{color:{DE}}}
.th-fr{{color:{FR}}}
.th-ja{{color:{JA}}}
td{{padding:10px 12px;border-top:1px solid #e6edf5;vertical-align:top}}
.zh{{color:#53647c;font-weight:650;white-space:nowrap}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 2px;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid currentColor;outline-offset:2px}}
.say .word{{font-size:1.05rem;font-weight:750}}
.say.en,.th-en,.say.en .word{{color:{EN}}}
.say.de,.th-de,.say.de .word{{color:{DE}}}
.say.fr,.th-fr,.say.fr .word{{color:{FR}}}
.say.ja,.th-ja,.say.ja .word{{color:{JA}}}
.sub{{font-size:.9rem;color:#3d4d63}}
.kata{{color:#6a5870}}
.roma{{font-size:.82rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {ACCENT};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid #dae3ef;border-left-width:4px;line-height:1.7;color:#52647a}}
.tip a{{color:{ACCENT};font-weight:650;text-decoration:none}}
.tip a:hover,.tip a:focus-visible{{text-decoration:underline}}
footer{{max-width:1180px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:700px){{main{{padding-top:25px}}.rate input{{width:100px}}}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 對表</a>　/　疑問詞對照</div></header>
<main>
<h1>四語疑問詞對照</h1>
<p class="note">who、what、when、where、why、how 與德、法、日對應詞，並附六句平行例句。點選任一格可朗讀；日文欄附漢字、平假名、片假名與羅馬拼音。</p>
{toc}
<div class="controls">
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
{sections}
<div class="tip"><strong>用法提醒：</strong>各國語法的語序不同：英文常是疑問詞＋助動詞＋主詞；德文是疑問詞＋動詞；法文口語常用 est-ce que；日文疑問詞可在句中，句尾加「か」。各語言專頁：<a href="../../en/wh-questions/">英文</a> · <a href="../../de/w-fragen/">德文</a> · <a href="../../fr/interrogatifs/">法文</a> · <a href="../../ja/gimonshi/">日文</a>。</div>
</main>
<footer>疑問詞對照｜四語筆記</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def main():
    out = ROOT / 'tables' / 'vocab'
    out.mkdir(parents=True, exist_ok=True)
    path = out / 'index.html'
    path.write_text(vocab_page(), encoding='utf-8')
    print(path)
    wh_out = ROOT / 'tables' / 'wh-questions'
    wh_out.mkdir(parents=True, exist_ok=True)
    wh_path = wh_out / 'index.html'
    wh_path.write_text(wh_page(), encoding='utf-8')
    print(wh_path)
    index = ROOT / 'tables' / 'index.html'
    index.write_text(index_page(), encoding='utf-8')
    print(index)


if __name__ == '__main__':
    main()
