"""German A1 grammar aligned with Goethe Start Deutsch 1 (GER A1)."""
from lesson_util import G, L

LESSONS = [
    L(
        'pronomen', 'A1', 'Pronomen', '德文 A1｜人稱代名詞',
        '主詞用主格。她、他們和您都寫 sie，只有尊稱 Sie 要大寫。',
        'ich、du、Sie 的主格：六組人稱、她與他們的差別，附例句、中文、朗讀與 PDF。',
        'sie 小寫是她或他們。Sie 大寫是您，動詞用複數：Sie sind。\nes 指事物，也用於天氣和時間：Es ist kalt. Es ist acht Uhr.',
        [
            G('單數', '說話的人與對方', [
                ['我', 'ich', '我'],
                ['你（熟）', 'du', '你'],
                ['他', 'er', '他'],
                ['她', 'sie', '她'],
            ], [
                ['Ich wohne in Taipei.', '我住在台北。'],
                ['Du lernst Deutsch.', '你在學德文。'],
                ['Er ist Lehrer.', '他是老師。'],
                ['Sie ist Ärztin.', '她是醫生。'],
            ]),
            G('複數與尊稱', '我們、你們、他們、您', [
                ['我們', 'wir', '我們'],
                ['你們（熟）', 'ihr', '你們'],
                ['他們', 'sie', '他們'],
                ['您（尊稱）', 'Sie', '您'],
            ], [
                ['Wir sind Studenten.', '我們是學生。'],
                ['Ihr seid pünktlich.', '你們很準時。'],
                ['Sie kommen aus Berlin.', '他們來自柏林。'],
                ['Wie heißen Sie?', '您貴姓？'],
            ]),
            G('es', '事物、天氣、時間', [
                ['它', 'es', '它'],
                ['天氣', 'es ist kalt', '天氣冷'],
                ['時間', 'es ist acht Uhr', '現在八點'],
                ['下雨', 'es regnet', '下雨'],
            ], [
                ['Das Buch ist neu. Es ist interessant.', '這本書是新的。它很有趣。'],
                ['Es ist kalt heute.', '今天天氣冷。'],
                ['Es ist acht Uhr.', '現在八點。'],
                ['Es regnet heute.', '今天下雨。'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'praesens', 'A1', 'Präsens', '德文 A1｜現在式',
        '規則動詞照詞幹加人稱詞尾。詞幹母音 a 或 e 時，du 和 er 常常要換音。',
        '現在式的規則變化、多一個 e 的動詞，以及 sprechen、fahren 的換音，附例句、中文、朗讀與 PDF。',
        '只有 du 和 er／sie／es 換音。wir、ihr、sie、Sie 用原詞幹。\n詞幹以 -t、-d 結尾時，du 和 er 先加 e：du arbeitest，er arbeitet。',
        [
            G('規則動詞', 'wohnen 住', [
                ['ich', 'ich wohne', '我住'],
                ['du', 'du wohnst', '你住'],
                ['er / sie', 'er wohnt', '他住'],
                ['wir', 'wir wohnen', '我們住'],
                ['ihr', 'ihr wohnt', '你們住'],
                ['sie / Sie', 'sie wohnen', '他們／您住'],
            ], [
                ['Ich wohne in Taipei.', '我住在台北。'],
                ['Wohnst du in der Nähe?', '你住在附近嗎？'],
                ['Sie wohnt in Berlin.', '她住在柏林。'],
                ['Wir wohnen zusammen.', '我們住在一起。'],
            ]),
            G('詞幹 -t / -d', 'arbeiten 工作', [
                ['ich', 'ich arbeite', '我工作'],
                ['du', 'du arbeitest', '你工作'],
                ['er / sie', 'er arbeitet', '他工作'],
                ['ihr', 'ihr arbeitet', '你們工作'],
            ], [
                ['Ich arbeite in Taipei.', '我在台北工作。'],
                ['Arbeitest du am Montag?', '你星期一工作嗎？'],
                ['Er arbeitet bis sechs.', '他工作到六點。'],
                ['Arbeitet ihr heute?', '你們今天工作嗎？'],
            ]),
            G('換音', 'du 與 er 改變詞幹母音', [
                ['說', 'du sprichst / er spricht', '你說／他說'],
                ['你們說', 'ihr sprecht', '你們說（不換音）'],
                ['搭車', 'du fährst / er fährt', '你搭／他搭'],
                ['讀', 'du liest / er liest', '你讀／他讀'],
            ], [
                ['Sprichst du Deutsch?', '你說德文嗎？'],
                ['Er spricht langsam.', '他說得很慢。'],
                ['Sie fährt schnell.', '她開得很快。'],
                ['Er liest ein Buch.', '他在讀一本書。'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'fragen', 'A1', 'Fragen', '德文 A1｜問句與動詞位置',
        '是非問句把動詞放在第一位。有疑問詞時，疑問詞第一位，動詞緊接在後。陳述句的動詞永遠在第二位。',
        '是非問句、W 疑問詞，以及時間放句首時的動詞第二位，附例句、中文、朗讀與 PDF。',
        '時間放到句首，動詞仍緊跟在後，主詞退到動詞後面：Heute lerne ich Deutsch.\n不要說 Heute ich lerne。',
        [
            G('是非問句', '動詞放第一位', [
                ['住', 'Wohnst du hier?', '你住這裡嗎？'],
                ['說', 'Sprichst du Deutsch?', '你說德文嗎？'],
                ['是', 'Ist das richtig?', '這樣對嗎？'],
                ['有', 'Haben Sie Zeit?', '您有時間嗎？'],
            ], [
                ['Wohnst du in Taipei?', '你住在台北嗎？'],
                ['Sprichst du Englisch?', '你說英文嗎？'],
                ['Ist das richtig?', '這樣對嗎？'],
                ['Haben Sie eine Frage?', '您有問題嗎？'],
            ]),
            G('W 疑問詞', '疑問詞後立刻是動詞', [
                ['誰', 'wer', '誰'],
                ['什麼／哪裡', 'was / wo', '什麼／哪裡'],
                ['從哪裡／去哪裡', 'woher / wohin', '從哪裡／去哪裡'],
                ['如何／何時／為什麼', 'wie / wann / warum', '如何／何時／為什麼'],
            ], [
                ['Wo wohnst du?', '你住在哪裡？'],
                ['Woher kommen Sie?', '您從哪裡來？'],
                ['Wohin gehst du?', '你去哪裡？'],
                ['Warum lernst du Deutsch?', '你為什麼學德文？'],
            ]),
            G('動詞第二位', '陳述句', [
                ['主詞起頭', 'Ich lerne heute Deutsch.', '我今天學德文。'],
                ['時間起頭', 'Heute lerne ich Deutsch.', '今天我學德文。'],
                ['明天起頭', 'Morgen bleibe ich hier.', '明天我留在這裡。'],
                ['地點起頭', 'Hier wohne ich.', '我住在這裡。'],
            ], [
                ['Ich lerne jeden Tag Deutsch.', '我每天學德文。'],
                ['Heute bleibe ich zu Hause.', '今天我留在家裡。'],
                ['Jetzt lese ich.', '現在我讀書。'],
                ['In Berlin ist es kalt.', '柏林天氣冷。'],
            ]),
        ],
    ),
    L(
        'artikel', 'A1', 'Artikel', '德文 A1｜冠詞與名詞性別',
        '德文名詞有陽性、陰性、中性。冠詞要跟性別一起記，名詞第一個字母大寫。',
        'der、die、das 與 ein、eine：主格性別、不加冠詞的職業，附例句、中文、朗讀與 PDF。',
        '名詞第一個字母大寫：der Tisch，不是 tisch。\n職業和國籍用 sein 時通常不加冠詞：Ich bin Student. Sie ist Taiwanerin.',
        [
            G('定冠詞', '說話雙方都知道是哪一個', [
                ['陽性', 'der Tisch', '這張桌子'],
                ['陰性', 'die Lampe', '這盞燈'],
                ['中性', 'das Buch', '這本書'],
                ['複數', 'die Bücher', '這些書'],
            ], [
                ['Der Tisch ist neu.', '這張桌子是新的。'],
                ['Die Lampe ist klein.', '這盞燈很小。'],
                ['Das Buch ist interessant.', '這本書很有趣。'],
                ['Die Bücher sind hier.', '這些書在這裡。'],
            ]),
            G('不定冠詞', '某一個', [
                ['陽性', 'ein Tisch', '一張桌子'],
                ['陰性', 'eine Lampe', '一盞燈'],
                ['中性', 'ein Buch', '一本書'],
                ['複數', 'keine Bücher / Bücher', '複數不用 ein'],
            ], [
                ['Hier ist ein Tisch.', '這裡有一張桌子。'],
                ['Das ist eine Lampe.', '那是一盞燈。'],
                ['Das ist ein Buch.', '那是一本書。'],
                ['Wir brauchen Bücher.', '我們需要書。'],
            ]),
            G('不加冠詞', '職業、國籍、材料', [
                ['職業', 'Ich bin Student.', '我是學生。'],
                ['國籍', 'Sie ist Taiwanerin.', '她是台灣人。'],
                ['語言', 'Ich lerne Deutsch.', '我學德文。'],
                ['材料', 'Ich trinke Wasser.', '我喝水。'],
            ], [
                ['Er ist Arzt.', '他是醫生。'],
                ['Ich bin Taiwaner.', '我是台灣人。'],
                ['Wir sprechen Deutsch.', '我們說德文。'],
                ['Ich trinke Wasser.', '我喝水。'],
            ]),
        ],
    ),
    L(
        'zeit', 'A1', 'Zeit', '德文 A1｜時間',
        '幾點用 um，星期用 am，月份用 im。半點用 halb，指的是下一個整點之前三十分。',
        'um、am、im，以及 halb、Viertel nach、Viertel vor，附例句、中文、朗讀與 PDF。',
        'halb acht 是七點半，不是八點半。\nViertel nach sieben 是七點十五。Viertel vor acht 是七點四十五。',
        [
            G('幾點', 'um 加鐘點', [
                ['整點', 'um acht Uhr', '八點'],
                ['半點', 'halb acht', '七點半'],
                ['過一刻', 'Viertel nach sieben', '七點十五'],
                ['差一刻', 'Viertel vor acht', '七點四十五'],
            ], [
                ['Es ist acht Uhr.', '現在八點。'],
                ['Es ist halb acht.', '現在七點半。'],
                ['Der Kurs beginnt um neun.', '課九點開始。'],
                ['Es ist Viertel vor neun.', '現在八點四十五。'],
            ]),
            G('星期與月份', 'am 與 im', [
                ['星期一', 'am Montag', '在星期一'],
                ['週末', 'am Wochenende', '在週末'],
                ['五月', 'im Mai', '在五月'],
                ['夏天', 'im Sommer', '在夏天'],
            ], [
                ['Am Montag arbeite ich.', '我星期一工作。'],
                ['Am Wochenende bleibe ich zu Hause.', '週末我留在家裡。'],
                ['Im Mai ist es warm.', '五月天氣暖和。'],
                ['Im Sommer ist es heiß.', '夏天天氣熱。'],
            ]),
            G('一天的時段', '上午、傍晚、夜裡', [
                ['早上', 'am Morgen', '在早上'],
                ['下午', 'am Nachmittag', '在下午'],
                ['晚上', 'am Abend', '在晚上'],
                ['夜裡', 'in der Nacht', '在夜裡'],
            ], [
                ['Am Morgen trinke ich Kaffee.', '早上我喝咖啡。'],
                ['Am Nachmittag lerne ich.', '下午我學習。'],
                ['Am Abend lese ich.', '晚上我讀書。'],
                ['In der Nacht schlafe ich.', '夜裡我睡覺。'],
            ]),
        ],
    ),
    L(
        'plural', 'A1', 'Plural', '德文 A1｜名詞複數',
        '複數沒有單一規則，要跟名詞一起記。複數定冠詞一律是 die。',
        '常見的 -e、-(e)n、-er、-s，以及不加詞尾的複數，附例句、中文、朗讀與 PDF。',
        '複數冠詞一律 die，不再用 der 或 das。\n有的複數還會變音：der Stuhl，die Stühle。das Buch，die Bücher。',
        [
            G('-e', '常伴隨著變音', [
                ['日子', 'der Tag / die Tage', '日子'],
                ['筆', 'der Stift / die Stifte', '筆'],
                ['椅子', 'der Stuhl / die Stühle', '椅子'],
                ['城市', 'die Stadt / die Städte', '城市'],
            ], [
                ['Die Tage sind lang.', '這些日子很長。'],
                ['Ich habe zwei Stifte.', '我有兩枝筆。'],
                ['Die Stühle sind frei.', '這些椅子是空的。'],
                ['Die Städte sind alt.', '這些城市很古老。'],
            ]),
            G('-(e)n', '陰性名詞最常見', [
                ['女人', 'die Frau / die Frauen', '女人'],
                ['燈', 'die Lampe / die Lampen', '燈'],
                ['問題', 'die Frage / die Fragen', '問題'],
                ['學生', 'der Student / die Studenten', '學生'],
            ], [
                ['Die Frauen sprechen Deutsch.', '這些女人說德文。'],
                ['Die Lampen sind an.', '燈是開著的。'],
                ['Ich habe zwei Fragen.', '我有兩個問題。'],
                ['Die Studenten lernen viel.', '學生們學得很多。'],
            ]),
            G('-er、-s、不變', '要整組記住', [
                ['孩子', 'das Kind / die Kinder', '孩子'],
                ['書', 'das Buch / die Bücher', '書'],
                ['汽車', 'das Auto / die Autos', '汽車'],
                ['老師', 'der Lehrer / die Lehrer', '老師'],
            ], [
                ['Die Kinder spielen.', '孩子們在玩。'],
                ['Die Bücher sind neu.', '這些書是新的。'],
                ['Die Autos sind teuer.', '這些車很貴。'],
                ['Die Lehrer sind freundlich.', '老師們很親切。'],
            ]),
        ],
    ),
    L(
        'akkusativ', 'A1', 'Akkusativ', '德文 A1｜受格',
        '動詞的直接受詞用受格。只有陽性單數的冠詞會變：der 變成 den，ein 變成 einen。',
        '受格冠詞與人稱代名詞：mich、dich、ihn，附例句、中文、朗讀與 PDF。',
        '陰性、中性和複數的受格冠詞看起來和主格一樣。\n真正會變的是陽性單數：den Mann，einen Kaffee。',
        [
            G('冠詞', '只有陽性單數改變', [
                ['陽性', 'den Mann / einen Kaffee', '這個男人／一杯咖啡'],
                ['陰性', 'die Frau / eine Lampe', '這個女人／一盞燈'],
                ['中性', 'das Buch / ein Buch', '這本書／一本書'],
                ['複數', 'die Bücher', '這些書'],
            ], [
                ['Ich sehe den Mann.', '我看見那個男人。'],
                ['Sie kauft einen Kaffee.', '她買一杯咖啡。'],
                ['Wir lesen das Buch.', '我們讀這本書。'],
                ['Er braucht die Bücher.', '他需要這些書。'],
            ]),
            G('人稱代名詞', '動詞後面的人', [
                ['我', 'mich', '我'],
                ['你', 'dich', '你'],
                ['他／她／它', 'ihn / sie / es', '他／她／它'],
                ['我們／你們', 'uns / euch', '我們／你們'],
                ['他們／您', 'sie / Sie', '他們／您'],
            ], [
                ['Sie kennt mich.', '她認識我。'],
                ['Ich sehe dich.', '我看見你。'],
                ['Wir besuchen ihn morgen.', '我們明天去看他。'],
                ['Kennt ihr uns?', '你們認識我們嗎？'],
            ]),
            G('es gibt', '有，後面用受格', [
                ['陽性', 'es gibt einen Park', '有一座公園'],
                ['陰性', 'es gibt eine Bäckerei', '有一家麵包店'],
                ['中性', 'es gibt ein Kino', '有一家電影院'],
                ['疑問', 'Gibt es hier einen Supermarkt?', '這裡有超市嗎？'],
            ], [
                ['Es gibt einen Park in der Nähe.', '附近有一座公園。'],
                ['Es gibt eine Bäckerei um die Ecke.', '轉角有一家麵包店。'],
                ['Gibt es hier ein Café?', '這裡有咖啡館嗎？'],
                ['Es gibt heute einen Kurs.', '今天有一堂課。'],
            ]),
        ],
    ),
    L(
        'possessiv', 'A1', 'Possessiv', '德文 A1｜所有格冠詞',
        '所有格冠詞跟著後面的名詞變，不跟著主人的性別變。用法和 ein 同一套。',
        'mein、dein、sein、ihr、unser、euer、Ihr 的主格與陽性受格，附例句、中文、朗讀與 PDF。',
        '詞尾看後面的名詞：mein Bruder，meine Schwester，mein Kind。\neuer 加詞尾時去掉一個 e：eure Lehrerin。尊稱您的要大寫：Ihr Buch。',
        [
            G('單數主人', '我的、你的、他的、她的', [
                ['我的', 'mein Name / meine Tasche', '我的名字／我的袋子'],
                ['你的', 'dein Bruder / deine Schwester', '你的兄弟／你的姊妹'],
                ['他的', 'sein Kurs', '他的課'],
                ['她的', 'ihre Freundin', '她的女性朋友'],
            ], [
                ['Mein Name ist Hao-Cheng.', '我的名字是 Hao-Cheng。'],
                ['Deine Tasche ist neu.', '你的袋子是新的。'],
                ['Sein Bruder wohnt in Berlin.', '他的兄弟住在柏林。'],
                ['Das ist ihre Schwester.', '這是她的姊妹。'],
            ]),
            G('複數與尊稱', '我們的、你們的、您的', [
                ['我們的', 'unser Kurs', '我們的課'],
                ['你們的', 'eure Lehrerin', '你們的女老師'],
                ['他們的', 'ihre Freunde', '他們的朋友'],
                ['您的', 'Ihr Pass', '您的護照'],
            ], [
                ['Unser Kurs beginnt um neun.', '我們的課九點開始。'],
                ['Eure Lehrerin ist freundlich.', '你們的女老師很親切。'],
                ['Ich kenne ihre Freunde.', '我認識他們的朋友。'],
                ['Ist das Ihr Buch?', '這是您的書嗎？'],
            ]),
            G('陽性受格', 'mein 變成 meinen', [
                ['主格', 'mein Stift', '我的筆'],
                ['受格', 'meinen Stift', '我的筆（受格）'],
                ['陰性不變', 'meine Tasche', '我的袋子'],
                ['中性不變', 'mein Buch', '我的書'],
            ], [
                ['Ich nehme meinen Stift.', '我拿我的筆。'],
                ['Sie sucht ihren Schlüssel.', '她在找她的鑰匙。'],
                ['Er liest sein Buch.', '他讀他的書。'],
                ['Wir besuchen unsere Lehrerin.', '我們去看我們的女老師。'],
            ]),
        ],
    ),
    L(
        'negation', 'A1', 'Nicht und Kein', '德文 A1｜nicht 與 kein',
        '否定名詞用 kein。否定動詞、形容詞或介系詞片語用 nicht。',
        'nicht 與 kein 的位置和詞尾，附例句、中文、朗讀與 PDF。',
        '有冠詞或想說沒有某個名詞時用 kein：kein Auto，keine Zeit，keinen Kaffee。\nnicht 常放在句尾，或放在形容詞和介系詞片語前面。',
        [
            G('nicht', '否定動詞、形容詞、地方', [
                ['動詞', 'Ich arbeite nicht.', '我不工作。'],
                ['形容詞', 'Das ist nicht teuer.', '那不貴。'],
                ['地方', 'Sie ist nicht in Berlin.', '她不在柏林。'],
                ['時間', 'Heute lerne ich nicht.', '我今天不學習。'],
            ], [
                ['Ich arbeite am Sonntag nicht.', '我星期天不工作。'],
                ['Das Buch ist nicht neu.', '這本書不是新的。'],
                ['Er kommt heute nicht.', '他今天不來。'],
                ['Am Abend koche ich nicht.', '晚上我不煮飯。'],
            ]),
            G('kein', '否定名詞，詞尾像 ein', [
                ['陽性主格', 'kein Kurs', '沒有課'],
                ['陽性受格', 'keinen Kaffee', '沒有咖啡'],
                ['陰性', 'keine Zeit', '沒有時間'],
                ['複數', 'keine Bücher', '沒有書'],
            ], [
                ['Ich habe kein Auto.', '我沒有車。'],
                ['Sie kauft keinen Kaffee.', '她不買咖啡。'],
                ['Wir haben keine Zeit.', '我們沒有時間。'],
                ['Hier gibt es keine Milch.', '這裡沒有牛奶。'],
            ]),
            G('對比', '同一個意思不要混用', [
                ['不是老師', 'Er ist nicht Lehrer.', '他不是老師。'],
                ['沒有老師', 'Es gibt keinen Lehrer.', '沒有老師。'],
                ['不貴', 'Das ist nicht teuer.', '那不貴。'],
                ['沒有問題', 'Ich habe keine Frage.', '我沒有問題。'],
            ], [
                ['Ich bin nicht müde.', '我不累。'],
                ['Ich habe keinen Hunger.', '我不餓。'],
                ['Das ist kein Fehler.', '那不是錯誤。'],
                ['Sie spricht nicht laut.', '她說話不大聲。'],
            ]),
        ],
    ),
    L(
        'koennen', 'A1', 'Können', '德文 A1｜können 與 möchten',
        'können 是做得到。möchten 是想要，語氣比 wollen 客氣。兩個都把真正的動詞以原形放在句尾。',
        'können、möchten 的變位，以及句尾原形，附例句、中文、朗讀與 PDF。',
        '情態動詞自己變位，句尾動詞用原形：Ich kann Deutsch sprechen.\nmöchten 的完整形式是 möchte、möchtest、möchte、möchten、möchtet、möchten。',
        [
            G('können', '做得到', [
                ['ich', 'ich kann', '我能'],
                ['du', 'du kannst', '你能'],
                ['er / sie', 'er kann', '他能'],
                ['wir', 'wir können', '我們能'],
                ['ihr', 'ihr könnt', '你們能'],
                ['sie / Sie', 'sie können', '他們／您能'],
            ], [
                ['Ich kann schwimmen.', '我會游泳。'],
                ['Kannst du Deutsch sprechen?', '你會說德文嗎？'],
                ['Sie kann gut kochen.', '她很會煮飯。'],
                ['Wir können heute kommen.', '我們今天能來。'],
            ]),
            G('möchten', '想要，語氣客氣', [
                ['ich', 'ich möchte', '我想要'],
                ['du', 'du möchtest', '你想要'],
                ['er / sie', 'er möchte', '他想要'],
                ['Sie', 'Was möchten Sie?', '您想要什麼？'],
            ], [
                ['Ich möchte einen Kaffee.', '我想要一杯咖啡。'],
                ['Möchtest du Wasser?', '你想喝水嗎？'],
                ['Er möchte nach Hause gehen.', '他想回家。'],
                ['Was möchten Sie trinken?', '您想喝什麼？'],
            ]),
            G('句尾原形', '第二個動詞不變化', [
                ['說', 'Ich kann Deutsch sprechen.', '我會說德文。'],
                ['讀', 'Kannst du Deutsch lesen?', '你能讀德文嗎？'],
                ['來', 'Sie können um acht kommen.', '您可以八點來。'],
                ['學習', 'Ich möchte Deutsch lernen.', '我想學德文。'],
            ], [
                ['Ich kann heute nicht kommen.', '我今天不能來。'],
                ['Kannst du das Fenster öffnen?', '你能打開窗戶嗎？'],
                ['Wir möchten hier bleiben.', '我們想留在這裡。'],
                ['Sie kann sehr gut singen.', '她很會唱歌。'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'imperativ', 'A1', 'Imperativ', '德文 A1｜命令句',
        '對熟人 du 通常拿掉人稱詞尾。對你們用 ihr 的動詞、不說 ihr。對您要把 Sie 說出來。',
        'du、ihr、Sie 三種命令句，以及 sein 的不規則形式，附例句、中文、朗讀與 PDF。',
        'sein 的命令句是 Sei!、Seid!、Seien Sie!。\n換音動詞用換過的詞幹：Sprich langsam! Lies den Text!',
        [
            G('du', '對一個熟人', [
                ['來', 'Komm!', '來！'],
                ['學習', 'Lern jeden Tag!', '每天學習！'],
                ['說', 'Sprich langsam!', '說慢一點！'],
                ['是', 'Sei pünktlich!', '準時一點！'],
            ], [
                ['Komm bitte herein!', '請進來！'],
                ['Lern Deutsch jeden Tag!', '每天學德文！'],
                ['Sprich langsamer!', '說慢一點！'],
                ['Sei nicht laut!', '不要大聲！'],
            ]),
            G('ihr', '對幾個熟人', [
                ['來', 'Kommt!', '你們來！'],
                ['讀', 'Lest den Text!', '你們讀課文！'],
                ['是', 'Seid leise!', '你們安靜！'],
                ['工作', 'Arbeitet zusammen!', '你們一起做！'],
            ], [
                ['Kommt bitte pünktlich!', '請你們準時來！'],
                ['Lest die Frage noch einmal!', '請你們再讀一次問題！'],
                ['Seid ruhig!', '你們安靜！'],
                ['Arbeitet nicht so schnell!', '你們別做得那麼快！'],
            ]),
            G('Sie', '對尊稱，動詞用原形', [
                ['來', 'Kommen Sie!', '您來！'],
                ['讀', 'Lesen Sie den Text!', '請您讀課文！'],
                ['說', 'Sprechen Sie langsam!', '請您說慢一點！'],
                ['是', 'Seien Sie pünktlich!', '請您準時！'],
            ], [
                ['Kommen Sie bitte herein!', '請進！'],
                ['Lesen Sie die erste Seite!', '請讀第一頁！'],
                ['Sprechen Sie Deutsch!', '請說德文！'],
                ['Seien Sie so nett!', '請幫個忙！'],
            ]),
        ],
    ),
]
