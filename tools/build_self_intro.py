"""Build self-introduction phrase pages for en, de, fr, and ja."""
import html
from pathlib import Path

from self_intro_data import LINES, SECTIONS

ROOT = Path(__file__).parent.parent

THEMES = {
    'en': {
        'brand': '英文筆記',
        'title': 'Self-Introduction｜英文自我介紹',
        'h1': '英文自我介紹',
        'intro': '簡易自我介紹句子。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#17355d',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'en-US',
        'slug': 'self-intro',
        'card_title': 'Self-Introduction',
        'card': '簡易自我介紹：姓名、年齡、出身、居住與工作、語言與興趣。可朗讀或全部循環播放。',
        'meta': '自我介紹 · 跟讀',
        'col': 1,
    },
    'de': {
        'brand': '德文筆記',
        'title': 'Vorstellung｜德文自我介紹',
        'h1': '德文自我介紹',
        'intro': '簡易自我介紹句子。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#1d6a4f',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'lang': 'de-DE',
        'slug': 'self-intro',
        'card_title': 'Vorstellung',
        'card': '簡易自我介紹：姓名、年齡、出身、居住與工作、語言與興趣。可朗讀或全部循環播放。',
        'meta': '自我介紹 · 跟讀',
        'col': 2,
    },
    'fr': {
        'brand': '法文筆記',
        'title': 'Présentation｜法文自我介紹',
        'h1': '法文自我介紹',
        'intro': '簡易自我介紹句子。點選可朗讀；也可用全部循環播放，並調整語速。',
        'accent': '#b3482f',
        'bg': '#f7f4f2',
        'border': '#eadfd6',
        'lang': 'fr-FR',
        'slug': 'self-intro',
        'card_title': 'Présentation',
        'card': '簡易自我介紹：姓名、年齡、出身、居住與工作、語言與興趣。可朗讀或全部循環播放。',
        'meta': '自我介紹 · 跟讀',
        'col': 3,
    },
    'ja': {
        'brand': '日文筆記',
        'title': '自己紹介｜日文自我介紹',
        'h1': '日文自我介紹',
        'intro': '簡易自我介紹句子。每一句附漢字、平假名、片假名與羅馬拼音。點選可朗讀；也可全部循環播放並調語速。',
        'accent': '#8d3a55',
        'bg': '#f7f3f5',
        'border': '#eadde2',
        'lang': 'ja-JP',
        'slug': 'self-intro',
        'card_title': '自己紹介',
        'card': '簡易自我介紹：姓名、年齡、出身、居住與工作、語言與興趣。附漢字、假名、羅馬拼音；可朗讀或循環播放。',
        'meta': '自我介紹 · 跟讀',
        'col': None,
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


def page_for(lang):
    theme = THEMES[lang]
    accent = theme['accent']
    parts = [controls_html(accent)]
    for title, rows in SECTIONS:
        body = []
        if lang == 'ja':
            for row in rows:
                zh, _en, _de, _fr, kanji, kana, roma = row
                kata = to_katakana(kana)
                body.append(
                    '<tr class="vocab-row">'
                    f'<td class="zh">{html.escape(zh)}</td>'
                    f'<td><button type="button" class="say" lang="ja" data-say="{html.escape(kanji)}" data-lang="ja-JP">'
                    f'<span class="kanji">{html.escape(kanji)}</span>'
                    f'<span class="kana"><span class="hira">{html.escape(kana)}</span>　'
                    f'<span class="kata">{html.escape(kata)}</span></span>'
                    f'<span class="roma">{html.escape(roma)}</span>'
                    f'</button></td></tr>'
                )
            head = '<thead><tr><th scope="col">中文</th><th scope="col">漢字 · 平假名 · 片假名 · 羅馬拼音</th></tr></thead>'
        else:
            col = theme['col']
            for row in rows:
                zh = row[0]
                word = row[col]
                body.append(
                    '<tr class="vocab-row">'
                    f'<td class="zh">{html.escape(zh)}</td>'
                    f'<td><button type="button" class="say" lang="{lang}" data-say="{html.escape(word)}" data-lang="{theme["lang"]}">'
                    f'<span class="word">{html.escape(word)}</span>'
                    f'</button></td></tr>'
                )
            label = {'en': '英文', 'de': '德文', 'fr': '法文'}[lang]
            head = f'<thead><tr><th scope="col">中文</th><th scope="col">{label}</th></tr></thead>'
        parts.append(
            f'<h2>{html.escape(title)}</h2>'
            f'<div class="tablewrap"><table>{head}<tbody>{"".join(body)}</tbody></table></div>'
        )

    tip = (
        '點選句子可單獨朗讀。「全部循環播放」會依頁面順序朗讀；勾選「播完從頭再播」會一直循環，直到按停止。語速可用滑桿調整。'
    )
    if lang == 'ja':
        tip += ' 每一句列出漢字、平假名、片假名與羅馬拼音。朗讀使用漢字句。'
    elif lang == 'fr':
        tip += ' 年齡用法文 avoir：J’ai 33 ans。'
    elif lang == 'de':
        tip += ' 年齡用 sein：Ich bin 33 Jahre alt。'
    else:
        tip += ' 年齡用 be：I am 33 years old。'

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
table{{border-collapse:collapse;width:100%;min-width:480px}}
th{{background:#f4f7fb;text-align:left;font-size:.9rem;padding:12px 14px}}
td{{padding:12px 14px;border-top:1px solid {theme['border']};vertical-align:top}}
.zh{{color:#53647c;width:34%;line-height:1.55}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 0;border-radius:8px}}
.say:hover,.say:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.word,.kanji{{font-size:1.08rem;font-weight:750;color:{accent};line-height:1.45}}
.kana{{font-size:.95rem;color:#3d4d63}}
.kata{{color:#6a5870}}
.roma{{font-size:.85rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {theme['border']};border-left-width:4px;line-height:1.7;color:#52647a}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.rate input{{width:100px}}.zh{{width:40%}}}}
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
    for marker in ('href="./numbers/"', 'href="./vocab/"', 'href="./alphabet/"', 'href="./gojuon/"'):
        pos = text.find(marker)
        if pos != -1:
            end = text.find('</article>', pos)
            if end != -1:
                insert_at = end + len('</article>')
                text = text[:insert_at] + '\n' + card + text[insert_at:]
                path.write_text(text, encoding='utf-8')
                print('index', path)
                return
    raise SystemExit(f'cannot inject self-intro into {path}')


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
