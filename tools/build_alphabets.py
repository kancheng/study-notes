"""Build alphabet / gojuon reference pages for en, de, fr, and ja."""
import html
from pathlib import Path

ROOT = Path(__file__).parent.parent

SPEECH = """
function speak(text, lang) {
  if (!('speechSynthesis' in window)) { alert('此瀏覽器不支援語音播放。'); return; }
  let started = false;
  const run = () => {
    if (started) return;
    started = true;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = lang;
    u.rate = 0.85;
    const prefix = lang.toLowerCase().replace('_','-').slice(0, 2);
    const voice = speechSynthesis.getVoices().find(v => v.lang.toLowerCase().replace('_','-').startsWith(prefix));
    if (voice) u.voice = voice;
    speechSynthesis.speak(u);
  };
  if (speechSynthesis.getVoices().length) run();
  else {
    speechSynthesis.addEventListener('voiceschanged', run, { once: true });
    setTimeout(run, 300);
  }
}
if ('speechSynthesis' in window) speechSynthesis.getVoices();
document.addEventListener('click', e => {
  const b = e.target.closest('[data-say]');
  if (b) speak(b.dataset.say, b.dataset.lang || 'en-US');
});
"""


def page_shell(lang_home, brand, title, h1, intro, accent, bg, border, body, speech_lang):
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
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:12px}}
.tile{{background:white;border:1px solid {border};border-radius:14px;padding:14px 10px;text-align:center;box-shadow:0 6px 18px #142f520c;cursor:pointer}}
.tile:hover,.tile:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.glyph{{font-size:1.85rem;font-weight:800;color:{accent};line-height:1.2}}
.pair{{font-size:1.05rem;color:#3d4d63;margin-top:4px}}
.roma,.name{{font-size:.88rem;color:#6a5870;margin-top:4px}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {border};border-left-width:4px}}
.kana-wrap{{overflow-x:auto;margin:12px 0 8px}}
.kana{{border-collapse:collapse;width:100%;min-width:640px;background:white;border:1px solid {border};border-radius:12px;overflow:hidden}}
.kana th,.kana td{{border:1px solid {border};padding:10px 8px;text-align:center;vertical-align:middle}}
.kana th{{background:#f8eef2;font-size:.9rem;color:#5c3a46}}
.kana td.rowhead{{background:#f8eef2;font-weight:750;white-space:nowrap}}
.kana .empty{{background:#faf7f8;color:#b7a8ae}}
.cell{{cursor:pointer;border-radius:8px}}
.cell:hover,.cell:focus-visible{{outline:2px solid {accent};outline-offset:-2px}}
.cell .hira{{font-size:1.45rem;font-weight:800;color:{accent};line-height:1.15}}
.cell .kata{{font-size:1.05rem;color:#3d4d63;margin-top:2px}}
.cell .roma{{font-size:.82rem;color:#6a5870;margin-top:2px}}
.accent-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:12px}}
footer{{max-width:1050px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:600px){{main{{padding-top:25px}}.glyph{{font-size:1.55rem}}}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← {html.escape(brand)}</a>　/　{html.escape(title.split('｜')[0])}</div></header>
<main>
<h1>{html.escape(h1)}</h1>
<p class="note">{html.escape(intro)}</p>
{body}
<div class="tip"><strong>用法提醒：</strong>點選字母或假名可朗讀。發音品質依裝置內安裝的語音而異。</div>
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


def write_en():
    letters = [
        ('A', 'a', 'ei'), ('B', 'b', 'bi'), ('C', 'c', 'si'), ('D', 'd', 'di'),
        ('E', 'e', 'i'), ('F', 'f', 'ef'), ('G', 'g', 'ji'), ('H', 'h', 'eich'),
        ('I', 'i', 'ai'), ('J', 'j', 'jei'), ('K', 'k', 'kei'), ('L', 'l', 'el'),
        ('M', 'm', 'em'), ('N', 'n', 'en'), ('O', 'o', 'ou'), ('P', 'p', 'pi'),
        ('Q', 'q', 'kiu'), ('R', 'r', 'ar'), ('S', 's', 'es'), ('T', 't', 'ti'),
        ('U', 'u', 'yu'), ('V', 'v', 'vi'), ('W', 'w', 'dabl yu'), ('X', 'x', 'eks'),
        ('Y', 'y', 'wai'), ('Z', 'z', 'zi / zed'),
    ]
    tiles = ''.join(latin_tile(u, l, n, u, 'en-US') for u, l, n in letters)
    body = f'''
<h2>26 個字母</h2>
<p class="note">大寫與小寫成對列出。名稱用常見的美式讀法；Z 在英式常讀作 zed。</p>
<div class="grid">{tiles}</div>
<div class="tip"><strong>補充：</strong>英文沒有獨立的變音字母。a / an 看的是後面的發音，不是字母本身：an hour、a university。</div>
'''
    page = page_shell(
        'en', '英文筆記', 'Alphabet｜英文字母', '英文字母表',
        '英文字母共 26 個。點選可聽字母名稱；下面標的是常見的美式讀法。',
        '#17355d', '#f2f5fa', '#dce4ef', body, 'en-US',
    )
    out = ROOT / 'en' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    print(out / 'index.html')


def write_de():
    letters = [
        ('A', 'a', 'ah'), ('B', 'b', 'be'), ('C', 'c', 'tse'), ('D', 'd', 'de'),
        ('E', 'e', 'eh'), ('F', 'f', 'ef'), ('G', 'g', 'ge'), ('H', 'h', 'ha'),
        ('I', 'i', 'i'), ('J', 'j', 'jot'), ('K', 'k', 'ka'), ('L', 'l', 'el'),
        ('M', 'm', 'em'), ('N', 'n', 'en'), ('O', 'o', 'oh'), ('P', 'p', 'pe'),
        ('Q', 'q', 'ku'), ('R', 'r', 'er'), ('S', 's', 'es'), ('T', 't', 'te'),
        ('U', 'u', 'u'), ('V', 'v', 'fau'), ('W', 'w', 've'), ('X', 'x', 'iks'),
        ('Y', 'y', 'üpsilon'), ('Z', 'z', 'tsett'),
    ]
    special = [
        ('Ä', 'ä', 'a-umlaut'), ('Ö', 'ö', 'o-umlaut'), ('Ü', 'ü', 'u-umlaut'),
        ('ẞ', 'ß', 'Eszett / scharfes S'),
    ]
    tiles = ''.join(latin_tile(u, l, n, u, 'de-DE') for u, l, n in letters)
    extra = ''.join(latin_tile(u, l, n, u if u != 'ẞ' else 'ß', 'de-DE') for u, l, n in special)
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
        'de', '德文筆記', 'Alphabet｜德文字母', '德文字母表',
        '德文使用拉丁字母，另有 Ä、Ö、Ü 與 ß。點選可聽字母名稱。',
        '#1d6a4f', '#f2f5fa', '#dce4ef', body, 'de-DE',
    )
    out = ROOT / 'de' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    print(out / 'index.html')


def write_fr():
    letters = [
        ('A', 'a', 'a'), ('B', 'b', 'bé'), ('C', 'c', 'cé'), ('D', 'd', 'dé'),
        ('E', 'e', 'e'), ('F', 'f', 'effe'), ('G', 'g', 'gé'), ('H', 'h', 'ache'),
        ('I', 'i', 'i'), ('J', 'j', 'ji'), ('K', 'k', 'ka'), ('L', 'l', 'elle'),
        ('M', 'm', 'emme'), ('N', 'n', 'enne'), ('O', 'o', 'o'), ('P', 'p', 'pé'),
        ('Q', 'q', 'ku'), ('R', 'r', 'erre'), ('S', 's', 'esse'), ('T', 't', 'té'),
        ('U', 'u', 'u'), ('V', 'v', 'vé'), ('W', 'w', 'double vé'), ('X', 'x', 'iks'),
        ('Y', 'y', 'i grec'), ('Z', 'z', 'zède'),
    ]
    accents = [
        ('É', 'é', 'e aigu'), ('È', 'è', 'e grave'), ('Ê', 'ê', 'e circonflexe'), ('Ë', 'ë', 'e tréma'),
        ('À', 'à', 'a grave'), ('Â', 'â', 'a circonflexe'),
        ('Ù', 'ù', 'u grave'), ('Û', 'û', 'u circonflexe'), ('Ü', 'ü', 'u tréma'),
        ('Ô', 'ô', 'o circonflexe'), ('Î', 'î', 'i circonflexe'), ('Ï', 'ï', 'i tréma'),
        ('Ç', 'ç', 'c cédille'), ('Œ', 'œ', 'e dans l’o'), ('Æ', 'æ', 'e dans l’a'),
    ]
    tiles = ''.join(latin_tile(u, l, n, u, 'fr-FR') for u, l, n in letters)
    extra = ''.join(latin_tile(u, l, n, l, 'fr-FR') for u, l, n in accents)
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
        'fr', '法文筆記', 'Alphabet｜法文字母', '法文字母表',
        '法文使用拉丁字母，並常搭配重音與合字。點選可聽字母或符號名稱。',
        '#b3482f', '#f7f4f2', '#eadfd6', body, 'fr-FR',
    )
    out = ROOT / 'fr' / 'alphabet'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
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
    # (hira, kata, roma) — Hepburn, matching site convention
    seion = [
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
    dakuon = [
        ('が行', [('が', 'ガ', 'ga'), ('ぎ', 'ギ', 'gi'), ('ぐ', 'グ', 'gu'), ('げ', 'ゲ', 'ge'), ('ご', 'ゴ', 'go')]),
        ('ざ行', [('ざ', 'ザ', 'za'), ('じ', 'ジ', 'ji'), ('ず', 'ズ', 'zu'), ('ぜ', 'ゼ', 'ze'), ('ぞ', 'ゾ', 'zo')]),
        ('だ行', [('だ', 'ダ', 'da'), ('ぢ', 'ヂ', 'ji'), ('づ', 'ヅ', 'zu'), ('で', 'デ', 'de'), ('ど', 'ド', 'do')]),
        ('ば行', [('ば', 'バ', 'ba'), ('び', 'ビ', 'bi'), ('ぶ', 'ブ', 'bu'), ('べ', 'ベ', 'be'), ('ぼ', 'ボ', 'bo')]),
    ]
    handaku = [
        ('ぱ行', [('ぱ', 'パ', 'pa'), ('ぴ', 'ピ', 'pi'), ('ぷ', 'プ', 'pu'), ('ぺ', 'ペ', 'pe'), ('ぽ', 'ポ', 'po')]),
    ]
    youon = [
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
    vowels = ['a', 'i', 'u', 'e', 'o']
    youon_headers = ['ya', 'yu', 'yo']

    body = f'''
<h2>清音（五十音）</h2>
<p class="note">每一格由上到下是平假名、片假名、平文式羅馬拼音。を的羅馬拼音寫成 o；助詞を也讀 o。</p>
{kana_table(vowels, seion)}
<h2>濁音</h2>
<p class="note">在清音右上加濁點「゛」。ぢ、づ現在多半寫成 じ、ず；羅馬拼音同樣寫成 ji、zu。</p>
{kana_table(vowels, dakuon)}
<h2>半濁音</h2>
<p class="note">在は行右上加半濁點「゜」，讀成 p 音。</p>
{kana_table(vowels, handaku)}
<h2>拗音</h2>
<p class="note">い段假名加小寫ゃ／ゅ／ょ。片假名同理。羅馬拼音寫成 kya、sha、cha 等。</p>
{kana_table(youon_headers, youon)}
<div class="tip"><strong>補充：</strong>促音「っ／ッ」讓後面子音拉長：きって = kitte。長音在平假名常寫成あ行母音，片假名多用「ー」。羅馬拼音長音照假名寫成 ou、oo、ei、ii、uu；片假名長音符號寫成雙母音。</div>
'''
    page = page_shell(
        'ja', '日文筆記', '五十音｜平假名・片假名', '日文五十音',
        '平假名、片假名對照，含清音、濁音、半濁音與拗音，並標平文式羅馬拼音。點選假名可朗讀。',
        '#8d3a55', '#f7f3f5', '#eadde2', body, 'ja-JP',
    )
    # Fix tip background for Japanese rose theme in kana headers - already set
    out = ROOT / 'ja' / 'gojuon'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    print(out / 'index.html')


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
        # Replace existing alphabet block if present, else skip duplicate
        return
    card = alphabet_card_html(lang)
    # Insert after the intro paragraphs, before first <h2>
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
