from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import A4
from pathlib import Path

ROOT = Path(__file__).parent.parent
NOTO = Path(__file__).parent / 'NotoSansTC.ttf'
DEJAVU = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
pdfmetrics.registerFont(TTFont('Chinese', str(NOTO)))

navy = HexColor('#17365e')
muted = HexColor('#53677c')
pale = HexColor('#eaf0f9')
line_color = HexColor('#dae2ed')
white = HexColor('#ffffff')
light = HexColor('#dde9ff')


def render_french():
    out = ROOT / 'fr/bonjour-verbes/Bonjour-Verbes-A1.pdf'
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4

    def text(x, y, s, size=10, color=navy, font='DejaVu'):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, y, s)

    def cn(x, y, s, size=10, color=navy):
        text(x, y, s, size, color, 'Chinese')

    def line(y):
        c.setStrokeColor(line_color)
        c.line(42, y, W - 42, y)

    y = 0

    def heading(title, sub):
        nonlocal y
        c.setFillColor(navy)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        text(42, H - 49, title, 20, white)
        cn(43, H - 74, sub, 11, light)
        y = H - 123

    heading('Bonjour Verbes - French A1', '三個必背動詞：現在式、例句、中文翻譯')
    groups = [
        ('ETRE (être)', '是／處於', [('je', 'je suis', '我是'), ('tu', 'tu es', '你是'), ('il / elle', 'il / elle est', '他／她是'), ('nous', 'nous sommes', '我們是'), ('vous', 'vous êtes', '您／你們是'), ('ils / elles', 'ils / elles sont', '他們／她們是')], [('Je suis étudiant.', '我是學生。'), ('Tu es prêt ?', '你準備好了嗎？'), ('Elle est française.', '她是法國人。'), ('Nous sommes à Taipei.', '我們在台北。'), ('Vous êtes professeur ?', '您是老師嗎？'), ('Ils sont ici.', '他們在這裡。')]),
        ('AVOIR', '有；表達年齡', [('je', 'j’ai', '我有'), ('tu', 'tu as', '你有'), ('il / elle', 'il / elle a', '他／她有'), ('nous', 'nous avons', '我們有'), ('vous', 'vous avez', '您／你們有'), ('ils / elles', 'ils / elles ont', '他們／她們有')], [('J’ai 25 ans.', '我 25 歲。'), ('Tu as un livre.', '你有一本書。'), ('Il a un frère.', '他有一個兄弟。'), ('Nous avons un cours.', '我們有一堂課。'), ('Vous avez une question ?', '您有問題嗎？'), ('Elles ont des amis.', '她們有朋友。')]),
        ("S’APPELER", '叫做／名字是', [('je', 'je m’appelle', '我叫'), ('tu', 'tu t’appelles', '你叫'), ('il / elle', 'il / elle s’appelle', '他／她叫'), ('nous', 'nous nous appelons', '我們叫'), ('vous', 'vous vous appelez', '您／你們叫'), ('ils / elles', 'ils / elles s’appellent', '他們／她們叫')], [('Je m’appelle Hao-Cheng.', '我叫 Hao-Cheng。'), ('Tu t’appelles comment ?', '你叫什麼名字？'), ('Elle s’appelle Marie.', '她叫 Marie。'), ('Nous nous appelons les Bleus.', '我們叫做「藍隊」。'), ('Vous vous appelez comment ?', '您叫什麼名字？'), ('Ils s’appellent Paul et Marc.', '他們叫 Paul 和 Marc。')]),
    ]
    for i, (title, meaning, rows, examples) in enumerate(groups):
        if i:
            c.showPage()
            heading('Bonjour Verbes - French A1', '現在式變位與跟讀例句')
        text(42, y, title, 18)
        cn(265, y, meaning, 12, muted)
        y -= 30
        c.setFillColor(pale)
        c.roundRect(42, y - 5, W - 84, 25, 5, fill=1, stroke=0)
        cn(55, y + 3, '人稱', 10)
        cn(190, y + 3, '現在式', 10)
        cn(390, y + 3, '中文', 10)
        y -= 23
        for subject, form, zh in rows:
            text(55, y, subject, 10)
            text(190, y, form, 10)
            cn(390, y, zh, 10)
            line(y - 9)
            y -= 30
        y -= 18
        cn(42, y, '例句與翻譯', 13)
        y -= 25
        for fr, zh in examples:
            text(55, y, fr, 10)
            cn(55, y - 18, zh, 10, muted)
            y -= 45
        if i == 2:
            y -= 5
            cn(42, y, '拼字：vous êtes、ils / elles sont、s’appeler。年齡用 avoir。', 10, muted)
        c.setFont('DejaVu', 8)
        c.setFillColor(muted)
        c.drawRightString(W - 42, 28, f'{i + 1} / 3')
    c.save()
    print(out)


def render_sheet(out, banner, first_sub, later_sub, groups, tip, form_header):
    c = canvas.Canvas(str(out), pagesize=A4)
    W, H = A4
    font = 'Chinese'
    state = {'y': 0}

    def text(x, y, s, size=10, color=navy):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, y, s)

    def heading(title, sub):
        c.setFillColor(navy)
        c.rect(0, H - 94, W, 94, fill=1, stroke=0)
        text(42, H - 49, title, 20, white)
        text(43, H - 74, sub, 11, light)
        state['y'] = H - 123

    heading(banner, first_sub)
    for i, (title, meaning, rows, examples) in enumerate(groups):
        if i:
            c.showPage()
            heading(banner, later_sub)
        y = state['y']
        text(42, y, title, 18)
        text(42 + stringWidth(title, font, 18) + 14, y, meaning, 12, muted)
        y -= 30
        c.setFillColor(pale)
        c.roundRect(42, y - 5, W - 84, 25, 5, fill=1, stroke=0)
        text(55, y + 3, '人稱', 10)
        text(168, y + 3, form_header, 10)
        text(400, y + 3, '中文', 10)
        y -= 23
        for subject, form, zh in rows:
            text(55, y, subject, 10)
            size = 10
            while size > 7 and stringWidth(form, font, size) > 220:
                size -= 1
            text(168, y, form, size)
            text(400, y, zh, 10)
            c.setStrokeColor(line_color)
            c.line(42, y - 9, W - 42, y - 9)
            y -= 30
        y -= 18
        text(42, y, '例句與翻譯', 13)
        y -= 25
        for line, zh in examples:
            text(55, y, line, 10)
            text(55, y - 18, zh, 10, muted)
            y -= 45
        if i == 2:
            y -= 5
            for n, part in enumerate(tip.split('\n')):
                text(42, y - n * 14, part, 10, muted)
        c.setFont(font, 8)
        c.setFillColor(muted)
        c.drawRightString(W - 42, 28, f'{i + 1} / 3')
    c.save()
    print(out)


def require_glyphs(sheets):
    from fontTools.ttLib import TTFont
    cmap = TTFont(str(NOTO)).getBestCmap()
    missing = []
    for label, chunks in sheets:
        for chunk in chunks:
            for ch in chunk:
                if ch.isspace() or ord(ch) < 32:
                    continue
                if ord(ch) not in cmap:
                    missing.append(f'{label}:{ch} U+{ord(ch):04X}')
    if missing:
        raise SystemExit('NotoSansTC missing glyphs:\n' + '\n'.join(missing))


en_groups = [
    ('BE', '是／處於', [('I', 'I am', '我是'), ('you', 'you are', '你是'), ('he / she', 'he / she is', '他／她是'), ('we', 'we are', '我們是'), ('you', 'you are', '你們是'), ('they', 'they are', '他們／她們是')], [('I am a student.', '我是學生。'), ('Are you ready?', '你準備好了嗎？'), ('She is French.', '她是法國人。'), ('We are in Taipei.', '我們在台北。'), ('Are you a teacher?', '您是老師嗎？'), ('They are here.', '他們在這裡。')]),
    ('HAVE', '有', [('I', 'I have', '我有'), ('you', 'you have', '你有'), ('he / she', 'he / she has', '他／她有'), ('we', 'we have', '我們有'), ('you', 'you have', '你們有'), ('they', 'they have', '他們／她們有')], [('I have a book.', '我有一本書。'), ('Do you have a pen?', '你有筆嗎？'), ('He has a brother.', '他有一個兄弟。'), ('We have a class.', '我們有一堂課。'), ('Do you have a question?', '您有問題嗎？'), ('They have friends.', '他們有朋友。')]),
    ('BE CALLED', '叫做／名字是', [('I', 'I am called', '我叫'), ('you', 'you are called', '你叫'), ('he / she', 'he / she is called', '他／她叫'), ('we', 'we are called', '我們叫'), ('you', 'you are called', '你們叫'), ('they', 'they are called', '他們／她們叫')], [('I am called Hao-Cheng.', '我叫 Hao-Cheng。'), ('What are you called?', '你叫什麼名字？'), ('She is called Marie.', '她叫 Marie。'), ('We are called the Blues.', '我們叫做「藍隊」。'), ('What are you called?', '您叫什麼名字？'), ('They are called Paul and Marc.', '他們叫 Paul 和 Marc。')]),
]
en_tip = '第三人稱單數加 -s：he is、she has。you 同時對應你和你們。\n自介更常說 My name is Hao-Cheng. 年齡用 be：I am 25 years old.'

de_groups = [
    ('SEIN', '是／處於', [('ich', 'ich bin', '我是'), ('du', 'du bist', '你是'), ('er / sie', 'er / sie ist', '他／她是'), ('wir', 'wir sind', '我們是'), ('ihr', 'ihr seid', '你們是'), ('sie / Sie', 'sie / Sie sind', '他們／您是')], [('Ich bin Student.', '我是學生。'), ('Bist du bereit?', '你準備好了嗎？'), ('Sie ist Französin.', '她是法國人。'), ('Wir sind in Taipei.', '我們在台北。'), ('Sind Sie Lehrer?', '您是老師嗎？'), ('Sie sind hier.', '他們在這裡。')]),
    ('HABEN', '有', [('ich', 'ich habe', '我有'), ('du', 'du hast', '你有'), ('er / sie', 'er / sie hat', '他／她有'), ('wir', 'wir haben', '我們有'), ('ihr', 'ihr habt', '你們有'), ('sie / Sie', 'sie / Sie haben', '他們／您有')], [('Ich habe ein Buch.', '我有一本書。'), ('Hast du einen Stift?', '你有筆嗎？'), ('Er hat einen Bruder.', '他有一個兄弟。'), ('Wir haben einen Kurs.', '我們有一堂課。'), ('Haben Sie eine Frage?', '您有問題嗎？'), ('Sie haben Freunde.', '他們有朋友。')]),
    ('HEISSEN (heißen)', '叫做／名字是', [('ich', 'ich heiße', '我叫'), ('du', 'du heißt', '你叫'), ('er / sie', 'er / sie heißt', '他／她叫'), ('wir', 'wir heißen', '我們叫'), ('ihr', 'ihr heißt', '你們叫'), ('sie / Sie', 'sie / Sie heißen', '他們／您叫')], [('Ich heiße Hao-Cheng.', '我叫 Hao-Cheng。'), ('Wie heißt du?', '你叫什麼名字？'), ('Sie heißt Marie.', '她叫 Marie。'), ('Wir heißen die Blauen.', '我們叫做「藍隊」。'), ('Wie heißen Sie?', '您叫什麼名字？'), ('Sie heißen Paul und Marc.', '他們叫 Paul 和 Marc。')]),
]
de_tip = '拼字：du bist、ihr seid、sie/Sie sind。du hast、er hat。heißt、heißen。年齡用 sein：Ich bin 25 Jahre alt.'

ja_groups = [
    ('DESU (です)', '是', [('私', '私は〜です', '我是'), ('あなた', 'あなたは〜です', '你是'), ('彼／彼女', '彼は／彼女は〜です', '他／她是'), ('私たち', '私たちは〜です', '我們是'), ('あなた', 'あなたは〜です', '您是'), ('彼ら／彼女たち', '彼らは／彼女たちは〜です', '他們／她們是')], [('私は学生です。', '我是學生。'), ('準備はいいですか。', '你準備好了嗎？'), ('彼女はフランス人です。', '她是法國人。'), ('私は 25 才です。', '我 25 歲。'), ('先生ですか。', '您是老師嗎？'), ('彼らは学生です。', '他們是學生。')]),
    ('ARIMASU / IMASU', '有；東西與人不同', [('私', '（私は）〜があります', '我有'), ('あなた', '（あなたは）〜があります', '你有'), ('彼／彼女', '（彼は／彼女は）〜があります', '他／她有'), ('私たち', '（私たちは）〜があります', '我們有'), ('あなた', '（あなたは）〜があります', '您有'), ('彼ら／彼女たち', '（彼らは／彼女たちは）〜があります', '他們／她們有')], [('本があります。', '我有一本書。'), ('ペンはありますか。', '你有筆嗎？'), ('彼には兄弟がいます。', '他有一個兄弟。'), ('授業があります。', '我們有一堂課。'), ('質問はありますか。', '您有問題嗎？'), ('彼女たちには友達がいます。', '她們有朋友。')]),
    ('TO IIMASU (と言います)', '叫做／名字是', [('私', '私は〜と言います', '我叫'), ('あなた', 'あなたは〜と言います', '你叫'), ('彼／彼女', '彼は／彼女は〜と言います', '他／她叫'), ('私たち', '私たちは〜と言います', '我們叫'), ('あなた', 'あなたは〜と言います', '您叫'), ('彼ら／彼女たち', '彼らは／彼女たちは〜と言います', '他們／她們叫')], [('私は Hao-Cheng と言います。', '我叫 Hao-Cheng。'), ('名前は何ですか。', '你叫什麼名字？'), ('彼女は Marie と言います。', '她叫 Marie。'), ('私たちは青組と言います。', '我們叫做「藍隊」。'), ('お名前は何ですか。', '您叫什麼名字？'), ('彼らは Paul と Marc と言います。', '他們叫 Paul 和 Marc。')]),
]
ja_tip = 'です、あります、います、と言います都不隨人稱變化。東西用あります，人用います。\n年齡用です：私は 25 才です。'


def chunks_of(groups, tip, *labels):
    parts = list(labels) + [tip]
    for title, meaning, rows, examples in groups:
        parts.extend([title, meaning])
        for row in rows:
            parts.extend(row)
        for example in examples:
            parts.extend(example)
    return parts


require_glyphs([
    ('en', chunks_of(en_groups, en_tip, 'Hello Verbs - English A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變化與跟讀例句', '人稱', '現在式', '中文', '例句與翻譯')),
    ('de', chunks_of(de_groups, de_tip, 'Hallo Verben - German A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變位與跟讀例句')),
    ('ja', chunks_of(ja_groups, ja_tip, 'Konnichiwa Doushi - Japanese A1', '三種必背說法：對照、例句、中文翻譯', '說法對照與跟讀例句', '說法')),
])

if DEJAVU.exists():
    pdfmetrics.registerFont(TTFont('DejaVu', str(DEJAVU)))
    render_french()
else:
    print('DejaVu not found; left the existing French PDF in place')

render_sheet(ROOT / 'en/hello-verbs/Hello-Verbs-A1.pdf', 'Hello Verbs - English A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變化與跟讀例句', en_groups, en_tip, '現在式')
render_sheet(ROOT / 'de/hallo-verben/Hallo-Verben-A1.pdf', 'Hallo Verben - German A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變位與跟讀例句', de_groups, de_tip, '現在式')
render_sheet(ROOT / 'ja/konnichiwa-doushi/Konnichiwa-Doushi-A1.pdf', 'Konnichiwa Doushi - Japanese A1', '三種必背說法：對照、例句、中文翻譯', '說法對照與跟讀例句', ja_groups, ja_tip, '說法')
