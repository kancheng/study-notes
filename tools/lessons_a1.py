from lesson_util import G, L

LESSONS = [
    L(
        'pronouns', 'A1', 'Pronouns', '英文 A1｜人稱、所有格、受格',
        '一句話裡，主詞用主格，擁有的東西用所有格，動詞後面的人用受格。',
        'I / my / me 這一組代名詞：主格、所有格、受格對照，附例句、中文、朗讀與 PDF。',
        'you 的主格和受格一樣。it 指事物或動物。',
        [
            G('主格', '當主詞', [
                ['我', 'I', '我'],
                ['你', 'you', '你'],
                ['他／她', 'he / she', '他／她'],
                ['我們', 'we', '我們'],
                ['他們', 'they', '他們'],
            ], [
                ['I am a student.', '我是學生。'],
                ['She is in Taipei.', '她在台北。'],
                ['We like English.', '我們喜歡英文。'],
                ['They are friends.', '他們是朋友。'],
            ]),
            G('所有格', '後面接名詞', [
                ['我的', 'my', '我的'],
                ['你的', 'your', '你的'],
                ['他的／她的', 'his / her', '他的／她的'],
                ['我們的', 'our', '我們的'],
                ['他們的', 'their', '他們的'],
            ], [
                ['My name is Hao-Cheng.', '我的名字是 Hao-Cheng。'],
                ['Her book is new.', '她的書是新的。'],
                ['Our class is at nine.', '我們的課在九點。'],
                ['Their teacher is kind.', '他們的老師很親切。'],
            ]),
            G('受格', '放在動詞或介系詞後面', [
                ['我', 'me', '我'],
                ['你', 'you', '你'],
                ['他／她', 'him / her', '他／她'],
                ['我們', 'us', '我們'],
                ['他們', 'them', '他們'],
            ], [
                ['She knows me.', '她認識我。'],
                ['I called him.', '我打電話給他。'],
                ['This gift is for us.', '這份禮物是給我們的。'],
                ['We met them at school.', '我們在學校遇到他們。'],
            ]),
        ],
    ),
    L(
        'a-an', 'A1', 'A and An', '英文 A1｜a、an 與複數',
        '單數可數名詞前面要有 a 或 an。母音開頭的音用 an，複數不再加 a。',
        'a、an 與複數名詞的差別，附例句、中文、朗讀與 PDF。',
        '看的是發音，不是字母。an hour 的 h 不發音，所以用 an。a university 開頭是 /ju/，所以用 a。',
        [
            G('a', '子音開頭的單數', [
                ['書', 'a book', '一本書'],
                ['學生', 'a student', '一個學生'],
                ['老師', 'a teacher', '一位老師'],
                ['大學', 'a university', '一所大學'],
            ], [
                ['I have a book.', '我有一本書。'],
                ['She is a student.', '她是一個學生。'],
                ['He is a teacher.', '他是一位老師。'],
                ['Taipei has a university.', '台北有一所大學。'],
            ]),
            G('an', '母音開頭的單數', [
                ['蘋果', 'an apple', '一顆蘋果'],
                ['點子', 'an idea', '一個點子'],
                ['小時', 'an hour', '一小時'],
                ['英文課', 'an English class', '一堂英文課'],
            ], [
                ['I want an apple.', '我要一顆蘋果。'],
                ['That is an idea.', '那是一個點子。'],
                ['Wait an hour.', '等一小時。'],
                ['We have an English class.', '我們有一堂英文課。'],
            ]),
            G('複數', '不加 a / an', [
                ['書', 'books', '書（多本）'],
                ['學生', 'students', '學生們'],
                ['蘋果', 'apples', '蘋果（多顆）'],
                ['朋友', 'friends', '朋友們'],
            ], [
                ['I have two books.', '我有兩本書。'],
                ['They are students.', '他們是學生。'],
                ['These apples are sweet.', '這些蘋果很甜。'],
                ['We are friends.', '我們是朋友。'],
            ]),
        ],
    ),
    L(
        'present-simple', 'A1', 'Present Simple', '英文 A1｜現在簡單式',
        '現在簡單式談習慣、事實和常做的事。第三人稱單數要加 -s。',
        '現在簡單式的肯定、否定和疑問，附例句、中文、朗讀與 PDF。',
        'he、she、it 的否定和疑問用 does，動詞不再加 -s：Does she like tea? 她喜歡茶嗎？',
        [
            G('肯定', '習慣與事實', [
                ['我／你／我們／他們', 'I work', '我工作'],
                ['他／她', 'he works', '他工作'],
                ['她喜歡', 'she likes', '她喜歡'],
                ['他們住', 'they live', '他們住'],
            ], [
                ['I work every day.', '我每天工作。'],
                ['He works in Taipei.', '他在台北工作。'],
                ['She likes tea.', '她喜歡茶。'],
                ['They live here.', '他們住在這裡。'],
            ]),
            G('否定', "don't / doesn't", [
                ['我', "I don't work", '我不工作'],
                ['你', "you don't like", '你不喜歡'],
                ['他', "he doesn't work", '他不工作'],
                ['她', "she doesn't like", '她不喜歡'],
            ], [
                ["I don't work on Sunday.", '我星期天不工作。'],
                ["You don't like coffee.", '你不喜歡咖啡。'],
                ["He doesn't work here.", '他不在這裡工作。'],
                ["She doesn't like milk.", '她不喜歡牛奶。'],
            ]),
            G('疑問', 'Do / Does', [
                ['你', 'Do you work?', '你工作嗎？'],
                ['他們', 'Do they live here?', '他們住這裡嗎？'],
                ['他', 'Does he work?', '他工作嗎？'],
                ['她', 'Does she like tea?', '她喜歡茶嗎？'],
            ], [
                ['Do you work every day?', '你每天工作嗎？'],
                ['Do they live in Taipei?', '他們住在台北嗎？'],
                ['Does he work here?', '他在這裡工作嗎？'],
                ['Does she like tea?', '她喜歡茶嗎？'],
            ]),
        ],
    ),
    L(
        'can', 'A1', 'Can', '英文 A1｜can',
        'can 表示做得到。後面直接接原形動詞，不隨人稱變化。',
        'can、cannot 和疑問句，附例句、中文、朗讀與 PDF。',
        "口語常把 cannot 縮成 can't。問句把 can 放到主詞前面。",
        [
            G('can', '做得到', [
                ['我', 'I can swim', '我會游泳'],
                ['你', 'you can help', '你能幫忙'],
                ['她', 'she can drive', '她會開車'],
                ['他們', 'they can come', '他們能來'],
            ], [
                ['I can swim.', '我會游泳。'],
                ['You can help me.', '你能幫我。'],
                ['She can drive.', '她會開車。'],
                ['They can come today.', '他們今天能來。'],
            ]),
            G("can't", '做不到', [
                ['我', "I can't drive", '我不會開車'],
                ['他', "he can't swim", '他不會游泳'],
                ['我們', "we can't stay", '我們不能留下'],
                ['她', "she can't come", '她不能來'],
            ], [
                ["I can't drive.", '我不會開車。'],
                ["He can't swim.", '他不會游泳。'],
                ["We can't stay long.", '我們不能留很久。'],
                ["She can't come tonight.", '她今晚不能來。'],
            ]),
            G('疑問', 'Can + 主詞', [
                ['你', 'Can you swim?', '你會游泳嗎？'],
                ['他', 'Can he help?', '他能幫忙嗎？'],
                ['她', 'Can she drive?', '她會開車嗎？'],
                ['他們', 'Can they come?', '他們能來嗎？'],
            ], [
                ['Can you swim?', '你會游泳嗎？'],
                ['Can he help me?', '他能幫我嗎？'],
                ['Can she drive?', '她會開車嗎？'],
                ['Can they come tomorrow?', '他們明天能來嗎？'],
            ]),
        ],
    ),
    L(
        'in-on-at', 'A1', 'In, On, At', '英文 A1｜in、on、at',
        'in 用在較大的地方、月份和早上；on 用在星期和某一天；at 用在幾點和較小的地點。',
        '時間與地點的 in、on、at，附例句、中文、朗讀與 PDF。',
        'at night、at home、in the morning 是固定說法。',
        [
            G('in', '範圍較大', [
                ['城市', 'in Taipei', '在台北'],
                ['月份', 'in July', '在七月'],
                ['早上', 'in the morning', '在早上'],
                ['年', 'in 2024', '在 2024 年'],
            ], [
                ['We are in Taipei.', '我們在台北。'],
                ['Her birthday is in July.', '她的生日在七月。'],
                ['I study in the morning.', '我早上讀書。'],
                ['He came in 2024.', '他在 2024 年來。'],
            ]),
            G('on', '某一天或表面', [
                ['星期', 'on Monday', '在星期一'],
                ['日期', 'on May 1', '在五月一日'],
                ['生日', 'on my birthday', '在我生日那天'],
                ['桌子上', 'on the desk', '在桌上'],
            ], [
                ['The class is on Monday.', '這堂課在星期一。'],
                ['We met on May 1.', '我們在五月一日見面。'],
                ['I rest on my birthday.', '我生日那天休息。'],
                ['The book is on the desk.', '書在桌上。'],
            ]),
            G('at', '時刻或小地點', [
                ['幾點', 'at seven', '在七點'],
                ['晚上', 'at night', '在晚上'],
                ['家', 'at home', '在家'],
                ['車站', 'at the station', '在車站'],
            ], [
                ['Class starts at seven.', '課在七點開始。'],
                ['I read at night.', '我晚上閱讀。'],
                ['She is at home.', '她在家。'],
                ['We met at the station.', '我們在車站見面。'],
            ]),
        ],
    ),
    L(
        'and-but-because', 'A1', 'And, But, Because', '英文 A1｜and、but、or、because',
        'and 把同類的東西接在一起，but 轉折，or 表示選擇，because 說明原因。',
        '四個最常用的連接詞，附例句、中文、朗讀與 PDF。',
        'because 後面是原因。結果用 so，下一階段再練。一句裡不要同時用 because 和 so。',
        [
            G('and / or', '並列或選擇', [
                ['和', 'tea and coffee', '茶和咖啡'],
                ['和', 'you and I', '你和我'],
                ['或', 'tea or coffee', '茶或咖啡'],
                ['或', 'Monday or Tuesday', '星期一或星期二'],
            ], [
                ['I like tea and coffee.', '我喜歡茶和咖啡。'],
                ['You and I are students.', '你和我是學生。'],
                ['Tea or coffee?', '茶還是咖啡？'],
                ['Monday or Tuesday is fine.', '星期一或星期二都可以。'],
            ]),
            G('but', '轉折', [
                ['但是', 'tired, but happy', '累但開心'],
                ['但是', 'small, but clean', '小但乾淨'],
                ['但是', 'hard, but useful', '難但有用'],
                ['但是', 'cold, but sunny', '冷但出太陽'],
            ], [
                ['I am tired, but I am happy.', '我很累，但我很開心。'],
                ['The room is small, but it is clean.', '房間很小，但很乾淨。'],
                ['English is hard, but it is useful.', '英文很難，但很有用。'],
                ['It is cold, but it is sunny.', '天氣很冷，但出太陽。'],
            ]),
            G('because', '原因', [
                ['因為', 'because it is late', '因為晚了'],
                ['因為', 'because I am tired', '因為我累了'],
                ['因為', 'because she is busy', '因為她很忙'],
                ['因為', 'because we like it', '因為我們喜歡'],
            ], [
                ['I stay home because it is late.', '因為晚了，我留在家。'],
                ['I rest because I am tired.', '因為我累了，所以休息。'],
                ['She cannot come because she is busy.', '她不能來，因為她很忙。'],
                ['We study English because we like it.', '我們學英文，因為我們喜歡它。'],
            ]),
        ],
    ),
]
