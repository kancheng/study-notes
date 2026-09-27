from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import A4
from pathlib import Path

ROOT = Path(__file__).parent.parent
NOTO = Path(__file__).parent / 'NotoSansTC.ttf'
pdfmetrics.registerFont(TTFont('Chinese', str(NOTO)))

navy = HexColor('#17365e')
muted = HexColor('#53677c')
pale = HexColor('#eaf0f9')
line_color = HexColor('#dae2ed')
white = HexColor('#ffffff')
light = HexColor('#dde9ff')


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
])

render_sheet(ROOT / 'en/hello-verbs/Hello-Verbs-A1.pdf', 'Hello Verbs - English A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變化與跟讀例句', en_groups, en_tip, '現在式')
render_sheet(ROOT / 'de/hallo-verben/Hallo-Verben-A1.pdf', 'Hallo Verben - German A1', '三個必背動詞：現在式、例句、中文翻譯', '現在式變位與跟讀例句', de_groups, de_tip, '現在式')
