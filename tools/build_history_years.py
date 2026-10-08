"""History-year speaking pages: en, fr, de, ja, and a four-language table.

Each page ends with a loopable list of years from 10 CE through 2040.
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_numbers as num

ROOT = Path(__file__).resolve().parent.parent

THEMES = {
    'en': {
        'brand': '英文筆記',
        'title': 'Years｜歷史年份',
        'h1': '英文歷史年份',
        'card_title': 'Years',
        'lang_attr': '',
        'accent': '#17355d',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'speech': 'en-US',
        'html_lang': 'en',
    },
    'fr': {
        'brand': '法文筆記',
        'title': 'Années｜歷史年份',
        'h1': '法文歷史年份',
        'card_title': 'Années',
        'lang_attr': ' lang="fr"',
        'accent': '#b3482f',
        'bg': '#f7f4f2',
        'border': '#eadfd6',
        'speech': 'fr-FR',
        'html_lang': 'fr',
    },
    'de': {
        'brand': '德文筆記',
        'title': 'Jahreszahlen｜歷史年份',
        'h1': '德文歷史年份',
        'card_title': 'Jahreszahlen',
        'lang_attr': ' lang="de"',
        'accent': '#1d6a4f',
        'bg': '#f2f5fa',
        'border': '#dce4ef',
        'speech': 'de-DE',
        'html_lang': 'de',
    },
    'ja': {
        'brand': '日文筆記',
        'title': '西暦｜歷史年份',
        'h1': '日文歷史年份',
        'card_title': '西暦',
        'lang_attr': ' lang="ja"',
        'accent': '#8d3a55',
        'bg': '#f7f3f5',
        'border': '#eadde2',
        'speech': 'ja-JP',
        'html_lang': 'ja',
    },
}

CARD = '歷史事件的年份念法與完整句子。頁尾可從西元 10 年循環朗讀到 2040 年。'


def en_year(n):
    """Spoken English year, not the cardinal used on the numbers page."""
    if n < 100:
        return num.en_under_100(n)
    if n < 1000:
        hundreds, rest = divmod(n, 100)
        head = num._EN_ONES[hundreds]
        if rest == 0:
            return f'{head} hundred'
        if rest < 10:
            return f'{head} oh {num._EN_ONES[rest]}'
        return f'{head} {num.en_under_100(rest)}'
    if n < 2000:
        hi, lo = divmod(n, 100)
        if lo == 0:
            if hi == 10:
                return 'one thousand'
            return f'{num.en_under_100(hi)} hundred'
        if lo < 10:
            return f'{num.en_under_100(hi)} oh {num._EN_ONES[lo]}'
        return f'{num.en_under_100(hi)} {num.en_under_100(lo)}'
    if n == 2000:
        return 'two thousand'
    if n < 2010:
        return f'two thousand {num.en_under_100(n - 2000)}'
    return f'twenty {num.en_under_100(n - 2000)}'


def de_year(n):
    """1100–1999 use Xhundert; 1000–1099 and 2000+ use tausend."""
    if n < 1000:
        return num.de_word(n)
    if n < 1100:
        rest = n - 1000
        if rest == 0:
            return 'tausend'
        return 'tausend' + num.de_under_100(rest, final=True)
    if n < 2000:
        hi, lo = divmod(n, 100)
        head = num.de_under_100(hi, final=True) + 'hundert'
        if lo == 0:
            return head
        return head + num.de_under_100(lo, final=True)
    rest = n - 2000
    if rest == 0:
        return 'zweitausend'
    return 'zweitausend' + num.de_under_100(rest, final=True)


def fr_year(n):
    return num.fr_word(n)


def ja_year_parts(n):
    kanji, hira, kata, roma, _say = num.ja_word(n)
    return {
        'kanji': kanji + '年',
        'hira': hira + 'ねん',
        'kata': num.to_katakana(hira + 'ねん'),
        'roma': roma + 'nen',
    }


def year_forms(n, bce=False):
    en = en_year(n)
    fr = fr_year(n)
    de = de_year(n)
    ja = ja_year_parts(n)
    if bce:
        en = f'{en} B C E'
        fr = f'{fr} avant notre ère'
        de = f'{de} vor Christus'
        ja = {
            'kanji': '紀元前' + ja['kanji'],
            'hira': 'きげんぜん' + ja['hira'],
            'kata': 'キゲンゼン' + ja['kata'],
            'roma': 'kigenzen' + ja['roma'],
        }
    return {'en': en, 'fr': fr, 'de': de, 'ja': ja}


# Predicates stay fixed; {en} {fr} {de} {ja_k} {ja_h} are filled from year_forms.
EVENTS = [
    (-202, True, '西漢建立', '劉邦建立漢朝',
     'The Western Han was founded in {en}.',
     'Les Han occidentaux ont été fondés en {fr}.',
     'Die Westliche Han-Dynastie wurde im Jahr {de} gegründet.',
     '{ja_k}に前漢が成立しました。',
     '{ja_h} に ぜんかん が せいりつしました。'),
    (-27, True, '羅馬帝國建立', '屋大維成為奧古斯都',
     'The Roman Empire was established in {en}.',
     "L'Empire romain a été fondé en {fr}.",
     'Das Römische Reich wurde im Jahr {de} gegründet.',
     '{ja_k}にローマ帝国が成立しました。',
     '{ja_h} に ローマていこく が せいりつしました。'),
    (25, False, '東漢建立', '劉秀稱帝',
     'The Eastern Han was founded in {en}.',
     'Les Han orientaux ont été fondés en {fr}.',
     'Die Östliche Han-Dynastie wurde im Jahr {de} gegründet.',
     '{ja_k}に後漢が成立しました。',
     '{ja_h} に ごかん が せいりつしました。'),
    (220, False, '三國時代開始', '曹魏建立',
     'The Three Kingdoms period began in {en}.',
     'La période des Trois Royaumes a commencé en {fr}.',
     'Die Zeit der Drei Reiche begann im Jahr {de}.',
     '{ja_k}に三国時代が始まりました。',
     '{ja_h} に さんごくじだい が はじまりました。'),
    (395, False, '羅馬帝國東西分治', '東西兩部分由不同皇帝統治',
     'The Roman Empire was divided into east and west in {en}.',
     "L'Empire romain a été divisé en Orient et en Occident en {fr}.",
     'Das Römische Reich wurde im Jahr {de} in Ost und West geteilt.',
     '{ja_k}にローマ帝国が東西に分かれました。',
     '{ja_h} に ローマていこく が とうざい に わかれました。'),
    (476, False, '西羅馬帝國滅亡', '東羅馬仍存續',
     'The Western Roman Empire fell in {en}.',
     "L'Empire romain d'Occident est tombé en {fr}.",
     'Das Weströmische Reich ging im Jahr {de} unter.',
     '{ja_k}に西ローマ帝国が滅亡しました。',
     '{ja_h} に にしローマていこく が めつぼうしました。'),
    (1066, False, '諾曼征服英格蘭', '諾曼第公爵威廉成為英格蘭國王',
     'The Normans conquered England in {en}.',
     "Les Normands ont conquis l'Angleterre en {fr}.",
     'Die Normannen eroberten England im Jahr {de}.',
     '{ja_k}にノルマン人がイングランドを征服しました。',
     '{ja_h} に ノルマンじん が イングランド を せいふくしました。'),
    (1219, False, '蒙古第一次西征開始', '成吉思汗進攻花剌子模',
     'The first Mongol campaign to the west began in {en}.',
     "La première campagne mongole vers l'ouest a commencé en {fr}.",
     'Der erste Mongolenfeldzug nach Westen begann im Jahr {de}.',
     '{ja_k}にモンゴルの第一次西征が始まりました。',
     '{ja_h} に モンゴル の だいいちじせいせい が はじまりました。'),
    (1624, False, '荷蘭開始統治臺灣南部', '荷蘭東印度公司',
     'The Dutch began to rule southern Taiwan in {en}.',
     'Les Néerlandais ont commencé à gouverner le sud de Taïwan en {fr}.',
     'Die Niederländer begannen im Jahr {de}, Südtaiwan zu regieren.',
     '{ja_k}にオランダが台湾南部の統治を始めました。',
     '{ja_h} に オランダ が たいわんなんぶ の とうち を はじめました。'),
    (1626, False, '西班牙開始佔領臺灣北部', '基隆、淡水一帶',
     'The Spanish began to occupy northern Taiwan in {en}.',
     'Les Espagnols ont commencé à occuper le nord de Taïwan en {fr}.',
     'Die Spanier begannen im Jahr {de}, Nordtaiwan zu besetzen.',
     '{ja_k}にスペインが台湾北部の占領を始めました。',
     '{ja_h} に スペイン が たいわんほくぶ の せんりょう を はじめました。'),
    (1642, False, '西班牙勢力退出臺灣', '荷蘭攻取雞籠',
     'The Spanish left Taiwan in {en}.',
     'Les Espagnols ont quitté Taïwan en {fr}.',
     'Die Spanier verließen Taiwan im Jahr {de}.',
     '{ja_k}にスペインが台湾から撤退しました。',
     '{ja_h} に スペイン が たいわん から てったいしました。'),
    (1662, False, '鄭成功取得臺灣統治權', '鄭氏政權',
     'Koxinga took control of Taiwan in {en}.',
     'Koxinga a pris le contrôle de Taïwan en {fr}.',
     'Koxinga übernahm im Jahr {de} die Herrschaft über Taiwan.',
     '{ja_k}に鄭成功が台湾の統治権を得ました。',
     '{ja_h} に ていせいこう が たいわん の とうちけん を えました。'),
    (1683, False, '清朝取得臺灣統治權', '清軍擊敗鄭氏政權',
     'The Qing took control of Taiwan in {en}.',
     'Les Qing ont pris le contrôle de Taïwan en {fr}.',
     'Die Qing übernahmen im Jahr {de} die Herrschaft über Taiwan.',
     '{ja_k}に清朝が台湾の統治権を得ました。',
     '{ja_h} に しんちょう が たいわん の とうちけん を えました。'),
    (1775, False, '美國獨立戰爭開始', '1775–1783',
     'The American Revolutionary War began in {en}.',
     "La guerre d'indépendance américaine a commencé en {fr}.",
     'Der Amerikanische Unabhängigkeitskrieg begann im Jahr {de}.',
     '{ja_k}にアメリカ独立戦争が始まりました。',
     '{ja_h} に アメリカどくりつせんそう が はじまりました。'),
    (1776, False, '美國宣布獨立', '7 月 4 日',
     'The United States declared independence in {en}.',
     'Les États-Unis ont déclaré leur indépendance en {fr}.',
     'Die Vereinigten Staaten erklärten im Jahr {de} ihre Unabhängigkeit.',
     '{ja_k}にアメリカが独立を宣言しました。',
     '{ja_h} に アメリカ が どくりつ を せんげんしました。'),
    (1789, False, '法國大革命開始', '攻佔巴士底監獄',
     'The French Revolution began in {en}.',
     'La Révolution française a commencé en {fr}.',
     'Die Französische Revolution begann im Jahr {de}.',
     '{ja_k}にフランス革命が始まりました。',
     '{ja_h} に フランスかくめい が はじまりました。'),
    (1830, False, '比利時革命與宣布獨立', '1831 年確立君主制',
     'The Belgian Revolution began in {en}.',
     'La révolution belge a commencé en {fr}.',
     'Die Belgische Revolution begann im Jahr {de}.',
     '{ja_k}にベルギー革命が始まりました。',
     '{ja_h} に ベルギーかくめい が はじまりました。'),
    (1853, False, '黑船來航', '培里艦隊抵達日本',
     'Commodore Perry arrived in Japan in {en}.',
     'Le commodore Perry est arrivé au Japon en {fr}.',
     'Kommodore Perry kam im Jahr {de} nach Japan.',
     '{ja_k}に黒船が来航しました。',
     '{ja_h} に くろふね が らいこうしました。'),
    (1868, False, '明治維新開始', '日本近代化改革',
     'The Meiji Restoration began in {en}.',
     'La restauration de Meiji a commencé en {fr}.',
     'Die Meiji-Restauration begann im Jahr {de}.',
     '{ja_k}に明治維新が始まりました。',
     '{ja_h} に めいじいしん が はじまりました。'),
    (1871, False, '德意志帝國建立', '德國統一',
     'The German Empire was founded in {en}.',
     "L'Empire allemand a été fondé en {fr}.",
     'Das Deutsche Kaiserreich wurde im Jahr {de} gegründet.',
     '{ja_k}にドイツ帝国が成立しました。',
     '{ja_h} に ドイツていこく が せいりつしました。'),
    (1894, False, '甲午戰爭開始', '1894–1895',
     'The First Sino-Japanese War began in {en}.',
     'La première guerre sino-japonaise a commencé en {fr}.',
     'Der Erste Chinesisch-Japanische Krieg begann im Jahr {de}.',
     '{ja_k}に日清戦争が始まりました。',
     '{ja_h} に にっしんせんそう が はじまりました。'),
    (1895, False, '日本開始統治臺灣', '《馬關條約》',
     'Japan began to rule Taiwan in {en}.',
     'Le Japon a commencé à gouverner Taïwan en {fr}.',
     'Japan begann im Jahr {de}, Taiwan zu regieren.',
     '{ja_k}に日本が台湾の統治を始めました。',
     '{ja_h} に にほん が たいわん の とうち を はじめました。'),
    (1904, False, '日俄戰爭開始', '1904–1905',
     'The Russo-Japanese War began in {en}.',
     'La guerre russo-japonaise a commencé en {fr}.',
     'Der Russisch-Japanische Krieg begann im Jahr {de}.',
     '{ja_k}に日露戦争が始まりました。',
     '{ja_h} に にちろせんそう が はじまりました。'),
    (1911, False, '辛亥革命', '中華民國於 1912 年成立',
     'The Xinhai Revolution began in {en}.',
     'La révolution Xinhai a commencé en {fr}.',
     'Die Xinhai-Revolution begann im Jahr {de}.',
     '{ja_k}に辛亥革命が始まりました。',
     '{ja_h} に しんがいかくめい が はじまりました。'),
    (1912, False, '中華民國成立', '1 月 1 日',
     'The Republic of China was founded in {en}.',
     'La République de Chine a été fondée en {fr}.',
     'Die Republik China wurde im Jahr {de} gegründet.',
     '{ja_k}に中華民国が成立しました。',
     '{ja_h} に ちゅうかみんこく が せいりつしました。'),
    (1914, False, '第一次世界大戰開始', '7 月 28 日',
     'The First World War began in {en}.',
     'La Première Guerre mondiale a commencé en {fr}.',
     'Der Erste Weltkrieg begann im Jahr {de}.',
     '{ja_k}に第一次世界大戦が始まりました。',
     '{ja_h} に だいいちじせかいたいせん が はじまりました。'),
    (1918, False, '第一次世界大戰停戰', '11 月 11 日',
     'The First World War armistice was signed in {en}.',
     "L'armistice de la Première Guerre mondiale a été signé en {fr}.",
     'Der Waffenstillstand des Ersten Weltkriegs wurde im Jahr {de} geschlossen.',
     '{ja_k}に第一次世界大戦が休戦しました。',
     '{ja_h} に だいいちじせかいたいせん が きゅうせんしました。'),
    (1939, False, '第二次世界大戰在歐洲爆發', '9 月 1 日',
     'The Second World War began in Europe in {en}.',
     'La Seconde Guerre mondiale a commencé en Europe en {fr}.',
     'Der Zweite Weltkrieg begann im Jahr {de} in Europa.',
     '{ja_k}に第二次世界大戦がヨーロッパで始まりました。',
     '{ja_h} に だいにじせかいたいせん が ヨーロッパ で はじまりました。'),
    (1945, False, '第二次世界大戰結束', '9 月 2 日日本正式簽署投降書',
     'The Second World War ended in {en}.',
     "La Seconde Guerre mondiale s'est terminée en {fr}.",
     'Der Zweite Weltkrieg endete im Jahr {de}.',
     '{ja_k}に第二次世界大戦が終わりました。',
     '{ja_h} に だいにじせかいたいせん が おわりました。'),
    (1945, False, '中華民國開始接收並治理臺灣', '10 月 25 日。與 1949 年政府遷臺不同',
     'The Republic of China began to administer Taiwan in {en}.',
     'La République de Chine a commencé à administrer Taïwan en {fr}.',
     'Die Republik China begann im Jahr {de}, Taiwan zu verwalten.',
     '{ja_k}に中華民国が台湾の接収を始めました。',
     '{ja_h} に ちゅうかみんこく が たいわん の せっしゅう を はじめました。'),
    (1949, False, '中華民國政府遷臺', '與 1945 年接收不同',
     'The government of the Republic of China moved to Taiwan in {en}.',
     "Le gouvernement de la République de Chine s'est installé à Taïwan en {fr}.",
     'Die Regierung der Republik China zog im Jahr {de} nach Taiwan.',
     '{ja_k}に中華民国政府が台湾へ移りました。',
     '{ja_h} に ちゅうかみんこくせいふ が たいわん へ うつりました。'),
    (1993, False, '歐洲聯盟成立', '《馬斯垂克條約》生效',
     'The European Union was established in {en}.',
     "L'Union européenne a été créée en {fr}.",
     'Die Europäische Union wurde im Jahr {de} gegründet.',
     '{ja_k}に欧州連合が発足しました。',
     '{ja_h} に おうしゅうれんごう が ほっそくしました。'),
]

NOTES = [
    (1453, False, '東羅馬帝國滅亡', '不要把 476 年西羅馬滅亡記成整個羅馬帝國的結束',
     'The Eastern Roman Empire fell in {en}.',
     "L'Empire romain d'Orient est tombé en {fr}.",
     'Das Oströmische Reich ging im Jahr {de} unter.',
     '{ja_k}に東ローマ帝国が滅亡しました。',
     '{ja_h} に ひがしローマていこく が めつぼうしました。'),
    (1957, False, '歐洲經濟共同體條約簽署', '歐盟的前身。條約於 1957 年簽署',
     'The Treaty of Rome was signed in {en}.',
     'Le traité de Rome a été signé en {fr}.',
     'Der Vertrag von Rom wurde im Jahr {de} unterzeichnet.',
     '{ja_k}にローマ条約が調印されました。',
     '{ja_h} に ローマじょうやく が ちょういんされました。'),
    (1958, False, '歐洲經濟共同體生效', '1957 年簽署，1958 年生效。歐盟本身是 1993 年',
     'The European Economic Community began in {en}.',
     'La Communauté économique européenne a commencé en {fr}.',
     'Die Europäische Wirtschaftsgemeinschaft begann im Jahr {de}.',
     '{ja_k}に欧州経済共同体が発足しました。',
     '{ja_h} に おうしゅうけいざいきょうどうたい が ほっそくしました。'),
]


def fill(event):
    year, bce, zh, note, en_t, fr_t, de_t, ja_t, ja_say_t = event
    forms = year_forms(abs(year), bce)
    ja = forms['ja']
    data = {
        'en': forms['en'],
        'fr': forms['fr'],
        'de': forms['de'],
        'ja_k': ja['kanji'],
        'ja_h': ja['hira'],
    }
    return {
        'year': abs(year),
        'bce': bce,
        'label': f'前 {abs(year)} 年' if bce else f'{abs(year)} 年',
        'zh': zh,
        'note': note,
        'en': en_t.format(**data),
        'fr': fr_t.format(**data),
        'de': de_t.format(**data),
        'ja': ja_t.format(**data),
        'ja_say': ja_say_t.format(**data),
        'forms': forms,
    }


def esc(text):
    return html.escape(text, quote=True)


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
  if ('speechSynthesis' in window) speechSynthesis.cancel();
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
    row.scrollIntoView({ block: 'nearest', behavior: 'auto' });
  }
  setStatus('播放中：' + item.text + '（' + (index + 1) + ' / ' + queue.length + '）');
  const rate = parseFloat(rateInput.value) || 0.9;
  speakOnce(item.text, item.lang, rate, () => {
    if (!playing) return;
    index += 1;
    setTimeout(playNext, 180);
  });
}

function itemsIn(selector) {
  return [...document.querySelectorAll(selector)].map(el => ({
    text: el.dataset.say,
    lang: el.dataset.lang,
    el,
  }));
}

function startQueue(items) {
  if (!items.length) return;
  voicesReady(() => {
    playing = true;
    queue = items;
    index = 0;
    playNext();
  });
}

rateInput.addEventListener('input', () => {
  rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);
});
rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);

document.getElementById('play-events').addEventListener('click', () => {
  startQueue(itemsIn('#events [data-say], #notes [data-say]'));
});
document.getElementById('play-years').addEventListener('click', () => {
  startQueue(itemsIn('#years [data-say]'));
});
document.getElementById('play-before').addEventListener('click', () => {
  startQueue(itemsIn('#years [data-say]').filter(item => Number(item.el.dataset.year) < 1800));
});
document.getElementById('play-after').addEventListener('click', () => {
  startQueue(itemsIn('#years [data-say]').filter(item => Number(item.el.dataset.year) >= 1800));
});
document.getElementById('stop-all').addEventListener('click', stopAll);

document.addEventListener('click', e => {
  const b = e.target.closest('[data-say]');
  if (!b || e.target.closest('.controls')) return;
  const rate = parseFloat(rateInput.value) || 0.9;
  voicesReady(() => {
    playing = false;
    queue = [];
    if ('speechSynthesis' in window) speechSynthesis.cancel();
    clearActive();
    const row = b.closest('.vocab-row');
    if (row) row.classList.add('active');
    setStatus('單句：' + b.dataset.say);
    speakOnce(b.dataset.say, b.dataset.lang, rate, () => {
      clearActive();
      setStatus('待命');
    });
  });
});

if ('speechSynthesis' in window) speechSynthesis.getVoices();
'''


def controls_html():
    return '''
<div class="controls">
  <div class="controls-row">
    <button type="button" id="play-events" class="ctrl">▶ 播放歷史句子</button>
    <button type="button" id="play-years" class="ctrl">▶ 循環播放 10–2040</button>
    <button type="button" id="play-before" class="ctrl">10–1799</button>
    <button type="button" id="play-after" class="ctrl">1800–2040</button>
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


def say_button(text, speech_lang, css, say=None, year=None):
    spoken = say if say is not None else text
    year_attr = f' data-year="{year}"' if year is not None else ''
    return (
        f'<button type="button" class="say {css}" lang="{css}" data-say="{esc(spoken)}" '
        f'data-lang="{speech_lang}"{year_attr}><span class="word">{esc(text)}</span></button>'
    )


def ja_button(kanji, hira, kata, roma, say, css='ja', year=None):
    year_attr = f' data-year="{year}"' if year is not None else ''
    return (
        f'<button type="button" class="say {css}" lang="ja" data-say="{esc(say)}" '
        f'data-lang="ja-JP"{year_attr}>'
        f'<span class="word">{esc(kanji)}</span>'
        f'<span class="sub"><span class="hira">{esc(hira)}</span>　<span class="kata">{esc(kata)}</span></span>'
        f'<span class="roma">{esc(roma)}</span></button>'
    )


RULES = {
    'en': (
        '四位數年份拆成前後兩段：1911 唸 nineteen eleven。十位是 0 時用 oh，1904 唸 nineteen oh four。'
        '1000 唸 one thousand。2000 唸 two thousand；2001–2009 唸 two thousand one；2010 起唸 twenty ten。'
        '三位數拆成「百位＋後面」：476 唸 four seventy-six。在某一年用 in。'
    ),
    'fr': (
        '年份用完整基數：1911 唸 mille neuf cent onze。71 要加 et：1871 是 soixante et onze。'
        '80 在最後是 quatre-vingts；後面還有數字就不再加 s。整百複數加 s（deux cents），後面有數時不加。'
        '在某一年用 en，不隨年份變化。'
    ),
    'de': (
        '1100–1999 用「幾個百」：1911 唸 neunzehnhundertelf。1000–1099 用 tausend：1066 唸 tausendsechsundsechzig。'
        '2000 起用 zweitausend。個位在十位前面：45 是 fünfundvierzig。在某一年用 im Jahr。'
    ),
    'ja': (
        '年份是基數再加年。1911 是 せんきゅうひゃくじゅういちねん。'
        '三百＝さんびゃく、六百＝ろっぴゃく、八百＝はっぴゃく。1904 是 せんきゅうひゃくよんねん，中間沒有じゅう。'
        '四讀よん、七讀なな，和數字表相同。在某一年用「年に」。'
    ),
}


def rules_block(lang):
    sample = year_forms(1911)
    if lang == 'ja':
        ja = sample['ja']
        body = ja_button(ja['kanji'], ja['hira'], ja['kata'], ja['roma'], ja['hira'])
    else:
        body = say_button(sample[lang], THEMES[lang]['speech'], lang)
    return (
        '<section id="reading"><h2>年份怎麼唸</h2>'
        f'<p class="note">{esc(RULES[lang])}</p>'
        '<div class="tablewrap"><table><thead><tr><th>範例</th><th>1911</th></tr></thead>'
        f'<tbody><tr class="vocab-row"><td class="zh">1911 年</td><td>{body}</td></tr></tbody></table></div></section>'
    )


def event_rows(items, lang):
    rows = []
    for item in items:
        if lang == 'ja':
            sentence = (
                f'<button type="button" class="say ja" lang="ja" data-say="{esc(item["ja_say"])}" data-lang="ja-JP">'
                f'<span class="word">{esc(item["ja"])}</span>'
                f'<span class="sub">{esc(item["ja_say"])}</span></button>'
            )
            spoken_year = ja_button(
                item['forms']['ja']['kanji'], item['forms']['ja']['hira'],
                item['forms']['ja']['kata'], item['forms']['ja']['roma'],
                item['forms']['ja']['hira'],
            )
        else:
            sentence = say_button(item[lang], THEMES[lang]['speech'], lang)
            spoken_year = say_button(item['forms'][lang], THEMES[lang]['speech'], lang)
        rows.append(
            '<tr class="vocab-row">'
            f'<td class="num">{esc(item["label"])}</td>'
            f'<td class="zh">{esc(item["zh"])}<div class="note-inline">{esc(item["note"])}</div></td>'
            f'<td>{spoken_year}</td>'
            f'<td>{sentence}</td>'
            '</tr>'
        )
    return ''.join(rows)


def mono_events(lang, events, notes):
    head = (
        '<thead><tr><th>年份</th><th>事件</th><th>年份念法</th><th>句子</th></tr></thead>'
    )
    return (
        '<section id="events"><h2>歷史句子</h2>'
        '<p class="note">先點年份念法，再點整句。1945 年有兩件事：9 月 2 日戰爭結束，10 月 25 日中華民國開始接收臺灣。</p>'
        f'<div class="tablewrap"><table>{head}<tbody>{event_rows(events, lang)}</tbody></table></div></section>'
        '<section id="notes"><h2>不要和上面的單一年份混在一起</h2>'
        '<p class="note">東羅馬帝國到 1453 年才滅亡。歐洲經濟共同體是 1957 年簽約、1958 年生效；歐洲聯盟是 1993 年。</p>'
        f'<div class="tablewrap"><table>{head}<tbody>{event_rows(notes, lang)}</tbody></table></div></section>'
    )


def year_sections(lang):
    parts = [
        '<section id="years"><h2>西元 10–2040</h2>',
        '<p class="note">從西元 10 年依序唸到 2040 年。上方「循環播放 10–2040」會照這個順序朗讀；勾選「播完從頭再播」會一直循環。</p>',
    ]
    ranges = [(10, 99)]
    for start in range(100, 2000, 100):
        ranges.append((start, start + 99))
    ranges.append((2000, 2040))
    links = ''.join(f'<a href="#y{start}">{start}–{end}</a>' for start, end in ranges)
    parts.append(f'<nav class="toc" aria-label="年份區間">{links}</nav>')
    speech = THEMES[lang]['speech']
    for start, end in ranges:
        rows = []
        for n in range(start, end + 1):
            forms = year_forms(n)
            if lang == 'ja':
                ja = forms['ja']
                button = ja_button(ja['kanji'], ja['hira'], ja['kata'], ja['roma'], ja['hira'], year=n)
            else:
                button = say_button(forms[lang], speech, lang, year=n)
            rows.append(
                f'<tr class="vocab-row"><td class="num">{n}</td><td>{button}</td></tr>'
            )
        parts.append(
            f'<section id="y{start}"><h3>{start}–{end}</h3>'
            '<div class="tablewrap"><table><thead><tr><th>年份</th><th>念法</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div></section>'
        )
    parts.append('</section>')
    return ''.join(parts)


def page_css(accent, bg, border, width):
    return f'''
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:{bg}}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:{accent};color:white;padding:22px max(20px,calc((100vw - {width}px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:{width}px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.35rem;margin:32px 0 10px}}
h3{{font-size:1.05rem;margin:22px 0 8px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 14px}}
.note-inline{{font-size:.85rem;color:#6a5870;font-weight:500;margin-top:3px}}
.toc{{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}}
.toc a{{display:inline-block;padding:5px 10px;border-radius:8px;background:white;border:1px solid {border};color:{accent};text-decoration:none;font-weight:650;font-size:.85rem}}
.toc a:hover,.toc a:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid {border};border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 18px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:{accent};color:white}}
.ctrl.stop{{background:#5c6675}}
.ctrl:hover,.ctrl:focus-visible{{filter:brightness(.92);outline:2px solid {accent};outline-offset:2px}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid {border};border-radius:14px;box-shadow:0 6px 18px #142f520c;margin:0 0 8px}}
table{{border-collapse:collapse;width:100%;min-width:640px}}
th{{background:#f4f7fb;text-align:left;font-size:.9rem;padding:10px 12px}}
td{{padding:8px 12px;border-top:1px solid {border};vertical-align:top}}
.num{{color:#53647c;width:88px;font-variant-numeric:tabular-nums;font-weight:650;white-space:nowrap}}
.zh{{font-weight:650}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:3px 0;border-radius:8px;color:{accent}}}
.say:hover,.say:focus-visible{{outline:2px solid {accent};outline-offset:2px}}
.word{{font-size:1.02rem;font-weight:750;line-height:1.45}}
.sub{{font-size:.9rem;color:#3d4d63;line-height:1.45}}
.kata{{color:#6a5870}}
.roma{{font-size:.82rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid {accent};padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid {border};border-left-width:4px;line-height:1.7;color:#52647a}}
footer{{max-width:{width}px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
@media(max-width:700px){{main{{padding-top:25px}}.rate input{{width:100px}}}}
'''


def mono_page(lang, events, notes):
    theme = THEMES[lang]
    intro = (
        '用歷史年份練習念數字。先看 1911 的念法，再唸事件句子。'
        '頁面最後可以從西元 10 年循環朗讀到 2040 年。'
    )
    body = ''.join([
        controls_html(),
        '<nav class="toc" aria-label="章節"><a href="#reading">年份怎麼唸</a><a href="#events">歷史句子</a><a href="#notes">補充</a><a href="#years">10–2040</a></nav>',
        rules_block(lang),
        mono_events(lang, events, notes),
        year_sections(lang),
        '<div class="tip"><strong>用法提醒：</strong>歷史句子和 10–2040 分開播放。'
        '西元前只出現在歷史句子裡。循環播放時可調語速；勾選「播完從頭再播」會一直循環，直到按停止。</div>',
    ])
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{esc(intro)}">
<title>{esc(theme["title"])}</title>
<style>{page_css(theme["accent"], theme["bg"], theme["border"], 1050)}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← {esc(theme["brand"])}</a>　/　{esc(theme["title"].split("｜")[0])}</div></header>
<main>
<h1>{esc(theme["h1"])}</h1>
<p class="note">{esc(intro)}</p>
{body}
</main>
<footer>{esc(theme["title"])}</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def compare_event_rows(items):
    rows = []
    for item in items:
        ja = item['forms']['ja']
        cells = [
            say_button(item['en'], 'en-US', 'en'),
            say_button(item['fr'], 'fr-FR', 'fr'),
            say_button(item['de'], 'de-DE', 'de'),
            (
                f'<button type="button" class="say ja" lang="ja" data-say="{esc(item["ja_say"])}" data-lang="ja-JP">'
                f'<span class="word">{esc(item["ja"])}</span>'
                f'<span class="sub">{esc(item["ja_say"])}</span></button>'
            ),
        ]
        rows.append(
            '<tr class="vocab-row">'
            f'<td class="num">{esc(item["label"])}</td>'
            f'<td class="zh">{esc(item["zh"])}<div class="note-inline">{esc(item["note"])}</div></td>'
            + ''.join(f'<td>{cell}</td>' for cell in cells)
            + '</tr>'
        )
        del ja
    return ''.join(rows)


def compare_years():
    parts = [
        '<section id="years"><h2>西元 10–2040</h2>',
        '<p class="note">每一列依英文、法文、德文、日文唸同一個年份。循環播放會照這個順序從 10 唸到 2040。</p>',
    ]
    ranges = [(10, 99)]
    for start in range(100, 2000, 100):
        ranges.append((start, start + 99))
    ranges.append((2000, 2040))
    links = ''.join(f'<a href="#y{start}">{start}–{end}</a>' for start, end in ranges)
    parts.append(f'<nav class="toc" aria-label="年份區間">{links}</nav>')
    head = (
        '<thead><tr><th>年份</th>'
        '<th class="th-en">英文</th><th class="th-fr">法文</th>'
        '<th class="th-de">德文</th><th class="th-ja">日文</th></tr></thead>'
    )
    for start, end in ranges:
        rows = []
        for n in range(start, end + 1):
            forms = year_forms(n)
            ja = forms['ja']
            rows.append(
                '<tr class="vocab-row">'
                f'<td class="num">{n}</td>'
                f'<td>{say_button(forms["en"], "en-US", "en", year=n)}</td>'
                f'<td>{say_button(forms["fr"], "fr-FR", "fr", year=n)}</td>'
                f'<td>{say_button(forms["de"], "de-DE", "de", year=n)}</td>'
                f'<td>{ja_button(ja["kanji"], ja["hira"], ja["kata"], ja["roma"], ja["hira"], year=n)}</td>'
                '</tr>'
            )
        parts.append(
            f'<section id="y{start}"><h3>{start}–{end}</h3>'
            f'<div class="tablewrap"><table>{head}<tbody>{"".join(rows)}</tbody></table></div></section>'
        )
    parts.append('</section>')
    return ''.join(parts)


def compare_page(events, notes):
    sample = year_forms(1911)
    ja = sample['ja']
    sample_row = (
        '<tr class="vocab-row"><td class="zh">1911 年</td>'
        f'<td>{say_button(sample["en"], "en-US", "en")}</td>'
        f'<td>{say_button(sample["fr"], "fr-FR", "fr")}</td>'
        f'<td>{say_button(sample["de"], "de-DE", "de")}</td>'
        f'<td>{ja_button(ja["kanji"], ja["hira"], ja["kata"], ja["roma"], ja["hira"])}</td></tr>'
    )
    grammar = '''
<tr class="vocab-row"><td class="zh">在某一年</td>
<td><button type="button" class="say en" data-say="in nineteen fourteen" data-lang="en-US"><span class="word">in 1914</span></button></td>
<td><button type="button" class="say fr" data-say="en mille neuf cent quatorze" data-lang="fr-FR"><span class="word">en 1914</span></button></td>
<td><button type="button" class="say de" data-say="im Jahr neunzehnhundertvierzehn" data-lang="de-DE"><span class="word">im Jahr 1914</span></button></td>
<td><button type="button" class="say ja" data-say="せんきゅうひゃくじゅうよんねん に" data-lang="ja-JP"><span class="word">1914年に</span><span class="sub">せんきゅうひゃくじゅうよんねん に</span></button></td>
</tr>
'''
    head = (
        '<thead><tr><th>年份</th><th>事件</th>'
        '<th class="th-en">英文</th><th class="th-fr">法文</th>'
        '<th class="th-de">德文</th><th class="th-ja">日文</th></tr></thead>'
    )
    intro = '同一個歷史年份，並排英文、法文、德文、日文。頁尾可從西元 10 年循環朗讀到 2040 年。'
    body = ''.join([
        controls_html(),
        '<nav class="toc" aria-label="章節"><a href="#reading">1911</a><a href="#grammar">在某一年</a><a href="#events">歷史句子</a><a href="#notes">補充</a><a href="#years">10–2040</a></nav>',
        '<section id="reading"><h2>1911 怎麼唸</h2>',
        '<p class="note">英文拆成 nineteen eleven。法文是 mille neuf cent onze。德文是 neunzehnhundertelf。日文是 せんきゅうひゃくじゅういちねん。</p>',
        f'<div class="tablewrap"><table><thead><tr><th>年份</th><th class="th-en">英文</th><th class="th-fr">法文</th><th class="th-de">德文</th><th class="th-ja">日文</th></tr></thead><tbody>{sample_row}</tbody></table></div></section>',
        '<section id="grammar"><h2>在某一年</h2>',
        '<div class="tablewrap"><table><thead><tr><th></th><th class="th-en">英文 in</th><th class="th-fr">法文 en</th><th class="th-de">德文 im Jahr</th><th class="th-ja">日文 年に</th></tr></thead>',
        f'<tbody>{grammar}</tbody></table></div></section>',
        '<section id="events"><h2>歷史句子</h2>',
        '<p class="note">1945 年有兩件事。西元前用 B C E、avant notre ère、vor Christus、紀元前。</p>',
        f'<div class="tablewrap"><table>{head}<tbody>{compare_event_rows(events)}</tbody></table></div></section>',
        '<section id="notes"><h2>不要和上面的單一年份混在一起</h2>',
        '<p class="note">東羅馬帝國到 1453 年才滅亡。歐洲經濟共同體是 1957 年簽約、1958 年生效；歐洲聯盟是 1993 年。</p>',
        f'<div class="tablewrap"><table>{head}<tbody>{compare_event_rows(notes)}</tbody></table></div></section>',
        compare_years(),
        '<div class="tip"><strong>用法提醒：</strong>法文 71 用 et，80 在句尾才加 s。'
        '德文 1100 以後用「幾個百」，個位在十位前。'
        '日文三百、六百、八百要變音；1904 沒有じゅう。四讀よん、七讀なな。</div>',
    ])
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{esc(intro)}">
<title>歷史年份對照｜四語筆記</title>
<style>{page_css("#445a7a", "#f2f5fa", "#dae3ef", 1180)}
.say.en,.th-en{{color:#17355d}}
.say.fr,.th-fr{{color:#b3482f}}
.say.de,.th-de{{color:#1d6a4f}}
.say.ja,.th-ja{{color:#8d3a55}}
.say.en:hover,.say.en:focus-visible{{outline-color:#17355d}}
.say.fr:hover,.say.fr:focus-visible{{outline-color:#b3482f}}
.say.de:hover,.say.de:focus-visible{{outline-color:#1d6a4f}}
.say.ja:hover,.say.ja:focus-visible{{outline-color:#8d3a55}}
table{{min-width:980px}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 對表</a>　/　歷史年份</div></header>
<main>
<h1>歷史年份對照</h1>
<p class="note">{esc(intro)}</p>
{body}
</main>
<footer>歷史年份對照 · 四語筆記</footer>
<script>
{SPEECH_JS}
</script>
</body>
</html>
'''


def self_check(events):
    expect = {
        1911: ('nineteen eleven', 'mille neuf cent onze', 'neunzehnhundertelf', 'せんきゅうひゃくじゅういちねん'),
        1912: ('nineteen twelve', 'mille neuf cent douze', 'neunzehnhundertzwölf', 'せんきゅうひゃくじゅうにねん'),
        1789: ('seventeen eighty-nine', 'mille sept cent quatre-vingt-neuf', 'siebzehnhundertneunundachtzig', 'せんななひゃくはちじゅうきゅうねん'),
        1868: ('eighteen sixty-eight', 'mille huit cent soixante-huit', 'achtzehnhundertachtundsechzig', 'せんはっぴゃくろくじゅうはちねん'),
        1871: ('eighteen seventy-one', 'mille huit cent soixante et onze', 'achtzehnhunderteinundsiebzig', 'せんはっぴゃくななじゅういちねん'),
        1904: ('nineteen oh four', 'mille neuf cent quatre', 'neunzehnhundertvier', 'せんきゅうひゃくよんねん'),
        1914: ('nineteen fourteen', 'mille neuf cent quatorze', 'neunzehnhundertvierzehn', 'せんきゅうひゃくじゅうよんねん'),
        1945: ('nineteen forty-five', 'mille neuf cent quarante-cinq', 'neunzehnhundertfünfundvierzig', 'せんきゅうひゃくよんじゅうごねん'),
        1993: ('nineteen ninety-three', 'mille neuf cent quatre-vingt-treize', 'neunzehnhundertdreiundneunzig', 'せんきゅうひゃくきゅうじゅうさんねん'),
        1066: ('ten sixty-six', 'mille soixante-six', 'tausendsechsundsechzig', 'せんろくじゅうろくねん'),
        1219: ('twelve nineteen', 'mille deux cent dix-neuf', 'zwölfhundertneunzehn', 'せんにひゃくじゅうきゅうねん'),
        10: ('ten', 'dix', 'zehn', 'じゅうねん'),
        395: ('three ninety-five', 'trois cent quatre-vingt-quinze', 'dreihundertfünfundneunzig', 'さんびゃくきゅうじゅうごねん'),
        1624: ('sixteen twenty-four', 'mille six cent vingt-quatre', 'sechzehnhundertvierundzwanzig', 'せんろっぴゃくにじゅうよんねん'),
        2000: ('two thousand', 'deux mille', 'zweitausend', 'にせんねん'),
        2001: ('two thousand one', 'deux mille un', 'zweitausendeins', 'にせんいちねん'),
        2010: ('twenty ten', 'deux mille dix', 'zweitausendzehn', 'にせんじゅうねん'),
        2040: ('twenty forty', 'deux mille quarante', 'zweitausendvierzig', 'にせんよんじゅうねん'),
    }
    for n, (e, f, d, h) in expect.items():
        got = year_forms(n)
        assert got['en'] == e, (n, 'en', got['en'], e)
        assert got['fr'] == f, (n, 'fr', got['fr'], f)
        assert got['de'] == d, (n, 'de', got['de'], d)
        assert got['ja']['hira'] == h, (n, 'ja', got['ja']['hira'], h)
    by_zh = {item['zh']: item for item in events}
    assert by_zh['中華民國成立']['en'] == 'The Republic of China was founded in nineteen twelve.'
    assert by_zh['中華民國成立']['fr'] == 'La République de Chine a été fondée en mille neuf cent douze.'
    assert by_zh['中華民國成立']['de'] == 'Die Republik China wurde im Jahr neunzehnhundertzwölf gegründet.'
    assert by_zh['法國大革命開始']['de'] == 'Die Französische Revolution begann im Jahr siebzehnhundertneunundachtzig.'
    assert by_zh['歐洲聯盟成立']['fr'] == "L'Union européenne a été créée en mille neuf cent quatre-vingt-treize."
    assert by_zh['明治維新開始']['ja_say'].startswith('せんはっぴゃくろくじゅうはちねん')
    assert year_forms(202, True)['en'] == 'two oh two B C E'
    assert year_forms(27, True)['de'] == 'siebenundzwanzig vor Christus'
    print('self_check ok', len(events), 'events')


def insert_card(path, needle, card):
    text = path.read_text(encoding='utf-8')
    if 'href="./years/"' in text:
        print('index exists', path)
        return
    pos = text.find(needle)
    if pos < 0:
        raise SystemExit(f'missing {needle} in {path}')
    end = text.find('</article>', pos)
    if needle.startswith('<h2>'):
        insert_at = pos + len(needle)
    else:
        insert_at = end + len('</article>')
    path.write_text(text[:insert_at] + '\n' + card + text[insert_at:], encoding='utf-8')
    print('index', path)


def main():
    events = [fill(item) for item in EVENTS]
    notes = [fill(item) for item in NOTES]
    self_check(events)
    for lang in ('en', 'fr', 'de', 'ja'):
        folder = ROOT / lang / 'years'
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / 'index.html'
        path.write_text(mono_page(lang, events, notes), encoding='utf-8')
        print(path, path.stat().st_size)
    compare = ROOT / 'tables' / 'years'
    compare.mkdir(parents=True, exist_ok=True)
    path = compare / 'index.html'
    path.write_text(compare_page(events, notes), encoding='utf-8')
    print(path, path.stat().st_size)

    cards = {
        'en': '<article class="item"><div class="meta">歷史 · 年份 · 跟讀</div><h3>Years</h3><p>歷史事件的年份念法與完整句子。頁尾可從西元 10 年循環朗讀到 2040 年。</p><a class="button" href="./years/">進入 Years →</a></article>',
        'fr': '<article class="item"><div class="meta">歷史 · 年份 · 跟讀</div><h3 lang="fr">Années</h3><p>歷史事件的年份念法與完整句子。頁尾可從西元 10 年循環朗讀到 2040 年。</p><a class="button" href="./years/">進入 Années →</a></article>',
        'de': '<article class="item"><div class="meta">歷史 · 年份 · 跟讀</div><h3 lang="de">Jahreszahlen</h3><p>歷史事件的年份念法與完整句子。頁尾可從西元 10 年循環朗讀到 2040 年。</p><a class="button" href="./years/">進入 Jahreszahlen →</a></article>',
        'ja': '<article class="item"><div class="meta">歷史 · 年份 · 跟讀</div><h3 lang="ja">西暦</h3><p>歷史事件的年份念法與完整句子。頁尾可從西元 10 年循環朗讀到 2040 年。</p><a class="button" href="./years/">進入 西暦 →</a></article>',
    }
    insert_card(ROOT / 'en' / 'index.html', 'href="./numbers/"', cards['en'])
    insert_card(ROOT / 'fr' / 'index.html', 'href="./numbers-be-ch/"', cards['fr'])
    insert_card(ROOT / 'de' / 'index.html', 'href="./numbers/"', cards['de'])
    insert_card(ROOT / 'ja' / 'index.html', 'href="./numbers/"', cards['ja'])
    compare_card = '''<article class="item">
<div class="meta">歷史 · 四語對照 · 跟讀</div>
<h3>歷史年份對照</h3>
<div class="langs">
<span class="en">EN</span>
<span class="de">DE</span>
<span class="fr">FR</span>
<span class="ja">JA</span>
</div>
<p>同一個歷史年份並排四種念法與事件句子。頁尾可從西元 10 年循環朗讀到 2040 年。</p>
<a class="button" href="./years/">進入歷史年份對照 →</a>
</article>'''
    insert_card(ROOT / 'tables' / 'index.html', '<h2>比較清單</h2>', compare_card)


if __name__ == '__main__':
    main()
