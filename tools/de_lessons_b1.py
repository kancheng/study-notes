"""German B1 grammar aligned with Goethe-Zertifikat B1 (GER B1)."""
from lesson_util import G, L

LESSONS = [
    L(
        'praeteritum', 'B1', 'Präteritum', '德文 B1｜簡單過去式',
        '書面敘事用 Präteritum。規則動詞加 -te。不規則動詞要整組記，du 再加 -st。',
        '規則過去、常見不規則，以及 können、müssen、wollen 的過去，附例句、中文、朗讀與 PDF。',
        '口語說昨天做了什麼，仍多用 Perfekt。小說、新聞和報告用 Präteritum。\nsein 的 war、haben 的 hatte 已在 A2。',
        [
            G('規則', '詞幹加 -te', [
                ['ich / er', 'lernte', '當時學習'],
                ['du', 'lerntest', '你當時學習'],
                ['wir / sie', 'lernten', '當時學習'],
                ['ihr', 'lerntet', '你們當時學習'],
            ], [
                ['Früher wohnte ich in Kaohsiung.', '我以前住在高雄。'],
                ['Sie arbeitete in einem Büro.', '她當時在辦公室工作。'],
                ['Wir lernten jeden Tag neue Wörter.', '我們當時每天學新單字。'],
                ['Er machte die Tür leise zu.', '他輕輕把門帶上。'],
            ]),
            G('不規則', '詞幹改變，詞尾仍短', [
                ['去', 'ging / gingst / gingen', '當時去'],
                ['來', 'kam / kamst / kamen', '當時來'],
                ['看', 'sah / sahst / sahen', '當時看'],
                ['說', 'sprach / sprachst / sprachen', '當時說'],
            ], [
                ['Gestern ging er früh ins Bett.', '昨天他很早去睡。'],
                ['Sie kam zu spät zum Kurs.', '她上課遲到了。'],
                ['Ich sah den Film allein.', '我一個人看了那部電影。'],
                ['Wir sprachen nur Deutsch.', '我們當時只說德文。'],
            ]),
            G('情態動詞過去', '寫成 konnte、musste、wollte', [
                ['能', 'ich konnte', '我當時能'],
                ['必須', 'ich musste', '我當時必須'],
                ['想要', 'ich wollte', '我當時想要'],
                ['被允許', 'ich durfte', '我當時被允許'],
            ], [
                ['Wir konnten nicht kommen.', '我們當時不能來。'],
                ['Ich musste lange warten.', '我必須等很久。'],
                ['Als Kind wollte ich Lehrer werden.', '我小時候想當老師。'],
                ['Er durfte nicht allein fahren.', '他當時不可以自己搭車去。'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'futur', 'B1', 'Futur', '德文 B1｜將來',
        'werden 放在第二位，真正的動詞以原形放在句尾。已經約好的事，用現在式加時間就夠了。',
        'werden 的變位、預測，以及現在式表示已排定的未來，附例句、中文、朗讀與 PDF。',
        '日曆上已經定了的事：Ich rufe dich morgen an。\n預測或承諾才常用 werden：Es wird morgen regnen。',
        [
            G('werden', '將來式助動詞', [
                ['ich', 'ich werde', '我將'],
                ['du', 'du wirst', '你將'],
                ['er / sie', 'er wird', '他將'],
                ['wir / sie', 'wir werden', '我們將'],
                ['ihr', 'ihr werdet', '你們將'],
            ], [
                ['Ich werde nächstes Jahr nach Deutschland fahren.', '我明年會去德國。'],
                ['Wirst du mitkommen?', '你會一起去嗎？'],
                ['Es wird morgen regnen.', '明天會下雨。'],
                ['Wir werden pünktlich sein.', '我們會準時。'],
            ]),
            G('預測與承諾', '現在還不確定', [
                ['承諾', 'Ich werde dir helfen.', '我會幫你。'],
                ['預測', 'Das wird schwer.', '那會很難。'],
                ['疑問', 'Wann wirst du fertig sein?', '你什麼時候會好？'],
                ['否定', 'Ich werde nicht vergessen.', '我不會忘記。'],
            ], [
                ['Ich werde dich später anrufen.', '我晚點會打電話給你。'],
                ['Der Test wird nicht leicht sein.', '考試不會容易。'],
                ['Sie wird die Stelle bekommen.', '她會得到那個職位。'],
                ['Wir werden das nicht noch einmal machen.', '我們不會再做一次。'],
            ]),
            G('現在式即可', '已經排定', [
                ['明天', 'Ich rufe dich morgen an.', '我明天打電話給你。'],
                ['幾點', 'Der Zug kommt um acht.', '火車八點到。'],
                ['下週', 'Nächste Woche haben wir einen Test.', '下週我們有考試。'],
                ['計劃', 'Ich fliege am Freitag.', '我星期五搭飛機。'],
            ], [
                ['Ich rufe dich morgen an.', '我明天打電話給你。'],
                ['Der Kurs beginnt um neun.', '課九點開始。'],
                ['Am Sonntag besuche ich meine Eltern.', '星期天我去看我父母。'],
                ['Wir fahren im Juli nach Berlin.', '我們七月去柏林。'],
            ]),
        ],
        cols=('用法', '形式', '中文'),
    ),
    L(
        'relativsatz', 'B1', 'Relativsatz', '德文 B1｜關係子句',
        '關係代名詞跟著前面的名詞，格則看它在子句裡的工作。子句的動詞放在句尾，逗號不能省。',
        '主格、受格、與格的 der、die、das，附例句、中文、朗讀與 PDF。',
        '關係代名詞的性別跟先行詞，格跟子句裡的角色。\nder Mann, der hier wohnt：der 是子句主詞。der Mann, den ich kenne：den 是子句受詞。',
        [
            G('主格', '關係代名詞是子句主詞', [
                ['陽性', 'der Mann, der ...', '那個……的男人'],
                ['陰性', 'die Frau, die ...', '那個……的女人'],
                ['中性', 'das Kind, das ...', '那個……的孩子'],
                ['複數', 'die Leute, die ...', '那些……的人'],
            ], [
                ['Das ist der Mann, der neben mir wohnt.', '那是住在我隔壁的男人。'],
                ['Die Frau, die dort steht, ist Ärztin.', '站在那裡的女人是醫生。'],
                ['Das Kind, das dort spielt, ist sechs.', '在那裡玩的孩子六歲。'],
                ['Die Leute, die hier arbeiten, sind freundlich.', '在這裡工作的人很親切。'],
            ]),
            G('受格', '關係代名詞是子句受詞', [
                ['陽性', 'der Film, den ...', '那部……的電影'],
                ['陰性', 'die Stadt, die ...', '那座……的城市'],
                ['中性', 'das Buch, das ...', '那本……的書'],
                ['複數', 'die Wörter, die ...', '那些……的單字'],
            ], [
                ['Der Film, den wir gesehen haben, war spannend.', '我們看過的那部電影很精彩。'],
                ['Taipei ist eine Stadt, die ich gut kenne.', '台北是我很熟悉的城市。'],
                ['Ich lese das Buch, das du empfohlen hast.', '我在讀你推薦的那本書。'],
                ['Die Wörter, die wir gestern gelernt haben, sind wichtig.', '我們昨天學的那些單字很重要。'],
            ]),
            G('與格', 'helfen、danken、gehören 的對象', [
                ['陽性', 'der Kollege, dem ...', '那位……的同事'],
                ['陰性', 'die Frau, der ...', '那位……的女人'],
                ['中性', 'das Kind, dem ...', '那個……的孩子'],
                ['複數', 'die Freunde, denen ...', '那些……的朋友'],
            ], [
                ['Der Kollege, dem ich helfe, ist neu.', '我幫忙的那位同事是新來的。'],
                ['Die Frau, der das Buch gehört, ist nicht hier.', '這本書的主人不在這裡。'],
                ['Das Kind, dem wir danken, heißt Lin.', '我們感謝的那個孩子叫 Lin。'],
                ['Die Freunde, denen ich schreibe, wohnen in Berlin.', '我寫信給他們的那些朋友住在柏林。'],
            ]),
        ],
    ),
    L(
        'infinitiv-zu', 'B1', 'Infinitiv mit zu', '德文 B1｜帶 zu 的不定詞',
        'versuchen、vergessen、vorhaben 後面的第二個動詞要加 zu。目的若是同一個主詞，用 um ... zu。',
        'zu、um ... zu、ohne ... zu，以及和 damit 的分工，附例句、中文、朗讀與 PDF。',
        '同一主詞的目的用 um ... zu。不同主詞用 damit。\nohne ... zu 表示沒做就發生：Er ging, ohne ein Wort zu sagen。',
        [
            G('動詞加 zu', '第二個動作', [
                ['試著', 'versuchen, ... zu', '試著做'],
                ['別忘了', 'vergessen, ... zu', '忘記做'],
                ['打算', 'vorhaben, ... zu', '打算做'],
                ['開始', 'anfangen, ... zu', '開始做'],
            ], [
                ['Ich versuche, jeden Tag zu lernen.', '我試著每天學習。'],
                ['Vergiss nicht, die Tür zu schließen.', '別忘了關門。'],
                ['Ich habe vor, mehr zu lesen.', '我打算多讀一點。'],
                ['Sie fängt an, besser zu sprechen.', '她開始說得比較好。'],
            ]),
            G('um ... zu', '為了，主詞相同', [
                ['為了學習', 'um Deutsch zu lernen', '為了學德文'],
                ['為了通過', 'um die Prüfung zu bestehen', '為了通過考試'],
                ['為了準時', 'um pünktlich zu sein', '為了準時'],
                ['重要的是', 'Es ist wichtig, ... zu', '做某事是重要的'],
            ], [
                ['Ich lerne Deutsch, um in Deutschland zu studieren.', '我學德文，為了到德國讀書。'],
                ['Sie steht früh auf, um den Zug zu erreichen.', '她早起，為了趕上火車。'],
                ['Es ist wichtig, ruhig zu bleiben.', '保持冷靜很重要。'],
                ['Wir bleiben hier, um den Zug nicht zu verpassen.', '我們留在這裡，免得錯過火車。'],
            ]),
            G('damit', '為了，主詞不同', [
                ['不同主詞', 'damit mein Bruder es versteht', '好讓我的兄弟聽得懂'],
                ['相同主詞也可用', 'damit ich bestehe', '好讓我通過'],
                ['動詞位置', '在 damit 從句句尾', 'versteht、bestehe'],
                ['不要加 zu', 'damit 後面是完整從句', '有自己的主詞和變位動詞'],
            ], [
                ['Ich spreche langsam, damit du mich verstehst.', '我說慢一點，好讓你聽懂我。'],
                ['Sie erklärt es noch einmal, damit alle es verstehen.', '她再解釋一次，好讓大家都懂。'],
                ['Ich wiederhole die Wörter, damit ich sie nicht vergesse.', '我複習單字，免得忘掉。'],
                ['Er schreibt den Satz auf, damit wir ihn lesen können.', '他把句子寫下來，好讓我們能讀。'],
            ]),
        ],
    ),
    L(
        'konnektoren', 'B1', 'Konnektoren', '德文 B1｜連接詞',
        'obwohl、damit、als、wenn、nachdem 把動詞放在從句句尾。trotzdem 是副詞，後面的動詞仍在第二位。',
        '雖然、為了、過去一次與重複，以及 nachdem 的過去完成，附例句、中文、朗讀與 PDF。',
        'als 是過去發生一次。wenn 是重複、現在或未來。\nobwohl 動詞在句尾。trotzdem 後面動詞第二位：Es regnet. Trotzdem gehen wir.',
        [
            G('obwohl 與 trotzdem', '雖然，兩種詞序', [
                ['從句', 'obwohl es regnet', '雖然下雨'],
                ['副詞', 'Trotzdem gehen wir.', '儘管如此我們還是去'],
                ['逗號', 'Obwohl es regnet, ...', '從句在前要逗號'],
                ['不要', 'obwohl 後面動詞不在第二位', '動詞在句尾'],
            ], [
                ['Obwohl es regnet, gehen wir spazieren.', '雖然下雨，我們還是去散步。'],
                ['Es regnet. Trotzdem gehen wir spazieren.', '下雨了。儘管如此我們還是去散步。'],
                ['Obwohl ich müde bin, lerne ich weiter.', '雖然我累了，我還是繼續學。'],
                ['Der Text ist schwer. Trotzdem verstehe ich ihn.', '課文很難。儘管如此我還是看得懂。'],
            ]),
            G('als 與 wenn', '一次，或是重複', [
                ['過去一次', 'als ich in Berlin war', '當我在柏林時'],
                ['每當', 'wenn ich Zeit hatte', '每當我有時間'],
                ['未來如果', 'wenn ich Zeit habe', '如果我有時間'],
                ['不要混', 'als 不談未來', '未來用 wenn'],
            ], [
                ['Als ich in Berlin war, habe ich viel gesehen.', '我在柏林的時候，看了很多東西。'],
                ['Wenn ich früher aufstand, frühstückte ich immer.', '以前我早起的時候，總是會吃早餐。'],
                ['Wenn ich morgen Zeit habe, rufe ich dich an.', '如果我明天有時間，我會打電話給你。'],
                ['Als sie ankam, war der Kurs schon vorbei.', '她到達的時候，課已經結束了。'],
            ]),
            G('nachdem', '先發生的事用過去完成', [
                ['先吃完', 'nachdem ich gegessen hatte', '我吃完之後'],
                ['助動詞', 'hatte / war + 過去分詞', '過去完成'],
                ['主句', '多用 Präteritum', '然後才發生'],
                ['移動', 'nachdem sie angekommen war', '她到達之後'],
            ], [
                ['Nachdem ich gegessen hatte, ging ich spazieren.', '我吃完之後去散步。'],
                ['Nachdem sie angekommen war, rief sie mich an.', '她到了之後打電話給我。'],
                ['Nachdem wir bezahlt hatten, verließen wir das Café.', '我們付完帳之後離開咖啡館。'],
                ['Er ging erst, nachdem er den Text gelesen hatte.', '他讀完課文才走。'],
            ]),
        ],
    ),
    L(
        'passiv', 'B1', 'Passiv', '德文 B1｜過程被動',
        '過程被動用 werden 加過去分詞。誰做的用 von。完成式的最後一個詞是 worden，不是 geworden。',
        '現在、過去、完成被動，以及與格動詞的被動，附例句、中文、朗讀與 PDF。',
        '完成被動：ist geschrieben worden。不要說 ist geschrieben geworden。\n與格動詞改成被動時，與格留著：Mir wird geholfen。',
        [
            G('現在與過去', 'wird 或 wurde + 過去分詞', [
                ['現在', 'wird gesprochen', '有人在說'],
                ['過去', 'wurde geschrieben', '當時被寫下'],
                ['施事者', 'von der Lehrerin', '由女老師'],
                ['不說施事者', 'Hier wird Deutsch gesprochen.', '這裡說德文'],
            ], [
                ['Hier wird Deutsch gesprochen.', '這裡說德文。'],
                ['Der Text wurde gestern geschrieben.', '課文是昨天寫的。'],
                ['Das Fenster wurde von der Lehrerin geöffnet.', '窗戶是女老師打開的。'],
                ['In Taiwan wird viel Tee getrunken.', '台灣喝很多茶。'],
            ]),
            G('完成', 'worden 放在句尾', [
                ['已經', 'ist bezahlt worden', '已經被付了'],
                ['疑問', 'Ist das schon gemacht worden?', '那已經做了嗎？'],
                ['否定', 'ist noch nicht korrigiert worden', '還沒被改'],
                ['不要', 'geworden', '完成被動不用這個'],
            ], [
                ['Die Rechnung ist schon bezahlt worden.', '帳單已經付了。'],
                ['Der Fehler ist noch nicht korrigiert worden.', '這個錯誤還沒被改正。'],
                ['Ist die E-Mail schon geschickt worden?', '電子郵件已經寄出了嗎？'],
                ['Die Tür ist von ihm geöffnet worden.', '門是他打開的。'],
            ]),
            G('與格保留', '沒有直接受詞的動詞', [
                ['幫助我', 'Mir wird geholfen.', '有人幫我。'],
                ['感謝您', 'Ihnen wird gedankt.', '有人感謝您。'],
                ['過去', 'Mir wurde nicht geholfen.', '當時沒有人幫我。'],
                ['給', 'Dem Kind wird ein Buch gegeben.', '有人給孩子一本書。'],
            ], [
                ['Mir wird im Kurs geholfen.', '課堂上有人幫我。'],
                ['Den Gästen wird gedankt.', '有人向客人致謝。'],
                ['Mir wurde gestern nicht geantwortet.', '昨天沒有人回我。'],
                ['Dem Kind wurde eine Geschichte erzählt.', '有人說了一個故事給孩子聽。'],
            ]),
        ],
    ),
    L(
        'konjunktiv-ii', 'B1', 'Konjunktiv II', '德文 B1｜第二虛擬式',
        '和現在事實相反，或想說得客氣，用 wäre、hätte、würde。口語裡大多數動詞用 würde 加原形。',
        'würde、wäre、hätte、könnte，以及 wenn 從句，附例句、中文、朗讀與 PDF。',
        '禮貌：Ich hätte gern einen Tee。Könnten Sie das wiederholen?\n假設：Wenn ich Zeit hätte, würde ich mehr lesen。sein 用 wäre，haben 用 hätte，通常不用 würde sein。',
        [
            G('würde', '口語最常用', [
                ['我會', 'ich würde bleiben', '我會留下'],
                ['你會', 'würdest du kommen?', '你會來嗎？'],
                ['禮貌請求', 'Würden Sie mir helfen?', '您可以幫我嗎？'],
                ['建議', 'An deiner Stelle würde ich fragen.', '如果我是你，我會問。'],
            ], [
                ['Ich würde mehr lesen.', '我會多讀一點。'],
                ['Würdest du mitkommen?', '你會一起去嗎？'],
                ['Würden Sie bitte langsamer sprechen?', '請您說慢一點好嗎？'],
                ['An deiner Stelle würde ich den Kurs nehmen.', '如果我是你，我會選這堂課。'],
            ]),
            G('wäre 與 hätte', '是、有的假設', [
                ['如果是', 'wenn ich in Berlin wäre', '如果我在柏林'],
                ['如果有', 'wenn ich Zeit hätte', '如果我有時間'],
                ['點餐', 'Ich hätte gern einen Tee.', '我想要一杯茶。'],
                ['如果我是你', 'wenn ich du wäre', '如果我是你'],
            ], [
                ['Wenn ich in Berlin wäre, würde ich viel spazieren gehen.', '如果我在柏林，我會常常散步。'],
                ['Wenn ich Zeit hätte, würde ich mehr lernen.', '如果我有時間，我會多學一點。'],
                ['Ich hätte gern einen Kaffee.', '我想要一杯咖啡。'],
                ['Wenn ich du wäre, würde ich nachfragen.', '如果我是你，我會再問一次。'],
            ]),
            G('könnte', '有可能、可以請對方', [
                ['我可以', 'ich könnte kommen', '我可以來'],
                ['您可以', 'Könnten Sie das wiederholen?', '您可以再說一次嗎？'],
                ['也許', 'Das könnte stimmen.', '那有可能是對的。'],
                ['從句', 'wenn du könntest', '如果你可以的話'],
            ], [
                ['Könnten Sie das bitte wiederholen?', '請您再說一次好嗎？'],
                ['Ich könnte dir morgen helfen.', '我明天可以幫你。'],
                ['Das könnte ein Fehler sein.', '那有可能是一個錯誤。'],
                ['Wenn du könntest, würde ich mich freuen.', '如果你可以的話，我會很高興。'],
            ]),
        ],
    ),
    L(
        'genitiv', 'B1', 'Genitiv', '德文 B1｜屬格',
        '屬格表示誰的，或放在 wegen、trotz、während 後面。陽性與中性名詞通常加 -s 或 -es。',
        'des、der，專有名詞的 -s，以及口語用 von 的說法，附例句、中文、朗讀與 PDF。',
        '口語常用 von 加與格：das Auto von meinem Bruder。書面用屬格：das Auto meines Bruders。\n陰性和複數不加 -s：der Mutter，der Kinder。冠詞是 der。',
        [
            G('誰的', 'des 與 der', [
                ['陽性', 'des Vaters / meines Bruders', '父親的／我兄弟的'],
                ['中性', 'des Kindes / des Films', '孩子的／電影的'],
                ['陰性', 'der Mutter / der Lehrerin', '母親的／女老師的'],
                ['複數', 'der Kinder', '孩子們的'],
            ], [
                ['Das ist das Auto meines Bruders.', '這是我兄弟的車。'],
                ['Das Ende des Films war überraschend.', '電影的結尾令人意外。'],
                ['Die Tasche der Lehrerin ist blau.', '女老師的袋子是藍色的。'],
                ['Die Namen der Kinder stehen auf der Liste.', '孩子們的名字在名單上。'],
            ]),
            G('介系詞', 'wegen、trotz、während', [
                ['因為', 'wegen des Regens', '因為下雨'],
                ['儘管', 'trotz der Kälte', '儘管寒冷'],
                ['在……期間', 'während des Unterrichts', '上課期間'],
                ['誰的', 'Wessen Tasche ist das?', '這是誰的袋子？'],
            ], [
                ['Wegen des Regens bleiben wir hier.', '因為下雨，我們留在這裡。'],
                ['Trotz der Kälte geht sie spazieren.', '儘管寒冷，她還是去散步。'],
                ['Während des Unterrichts spricht er Deutsch.', '上課時他說德文。'],
                ['Wessen Buch ist das?', '這是誰的書？'],
            ]),
            G('名字與口語', '-s，或 von', [
                ['名字', 'Annas Buch', 'Anna 的書'],
                ['以 s 結尾', 'das Auto von Hans', 'Hans 的車，口語用 von'],
                ['口語', 'das Buch von Anna', 'Anna 的書'],
                ['書面', 'das Buch meines Vaters', '我父親的書'],
            ], [
                ['Das ist Annas Buch.', '這是 Anna 的書。'],
                ['Das Auto von Hans ist neu.', 'Hans 的車是新的。'],
                ['Das ist das Buch von Anna.', '這是 Anna 的書。'],
                ['Die Farbe des Hauses gefällt mir.', '我喜歡這房子的顏色。'],
            ]),
        ],
    ),
    L(
        'n-deklination', 'B1', 'n-Deklination', '德文 B1｜弱變化陽性名詞',
        '一部分陽性名詞除了主格單數，其他格都加 -en 或 -n。多半是人或職業。',
        'Student、Kollege、Herr、Name 的格變化，附例句、中文、朗讀與 PDF。',
        '除了主格單數，都要加詞尾：den Studenten，dem Studenten，des Studenten。\nHerr 的詞尾是短的 -n：den Herrn，des Herrn。Name 的屬格是 des Namens。',
        [
            G('-ent 與 -e', '學生、同事、男孩', [
                ['主格', 'der Student', '學生'],
                ['受格／與格／屬格', 'den / dem / des Studenten', '學生的其他格'],
                ['同事', 'der Kollege / den Kollegen', '同事'],
                ['男孩', 'der Junge / den Jungen', '男孩'],
            ], [
                ['Der Student kommt aus Korea.', '這名學生來自韓國。'],
                ['Ich kenne den Studenten.', '我認識這名學生。'],
                ['Ich danke dem Kollegen.', '我感謝這位同事。'],
                ['Kennst du den Jungen?', '你認識那個男孩嗎？'],
            ]),
            G('Herr 與 Name', '詞尾比較短，或屬格加 -s', [
                ['先生主格', 'der Herr', '先生'],
                ['先生其他格', 'den Herrn / dem Herrn / des Herrn', '先生'],
                ['名字', 'der Name / den Namen', '名字'],
                ['名字屬格', 'des Namens', '名字的'],
            ], [
                ['Der Herr an der Tür heißt Müller.', '門口那位先生叫 Müller。'],
                ['Ich danke dem Herrn.', '我感謝這位先生。'],
                ['Wie schreibt man den Namen?', '這個名字怎麼拼？'],
                ['Der Name des Herrn ist Müller.', '這位先生的名字是 Müller。'],
            ]),
            G('怎麼認', '人、職業、少數例外', [
                ['職業', 'Journalist, Student', '以 -ent、-ant、-ist 結尾'],
                ['人', 'Kollege, Junge, Mensch', '陽性、指人、以 -e 結尾'],
                ['人', 'den Menschen', '人（受格）'],
                ['要一起記', 'Herr, Name', '不規則的短詞尾'],
            ], [
                ['Der Journalist stellt eine Frage.', '記者問了一個問題。'],
                ['Wir kennen den Journalisten.', '我們認識這位記者。'],
                ['Der Mensch braucht Schlaf.', '人需要睡眠。'],
                ['Ich frage den Menschen an der Tür.', '我問門口那個人。'],
            ]),
        ],
    ),
    L(
        'verben-praep', 'B1', 'Verben + Präposition', '德文 B1｜動詞配介系詞',
        '有些動詞自己帶一個固定介系詞，格也固定。不能按中文的意思換成別的介系詞。',
        'warten auf、denken an、sprechen mit、sich freuen auf 與 über，附例句、中文、朗讀與 PDF。',
        '介系詞是動詞的一部分。問句用 wo(r) 加同一個介系詞：Worauf wartest du?\n人用介系詞加代名詞：Auf wen wartest du?',
        [
            G('受格', 'auf、an、über、für', [
                ['等待', 'warten auf + 受格', '等待某人某事'],
                ['想到', 'denken an + 受格', '想到某人某事'],
                ['談論', 'sprechen über + 受格', '談論某事'],
                ['對……有興趣', 'sich interessieren für', '對某事有興趣'],
            ], [
                ['Ich warte auf den Zug.', '我在等火車。'],
                ['Worauf wartest du?', '你在等什麼？'],
                ['Ich denke oft an meine Familie.', '我常常想到我的家人。'],
                ['Sie spricht über ihren Plan.', '她在談她的計劃。'],
            ]),
            G('與格', 'mit、bei、nach', [
                ['和……說', 'sprechen mit + 與格', '和某人說話'],
                ['幫忙做', 'helfen bei + 與格', '幫忙某事'],
                ['詢問', 'fragen nach + 與格', '詢問某事'],
                ['屬於', 'gehören zu + 與格', '屬於某一群'],
            ], [
                ['Sie spricht mit ihrer Chefin.', '她在和她的主管說話。'],
                ['Kannst du mir bei der Aufgabe helfen?', '你能幫我做這份作業嗎？'],
                ['Er fragt nach dem Preis.', '他詢問價格。'],
                ['Das gehört nicht zu meiner Arbeit.', '那不屬於我的工作。'],
            ]),
            G('auf 或 über', '尚未發生，或已經發生', [
                ['期待', 'sich freuen auf + 受格', '期待尚未發生的事'],
                ['高興', 'sich freuen über + 受格', '為已發生的事高興'],
                ['問期待', 'Worauf freust du dich?', '你在期待什麼？'],
                ['問原因', 'Worüber freust du dich?', '你為什麼高興？'],
            ], [
                ['Wir freuen uns auf das Wochenende.', '我們期待週末。'],
                ['Er freut sich über das Geschenk.', '他為這份禮物感到高興。'],
                ['Worauf freust du dich?', '你在期待什麼？'],
                ['Wir freuen uns über die Nachricht.', '我們為這個消息感到高興。'],
            ]),
        ],
    ),
    L(
        'rede', 'B1', 'Indirekte Rede', '德文 B1｜間接轉述',
        '轉述一件事用 dass。轉述問句時，是非問句用 ob，其他疑問詞留著，動詞都放在句尾。',
        'dass、時態是否倒退、間接問句，以及用 sollen 轉述命令，附例句、中文、朗讀與 PDF。',
        '事情現在仍成立時，從句可維持現在式：Er sagte, dass er in Taipei wohnt。\n轉述命令用 sollen：Er sagte, ich soll pünktlich kommen。',
        [
            G('dass', '轉述一句話', [
                ['現在說', 'Sie sagt, dass sie müde ist.', '她說她累了。'],
                ['當時說', 'Sie sagte, dass sie müde war.', '她當時說她累了。'],
                ['現在仍成立', 'Er sagte, dass er in Taipei wohnt.', '他說他住在台北。'],
                ['逗號', 'sagt, dass', 'dass 前要逗號'],
            ], [
                ['Anna sagt, dass sie keine Zeit hat.', 'Anna 說她沒有時間。'],
                ['Anna sagte, dass sie keine Zeit hatte.', 'Anna 當時說她沒有時間。'],
                ['Er sagte, dass er in Taipei wohnt.', '他說他住在台北。'],
                ['Ich habe gehört, dass der Kurs ausfällt.', '我聽說這堂課取消了。'],
            ]),
            G('間接問句', 'ob 或原來的疑問詞', [
                ['是非', 'ob ich Zeit habe', '我有沒有時間'],
                ['哪裡', 'wo ich wohne', '我住在哪裡'],
                ['為什麼', 'warum sie kommt', '她為什麼來'],
                ['句尾', '動詞在從句句尾', '沒有問句語序'],
            ], [
                ['Sie fragt, ob ich Zeit habe.', '她問我有沒有時間。'],
                ['Er fragte mich, wo ich wohne.', '他問我住在哪裡。'],
                ['Weißt du, wann der Zug kommt?', '你知道火車幾點到嗎？'],
                ['Sie wollte wissen, warum ich Deutsch lerne.', '她想知道我為什麼學德文。'],
            ]),
            G('命令', '用 sollen 轉述', [
                ['要我來', 'ich soll kommen', '我應該來'],
                ['過去', 'ich sollte früher kommen', '我當時應該早點來'],
                ['不要', 'wir sollen nicht warten', '我們不該等'],
                ['請某人', 'Er bat mich, früher zu kommen.', '他請我早點來'],
            ], [
                ['Der Lehrer sagt, wir sollen den Text lesen.', '老師說我們應該讀課文。'],
                ['Er sagte, ich sollte pünktlich kommen.', '他當時說我應該準時來。'],
                ['Sie sagt, ich soll sie anrufen.', '她說我應該打電話給她。'],
                ['Er bat mich, die Tür zu schließen.', '他請我把門關上。'],
            ]),
        ],
    ),
]
