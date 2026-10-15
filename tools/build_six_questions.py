# -*- coding: utf-8 -*-
"""六類口說問題 + habiter／live／wohnen：寫入四語對話與地點頁，並產生對照。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q = "\u2019"
MARK = "lesson-six-2026"


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def insert_before(path, needle, block):
    text = read(path)
    if MARK in text:
        print("skip", path.relative_to(ROOT))
        return
    pos = text.rfind(needle) if needle == "</main>" else text.find(needle)
    if pos < 0:
        raise SystemExit(f"{needle!r} missing in {path}")
    write(path, text[:pos] + block + "\n" + text[pos:])
    print("inserted", path.relative_to(ROOT))


def replace_once(path, old, new):
    text = read(path)
    if new.strip()[:40] in text and MARK in text:
        print("already", path.relative_to(ROOT))
        return
    if old not in text:
        raise SystemExit(f"missing in {path}: {old[:90]!r}")
    write(path, text.replace(old, new, 1))
    print("patched", path.relative_to(ROOT))


def btn(lang, code, say, inner=None):
    shown = say if inner is None else inner
    return (
        f'<button type="button" class="say" lang="{lang}" data-say="{say}" data-lang="{code}">'
        f'<span class="word">{shown}</span></button>'
    )


def fr(say):
    return btn("fr", "fr-FR", say)


def en(say):
    return btn("en", "en-US", say)


def de(say):
    return btn("de", "de-DE", say)


def ja(say, kanji, hira, kata, roma):
    return (
        f'<button type="button" class="say" lang="ja" data-say="{say}" data-lang="ja-JP">'
        f'<span class="kanji">{kanji}</span>'
        f'<span class="kana"><span class="hira">{hira}</span>　<span class="kata">{kata}</span></span>'
        f'<span class="roma">{roma}</span></button>'
    )


def table(headers, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    return (
        '<div class="tablewrap"><table><thead><tr>'
        + th
        + "</tr></thead><tbody>\n"
        + "\n".join(rows)
        + "\n</tbody></table></div>"
    )


def tr(*cells):
    tds = []
    for i, cell in enumerate(cells):
        cls = ' class="zh"' if i == 0 else ""
        tds.append(f"<td{cls}>{cell}</td>")
    return '<tr class="vocab-row">' + "".join(tds) + "</tr>"


def french_dialogue():
    six = [
        tr(
            "國籍",
            fr(f"Vous êtes de quelle nationalité ?"),
            fr(f"Tu es de quelle nationalité ?"),
            "您／你是哪國人？",
            fr("Je suis taïwanais."),
        ),
        tr(
            "年齡",
            fr("Vous avez quel âge ?"),
            fr(f"Tu as quel âge ?"),
            "您／你幾歲？",
            fr(f"J{Q}ai trente-trois ans."),
        ),
        tr(
            "電話",
            fr(f"Quel est votre numéro de téléphone ?"),
            fr(f"Quel est ton numéro de téléphone ?"),
            "您／你的電話號碼是多少？",
            fr(f"Mon numéro de téléphone est le…"),
        ),
        tr(
            "喜好",
            fr(f"Qu{Q}est-ce que vous aimez ?"),
            fr(f"Qu{Q}est-ce que tu aimes ?"),
            "您／你喜歡什麼？",
            fr(f"J{Q}aime voyager."),
        ),
        tr(
            "語言",
            fr("Vous parlez quelles langues ?"),
            fr("Tu parles quelles langues ?"),
            "您／你會說哪些語言？",
            fr("Je parle chinois et anglais."),
        ),
        tr(
            "居住",
            fr("Vous habitez où ?"),
            fr("Tu habites où ?"),
            "您／你住在哪裡？",
            fr(f"J{Q}habite à Taipei."),
        ),
    ]
    extras = [
        tr("您的國籍是什麼？", fr("Quelle est votre nationalité ?")),
        tr("您喜歡什麼？（口語）", fr("Vous aimez quoi ?")),
        tr("你喜歡什麼？（口語）", fr("Tu aimes quoi ?")),
    ]
    conj = [
        tr("je 我", "j’habite", fr(f"J{Q}habite à Taipei."), "我住在臺北。"),
        tr("tu 你", "tu habites", fr("Tu habites à Taipei."), "你住在臺北。"),
        tr("il 他", "il habite", fr("Il habite à Taipei."), "他住在臺北。"),
        tr("elle 她", "elle habite", fr("Elle habite à Taipei."), "她住在臺北。"),
        tr("on 我們／人們", "on habite", fr("On habite à Taipei."), "我們住在臺北。"),
        tr("nous 我們", "nous habitons", fr("Nous habitons à Taipei."), "我們住在臺北。"),
        tr("vous 您／你們", "vous habitez", fr("Vous habitez à Taipei."), "您／你們住在臺北。"),
        tr("ils 他們", "ils habitent", fr("Ils habitent à Taipei."), "他們住在臺北。"),
        tr("elles 她們", "elles habitent", fr("Elles habitent à Taipei."), "她們住在臺北。"),
    ]
    endings = [
        tr("je", "-e", "habite"),
        tr("tu", "-es", "habites"),
        tr("il / elle / on", "-e", "habite"),
        tr("nous", "-ons", "habitons"),
        tr("vous", "-ez", "habitez"),
        tr("ils / elles", "-ent", "habitent"),
    ]
    three = [
        tr("je", "j’habite", "je parle", "j’aime"),
        tr("tu", "tu habites", "tu parles", "tu aimes"),
        tr("il / elle / on", "habite", "parle", "aime"),
        tr("nous", "nous habitons", "nous parlons", "nous aimons"),
        tr("vous", "vous habitez", "vous parlez", "vous aimez"),
        tr("ils / elles", "habitent", "parlent", "aiment"),
    ]
    reply = [
        tr("Vous êtes… ?", fr("Je suis…"), "您是……？→ 我是……"),
        tr("Vous avez… ?", fr(f"J{Q}ai…"), "您有……？→ 我有……"),
        tr("Vous aimez… ?", fr(f"J{Q}aime…"), "您喜歡……？→ 我喜歡……"),
        tr("Vous parlez… ?", fr("Je parle…"), "您說……？→ 我說……"),
        tr("Vous habitez… ?", fr(f"J{Q}habite…"), "您住……？→ 我住……"),
    ]
    likes = [
        tr("我喜歡瑜伽。", fr(f"J{Q}aime le yoga.")),
        tr("我喜歡做瑜伽。", fr(f"J{Q}aime faire du yoga.")),
        tr("我喜歡旅行。", fr(f"J{Q}aime les voyages.")),
        tr("我喜歡去旅行。", fr(f"J{Q}aime voyager.")),
        tr("我喜歡健行。", fr(f"J{Q}aime la randonnée.")),
        tr("我喜歡比利時、荷蘭和奧地利。", fr(f"J{Q}aime la Belgique, les Pays-Bas et l{Q}Autriche.")),
        tr("我會說中文和英文。", fr("Je parle chinois et anglais.")),
        tr("我正在學法文、德文和日文。", fr(f"J{Q}apprends le français, l{Q}allemand et le japonais.")),
        tr("我住在臺灣臺北。", fr(f"J{Q}habite à Taipei, à Taïwan.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>六類問題與回答</h2>",
        f'<p class="note">vous＝您／你們；tu＝你。跟老師或考官練習時，可先統一用 vous。年齡示範用 trente-trois ans。</p>',
        table(["主題", "vous 禮貌", "tu 熟人", "中文", "回答範例"], six),
        "<h2>補充問法</h2>",
        table(["中文", "法文"], extras),
        "<h2>habiter「居住」現在式</h2>",
        f'<p class="note">habiter 是 -er 動詞。去掉 -er，留下 habit-，再加字尾。h 是啞音，所以 je + habite → j{Q}habite。on 表示「我們」時，動詞仍用第三人稱單數 on habite。être、avoir 不能套這套字尾。</p>',
        table(["主詞", "變位", "完整例句", "中文"], conj),
        "<h2>字尾表</h2>",
        table(["主詞", "字尾", "結果"], endings),
        "<h2>三個 -er 動詞對照</h2>",
        table(["主詞", "habiter", "parler", "aimer"], three),
        "<h2>對方問 → 你回答</h2>",
        table(["對方問", "你回答", "說明"], reply),
        "<h2>喜好與語言補充</h2>",
        table(["中文", "法文"], likes),
        f'<div class="tip"><strong>用法提醒：</strong>完整 -er 動詞表見 <a href="../verbes-er/">Verbes en -er</a>。城市用 à、國家用 en／au／aux，見 <a href="../pays-prepositions/">En, au, aux</a>。四語並排見 <a href="../../tables/six-qa/">六類問答對照</a>。</div>',
        "",
    ])


def french_place():
    rows = [
        tr("比利時〔陰性〕", fr(f"J{Q}habite en Belgique."), fr(f"J{Q}aime la Belgique.")),
        tr("荷蘭〔複數〕", fr(f"J{Q}habite aux Pays-Bas."), fr(f"J{Q}aime les Pays-Bas.")),
        tr("奧地利〔陰性〕", fr(f"J{Q}habite en Autriche."), fr(f"J{Q}aime l{Q}Autriche.")),
        tr("日本〔陽性、子音開頭〕", fr(f"J{Q}habite au Japon."), fr(f"J{Q}aime le Japon.")),
        tr("伊朗〔陽性、母音開頭〕", fr(f"J{Q}habite en Iran."), fr(f"J{Q}aime l{Q}Iran.")),
        tr("臺灣", fr(f"J{Q}habite à Taïwan."), fr(f"J{Q}aime Taïwan.")),
        tr("臺北〔城市〕", fr(f"J{Q}habite à Taipei."), fr(f"J{Q}aime Taipei.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>住在與喜歡：介詞不同</h2>",
        f'<p class="note">城市用 à。陰性國家與母音開頭的陽性國家用 en。子音開頭的陽性國家用 au。複數國家用 aux。臺灣常用 à Taïwan。「喜歡」用定冠詞；「住在」用地名介詞。</p>',
        table(["地點", "住在", "喜歡"], rows),
        f'<div class="tip"><strong>對照：</strong>{fr(f"J{Q}aime la Belgique.")} 是喜歡比利時；{fr(f"J{Q}habite en Belgique.")} 是住在比利時。</div>',
        "",
    ])


def english_dialogue():
    six = [
        tr("國籍", en("What nationality are you?"), en("Where are you from?"), "您／你是哪國人？", en("I'm Taiwanese.")),
        tr("年齡", en("How old are you?"), en("How old are you?"), "您／你幾歲？", en("I'm thirty-three.")),
        tr("電話", en("What's your phone number?"), en("What's your number?"), "您／你的電話號碼是多少？", en("My phone number is…")),
        tr("喜好", en("What do you like?"), en("What do you like?"), "您／你喜歡什麼？", en("I like traveling.")),
        tr("語言", en("What languages do you speak?"), en("What languages do you speak?"), "您／你會說哪些語言？", en("I speak Chinese and English.")),
        tr("居住", en("Where do you live?"), en("Where do you live?"), "您／你住在哪裡？", en("I live in Taipei.")),
    ]
    conj = [
        tr("I", "live", en("I live in Taipei."), "我住在臺北。"),
        tr("you", "live", en("You live in Taipei."), "你住在臺北。"),
        tr("he / she", "lives", en("He lives in Taipei."), "他住在臺北。"),
        tr("we", "live", en("We live in Taipei."), "我們住在臺北。"),
        tr("they", "live", en("They live in Taipei."), "他們住在臺北。"),
    ]
    reply = [
        tr("Are you… ?", en("I am… / I'm…")),
        tr("How old are you?", en("I'm thirty-three.")),
        tr("What do you like?", en("I like…")),
        tr("What languages do you speak?", en("I speak…")),
        tr("Where do you live?", en("I live…")),
    ]
    likes = [
        tr("我喜歡瑜伽。", en("I like yoga.")),
        tr("我喜歡做瑜伽。", en("I like doing yoga.")),
        tr("我喜歡旅行。", en("I like traveling.")),
        tr("我喜歡比利時、荷蘭和奧地利。", en("I like Belgium, the Netherlands, and Austria.")),
        tr("我會說中文和英文。", en("I speak Chinese and English.")),
        tr("我正在學法文、德文和日文。", en("I'm learning French, German, and Japanese.")),
        tr("我住在臺灣臺北。", en("I live in Taipei, Taiwan.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>六類問題與回答</h2>",
        '<p class="note">英文沒有 tu／vous，但可用較完整或較短的問法。年齡用 be，不說 I have thirty-three years。he／she 的 live 要加 s：lives。</p>',
        table(["主題", "常用問法", "另一種問法", "中文", "回答範例"], six),
        "<h2>live「居住」現在式</h2>",
        table(["主詞", "動詞", "完整例句", "中文"], conj),
        "<h2>對方問 → 你回答</h2>",
        table(["對方問", "你回答"], reply),
        "<h2>喜好與語言補充</h2>",
        table(["中文", "英文"], likes),
        '<div class="tip"><strong>用法提醒：</strong>國家和城市都用 in：I live in Taiwan／in Taipei。四語並排見 <a href="../../tables/six-qa/">六類問答對照</a>。</div>',
        "",
    ])


def english_place():
    rows = [
        tr("比利時", en("I live in Belgium."), en("I like Belgium.")),
        tr("荷蘭", en("I live in the Netherlands."), en("I like the Netherlands.")),
        tr("奧地利", en("I live in Austria."), en("I like Austria.")),
        tr("日本", en("I live in Japan."), en("I like Japan.")),
        tr("臺灣", en("I live in Taiwan."), en("I like Taiwan.")),
        tr("臺北", en("I live in Taipei."), en("I like Taipei.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>住在與喜歡</h2>",
        '<p class="note">英文住在國家或城市都用 in。喜歡直接接國名，定冠詞只在少數國名需要，例如 the Netherlands。</p>',
        table(["地點", "住在", "喜歡"], rows),
        "",
    ])


def german_dialogue():
    six = [
        tr("國籍", de("Welche Nationalität haben Sie?"), de("Welche Nationalität hast du?"), "您／你是哪國人？", de("Ich bin Taiwaner.")),
        tr("年齡", de("Wie alt sind Sie?"), de("Wie alt bist du?"), "您／你幾歲？", de("Ich bin dreiunddreißig Jahre alt.")),
        tr("電話", de("Wie ist Ihre Telefonnummer?"), de("Wie ist deine Telefonnummer?"), "您／你的電話號碼是多少？", de("Meine Telefonnummer ist…")),
        tr("喜好", de("Was mögen Sie?"), de("Was magst du?"), "您／你喜歡什麼？", de("Ich mag Reisen.")),
        tr("語言", de("Welche Sprachen sprechen Sie?"), de("Welche Sprachen sprichst du?"), "您／你會說哪些語言？", de("Ich spreche Chinesisch und Englisch.")),
        tr("居住", de("Wo wohnen Sie?"), de("Wo wohnst du?"), "您／你住在哪裡？", de("Ich wohne in Taipeh.")),
    ]
    conj = [
        tr("ich", "wohne", de("Ich wohne in Taipeh."), "我住在臺北。"),
        tr("du", "wohnst", de("Du wohnst in Taipeh."), "你住在臺北。"),
        tr("er / sie / es", "wohnt", de("Er wohnt in Taipeh."), "他住在臺北。"),
        tr("wir", "wohnen", de("Wir wohnen in Taipeh."), "我們住在臺北。"),
        tr("ihr", "wohnt", de("Ihr wohnt in Taipeh."), "你們住在臺北。"),
        tr("sie / Sie", "wohnen", de("Sie wohnen in Taipeh."), "他們／您住在臺北。"),
    ]
    reply = [
        tr("Sind Sie… ?", de("Ich bin…")),
        tr("Wie alt sind Sie?", de("Ich bin … Jahre alt.")),
        tr("Was mögen Sie?", de("Ich mag…")),
        tr("Welche Sprachen sprechen Sie?", de("Ich spreche…")),
        tr("Wo wohnen Sie?", de("Ich wohne…")),
    ]
    likes = [
        tr("我喜歡瑜伽。", de("Ich mag Yoga.")),
        tr("我喜歡旅行。", de("Ich mag Reisen.")),
        tr("我喜歡比利時、荷蘭和奧地利。", de("Ich mag Belgien, die Niederlande und Österreich.")),
        tr("我會說中文和英文。", de("Ich spreche Chinesisch und Englisch.")),
        tr("我正在學法文、德文和日文。", de("Ich lerne Französisch, Deutsch und Japanisch.")),
        tr("我住在臺灣臺北。", de("Ich wohne in Taipeh, in Taiwan.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>六類問題與回答</h2>",
        '<p class="note">跟老師或考官可先統一用 Sie。年齡用 sein + Jahre alt，不是 haben。wohnen 是規則動詞。</p>',
        table(["主題", "Sie 禮貌", "du 熟人", "中文", "回答範例"], six),
        "<h2>wohnen「居住」現在式</h2>",
        table(["主詞", "變位", "完整例句", "中文"], conj),
        "<h2>對方問 → 你回答</h2>",
        table(["對方問", "你回答"], reply),
        "<h2>喜好與語言補充</h2>",
        table(["中文", "德文"], likes),
        '<div class="tip"><strong>用法提醒：</strong>城市和多數國家用 in：Ich wohne in Taiwan／in Taipeh。四語並排見 <a href="../../tables/six-qa/">六類問答對照</a>。</div>',
        "",
    ])


def german_place():
    rows = [
        tr("比利時", de("Ich wohne in Belgien."), de("Ich mag Belgien.")),
        tr("荷蘭", de("Ich wohne in den Niederlanden."), de("Ich mag die Niederlande.")),
        tr("奧地利", de("Ich wohne in Österreich."), de("Ich mag Österreich.")),
        tr("日本", de("Ich wohne in Japan."), de("Ich mag Japan.")),
        tr("臺灣", de("Ich wohne in Taiwan."), de("Ich mag Taiwan.")),
        tr("臺北", de("Ich wohne in Taipeh."), de("Ich mag Taipeh.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>住在與喜歡</h2>",
        '<p class="note">多數國名用 in，不加冠詞。die Niederlande 是複數，所以說 in den Niederlanden。mögen 後面直接接國名。</p>',
        table(["地點", "住在", "喜歡"], rows),
        "",
    ])


def japanese_dialogue():
    def j(say, kanji, hira, kata, roma):
        return ja(say, kanji, hira, kata, roma)

    six = [
        tr(
            "國籍",
            j("どの国の人ですか。", "どの国の人ですか。", "どの くに の ひと ですか。", "ドノ クニ ノ ヒト デスカ。", "Dono kuni no hito desu ka."),
            j("どちらの国から来ましたか。", "どちらの国から来ましたか。", "どちら の くに から きましたか。", "ドチラ ノ クニ カラ キマシタカ。", "Dochira no kuni kara kimashita ka."),
            "您／你是哪國人？",
            j("台湾人です。", "台湾人です。", "たいわんじん です。", "タイワンジン デス。", "Taiwanjin desu."),
        ),
        tr(
            "年齡",
            j("何歳ですか。", "何歳ですか。", "なんさい ですか。", "ナンサイ デスカ。", "Nansai desu ka."),
            j("おいくつですか。", "おいくつですか。", "おいくつ ですか。", "オイクツ デスカ。", "O-ikutsu desu ka."),
            "您／你幾歲？",
            j("三十三歳です。", "三十三歳です。", "さんじゅうさんさい です。", "サンジュウサンサイ デス。", "Sanjuusansai desu."),
        ),
        tr(
            "電話",
            j("電話番号は何番ですか。", "電話番号は何番ですか。", "でんわばんごう は なんばん ですか。", "デンワバンゴウ ハ ナンバン デスカ。", "Denwa bangou wa nanban desu ka."),
            j("電話番号を教えてください。", "電話番号を教えてください。", "でんわばんごう を おしえて ください。", "デンワバンゴウ ヲ オシエテ クダサイ。", "Denwa bangou o oshiete kudasai."),
            "您／你的電話號碼是多少？",
            j("電話番号は……です。", "電話番号は……です。", "でんわばんごう は …… です。", "デンワバンゴウ ハ …… デス。", "Denwa bangou wa … desu."),
        ),
        tr(
            "喜好",
            j("何が好きですか。", "何が好きですか。", "なに が すき ですか。", "ナニ ガ スキ デスカ。", "Nani ga suki desu ka."),
            j("趣味は何ですか。", "趣味は何ですか。", "しゅみ は なん ですか。", "シュミ ハ ナン デスカ。", "Shumi wa nan desu ka."),
            "您／你喜歡什麼？",
            j("旅行が好きです。", "旅行が好きです。", "りょこう が すき です。", "リョコウ ガ スキ デス。", "Ryokou ga suki desu."),
        ),
        tr(
            "語言",
            j("何語が話せますか。", "何語が話せますか。", "なにご が はなせますか。", "ナニゴ ガ ハナセマスカ。", "Nanigo ga hanasemasu ka."),
            j("どんな言語ができますか。", "どんな言語ができますか。", "どんな げんご が できますか。", "ドンナ ゲンゴ ガ デキマスカ。", "Donna gengo ga dekimasu ka."),
            "您／你會說哪些語言？",
            j("中国語と英語が話せます。", "中国語と英語が話せます。", "ちゅうごくご と えいご が はなせます。", "チュウゴクゴ ト エイゴ ガ ハナセマス。", "Chuugokugo to eigo ga hanasemasu."),
        ),
        tr(
            "居住",
            j("どこに住んでいますか。", "どこに住んでいますか。", "どこ に すんでいますか。", "ドコ ニ スンデイマスカ。", "Doko ni sunde imasu ka."),
            j("お住まいはどちらですか。", "お住まいはどちらですか。", "おすまい は どちら ですか。", "オスマイ ハ ドチラ デスカ。", "O-sumai wa dochira desu ka."),
            "您／你住在哪裡？",
            j("台北に住んでいます。", "台北に住んでいます。", "たいぺい に すんでいます。", "タイペイ ニ スンデイマス。", "Taipei ni sunde imasu."),
        ),
    ]
    conj = [
        tr("私", "住んでいます", j("私は台北に住んでいます。", "私は台北に住んでいます。", "わたし は たいぺい に すんでいます。", "ワタシ ハ タイペイ ニ スンデイマス。", "Watashi wa Taipei ni sunde imasu."), "我住在臺北。"),
        tr("あなた", "住んでいます", j("あなたは台北に住んでいます。", "あなたは台北に住んでいます。", "あなた は たいぺい に すんでいます。", "アナタ ハ タイペイ ニ スンデイマス。", "Anata wa Taipei ni sunde imasu."), "你住在臺北。"),
        tr("彼／彼女", "住んでいます", j("彼は台北に住んでいます。", "彼は台北に住んでいます。", "かれ は たいぺい に すんでいます。", "カレ ハ タイペイ ニ スンデイマス。", "Kare wa Taipei ni sunde imasu."), "他住在臺北。"),
        tr("私たち", "住んでいます", j("私たちは台北に住んでいます。", "私たちは台北に住んでいます。", "わたし たち は たいぺい に すんでいます。", "ワタシタチ ハ タイペイ ニ スンデイマス。", "Watashitachi wa Taipei ni sunde imasu."), "我們住在臺北。"),
    ]
    reply = [
        tr("どの国の人ですか。", j("台湾人です。", "台湾人です。", "たいわんじん です。", "タイワンジン デス。", "Taiwanjin desu.")),
        tr("何歳ですか。", j("三十三歳です。", "三十三歳です。", "さんじゅうさんさい です。", "サンジュウサンサイ デス。", "Sanjuusansai desu.")),
        tr("何が好きですか。", j("旅行が好きです。", "旅行が好きです。", "りょこう が すき です。", "リョコウ ガ スキ デス。", "Ryokou ga suki desu.")),
        tr("何語が話せますか。", j("中国語と英語が話せます。", "中国語と英語が話せます。", "ちゅうごくご と えいご が はなせます。", "チュウゴクゴ ト エイゴ ガ ハナセマス。", "Chuugokugo to eigo ga hanasemasu.")),
        tr("どこに住んでいますか。", j("台北に住んでいます。", "台北に住んでいます。", "たいぺい に すんでいます。", "タイペイ ニ スンデイマス。", "Taipei ni sunde imasu.")),
    ]
    likes = [
        tr("我喜歡瑜伽。", j("ヨガが好きです。", "ヨガが好きです。", "ヨガ が すき です。", "ヨガ ガ スキ デス。", "Yoga ga suki desu.")),
        tr("我喜歡旅行。", j("旅行が好きです。", "旅行が好きです。", "りょこう が すき です。", "リョコウ ガ スキ デス。", "Ryokou ga suki desu.")),
        tr("我喜歡比利時、荷蘭和奧地利。", j("ベルギーとオランダとオーストリアが好きです。", "ベルギーとオランダとオーストリアが好きです。", "ベルギー と オランダ と オーストリア が すき です。", "ベルギー ト オランダ ト オーストリア ガ スキ デス。", "Berugii to Oranda to Oosutoria ga suki desu.")),
        tr("我會說中文和英文。", j("中国語と英語が話せます。", "中国語と英語が話せます。", "ちゅうごくご と えいご が はなせます。", "チュウゴクゴ ト エイゴ ガ ハナセマス。", "Chuugokugo to eigo ga hanasemasu.")),
        tr("我正在學法文、德文和日文。", j("フランス語とドイツ語と日本語を勉強しています。", "フランス語とドイツ語と日本語を勉強しています。", "フランスご と ドイツご と にほんご を べんきょうしています。", "フランスゴ ト ドイツゴ ト ニホンゴ ヲ ベンキョウシテイマス。", "Furansugo to Doitsugo to Nihongo o benkyou shite imasu.")),
        tr("我住在臺灣臺北。", j("台湾の台北に住んでいます。", "台湾の台北に住んでいます。", "たいわん の たいぺい に すんでいます。", "タイワン ノ タイペイ ニ スンデイマス。", "Taiwan no Taipei ni sunde imasu.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>六類問題與回答</h2>",
        '<p class="note">課堂多用です／ます。居住常用「住んでいます」。年齡用「歳です」。</p>',
        table(["主題", "常用問法", "另一種問法", "中文", "回答範例"], six),
        "<h2>住む「居住」</h2>",
        '<p class="note">口語說現在住哪裡，多用「住んでいます」。場所後面加助詞に。</p>',
        table(["主詞", "動詞", "完整例句", "中文"], conj),
        "<h2>對方問 → 你回答</h2>",
        table(["對方問", "你回答"], reply),
        "<h2>喜好與語言補充</h2>",
        table(["中文", "日文"], likes),
        '<div class="tip"><strong>用法提醒：</strong>喜歡用「が好きです」；會說語言用「が話せます」。四語並排見 <a href="../../tables/six-qa/">六類問答對照</a>。</div>',
        "",
    ])


def japanese_place():
    def j(say, kanji, hira, kata, roma):
        return ja(say, kanji, hira, kata, roma)

    rows = [
        tr("比利時", j("ベルギーに住んでいます。", "ベルギーに住んでいます。", "ベルギー に すんでいます。", "ベルギー ニ スンデイマス。", "Berugii ni sunde imasu."), j("ベルギーが好きです。", "ベルギーが好きです。", "ベルギー が すき です。", "ベルギー ガ スキ デス。", "Berugii ga suki desu.")),
        tr("荷蘭", j("オランダに住んでいます。", "オランダに住んでいます。", "オランダ に すんでいます。", "オランダ ニ スンデイマス。", "Oranda ni sunde imasu."), j("オランダが好きです。", "オランダが好きです。", "オランダ が すき です。", "オランダ ガ スキ デス。", "Oranda ga suki desu.")),
        tr("奧地利", j("オーストリアに住んでいます。", "オーストリアに住んでいます。", "オーストリア に すんでいます。", "オーストリア ニ スンデイマス。", "Oosutoria ni sunde imasu."), j("オーストリアが好きです。", "オーストリアが好きです。", "オーストリア が すき です。", "オーストリア ガ スキ デス。", "Oosutoria ga suki desu.")),
        tr("日本", j("日本に住んでいます。", "日本に住んでいます。", "にほん に すんでいます。", "ニホン ニ スンデイマス。", "Nihon ni sunde imasu."), j("日本が好きです。", "日本が好きです。", "にほん が すき です。", "ニホン ガ スキ デス。", "Nihon ga suki desu.")),
        tr("臺灣", j("台湾に住んでいます。", "台湾に住んでいます。", "たいわん に すんでいます。", "タイワン ニ スンデイマス。", "Taiwan ni sunde imasu."), j("台湾が好きです。", "台湾が好きです。", "たいわん が すき です。", "タイワン ガ スキ デス。", "Taiwan ga suki desu.")),
        tr("臺北", j("台北に住んでいます。", "台北に住んでいます。", "たいぺい に すんでいます。", "タイペイ ニ スンデイマス。", "Taipei ni sunde imasu."), j("台北が好きです。", "台北が好きです。", "たいぺい が すき です。", "タイペイ ガ スキ デス。", "Taipei ga suki desu.")),
    ]
    return "\n".join([
        f"<!-- {MARK} -->",
        "<h2>住在與喜歡</h2>",
        '<p class="note">住在哪裡用「に住んでいます」。喜歡用「が好きです」。兩者助詞不同。</p>',
        table(["地點", "住在", "喜歡"], rows),
        "",
    ])


def patch_indexes():
    cards = {
        ROOT / "fr" / "index.html": (
            "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（rêver de）。",
            "六類口說問答（國籍、年齡、電話、喜好、語言、居住），以及 habiter 變位。",
        ),
        ROOT / "en" / "index.html": (
            "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（dream of）。",
            "六類口說問答（國籍、年齡、電話、喜好、語言、居住），以及 live 變位。",
        ),
        ROOT / "de" / "index.html": (
            "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（träumen von）。",
            "六類口說問答（國籍、年齡、電話、喜好、語言、居住），以及 wohnen 變位。",
        ),
        ROOT / "ja" / "index.html": (
            "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想。",
            "六類口說問答（國籍、年齡、電話、喜好、語言、居住），以及住んでいます。",
        ),
    }
    for path, (old, new) in cards.items():
        text = read(path)
        if new in text:
            print("index ok", path.name)
            continue
        if old not in text:
            print("index skip", path.name)
            continue
        write(path, text.replace(old, new, 1))
        print("index", path.relative_to(ROOT))
    # verbes-er card
    fr_index = ROOT / "fr" / "index.html"
    text = read(fr_index)
    old = "parler、manger、acheter 的現在式，附例句、中文、朗讀與 PDF。"
    new = "habiter、parler、aimer、manger、acheter 的現在式，附例句、中文、朗讀與 PDF。"
    if old in text and new not in text:
        write(fr_index, text.replace(old, new, 1))
        print("index verbes-er")


def write_comparison():
    path = ROOT / "tables" / "six-qa" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    def e(s):
        return f'<button type="button" class="say en" data-say="{s}" data-lang="en-US"><span class="word">{s}</span></button>'

    def f(s):
        return f'<button type="button" class="say fr" data-say="{s}" data-lang="fr-FR"><span class="word">{s}</span></button>'

    def d(s):
        return f'<button type="button" class="say de" data-say="{s}" data-lang="de-DE"><span class="word">{s}</span></button>'

    def j(say, kanji, hira, kata, roma):
        return (
            f'<button type="button" class="say ja" data-say="{say}" data-lang="ja-JP">'
            f'<span class="word">{kanji}</span>'
            f'<span class="sub"><span class="hira">{hira}</span>　<span class="kata">{kata}</span></span>'
            f'<span class="roma">{roma}</span></button>'
        )

    def row(zh, cells):
        return (
            '<tr class="vocab-row"><td class="zh">'
            + zh
            + "</td>"
            + "".join(f"<td>{c}</td>" for c in cells)
            + "</tr>"
        )

    qa = [
        ("國籍？", e("What nationality are you?"), f(f"Vous êtes de quelle nationalité ?"), d("Welche Nationalität haben Sie?"), j("どの国の人ですか。", "どの国の人ですか。", "どの くに の ひと ですか。", "ドノ クニ ノ ヒト デスカ。", "Dono kuni no hito desu ka.")),
        ("國籍答", e("I'm Taiwanese."), f("Je suis taïwanais."), d("Ich bin Taiwaner."), j("台湾人です。", "台湾人です。", "たいわんじん です。", "タイワンジン デス。", "Taiwanjin desu.")),
        ("年齡？", e("How old are you?"), f("Vous avez quel âge ?"), d("Wie alt sind Sie?"), j("何歳ですか。", "何歳ですか。", "なんさい ですか。", "ナンサイ デスカ。", "Nansai desu ka.")),
        ("年齡答", e("I'm thirty-three."), f(f"J{Q}ai trente-trois ans."), d("Ich bin dreiunddreißig Jahre alt."), j("三十三歳です。", "三十三歳です。", "さんじゅうさんさい です。", "サンジュウサンサイ デス。", "Sanjuusansai desu.")),
        ("電話？", e("What's your phone number?"), f(f"Quel est votre numéro de téléphone ?"), d("Wie ist Ihre Telefonnummer?"), j("電話番号は何番ですか。", "電話番号は何番ですか。", "でんわばんごう は なんばん ですか。", "デンワバンゴウ ハ ナンバン デスカ。", "Denwa bangou wa nanban desu ka.")),
        ("喜好？", e("What do you like?"), f(f"Qu{Q}est-ce que vous aimez ?"), d("Was mögen Sie?"), j("何が好きですか。", "何が好きですか。", "なに が すき ですか。", "ナニ ガ スキ デスカ。", "Nani ga suki desu ka.")),
        ("喜好答", e("I like traveling."), f(f"J{Q}aime voyager."), d("Ich mag Reisen."), j("旅行が好きです。", "旅行が好きです。", "りょこう が すき です。", "リョコウ ガ スキ デス。", "Ryokou ga suki desu.")),
        ("語言？", e("What languages do you speak?"), f("Vous parlez quelles langues ?"), d("Welche Sprachen sprechen Sie?"), j("何語が話せますか。", "何語が話せますか。", "なにご が はなせますか。", "ナニゴ ガ ハナセマスカ。", "Nanigo ga hanasemasu ka.")),
        ("語言答", e("I speak Chinese and English."), f("Je parle chinois et anglais."), d("Ich spreche Chinesisch und Englisch."), j("中国語と英語が話せます。", "中国語と英語が話せます。", "ちゅうごくご と えいご が はなせます。", "チュウゴクゴ ト エイゴ ガ ハナセマス。", "Chuugokugo to eigo ga hanasemasu.")),
        ("居住？", e("Where do you live?"), f("Vous habitez où ?"), d("Wo wohnen Sie?"), j("どこに住んでいますか。", "どこに住んでいますか。", "どこ に すんでいますか。", "ドコ ニ スンデイマスカ。", "Doko ni sunde imasu ka.")),
        ("居住答", e("I live in Taipei."), f(f"J{Q}habite à Taipei."), d("Ich wohne in Taipeh."), j("台北に住んでいます。", "台北に住んでいます。", "たいぺい に すんでいます。", "タイペイ ニ スンデイマス。", "Taipei ni sunde imasu.")),
    ]
    verbs = [
        ("我住", e("I live"), f(f"j{Q}habite"), d("ich wohne"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
        ("你住", e("you live"), f("tu habites"), d("du wohnst"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
        ("他住", e("he lives"), f("il habite"), d("er wohnt"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
        ("我們住", e("we live"), f("nous habitons"), d("wir wohnen"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
        ("您住", e("you live"), f("vous habitez"), d("Sie wohnen"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
        ("他們住", e("they live"), f("ils habitent"), d("sie wohnen"), j("住んでいます", "住んでいます", "すんでいます", "スンデイマス", "sunde imasu")),
    ]
    place = [
        ("住在比利時", e("I live in Belgium."), f(f"J{Q}habite en Belgique."), d("Ich wohne in Belgien."), j("ベルギーに住んでいます。", "ベルギーに住んでいます。", "ベルギー に すんでいます。", "ベルギー ニ スンデイマス。", "Berugii ni sunde imasu.")),
        ("喜歡比利時", e("I like Belgium."), f(f"J{Q}aime la Belgique."), d("Ich mag Belgien."), j("ベルギーが好きです。", "ベルギーが好きです。", "ベルギー が すき です。", "ベルギー ガ スキ デス。", "Berugii ga suki desu.")),
        ("住在荷蘭", e("I live in the Netherlands."), f(f"J{Q}habite aux Pays-Bas."), d("Ich wohne in den Niederlanden."), j("オランダに住んでいます。", "オランダに住んでいます。", "オランダ に すんでいます。", "オランダ ニ スンデイマス。", "Oranda ni sunde imasu.")),
        ("住在奧地利", e("I live in Austria."), f(f"J{Q}habite en Autriche."), d("Ich wohne in Österreich."), j("オーストリアに住んでいます。", "オーストリアに住んでいます。", "オーストリア に すんでいます。", "オーストリア ニ スンデイマス。", "Oosutoria ni sunde imasu.")),
        ("住在臺灣臺北", e("I live in Taipei, Taiwan."), f(f"J{Q}habite à Taipei, à Taïwan."), d("Ich wohne in Taipeh, in Taiwan."), j("台湾の台北に住んでいます。", "台湾の台北に住んでいます。", "たいわん の たいぺい に すんでいます。", "タイワン ノ タイペイ ニ スンデイマス。", "Taiwan no Taipei ni sunde imasu.")),
    ]
    head = (
        '<thead><tr><th scope="col">中文</th><th scope="col" class="th-en">英文</th>'
        '<th scope="col" class="th-fr">法文</th><th scope="col" class="th-de">德文</th>'
        '<th scope="col" class="th-ja">日文</th></tr></thead>'
    )

    def section(sid, title, note, items):
        body = "\n".join(row(zh, [a, b, c, d_]) for zh, a, b, c, d_ in items)
        return (
            f'<section id="{sid}"><h2>{title}</h2><p class="note">{note}</p>'
            f'<div class="tablewrap"><table>{head}<tbody>\n{body}\n</tbody></table></div></section>'
        )

    html = f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="六類口說問答與居住動詞：英、法、德、日並排對照。">
<title>六類問答對照｜四語筆記</title>
<style>
:root{{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:#f2f5fa}}
*{{box-sizing:border-box}}
body{{margin:0}}
header{{background:#445a7a;color:white;padding:22px max(20px,calc((100vw - 1180px)/2))}}
header .brand{{font-size:1.35rem;font-weight:800}}
header a{{color:inherit;text-decoration:none}}
main{{max-width:1180px;margin:auto;padding:32px 20px 70px}}
h1{{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}}
h2{{font-size:1.25rem;margin:32px 0 12px}}
p{{line-height:1.7;color:#53647c}}
.note{{font-size:.92rem;color:#52647d;margin:0 0 18px}}
.toc{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}}
.toc a{{display:inline-block;padding:7px 12px;border-radius:9px;background:white;border:1px solid #dae3ef;color:#445a7a;text-decoration:none;font-weight:650;font-size:.92rem}}
.controls{{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid #dae3ef;border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}}
.controls-row{{display:flex;flex-wrap:wrap;gap:12px;align-items:center}}
.ctrl{{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:#445a7a;color:white}}
.ctrl.stop{{background:#5c6675}}
.rate,.loop{{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}}
.rate input{{width:140px}}
.status{{margin-top:10px;font-size:.9rem;color:#6a5870}}
.tablewrap{{overflow-x:auto;background:white;border:1px solid #dae3ef;border-radius:14px;box-shadow:0 6px 18px #142f520c}}
table{{border-collapse:collapse;width:100%;min-width:980px}}
th{{background:#eef2f7;text-align:left;font-size:.9rem;padding:12px}}
.th-en{{color:#17355d}}.th-fr{{color:#b3482f}}.th-de{{color:#1d6a4f}}.th-ja{{color:#8d3a55}}
td{{padding:10px 12px;border-top:1px solid #e6edf5;vertical-align:top}}
.zh{{color:#53647c;font-weight:650;white-space:nowrap}}
.say{{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 2px;border-radius:8px}}
.say .word{{font-size:1.02rem;font-weight:750}}
.say.en,.th-en{{color:#17355d}}.say.fr,.th-fr{{color:#b3482f}}.say.de,.th-de{{color:#1d6a4f}}.say.ja,.th-ja{{color:#8d3a55}}
.sub{{font-size:.88rem;color:#3d4d63}}.roma{{font-size:.8rem;color:#6a5870}}
.vocab-row.active{{background:#fff4d8}}
.tip{{background:white;border-left:4px solid #445a7a;padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid #dae3ef;border-left-width:4px;line-height:1.7;color:#52647a}}
.tip a{{color:#445a7a;font-weight:650}}
footer{{max-width:1180px;margin:auto;padding:20px;color:#627087;font-size:.9rem}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 對表</a>　/　六類問答</div></header>
<main>
<h1>六類問答對照</h1>
<p class="note">國籍、年齡、電話、喜好、語言、居住，以及「住」的動詞。法文 habiter 是 -er 規則動詞；英文 he／she 用 lives；德文 wohnen；日文常用住んでいます。</p>
<nav class="toc"><a href="#qa">六類問答</a><a href="#verbs">居住動詞</a><a href="#place">住在／喜歡</a></nav>
<div class="controls">
  <div class="controls-row">
    <button type="button" id="play-all" class="ctrl">▶ 全部循環播放</button>
    <button type="button" id="stop-all" class="ctrl stop">■ 停止</button>
    <label class="rate">語速 <input id="rate" type="range" min="0.5" max="1.4" step="0.1" value="0.9"> <span id="rate-label">0.9</span></label>
    <label class="loop"><input id="loop" type="checkbox" checked> 播完從頭再播</label>
  </div>
  <div id="play-status" class="status">待命</div>
</div>
{section("qa", "六類問答", "法文跟老師練習可先統一用 vous。年齡：法文用 avoir，英文／德文用 be／sein，日文用歳です。", qa)}
{section("verbs", "居住動詞", "法文 on habite 仍是第三人稱單數。英文只有 he／she／it 加 s。", verbs)}
{section("place", "住在與喜歡", "法文住在用 en／au／aux／à，喜歡用定冠詞。英文住在與喜歡的國名介詞用法不同於法文。", place)}
<div class="tip"><strong>單語頁：</strong>
<a href="../../fr/dialogue-a1/">法文對話</a>、
<a href="../../fr/verbes-er/">法文 -er 動詞</a>、
<a href="../../fr/pays-prepositions/">法文地點</a>；
<a href="../../en/dialogue-a1/">英文</a>、
<a href="../../de/dialogue-a1/">德文</a>、
<a href="../../ja/dialogue-a1/">日文</a>。</div>
</main>
<footer>六類問答對照｜英・法・德・日</footer>
<script>
const rateInput=document.getElementById('rate'),rateLabel=document.getElementById('rate-label'),loopBox=document.getElementById('loop'),statusEl=document.getElementById('play-status');
let queue=[],index=0,playing=false;
function voicesReady(cb){{if(!('speechSynthesis' in window)){{alert('此瀏覽器不支援語音播放。');return;}}if(speechSynthesis.getVoices().length){{cb();return;}}speechSynthesis.addEventListener('voiceschanged',()=>cb(),{{once:true}});setTimeout(cb,300);}}
function pickVoice(lang){{const p=lang.toLowerCase().replace('_','-').slice(0,2);return speechSynthesis.getVoices().find(v=>v.lang.toLowerCase().replace('_','-').startsWith(p));}}
function speakOnce(text,lang,rate,onend){{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(text);u.lang=lang;u.rate=rate;const v=pickVoice(lang);if(v)u.voice=v;u.onend=()=>{{if(onend)onend();}};u.onerror=()=>{{if(onend)onend();}};speechSynthesis.speak(u);}}
function clearActive(){{document.querySelectorAll('.vocab-row.active').forEach(r=>r.classList.remove('active'));}}
function setStatus(t){{if(statusEl)statusEl.textContent=t;}}
function stopAll(){{playing=false;queue=[];index=0;if('speechSynthesis' in window)speechSynthesis.cancel();clearActive();setStatus('已停止');}}
function playNext(){{if(!playing)return;if(index>=queue.length){{if(loopBox&&loopBox.checked&&queue.length){{index=0;}}else{{stopAll();setStatus('播放完畢');return;}}}}const item=queue[index];clearActive();const row=item.el.closest('.vocab-row');if(row){{row.classList.add('active');row.scrollIntoView({{block:'nearest',behavior:'auto'}});}}setStatus('播放中：'+item.text+'（'+(index+1)+' / '+queue.length+'）');speakOnce(item.text,item.lang,parseFloat(rateInput.value)||0.9,()=>{{if(!playing)return;index+=1;setTimeout(playNext,180);}});}}
rateInput.addEventListener('input',()=>{{rateLabel.textContent=parseFloat(rateInput.value).toFixed(1);}});rateLabel.textContent=parseFloat(rateInput.value).toFixed(1);
document.getElementById('play-all').addEventListener('click',()=>{{voicesReady(()=>{{playing=true;queue=[...document.querySelectorAll('[data-say]')].map(el=>({{text:el.dataset.say,lang:el.dataset.lang,el}}));index=0;playNext();}});}});
document.getElementById('stop-all').addEventListener('click',stopAll);
document.addEventListener('click',e=>{{const b=e.target.closest('[data-say]');if(!b||e.target.closest('.controls'))return;voicesReady(()=>{{playing=false;queue=[];speechSynthesis.cancel();clearActive();const row=b.closest('.vocab-row');if(row)row.classList.add('active');setStatus('單句：'+b.dataset.say);speakOnce(b.dataset.say,b.dataset.lang,parseFloat(rateInput.value)||0.9,()=>{{clearActive();setStatus('待命');}});}});}});
if('speechSynthesis' in window)speechSynthesis.getVoices();
</script>
</body>
</html>
'''
    write(path, html)
    print(path, path.stat().st_size)

    tables_index = ROOT / "tables" / "index.html"
    text = read(tables_index)
    if 'href="./six-qa/"' in text:
        print("tables index ok")
        return
    card = '''<article class="item">
<div class="meta">課堂 · 六類問答 · 跟讀</div>
<h3>六類問答對照</h3>
<div class="langs">
<span class="en">EN</span>
<span class="de">DE</span>
<span class="fr">FR</span>
<span class="ja">JA</span>
</div>
<p>國籍、年齡、電話、喜好、語言、居住，以及「住」的動詞；住在與喜歡的介詞對照。</p>
<a class="button" href="./six-qa/">進入六類問答對照 →</a>
</article>
'''
    marker = '<h2>比較清單</h2>'
    pos = text.find(marker)
    if pos < 0:
        raise SystemExit("tables index marker missing")
    insert_at = pos + len(marker)
    write(tables_index, text[:insert_at] + "\n" + card + text[insert_at:])
    print("tables index")


def rebuild_verbes_er():
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_fr_grammar as b
    lesson = next(x for x in b.LESSONS if x.get("slug") == "verbes-er")
    idx = b.LESSONS.index(lesson)
    prev_lesson = b.LESSONS[idx - 1] if idx else None
    next_lesson = b.LESSONS[idx + 1] if idx + 1 < len(b.LESSONS) else None
    b.require_glyphs([lesson])
    b.write_html(lesson, prev_lesson, next_lesson)
    b.render_pdf(lesson)
    # refresh card text on index via write_index would rewrite whole index - skip, patch_indexes handles card
    print("rebuilt verbes-er")


def main():
    insert_before(ROOT / "fr" / "dialogue-a1" / "index.html", "</main>", french_dialogue())
    insert_before(ROOT / "fr" / "pays-prepositions" / "index.html", "</main>", french_place())
    insert_before(ROOT / "en" / "dialogue-a1" / "index.html", "</main>", english_dialogue())
    insert_before(ROOT / "en" / "pays-prepositions" / "index.html", "</main>", english_place())
    insert_before(ROOT / "de" / "dialogue-a1" / "index.html", "</main>", german_dialogue())
    insert_before(ROOT / "de" / "pays-prepositions" / "index.html", "</main>", german_place())
    insert_before(ROOT / "ja" / "dialogue-a1" / "index.html", "</main>", japanese_dialogue())
    insert_before(ROOT / "ja" / "pays-prepositions" / "index.html", "</main>", japanese_place())
    write_comparison()
    patch_indexes()
    rebuild_verbes_er()


if __name__ == "__main__":
    main()
