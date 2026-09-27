from lesson_util import G, L

LESSONS = [
    L(
        'which-clause', 'B2', 'Which Clause', '英文 B2｜逗號後的 which',
        '逗號後面的 who 或 which 是補上額外資訊，拿掉整句仍然知道在說誰。which 也可以指前面整件事。',
        '非限定用法，附例句、中文、朗讀與 PDF。',
        '這種句子不用 that。My brother, who lives in Taipei, is a doctor.',
        [
            G('who，補充人', '逗號隔開', [
                ['弟弟', 'my brother, who lives in Taipei', '我住台北的弟弟'],
                ['老師', 'Ms. Lin, who teaches us', '教我們的林老師'],
                ['Marie', 'Marie, who called', '打來的 Marie'],
                ['父親', 'my father, who is a doctor', '我那當醫生的父親'],
            ], [
                ['My brother, who lives in Taipei, is a doctor.', '我弟弟住在台北，他是醫生。'],
                ['Ms. Lin, who teaches us, is kind.', '林老師教我們，她很親切。'],
                ['Marie, who called last night, is my friend.', 'Marie 昨晚打來，她是我的朋友。'],
                ['My father, who is a doctor, works late.', '我父親是醫生，他工作到很晚。'],
            ]),
            G('which，補充事物', '逗號隔開', [
                ['書', 'the book, which I bought', '那本書，我買的'],
                ['城市', 'Taipei, which is big', '台北，它很大'],
                ['考試', 'the test, which was hard', '那場考試，它很難'],
                ['店', 'the shop, which is new', '那家店，它是新的'],
            ], [
                ['This book, which I bought yesterday, is useful.', '這本書是我昨天買的，它很有用。'],
                ['Taipei, which is a big city, is my home.', '台北是個大城市，它是我家。'],
                ['The test, which was hard, is over.', '那場考試很難，它結束了。'],
                ['The shop, which is new, sells tea.', '那家店是新的，它賣茶。'],
            ]),
            G('which 指整句', '前面那件事', [
                ['贏了', 'which surprised us', '這讓我們驚訝'],
                ['遲到', 'which made her angry', '這讓她生氣'],
                ['下雨', 'which was a problem', '這是個問題'],
                ['幫忙', 'which was kind', '這很貼心'],
            ], [
                ['The team won, which surprised us.', '隊伍贏了，這讓我們很驚訝。'],
                ['He was late, which made her angry.', '他遲到了，這讓她生氣。'],
                ['It rained all day, which was a problem.', '雨下了一整天，這是個問題。'],
                ['She waited for me, which was kind.', '她等我，這很貼心。'],
            ]),
        ],
    ),
    L(
        'third-conditional', 'B2', 'Third Conditional', '英文 B2｜第三條件句',
        '第三條件句談過去沒有發生的事。if 用過去完成，主句用 would have 加過去分詞。',
        'If I had…, I would have…，附例句、中文、朗讀與 PDF。',
        '這是事後的想像。事實是當時沒有做。',
        [
            G('if + 過去完成', '當時沒有', [
                ['知道', 'If I had known', '如果我當時知道'],
                ['努力', 'If she had studied', '如果她當時用功'],
                ['離開', 'If we had left', '如果我們當時離開'],
                ['打電話', 'If he had called', '如果他當時打了'],
            ], [
                ['If I had known, I would have told you.', '如果我當時知道，我就會告訴你。'],
                ['If she had studied, she would have passed.', '如果她當時用功，她就會通過。'],
                ['If we had left earlier, we would have caught the bus.', '如果我們當時早點離開，就會趕上公車。'],
                ['If he had called, I would have waited.', '如果他當時打了，我就會等。'],
            ]),
            G('would have', '當時會發生的結果', [
                ['會告訴', 'would have told', '當時會告訴'],
                ['會通過', 'would have passed', '當時會通過'],
                ['不會去', 'would not have gone', '當時就不會去'],
                ['會幫忙', 'would have helped', '當時會幫忙'],
            ], [
                ['I would have told you if I had known.', '如果我當時知道，我就會告訴你。'],
                ['She would have passed if she had studied.', '如果她當時用功，她就會通過。'],
                ['I would not have gone if it had rained.', '如果當時下雨，我就不會去。'],
                ['He would have helped if you had asked.', '如果你當時開口，他就會幫忙。'],
            ]),
            G('否定的過去', '當時沒有做的那一件', [
                ['沒下雨', 'if it had not rained', '如果當時沒下雨'],
                ['沒遲到', 'if I had not been late', '如果我當時沒遲到'],
                ['沒忘記', 'if she had not forgotten', '如果她當時沒忘記'],
                ['沒有你', 'if you had not helped', '如果當時沒有你幫忙'],
            ], [
                ['If it had not rained, we would have played.', '如果當時沒下雨，我們就會打球。'],
                ['If I had not been late, I would have seen her.', '如果我當時沒遲到，我就會見到她。'],
                ['If she had not forgotten, she would have brought it.', '如果她當時沒忘記，她就會帶它來。'],
                ['I would have failed if you had not helped.', '如果當時沒有你幫忙，我就會失敗。'],
            ]),
        ],
    ),
    L(
        'participle-clause', 'B2', 'Participle Clause', '英文 B2｜分詞當狀語',
        '分詞片語可以代替一個副詞子句。-ing 的主詞必須和主要句子的主詞相同。',
        'Walking… 和 Being tired…，附例句、中文、朗讀與 PDF。',
        'Walking home, the rain started. 是錯的，因為雨不會走路。要寫 Walking home, I got wet. 或 When I was walking home, the rain started.',
        [
            G('V-ing', '同時或原因', [
                ['走回家', 'Walking home, I', '走回家時，我'],
                ['感到累', 'Feeling tired, she', '覺得累，她'],
                ['看到', 'Seeing the bus, we', '看到公車，我們'],
                ['不知道', 'Not knowing the answer, he', '不知道答案，他'],
            ], [
                ['Walking home, I met Marie.', '走回家時，我遇到 Marie。'],
                ['Feeling tired, she sat down.', '覺得累，她坐下了。'],
                ['Seeing the bus, we ran.', '看到公車，我們跑了起來。'],
                ['Not knowing the answer, he kept quiet.', '不知道答案，他保持安靜。'],
            ]),
            G('過去分詞', '被動的狀態', [
                ['建成', 'Built in 1990, the school', '建於 1990 年，這所學校'],
                ['寫成', 'Written in English, the letter', '用英文寫成，這封信'],
                ['疲倦', 'Tired after work, I', '工作後很累，我'],
                ['受驚', 'Surprised by the news, she', '被消息嚇到，她'],
            ], [
                ['Built in 1990, the school is still new.', '這所學校建於 1990 年，它仍然很新。'],
                ['Written in English, the letter was easy to read.', '這封信用英文寫成，很容易讀。'],
                ['Tired after work, I went to bed.', '工作後很累，我去睡了。'],
                ['Surprised by the news, she called me.', '被消息嚇到，她打給我。'],
            ]),
            G('改寫', '子句與分詞', [
                ['because', 'Because he was tired, he left.', '因為他累了，他離開。'],
                ['分詞', 'Being tired, he left.', '因為累了，他離開。'],
                ['when', 'When I walked home, I met her.', '我走回家時遇到她。'],
                ['分詞', 'Walking home, I met her.', '走回家時，我遇到她。'],
            ], [
                ['Because he was tired, he left.', '因為他累了，他離開了。'],
                ['Being tired, he left.', '因為累了，他離開了。'],
                ['When I walked home, I met her.', '我走回家時遇到她。'],
                ['Walking home, I met her.', '走回家時，我遇到她。'],
            ]),
        ],
    ),
    L(
        'causative', 'B2', 'Causative', '英文 B2｜使役與感官動詞',
        'make、let、have 後面接原形。see 和 hear 可以接原形，表示看到或聽到整個過程，也可以接 V-ing，表示看到正在做。',
        'make、let、have、see、hear，附例句、中文、朗讀與 PDF。',
        'get 不一樣，要加 to：I got him to help. 請他幫忙。',
        [
            G('make / let / have', '叫、讓、請', [
                ['叫', 'make me laugh', '使我笑'],
                ['讓', 'let me go', '讓我走'],
                ['請人做', 'have him fix it', '請他修好'],
                ['使', 'made her happy', '使她開心'],
            ], [
                ['The story made me laugh.', '這個故事使我笑了。'],
                ['My parents let me go.', '我的父母讓我去。'],
                ['I had him fix the bike.', '我請他修好腳踏車。'],
                ['The news made her happy.', '這消息使她開心。'],
            ]),
            G('see / hear + 原形', '整個過程', [
                ['看見', 'saw him leave', '看見他離開'],
                ['聽見', 'heard her sing', '聽見她唱歌'],
                ['看見', 'saw them play', '看見他們打'],
                ['聽見', 'heard the bell ring', '聽見鈴響'],
            ], [
                ['I saw him leave.', '我看見他離開。'],
                ['We heard her sing.', '我們聽見她唱歌。'],
                ['She saw them play baseball.', '她看見他們打棒球。'],
                ['I heard the bell ring.', '我聽見鈴響了。'],
            ]),
            G('see / hear + V-ing', '正在做的片段', [
                ['看見', 'saw him leaving', '看見他正在離開'],
                ['聽見', 'heard her singing', '聽見她正在唱'],
                ['看見', 'saw them playing', '看見他們正在打'],
                ['聽見', 'heard the baby crying', '聽見嬰兒正在哭'],
            ], [
                ['I saw him leaving.', '我看見他正在離開。'],
                ['We heard her singing.', '我們聽見她正在唱歌。'],
                ['She saw them playing baseball.', '她看見他們正在打棒球。'],
                ['I heard the baby crying.', '我聽見嬰兒正在哭。'],
            ]),
        ],
    ),
    L(
        'wish', 'B2', 'Wish', '英文 B2｜wish 與 as if',
        'wish 後面用過去式，表示希望現在不是這樣。希望過去不是那樣，用過去完成。as if 也常用過去式表示不像真的。',
        'wish 和 as if，附例句、中文、朗讀與 PDF。',
        'I wish I were taller. be 常用 were。I wish I had studied. 是後悔過去。',
        [
            G('wish + 過去式', '希望現在不同', [
                ['知道', 'I wish I knew', '但願我知道'],
                ['是', 'I wish I were', '但願我是'],
                ['有', 'I wish I had', '但願我有'],
                ['住', 'I wish she lived', '但願她住'],
            ], [
                ['I wish I knew the answer.', '但願我知道答案。'],
                ['I wish I were taller.', '但願我更高。'],
                ['I wish I had more time.', '但願我有更多時間。'],
                ['I wish she lived closer.', '但願她住得更近。'],
            ]),
            G('wish + 過去完成', '後悔過去', [
                ['用功', 'I wish I had studied', '但願我當時有用功'],
                ['去', 'I wish I had gone', '但願我當時有去'],
                ['說', 'I wish I had said', '但願我當時有說'],
                ['幫忙', 'I wish you had helped', '但願你當時有幫'],
            ], [
                ['I wish I had studied harder.', '但願我當時更用功。'],
                ['I wish I had gone with them.', '但願我當時跟他們去了。'],
                ['I wish I had said thank you.', '但願我當時說了謝謝。'],
                ['I wish you had helped me.', '但願你當時有幫我。'],
            ]),
            G('as if', '好像', [
                ['知道', 'as if he knew', '好像他知道'],
                ['是老闆', 'as if she were the boss', '好像她是老闆'],
                ['見過', 'as if they had met', '好像他們見過'],
                ['擁有', 'as if he owned it', '好像他擁有它'],
            ], [
                ['He talks as if he knew everything.', '他說話好像什麼都知道。'],
                ['She acts as if she were the boss.', '她表現得好像她是老闆。'],
                ['They smiled as if they had met before.', '他們笑得好像以前見過。'],
                ['He spends money as if he owned the shop.', '他花錢好像這家店是他的。'],
            ]),
        ],
    ),
    L(
        'subjunctive', 'B2', 'Subjunctive', '英文 B2｜建議與要求的 that',
        'suggest、insist、demand、recommend 後面的 that 子句，動詞用原形。should 可以加上，也可以省略。',
        'suggest that he study，附例句、中文、朗讀與 PDF。',
        '原形不分人稱：that he study，不加 -s。',
        [
            G('suggest / recommend', '建議', [
                ['建議', 'suggested that he study', '建議他用功'],
                ['建議', 'suggested that we leave', '建議我們離開'],
                ['推薦', 'recommended that she rest', '建議她休息'],
                ['推薦', 'recommended that I see a doctor', '建議我去看醫生'],
            ], [
                ['The teacher suggested that he study more.', '老師建議他多讀一點。'],
                ['She suggested that we leave early.', '她建議我們早點離開。'],
                ['The doctor recommended that she rest.', '醫生建議她休息。'],
                ['They recommended that I see a doctor.', '他們建議我去看醫生。'],
            ]),
            G('insist / demand', '堅持、要求', [
                ['堅持', 'insisted that I stay', '堅持要我留下'],
                ['堅持', 'insisted that she be told', '堅持要告訴她'],
                ['要求', 'demanded that he apologize', '要求他道歉'],
                ['要求', 'demanded that the door be closed', '要求把門關上'],
            ], [
                ['He insisted that I stay.', '他堅持要我留下。'],
                ['She insisted that she be told.', '她堅持要有人告訴她。'],
                ['The teacher demanded that he apologize.', '老師要求他道歉。'],
                ['They demanded that the door be closed.', '他們要求把門關上。'],
            ]),
            G('should', '加上 should 也可以', [
                ['建議', 'that he should study', '他應該用功'],
                ['建議', 'that we should wait', '我們應該等'],
                ['要求', 'that she should come', '她應該來'],
                ['要求', 'that it should be done', '這應該被做完'],
            ], [
                ['I suggest that he should study.', '我建議他應該用功。'],
                ['She suggested that we should wait.', '她建議我們應該等。'],
                ['He demanded that she should come.', '他要求她應該來。'],
                ['They asked that it should be done today.', '他們要求這件事今天應該做完。'],
            ]),
        ],
    ),
    L(
        'gerund-or-infinitive', 'B2', 'Gerund or Infinitive', '英文 B2｜to V 與 V-ing 意思不同',
        'stop、remember、forget、try 後面接 to V 或 V-ing，意思不一樣。',
        '四個動詞的兩種接法，附例句、中文、朗讀與 PDF。',
        'remember to V 是記得要去做。remember V-ing 是記得做過。',
        [
            G('stop / remember', '停下來，以及記得', [
                ['停下某事', 'stop talking', '停止說話'],
                ['停下去做', 'stop to talk', '停下來以便說話'],
                ['記得要做', 'remember to lock', '記得要鎖'],
                ['記得做過', 'remember locking', '記得鎖過'],
            ], [
                ['Please stop talking.', '請停止說話。'],
                ['He stopped to talk to me.', '他停下來跟我說話。'],
                ['Remember to lock the door.', '記得要鎖門。'],
                ['I remember locking the door.', '我記得鎖過門。'],
            ]),
            G('forget / try', '忘記，以及試', [
                ['忘記要做', 'forgot to call', '忘了要打'],
                ['忘記做過', 'forgot meeting', '忘了見過'],
                ['試著', 'try to open', '試著打開'],
                ['試一試', 'try opening', '打開看看'],
            ], [
                ['I forgot to call her.', '我忘了要打給她。'],
                ['I will never forget meeting her.', '我永遠不會忘記見過她。'],
                ['Try to open the window.', '試著把窗戶打開。'],
                ['Try opening the window.', '打開窗戶看看。'],
            ]),
            G('對照', '同一動詞兩句', [
                ['regret to', 'regret to say', '很遺憾要說'],
                ['regret -ing', 'regret saying', '後悔說過'],
                ['go on to', 'went on to explain', '接著去說明'],
                ['go on -ing', 'went on talking', '繼續說'],
            ], [
                ['I regret to say that I cannot come.', '很遺憾，我得說我不能來。'],
                ['I regret saying that.', '我後悔說了那句話。'],
                ['She told the story and went on to explain it.', '她講完故事，接著說明。'],
                ['He went on talking for an hour.', '他繼續說了一小時。'],
            ]),
        ],
    ),
    L(
        'dummy-it', 'B2', 'Dummy It', '英文 B2｜形式主詞與形式受詞 it',
        '真正的主詞太長時，先用 it 占位子，把 to V 或 that 子句放到後面。受詞也可以用 it 先占。',
        'It is… to V、It is… that，以及 find it hard to V，附例句、中文、朗讀與 PDF。',
        'It is important to rest. 真正的主詞是 to rest。',
        [
            G('形式主詞 to V', 'It is + 形容詞', [
                ['重要', 'It is important to rest.', '休息很重要。'],
                ['難', 'It is hard to say.', '很難講。'],
                ['好', 'It is good to see you.', '見到你很好。'],
                ['可能', 'It is possible to finish.', '有可能做完。'],
            ], [
                ['It is important to rest.', '休息很重要。'],
                ['It is hard to say no.', '拒絕很難說。'],
                ['It is good to see you.', '見到你很好。'],
                ['It is possible to finish today.', '今天有可能做完。'],
            ]),
            G('形式主詞 that', 'It is said that', [
                ['據說', 'It is said that', '據說'],
                ['清楚', 'It is clear that', '很清楚'],
                ['真的', 'It is true that', '的確'],
                ['可惜', 'It is a pity that', '可惜'],
            ], [
                ['It is said that the test is easy.', '據說考試很簡單。'],
                ['It is clear that she is right.', '很清楚，她是對的。'],
                ['It is true that we need time.', '的確，我們需要時間。'],
                ['It is a pity that he cannot come.', '可惜他不能來。'],
            ]),
            G('形式受詞', 'find / think it', [
                ['覺得難', 'find it hard to', '覺得……很難'],
                ['覺得有用', 'find it useful to', '覺得……有用'],
                ['認為可能', 'think it possible to', '認為……有可能'],
                ['使成', 'make it clear that', '說清楚'],
            ], [
                ['I find it hard to get up early.', '我覺得早起很難。'],
                ['She finds it useful to take notes.', '她覺得做筆記有用。'],
                ['We think it possible to finish.', '我們認為有可能做完。'],
                ['Please make it clear that you will come.', '請說清楚你會來。'],
            ]),
        ],
    ),
    L(
        'agreement', 'B2', 'Agreement', '英文 B2｜主詞與動詞一致',
        '動詞跟真正的主詞一致。the number of 是單數，a number of 是複數。together with 不改變原來的主詞。',
        '容易看錯主詞的句子，附例句、中文、朗讀與 PDF。',
        'each、every、either、neither 當主詞時，動詞用單數。',
        [
            G('the number / a number', '單數與複數', [
                ['數目', 'The number of students is', '學生人數是'],
                ['一些', 'A number of students are', '一些學生'],
                ['數目', 'The number of books is', '書的數量是'],
                ['一些', 'A number of books are', '一些書'],
            ], [
                ['The number of students is twenty.', '學生人數是二十。'],
                ['A number of students are absent.', '一些學生缺席。'],
                ['The number of books is small.', '書的數量很少。'],
                ['A number of books are missing.', '一些書不見了。'],
            ]),
            G('together with', '主詞仍是第一個', [
                ['和', 'The teacher, together with the students, is', '老師和學生'],
                ['以及', 'Marie, as well as her friends, is', 'Marie 和她的朋友'],
                ['連同', 'The book, along with the notes, is', '書連同筆記'],
                ['不是', 'He, not they, is', '是他，不是他們'],
            ], [
                ['The teacher, together with the students, is here.', '老師和學生都在這裡。'],
                ['Marie, as well as her friends, is ready.', 'Marie 和她的朋友都準備好了。'],
                ['The book, along with the notes, is on the desk.', '書連同筆記在桌上。'],
                ['He, not they, is responsible.', '負責的是他，不是他們。'],
            ]),
            G('each / either', '單數', [
                ['每一個', 'Each of the boys is', '每個男孩都'],
                ['每一個', 'Every student has', '每個學生都有'],
                ['兩者之一', 'Either answer is', '兩個答案都可以'],
                ['兩者皆非', 'Neither plan works', '兩個計畫都不行'],
            ], [
                ['Each of the boys is ready.', '每個男孩都準備好了。'],
                ['Every student has a book.', '每個學生都有一本書。'],
                ['Either answer is correct.', '兩個答案都正確。'],
                ['Neither plan works.', '兩個計畫都不行。'],
            ]),
        ],
    ),
    L(
        'inversion-negative', 'B2', 'Negative Inversion', '英文 B2｜否定副詞倒裝',
        'Never、Seldom、Not only 放到句首時，句子要倒裝，像問句一樣把助動詞放在主詞前面。',
        '否定副詞開頭的倒裝，附例句、中文、朗讀與 PDF。',
        'Not only 倒裝的是前半句。Hardly...when 和 No sooner...than 用過去完成。',
        [
            G('never / seldom', '幾乎不', [
                ['從不', 'Never have I seen', '我從未見過'],
                ['很少', 'Seldom does she complain', '她很少抱怨'],
                ['幾乎不', 'Hardly did I know', '我幾乎不知道'],
                ['很少', 'Rarely do we meet', '我們很少見面'],
            ], [
                ['Never have I seen such a view.', '我從未見過這樣的景色。'],
                ['Seldom does she complain.', '她很少抱怨。'],
                ['Hardly did I know what to say.', '我幾乎不知道該說什麼。'],
                ['Rarely do we meet on Sunday.', '我們很少在星期天見面。'],
            ]),
            G('not only', '不但', [
                ['離開', 'Not only did he leave', '他不但離開'],
                ['讀', 'Not only does she study', '她不但讀書'],
                ['幫忙', 'Not only did they help', '他們不但幫忙'],
                ['晚', 'Not only was I late', '我不但遲到'],
            ], [
                ['Not only did he leave, but he also took the book.', '他不但離開，還把書拿走了。'],
                ['Not only does she study English, but she also teaches it.', '她不但讀英文，還教英文。'],
                ['Not only did they help, but they also stayed.', '他們不但幫忙，還留下來。'],
                ['Not only was I late, but I also forgot the book.', '我不但遲到，還忘了書。'],
            ]),
            G('hardly / no sooner', '一……就', [
                ['剛', 'Hardly had I sat down when', '我剛坐下就'],
                ['剛', 'No sooner had she left than', '她剛離開就'],
                ['剛到', 'Hardly had we arrived when', '我們剛到就'],
                ['剛說', 'No sooner had he spoken than', '他剛說完就'],
            ], [
                ['Hardly had I sat down when the phone rang.', '我剛坐下，電話就響了。'],
                ['No sooner had she left than it rained.', '她剛離開，就下雨了。'],
                ['Hardly had we arrived when the class started.', '我們剛到，課就開始了。'],
                ['No sooner had he spoken than everyone laughed.', '他剛說完，大家就笑了。'],
            ]),
        ],
    ),
    L(
        'inversion-so-only', 'B2', 'So and Only', '英文 B2｜so、neither 與 only',
        'So 接肯定的「也是」，Neither 接否定的「也不」。Only 放在句首修飾時間或條件時，主要句子要倒裝。',
        'So do I、Neither can she、Only then did I understand，附例句、中文、朗讀與 PDF。',
        'So 和 Neither 後面的助動詞要跟前一句相同。前一句是 be，就用 be。',
        [
            G('so / neither', '也是、也不', [
                ['也是', 'So do I.', '我也是。'],
                ['也是', 'So is she.', '她也是。'],
                ['也不', 'Neither can I.', '我也不能。'],
                ['也不', 'Neither did he.', '他也沒有。'],
            ], [
                ['I like tea. So do I.', '我喜歡茶。我也是。'],
                ['She is ready. So is he.', '她準備好了。他也是。'],
                ['I cannot swim. Neither can she.', '我不會游泳。她也不會。'],
                ['He did not go. Neither did I.', '他沒去。我也沒去。'],
            ]),
            G('only + 時間', '句首倒裝', [
                ['那時', 'Only then did I understand.', '直到那時我才懂。'],
                ['後來', 'Only later did she know.', '直到後來她才知道。'],
                ['昨天', 'Only yesterday did he call.', '直到昨天才打來。'],
                ['現在', 'Only now do we see.', '直到現在我們才看見。'],
            ], [
                ['Only then did I understand.', '直到那時我才懂。'],
                ['Only later did she know the truth.', '直到後來她才知道真相。'],
                ['Only yesterday did he call.', '直到昨天才打來。'],
                ['Only now do we see the problem.', '直到現在我們才看見問題。'],
            ]),
            G('only if / when', '條件在前', [
                ['只有當', 'Only when I arrived did I see', '只有當我到達時才看見'],
                ['只有如果', 'Only if you try will you', '只有如果你試，你才會'],
                ['只有在', 'Only in Taipei can you', '只有在台北你才能'],
                ['只有這樣', 'Only in this way can we', '只有這樣我們才能'],
            ], [
                ['Only when I arrived did I see her.', '只有當我到達時，我才看見她。'],
                ['Only if you try will you learn.', '只有如果你試，你才會學會。'],
                ['Only in Taipei can you eat this.', '只有在台北你才能吃到這個。'],
                ['Only in this way can we finish.', '只有這樣我們才能做完。'],
            ]),
        ],
    ),
    L(
        'cleft', 'B2', 'Cleft Sentences', '英文 B2｜It is…that 強調句',
        'It is…that 把想強調的人、事物或時間拉到前面。強調動詞時用 do、does、did。',
        '分裂句與 do 強調，附例句、中文、朗讀與 PDF。',
        'It was Marie that called. 強調的是 Marie，不是別人。',
        [
            G('強調人', 'It is / was…that', [
                ['Marie', 'It was Marie that called.', '打來的是 Marie。'],
                ['他', 'It is he that knows.', '知道的人是他。'],
                ['老師', 'It was the teacher that helped.', '幫忙的是老師。'],
                ['你', 'It is you that I need.', '我需要的是你。'],
            ], [
                ['It was Marie that called.', '打來的是 Marie。'],
                ['It is he that knows the answer.', '知道答案的人是他。'],
                ['It was the teacher that helped me.', '幫忙我的是老師。'],
                ['It is you that I need.', '我需要的是你。'],
            ]),
            G('強調時間或地點', 'when / where 也可以', [
                ['昨天', 'It was yesterday that we met.', '我們是昨天見面的。'],
                ['在台北', 'It is in Taipei that she lives.', '她是住在台北。'],
                ['在學校', 'It was at school that I saw him.', '我是在學校看到他的。'],
                ['星期一', 'It is on Monday that class starts.', '課是星期一開始的。'],
            ], [
                ['It was yesterday that we met.', '我們是昨天見面的。'],
                ['It is in Taipei that she lives.', '她是住在台北。'],
                ['It was at school that I saw him.', '我是在學校看到他的。'],
                ['It is on Monday that the class starts.', '課是星期一開始的。'],
            ]),
            G('do / did', '強調動詞', [
                ['現在', 'I do like it.', '我確實喜歡。'],
                ['第三人稱', 'She does know.', '她確實知道。'],
                ['過去', 'I did call.', '我確實打了。'],
                ['請', 'Do sit down.', '請坐下。'],
            ], [
                ['I do like this book.', '我確實喜歡這本書。'],
                ['She does know the answer.', '她確實知道答案。'],
                ['I did call you.', '我確實打給你了。'],
                ['Do sit down.', '請坐下。'],
            ]),
        ],
    ),
    L(
        'reduced-relative', 'B2', 'Reduced Relative', '英文 B2｜關係子句省略',
        '關係子句如果是 who is 或 which is，可以把代名詞和 be 拿掉，只留分詞或介系詞片語。介系詞也可以放到 which 前面。',
        '分詞省略與介系詞提前，附例句、中文、朗讀與 PDF。',
        'The man who is standing there 可以寫成 The man standing there.',
        [
            G('V-ing', '拿掉 who is', [
                ['站著', 'the man standing there', '站在那裡的男人'],
                ['住', 'the students living here', '住在這裡的學生'],
                ['等', 'the bus coming now', '現在來的公車'],
                ['哭', 'the girl crying', '正在哭的女孩'],
            ], [
                ['The man standing there is my uncle.', '站在那裡的男人是我叔叔。'],
                ['The students living here are new.', '住在這裡的學生是新來的。'],
                ['The bus coming now is late.', '現在來的這班公車是晚的。'],
                ['The girl crying is Marie.', '正在哭的女孩是 Marie。'],
            ]),
            G('過去分詞', '拿掉 which was', [
                ['寫的', 'the book written by her', '她寫的書'],
                ['蓋的', 'the school built in 1990', '1990 年蓋的學校'],
                ['用的', 'the language used here', '這裡使用的語言'],
                ['邀請的', 'the students invited', '被邀請的學生'],
            ], [
                ['The book written by her is new.', '她寫的那本書是新的。'],
                ['The school built in 1990 is still used.', '1990 年蓋的那所學校仍在使用。'],
                ['English is the language used here.', '英文是這裡使用的語言。'],
                ['The students invited yesterday came.', '昨天被邀請的學生來了。'],
            ]),
            G('介系詞提前', 'in which、to whom', [
                ['住在', 'the city in which I live', '我住的城市'],
                ['談到', 'the man to whom I spoke', '我交談的男人'],
                ['用', 'the pen with which she wrote', '她用來寫的筆'],
                ['來自', 'the club of which he is a member', '他所屬的社團'],
            ], [
                ['Taipei is the city in which I live.', '台北是我住的城市。'],
                ['He is the man to whom I spoke.', '他就是我和他說話的那個人。'],
                ['This is the pen with which she wrote.', '這是她用來寫字的筆。'],
                ['That is the club of which he is a member.', '那是他所屬的社團。'],
            ]),
        ],
    ),
    L(
        'parallelism', 'B2', 'Parallelism', '英文 B2｜對等與平行結構',
        'and、or、but 兩邊的詞性要一樣。both…and、either…or、neither…nor、not only…but also 也要對稱。',
        '平行結構，附例句、中文、朗讀與 PDF。',
        '游泳和跑步都用 V-ing：She likes swimming and running. 不要一邊用 swimming、一邊用 to run。',
        [
            G('and 兩邊相同', '名詞、動詞、形容詞', [
                ['V-ing', 'swimming and running', '游泳和跑步'],
                ['to V', 'to read and to write', '讀和寫'],
                ['形容詞', 'kind and patient', '親切又有耐心'],
                ['名詞', 'tea and coffee', '茶和咖啡'],
            ], [
                ['She likes swimming and running.', '她喜歡游泳和跑步。'],
                ['I want to read and to write.', '我想閱讀和寫作。'],
                ['The teacher is kind and patient.', '老師親切又有耐心。'],
                ['We ordered tea and coffee.', '我們點了茶和咖啡。'],
            ]),
            G('both / either / neither', '成對', [
                ['兩者都', 'both tea and coffee', '茶和咖啡都'],
                ['二選一', 'either Monday or Tuesday', '星期一或星期二'],
                ['兩者都不', 'neither he nor she', '他和她都不'],
                ['不但而且', 'not only read but also write', '不但讀而且寫'],
            ], [
                ['I like both tea and coffee.', '茶和咖啡我都喜歡。'],
                ['We can meet either Monday or Tuesday.', '我們可以星期一或星期二見面。'],
                ['Neither he nor she was late.', '他和她都沒有遲到。'],
                ['She can not only read but also write Chinese.', '她不但能讀中文，而且能寫。'],
            ]),
            G('比較也要平行', 'than 兩邊', [
                ['V-ing', 'swimming than running', '游泳勝過跑步'],
                ['to V', 'to stay than to leave', '留下勝過離開'],
                ['子句', 'what he says than what he does', '他說的勝過他做的'],
                ['名詞', 'tea than coffee', '茶勝過咖啡'],
            ], [
                ['She likes swimming more than running.', '她喜歡游泳勝過跑步。'],
                ['I prefer to stay rather than leave.', '我寧願留下，而不是離開。'],
                ['What he says is better than what he does.', '他說的比他做的好。'],
                ['I like tea more than coffee.', '我喜歡茶勝過咖啡。'],
            ]),
        ],
    ),
]
