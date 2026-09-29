"""Build email-writing lesson pages for en, de, fr, and ja."""
import html
from pathlib import Path

from email_data import EXAMPLE, INTRO_BY_LANG, INTRO_SHARED, SUBJECT_PART

ROOT = Path(__file__).parent.parent

THEMES = {
    'en': {
        'brand': '英文筆記',
        'title': 'Email Writing｜英文電子郵件寫作',
        'h1': '英文電子郵件寫作',
        'intro': '電子郵件入門：結構說明、一封完整範例，以及逐行講解。點選句子可朗讀，也可全部循環播放。',
        'accent': '#17355d',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'en-US',
        'slug': 'email',
        'card_title': 'Email Writing',
        'card': '電子郵件入門：主旨、稱呼、來意、請求與結尾。附完整範例與逐行說明，可朗讀或循環播放。',
        'meta': '寫作 · 電子郵件 · 跟讀',
        'lang_label': '英文',
        'subject_label': 'Subject',
    },
    'de': {
        'brand': '德文筆記',
        'title': 'E-Mail schreiben｜德文電子郵件寫作',
        'h1': '德文電子郵件寫作',
        'intro': '電子郵件入門：結構說明、一封完整範例，以及逐行講解。點選句子可朗讀，也可全部循環播放。',
        'accent': '#1d6a4f',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'de-DE',
        'slug': 'email',
        'card_title': 'E-Mail schreiben',
        'card': '電子郵件入門：主旨、稱呼、來意、請求與結尾。附完整範例與逐行說明，可朗讀或循環播放。',
        'meta': '寫作 · 電子郵件 · 跟讀',
        'lang_label': '德文',
        'subject_label': 'Betreff',
    },
    'fr': {
        'brand': '法文筆記',
        'title': 'Écrire un e-mail｜法文電子郵件寫作',
        'h1': '法文電子郵件寫作',
        'intro': '電子郵件入門：結構說明、一封完整範例，以及逐行講解。點選句子可朗讀，也可全部循環播放。',
        'accent': '#b3482f',
        'bg': '#f7f4f2',
        'border': '#eadfd6',
        'lang': 'fr-FR',
        'slug': 'email',
        'card_title': 'Écrire un e-mail',
        'card': '電子郵件入門：主旨、稱呼、來意、請求與結尾。附完整範例與逐行說明，可朗讀或循環播放。',
        'meta': '寫作 · 電子郵件 · 跟讀',
        'lang_label': '法文',
        'subject_label': 'Objet',
    },
    'ja': {
        'brand': '日文筆記',
        'title': 'メールの書き方｜日文電子郵件寫作',
        'h1': '日文電子郵件寫作',
        'intro': '電子郵件入門：結構說明、一封完整範例，以及逐行講解。每一行附漢字、平假名、片假名與羅馬拼音；可朗讀或循環播放。',
        'accent': '#8d3a55',
        'bg': '#f7f3f5',
        'border': '#eadde2',
        'lang': 'ja-JP',
        'slug': 'email',
        'card_title': 'メールの書き方',
        'card': '電子郵件入門：件名、稱呼、來意、請求與結尾。附完整範例與逐行說明（漢字／假名／羅馬拼音），可朗讀或循環播放。',
        'meta': '寫作 · 電子郵件 · 跟讀',
        'lang_label': '日文',
        'subject_label': '件名',
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
  // Prefer line-by-line table so the full sample is not spoken twice.
  const scope = document.querySelectorAll('#lines [data-say]');
  const nodes = scope.length ? scope : document.querySelectorAll('[data-say]');
  return [...nodes].map(el => ({
    text: el.dataset.say,
    lang: el.dataset.lang || lessonLang,
    el,
  }));
}

function clearActive() {
  document.querySelectorAll('.vocab-row.active, .mail-line.active').forEach(r => r.classList.remove('active'));
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
  const row = item.el.closest('.vocab-row, .mail-line');
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
    const row = b.closest('.vocab-row, .mail-line');
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


def to_katakana(text):
    out = []
    for ch in text:
        code = ord(ch)
        if 0x3041 <= code <= 0x3096:
            out.append(chr(code + 0x60))
        else:
            out.append(ch)
    return ''.join(out)


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


def intro_html(lang):
    items = INTRO_SHARED + INTRO_BY_LANG[lang]
    blocks = []
    for title, body in items:
        blocks.append(
            '<div class="intro-item">'
            f'<h3>{html.escape(title)}</h3>'
            f'<p>{html.escape(body)}</p>'
            '</div>'
        )
    return (
        '<section class="intro-sec" id="intro">'
        '<h2>電子郵件寫作入門</h2>'
        '<p class="note">先掌握結構與語氣，再套用下面的完整範例。正式程度依收件人調整；不確定時，選稍正式的寫法較安全。</p>'
        f'<div class="intro-grid">{"".join(blocks)}</div>'
        '</section>'
    )


def say_button_latin(text, lang_code, css_lang):
    return (
        f'<button type="button" class="say" lang="{css_lang}" '
        f'data-say="{html.escape(text)}" data-lang="{lang_code}">'
        f'<span class="word">{html.escape(text)}</span>'
        f'</button>'
    )


def say_button_ja(kanji, kana, roma):
    kata = to_katakana(kana)
    return (
        f'<button type="button" class="say" lang="ja" '
        f'data-say="{html.escape(kanji)}" data-lang="ja-JP">'
        f'<span class="kanji">{html.escape(kanji)}</span>'
        f'<span class="kana"><span class="hira">{html.escape(kana)}</span>　'
        f'<span class="kata">{html.escape(kata)}</span></span>'
        f'<span class="roma">{html.escape(roma)}</span>'
        f'</button>'
    )


def example_block_html(lang, theme):
    rows = EXAMPLE[lang]
    subject_label = theme['subject_label']
    lines = []
    for row in rows:
        if lang == 'ja':
            part, kanji, kana, roma, _note = row
            speak = say_button_ja(kanji, kana, roma)
        else:
            part, text, _note = row
            speak = say_button_latin(text, theme['lang'], lang)
        if part == SUBJECT_PART:
            lines.append(
                f'<div class="mail-line subject vocab-row">'
                f'<span class="mail-label">{html.escape(subject_label)}</span>'
                f'{speak}'
                f'</div>'
            )
        else:
            lines.append(f'<div class="mail-line vocab-row">{speak}</div>')
    return (
        '<section id="example">'
        '<h2>完整範例</h2>'
        '<p class="note">情境：Hao-Cheng 第一次寫信給田中女士，請求下週短短開會討論專案時程。點選任一行可朗讀。</p>'
        f'<div class="mail">{"".join(lines)}</div>'
        '</section>'
    )


def line_table_html(lang, theme):
    rows = EXAMPLE[lang]
    body = []
    if lang == 'ja':
        head = (
            '<thead><tr>'
            '<th scope="col">段落</th>'
            '<th scope="col">漢字 · 平假名 · 片假名 · 羅馬拼音</th>'
            '<th scope="col">說明</th>'
            '</tr></thead>'
        )
        for part, kanji, kana, roma, note in rows:
            body.append(
                '<tr class="vocab-row">'
                f'<td class="part">{html.escape(part)}</td>'
                f'<td>{say_button_ja(kanji, kana, roma)}</td>'
                f'<td class="zh">{html.escape(note)}</td>'
                '</tr>'
            )
    else:
        label = theme['lang_label']
        head = (
            '<thead><tr>'
            '<th scope="col">段落</th>'
            f'<th scope="col">{html.escape(label)}</th>'
            '<th scope="col">說明</th>'
            '</tr></thead>'
        )
        for part, text, note in rows:
            body.append(
                '<tr class="vocab-row">'
                f'<td class="part">{html.escape(part)}</td>'
                f'<td>{say_button_latin(text, theme["lang"], lang)}</td>'
                f'<td class="zh">{html.escape(note)}</td>'
                '</tr>'
            )
    return (
        '<section id="lines">'
        '<h2>逐行說明</h2>'
        '<p class="note">每一行對應範例中的一個區塊：看說法、聽發音，並對照中文說明為什麼這樣寫。</p>'
        f'<div class="tablewrap"><table>{head}<tbody>{"".join(body)}</tbody></table></div>'
        '</section>'
    )


def tip_html(lang):
    tips = {
        'en': '主旨保持簡短清楚。正式信用 Dear Ms./Mr. + 姓與 Best regards；回信可先 Thank you for your email.',
        'de': '正式信用 Sehr geehrte(r)… 與 Mit freundlichen Grüßen（多半不加逗號）。公事用 Sie／Ihnen。',
        'fr': '主旨寫在 Objet。正式可用 Madame／Monsieur 與 Cordialement；請求多用 conditionnel（pourriez、voudrais）。',
        'ja': '件名寫具體事由。稱呼用「様」；來意可用「〜と思い、メールいたしました」。朗讀以漢字句為準。',
    }
    return (
        '<div class="tip"><strong>用法提醒：</strong>'
        f'{html.escape(tips[lang])} '
        '上方「全部循環播放」會依頁面可點讀句子順序朗讀；可調語速，勾選後會循環直到按停止。'
        '</div>'
    )


def toc_html():
    return (
        '<nav class="toc" aria-label="章節">'
        '<a href="#intro">寫作入門</a>'
        '<a href="#example">完整範例</a>'
        '<a href="#lines">逐行說明</a>'
        '</nav>'
    )


def page_for(lang):
    theme = THEMES[lang]
    accent = theme['accent']
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
h2{{font-size:1.25rem;margin:32px 0 10px}}
h3{{font-size:1.02rem;margin:0 0 6px;color:{accent}}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.toc{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}}
.toc a{{display:inline-block;padding:7px 12px;border-radius:9px;background:white;border:1px solid {theme['border']};color:{accent};text-decoration:none;font-weight:650;font-size:.92rem}}
.toc a:hover,.toc a:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.intro-grid{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin:0 0 8px}}
.intro-item{{background:white;border:1px solid {theme['border']};border-radius:14px;padding:14px 16px;box-shadow:0 6px 18px #142f520c}}
.intro-item p{{margin:0;font-size:.95rem}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid {theme['border']};border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:22px 0;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{accent};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {accent};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.mail{{background:white;border:1px solid {theme['border']};border-radius:14px;padding:18px 20px;box-shadow:0 6px 18px #142f520c;display:flex;flex-direction:column;gap:10px}}
.mail-line{{border-radius:8px;padding:4px 2px}}
.mail-line.subject{{padding-bottom:12px;margin-bottom:4px;border-bottom:1px dashed {theme['border']}}}
.mail-label{{display:block;font-size:.82rem;font-weight:700;color:#6a5870;margin:0 0 4px}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid {theme['border']};border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:560px}}
th{{background:#f4f7fb;text-align:left;font-size:.9rem;padding:12px 14px}}
td{{padding:12px 14px;border-top:1px solid {theme['border']};vertical-align:top}}
.part{{color:{accent};font-weight:750;white-space:nowrap;width:7.5rem}}
.zh{{color:#53647c;line-height:1.55}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 0;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.word,.kanji{{font-size:1.05rem;font-weight:750;color:{accent};line-height:1.45}}
.kana{{font-size:.95rem;color:#3d4d63}}
.kata{{color:#6a5870}}
.roma{{font-size:.85rem;color:#6a5870}}
.vocab-row.active,.mail-line.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {theme['border']};border-left-width:4px;line-height:1.7;color:#52647a}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.rate input{{width:100px}}.part{{white-space:normal}}}}
</style>
</head>
<body data-lang="{theme['lang']}">
<header><div class="brand"><a href="../index.html">← {html.escape(theme['brand'])}</a>　/　{html.escape(theme['card_title'])}</div></header>
<main>
<h1>{html.escape(theme['h1'])}</h1>
<p class="note">{html.escape(theme['intro'])}</p>
{toc_html()}
{intro_html(lang)}
{controls_html(accent)}
{example_block_html(lang, theme)}
{line_table_html(lang, theme)}
{tip_html(lang)}
</main>
<footer>{html.escape(theme['title'])}</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def card_html(lang):
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
    card = card_html(lang)
    for marker in ('href="./self-intro/"', 'href="./numbers/"', 'href="./vocab/"', 'href="./alphabet/"', 'href="./gojuon/"'):
        pos = text.find(marker)
        if pos != -1:
            end = text.find('</article>', pos)
            if end != -1:
                insert_at = end + len('</article>')
                text = text[:insert_at] + '\n' + card + text[insert_at:]
                path.write_text(text, encoding='utf-8')
                print('index', path)
                return
    raise SystemExit(f'cannot inject email into {path}')


def main():
    for lang in ('en', 'de', 'fr', 'ja'):
        folder = ROOT / lang / THEMES[lang]['slug']
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / 'index.html'
        path.write_text(page_for(lang), encoding='utf-8')
        print(path)
        inject_index(lang)


if __name__ == '__main__':
    main()
