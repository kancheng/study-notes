from lesson_util import G, L

LESSONS = [
    L(
        'sentence-patterns', 'A2', 'Sentence Patterns', '英文 A2｜五種基本句型',
        '英文句子可以先看成五種骨架。先找到動詞，再看它後面需要什麼。',
        'SV、SVC、SVO、SVOO、SVOC 五種基本句型，附例句、中文、朗讀與 PDF。',
        'SVC 的動詞是 be、look、taste 這類。SVOC 的補語是在說明受詞，例如 We call him Tom.',
        [
            G('SV / SVC', '動詞後面沒有受詞，或接補語', [
                ['SV', 'Birds fly.', '鳥會飛。'],
                ['SV', 'She smiled.', '她笑了。'],
                ['SVC', 'She is kind.', '她很親切。'],
                ['SVC', 'The soup tastes good.', '這湯很好喝。'],
            ], [
                ['Birds fly.', '鳥會飛。'],
                ['She smiled.', '她笑了。'],
                ['She is kind.', '她很親切。'],
                ['The soup tastes good.', '這湯很好喝。'],
            ]),
            G('SVO / SVOO', '一個或兩個受詞', [
                ['SVO', 'I like tea.', '我喜歡茶。'],
                ['SVO', 'They play baseball.', '他們打棒球。'],
                ['SVOO', 'She gave me a book.', '她給我一本書。'],
                ['SVOO', 'He told us a story.', '他說了一個故事給我們聽。'],
            ], [
                ['I like tea.', '我喜歡茶。'],
                ['They play baseball.', '他們打棒球。'],
                ['She gave me a book.', '她給我一本書。'],
                ['He told us a story.', '他說了一個故事給我們聽。'],
            ]),
            G('SVOC', '受詞再加補語', [
                ['稱呼', 'We call him Tom.', '我們叫他 Tom。'],
                ['使成', 'The news made her happy.', '這消息讓她開心。'],
                ['使成', 'Please keep the door open.', '請讓門開著。'],
                ['認定', 'I found the book useful.', '我覺得這本書有用。'],
            ], [
                ['We call him Tom.', '我們叫他 Tom。'],
                ['The news made her happy.', '這消息讓她開心。'],
                ['Please keep the door open.', '請讓門開著。'],
                ['I found the book useful.', '我覺得這本書有用。'],
            ]),
        ],
    ),
    L(
        'the-uncountable', 'A2', 'The and Uncountable', '英文 A2｜the 與不可數名詞',
        'the 指雙方都知道的那一個。水、建議、資訊這類不可數名詞沒有複數，也不能加 a。',
        'the、不加冠詞，以及不可數名詞，附例句、中文、朗讀與 PDF。',
        'advice、information、homework 都是不可數。要說一件用 a piece of advice。',
        [
            G('the', '特定的那一個', [
                ['唯一', 'the sun', '太陽'],
                ['前面提過', 'the book', '那本書'],
                ['序數', 'the first class', '第一堂課'],
                ['樂器', 'the piano', '鋼琴'],
            ], [
                ['The sun is hot.', '太陽很熱。'],
                ['I bought a book. The book is new.', '我買了一本書。那本書是新的。'],
                ['She is in the first class.', '她在第一堂課。'],
                ['He plays the piano.', '他彈鋼琴。'],
            ]),
            G('不加冠詞', '泛指或固定說法', [
                ['三餐', 'breakfast', '早餐'],
                ['上學', 'go to school', '去上學'],
                ['語言', 'English', '英文'],
                ['運動', 'play baseball', '打棒球'],
            ], [
                ['I eat breakfast at seven.', '我七點吃早餐。'],
                ['They go to school every day.', '他們每天去上學。'],
                ['English is useful.', '英文很有用。'],
                ['We play baseball.', '我們打棒球。'],
            ]),
            G('不可數', '沒有複數', [
                ['水', 'water', '水'],
                ['建議', 'advice', '建議'],
                ['資訊', 'information', '資訊'],
                ['作業', 'homework', '作業'],
            ], [
                ['I need some water.', '我需要一些水。'],
                ['She gave me advice.', '她給了我建議。'],
                ['This information is useful.', '這資訊很有用。'],
                ['The homework is easy.', '這作業很簡單。'],
            ]),
        ],
    ),
    L(
        'present-continuous', 'A2', 'Present Continuous', '英文 A2｜現在進行式',
        '現在進行式是 am / is / are 加 -ing，表示此刻正在做。習慣仍用現在簡單式。',
        '此刻正在做、和習慣的差別，以及疑問句，附例句、中文、朗讀與 PDF。',
        'know、like、want 這類狀態動詞通常不用進行式。說 I know her.，不說 I am knowing her.',
        [
            G('正在做', 'am / is / are + -ing', [
                ['我', 'I am reading', '我正在讀'],
                ['你', 'you are working', '你正在工作'],
                ['她', 'she is studying', '她正在讀'],
                ['他們', 'they are playing', '他們正在玩'],
            ], [
                ['I am reading now.', '我現在正在讀。'],
                ['You are working hard.', '你正在努力工作。'],
                ['She is studying English.', '她正在讀英文。'],
                ['They are playing baseball.', '他們正在打棒球。'],
            ]),
            G('對比', '此刻與習慣', [
                ['習慣', 'I read every night.', '我每晚閱讀。'],
                ['此刻', 'I am reading now.', '我現在正在讀。'],
                ['習慣', 'He works here.', '他在這裡工作。'],
                ['此刻', 'He is working now.', '他現在正在工作。'],
            ], [
                ['I read every night.', '我每晚閱讀。'],
                ['I am reading now.', '我現在正在讀。'],
                ['He works in Taipei.', '他在台北工作。'],
                ['He is working at home today.', '他今天在家工作。'],
            ]),
            G('疑問與否定', '把 be 移到前面', [
                ['你', 'Are you reading?', '你正在讀嗎？'],
                ['她', 'Is she studying?', '她正在讀嗎？'],
                ['我', 'I am not sleeping', '我不是在睡'],
                ['他們', 'They are not playing', '他們不是在玩'],
            ], [
                ['Are you reading now?', '你現在正在讀嗎？'],
                ['Is she studying English?', '她正在讀英文嗎？'],
                ['I am not sleeping.', '我不是在睡。'],
                ['They are not playing today.', '他們今天沒有在玩。'],
            ]),
        ],
    ),
    L(
        'past-simple', 'A2', 'Past Simple', '英文 A2｜過去簡單式與過去進行式',
        '過去簡單式談已發生的事。過去進行式是 was / were 加 -ing，談當時正在做的事。',
        '規則與不規則過去式、過去進行式，以及 when / while，附例句、中文、朗讀與 PDF。',
        'when 常接較短的那件事，while 接較長、正在進行的事。',
        [
            G('過去簡單式', '昨天、剛才', [
                ['規則', 'worked', '工作了'],
                ['規則', 'studied', '讀了'],
                ['不規則', 'went', '去了'],
                ['不規則', 'saw', '看到了'],
            ], [
                ['I worked yesterday.', '我昨天工作了。'],
                ['She studied last night.', '她昨晚讀了書。'],
                ['We went to school.', '我們去了學校。'],
                ['He saw a movie.', '他看了一部電影。'],
            ]),
            G('過去進行式', '當時正在做', [
                ['我', 'I was reading', '我當時正在讀'],
                ['她', 'she was cooking', '她當時正在煮'],
                ['我們', 'we were waiting', '我們當時正在等'],
                ['他們', 'they were playing', '他們當時正在玩'],
            ], [
                ['I was reading at eight.', '我八點當時正在讀。'],
                ['She was cooking dinner.', '她當時正在煮晚餐。'],
                ['We were waiting for the bus.', '我們當時正在等公車。'],
                ['They were playing baseball.', '他們當時正在打棒球。'],
            ]),
            G('when / while', '兩件事同時', [
                ['when', 'when he called', '當他打來時'],
                ['while', 'while I was reading', '當我正在讀時'],
                ['when', 'when the rain started', '當雨開始下時'],
                ['while', 'while she was cooking', '當她正在煮時'],
            ], [
                ['I was reading when he called.', '他打來時，我正在讀。'],
                ['He called while I was reading.', '我正在讀的時候，他打來了。'],
                ['We were walking when the rain started.', '雨開始下時，我們正在走。'],
                ['I arrived while she was cooking.', '她正在煮的時候，我到了。'],
            ]),
        ],
    ),
    L(
        'will-going-to', 'A2', 'Will and Going to', '英文 A2｜will 與 be going to',
        'will 常用在說話當下才決定的事。be going to 常用在已經有的計畫。已經排定的行程也可用現在進行式。',
        '三種談未來的說法，附例句、中文、朗讀與 PDF。',
        'will 的否定是 will not，口語縮成 won\'t。',
        [
            G('will', '現在決定', [
                ['我', 'I will help', '我會幫忙'],
                ['她', 'she will call', '她會打'],
                ['我們', 'we will wait', '我們會等'],
                ['否定', "I won't stay", '我不會留下'],
            ], [
                ['I will help you.', '我會幫你。'],
                ['She will call later.', '她稍後會打。'],
                ['We will wait here.', '我們會在這裡等。'],
                ["I won't stay long.", '我不會留很久。'],
            ]),
            G('be going to', '已經的計畫', [
                ['我', 'I am going to study', '我打算讀'],
                ['他', 'he is going to leave', '他打算離開'],
                ['我們', 'we are going to meet', '我們打算見面'],
                ['她', 'she is going to cook', '她打算煮'],
            ], [
                ['I am going to study tonight.', '我今晚打算讀書。'],
                ['He is going to leave tomorrow.', '他明天打算離開。'],
                ['We are going to meet at seven.', '我們打算七點見面。'],
                ['She is going to cook dinner.', '她打算煮晚餐。'],
            ]),
            G('現在進行式', '已排定', [
                ['我', 'I am meeting her', '我約了她'],
                ['我們', 'we are leaving', '我們要出發'],
                ['課', 'class is starting', '課要開始'],
                ['他', 'he is flying', '他要搭飛機'],
            ], [
                ['I am meeting her at six.', '我六點要和她見面。'],
                ['We are leaving tomorrow.', '我們明天要出發。'],
                ['Class is starting at nine.', '課九點開始。'],
                ['He is flying to Tokyo on Friday.', '他星期五要飛東京。'],
            ]),
        ],
    ),
    L(
        'quantifiers', 'A2', 'Quantifiers', '英文 A2｜數量詞',
        'some 用在肯定句，any 常用在否定和疑問。可數用 many 和 a few，不可數用 much 和 a little。',
        'some、any、many、much、a few、a little，附例句、中文、朗讀與 PDF。',
        'a few 和 a little 是「有一些」。few 和 little 沒有 a 時，語氣是「很少、幾乎沒有」。',
        [
            G('some / any', '一些／任何', [
                ['肯定', 'some water', '一些水'],
                ['肯定', 'some books', '一些書'],
                ['否定', "any money", '任何錢'],
                ['疑問', 'any questions', '任何問題'],
            ], [
                ['I need some water.', '我需要一些水。'],
                ['She has some books.', '她有一些書。'],
                ["I don't have any money.", '我沒有任何錢。'],
                ['Do you have any questions?', '你有任何問題嗎？'],
            ]),
            G('many / much', '很多', [
                ['可數', 'many friends', '很多朋友'],
                ['可數', 'many books', '很多書'],
                ['不可數', 'much time', '很多時間'],
                ['不可數', 'much homework', '很多作業'],
            ], [
                ['She has many friends.', '她有很多朋友。'],
                ['How many books do you have?', '你有多少本書？'],
                ['I don\'t have much time.', '我沒有很多時間。'],
                ['There is too much homework.', '作業太多了。'],
            ]),
            G('a few / a little', '有一些', [
                ['可數', 'a few friends', '有幾個朋友'],
                ['可數', 'a few questions', '有幾個問題'],
                ['不可數', 'a little water', '有一點水'],
                ['不可數', 'a little time', '有一點時間'],
            ], [
                ['I have a few friends here.', '我在這裡有幾個朋友。'],
                ['She asked a few questions.', '她問了幾個問題。'],
                ['There is a little water.', '有一點水。'],
                ['We have a little time.', '我們有一點時間。'],
            ]),
        ],
    ),
    L(
        'comparatives', 'A2', 'Comparatives', '英文 A2｜比較級與最高級',
        '兩者用比較級，三者以上用最高級。短詞加 -er / -est，長詞用 more / most。',
        '比較級、最高級和不規則變化，附例句、中文、朗讀與 PDF。',
        'good 的比較級是 better，最高級是 best。bad 是 worse、worst。far 是 farther、farthest。',
        [
            G('比較級', '兩者', [
                ['短詞', 'taller than', '比……高'],
                ['短詞', 'older than', '比……年長'],
                ['長詞', 'more useful than', '比……有用'],
                ['一樣', 'as tall as', '和……一樣高'],
            ], [
                ['He is taller than me.', '他比我高。'],
                ['She is older than her brother.', '她比她弟弟年長。'],
                ['English is more useful than I thought.', '英文比我原本想的有用。'],
                ['I am as tall as you.', '我和你一樣高。'],
            ]),
            G('最高級', '三者以上', [
                ['短詞', 'the tallest', '最高的'],
                ['短詞', 'the oldest', '最年長的'],
                ['長詞', 'the most useful', '最有用的'],
                ['地點', 'in the class', '在班上'],
            ], [
                ['He is the tallest boy in the class.', '他是班上最高的男孩。'],
                ['She is the oldest of the three.', '她是三個人裡最年長的。'],
                ['This is the most useful book.', '這是最有用的書。'],
                ['Taipei is the biggest city here.', '台北是這裡最大的城市。'],
            ]),
            G('不規則', 'good、bad、far', [
                ['好', 'better / best', '更好／最好'],
                ['壞', 'worse / worst', '更差／最差'],
                ['遠', 'farther / farthest', '更遠／最遠'],
                ['少', 'less / least', '較少／最少'],
            ], [
                ['This book is better.', '這本書更好。'],
                ['Today is worse than yesterday.', '今天比昨天更差。'],
                ['His home is farther.', '他家更遠。'],
                ['I have less time today.', '我今天時間較少。'],
            ]),
        ],
    ),
    L(
        'modals', 'A2', 'Modals', '英文 A2｜其他情態動詞',
        'should 是建議，must 是必須，may 和 might 是可能，could 可以是過去的能力或客氣的請求。',
        'should、must、may、might、could，附例句、中文、朗讀與 PDF。',
        '這些詞後面都接原形動詞，不隨人稱加 -s。',
        [
            G('should / must', '建議與必須', [
                ['建議', 'you should rest', '你應該休息'],
                ['建議否定', 'you should not worry', '你不該擔心'],
                ['必須', 'you must stop', '你必須停'],
                ['禁止', 'you must not smoke', '你不准抽菸'],
            ], [
                ['You should rest.', '你應該休息。'],
                ['You should not worry.', '你不該擔心。'],
                ['You must finish the homework.', '你必須把作業做完。'],
                ['You must not smoke here.', '你不准在這裡抽菸。'],
            ]),
            G('may / might', '可能', [
                ['可能', 'it may rain', '可能下雨'],
                ['更沒把握', 'it might rain', '也許下雨'],
                ['許可', 'you may sit here', '你可以坐這裡'],
                ['她', 'she might come', '她也許會來'],
            ], [
                ['It may rain tonight.', '今晚可能下雨。'],
                ['It might rain later.', '稍後也許會下雨。'],
                ['You may sit here.', '你可以坐這裡。'],
                ['She might come tomorrow.', '她明天也許會來。'],
            ]),
            G('could', '過去能力或客氣請求', [
                ['過去', 'I could swim', '我以前會游泳'],
                ['過去否定', "I couldn't drive", '我以前不會開車'],
                ['請求', 'Could you help me?', '可以請你幫我嗎？'],
                ['可能', 'it could be true', '這可能是真的'],
            ], [
                ['I could swim when I was five.', '我五歲時就會游泳。'],
                ["I couldn't drive last year.", '我去年還不會開車。'],
                ['Could you help me?', '可以請你幫我嗎？'],
                ['It could be true.', '這可能是真的。'],
            ]),
        ],
    ),
    L(
        'infinitive-gerund', 'A2', 'Infinitive and Gerund', '英文 A2｜to V 與 V-ing',
        '有些動詞後面接 to V，有些接 V-ing。這一課先記最常見的分組。',
        'want、decide 接 to V；like、enjoy、finish 接 V-ing，附例句、中文、朗讀與 PDF。',
        'like 兩邊都可以：I like to read. 和 I like reading. 意思接近。enjoy 和 finish 只能接 V-ing。',
        [
            G('to V', 'want、decide、hope', [
                ['想要', 'want to go', '想去'],
                ['決定', 'decide to stay', '決定留下'],
                ['希望', 'hope to see', '希望見到'],
                ['需要', 'need to rest', '需要休息'],
            ], [
                ['I want to go home.', '我想回家。'],
                ['She decided to stay.', '她決定留下。'],
                ['We hope to see you.', '我們希望見到你。'],
                ['He needs to rest.', '他需要休息。'],
            ]),
            G('V-ing', 'enjoy、finish、practice', [
                ['享受', 'enjoy reading', '享受閱讀'],
                ['做完', 'finish doing', '做完'],
                ['練習', 'practice speaking', '練習說'],
                ['考慮', 'consider joining', '考慮加入'],
            ], [
                ['I enjoy reading.', '我享受閱讀。'],
                ['She finished doing her homework.', '她把作業做完了。'],
                ['We practice speaking English.', '我們練習說英文。'],
                ['He is considering joining the club.', '他正在考慮加入社團。'],
            ]),
            G('like', '兩邊都可以', [
                ['to V', 'like to swim', '喜歡游泳'],
                ['V-ing', 'like swimming', '喜歡游泳'],
                ['to V', 'love to cook', '喜愛下廚'],
                ['V-ing', 'love cooking', '喜愛下廚'],
            ], [
                ['I like to swim.', '我喜歡游泳。'],
                ['I like swimming.', '我喜歡游泳。'],
                ['She loves to cook.', '她喜愛下廚。'],
                ['She loves cooking.', '她喜愛下廚。'],
            ]),
        ],
    ),
    L(
        'so-because', 'A2', 'So and Because', '英文 A2｜so 與 because',
        'because 引出原因，so 引出結果。because of 後面接名詞，不接完整句子。',
        '原因、結果，以及 because of，附例句、中文、朗讀與 PDF。',
        '同一句不要寫 Because I was tired, so I rested. 原因和結果只留一個連接詞。',
        [
            G('because', '原因子句', [
                ['因為累', 'because I was tired', '因為我累了'],
                ['因為雨', 'because it rained', '因為下雨'],
                ['因為忙', 'because she was busy', '因為她很忙'],
                ['放句首', 'Because it was late', '因為晚了'],
            ], [
                ['I rested because I was tired.', '我休息了，因為我累了。'],
                ['We stayed home because it rained.', '我們留在家，因為下雨。'],
                ['She left because she was busy.', '她離開了，因為她很忙。'],
                ['Because it was late, I went home.', '因為晚了，我回家了。'],
            ]),
            G('so', '結果', [
                ['所以', 'so I rested', '所以我休息'],
                ['所以', 'so we stayed', '所以我們留下'],
                ['所以', 'so she left', '所以她離開'],
                ['所以', 'so I called', '所以我打了電話'],
            ], [
                ['I was tired, so I rested.', '我累了，所以我休息。'],
                ['It rained, so we stayed home.', '下雨了，所以我們留在家。'],
                ['She was busy, so she left.', '她很忙，所以她離開了。'],
                ['It was late, so I called her.', '晚了，所以我打給她。'],
            ]),
            G('because of', '後面接名詞', [
                ['雨', 'because of the rain', '因為雨'],
                ['交通', 'because of the traffic', '因為交通'],
                ['他', 'because of him', '因為他'],
                ['考試', 'because of the test', '因為考試'],
            ], [
                ['We stayed home because of the rain.', '因為雨，我們留在家。'],
                ['I was late because of the traffic.', '因為交通，我遲到了。'],
                ['She smiled because of him.', '因為他，她笑了。'],
                ['He studied hard because of the test.', '因為考試，他很用功。'],
            ]),
        ],
    ),
    L(
        'question-tags', 'A2', 'Question Tags', '英文 A2｜附加問句',
        '陳述句是肯定，後面的小問句就用否定。陳述句是否定，小問句就用肯定。',
        '附加問句的肯定與否定，以及 I am 的特別形式，附例句、中文、朗讀與 PDF。',
        'I am late, aren\'t I? 是固定說法，不用 amn\'t I。',
        [
            G('肯定 + 否定', '前面說是，後面問不是嗎', [
                ['be', "aren't you?", '不是嗎'],
                ['do', "doesn't she?", '不是嗎'],
                ['can', "can't they?", '不能嗎'],
                ['will', "won't he?", '不會嗎'],
            ], [
                ['You are a student, aren\'t you?', '你是學生，不是嗎？'],
                ['She likes tea, doesn\'t she?', '她喜歡茶，不是嗎？'],
                ['They can swim, can\'t they?', '他們會游泳，不是嗎？'],
                ['He will come, won\'t he?', '他會來，不是嗎？'],
            ]),
            G('否定 + 肯定', '前面說不是，後面問是嗎', [
                ['be', 'is she?', '是嗎'],
                ['do', 'do you?', '會嗎'],
                ['did', 'did he?', '有嗎'],
                ['can', 'can we?', '能嗎'],
            ], [
                ["She isn't busy, is she?", '她不忙，是嗎？'],
                ["You don't like coffee, do you?", '你不喜歡咖啡，對吧？'],
                ["He didn't call, did he?", '他沒有打來，對吧？'],
                ["We can't stay, can we?", '我們不能留下，對吧？'],
            ]),
            G('特別形式', 'I am 與 Let\'s', [
                ['I am', "aren't I?", '不是嗎'],
                ['Let\'s', 'shall we?', '好嗎'],
                ['祈使', 'will you?', '好嗎'],
                ['there', "isn't there?", '不是嗎'],
            ], [
                ["I am late, aren't I?", '我遲到了，不是嗎？'],
                ["Let's go, shall we?", '我們走吧，好嗎？'],
                ['Open the door, will you?', '開門好嗎？'],
                ["There is a class today, isn't there?", '今天有課，不是嗎？'],
            ]),
        ],
    ),
]
