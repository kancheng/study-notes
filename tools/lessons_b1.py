from lesson_util import G, L

LESSONS = [
    L(
        'present-perfect', 'B1', 'Present Perfect', '英文 B1｜現在完成式',
        '現在完成式是 have 或 has 加過去分詞。它把過去的事接到現在：經驗、持續，以及剛剛完成。',
        '經驗、since / for，以及 just、already、yet，附例句、中文、朗讀與 PDF。',
        'have been 是去過又回來。have gone 是去了、人還在那裡。',
        [
            G('經驗', '有沒有做過', [
                ['去過', 'have been to', '去過'],
                ['人還在那裡', 'has gone to', '去了'],
                ['看過', 'have seen', '看過'],
                ['沒做過', 'have never tried', '從來沒試過'],
            ], [
                ['I have been to Tainan.', '我去過台南。'],
                ['She has gone to the library.', '她去圖書館了。'],
                ['We have seen that movie.', '我們看過那部電影。'],
                ['I have never tried sushi.', '我從來沒試過壽司。'],
            ]),
            G('since / for', '從何時開始、持續多久', [
                ['時點', 'since 2020', '從 2020 年起'],
                ['時點', 'since Monday', '從星期一開始'],
                ['期間', 'for three years', '三年了'],
                ['期間', 'for two hours', '兩小時了'],
            ], [
                ['I have lived here since 2020.', '我從 2020 年住在這裡。'],
                ['She has been busy since Monday.', '她從星期一就很忙。'],
                ['We have studied English for three years.', '我們學英文三年了。'],
                ['He has waited for two hours.', '他已經等了兩小時。'],
            ]),
            G('just / already / yet', '剛剛、已經、尚未', [
                ['剛剛', 'have just finished', '剛剛做完'],
                ['已經', 'has already left', '已經離開'],
                ['尚未', 'have not finished yet', '還沒做完'],
                ['疑問', 'Have you eaten yet?', '你吃了嗎？'],
            ], [
                ['I have just finished my homework.', '我剛剛把作業做完。'],
                ['She has already left.', '她已經離開了。'],
                ['We have not finished yet.', '我們還沒做完。'],
                ['Have you eaten yet?', '你吃了嗎？'],
            ]),
        ],
    ),
    L(
        'present-perfect-continuous', 'B1', 'Present Perfect Continuous', '英文 B1｜現在完成進行式',
        'have / has been 加 -ing，強調從過去一直做到現在，而且動作還看得到過程。',
        '和現在完成式的差別，附例句、中文、朗讀與 PDF。',
        '如果重點是做完的結果，用現在完成式：I have read the book. 如果重點是一直在做，用進行：I have been reading.',
        [
            G('一直在做', 'have been + -ing', [
                ['我', 'have been reading', '一直在讀'],
                ['她', 'has been working', '一直在工作'],
                ['我們', 'have been waiting', '一直在等'],
                ['下雨', 'has been raining', '一直在下雨'],
            ], [
                ['I have been reading for an hour.', '我一直讀了一小時。'],
                ['She has been working all day.', '她整天都在工作。'],
                ['We have been waiting since noon.', '我們從中午一直等到現在。'],
                ['It has been raining.', '雨一直下著。'],
            ]),
            G('看得到過程', '現在的跡象', [
                ['眼睛', 'Your eyes are red.', '你的眼睛紅了。'],
                ['手', 'His hands are dirty.', '他的手很髒。'],
                ['累', 'I am tired.', '我累了。'],
                ['濕', 'The ground is wet.', '地面是濕的。'],
            ], [
                ['Your eyes are red. You have been crying.', '你的眼睛紅了。你一直在哭。'],
                ['His hands are dirty. He has been painting.', '他的手很髒。他一直在油漆。'],
                ['I am tired. I have been studying.', '我累了。我一直在讀書。'],
                ['The ground is wet. It has been raining.', '地面是濕的。雨一直下著。'],
            ]),
            G('對比', '結果與過程', [
                ['結果', 'I have read the book.', '我讀完這本書了。'],
                ['過程', 'I have been reading it.', '我一直在讀它。'],
                ['結果', 'She has written the letter.', '她把信寫好了。'],
                ['過程', 'She has been writing it.', '她一直在寫信。'],
            ], [
                ['I have read the book.', '我讀完這本書了。'],
                ['I have been reading it all morning.', '我整個早上都在讀它。'],
                ['She has written the letter.', '她把信寫好了。'],
                ['She has been writing it since lunch.', '她從午餐後一直在寫。'],
            ]),
        ],
    ),
    L(
        'passive', 'B1', 'Passive', '英文 B1｜被動語態',
        '當受詞比做事的人重要，就把受詞放到句首，用 be 加過去分詞。',
        '現在、過去和現在完成的被動，附例句、中文、朗讀與 PDF。',
        'by 用來補出做事的人。不重要時可以省略。',
        [
            G('現在', 'am / is / are + p.p.', [
                ['做成', 'is made', '被做成'],
                ['使用', 'is used', '被使用'],
                ['講', 'is spoken', '被講'],
                ['需要', 'are needed', '被需要'],
            ], [
                ['This car is made in Japan.', '這輛車是在日本製造的。'],
                ['English is used here.', '這裡使用英文。'],
                ['Chinese is spoken in Taiwan.', '台灣說中文。'],
                ['Teachers are needed.', '需要老師。'],
            ]),
            G('過去', 'was / were + p.p.', [
                ['寫', 'was written', '被寫'],
                ['蓋', 'was built', '被蓋'],
                ['邀請', 'were invited', '被邀請'],
                ['發現', 'was found', '被發現'],
            ], [
                ['The letter was written yesterday.', '這封信是昨天寫的。'],
                ['The school was built in 1990.', '這所學校建於 1990 年。'],
                ['We were invited to the party.', '我們被邀請去派對。'],
                ['The book was found under the desk.', '書在桌子底下被找到。'],
            ]),
            G('現在完成', 'have / has been + p.p.', [
                ['做完', 'has been finished', '已經被做完'],
                ['送出', 'has been sent', '已經被送出'],
                ['修好', 'have been fixed', '已經被修好'],
                ['選上', 'has been chosen', '已經被選上'],
            ], [
                ['The work has been finished.', '工作已經做完了。'],
                ['The email has been sent.', '信已經寄出了。'],
                ['The lights have been fixed.', '燈已經修好了。'],
                ['She has been chosen for the team.', '她已經被選進隊裡。'],
            ]),
        ],
    ),
    L(
        'modal-passive', 'B1', 'Modal Passive', '英文 B1｜情態動詞的被動',
        '情態動詞後面用 be 加過去分詞，表示必須、可以或應該被做。',
        'can、must、should 的被動，附例句、中文、朗讀與 PDF。',
        '主動的 Someone must finish it. 改成被動是 It must be finished.',
        [
            G('must be', '必須被做', [
                ['做完', 'must be finished', '必須被做完'],
                ['交', 'must be handed in', '必須被交'],
                ['清洗', 'must be washed', '必須被洗'],
                ['遵守', 'must be followed', '必須被遵守'],
            ], [
                ['The work must be finished today.', '工作今天必須做完。'],
                ['Homework must be handed in.', '作業必須交。'],
                ['The cups must be washed.', '杯子必須洗。'],
                ['The rules must be followed.', '規則必須遵守。'],
            ]),
            G('can be', '可以被做', [
                ['回收', 'can be recycled', '可以被回收'],
                ['看見', 'can be seen', '可以被看見'],
                ['使用', 'can be used', '可以被使用'],
                ['修好', 'can be fixed', '可以被修好'],
            ], [
                ['Paper can be recycled.', '紙可以被回收。'],
                ['The mountain can be seen from here.', '從這裡可以看見那座山。'],
                ['This room can be used.', '這間房間可以使用。'],
                ['The bike can be fixed.', '腳踏車可以修好。'],
            ]),
            G('should be', '應該被做', [
                ['清洗', 'should be cleaned', '應該被清潔'],
                ['回答', 'should be answered', '應該被回答'],
                ['記住', 'should be remembered', '應該被記住'],
                ['完成', 'should be done', '應該被完成'],
            ], [
                ['The room should be cleaned.', '房間應該打掃。'],
                ['The question should be answered.', '這個問題應該回答。'],
                ['This rule should be remembered.', '這條規則應該記住。'],
                ['The work should be done soon.', '工作應該快點做完。'],
            ]),
        ],
    ),
    L(
        'noun-clause-that', 'B1', 'Noun Clause That', '英文 B1｜that 名詞子句',
        'that 後面接一整句，當作動詞的受詞，或放在 be 後面當補語。口語裡 that 常常省略。',
        'I think that、I know that，以及 The fact is that，附例句、中文、朗讀與 PDF。',
        'that 子句裡仍用陳述句語序，不把助動詞移到前面。',
        [
            G('動詞受詞', 'think、know、say', [
                ['認為', 'I think that', '我認為'],
                ['知道', 'I know that', '我知道'],
                ['說', 'She said that', '她說'],
                ['希望', 'We hope that', '我們希望'],
            ], [
                ['I think that she is right.', '我認為她是對的。'],
                ['I know that he is busy.', '我知道他很忙。'],
                ['She said that the test was easy.', '她說考試很簡單。'],
                ['We hope that you can come.', '我們希望你能來。'],
            ]),
            G('省略 that', '口語常見', [
                ['認為', 'I think she is right.', '我認為她是對的。'],
                ['知道', 'I know he is busy.', '我知道他很忙。'],
                ['相信', 'I believe you.', '我相信你。'],
                ['確定', 'I am sure she knows.', '我確定她知道。'],
            ], [
                ['I think she is right.', '我認為她是對的。'],
                ['I know he is busy.', '我知道他很忙。'],
                ['I believe you can do it.', '我相信你做得到。'],
                ['I am sure she knows the answer.', '我確定她知道答案。'],
            ]),
            G('補語', 'The fact is that', [
                ['事實', 'The fact is that', '事實是'],
                ['問題', 'The problem is that', '問題是'],
                ['消息', 'The news is that', '消息是'],
                ['想法', 'My idea is that', '我的想法是'],
            ], [
                ['The fact is that we need more time.', '事實是我們需要更多時間。'],
                ['The problem is that it is late.', '問題是已經晚了。'],
                ['The news is that she won.', '消息是她贏了。'],
                ['My idea is that we should wait.', '我的想法是我們應該等。'],
            ]),
        ],
    ),
    L(
        'noun-clause-wh', 'B1', 'Noun Clause Wh', '英文 B1｜whether 與疑問詞子句',
        '不確定是不是，用 whether 或 if。問的是什麼、誰、哪裡，就把疑問詞放在子句開頭，後面用陳述句語序。',
        'whether / if 和 what、where、why 子句，附例句、中文、朗讀與 PDF。',
        '介系詞後面用 whether，不用 if：I am worried about whether he will come.',
        [
            G('whether / if', '是否', [
                ['是否', 'whether she will come', '她會不會來'],
                ['是否', 'if he knows', '他知不知道'],
                ['是否要', 'whether to go', '要不要去'],
                ['是否', 'whether it is true', '是不是真的'],
            ], [
                ['I do not know whether she will come.', '我不知道她會不會來。'],
                ['Ask if he knows the answer.', '問問他知不知道答案。'],
                ['She cannot decide whether to go.', '她無法決定要不要去。'],
                ['I wonder whether it is true.', '我想知道這是不是真的。'],
            ]),
            G('what / who', '什麼、誰', [
                ['什麼', 'what he wants', '他想要什麼'],
                ['誰', 'who she is', '她是誰'],
                ['哪一個', 'which book you need', '你需要哪本書'],
                ['什麼', 'what happened', '發生了什麼'],
            ], [
                ['I know what he wants.', '我知道他想要什麼。'],
                ['Do you know who she is?', '你知道她是誰嗎？'],
                ['Tell me which book you need.', '告訴我你需要哪本書。'],
                ['Nobody knows what happened.', '沒有人知道發生了什麼事。'],
            ]),
            G('where / when / why', '地點、時間、原因', [
                ['哪裡', 'where she lives', '她住哪裡'],
                ['何時', 'when the class starts', '課何時開始'],
                ['為什麼', 'why he left', '他為什麼離開'],
                ['如何', 'how it works', '它怎麼運作'],
            ], [
                ['I know where she lives.', '我知道她住哪裡。'],
                ['Please tell me when the class starts.', '請告訴我課何時開始。'],
                ['I understand why he left.', '我了解他為什麼離開。'],
                ['She explained how it works.', '她說明了它怎麼運作。'],
            ]),
        ],
    ),
    L(
        'relative-who-which', 'B1', 'Relative Who Which', '英文 B1｜who、which、that',
        '關係代名詞把兩句合成一句。人用 who 或 that，事物用 which 或 that。',
        '主格關係代名詞，附例句、中文、朗讀與 PDF。',
        '限定用法不加逗號，用來指出是哪一個。The student who sits here is my friend.',
        [
            G('who', '人', [
                ['坐', 'the student who sits here', '坐在這裡的學生'],
                ['教', 'the teacher who teaches us', '教我們的老師'],
                ['住', 'the man who lives next door', '住隔壁的男人'],
                ['幫助', 'the girl who helped me', '幫助我的女孩'],
            ], [
                ['The student who sits here is my friend.', '坐在這裡的學生是我的朋友。'],
                ['The teacher who teaches us is kind.', '教我們的老師很親切。'],
                ['The man who lives next door is a doctor.', '住隔壁的男人是醫生。'],
                ['I thanked the girl who helped me.', '我向幫助我的女孩道謝。'],
            ]),
            G('which', '事物', [
                ['我買的', 'the book which I bought', '我買的書'],
                ['很有用', 'a book which is useful', '有用的書'],
                ['她寫的', 'the letter which she wrote', '她寫的信'],
                ['我們坐的', 'the bus which we took', '我們坐的公車'],
            ], [
                ['The book which I bought is new.', '我買的那本書是新的。'],
                ['This is a book which is useful.', '這是一本有用的書。'],
                ['The letter which she wrote is long.', '她寫的那封信很長。'],
                ['The bus which we took was late.', '我們坐的那班公車遲到了。'],
            ]),
            G('that', '人與事物都可以', [
                ['人', 'the student that sits here', '坐在這裡的學生'],
                ['物', 'the book that I need', '我需要的書'],
                ['人', 'the friend that called', '打來的朋友'],
                ['物', 'the movie that we saw', '我們看的電影'],
            ], [
                ['The student that sits here is new.', '坐在這裡的學生是新來的。'],
                ['This is the book that I need.', '這是我需要的書。'],
                ['The friend that called is Marie.', '打來的朋友是 Marie。'],
                ['The movie that we saw was good.', '我們看的那部電影很好。'],
            ]),
        ],
    ),
    L(
        'relative-whose-whom', 'B1', 'Relative Whose Whom', '英文 B1｜whose 與 whom',
        'whose 表示「那個人的」。whom 是受格，用在人被動詞或介系詞接到的時候。',
        'whose、whom，以及口語裡用 who 代替 whom，附例句、中文、朗讀與 PDF。',
        '口語常把受格 whom 說成 who，或直接省略：the man I met。書面仍常見 whom。',
        [
            G('whose', '……的', [
                ['袋子', 'whose bag was lost', '袋子掉了的人'],
                ['父親', 'whose father is a doctor', '父親是醫生的人'],
                ['名字', 'whose name I forgot', '我忘了名字的人'],
                ['家', 'whose house is near', '家在附近的人'],
            ], [
                ['The girl whose bag was lost is crying.', '袋子掉了的女孩正在哭。'],
                ['I know a boy whose father is a doctor.', '我認識一個父親是醫生的男孩。'],
                ['She is the student whose name I forgot.', '她就是我忘了名字的那個學生。'],
                ['The man whose house is near us is kind.', '家在我們附近的那個男人很親切。'],
            ]),
            G('whom', '受格', [
                ['遇見', 'whom I met', '我遇見的人'],
                ['邀請', 'whom we invited', '我們邀請的人'],
                ['談到', 'whom she talked about', '她談到的人'],
                ['依賴', 'on whom I can rely', '我可以依靠的人'],
            ], [
                ['The man whom I met is a teacher.', '我遇見的那個男人是老師。'],
                ['The students whom we invited came.', '我們邀請的學生來了。'],
                ['The friend whom she talked about is here.', '她談到的那個朋友在這裡。'],
                ['He is a person on whom I can rely.', '他是我可以依靠的人。'],
            ]),
            G('口語', 'who 或省略', [
                ['who', 'the man who I met', '我遇見的人'],
                ['省略', 'the man I met', '我遇見的人'],
                ['who', 'the girl who we saw', '我們看到的女孩'],
                ['省略', 'the teacher we like', '我們喜歡的老師'],
            ], [
                ['The man who I met is a teacher.', '我遇見的那個男人是老師。'],
                ['The man I met is a teacher.', '我遇見的那個男人是老師。'],
                ['The girl who we saw is Marie.', '我們看到的女孩是 Marie。'],
                ['The teacher we like is kind.', '我們喜歡的老師很親切。'],
            ]),
        ],
    ),
    L(
        'relative-where-when', 'B1', 'Relative Where When', '英文 B1｜where、when、why',
        '關係副詞用來接地方、時間和原因。where 等於 in which，when 等於 on which 或 at which。',
        'where、when、why，附例句、中文、朗讀與 PDF。',
        'the reason why 的 why 可以省略。地方如果已經有介系詞，就用 which：the city in which I live.',
        [
            G('where', '地方', [
                ['城市', 'the city where I live', '我住的城市'],
                ['學校', 'the school where she studies', '她就讀的學校'],
                ['店', 'the shop where we met', '我們見面的店'],
                ['國家', 'a country where it snows', '會下雪的國家'],
            ], [
                ['Taipei is the city where I live.', '台北是我住的城市。'],
                ['This is the school where she studies.', '這是她就讀的學校。'],
                ['That is the shop where we met.', '那是我們見面的店。'],
                ['I want to visit a country where it snows.', '我想去一個會下雪的國家。'],
            ]),
            G('when', '時間', [
                ['日子', 'the day when we met', '我們見面的那天'],
                ['年', 'the year when he left', '他離開的那年'],
                ['時刻', 'a time when I can rest', '我能休息的時候'],
                ['夏天', 'the summer when it was hot', '很熱的那個夏天'],
            ], [
                ['I remember the day when we met.', '我記得我們見面的那天。'],
                ['2020 was the year when he left.', '2020 年是他離開的那年。'],
                ['Sunday is a time when I can rest.', '星期天是我能休息的時候。'],
                ['I remember the summer when it was hot.', '我記得那個很熱的夏天。'],
            ]),
            G('why', '原因', [
                ['理由', 'the reason why she left', '她離開的理由'],
                ['原因', 'the reason why I called', '我打來的原因'],
                ['省略', 'the reason she cried', '她哭的原因'],
                ['這就是', 'That is why', '那就是為什麼'],
            ], [
                ['I know the reason why she left.', '我知道她離開的理由。'],
                ['That is the reason why I called.', '那就是我打來的原因。'],
                ['Do you know the reason she cried?', '你知道她哭的原因嗎？'],
                ['He was tired. That is why he left.', '他累了。那就是他離開的原因。'],
            ]),
        ],
    ),
    L(
        'time-clauses', 'B1', 'Time Clauses', '英文 B1｜時間副詞子句',
        'when、while、as soon as、not until 後面接時間子句。談未來時，時間子句用現在式，主句用 will。',
        '四種時間連接，附例句、中文、朗讀與 PDF。',
        'When I arrive, I will call you. 時間子句不寫 When I will arrive.',
        [
            G('when / while', '當……時', [
                ['when', 'when I arrive', '當我到達時'],
                ['when', 'when she calls', '當她打來時'],
                ['while', 'while you wait', '當你等待時'],
                ['while', 'while he was out', '當他外出時'],
            ], [
                ['When I arrive, I will call you.', '我到的時候會打給你。'],
                ['Please tell me when she calls.', '她打來時請告訴我。'],
                ['Read while you wait.', '等待時讀點東西。'],
                ['I called while he was out.', '他外出時我打了電話。'],
            ]),
            G('as soon as', '一……就', [
                ['到了', 'as soon as I arrive', '我一到'],
                ['結束', 'as soon as class ends', '課一結束'],
                ['看到', 'as soon as she saw me', '她一看到我'],
                ['回家', 'as soon as we got home', '我們一到家'],
            ], [
                ['I will text you as soon as I arrive.', '我一到就傳訊息給你。'],
                ['We can leave as soon as class ends.', '課一結束我們就能走。'],
                ['She smiled as soon as she saw me.', '她一看到我就笑了。'],
                ['It started to rain as soon as we got home.', '我們一到家就開始下雨。'],
            ]),
            G('not until', '直到……才', [
                ['直到', 'not until six', '直到六點才'],
                ['直到', 'not until he called', '直到他打來才'],
                ['直到', 'not until tomorrow', '直到明天才'],
                ['直到', 'not until the rain stops', '直到雨停才'],
            ], [
                ['I will not leave until six.', '我直到六點才會離開。'],
                ['She did not rest until he called.', '直到他打來，她才休息。'],
                ['The shop does not open until tomorrow.', '這家店直到明天才開。'],
                ['We will not go out until the rain stops.', '直到雨停，我們才會出去。'],
            ]),
        ],
    ),
    L(
        'so-that-result', 'B1', 'So That Result', '英文 B1｜so…that 與 such…that',
        'so…that 和 such…that 都表示「如此……以至於」。so 後面接形容詞或副詞，such 後面接名詞片語。',
        '結果子句的兩種寫法，附例句、中文、朗讀與 PDF。',
        'so many / so much 後面仍用 so，即使後面有名詞：so many books that...。',
        [
            G('so + 形容詞', '如此……以至於', [
                ['累', 'so tired that', '累到'],
                ['忙', 'so busy that', '忙到'],
                ['快', 'so fast that', '快到'],
                ['便宜', 'so cheap that', '便宜到'],
            ], [
                ['I was so tired that I fell asleep.', '我累到睡著了。'],
                ['She is so busy that she cannot come.', '她忙到不能來。'],
                ['He ran so fast that I could not follow.', '他跑得快到我跟不上。'],
                ['The book was so cheap that I bought two.', '這本書便宜到我買了兩本。'],
            ]),
            G('such + 名詞', '如此一個……', [
                ['好老師', 'such a good teacher that', '這麼好的老師，以至於'],
                ['大雨', 'such heavy rain that', '這麼大的雨，以至於'],
                ['難的考試', 'such a hard test that', '這麼難的考試，以至於'],
                ['好心的人', 'such kind people that', '這麼好心的人，以至於'],
            ], [
                ['She is such a good teacher that we all like her.', '她是這麼好的老師，我們都很喜歡她。'],
                ['It was such heavy rain that we stayed home.', '雨大到我們留在家。'],
                ['It was such a hard test that many students failed.', '考試難到許多學生不及格。'],
                ['They are such kind people that I trust them.', '他們人這麼好，我信任他們。'],
            ]),
            G('so many / so much', '數量太多', [
                ['可數', 'so many books that', '書多到'],
                ['可數', 'so few chairs that', '椅子少到'],
                ['不可數', 'so much work that', '工作多到'],
                ['不可數', 'so little time that', '時間少到'],
            ], [
                ['I have so many books that I need a new shelf.', '我的書多到需要一個新書架。'],
                ['There were so few chairs that some students stood.', '椅子少到有些學生站著。'],
                ['There is so much work that I cannot rest.', '工作多到我無法休息。'],
                ['We have so little time that we must hurry.', '我們時間少到必須趕快。'],
            ]),
        ],
    ),
    L(
        'although', 'B1', 'Although', '英文 B1｜although 與 despite',
        'although 和 even though 後面接完整句子。despite 和 in spite of 後面接名詞或 V-ing。',
        '讓步：雖然，附例句、中文、朗讀與 PDF。',
        'although 不和 but 連用。Although it rained, we went out. 逗號後面不再加 but。',
        [
            G('although', '後面接句子', [
                ['雖然下雨', 'although it rained', '雖然下雨'],
                ['雖然累', 'although I was tired', '雖然我累了'],
                ['即使難', 'even though it is hard', '即使很難'],
                ['即使晚', 'even though it was late', '即使晚了'],
            ], [
                ['Although it rained, we went out.', '雖然下雨，我們還是出去了。'],
                ['Although I was tired, I finished the work.', '雖然我累了，我還是把工作做完。'],
                ['Even though it is hard, I will try.', '即使很難，我也會試。'],
                ['She kept reading even though it was late.', '即使晚了，她仍繼續讀。'],
            ]),
            G('despite', '後面接名詞', [
                ['雨', 'despite the rain', '儘管下雨'],
                ['交通', 'despite the traffic', '儘管交通'],
                ['疲倦', 'despite his tiredness', '儘管他很累'],
                ['噪音', 'despite the noise', '儘管噪音'],
            ], [
                ['We went out despite the rain.', '儘管下雨，我們還是出去了。'],
                ['I arrived on time despite the traffic.', '儘管交通壅塞，我還是準時到。'],
                ['He finished the race despite his tiredness.', '儘管很累，他還是跑完了。'],
                ['She studied despite the noise.', '儘管有噪音，她還是讀了書。'],
            ]),
            G('despite + V-ing', '後面接動作', [
                ['感到不適', 'despite feeling sick', '儘管感到不適'],
                ['感到累', 'despite feeling tired', '儘管覺得累'],
                ['失敗', 'despite failing once', '儘管失敗過一次'],
                ['忙碌', 'despite being busy', '儘管忙碌'],
            ], [
                ['He went to school despite feeling sick.', '儘管感到不適，他還是去上學。'],
                ['I kept working despite feeling tired.', '儘管覺得累，我仍繼續工作。'],
                ['She tried again despite failing once.', '儘管失敗過一次，她又試了。'],
                ['He helped us despite being busy.', '儘管忙碌，他還是幫了我們。'],
            ]),
        ],
    ),
    L(
        'purpose', 'B1', 'Purpose', '英文 B1｜so that 與 in order to',
        '目的可以用 so that 接句子，或用 in order to、to 接原形動詞。',
        '為了，附例句、中文、朗讀與 PDF。',
        'so that 子句裡常有 can、could、will。in order to 後面不要再加主詞。',
        [
            G('so that', '後面接句子', [
                ['能趕上', 'so that I can catch', '為了能趕上'],
                ['能看見', 'so that she could see', '為了能看見'],
                ['不會遲到', 'so that we will not be late', '為了不會遲到'],
                ['能休息', 'so that he could rest', '為了他能休息'],
            ], [
                ['I leave early so that I can catch the bus.', '我提早離開，為了能趕上公車。'],
                ['She stood up so that she could see.', '她站起來，為了能看見。'],
                ['We hurried so that we would not be late.', '我們趕快走，為了不會遲到。'],
                ['I turned off the light so that he could rest.', '我把燈關掉，為了他能休息。'],
            ]),
            G('in order to', '後面接動詞', [
                ['趕上', 'in order to catch', '為了趕上'],
                ['通過', 'in order to pass', '為了通過'],
                ['省錢', 'in order to save money', '為了省錢'],
                ['學習', 'in order to learn', '為了學習'],
            ], [
                ['I left early in order to catch the bus.', '我提早離開，為了趕上公車。'],
                ['She studies hard in order to pass.', '她用功，為了通過考試。'],
                ['We cook at home in order to save money.', '我們在家煮，為了省錢。'],
                ['He came here in order to learn English.', '他來這裡是為了學英文。'],
            ]),
            G('to V', '較短的目的', [
                ['買', 'to buy milk', '為了買牛奶'],
                ['問', 'to ask a question', '為了問問題'],
                ['見', 'to see her', '為了見她'],
                ['休息', 'to rest', '為了休息'],
            ], [
                ['I went out to buy milk.', '我出去買牛奶。'],
                ['She raised her hand to ask a question.', '她舉手問問題。'],
                ['We called to see her.', '我們打電話是為了見她。'],
                ['He sat down to rest.', '他坐下休息。'],
            ]),
        ],
    ),
    L(
        'first-conditional', 'B1', 'First Conditional', '英文 B1｜第一條件句',
        '如果未來有這個條件，就會有那個結果。if 子句用現在式，主句用 will。',
        'If + 現在式，will，以及 unless，附例句、中文、朗讀與 PDF。',
        'unless 的意思接近 if not。Unless it rains 等於 If it does not rain.',
        [
            G('if + 現在', '可能發生', [
                ['下雨', 'if it rains', '如果下雨'],
                ['有時間', 'if I have time', '如果我有時間'],
                ['她來', 'if she comes', '如果她來'],
                ['你努力', 'if you try', '如果你試'],
            ], [
                ['If it rains, I will stay home.', '如果下雨，我會留在家。'],
                ['If I have time, I will call you.', '如果我有時間，我會打給你。'],
                ['If she comes, we will start.', '如果她來，我們就開始。'],
                ['If you try, you will understand.', '如果你試，你會懂。'],
            ]),
            G('主句在前', 'will 也可以放前面', [
                ['留下', 'I will stay if', '我會留下，如果'],
                ['幫忙', 'I will help if', '我會幫忙，如果'],
                ['等', 'We will wait if', '我們會等，如果'],
                ['去', 'She will go if', '她會去，如果'],
            ], [
                ['I will stay home if it rains.', '如果下雨，我會留在家。'],
                ['I will help if you ask.', '如果你開口，我會幫忙。'],
                ['We will wait if you are late.', '如果你遲到，我們會等。'],
                ['She will go if she is free.', '如果她有空，她會去。'],
            ]),
            G('unless', '如果不', [
                ['不下雨', 'unless it rains', '除非下雨'],
                ['不趕快', 'unless we hurry', '除非我們趕快'],
                ['你不試', 'unless you try', '除非你試'],
                ['她不來', 'unless she comes', '除非她來'],
            ], [
                ['I will go out unless it rains.', '除非下雨，否則我會出去。'],
                ['We will be late unless we hurry.', '除非我們趕快，否則會遲到。'],
                ['You will not know unless you try.', '除非你試，否則不會知道。'],
                ['We cannot start unless she comes.', '除非她來，否則我們不能開始。'],
            ]),
        ],
    ),
    L(
        'second-conditional', 'B1', 'Second Conditional', '英文 B1｜第二條件句',
        '和第二條件句談的是現在或未來不太可能、或與事實相反的情況。if 用過去式，主句用 would。',
        'If I were、If I had，附例句、中文、朗讀與 PDF。',
        'be 在這種句子裡常用 were，不分人稱：If I were you.',
        [
            G('If I were', '與現在事實相反', [
                ['如果我是你', 'If I were you', '如果我是你'],
                ['如果她在', 'If she were here', '如果她在這裡'],
                ['如果我是老師', 'If I were a teacher', '如果我是老師'],
                ['如果現在是夏天', 'If it were summer', '如果現在是夏天'],
            ], [
                ['If I were you, I would rest.', '如果我是你，我會休息。'],
                ['If she were here, she would help.', '如果她在這裡，她會幫忙。'],
                ['If I were a teacher, I would be patient.', '如果我是老師，我會有耐心。'],
                ['If it were summer, we would swim.', '如果現在是夏天，我們會去游泳。'],
            ]),
            G('If + 過去式', '想像的情況', [
                ['有時間', 'If I had time', '如果我有時間'],
                ['有錢', 'If we had money', '如果我們有錢'],
                ['住得近', 'If he lived near', '如果他住得近'],
                ['會說法文', 'If she spoke French', '如果她會說法文'],
            ], [
                ['If I had time, I would learn guitar.', '如果我有時間，我會學吉他。'],
                ['If we had money, we would travel.', '如果我們有錢，我們會去旅行。'],
                ['If he lived near, he would walk.', '如果他住得近，他會走路來。'],
                ['If she spoke French, she could help.', '如果她會說法文，她就能幫忙。'],
            ]),
            G('would', '想像中的結果', [
                ['會去', 'I would go', '我會去'],
                ['會買', 'she would buy', '她會買'],
                ['不會擔心', 'I would not worry', '我不會擔心'],
                ['會說', 'what would you do', '你會怎麼做'],
            ], [
                ['I would go if I were free.', '如果我有空，我會去。'],
                ['She would buy it if it were cheaper.', '如果它更便宜，她會買。'],
                ['I would not worry if I were you.', '如果我是你，我不會擔心。'],
                ['What would you do if you won?', '如果你贏了，你會怎麼做？'],
            ]),
        ],
    ),
    L(
        'participle-adjective', 'B1', 'Participle Adjective', '英文 B1｜分詞當形容詞',
        '-ing 形容造成感覺的事物，-ed 形容人的感受。現在分詞也能描述正在做的人，過去分詞描述已被做的事物。',
        'interesting / interested，以及 crying、broken，附例句、中文、朗讀與 PDF。',
        'The movie is interesting. I am interested. 事物用 -ing，人的感受用 -ed。',
        [
            G('-ing / -ed', '事物與感受', [
                ['有趣／感興趣', 'interesting / interested', '有趣的／感興趣的'],
                ['無聊／感到無聊', 'boring / bored', '無聊的／感到無聊的'],
                ['令人興奮／感到興奮', 'exciting / excited', '令人興奮的／感到興奮的'],
                ['令人疲倦／感到疲倦', 'tiring / tired', '累人的／感到累的'],
            ], [
                ['The movie is interesting.', '這部電影很有趣。'],
                ['I am interested in the movie.', '我對這部電影感興趣。'],
                ['The game is exciting, so we are excited.', '這場比賽很刺激，所以我們很興奮。'],
                ['The work is tiring, and I am tired.', '這工作很累人，我也累了。'],
            ]),
            G('正在做的', 'V-ing 修飾名詞', [
                ['哭的', 'the crying baby', '正在哭的嬰兒'],
                ['跑的', 'the running boy', '正在跑的男孩'],
                ['微笑的', 'the smiling girl', '微笑的女孩'],
                ['上升的', 'the rising sun', '升起的太陽'],
            ], [
                ['The crying baby needs milk.', '正在哭的嬰兒需要牛奶。'],
                ['The running boy is my brother.', '正在跑的男孩是我弟弟。'],
                ['The smiling girl is Marie.', '微笑的女孩是 Marie。'],
                ['We watched the rising sun.', '我們看著升起的太陽。'],
            ]),
            G('已被做的', '過去分詞修飾名詞', [
                ['破的', 'a broken window', '破掉的窗戶'],
                ['寫好的', 'a written report', '寫好的報告'],
                ['遺失的', 'the lost bag', '遺失的袋子'],
                ['煮好的', 'cooked food', '煮好的食物'],
            ], [
                ['There is a broken window.', '有一扇破掉的窗戶。'],
                ['Please read the written report.', '請讀那份寫好的報告。'],
                ['She found the lost bag.', '她找到了遺失的袋子。'],
                ['We ate the cooked food.', '我們吃了煮好的食物。'],
            ]),
        ],
    ),
    L(
        'used-to', 'B1', 'Used To', '英文 B1｜used to 與 be used to',
        'used to 加原形，表示過去的習慣，現在不是了。be used to 和 get used to 加 V-ing 或名詞，表示習慣於。',
        '三種 used to，附例句、中文、朗讀與 PDF。',
        'be used to 的 used 是形容詞，to 是介系詞，所以後面接 V-ing：I am used to getting up early.',
        [
            G('used to V', '過去如此，現在不是', [
                ['住', 'used to live', '以前住'],
                ['玩', 'used to play', '以前玩'],
                ['走路', 'used to walk', '以前走路'],
                ['否定', 'did not use to', '以前並不'],
            ], [
                ['I used to live in Tainan.', '我以前住在台南。'],
                ['She used to play the piano.', '她以前彈鋼琴。'],
                ['We used to walk to school.', '我們以前走路去學校。'],
                ['He did not use to like coffee.', '他以前並不喜歡咖啡。'],
            ]),
            G('be used to', '已經習慣', [
                ['早起', 'am used to getting up', '習慣早起'],
                ['熱', 'is used to the heat', '習慣炎熱'],
                ['噪音', 'are used to the noise', '習慣噪音'],
                ['開車', 'is used to driving', '習慣開車'],
            ], [
                ['I am used to getting up early.', '我習慣早起。'],
                ['She is used to the heat.', '她習慣炎熱。'],
                ['They are used to the noise.', '他們習慣噪音。'],
                ['He is used to driving in the city.', '他習慣在城市開車。'],
            ]),
            G('get used to', '慢慢變得習慣', [
                ['新學校', 'get used to the school', '習慣新學校'],
                ['早起', 'get used to getting up', '變得習慣早起'],
                ['食物', 'got used to the food', '變得習慣食物'],
                ['工作', 'getting used to the job', '正在習慣工作'],
            ], [
                ['You will get used to the school.', '你會習慣這所學校。'],
                ['I cannot get used to getting up at six.', '我還無法習慣六點起床。'],
                ['We got used to the food.', '我們變得習慣那種食物。'],
                ['She is getting used to the job.', '她正在習慣這份工作。'],
            ]),
        ],
    ),
    L(
        'reported-speech', 'B1', 'Reported Speech', '英文 B1｜轉述',
        '轉述別人的話時，現在式常改成過去式，代名詞和時間也跟著說話的人改變。',
        'said that、told me，以及問句的轉述，附例句、中文、朗讀與 PDF。',
        'tell 後面要有人：told me。say 可以直接接 that。問句轉述用 asked if 或 asked what，語序改成陳述句。',
        [
            G('陳述句', 'said / told', [
                ['say', 'said that she was tired', '說她累了'],
                ['tell', 'told me that he was busy', '告訴我他很忙'],
                ['時態', 'is → was', '現在改過去'],
                ['時間', 'today → that day', '今天改那天'],
            ], [
                ['She said that she was tired.', '她說她累了。'],
                ['He told me that he was busy.', '他告訴我他很忙。'],
                ['They said that the test was easy.', '他們說考試很簡單。'],
                ['Marie said that she would come the next day.', 'Marie 說她隔天會來。'],
            ]),
            G('是否問句', 'asked if / whether', [
                ['是否', 'asked if I was ready', '問我是否準備好'],
                ['是否', 'asked whether she could go', '問她能不能去'],
                ['是否知道', 'asked if he knew', '問他知不知道'],
                ['是否喜歡', 'asked whether we liked it', '問我們喜不喜歡'],
            ], [
                ['She asked if I was ready.', '她問我是否準備好了。'],
                ['He asked whether she could go.', '他問她能不能去。'],
                ['I asked if he knew the answer.', '我問他知不知道答案。'],
                ['They asked whether we liked the movie.', '他們問我們喜不喜歡那部電影。'],
            ]),
            G('疑問詞', '語序不倒裝', [
                ['哪裡', 'asked where I lived', '問我住哪裡'],
                ['什麼', 'asked what I wanted', '問我想要什麼'],
                ['為什麼', 'asked why she left', '問她為什麼離開'],
                ['何時', 'asked when the class started', '問課何時開始'],
            ], [
                ['She asked where I lived.', '她問我住哪裡。'],
                ['He asked what I wanted.', '他問我想要什麼。'],
                ['I asked why she left.', '我問她為什麼離開。'],
                ['They asked when the class started.', '他們問課何時開始。'],
            ]),
        ],
    ),
]
