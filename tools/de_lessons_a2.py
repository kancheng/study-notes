"""German A2 grammar aligned with Goethe Start Deutsch 2 (GER A2)."""
from lesson_util import G, L

LESSONS = [
    L(
        'perfekt', 'A2', 'Perfekt', '德文 A2｜現在完成式',
        '口語說過去，多用 Perfekt：助動詞 haben 或 sein 放在第二位，過去分詞放在句尾。',
        'haben 與 sein 的選擇、規則與不規則過去分詞，附例句、中文、朗讀與 PDF。',
        '移動、狀態改變，以及 sein、bleiben、werden，助動詞用 sein。\n大多數其他動詞用 haben。不可分前綴 be-、er-、ver- 的過去分詞不加 ge。',
        [
            G('haben', '規則與不規則過去分詞', [
                ['學習', 'gelernt', '學過'],
                ['工作', 'gearbeitet', '工作過'],
                ['讀', 'gelesen', '讀過'],
                ['說', 'gesprochen', '說過'],
            ], [
                ['Ich habe gestern Deutsch gelernt.', '我昨天學了德文。'],
                ['Hast du schon gegessen?', '你吃過了嗎？'],
                ['Er hat einen Kaffee getrunken.', '他喝了一杯咖啡。'],
                ['Wir haben Freunde besucht.', '我們拜訪了朋友。'],
            ]),
            G('sein', '移動、停留、sein', [
                ['去', 'gegangen', '去過'],
                ['來', 'gekommen', '來過'],
                ['搭', 'gefahren', '搭過'],
                ['停留', 'geblieben', '留過'],
            ], [
                ['Ich bin nach Hause gegangen.', '我回家了。'],
                ['Sie ist mit dem Bus gekommen.', '她搭公車來了。'],
                ['Wir sind nach Berlin gefahren.', '我們去了柏林。'],
                ['Bist du zu Hause geblieben?', '你留在家裡了嗎？'],
            ]),
            G('句中的位置', '助動詞第二位，分詞句尾', [
                ['昨天', 'Gestern habe ich gelesen.', '昨天我讀了書。'],
                ['已經', 'Ich habe schon gegessen.', '我已經吃了。'],
                ['從未', 'Ich bin noch nie in Berlin gewesen.', '我從來沒去過柏林。'],
                ['疑問', 'Hast du das Buch gelesen?', '你讀了那本書嗎？'],
            ], [
                ['Gestern habe ich ein Buch gelesen.', '昨天我讀了一本書。'],
                ['Ich habe die E-Mail schon geschrieben.', '我已經寫了那封電子郵件。'],
                ['Sie ist noch nie in Taiwan gewesen.', '她從來沒來過台灣。'],
                ['Was hast du am Wochenende gemacht?', '你週末做了什麼？'],
            ]),
        ],
    ),
    L(
        'war-hatte', 'A2', 'War und Hatte', '德文 A2｜war 與 hatte',
        'sein 和 haben 說過去時，口語也常用簡單過去：war 和 hatte。其他動詞的簡單過去留到 B1。',
        'war、hatte 的六組人稱，以及和 Perfekt 的分工，附例句、中文、朗讀與 PDF。',
        '敘述昨天做了什麼，一般動詞仍用 Perfekt：Ich habe gelernt。\n是、有、在，常用 war 和 hatte：Ich war müde. Ich hatte Zeit.',
        [
            G('war', 'sein 的過去', [
                ['ich / er', 'war', '當時是'],
                ['du', 'warst', '你當時是'],
                ['wir / sie', 'waren', '當時是'],
                ['ihr', 'wart', '你們當時是'],
            ], [
                ['Ich war gestern müde.', '我昨天很累。'],
                ['Wo warst du?', '你當時在哪裡？'],
                ['Wir waren zu Hause.', '我們當時在家。'],
                ['Der Kurs war interessant.', '那堂課很有趣。'],
            ]),
            G('hatte', 'haben 的過去', [
                ['ich / er', 'hatte', '當時有'],
                ['du', 'hattest', '你當時有'],
                ['wir / sie', 'hatten', '當時有'],
                ['ihr', 'hattet', '你們當時有'],
            ], [
                ['Ich hatte keine Zeit.', '我當時沒有時間。'],
                ['Hattest du Hunger?', '你當時餓嗎？'],
                ['Wir hatten eine Frage.', '我們當時有一個問題。'],
                ['Sie hatte einen Bruder.', '她當時有一個兄弟。'],
            ]),
            G('怎麼選', 'war、hatte 或 Perfekt', [
                ['狀態', 'Ich war krank.', '我當時生病。'],
                ['擁有', 'Ich hatte ein Buch.', '我當時有一本書。'],
                ['做過的事', 'Ich habe geschlafen.', '我睡了。'],
                ['去過', 'Ich bin gegangen.', '我去了。'],
            ], [
                ['Gestern war ich zu Hause.', '昨天我在家。'],
                ['Ich hatte leider keine Zeit.', '我當時可惜沒有時間。'],
                ['Ich habe zehn Stunden geschlafen.', '我睡了十個小時。'],
                ['Danach bin ich spazieren gegangen.', '之後我去散步了。'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'trennbar', 'A2', 'Trennbar', '德文 A2｜可分動詞',
        '可分動詞的前綴在現在式裡放到句尾。完成式的 ge 夾在前綴和詞幹中間。',
        'aufstehen、anrufen、einkaufen 的現在式、命令句與 Perfekt，附例句、中文、朗讀與 PDF。',
        '前綴在句尾，中間可以放很多詞：Ich stehe um sieben Uhr auf。\n完成式：aufgestanden、angerufen、eingekauft。mitkommen 用 sein。',
        [
            G('現在式', '前綴放句尾', [
                ['起床', 'ich stehe auf', '我起床'],
                ['打電話', 'er ruft an', '他打電話'],
                ['購物', 'wir kaufen ein', '我們購物'],
                ['一起去', 'kommst du mit?', '你一起去嗎？'],
            ], [
                ['Ich stehe um sieben auf.', '我七點起床。'],
                ['Er ruft seine Mutter an.', '他打電話給他母親。'],
                ['Wir kaufen am Samstag ein.', '我們星期六購物。'],
                ['Kommst du heute mit?', '你今天一起去嗎？'],
            ]),
            G('Perfekt', 'ge 夾在前綴中間', [
                ['起床', 'aufgestanden', '起床了（用 sein）'],
                ['打電話', 'angerufen', '打過電話'],
                ['購物', 'eingekauft', '買過東西'],
                ['一起去', 'mitgekommen', '一起去了（用 sein）'],
            ], [
                ['Ich bin um sieben aufgestanden.', '我七點起了床。'],
                ['Hast du Anna angerufen?', '你打電話給 Anna 了嗎？'],
                ['Wir haben gestern eingekauft.', '我們昨天買了東西。'],
                ['Sie ist mitgekommen.', '她一起去了。'],
            ]),
            G('命令句', '前綴仍在句尾', [
                ['du', 'Steh auf!', '起床！'],
                ['ihr', 'Steht auf!', '你們起床！'],
                ['Sie', 'Stehen Sie auf!', '請您起床！'],
                ['開門', 'Mach die Tür auf!', '把門打開！'],
            ], [
                ['Steh bitte auf!', '請起床！'],
                ['Ruf mich später an!', '晚點打電話給我！'],
                ['Kommen Sie bitte mit!', '請您一起去！'],
                ['Machen Sie das Fenster auf!', '請打開窗戶！'],
            ]),
        ],
    ),
    L(
        'dativ', 'A2', 'Dativ', '德文 A2｜與格',
        '給誰、幫誰、對誰，用與格。複數與格冠詞是 den，名詞通常再加 -n。',
        '與格冠詞、人稱代名詞，以及 helfen、danken、gefallen、gehören，附例句、中文、朗讀與 PDF。',
        '複數與格：den Kindern，den Freunden。名詞若已是 -n 或 -s，就不再加：den Eltern，den Autos。\n人稱：mir、dir、ihm、ihr、uns、euch、ihnen、Ihnen。',
        [
            G('冠詞', '陽性與中性都變成 dem', [
                ['陽性', 'dem Mann / einem Freund', '這個男人／一位朋友'],
                ['陰性', 'der Frau / einer Freundin', '這個女人／一位女性朋友'],
                ['中性', 'dem Kind / einem Kind', '這個孩子'],
                ['複數', 'den Kindern', '這些孩子'],
            ], [
                ['Ich helfe dem Mann.', '我幫助那個男人。'],
                ['Das Buch gehört der Frau.', '這本書是那個女人的。'],
                ['Wir danken einem Freund.', '我們感謝一位朋友。'],
                ['Sie gibt den Kindern Wasser.', '她拿水給孩子們。'],
            ]),
            G('人稱代名詞', '給我、給你、給他', [
                ['我／你', 'mir / dir', '我／你'],
                ['他／她', 'ihm / ihr', '他／她'],
                ['我們／你們', 'uns / euch', '我們／你們'],
                ['他們／您', 'ihnen / Ihnen', '他們／您'],
            ], [
                ['Kannst du mir helfen?', '你能幫我嗎？'],
                ['Ich danke dir.', '我謝謝你。'],
                ['Das Buch gefällt ihm.', '他喜歡這本書。'],
                ['Wie geht es Ihnen?', '您好嗎？'],
            ]),
            G('固定用與格的動詞', '不是直接受詞', [
                ['幫助', 'helfen + 與格', '幫助某人'],
                ['感謝', 'danken + 與格', '感謝某人'],
                ['喜歡', 'gefallen + 與格', '令某人喜歡'],
                ['屬於', 'gehören + 與格', '屬於某人'],
            ], [
                ['Ich helfe meiner Mutter.', '我幫我母親。'],
                ['Wir danken Ihnen.', '我們感謝您。'],
                ['Der Film gefällt mir.', '我喜歡這部電影。'],
                ['Das Auto gehört meinem Bruder.', '這輛車是我兄弟的。'],
            ]),
        ],
    ),
    L(
        'praepositionen', 'A2', 'Präpositionen', '德文 A2｜介系詞與格',
        '有些介系詞永遠跟與格，有些永遠跟受格。雙向介系詞看是位置還是方向。',
        'aus、bei、mit、nach、seit、von、zu，受格介系詞，以及 auf、in 的位置與方向，附例句、中文、朗讀與 PDF。',
        'wo 用與格：Ich bin in der Schule。wohin 用受格：Ich gehe in die Schule。\n常用縮寫：zum、zur、ins、im、am。時間、方式、地點依序放：Ich fahre morgen mit dem Bus nach Berlin。',
        [
            G('永遠與格', 'aus bei mit nach seit von zu', [
                ['從', 'aus Taiwan', '從台灣'],
                ['在某人家', 'bei meinen Eltern', '在我父母家'],
                ['搭乘', 'mit dem Bus', '搭公車'],
                ['自從／去找', 'seit einem Monat / zum Arzt', '一個月以來／去看醫生'],
            ], [
                ['Ich komme aus Taiwan.', '我從台灣來。'],
                ['Sie wohnt bei ihren Eltern.', '她住在父母家。'],
                ['Wir fahren mit dem Zug.', '我們搭火車。'],
                ['Ich lerne seit einem Monat Deutsch.', '我學德文一個月了。'],
            ]),
            G('永遠受格', 'durch für gegen ohne um', [
                ['為了', 'für dich', '為了你'],
                ['穿過', 'durch den Park', '穿過公園'],
                ['沒有', 'ohne dich', '沒有你'],
                ['圍繞', 'um den Tisch', '圍著桌子'],
            ], [
                ['Das Geschenk ist für dich.', '這份禮物是給你的。'],
                ['Wir gehen durch den Park.', '我們穿過公園。'],
                ['Ohne dich gehe ich nicht.', '沒有你我不去。'],
                ['Die Kinder sitzen um den Tisch.', '孩子們圍著桌子坐。'],
            ]),
            G('位置或方向', 'wo 與格，wohin 受格', [
                ['在桌上', 'auf dem Tisch', '在桌上（位置）'],
                ['放到桌上', 'auf den Tisch', '放到桌上（方向）'],
                ['在學校', 'in der Schule', '在學校裡'],
                ['去學校', 'in die Schule', '到學校去'],
            ], [
                ['Das Buch liegt auf dem Tisch.', '書放在桌上。'],
                ['Ich lege das Buch auf den Tisch.', '我把書放到桌上。'],
                ['Wir sind in der Schule.', '我們在學校。'],
                ['Ich gehe in die Schule.', '我去學校。'],
            ]),
        ],
    ),
    L(
        'modalverben', 'A2', 'Modalverben', '德文 A2｜情態動詞',
        'müssen 是必須，dürfen 是被允許，sollen 是該做，wollen 是想要。真正的動詞仍以原形放在句尾。',
        'müssen、dürfen、wollen、sollen 的變位，以及不必和禁止的差別，附例句、中文、朗讀與 PDF。',
        'nicht dürfen 是禁止。nicht müssen 是不必。\nkönnen 和 möchten 已在 A1。人稱 man 常和這些動詞一起用：Man darf hier nicht rauchen。',
        [
            G('müssen', '必須', [
                ['ich / er', 'muss', '必須'],
                ['du', 'musst', '你必須'],
                ['wir / sie', 'müssen', '必須'],
                ['ihr', 'müsst', '你們必須'],
            ], [
                ['Ich muss heute arbeiten.', '我今天必須工作。'],
                ['Musst du schon gehen?', '你必須走了嗎？'],
                ['Wir müssen pünktlich sein.', '我們必須準時。'],
                ['Du musst nicht kommen.', '你不必來。'],
            ]),
            G('dürfen', '被允許', [
                ['ich / er', 'darf', '可以'],
                ['du', 'darfst', '你可以'],
                ['wir / sie', 'dürfen', '可以'],
                ['ihr', 'dürft', '你們可以'],
            ], [
                ['Darf ich das Fenster öffnen?', '我可以打開窗戶嗎？'],
                ['Hier darf man nicht rauchen.', '這裡禁止抽菸。'],
                ['Ihr dürft jetzt gehen.', '你們現在可以走了。'],
                ['Kinder dürfen den Wein nicht trinken.', '孩子不可以喝葡萄酒。'],
            ]),
            G('wollen 與 sollen', '想要，以及該做', [
                ['我要', 'ich will', '我想要'],
                ['你要', 'du willst', '你想要'],
                ['我應該', 'ich soll', '我應該'],
                ['您應該', 'Sie sollen', '您應該'],
            ], [
                ['Was willst du trinken?', '你想喝什麼？'],
                ['Sie will Ärztin werden.', '她想當醫生。'],
                ['Wir sollen den Text lesen.', '我們應該讀這篇課文。'],
                ['Soll ich das Fenster zumachen?', '要不要我把窗戶關上？'],
            ]),
        ],
        cols=('人稱', '形式', '中文'),
    ),
    L(
        'komparativ', 'A2', 'Komparativ', '德文 A2｜比較級與最高級',
        '比較級加 -er，最高級用 am ...-sten。一樣用 so ... wie，不一樣用 als。',
        '規則變化、變音、gut 和 gern 的不規則，附例句、中文、朗讀與 PDF。',
        '一樣：so groß wie。不一樣：größer als。\ngut 的比較級是 besser，最高級是 am besten。gern 是 lieber、am liebsten。viel 是 mehr、am meisten。',
        [
            G('規則', '-er 與 am ...-sten', [
                ['小', 'klein / kleiner / am kleinsten', '小／較小／最小'],
                ['快', 'schnell / schneller / am schnellsten', '快／較快／最快'],
                ['有趣', 'interessant / interessanter', '有趣／較有趣'],
                ['最高級', 'am interessantesten', '最有趣'],
            ], [
                ['Dieses Zimmer ist kleiner.', '這間房間比較小。'],
                ['Der Bus ist schneller als das Fahrrad.', '公車比腳踏車快。'],
                ['Das ist am interessantesten.', '那是最有趣的。'],
                ['Der Film ist interessanter als das Buch.', '電影比書有趣。'],
            ]),
            G('變音與不規則', '單音節常見變音', [
                ['大', 'groß / größer / am größten', '大／較大／最大'],
                ['老', 'alt / älter / am ältesten', '年長／較年長／最年長'],
                ['好', 'gut / besser / am besten', '好／較好／最好'],
                ['喜歡', 'gern / lieber / am liebsten', '喜歡／更喜歡／最喜歡'],
            ], [
                ['Taipei ist größer als Tainan.', '台北比台南大。'],
                ['Mein Bruder ist älter als ich.', '我的兄弟比我年長。'],
                ['Dieses Buch ist besser.', '這本書比較好。'],
                ['Am liebsten trinke ich Tee.', '我最喜歡喝茶。'],
            ]),
            G('一樣或不一樣', 'so ... wie 與 als', [
                ['一樣大', 'so groß wie', '和……一樣大'],
                ['不一樣', 'nicht so schwer wie', '沒有……那麼難'],
                ['比', 'größer als', '比……大'],
                ['更多', 'mehr als', '比……多'],
            ], [
                ['Sie spricht so gut wie du.', '她說得和你一樣好。'],
                ['Deutsch ist nicht so schwer wie Chinesisch.', '德文沒有中文那麼難。'],
                ['Er ist größer als sein Bruder.', '他比他的兄弟高。'],
                ['Ich habe mehr Zeit als gestern.', '我的時間比昨天多。'],
            ]),
        ],
    ),
    L(
        'adjektiv', 'A2', 'Adjektiv', '德文 A2｜形容詞詞尾',
        '形容詞放在 sein 後面、單獨描述時不加詞尾。放在冠詞和名詞中間才加詞尾。',
        '述語不加詞尾、定冠詞後的詞尾、ein 後面的詞尾，附例句、中文、朗讀與 PDF。',
        '先看冠詞，再看名詞的性別和格。\n陽性受格最容易錯：einen heißen Kaffee，den kleinen Tisch。',
        [
            G('述語', 'sein 後面不加詞尾', [
                ['熱', 'Der Kaffee ist heiß.', '咖啡是熱的。'],
                ['冷', 'Das Wasser ist kalt.', '水是冷的。'],
                ['好', 'Die Idee ist gut.', '這個主意很好。'],
                ['新', 'Die Bücher sind neu.', '這些書是新的。'],
            ], [
                ['Der Kaffee ist heiß.', '咖啡是熱的。'],
                ['Die Suppe ist warm.', '湯是溫的。'],
                ['Das Kind ist müde.', '孩子累了。'],
                ['Die Fragen sind schwer.', '這些問題很難。'],
            ]),
            G('定冠詞後面', 'der heiße Kaffee', [
                ['主格陽性', 'der heiße Kaffee', '熱咖啡'],
                ['受格陽性', 'den heißen Kaffee', '熱咖啡（受格）'],
                ['陰性', 'die gute Idee', '好主意'],
                ['複數', 'die neuen Bücher', '新書'],
            ], [
                ['Der heiße Kaffee steht auf dem Tisch.', '熱咖啡放在桌上。'],
                ['Ich trinke den heißen Kaffee.', '我喝這杯熱咖啡。'],
                ['Die gute Idee gefällt mir.', '我喜歡這個好主意。'],
                ['Die neuen Bücher sind teuer.', '這些新書很貴。'],
            ]),
            G('ein 後面', 'ein heißer Kaffee', [
                ['主格陽性', 'ein heißer Kaffee', '一杯熱咖啡'],
                ['受格陽性', 'einen heißen Kaffee', '一杯熱咖啡（受格）'],
                ['陰性', 'eine gute Idee', '一個好主意'],
                ['中性', 'ein kaltes Getränk', '一杯冷飲'],
            ], [
                ['Das ist ein heißer Kaffee.', '那是一杯熱咖啡。'],
                ['Ich möchte einen heißen Kaffee.', '我想要一杯熱咖啡。'],
                ['Sie hat eine gute Idee.', '她有一個好主意。'],
                ['Er bestellt ein kaltes Getränk.', '他點一杯冷飲。'],
            ]),
        ],
    ),
    L(
        'reflexiv', 'A2', 'Reflexiv', '德文 A2｜反身動詞',
        '動作回到主詞自己身上時，用反身代名詞。第三人稱和尊稱用 sich，其餘用人稱受格或與格。',
        'mich、dich、sich，身體部位的與格，以及 sich freuen auf 和 über，附例句、中文、朗讀與 PDF。',
        '受格反身：mich、dich、sich、uns、euch、sich。\n身體部位用與格反身，再加受格名詞：Ich wasche mir die Hände。',
        [
            G('受格反身', '洗自己、穿上、見面', [
                ['我', 'ich wasche mich', '我洗澡'],
                ['你', 'du wäschst dich', '你洗澡'],
                ['他', 'er zieht sich an', '他穿衣服'],
                ['我們', 'wir treffen uns', '我們見面'],
            ], [
                ['Ich wasche mich jeden Morgen.', '我每天早上洗澡。'],
                ['Wäschst du dich mit kaltem Wasser?', '你用冷水洗澡嗎？'],
                ['Er zieht sich schnell an.', '他很快穿上衣服。'],
                ['Wir treffen uns um acht.', '我們八點見面。'],
            ]),
            G('與格反身', '洗自己的某個部位', [
                ['手', 'ich wasche mir die Hände', '我洗手'],
                ['牙', 'du putzt dir die Zähne', '你刷牙'],
                ['頭髮', 'er kämmt sich die Haare', '他梳頭髮'],
                ['完成式', 'ich habe mir die Hände gewaschen', '我洗了手'],
            ], [
                ['Ich wasche mir die Hände.', '我洗手。'],
                ['Putzt du dir die Zähne?', '你刷牙了嗎？'],
                ['Sie kämmt sich die Haare.', '她梳頭髮。'],
                ['Er hat sich die Jacke angezogen.', '他穿上了外套。'],
            ]),
            G('固定搭配', '介系詞不能換', [
                ['期待', 'sich freuen auf + 受格', '期待尚未發生的事'],
                ['感到高興', 'sich freuen über + 受格', '為已經發生的事高興'],
                ['對……有興趣', 'sich interessieren für', '對某事有興趣'],
                ['坐下', 'ich setze mich', '我坐下'],
            ], [
                ['Ich freue mich auf den Kurs.', '我期待這堂課。'],
                ['Sie freut sich über das Geschenk.', '她為這份禮物感到高興。'],
                ['Er interessiert sich für Musik.', '他對音樂有興趣。'],
                ['Setz dich bitte!', '請坐下！'],
            ]),
        ],
    ),
    L(
        'nebensatz', 'A2', 'Nebensatz', '德文 A2｜從句',
        'weil、dass、wenn、ob 開頭的從句，動詞放到該從句的句尾。denn 不是從句，動詞仍在第二位。',
        'weil、dass、wenn、ob 與 denn 的動詞位置，附例句、中文、朗讀與 PDF。',
        'weil 把動詞送到句尾。denn 後面仍是正常主句：動詞第二位。\n從句前要加逗號。ob 用來轉述是非問句，dass 用來轉述一件事。',
        [
            G('weil 與 denn', '原因的兩種動詞位置', [
                ['因為（從句）', 'weil ich krank bin', '因為我生病'],
                ['因為（主句）', 'denn ich bin krank', '因為我生病'],
                ['所以留下', 'Ich bleibe zu Hause', '我留在家裡'],
                ['逗號', 'zu Hause, weil ...', '從句前要逗號'],
            ], [
                ['Ich bleibe zu Hause, weil ich krank bin.', '我留在家裡，因為我生病。'],
                ['Ich bleibe zu Hause, denn ich bin krank.', '我留在家裡，因為我生病。'],
                ['Sie lernt Deutsch, weil sie die Sprache braucht.', '她學德文，因為她需要這個語言。'],
                ['Er kommt nicht, denn er hat keine Zeit.', '他不來，因為他沒有時間。'],
            ]),
            G('dass 與 ob', '一件事，或是不是', [
                ['一件事', 'dass er kommt', '他會來'],
                ['不知道是不是', 'ob sie kommt', '她來不來'],
                ['我想', 'Ich denke, dass ...', '我認為……'],
                ['我不知道', 'Ich weiß nicht, ob ...', '我不知道是否……'],
            ], [
                ['Ich denke, dass er morgen kommt.', '我認為他明天會來。'],
                ['Sie sagt, dass sie müde ist.', '她說她累了。'],
                ['Ich weiß nicht, ob sie Zeit hat.', '我不知道她有沒有時間。'],
                ['Weißt du, ob der Kurs heute ist?', '你知道今天有沒有課嗎？'],
            ]),
            G('wenn', '如果、每當', [
                ['如果有時間', 'wenn ich Zeit habe', '如果我有時間'],
                ['從句在前', 'Wenn ich Zeit habe, koche ich.', '如果我有時間，我就煮飯。'],
                ['每當', 'wenn es regnet', '每當下雨'],
                ['動詞', '在從句句尾', 'habe、regnet'],
            ], [
                ['Wenn ich Zeit habe, koche ich.', '如果我有時間，我就煮飯。'],
                ['Ich bleibe hier, wenn es regnet.', '如果下雨，我就留在這裡。'],
                ['Wenn du willst, kommen wir mit.', '如果你願意，我們就一起去。'],
                ['Ruf mich an, wenn du ankommst.', '你到了就打電話給我。'],
            ]),
        ],
    ),
]
