"""French A1 grammar aligned with DELF A1 (CECRL)."""
from lesson_util import G, L

LESSONS = [
    L(
        'bonjour-verbes', 'A1', 'Bonjour Verbes', '法文 A1｜être、avoir、s’appeler',
        '自我介紹先記這三個動詞。être 是「是」，avoir 是「有」，s’appeler 是「叫做」。年齡用 avoir，不用 être。',
        'être、avoir、s’appeler 的現在式：六組人稱、例句、中文翻譯、朗讀與 PDF。',
        '女性要配合性別：étudiante、française、prête。\n年齡用 avoir：J’ai 25 ans. s’appeler 在 nous 不重複子音：nous nous appelons。',
        [
            G('être', '是', [
                ['je', 'je suis', '我是'],
                ['tu', 'tu es', '你是'],
                ['il / elle', 'il / elle est', '他／她是'],
                ['nous', 'nous sommes', '我們是'],
                ['vous', 'vous êtes', '您／你們是'],
                ['ils / elles', 'ils / elles sont', '他們／她們是'],
            ], [
                ['Je suis étudiant.', '我是學生。'],
                ['Tu es prêt ?', '你準備好了嗎？'],
                ['Elle est française.', '她是法國人。'],
                ['Nous sommes à Taipei.', '我們在台北。'],
            ]),
            G('avoir', '有；年齡', [
                ['je', 'j’ai', '我有'],
                ['tu', 'tu as', '你有'],
                ['il / elle', 'il / elle a', '他／她有'],
                ['nous', 'nous avons', '我們有'],
                ['vous', 'vous avez', '您／你們有'],
                ['ils / elles', 'ils / elles ont', '他們／她們有'],
            ], [
                ['J’ai 25 ans.', '我二十五歲。'],
                ['Tu as un livre ?', '你有一本書嗎？'],
                ['Il a un frère.', '他有一個兄弟。'],
                ['Nous avons un cours.', '我們有一堂課。'],
            ]),
            G('s’appeler', '叫做', [
                ['je', 'je m’appelle', '我叫'],
                ['tu', 'tu t’appelles', '你叫'],
                ['il / elle', 'il / elle s’appelle', '他／她叫'],
                ['nous', 'nous nous appelons', '我們叫'],
                ['vous', 'vous vous appelez', '您／你們叫'],
                ['ils / elles', 'ils / elles s’appellent', '他們／她們叫'],
            ], [
                ['Je m’appelle Hao-Cheng.', '我叫 Hao-Cheng。'],
                ['Tu t’appelles comment ?', '你叫什麼名字？'],
                ['Elle s’appelle Marie.', '她叫 Marie。'],
                ['Vous vous appelez comment ?', '您貴姓？'],
            ]),
        ],
        cols=('人稱', '現在式', '中文'),
    ),
    L(
        'articles', 'A1', 'Articles', '法文 A1｜冠詞',
        '不定冠詞指某一個尚未特定的東西。定冠詞指雙方都知道的東西。à 和 de 碰到 le、les 要縮成一個詞。',
        'un、une、des，le、la、les，以及 au、du、aux，附例句、中文、朗讀與 PDF。',
        '母音或啞音 h 前面，le 和 la 寫成 l’：l’école、l’hôtel。\nà le 要寫 au，à les 要寫 aux。de le 要寫 du，de les 要寫 des。',
        [
            G('不定冠詞', '某一個、一些', [
                ['一個（陽）', 'un café', '一家咖啡館'],
                ['一個（陰）', 'une école', '一所學校'],
                ['一些', 'des amis', '一些朋友'],
                ['問句', 'Tu as un stylo ?', '你有筆嗎？'],
            ], [
                ['C’est un livre.', '這是一本書。'],
                ['J’ai une question.', '我有一個問題。'],
                ['Nous avons des cours le matin.', '我們早上有課。'],
                ['Tu veux un café ?', '你要一杯咖啡嗎？'],
            ]),
            G('定冠詞', '特定的那個', [
                ['陽', 'le livre', '這本書'],
                ['陰', 'la gare', '火車站'],
                ['母音前', 'l’hôtel', '旅館'],
                ['複數', 'les enfants', '孩子們'],
            ], [
                ['Le livre est sur la table.', '書在桌上。'],
                ['La gare est près d’ici.', '火車站在附近。'],
                ['L’hôtel est ouvert.', '旅館開著。'],
                ['Les enfants sont à l’école.', '孩子們在學校。'],
            ]),
            G('縮約', 'à 與 de 碰到 le、les', [
                ['à + le', 'au marché', '去市場'],
                ['à + les', 'aux étudiants', '對學生們'],
                ['de + le', 'du professeur', '老師的'],
                ['de + les', 'des enfants', '孩子們的'],
            ], [
                ['Nous allons au marché.', '我們去市場。'],
                ['Je parle aux étudiants.', '我在跟學生說話。'],
                ['C’est le livre du professeur.', '這是老師的書。'],
                ['Je connais les noms des étudiants.', '我知道學生們的名字。'],
            ]),
        ],
    ),
    L(
        'adjectifs', 'A1', 'Adjectifs', '法文 A1｜形容詞',
        '形容詞要配合名詞的性和數。多數形容詞放在名詞後面。少數常見的放在前面，其中 beau、nouveau、vieux 在母音前要改形。',
        '性數配合、前後位置，以及 bel、nouvel、vieil，附例句、中文、朗讀與 PDF。',
        '放在名詞前的常見形容詞有 beau、bon、grand、jeune、joli、petit、vieux、nouveau。\n陽性和母音名詞之間：beau → bel，nouveau → nouvel，vieux → vieil。',
        [
            G('性與數', '跟著名詞變', [
                ['陽', 'grand', '高'],
                ['陰', 'grande', '高'],
                ['陽複', 'intéressants', '有趣'],
                ['陰複', 'intéressantes', '有趣'],
            ], [
                ['Paul est grand.', 'Paul 個子高。'],
                ['Marie est grande.', 'Marie 個子高。'],
                ['Ces livres sont intéressants.', '這些書很有趣。'],
                ['Ces questions sont intéressantes.', '這些問題很有趣。'],
            ]),
            G('位置', '前與後', [
                ['前面', 'une petite maison', '一間小房子'],
                ['後面', 'une robe rouge', '一件紅洋裝'],
                ['好', 'un bon café', '一杯好咖啡'],
                ['年輕', 'une jeune femme', '一位年輕女子'],
            ], [
                ['J’habite une petite maison.', '我住一間小房子。'],
                ['Elle porte une robe rouge.', '她穿一件紅洋裝。'],
                ['C’est un bon café.', '這是一杯好咖啡。'],
                ['Marc est un jeune homme.', 'Marc 是一位年輕人。'],
            ]),
            G('母音前', 'bel、nouvel、vieil', [
                ['美', 'un bel appartement', '一間漂亮的公寓'],
                ['新', 'un nouvel ami', '一位新朋友'],
                ['老', 'un vieil ami', '一位老朋友'],
                ['陰', 'une belle ville', '一座漂亮的城市'],
            ], [
                ['C’est un bel appartement.', '這是一間漂亮的公寓。'],
                ['J’ai un nouvel ami.', '我有一位新朋友。'],
                ['Paul est un vieil ami.', 'Paul 是一位老朋友。'],
                ['Taipei est une belle ville.', '台北是一座漂亮的城市。'],
            ]),
        ],
    ),
    L(
        'negation', 'A1', 'Négation', '法文 A1｜ne…pas',
        '否定把 ne 放在動詞前，pas 放在動詞後。je 後面如果是母音，ne 寫成 n’。否定句裡，不定冠詞 un、une、des 常改成 de。',
        'ne…pas、省音，以及 pas de，附例句、中文、朗讀與 PDF。',
        '有代詞時，ne 放在代詞前：Je ne le vois pas. 這會在 A2 再練。\nIl n’y a pas de 後面直接接名詞，不加 un 或 une。',
        [
            G('ne…pas', '不是、沒有做', [
                ['不是', 'je ne suis pas', '我不是'],
                ['沒有', 'je n’ai pas', '我沒有'],
                ['不住', 'il n’habite pas', '他不住'],
                ['不說', 'nous ne parlons pas', '我們不說'],
            ], [
                ['Je ne suis pas médecin.', '我不是醫生。'],
                ['Je n’ai pas de frère.', '我沒有兄弟。'],
                ['Il n’habite pas ici.', '他不住這裡。'],
                ['Nous ne parlons pas anglais.', '我們不說英文。'],
            ]),
            G('省音', '母音前 n’', [
                ['不喜歡', 'je n’aime pas', '我不喜歡'],
                ['不是', 'ce n’est pas', '這不是'],
                ['沒有', 'il n’y a pas', '沒有'],
                ['你不是', 'tu n’es pas', '你不是'],
            ], [
                ['Je n’aime pas le café.', '我不喜歡咖啡。'],
                ['Ce n’est pas mon sac.', '這不是我的袋子。'],
                ['Il n’y a pas de sucre.', '沒有糖。'],
                ['Tu n’es pas en retard.', '你沒有遲到。'],
            ]),
            G('pas de', '否定後不再用 un', [
                ['沒有書', 'pas de livre', '沒有書'],
                ['沒有朋友', 'pas d’amis', '沒有朋友'],
                ['沒有課', 'pas de cours', '沒有課'],
                ['沒有問題', 'pas de problème', '沒問題'],
            ], [
                ['Je n’ai pas de stylo.', '我沒有筆。'],
                ['Elle n’a pas d’enfants.', '她沒有孩子。'],
                ['Nous n’avons pas de cours aujourd’hui.', '我們今天沒有課。'],
                ['Il n’y a pas de problème.', '沒問題。'],
            ]),
        ],
    ),
    L(
        'questions', 'A1', 'Questions', '法文 A1｜提問',
        '口語最穩的問法是 est-ce que。疑問詞放在句首。對您說話時，也可以把動詞和 vous 倒過來。',
        'est-ce que、où、comment、quel，附例句、中文、朗讀與 PDF。',
        'quel 要配性數：quel、quelle、quels、quelles。\n問名字可以說 Tu t’appelles comment ? 對您說 Comment vous appelez-vous ?',
        [
            G('est-ce que', '是不是', [
                ['你說', 'Est-ce que tu parles français ?', '你說法文嗎？'],
                ['您住', 'Est-ce que vous habitez ici ?', '您住這裡嗎？'],
                ['她來', 'Est-ce qu’elle vient ?', '她來嗎？'],
                ['有', 'Est-ce qu’il y a un café ?', '有咖啡館嗎？'],
            ], [
                ['Est-ce que tu parles français ?', '你說法文嗎？'],
                ['Est-ce que vous habitez à Taipei ?', '您住台北嗎？'],
                ['Est-ce qu’elle vient demain ?', '她明天來嗎？'],
                ['Est-ce qu’il y a une banque près d’ici ?', '附近有銀行嗎？'],
            ]),
            G('疑問詞', '哪裡、如何、什麼', [
                ['哪裡', 'Où habites-tu ?', '你住哪裡？'],
                ['如何', 'Comment allez-vous ?', '您好嗎？'],
                ['什麼', 'Qu’est-ce que c’est ?', '這是什麼？'],
                ['為什麼', 'Pourquoi tu étudies le français ?', '你為什麼學法文？'],
            ], [
                ['Où est la gare ?', '火車站在哪裡？'],
                ['Comment allez-vous ?', '您好嗎？'],
                ['Qu’est-ce que vous faites ?', '您在做什麼？'],
                ['Pourquoi est-ce que tu restes ?', '你為什麼留下？'],
            ]),
            G('quel', '哪一個', [
                ['陽', 'Quel livre ?', '哪一本書？'],
                ['陰', 'Quelle heure est-il ?', '現在幾點？'],
                ['陽複', 'Quels jours ?', '哪幾天？'],
                ['陰複', 'Quelles langues ?', '哪些語言？'],
            ], [
                ['Quel est ton nom ?', '你叫什麼名字？'],
                ['Quelle heure est-il ?', '現在幾點？'],
                ['Quels jours travailles-tu ?', '你哪幾天工作？'],
                ['Quelles langues est-ce que vous parlez ?', '您會說哪些語言？'],
            ]),
        ],
    ),
    L(
        'verbes-er', 'A1', 'Verbes en -er', '法文 A1｜-er 動詞',
        '大多數動詞是 -er。去掉 -er 之後，照人稱加詞尾。nous 的詞尾是 -ons。manger 在 nous 要保留 e，acheter 在單數要把 e 改成 è。',
        'parler、manger、acheter 的現在式，附例句、中文、朗讀與 PDF。',
        'je、tu、il、ils 的詞尾不發音，所以 parle、parles、parlent 聽起來一樣。\n母音前 je 省成 j’：j’habite、j’aime、j’achète。',
        [
            G('parler', '說', [
                ['je', 'je parle', '我說'],
                ['tu', 'tu parles', '你說'],
                ['il / elle', 'il parle', '他說'],
                ['nous', 'nous parlons', '我們說'],
                ['vous', 'vous parlez', '您說'],
                ['ils / elles', 'ils parlent', '他們說'],
            ], [
                ['Je parle français.', '我說法文。'],
                ['Tu parles anglais ?', '你說英文嗎？'],
                ['Elle parle lentement.', '她說得很慢。'],
                ['Nous parlons de Taipei.', '我們在談台北。'],
            ]),
            G('manger', 'nous 保留 e', [
                ['je', 'je mange', '我吃'],
                ['nous', 'nous mangeons', '我們吃'],
                ['vous', 'vous mangez', '您吃'],
                ['開始', 'nous commençons', '我們開始'],
            ], [
                ['Je mange à midi.', '我中午吃飯。'],
                ['Nous mangeons ensemble.', '我們一起吃。'],
                ['Vous mangez où ?', '您在哪裡吃？'],
                ['Nous commençons à neuf heures.', '我們九點開始。'],
            ]),
            G('acheter', '單數改成 è', [
                ['je', 'j’achète', '我買'],
                ['tu', 'tu achètes', '你買'],
                ['nous', 'nous achetons', '我們買'],
                ['ils', 'ils achètent', '他們買'],
            ], [
                ['J’achète un livre.', '我買一本書。'],
                ['Tu achètes une pomme ?', '你買一顆蘋果嗎？'],
                ['Nous achetons des billets.', '我們買票。'],
                ['Ils achètent une maison.', '他們買一間房子。'],
            ]),
        ],
        cols=('人稱', '現在式', '中文'),
    ),
    L(
        'aller-faire', 'A1', 'Aller et faire', '法文 A1｜aller、faire、venir',
        '這三個動詞不照 -er 的規則。aller 加原形動詞，表示即將做。faire 也用來講天氣。venir 常和 de 一起，表示從哪裡來。',
        'aller、faire、venir 的現在式，以及 aller 加原形，附例句、中文、朗讀與 PDF。',
        'aller 的 vous 是 allez，ils 是 vont。\n即將發生用 aller + 原形：Je vais partir. 天氣用 faire：Il fait beau.',
        [
            G('aller', '去；即將', [
                ['je', 'je vais', '我去'],
                ['tu', 'tu vas', '你去'],
                ['il / elle', 'il va', '他去'],
                ['nous', 'nous allons', '我們去'],
                ['vous', 'vous allez', '您去'],
                ['ils / elles', 'ils vont', '他們去'],
            ], [
                ['Je vais à l’école.', '我去學校。'],
                ['Tu vas bien ?', '你好嗎？'],
                ['Nous allons au marché.', '我們去市場。'],
                ['Je vais prendre un café.', '我要去喝杯咖啡。'],
            ]),
            G('faire', '做；天氣', [
                ['je', 'je fais', '我做'],
                ['tu', 'tu fais', '你做'],
                ['il / elle', 'il fait', '他做'],
                ['nous', 'nous faisons', '我們做'],
                ['vous', 'vous faites', '您做'],
                ['ils / elles', 'ils font', '他們做'],
            ], [
                ['Je fais mes devoirs.', '我在寫作業。'],
                ['Il fait beau aujourd’hui.', '今天天氣很好。'],
                ['Vous faites la cuisine ?', '您在做飯嗎？'],
                ['Ils font leurs devoirs.', '他們在寫作業。'],
            ]),
            G('venir', '來；從哪裡來', [
                ['je', 'je viens', '我來'],
                ['tu', 'tu viens', '你來'],
                ['il / elle', 'il vient', '他來'],
                ['nous', 'nous venons', '我們來'],
                ['vous', 'vous venez', '您來'],
                ['ils / elles', 'ils viennent', '他們來'],
            ], [
                ['Je viens de Taipei.', '我從台北來。'],
                ['Tu viens d’où ?', '你從哪裡來？'],
                ['Elle vient demain.', '她明天來。'],
                ['Ils viennent avec nous.', '他們跟我們一起來。'],
            ]),
        ],
        cols=('人稱', '現在式', '中文'),
    ),
    L(
        'prepositions', 'A1', 'Prépositions', '法文 A1｜介詞與地點',
        '城市用 à。陰性國家用 en，陽性國家用 au，複數國家用 aux。chez 是在某人那裡。dans 是在裡面，sur 是在上面。',
        'à、en、au、chez、dans、sur，附例句、中文、朗讀與 PDF。',
        '陰性國家用 en：en France、en Chine。城市用 à：à Paris、à Taipei。台灣常說 à Taïwan。\n從哪裡來：venir de Taipei、venir de France、venir du Japon。',
        [
            G('城市與國家', 'à、en、au', [
                ['城市', 'à Taipei', '在台北'],
                ['陰性國家', 'en France', '在法國'],
                ['陽性國家', 'au Japon', '在日本'],
                ['複數', 'aux États-Unis', '在美國'],
            ], [
                ['J’habite à Taipei.', '我住在台北。'],
                ['Il travaille en France.', '他在法國工作。'],
                ['Nous allons au Japon.', '我們要去日本。'],
                ['Elle habite aux États-Unis.', '她住在美國。'],
            ]),
            G('chez、dans、sur', '在哪裡', [
                ['某人那裡', 'chez mes parents', '在我父母家'],
                ['裡面', 'dans le sac', '在袋子裡'],
                ['上面', 'sur la table', '在桌上'],
                ['附近', 'près de la gare', '火車站附近'],
            ], [
                ['J’habite chez mes parents.', '我住在父母家。'],
                ['Le stylo est dans le sac.', '筆在袋子裡。'],
                ['Le livre est sur la table.', '書在桌上。'],
                ['La banque est près de la gare.', '銀行在火車站附近。'],
            ]),
            G('de', '從、的', [
                ['從城市', 'de Taipei', '從台北'],
                ['從陽性國', 'du Japon', '從日本'],
                ['從陰性國', 'de France', '從法國'],
                ['誰的', 'de Marie', 'Marie 的'],
            ], [
                ['Je viens de Taipei.', '我從台北來。'],
                ['Il vient du Japon.', '他從日本來。'],
                ['Elle vient de France.', '她從法國來。'],
                ['C’est le sac de Marie.', '這是 Marie 的袋子。'],
            ]),
        ],
    ),
    L(
        'heure', 'A1', 'L’heure', '法文 A1｜時間與星期',
        '問時間說 Quelle heure est-il ? 回答用 Il est。一點用 heure 單數，兩點以上用 heures。星期幾不習慣大寫。習慣性的星期前面加 le。',
        '整點、半點、差一刻，以及星期，附例句、中文、朗讀與 PDF。',
        '正午是 Il est midi. 午夜是 Il est minuit. 這兩句不加 heures。\n差一刻用 moins le quart：neuf heures moins le quart 是八點四十五分。',
        [
            G('整點與半點', 'Il est', [
                ['一點', 'Il est une heure.', '現在一點。'],
                ['八點', 'Il est huit heures.', '現在八點。'],
                ['八點半', 'Il est huit heures et demie.', '現在八點半。'],
                ['正午', 'Il est midi.', '現在正午。'],
            ], [
                ['Quelle heure est-il ?', '現在幾點？'],
                ['Il est huit heures.', '現在八點。'],
                ['Il est huit heures et demie.', '現在八點半。'],
                ['Il est midi.', '現在正午。'],
            ]),
            G('刻', '一刻、差一刻', [
                ['八點一刻', 'huit heures et quart', '八點十五分'],
                ['差一刻', 'neuf heures moins le quart', '八點四十五分'],
                ['差十分', 'trois heures moins dix', '兩點五十分'],
                ['問', 'À quelle heure ?', '幾點？'],
            ], [
                ['Il est huit heures et quart.', '現在八點一刻。'],
                ['Il est neuf heures moins le quart.', '現在八點四十五分。'],
                ['Le cours commence à neuf heures.', '課九點開始。'],
                ['À quelle heure est-ce que tu manges ?', '你幾點吃飯？'],
            ]),
            G('星期', 'le + 星期', [
                ['星期一', 'le lundi', '每星期一'],
                ['今天', 'aujourd’hui', '今天'],
                ['明天', 'demain', '明天'],
                ['昨天', 'hier', '昨天'],
            ], [
                ['Le lundi, j’ai un cours.', '每星期一我有課。'],
                ['Aujourd’hui, c’est mercredi.', '今天是星期三。'],
                ['Demain, je travaille.', '我明天工作。'],
                ['Le dimanche, je ne travaille pas.', '我星期日不工作。'],
            ]),
        ],
    ),
    L(
        'cest', 'A1', 'C’est et il y a', '法文 A1｜c’est、il est、il y a',
        'il y a 表示某地有某物。介紹一個名詞用 c’est，後面常有冠詞。說明身份或國籍時，il est、elle est 後面的職業和國籍不加冠詞。',
        'il y a、c’est、il est 的差別，附例句、中文、朗讀與 PDF。',
        'C’est un médecin. 是在指出「這一位是醫生」。Elle est médecin. 是在說明她的職業。\n國籍同樣：Elle est française. C’est une Française. 當國籍當名詞時要大寫並加冠詞。',
        [
            G('il y a', '有', [
                ['有一家', 'il y a un café', '有一家咖啡館'],
                ['有一些', 'il y a des chaises', '有一些椅子'],
                ['沒有', 'il n’y a pas de', '沒有'],
                ['附近', 'près d’ici', '這附近'],
            ], [
                ['Il y a un café près d’ici.', '這附近有一家咖啡館。'],
                ['Il y a des chaises dans la salle.', '房間裡有椅子。'],
                ['Il n’y a pas de lait.', '沒有牛奶。'],
                ['Qu’est-ce qu’il y a dans ton sac ?', '你的袋子裡有什麼？'],
            ]),
            G('c’est', '這是，後面接名詞', [
                ['這是', 'c’est un livre', '這是一本書'],
                ['這位是', 'c’est Marie', '這位是 Marie'],
                ['不是', 'ce n’est pas', '這不是'],
                ['這些是', 'ce sont des amis', '這些是朋友'],
            ], [
                ['C’est un dictionnaire.', '這是一本字典。'],
                ['C’est Marie. Elle est française.', '這位是 Marie。她是法國人。'],
                ['Ce n’est pas mon sac.', '這不是我的袋子。'],
                ['Ce sont mes amis.', '這些是我的朋友。'],
            ]),
            G('il est', '他是，後面接形容詞或職業', [
                ['職業', 'elle est médecin', '她是醫生'],
                ['國籍', 'il est français', '他是法國人'],
                ['形容', 'il est utile', '它很有用'],
                ['有冠詞', 'c’est un médecin', '這位是一位醫生'],
            ], [
                ['Elle est médecin.', '她是醫生。'],
                ['Il est français.', '他是法國人。'],
                ['Ce dictionnaire est utile. Il est utile.', '這本字典很有用。它很有用。'],
                ['C’est un médecin.', '這位是一位醫生。'],
            ]),
        ],
    ),
]
LESSONS[0]['meta'] = 'A1 · 動詞 · 例句跟讀'
