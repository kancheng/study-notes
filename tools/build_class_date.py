# -*- coding: utf-8 -*-
"""課堂日期、quel、個人問句、à/en/dans：寫入四語現有專題，並產生對照頁。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q = "\u2019"
MARK = "lesson-class-2026"


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(path, old, new):
    text = read(path)
    if new in text:
        print("already", path.relative_to(ROOT))
        return
    if old not in text:
        raise SystemExit(f"missing in {path}: {old[:90]!r}")
    if text.count(old) != 1:
        raise SystemExit(f"not unique in {path}: {old[:90]!r}")
    write(path, text.replace(old, new, 1))
    print("patched", path.relative_to(ROOT))


def insert_before(path, needle, block):
    text = read(path)
    if MARK in text:
        print("skip insert", path.relative_to(ROOT))
        return
    pos = text.rfind(needle) if needle == "</main>" else text.find(needle)
    if pos < 0:
        raise SystemExit(f"{needle!r} missing in {path}")
    write(path, text[:pos] + block + "\n" + text[pos:])
    print("inserted", path.relative_to(ROOT))


def replace_between(path, start, end, middle):
    text = read(path)
    if MARK in text:
        print("skip between", path.relative_to(ROOT))
        return
    i = text.find(start)
    j = text.find(end, i + len(start) if i >= 0 else 0)
    if i < 0 or j < 0:
        raise SystemExit(f"bounds missing in {path}")
    write(path, text[:i] + middle + text[j:])
    print("replaced block", path.relative_to(ROOT))


def btn(lang, code, say, inner=None):
    shown = say if inner is None else inner
    return (
        f'<button type="button" class="say" lang="{lang}" data-say="{say}" data-lang="{code}">'
        f'<span class="word">{shown}</span></button>'
    )


def fr(say):
    return btn("fr", "fr-FR", say)


def en(say, shown=None):
    return btn("en", "en-US", say, shown)


def de(say):
    return btn("de", "de-DE", say)


def ja(say, kanji, hira, kata, roma):
    return (
        '<button type="button" class="say" lang="ja" data-say="' + say + '" data-lang="ja-JP">'
        f'<span class="kanji">{kanji}</span>'
        f'<span class="kana"><span class="hira">{hira}</span>　<span class="kata">{kata}</span></span>'
        f'<span class="roma">{roma}</span></button>'
    )


def table(headers, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = "\n".join(rows)
    return (
        '<div class="tablewrap"><table><thead><tr>'
        + th
        + "</tr></thead><tbody>\n"
        + body
        + "\n</tbody></table></div>"
    )


def tr(*cells):
    tds = []
    for i, cell in enumerate(cells):
        cls = ' class="zh"' if i == 0 else ""
        tds.append(f"<td{cls}>{cell}</td>")
    return '<tr class="vocab-row">' + "".join(tds) + "</tr>"


def block(title, note, headers, rows, tip=None):
    parts = [f"<!-- {MARK} -->", f"<h2>{title}</h2>"]
    if note:
        parts.append(f'<p class="note">{note}</p>')
    parts.append(table(headers, rows))
    if tip:
        parts.append(f'<div class="tip"><strong>用法提醒：</strong>{tip}</div>')
    return "\n".join(parts) + "\n"


def patch_french_date():
    path = ROOT / "fr" / "date-quel" / "index.html"
    replace_once(
        path,
        f"日常口語問「今天幾號／星期幾」。<em>quel jour</em> 依上下文可問日期或星期。",
        f"星期和日期要分開問。<em>quel jour</em> 只問星期幾；<em>quelle date</em> 才問幾月幾日。",
    )
    replace_once(path, "今天星期幾／今天是幾號？（口語）", "今天星期幾？（口語）")
    replace_once(path, "今天是哪一天？", "今天星期幾？（另一種口語）")
    old_row = (
        "<tr class=\"vocab-row\"><td class=\"zh\">今天是幾月幾日？（較明確）</td>"
        "<td><button type=\"button\" class=\"say\" lang=\"fr\" "
        f"data-say=\"Quelle est la date aujourd{Q}hui ?\" data-lang=\"fr-FR\">"
        f"<span class=\"word\">Quelle est la date aujourd{Q}hui ?</span></button></td></tr>"
    )
    new_row = old_row + "\n" + tr(
        "今天幾月幾日？",
        fr(f"Quelle est la date d{Q}aujourd{Q}hui ?"),
    )
    replace_once(path, old_row, new_row)
    replace_once(
        path,
        f"<em>on</em>＝人們／我們（日期用 on est…）；<em>c{Q}est</em>＝這是；"
        f"<em>quel</em> 配合陽性單數 <em>jour</em>；<em>quelle</em> 配合陰性單數 <em>date</em>。",
        f"<em>on</em> 在這裡是口語的「我們／現在」。<em>est</em> 是 être 的現在式。"
        f"<em>quel</em> 配合陽性單數 <em>jour</em>；<em>quelle</em> 配合陰性單數 <em>date</em>。"
        f"<em>d{Q}aujourd{Q}hui</em> 是 de + aujourd{Q}hui。",
    )
    replace_once(
        path,
        f"日期結構：<strong>le + 日 + 月</strong>（日在前）。一日用序數 <em>premier</em>；"
        f"其餘日子多用基數，如 <em>le deux octobre</em>。月份、星期一般<strong>不大寫</strong>。",
        "書寫是 <strong>le + 日期 + 月份 + 年份</strong>。只有每月 1 日用 <em>premier</em>，"
        "其他日期用基數，而且前面要有 <em>le</em>。<em>mille</em> 不加 s。"
        "星期和月份通常小寫，例如 jeudi、octobre。",
    )
    replace_once(
        path,
        f"手寫稿亦寫 <em>Aujourd{Q}hui, c{Q}est le 1er octobre.</em>（<em>1er</em> 讀 <em>premier</em>）。"
        f"問年齡用 <em>Tu as quel âge ?</em>（<em>quel</em>＋<em>âge</em> 陽性）；"
        f"問國籍用 <em>de quelle nationalité</em>（<em>quelle</em>＋<em>nationalité</em> 陰性）。",
        f"1 日寫成 <em>1er</em>、讀 <em>premier</em>。問女生幾歲仍說 <em>Quel âge… ?</em>，"
        f"因為看的是名詞 <em>âge</em> 的性別，不是被問的人。國籍名詞 <em>nationalité</em> 是陰性，用 <em>quelle</em>。",
    )
    rows = [
        tr("日、天", "陽性單數", fr("quel jour")),
        tr("國家", "陽性單數", fr("quel pays")),
        tr("年齡", "陽性單數", fr("quel âge")),
        tr("日期", "陰性單數", fr("quelle date")),
        tr("城市", "陰性單數", fr("quelle ville")),
        tr("國籍", "陰性單數", fr("quelle nationalité")),
        tr("國家", "陽性複數", fr("quels pays")),
        tr("城市", "陰性複數", fr("quelles villes")),
        tr("問女生幾歲，仍看名詞", "âge 陽性", fr("Quel âge a-t-elle ?")),
    ]
    middle = "\n".join([
        f"<!-- {MARK} -->",
        "<h2>日期怎麼讀</h2>",
        "<p class=\"note\">以下是課堂日期。十月一日已在上一表；這裡補六日、八日，以及完整年份。</p>",
        table(["中文", "法文"], [
            tr("今天星期四。", fr("On est jeudi.")),
            tr("今天是十月六日。", fr(f"Aujourd{Q}hui, c{Q}est le six octobre.")),
            tr("今天是十月八日。", fr(f"Aujourd{Q}hui, c{Q}est le huit octobre.")),
            tr("今天是 2026 年 10 月 8 日。", fr(f"Aujourd{Q}hui, c{Q}est le huit octobre deux mille vingt-six.")),
        ]),
        "<h2>quel／quelle／quels／quelles</h2>",
        "<p class=\"note\">這四個形式都是「哪一個／哪些」，發音相同，要配合<strong>名詞</strong>的性別與數量。單數陽性 quel、陰性 quelle；複數陽性 quels、陰性 quelles。</p>",
        table(["名詞", "性別與數量", "搭配"], rows),
        "",
    ])
    replace_between(path, "<h2>疑問限定詞 quel</h2>", "<h2>星期速查</h2>", middle)


def patch_notes():
    replace_once(
        ROOT / "de" / "date-quel" / "index.html",
        "口語也常簡單問 <em>Welcher Tag ist heute?</em>（可指日期或星期，依上下文）。",
        "口語 <em>Welcher Tag ist heute?</em> 有時分不清。星期用 <em>Welcher Wochentag ist heute?</em>，月日用 <em>Welches Datum haben wir heute?</em>。",
    )
    replace_once(
        ROOT / "de" / "date-quel" / "index.html",
        "朗讀日期時 <em>1.</em> 讀 <em>erste</em>。月份、星期為名詞，書寫時首字母大寫。",
        "德文每個日期都用序數：1. 讀 erste，6. 讀 sechste，8. 讀 achte。月份、星期首字母大寫。",
    )
    replace_once(
        ROOT / "ja" / "date-quel" / "index.html",
        "一日讀 <strong>ついたち</strong>，其他日子多用 <strong>〜日</strong>（にち／か）。",
        "一日讀 <strong>ついたち</strong>，六日讀 <strong>むいか</strong>，八日讀 <strong>ようか</strong>。",
    )


def french_dialogue():
    rows = [
        tr("Paul 的國籍是什麼？", fr("Quelle est la nationalité de Paul ?")),
        tr("Paul 是法國人。（範例）", fr("Paul est français.")),
        tr("他是法國人。", fr("Il est français.")),
        tr("Paul 三十二歲。（範例）", fr("Paul a trente-deux ans.")),
        tr("我三十二歲。", fr(f"J{Q}ai trente-deux ans.")),
        tr("他三十二歲。", fr("Il a trente-deux ans.")),
        tr("Paul 夢想什麼？", fr("Paul rêve de quoi ?")),
        tr("Paul 夢想去旅行。", fr("Paul rêve de voyager.")),
        tr("他夢想去旅行。", fr("Il rêve de voyager.")),
    ]
    return block(
        "國籍、年齡與夢想",
        "上方已有口語問法。這裡補另一種國籍問句、範例回答，以及 rêver de。年齡用 avoir，不是 être。筆記若寫成 Paul a rêve quoi，要改成 Paul rêve de quoi。",
        ["中文", "法文"],
        rows,
        f"rêver de 後面接名詞或動詞原形，例如 rêve de voyager。喜好仍用上方的 aimer；夢想用 rêver。四語並排見 <a href=\"../../tables/date-place/\">日期與地點對照</a>。",
    )


def french_place():
    place = [
        tr("城市", "à", fr("à Barcelone")),
        tr("城市", "à", fr("à Paris")),
        tr("陰性國家", "en", fr("en Espagne")),
        tr("陰性國家", "en", fr("en France")),
        tr("母音開頭的陽性國家", "en", fr("en Iran")),
        tr("子音開頭的陽性國家", "au", fr("au Japon")),
        tr("子音開頭的陽性國家", "au", fr("au Canada")),
        tr("複數國家", "aux", fr("aux États-Unis")),
    ]
    move = [
        tr("開車／搭汽車（方式）", fr("en voiture")),
        tr("在車裡（位置）", fr("dans la voiture")),
        tr("搭公車", fr("en bus")),
        tr("搭火車", fr("en train")),
        tr("搭地鐵", fr("en métro")),
        tr("搭飛機", fr("en avion")),
        tr("步行", fr("à pied")),
        tr("騎自行車", fr("à vélo")),
    ]
    ask = [
        tr("Ana 住在哪個國家？", fr("Ana habite dans quel pays ?")),
        tr("Ana 住在哪座城市？", fr("Ana habite dans quelle ville ?")),
        tr("Ana 住在西班牙的巴塞隆納。", fr(f"Ana habite en Espagne, à Barcelone.")),
        tr("她住在西班牙。", fr("Elle habite en Espagne.")),
        tr("她住在巴塞隆納。", fr("Elle habite à Barcelone.")),
        tr("你怎麼去學校？", fr(f"Tu vas à l{Q}école comment ?")),
        tr("開車／搭汽車。", fr("En voiture.")),
        tr("我開車／搭汽車去學校。", fr(f"Je vais à l{Q}école en voiture.")),
        tr("鑰匙在哪裡？", fr("Où sont les clés ?")),
        tr("在車裡。", fr("Dans la voiture.")),
        tr("鑰匙在車裡。", fr("Les clés sont dans la voiture.")),
        tr("它們在車裡。", fr("Elles sont dans la voiture.")),
    ]
    return "\n".join([
        block(
            "問 Ana 住在哪裡",
            "問「哪個國家／哪座城市」用 dans quel／dans quelle。回答具體地名時，改用地名自己的介詞，例如 en Espagne、à Barcelone。",
            ["中文", "法文"],
            ask,
        ),
        "<h2>地名介詞</h2>",
        "<p class=\"note\">城市用 à。陰性國家，以及母音開頭的陽性國家，用 en。子音開頭的陽性國家用 au。複數國家用 aux。</p>",
        table(["類型", "介詞", "例子"], place),
        "<h2>en voiture 與 dans la voiture</h2>",
        "<p class=\"note\">en voiture 是交通方式，不一定表示自己開車，也可能是別人載。dans la voiture 是位置，表示在那輛車裡。où 是「哪裡」；沒有重音的 ou 是「或者」。</p>",
        table(["中文", "法文"], move),
        "<div class=\"tip\"><strong>先記這四組：</strong>quel jour／quelle date；年齡用 avoir；en Espagne／à Barcelone；en voiture／dans la voiture。四語並排見 <a href=\"../../tables/date-place/\">日期與地點對照</a>。</div>",
        "",
    ])


def english_date():
    rows = [
        tr("今天是十月六日。書寫 October 6th。", en("Today is October sixth.")),
        tr("今天是十月八日。書寫 October 8th。", en("Today is October eighth.")),
        tr("今天是 2026 年 10 月 8 日。", en("Today is October eighth, twenty twenty-six.", "Today is October eighth, twenty twenty-six.")),
    ]
    return block(
        "六日、八日與年份",
        "英文把月份放前面，1 日、2 日、3 日用 1st、2nd、3rd，其餘加 th。6 讀 sixth，8 讀 eighth。月份和星期要大寫。2026 年讀 twenty twenty-six。",
        ["中文", "英文"],
        rows,
        "What day 問星期，What's the date 問月日。英文的 which／what 不隨名詞性別變化。",
    )


def english_dialogue():
    rows = [
        tr("Paul 是什麼國籍？", en("What nationality is Paul?")),
        tr("Paul 的國籍是什麼？", en("What is Paul's nationality?")),
        tr("Paul 是法國人。（範例）", en("Paul is French.")),
        tr("Paul 三十二歲。", en("Paul is thirty-two.")),
        tr("Paul 三十二歲。（完整）", en("Paul is thirty-two years old.")),
        tr("我三十二歲。", en("I'm thirty-two.")),
        tr("Paul 夢想什麼？", en("What does Paul dream of?")),
        tr("Paul 夢想去旅行。", en("Paul dreams of traveling.")),
    ]
    return block(
        "國籍、年齡與夢想",
        "英文年齡用 be，不說 have thirty-two years。國籍形容詞 French 要大寫。夢想是 dream of，後面用 traveling。",
        ["中文", "英文"],
        rows,
    )


def english_place():
    ask = [
        tr("Ana 住在哪個國家？", en("Which country does Ana live in?")),
        tr("Ana 住在哪座城市？", en("Which city does Ana live in?")),
        tr("Ana 住在西班牙的巴塞隆納。", en("Ana lives in Spain, in Barcelona.")),
        tr("她住在西班牙。", en("She lives in Spain.")),
        tr("她住在巴塞隆納。", en("She lives in Barcelona.")),
        tr("你怎麼去學校？", en("How do you get to school?")),
        tr("開車／搭汽車。", en("By car.")),
        tr("我開車／搭汽車去學校。", en("I go to school by car.")),
        tr("鑰匙在哪裡？", en("Where are the keys?")),
        tr("在車裡。", en("In the car.")),
        tr("鑰匙在車裡。", en("The keys are in the car.")),
    ]
    move = [
        tr("開車／搭汽車（方式）", en("by car")),
        tr("在車裡（位置）", en("in the car")),
        tr("搭公車", en("by bus")),
        tr("搭火車", en("by train")),
        tr("搭地鐵", en("by subway")),
        tr("搭飛機", en("by plane")),
        tr("步行", en("on foot")),
        tr("騎自行車", en("by bike")),
    ]
    return "\n".join([
        block(
            "Ana 的國家、城市與車子",
            "英文的國家和城市都用 in。by car 是交通方式，可能是自己開，也可能是別人載。in the car 是在車裡。",
            ["中文", "英文"],
            ask,
        ),
        "<h2>交通方式</h2>",
        table(["中文", "英文"], move),
        "<div class=\"tip\"><strong>先記這四組：</strong>What day／What's the date；年齡用 be；in Spain／in Barcelona；by car／in the car。四語並排見 <a href=\"../../tables/date-place/\">日期與地點對照</a>。</div>",
        "",
    ])


def german_date():
    rows = [
        tr("今天是十月六日。書寫 6. Oktober。", de("Heute ist der sechste Oktober.")),
        tr("今天是十月八日。書寫 8. Oktober。", de("Heute ist der achte Oktober.")),
        tr("今天是 2026 年 10 月 8 日。", de("Heute ist der achte Oktober zweitausendsechsundzwanzig.")),
        tr("日期，陽性", de("welcher Tag")),
        tr("星期，陽性", de("welcher Wochentag")),
        tr("日期（月日），中性", de("welches Datum")),
        tr("城市，陰性", de("welche Stadt")),
        tr("國家，中性", de("welches Land")),
    ]
    return block(
        "六日、八日與 welcher",
        "德文每一天都用序數，不像法文只有 1 日用 premier。序數前面用陽性 der：der erste、der sechste、der achte。2026 讀 zweitausendsechsundzwanzig。welcher 要配合名詞的性別。",
        ["中文", "德文"],
        rows,
    )


def german_dialogue():
    rows = [
        tr("Paul 是什麼國籍？", de("Welche Nationalität hat Paul?")),
        tr("Paul 是法國人。（範例）", de("Paul ist Franzose.")),
        tr("Paul 三十二歲。", de("Paul ist zweiunddreißig Jahre alt.")),
        tr("我三十二歲。", de("Ich bin zweiunddreißig Jahre alt.")),
        tr("Paul 夢想什麼？", de("Wovon träumt Paul?")),
        tr("Paul 夢想去旅行。", de("Paul träumt davon, zu reisen.")),
    ]
    return block(
        "國籍、年齡與夢想",
        "德文年齡用 sein，說 Jahre alt。國籍用 Franzose；若是女性則說 Französin。夢想是 träumen von，問句常變成 wovon，回答用 davon。",
        ["中文", "德文"],
        rows,
    )


def german_place():
    ask = [
        tr("Ana 住在哪個國家？", de("In welchem Land wohnt Ana?")),
        tr("Ana 住在哪座城市？", de("In welcher Stadt wohnt Ana?")),
        tr("Ana 住在西班牙的巴塞隆納。", de("Ana wohnt in Spanien, in Barcelona.")),
        tr("她住在西班牙。", de("Sie wohnt in Spanien.")),
        tr("她住在巴塞隆納。", de("Sie wohnt in Barcelona.")),
        tr("你怎麼去學校？", de("Wie kommst du zur Schule?")),
        tr("開車／搭汽車。", de("Mit dem Auto.")),
        tr("我開車去學校。", de("Ich fahre mit dem Auto zur Schule.")),
        tr("鑰匙在哪裡？", de("Wo sind die Schlüssel?")),
        tr("在車裡。", de("Im Auto.")),
        tr("鑰匙在車裡。", de("Die Schlüssel sind im Auto.")),
    ]
    move = [
        tr("開車／搭汽車（方式）", de("mit dem Auto")),
        tr("在車裡（位置）", de("im Auto")),
        tr("搭公車", de("mit dem Bus")),
        tr("搭火車", de("mit dem Zug")),
        tr("搭地鐵", de("mit der U-Bahn")),
        tr("搭飛機", de("mit dem Flugzeug")),
        tr("步行", de("zu Fuß")),
        tr("騎自行車", de("mit dem Fahrrad")),
    ]
    places = [
        tr("城市", de("in Barcelona")),
        tr("多數國家，不加冠詞", de("in Spanien")),
        tr("多數國家，不加冠詞", de("in Frankreich")),
        tr("帶冠詞的陽性國家", de("im Iran")),
        tr("複數國家", de("in den USA")),
    ]
    return "\n".join([
        block(
            "Ana 的國家、城市與車子",
            "問地方用 in welchem Land、in welcher Stadt，介詞搭配第三格。多數國名不加冠詞：in Spanien。mit dem Auto 是交通方式；im Auto（in dem Auto）是在車裡。",
            ["中文", "德文"],
            ask,
        ),
        "<h2>地名</h2>",
        "<p class=\"note\">城市和多數國家都用 in。有冠詞的國名要變格，例如 im Iran、in den USA。這和法文的 en／au／à 不是一對一。</p>",
        table(["類型", "德文"], places),
        "<h2>交通方式</h2>",
        "<p class=\"note\">交通工具多用 mit + 第三格。U-Bahn 是陰性，所以說 mit der U-Bahn。步行是 zu Fuß。</p>",
        table(["中文", "德文"], move),
        "<div class=\"tip\"><strong>先記這四組：</strong>Wochentag／Datum；年齡用 sein；in Spanien／in Barcelona；mit dem Auto／im Auto。四語並排見 <a href=\"../../tables/date-place/\">日期與地點對照</a>。</div>",
        "",
    ])


def japanese_date():
    rows = [
        tr("今天是十月六日。", ja(
            "きょうはじゅうがつむいかです。",
            "今日は十月六日です。",
            "きょう は じゅうがつ むいか です。",
            "キョウ ハ ジュウガツ ムイカ デス。",
            "Kyou wa juugatsu muika desu.",
        )),
        tr("今天是十月八日。", ja(
            "きょうはじゅうがつようかです。",
            "今日は十月八日です。",
            "きょう は じゅうがつ ようか です。",
            "キョウ ハ ジュウガツ ヨウカ デス。",
            "Kyou wa juugatsu youka desu.",
        )),
        tr("今天是 2026 年 10 月 8 日。", ja(
            "きょうはにせんにじゅうろくねんじゅうがつようかです。",
            "今日は二千二十六年十月八日です。",
            "きょう は にせんにじゅうろくねん じゅうがつ ようか です。",
            "キョウ ハ ニセンニジュウロクネン ジュウガツ ヨウカ デス。",
            "Kyou wa nisen nijuurokunen juugatsu youka desu.",
        )),
        tr("一日", ja("ついたち", "一日", "ついたち", "ツイタチ", "tsuitachi")),
        tr("六日", ja("むいか", "六日", "むいか", "ムイカ", "muika")),
        tr("八日", ja("ようか", "八日", "ようか", "ヨウカ", "youka")),
        tr("十四日", ja("じゅうよっか", "十四日", "じゅうよっか", "ジュウヨッカ", "juuyokka")),
        tr("二十日", ja("はつか", "二十日", "はつか", "ハツカ", "hatsuka")),
        tr("二十四日", ja("にじゅうよっか", "二十四日", "にじゅうよっか", "ニジュウヨッカ", "nijuuyokka")),
    ]
    return block(
        "六日、八日與特別讀音",
        "日期的一日、六日、八日不按普通數字讀。朗讀這些日期時用平假名，避免八日被讀成はちにち。何日問日期，何曜日問星期。",
        ["中文", "日文"],
        rows,
    )


def japanese_dialogue():
    rows = [
        tr("Paul 是哪國人？", ja(
            "ポールは何人ですか。",
            "ポールは何人ですか。",
            "ポール は なにじん ですか。",
            "ポール ハ ナニジン デスカ。",
            "Pooru wa nanijin desu ka.",
        )),
        tr("Paul 是法國人。（範例）", ja(
            "ポールはフランス人です。",
            "ポールはフランス人です。",
            "ポール は フランスじん です。",
            "ポール ハ フランスジン デス。",
            "Pooru wa Furansujin desu.",
        )),
        tr("Paul 幾歲？", ja(
            "ポールは何歳ですか。",
            "ポールは何歳ですか。",
            "ポール は なんさい ですか。",
            "ポール ハ ナンサイ デスカ。",
            "Pooru wa nansai desu ka.",
        )),
        tr("Paul 三十二歲。", ja(
            "ポールは三十二歳です。",
            "ポールは三十二歳です。",
            "ポール は さんじゅうにさい です。",
            "ポール ハ サンジュウニサイ デス。",
            "Pooru wa sanjuunisai desu.",
        )),
        tr("我三十二歲。", ja(
            "私は三十二歳です。",
            "私は三十二歳です。",
            "わたし は さんじゅうにさい です。",
            "ワタシ ハ サンジュウニサイ デス。",
            "Watashi wa sanjuunisai desu.",
        )),
        tr("Paul 夢想什麼？", ja(
            "ポールは何を夢見ていますか。",
            "ポールは何を夢見ていますか。",
            "ポール は なに を ゆめみていますか。",
            "ポール ハ ナニ ヲ ユメミテイマスカ。",
            "Pooru wa nani o yumemite imasu ka.",
        )),
        tr("Paul 夢想去旅行。", ja(
            "ポールは旅行を夢見ています。",
            "ポールは旅行を夢見ています。",
            "ポール は りょこう を ゆめみています。",
            "ポール ハ リョコウ ヲ ユメミテイマス。",
            "Pooru wa ryokou o yumemite imasu.",
        )),
    ]
    return block(
        "國籍、年齡與夢想",
        "國籍用「何人」，回答用「フランス人です」。年齡用「何歳／歳です」，不是「有」。夢想用「何を夢見ていますか」。",
        ["中文", "日文"],
        rows,
    )


def japanese_place():
    ask = [
        tr("Ana 住在哪個國家？", ja(
            "アナはどの国に住んでいますか。",
            "アナはどの国に住んでいますか。",
            "アナ は どの くに に すんでいますか。",
            "アナ ハ ドノ クニ ニ スンデイマスカ。",
            "Ana wa dono kuni ni sunde imasu ka.",
        )),
        tr("Ana 住在哪座城市？", ja(
            "アナはどの都市に住んでいますか。",
            "アナはどの都市に住んでいますか。",
            "アナ は どの とし に すんでいますか。",
            "アナ ハ ドノ トシ ニ スンデイマスカ。",
            "Ana wa dono toshi ni sunde imasu ka.",
        )),
        tr("Ana 住在西班牙的巴塞隆納。", ja(
            "アナはスペインのバルセロナに住んでいます。",
            "アナはスペインのバルセロナに住んでいます。",
            "アナ は スペイン の バルセロナ に すんでいます。",
            "アナ ハ スペイン ノ バルセロナ ニ スンデイマス。",
            "Ana wa Supein no Baruserona ni sunde imasu.",
        )),
        tr("她住在西班牙。", ja(
            "アナはスペインに住んでいます。",
            "アナはスペインに住んでいます。",
            "アナ は スペイン に すんでいます。",
            "アナ ハ スペイン ニ スンデイマス。",
            "Ana wa Supein ni sunde imasu.",
        )),
        tr("她住在巴塞隆納。", ja(
            "アナはバルセロナに住んでいます。",
            "アナはバルセロナに住んでいます。",
            "アナ は バルセロナ に すんでいます。",
            "アナ ハ バルセロナ ニ スンデイマス。",
            "Ana wa Baruserona ni sunde imasu.",
        )),
        tr("你怎麼去學校？", ja(
            "学校へはどうやって行きますか。",
            "学校へはどうやって行きますか。",
            "がっこう へ は どうやって いきますか。",
            "ガッコウ ヘ ハ ドウヤッテ イキマスカ。",
            "Gakkou e wa douyatte ikimasu ka.",
        )),
        tr("開車／搭汽車。", ja(
            "車で行きます。",
            "車で行きます。",
            "くるま で いきます。",
            "クルマ デ イキマス。",
            "Kuruma de ikimasu.",
        )),
        tr("我開車／搭汽車去學校。", ja(
            "私は車で学校へ行きます。",
            "私は車で学校へ行きます。",
            "わたし は くるま で がっこう へ いきます。",
            "ワタシ ハ クルマ デ ガッコウ ヘ イキマス。",
            "Watashi wa kuruma de gakkou e ikimasu.",
        )),
        tr("鑰匙在哪裡？", ja(
            "鍵はどこですか。",
            "鍵はどこですか。",
            "かぎ は どこ ですか。",
            "カギ ハ ドコ デスカ。",
            "Kagi wa doko desu ka.",
        )),
        tr("在車裡。", ja(
            "車の中にあります。",
            "車の中にあります。",
            "くるま の なか に あります。",
            "クルマ ノ ナカ ニ アリマス。",
            "Kuruma no naka ni arimasu.",
        )),
        tr("鑰匙在車裡。", ja(
            "鍵は車の中にあります。",
            "鍵は車の中にあります。",
            "かぎ は くるま の なか に あります。",
            "カギ ハ クルマ ノ ナカ ニ アリマス。",
            "Kagi wa kuruma no naka ni arimasu.",
        )),
    ]
    move = [
        tr("開車／搭汽車（方式）", ja("車で", "車で", "くるま で", "クルマ デ", "kuruma de")),
        tr("在車裡（位置）", ja("車の中に", "車の中に", "くるま の なか に", "クルマ ノ ナカ ニ", "kuruma no naka ni")),
        tr("搭公車", ja("バスで", "バスで", "バス で", "バス デ", "basu de")),
        tr("搭火車", ja("電車で", "電車で", "でんしゃ で", "デンシャ デ", "densha de")),
        tr("搭地鐵", ja("地下鉄で", "地下鉄で", "ちかてつ で", "チカテツ デ", "chikatetsu de")),
        tr("搭飛機", ja("飛行機で", "飛行機で", "ひこうき で", "ヒコウキ デ", "hikouki de")),
        tr("步行", ja("歩いて", "歩いて", "あるいて", "アルイテ", "aruite")),
        tr("騎自行車", ja("自転車で", "自転車で", "じてんしゃ で", "ジテンシャ デ", "jitensha de")),
    ]
    return "\n".join([
        block(
            "Ana 的國家、城市與車子",
            "國家和城市都用助詞に。車で 是交通方式；車の中 是在車裡。西班牙的巴塞隆納用「スペインのバルセロナ」。",
            ["中文", "日文"],
            ask,
        ),
        "<h2>交通方式</h2>",
        "<p class=\"note\">交通方式用で，步行用歩いて。位置用「の中に」。</p>",
        table(["中文", "日文"], move),
        "<div class=\"tip\"><strong>先記這四組：</strong>何曜日／何日；年齡用歳です；國家和城市都用に；車で／車の中。四語並排見 <a href=\"../../tables/date-place/\">日期與地點對照</a>。</div>",
        "",
    ])


def patch_indexes():
    pairs = [
        (ROOT / "fr" / "index.html",
         "日期問句與 quel／quelle：今天幾號、星期幾，附回答範例。",
         "星期幾與幾月幾日要分開問；quel 配合名詞的性別與單複數。附日期讀法。"),
        (ROOT / "fr" / "index.html",
         "自我介紹問答：tu／vous 對照（姓名、國籍、年齡、喜好），附範本句可朗讀。",
         "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（rêver de）。"),
        (ROOT / "fr" / "index.html",
         "國家介詞 en／au／aux，以及出生（né／née）與居住。可朗讀。",
         "國家與城市介詞，Ana 的居住問句，以及 en voiture 和 dans la voiture。"),
        (ROOT / "en" / "index.html",
         "日期與星期問句：What day… / What's the date…，附回答範例。",
         "星期與日期問句，以及 October 6th、8th 和 2026 的讀法。"),
        (ROOT / "en" / "index.html",
         "自我介紹問答：姓名、國籍、年齡、喜好（口語／較禮貌），附範本句。",
         "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（dream of）。"),
        (ROOT / "en" / "index.html",
         "國家與城市的 in／to／from，以及出生與居住。",
         "國家與城市的 in，Ana 的居住問句，以及 by car 和 in the car。"),
        (ROOT / "de" / "index.html",
         "日期與星期問句：Welcher Tag…／Welches Datum…，附回答範例。",
         "星期與日期要分開問；每個日期都用序數，含 6.、8. 與 2026。"),
        (ROOT / "de" / "index.html",
         "自我介紹問答：du／Sie 對照（姓名、出身、年齡、喜好），附範本句。",
         "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想（träumen von）。"),
        (ROOT / "de" / "index.html",
         "國家與城市介詞 in／nach／aus，以及出生與居住。",
         "國家與城市介詞，Ana 的居住問句，以及 mit dem Auto 和 im Auto。"),
        (ROOT / "ja" / "index.html",
         "何日／何曜日：日期與星期問句，附回答範例。",
         "何日／何曜日，以及一日、六日、八日和 2026 年的讀法。"),
        (ROOT / "ja" / "index.html",
         "自我介紹問答：姓名、國籍、年齡、喜好，附範本句。",
         "自我介紹問答：國籍、年齡、喜好，以及 Paul 的夢想。"),
        (ROOT / "ja" / "index.html",
         "場所助詞：住む／生まれる／来る／行く，以及國家、城市例子。",
         "場所助詞，Ana 的居住問句，以及車で和車の中。"),
    ]
    for path, old, new in pairs:
        replace_once(path, old, new)
    index = ROOT / "tables" / "index.html"
    text = read(index)
    card = """<article class="item">
<div class="meta">課堂 · 日期 · 地點 · 跟讀</div>
<h3>日期與地點對照</h3>
<div class="langs">
<span class="en">EN</span>
<span class="de">DE</span>
<span class="fr">FR</span>
<span class="ja">JA</span>
</div>
<p>星期與日期、年齡動詞、國家與城市、交通方式與車內位置。九句問答並排，可循環朗讀。</p>
<a class="button" href="./date-place/">進入日期與地點對照 →</a>
</article>
"""
    needle = '<a class="button" href="./years/">進入歷史年份對照 →</a>\n</article>\n'
    if "date-place" in text:
        print("already", index.relative_to(ROOT))
        return
    if needle not in text:
        raise SystemExit("years card missing")
    write(index, text.replace(needle, needle + card, 1))
    print("card", index.relative_to(ROOT))


def ja_cmp(say, kanji, hira, kata, roma):
    return (
        f'<button type="button" class="say ja" data-say="{say}" data-lang="ja-JP">'
        f'<span class="word">{kanji}</span>'
        f'<span class="sub"><span class="hira">{hira}</span>　<span class="kata">{kata}</span></span>'
        f'<span class="roma">{roma}</span></button>'
    )


def cell_btn(cls, say, lang, shown=None):
    shown = say if shown is None else shown
    return (
        f'<button type="button" class="say {cls}" data-say="{say}" data-lang="{lang}">'
        f'<span class="word">{shown}</span></button>'
    )


def cmp_row(zh, cells):
    tds = [f'<td class="zh">{zh}</td>']
    tds.extend(f"<td>{c}</td>" for c in cells)
    return '<tr class="vocab-row">' + "".join(tds) + "</tr>"


def write_comparison():
    path = ROOT / "tables" / "date-place" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)

    def e(s, shown=None):
        return cell_btn("en", s, "en-US", shown)

    def f(s):
        return cell_btn("fr", s, "fr-FR")

    def d(s):
        return cell_btn("de", s, "de-DE")

    splits = [
        cmp_row("星期／日期", [
            e("What day is it today?") + e("What's today's date?"),
            f(f"On est quel jour aujourd{Q}hui ?") + f(f"Quelle est la date d{Q}aujourd{Q}hui ?"),
            d("Welcher Wochentag ist heute?") + d("Welches Datum haben wir heute?"),
            ja_cmp("今日は何曜日ですか。", "今日は何曜日ですか。", "きょう は なんようび ですか。", "キョウ ハ ナンヨウビ デスカ。", "Kyou wa nanyoubi desu ka.")
            + ja_cmp("今日の日付は何ですか。", "今日の日付は何ですか。", "きょう の ひづけ は なん ですか。", "キョウ ノ ヒヅケ ハ ナン デスカ。", "Kyou no hizuke wa nan desu ka."),
        ]),
        cmp_row("年齡", [
            e("Paul is thirty-two."),
            f("Paul a trente-deux ans."),
            d("Paul ist zweiunddreißig Jahre alt."),
            ja_cmp("ポールは三十二歳です。", "ポールは三十二歳です。", "ポール は さんじゅうにさい です。", "ポール ハ サンジュウニサイ デス。", "Pooru wa sanjuunisai desu."),
        ]),
        cmp_row("國家／城市", [
            e("Ana lives in Spain, in Barcelona."),
            f(f"Ana habite en Espagne, à Barcelone."),
            d("Ana wohnt in Spanien, in Barcelona."),
            ja_cmp("アナはスペインのバルセロナに住んでいます。", "アナはスペインのバルセロナに住んでいます。", "アナ は スペイン の バルセロナ に すんでいます。", "アナ ハ スペイン ノ バルセロナ ニ スンデイマス。", "Ana wa Supein no Baruserona ni sunde imasu."),
        ]),
        cmp_row("方式／位置", [
            e("by car") + e("in the car"),
            f("en voiture") + f("dans la voiture"),
            d("mit dem Auto") + d("im Auto"),
            ja_cmp("車で", "車で", "くるま で", "クルマ デ", "kuruma de")
            + ja_cmp("車の中に", "車の中に", "くるま の なか に", "クルマ ノ ナカ ニ", "kuruma no naka ni"),
        ]),
    ]
    dates = [
        cmp_row("10 月 1 日", [
            e("October first", "October 1st / first"),
            f("le premier octobre"),
            d("der erste Oktober"),
            ja_cmp("ついたち", "十月一日", "じゅうがつ ついたち", "ジュウガツ ツイタチ", "juugatsu tsuitachi"),
        ]),
        cmp_row("10 月 6 日", [
            e("October sixth", "October 6th / sixth"),
            f("le six octobre"),
            d("der sechste Oktober"),
            ja_cmp("むいか", "十月六日", "じゅうがつ むいか", "ジュウガツ ムイカ", "juugatsu muika"),
        ]),
        cmp_row("10 月 8 日", [
            e("October eighth", "October 8th / eighth"),
            f("le huit octobre"),
            d("der achte Oktober"),
            ja_cmp("ようか", "十月八日", "じゅうがつ ようか", "ジュウガツ ヨウカ", "juugatsu youka"),
        ]),
        cmp_row("2026 年", [
            e("twenty twenty-six"),
            f("deux mille vingt-six"),
            d("zweitausendsechsundzwanzig"),
            ja_cmp("にせんにじゅうろくねん", "二千二十六年", "にせんにじゅうろくねん", "ニセンニジュウロクネン", "nisen nijuurokunen"),
        ]),
    ]
    places = [
        cmp_row("城市", [e("in Barcelona"), f("à Barcelone"), d("in Barcelona"), ja_cmp("バルセロナに", "バルセロナに", "バルセロナ に", "バルセロナ ニ", "Baruserona ni")]),
        cmp_row("陰性國家", [e("in Spain"), f("en Espagne"), d("in Spanien"), ja_cmp("スペインに", "スペインに", "スペイン に", "スペイン ニ", "Supein ni")]),
        cmp_row("另一個陰性國家", [e("in France"), f("en France"), d("in Frankreich"), ja_cmp("フランスに", "フランスに", "フランス に", "フランス ニ", "Furansu ni")]),
        cmp_row("母音開頭的陽性國家", [e("in Iran"), f("en Iran"), d("im Iran"), ja_cmp("イランに", "イランに", "イラン に", "イラン ニ", "Iran ni")]),
        cmp_row("子音開頭的陽性國家", [e("in Japan"), f("au Japon"), d("in Japan"), ja_cmp("日本に", "日本に", "にほん に", "ニホン ニ", "Nihon ni")]),
        cmp_row("複數國家", [e("in the United States"), f("aux États-Unis"), d("in den USA"), ja_cmp("アメリカに", "アメリカに", "アメリカ に", "アメリカ ニ", "Amerika ni")]),
    ]
    moves = [
        cmp_row("汽車，交通方式", [e("by car"), f("en voiture"), d("mit dem Auto"), ja_cmp("車で", "車で", "くるま で", "クルマ デ", "kuruma de")]),
        cmp_row("汽車，所在位置", [e("in the car"), f("dans la voiture"), d("im Auto"), ja_cmp("車の中に", "車の中に", "くるま の なか に", "クルマ ノ ナカ ニ", "kuruma no naka ni")]),
        cmp_row("公車", [e("by bus"), f("en bus"), d("mit dem Bus"), ja_cmp("バスで", "バスで", "バス で", "バス デ", "basu de")]),
        cmp_row("火車", [e("by train"), f("en train"), d("mit dem Zug"), ja_cmp("電車で", "電車で", "でんしゃ で", "デンシャ デ", "densha de")]),
        cmp_row("地鐵", [e("by subway"), f("en métro"), d("mit der U-Bahn"), ja_cmp("地下鉄で", "地下鉄で", "ちかてつ で", "チカテツ デ", "chikatetsu de")]),
        cmp_row("飛機", [e("by plane"), f("en avion"), d("mit dem Flugzeug"), ja_cmp("飛行機で", "飛行機で", "ひこうき で", "ヒコウキ デ", "hikouki de")]),
        cmp_row("步行", [e("on foot"), f("à pied"), d("zu Fuß"), ja_cmp("歩いて", "歩いて", "あるいて", "アルイテ", "aruite")]),
        cmp_row("自行車", [e("by bike"), f("à vélo"), d("mit dem Fahrrad"), ja_cmp("自転車で", "自転車で", "じてんしゃ で", "ジテンシャ デ", "jitensha de")]),
    ]
    questions = [
        ("今天星期幾？", "What day is it today?", f"On est quel jour aujourd{Q}hui ?", "Welcher Wochentag ist heute?",
         ("今日は何曜日ですか。", "今日は何曜日ですか。", "きょう は なんようび ですか。", "キョウ ハ ナンヨウビ デスカ。", "Kyou wa nanyoubi desu ka.")),
        ("今天幾月幾日？", "What's today's date?", f"Quelle est la date d{Q}aujourd{Q}hui ?", "Welches Datum haben wir heute?",
         ("今日の日付は何ですか。", "今日の日付は何ですか。", "きょう の ひづけ は なん ですか。", "キョウ ノ ヒヅケ ハ ナン デスカ。", "Kyou no hizuke wa nan desu ka.")),
        ("Paul 是什麼國籍？", "What nationality is Paul?", "Paul est de quelle nationalité ?", "Welche Nationalität hat Paul?",
         ("ポールは何人ですか。", "ポールは何人ですか。", "ポール は なにじん ですか。", "ポール ハ ナニジン デスカ。", "Pooru wa nanijin desu ka.")),
        ("Paul 幾歲？", "How old is Paul?", "Paul a quel âge ?", "Wie alt ist Paul?",
         ("ポールは何歳ですか。", "ポールは何歳ですか。", "ポール は なんさい ですか。", "ポール ハ ナンサイ デスカ。", "Pooru wa nansai desu ka.")),
        ("Paul 夢想什麼？", "What does Paul dream of?", "Paul rêve de quoi ?", "Wovon träumt Paul?",
         ("ポールは何を夢見ていますか。", "ポールは何を夢見ていますか。", "ポール は なに を ゆめみていますか。", "ポール ハ ナニ ヲ ユメミテイマスカ。", "Pooru wa nani o yumemite imasu ka.")),
        ("Ana 住在哪個國家？", "Which country does Ana live in?", "Ana habite dans quel pays ?", "In welchem Land wohnt Ana?",
         ("アナはどの国に住んでいますか。", "アナはどの国に住んでいますか。", "アナ は どの くに に すんでいますか。", "アナ ハ ドノ クニ ニ スンデイマスカ。", "Ana wa dono kuni ni sunde imasu ka.")),
        ("Ana 住在哪座城市？", "Which city does Ana live in?", "Ana habite dans quelle ville ?", "In welcher Stadt wohnt Ana?",
         ("アナはどの都市に住んでいますか。", "アナはどの都市に住んでいますか。", "アナ は どの とし に すんでいますか。", "アナ ハ ドノ トシ ニ スンデイマスカ。", "Ana wa dono toshi ni sunde imasu ka.")),
        ("你怎麼去學校？", "How do you get to school?", f"Tu vas à l{Q}école comment ?", "Wie kommst du zur Schule?",
         ("学校へはどうやって行きますか。", "学校へはどうやって行きますか。", "がっこう へ は どうやって いきますか。", "ガッコウ ヘ ハ ドウヤッテ イキマスカ。", "Gakkou e wa douyatte ikimasu ka.")),
        ("鑰匙在哪裡？", "Where are the keys?", "Où sont les clés ?", "Wo sind die Schlüssel?",
         ("鍵はどこですか。", "鍵はどこですか。", "かぎ は どこ ですか。", "カギ ハ ドコ デスカ。", "Kagi wa doko desu ka.")),
    ]
    answers = [
        ("今天星期四。", "It's Thursday.", "On est jeudi.", "Heute ist Donnerstag.",
         ("今日は木曜日です。", "今日は木曜日です。", "きょう は もくようび です。", "キョウ ハ モクヨウビ デス。", "Kyou wa mokuyoubi desu.")),
        ("今天是 2026 年 10 月 8 日。", "It's October eighth, twenty twenty-six.", f"Aujourd{Q}hui, c{Q}est le huit octobre deux mille vingt-six.", "Heute ist der achte Oktober zweitausendsechsundzwanzig.",
         ("きょうはにせんにじゅうろくねんじゅうがつようかです。", "今日は二千二十六年十月八日です。", "きょう は にせんにじゅうろくねん じゅうがつ ようか です。", "キョウ ハ ニセンニジュウロクネン ジュウガツ ヨウカ デス。", "Kyou wa nisen nijuurokunen juugatsu youka desu.")),
        ("Paul 是法國人。", "Paul is French.", "Paul est français.", "Paul ist Franzose.",
         ("ポールはフランス人です。", "ポールはフランス人です。", "ポール は フランスじん です。", "ポール ハ フランスジン デス。", "Pooru wa Furansujin desu.")),
        ("Paul 三十二歲。", "Paul is thirty-two.", "Paul a trente-deux ans.", "Paul ist zweiunddreißig Jahre alt.",
         ("ポールは三十二歳です。", "ポールは三十二歳です。", "ポール は さんじゅうにさい です。", "ポール ハ サンジュウニサイ デス。", "Pooru wa sanjuunisai desu.")),
        ("Paul 夢想去旅行。", "Paul dreams of traveling.", "Paul rêve de voyager.", "Paul träumt davon, zu reisen.",
         ("ポールは旅行を夢見ています。", "ポールは旅行を夢見ています。", "ポール は りょこう を ゆめみています。", "ポール ハ リョコウ ヲ ユメミテイマス。", "Pooru wa ryokou o yumemite imasu.")),
        ("Ana 住在西班牙。", "Ana lives in Spain.", "Ana habite en Espagne.", "Ana wohnt in Spanien.",
         ("アナはスペインに住んでいます。", "アナはスペインに住んでいます。", "アナ は スペイン に すんでいます。", "アナ ハ スペイン ニ スンデイマス。", "Ana wa Supein ni sunde imasu.")),
        ("Ana 住在巴塞隆納。", "Ana lives in Barcelona.", "Ana habite à Barcelone.", "Ana wohnt in Barcelona.",
         ("アナはバルセロナに住んでいます。", "アナはバルセロナに住んでいます。", "アナ は バルセロナ に すんでいます。", "アナ ハ バルセロナ ニ スンデイマス。", "Ana wa Baruserona ni sunde imasu.")),
        ("我開車／搭汽車去學校。", "I go to school by car.", f"Je vais à l{Q}école en voiture.", "Ich fahre mit dem Auto zur Schule.",
         ("私は車で学校へ行きます。", "私は車で学校へ行きます。", "わたし は くるま で がっこう へ いきます。", "ワタシ ハ クルマ デ ガッコウ ヘ イキマス。", "Watashi wa kuruma de gakkou e ikimasu.")),
        ("鑰匙在車裡。", "The keys are in the car.", "Les clés sont dans la voiture.", "Die Schlüssel sind im Auto.",
         ("鍵は車の中にあります。", "鍵は車の中にあります。", "かぎ は くるま の なか に あります。", "カギ ハ クルマ ノ ナカ ニ アリマス。", "Kagi wa kuruma no naka ni arimasu.")),
    ]

    def qa_rows(items):
        out = []
        for zh, ens, frs, des, ja_item in items:
            out.append(cmp_row(zh, [e(ens), f(frs), d(des), ja_cmp(*ja_item)]))
        return "\n".join(out)

    head = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="英、法、德、日對照：星期與日期、年齡、國家與城市、交通方式與車內位置。點選可朗讀。">
<title>日期與地點對照｜四語筆記</title>
<style>
:root{font-family:system-ui,-apple-system,'Noto Sans TC','Yu Gothic',sans-serif;color:#182a45;background:#f2f5fa}
*{box-sizing:border-box}
body{margin:0}
header{background:#445a7a;color:white;padding:22px max(20px,calc((100vw - 1180px)/2))}
header .brand{font-size:1.35rem;font-weight:800}
header a{color:inherit;text-decoration:none}
main{max-width:1180px;margin:auto;padding:32px 20px 70px}
h1{font-size:clamp(1.8rem,4vw,2.65rem);margin:0 0 8px}
h2{font-size:1.25rem;margin:32px 0 12px}
p{line-height:1.7;color:#53647c}
.note{font-size:.92rem;color:#52647d;margin:0 0 18px}
.toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}
.toc a{display:inline-block;padding:7px 12px;border-radius:9px;background:white;border:1px solid #dae3ef;color:#445a7a;text-decoration:none;font-weight:650;font-size:.92rem}
.toc a:hover,.toc a:focus-visible{outline:2px solid #445a7a;outline-offset:2px}
.controls{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border:1px solid #dae3ef;border-radius:14px;padding:14px 16px;box-shadow:0 8px 24px #142f5214;margin:0 0 22px;backdrop-filter:blur(6px)}
.controls-row{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.ctrl{cursor:pointer;border:0;border-radius:9px;font:inherit;font-weight:750;padding:10px 14px;background:#445a7a;color:white}
.ctrl.stop{background:#5c6675}
.ctrl:hover,.ctrl:focus-visible{filter:brightness(.92);outline:2px solid #445a7a;outline-offset:2px}
.rate,.loop{font-size:.92rem;color:#3d4d63;display:flex;align-items:center;gap:8px}
.rate input{width:140px}
.status{margin-top:10px;font-size:.9rem;color:#6a5870}
.tablewrap{overflow-x:auto;background:white;border:1px solid #dae3ef;border-radius:14px;box-shadow:0 6px 18px #142f520c}
table{border-collapse:collapse;width:100%;min-width:980px}
th{background:#eef2f7;text-align:left;font-size:.9rem;padding:12px 12px;white-space:nowrap}
.th-en{color:#17355d}.th-fr{color:#b3482f}.th-de{color:#1d6a4f}.th-ja{color:#8d3a55}
td{padding:10px 12px;border-top:1px solid #e6edf5;vertical-align:top}
.zh{color:#53647c;font-weight:650;white-space:nowrap}
.say{display:flex;flex-direction:column;align-items:flex-start;gap:2px;width:100%;background:transparent;border:0;cursor:pointer;font:inherit;text-align:left;padding:4px 2px;border-radius:8px}
.say:hover,.say:focus-visible{outline:2px solid currentColor;outline-offset:2px}
.say .word{font-size:1.05rem;font-weight:750}
.say.en,.say.en .word{color:#17355d}
.say.fr,.say.fr .word{color:#b3482f}
.say.de,.say.de .word{color:#1d6a4f}
.say.ja,.say.ja .word{color:#8d3a55}
.sub{font-size:.9rem;color:#3d4d63}
.kata{color:#6a5870}
.roma{font-size:.82rem;color:#6a5870}
.vocab-row.active{background:#fff4d8}
.tip{background:white;border-left:4px solid #445a7a;padding:14px 18px;border-radius:8px;margin-top:28px;border:1px solid #dae3ef;border-left-width:4px;line-height:1.7;color:#52647a}
.tip a{color:#445a7a;font-weight:650}
footer{max-width:1180px;margin:auto;padding:20px;color:#627087;font-size:.9rem}
@media(max-width:700px){main{padding-top:25px}.rate input{width:100px}}
</style>
</head>
<body>
<header><div class="brand"><a href="../index.html">← 對表</a>　/　日期與地點對照</div></header>
<main>
<h1>日期、問句與地點</h1>
<p class="note">同一件事並排四種說法。年齡、地名介詞和「在車裡」都按各語言自己的文法，不逐字搬法文。點選可朗讀；日文日期的六日、八日用平假名朗讀，避免讀錯。</p>
<nav class="toc" aria-label="章節"><a href="#split">四組對照</a><a href="#dates">日期讀法</a><a href="#place">地名</a><a href="#move">交通與位置</a><a href="#ask">問句</a><a href="#answer">回答</a></nav>
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
"""
    thead = """<thead><tr><th scope="col">中文</th><th scope="col" class="th-en">英文</th><th scope="col" class="th-fr">法文</th><th scope="col" class="th-de">德文</th><th scope="col" class="th-ja">日文</th></tr></thead>"""

    def section(sid, title, note, rows_html):
        return (
            f'<section id="{sid}">\n<h2>{title}</h2>\n<p class="note">{note}</p>\n'
            f'<div class="tablewrap"><table>\n{thead}\n<tbody>\n{rows_html}\n</tbody></table></div>\n</section>\n'
        )

    body = "\n".join([
        section("split", "四組對照", "年齡：英文和德文用「是」，法文用「有」，日文用「歳です」。國家和城市：英文、德文、日文的介詞或助詞相同；法文要換。交通方式不等於人在車裡。", "\n".join(splits)),
        section("dates", "日期讀法", "法文只有 1 日用 premier，6 日、8 日用基數，前面要有 le。德文每一天都用序數。英文月份在前，並用序數。日文一日、六日、八日有特別讀音。", "\n".join(dates)),
        section("place", "地名", "這一欄的「陰性國家、陽性國家」是在說明法文介詞。德文多數國名都用 in，只有帶冠詞的國名要變格。日文地名後加に。", "\n".join(places)),
        section("move", "交通與位置", "法文 en voiture 不一定是自己開。德文 mit 後面用第三格，im Auto 等於 in dem Auto。日文方式用で，裡面用の中に。", "\n".join(moves)),
        section("ask", "問句", "法文問國籍、城市時，quel 的形式看名詞，不看被問的人是男是女。", qa_rows(questions)),
        section("answer", "回答", "Paul 的國籍、年齡和夢想是課堂範例，不是已知的個人資料。星期四對應課堂例句。", qa_rows(answers)),
        """<div class="tip"><strong>各語言專題：</strong>
<a href="../../fr/date-quel/">法文日期</a>、
<a href="../../fr/dialogue-a1/">法文問答</a>、
<a href="../../fr/pays-prepositions/">法文地點</a>；
<a href="../../en/date-quel/">英文</a>、
<a href="../../de/date-quel/">德文</a>、
<a href="../../ja/date-quel/">日文</a>的日期頁也已補上對應句子。</div>""",
    ])
    script = r"""
<script>
const rateInput = document.getElementById('rate');
const rateLabel = document.getElementById('rate-label');
const loopBox = document.getElementById('loop');
const statusEl = document.getElementById('play-status');
let playing = false, queue = [], index = 0;

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
  u.lang = lang; u.rate = rate;
  const voice = pickVoice(lang);
  if (voice) u.voice = voice;
  u.onend = () => { if (onend) onend(); };
  u.onerror = () => { if (onend) onend(); };
  speechSynthesis.speak(u);
}
function allItems() {
  return [...document.querySelectorAll('[data-say]')].map(el => ({ text: el.dataset.say, lang: el.dataset.lang, el }));
}
function clearActive() {
  document.querySelectorAll('.vocab-row.active').forEach(r => r.classList.remove('active'));
}
function setStatus(text) { if (statusEl) statusEl.textContent = text; }
function stopAll() {
  playing = false; queue = []; index = 0;
  speechSynthesis.cancel(); clearActive(); setStatus('已停止');
}
function playNext() {
  if (!playing) return;
  if (index >= queue.length) {
    if (loopBox && loopBox.checked && queue.length) index = 0;
    else { stopAll(); setStatus('播放完畢'); return; }
  }
  const item = queue[index];
  clearActive();
  const row = item.el.closest('.vocab-row');
  if (row) { row.classList.add('active'); row.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); }
  setStatus('播放中：' + item.text + '（' + (index + 1) + ' / ' + queue.length + '）');
  const rate = parseFloat(rateInput.value) || 0.9;
  speakOnce(item.text, item.lang, rate, () => { if (!playing) return; index += 1; setTimeout(playNext, 280); });
}
function startQueue(items, startAt) {
  if (!items.length) return;
  voicesReady(() => { playing = true; queue = items; index = startAt || 0; playNext(); });
}
rateInput.addEventListener('input', () => { rateLabel.textContent = parseFloat(rateInput.value).toFixed(1); });
rateLabel.textContent = parseFloat(rateInput.value).toFixed(1);
document.getElementById('play-all').addEventListener('click', () => startQueue(allItems(), 0));
document.getElementById('stop-all').addEventListener('click', stopAll);
document.addEventListener('click', e => {
  const b = e.target.closest('[data-say]');
  if (!b || e.target.closest('.controls')) return;
  const rate = parseFloat(rateInput.value) || 0.9;
  voicesReady(() => {
    playing = false; queue = []; clearActive();
    const row = b.closest('.vocab-row');
    if (row) row.classList.add('active');
    setStatus('單字：' + b.dataset.say);
    speakOnce(b.dataset.say, b.dataset.lang, rate, () => { clearActive(); setStatus('待命'); });
  });
});
if ('speechSynthesis' in window) speechSynthesis.getVoices();
</script>
</body>
</html>
"""
    write(path, head + body + "\n</main>\n<footer>日期與地點對照｜英・法・德・日</footer>\n" + script)
    print("wrote", path.relative_to(ROOT))


def main():
    patch_french_date()
    patch_notes()
    insert_before(ROOT / "fr" / "dialogue-a1" / "index.html", "</main>", french_dialogue())
    insert_before(ROOT / "fr" / "pays-prepositions" / "index.html", "</main>", french_place())
    insert_before(ROOT / "en" / "date-quel" / "index.html", "</main>", english_date())
    insert_before(ROOT / "en" / "dialogue-a1" / "index.html", "</main>", english_dialogue())
    insert_before(ROOT / "en" / "pays-prepositions" / "index.html", "</main>", english_place())
    insert_before(ROOT / "de" / "date-quel" / "index.html", "</main>", german_date())
    insert_before(ROOT / "de" / "dialogue-a1" / "index.html", "</main>", german_dialogue())
    insert_before(ROOT / "de" / "pays-prepositions" / "index.html", "</main>", german_place())
    insert_before(ROOT / "ja" / "date-quel" / "index.html", "</main>", japanese_date())
    insert_before(ROOT / "ja" / "dialogue-a1" / "index.html", "</main>", japanese_dialogue())
    insert_before(ROOT / "ja" / "pays-prepositions" / "index.html", "</main>", japanese_place())
    patch_indexes()
    write_comparison()


if __name__ == "__main__":
    main()
