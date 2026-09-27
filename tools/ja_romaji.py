"""Hepburn romaji generated from spaced kana.

Particles written as their own tokens become wa, o, and e.
Long vowels follow the kana: ou, oo, ei, ii. A choonpu doubles the vowel.
"""

_DIGRAPH = {
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
    'ぢゃ': 'ja', 'ぢゅ': 'ju', 'ぢょ': 'jo',
}

_MONO = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'o', 'ん': 'n',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ゔ': 'vu',
}

_SMALL_VOWEL = {'ぁ': 'a', 'ぃ': 'i', 'ぅ': 'u', 'ぇ': 'e', 'ぉ': 'o'}
_PUNCT = {'。': '.', '、': ',', '？': '?', '！': '!', '「': '"', '」': '"', '『': '"', '』': '"'}
_TOKEN = {'は': 'wa', 'を': 'o', 'へ': 'e', 'こんにちは': 'konnichiwa', 'こんばんは': 'konbanwa'}


def _kata_to_hira(text):
    out = []
    for ch in text:
        code = ord(ch)
        if 0x30A1 <= code <= 0x30F6:
            out.append(chr(code - 0x60))
        elif ch == 'ー':
            out.append('ー')
        else:
            out.append(ch)
    return ''.join(out)


def _geminate(syllable):
    if syllable.startswith('ch'):
        return 't' + syllable
    if syllable.startswith('sh'):
        return 's' + syllable
    return syllable[0] + syllable


def _apply_small_vowel(prev, vowel):
    if prev == 'fu':
        return 'f' + vowel
    if prev == 'u':
        return 'w' + vowel
    if prev == 'vu':
        return 'v' + vowel
    if prev.endswith(('a', 'i', 'u', 'e', 'o')):
        return prev[:-1] + vowel
    return prev + vowel


def _syllable(text, index):
    rest = text[index:]
    if rest[:2] in _DIGRAPH:
        return _DIGRAPH[rest[:2]], index + 2
    ch = rest[0]
    if ch in _MONO:
        return _MONO[ch], index + 1
    if ch in _SMALL_VOWEL or ch == 'っ' or ch == 'ー':
        raise ValueError(f'kana starts with {ch}: {text}')
    raise ValueError(f'cannot read {ch} in {text}')


def _convert_core(text):
    text = _kata_to_hira(text)
    out = []
    i = 0
    while i < len(text):
        if text[i] == 'っ':
            syllable, nxt = _syllable(text, i + 1)
            if nxt < len(text) and text[nxt] in _SMALL_VOWEL:
                syllable = _apply_small_vowel(syllable, _SMALL_VOWEL[text[nxt]])
                nxt += 1
            out.append(_geminate(syllable))
            i = nxt
            continue
        if text[i] == 'ー':
            if not out or not out[-1][-1] in 'aiueo':
                raise ValueError(f'choonpu without a vowel: {text}')
            out[-1] += out[-1][-1]
            i += 1
            continue
        if text[i] == 'ん':
            nxt = text[i + 1] if i + 1 < len(text) else ''
            if nxt and nxt in 'あいうえおやゆよぁぃぅぇぉ':
                out.append("n'")
            else:
                out.append('n')
            i += 1
            continue
        syllable, nxt = _syllable(text, i)
        if nxt < len(text) and text[nxt] in _SMALL_VOWEL:
            syllable = _apply_small_vowel(syllable, _SMALL_VOWEL[text[nxt]])
            nxt += 1
        out.append(syllable)
        i = nxt
    return ''.join(out)


def _split_token(token):
    core = token
    suffix = ''
    while core and core[-1] in _PUNCT:
        suffix = _PUNCT[core[-1]] + suffix
        core = core[:-1]
    prefix = ''
    while core and core[0] in _PUNCT:
        prefix += _PUNCT[core[0]]
        core = core[1:]
    return prefix, core, suffix


def to_romaji(kana_line):
    parts = []
    for token in kana_line.split():
        prefix, core, suffix = _split_token(token)
        if not core:
            if prefix or suffix:
                parts.append(prefix + suffix)
            continue
        if core in _TOKEN:
            body = _TOKEN[core]
        elif all(('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ch in "-'" for ch in core):
            body = core
        else:
            body = _convert_core(core)
        parts.append(prefix + body + suffix)
    text = ' '.join(part for part in parts if part)
    if not any(mark in kana_line for mark in '。？！'):
        return text
    for index, ch in enumerate(text):
        if ch.isalpha():
            return text[:index] + ch.upper() + text[index + 1:]
    return text


def self_test():
    pairs = [
        ('わたし', 'watashi'),
        ('は', 'wa'),
        ('を', 'o'),
        ('へ', 'e'),
        ('がくせい', 'gakusei'),
        ('きょう', 'kyou'),
        ('コーヒー', 'koohii'),
        ('がっこう', 'gakkou'),
        ('ちょっと', 'chotto'),
        ('いっぱい', 'ippai'),
        ('いっしょ', 'issho'),
        ('きんえん', "kin'en"),
        ('フランス', 'furansu'),
        ('じゅぎょう', 'jugyou'),
        ('しゃしん', 'shashin'),
        ('りょこう', 'ryokou'),
        ('こんにちは', 'konnichiwa'),
        ('こんばんは', 'konbanwa'),
        ('でんわ', 'denwa'),
        ('パーティー', 'paatii'),
        ('まっちゃ', 'matcha'),
        ('にほんご', 'nihongo'),
        ('わたし は がくせい です。', 'Watashi wa gakusei desu.'),
        ('おなまえ は なん です か。', 'Onamae wa nan desu ka.'),
        ('あした、 ともだち に あいます。', 'Ashita, tomodachi ni aimasu.'),
    ]
    bad = []
    for kana, expect in pairs:
        got = to_romaji(kana)
        if got != expect:
            bad.append(f'{kana} => {got!r} expected {expect!r}')
    if bad:
        raise SystemExit('romaji self-test failed:\n' + '\n'.join(bad))
