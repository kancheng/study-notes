"""French A2 grammar aligned with DELF A2 (CECRL)."""
from lesson_util import G, L

LESSONS = [
    L(
        'passe-compose', 'A2', 'Passé composé', '法文 A2｜複合過去',
        '複合過去表示已經完成的事。大多數動詞用 avoir。表示移動、狀態變化，以及代詞動詞，用 être，過去分詞要配合主詞的性數。',
        'avoir 與 être 的複合過去、過去分詞配合，附例句、中文、朗讀與 PDF。',
        '用 être 的常見動詞：aller、venir、arriver、partir、entrer、sortir、monter、descendre、rester、tomber、naître、mourir、devenir。\n否定放在助動詞兩邊：je n’ai pas parlé、elle n’est pas partie。',
        [
            G('avoir', '大多數動詞', [
                ['說了', 'j’ai parlé', '我說了'],
                ['做完了', 'elle a fini', '她做完了'],
                ['搭了', 'nous avons pris', '我們搭了'],
                ['沒看', 'je n’ai pas vu', '我沒看'],
            ], [
                ['Hier, j’ai visité un musée.', '昨天我參觀了一座博物館。'],
                ['Elle a fini ses devoirs.', '她寫完作業了。'],
                ['Nous avons pris le métro.', '我們搭了地鐵。'],
                ['Je n’ai pas vu ce film.', '我沒看過這部電影。'],
            ]),
            G('être', '移動與變化，分詞要配合', [
                ['去了（陰）', 'elle est allée', '她去了'],
                ['到了', 'elle est arrivée', '她到了'],
                ['離開了', 'ils sont partis', '他們離開了'],
                ['去了（陰複）', 'elles sont allées', '她們去了'],
            ], [
                ['Elle est allée au cinéma.', '她去看電影了。'],
                ['Elle est arrivée à huit heures.', '她八點到了。'],
                ['Ils sont partis tôt.', '他們很早離開了。'],
                ['Elles sont restées à la maison.', '她們留在家裡。'],
            ]),
            G('分詞', '不規則的幾個', [
                ['做', 'fait', '做了'],
                ['看', 'vu', '看了'],
                ['拿', 'pris', '拿了'],
                ['寫', 'écrit', '寫了'],
            ], [
                ['J’ai fait un gâteau.', '我做了一個蛋糕。'],
                ['Tu as vu Marie ?', '你看到 Marie 了嗎？'],
                ['Il a pris un café.', '他喝了一杯咖啡。'],
                ['Nous avons écrit une lettre.', '我們寫了一封信。'],
            ]),
        ],
    ),
    L(
        'imparfait', 'A2', 'Imparfait', '法文 A2｜未完成過去',
        '未完成過去用來描寫過去的背景、習慣，以及當時正在持續的狀態。做法是拿 nous 現在式，去掉 -ons，再加詞尾。',
        'parler、être、avoir 的未完成過去，附例句、中文、朗讀與 PDF。',
        '詞尾是 -ais、-ais、-ait、-ions、-iez、-aient。\nêtre 的詞幹是 ét-：j’étais。avoir 的詞幹是 av-：j’avais。',
        [
            G('parler', '去掉 nous 的 -ons', [
                ['je', 'je parlais', '我當時說'],
                ['tu', 'tu parlais', '你當時說'],
                ['il / elle', 'il parlait', '他當時說'],
                ['nous', 'nous parlions', '我們當時說'],
                ['vous', 'vous parliez', '您當時說'],
                ['ils / elles', 'ils parlaient', '他們當時說'],
            ], [
                ['Quand j’étais petit, j’habitais à Paris.', '我小時候住在巴黎。'],
                ['Tous les soirs, nous regardions un film.', '以前我們每天晚上看一部電影。'],
                ['Elle parlait très vite.', '她當時說得很快。'],
                ['Vous habitiez où avant ?', '您以前住哪裡？'],
            ]),
            G('être', '詞幹 ét-', [
                ['je', 'j’étais', '我當時是'],
                ['il / elle', 'il était', '他當時是'],
                ['nous', 'nous étions', '我們當時是'],
                ['ils', 'ils étaient', '他們當時是'],
            ], [
                ['J’étais fatigué.', '我當時很累。'],
                ['Il était midi.', '當時是正午。'],
                ['Nous étions en classe.', '我們當時在上課。'],
                ['Ils étaient contents.', '他們當時很高興。'],
            ]),
            G('avoir 與天氣', '當時的狀態', [
                ['有', 'elle avait', '她當時有'],
                ['我們有', 'nous avions', '我們當時有'],
                ['天氣', 'il faisait froid', '當時很冷'],
                ['是', 'c’était', '那曾是'],
            ], [
                ['Elle avait un chien.', '她當時有一隻狗。'],
                ['Nous avions peu de temps.', '我們當時時間不多。'],
                ['Il faisait froid ce jour-là.', '那天很冷。'],
                ['C’était une belle ville.', '那曾是一座漂亮的城市。'],
            ]),
        ],
        cols=('人稱', '未完成過去', '中文'),
    ),
    L(
        'futur', 'A2', 'Futur', '法文 A2｜將來',
        '即將發生用 aller 加原形。較遠或書面的將來用簡單將來式，詞尾是 -ai、-as、-a、-ons、-ez、-ont。venir de 加原形表示剛剛做完。',
        '近期將來、簡單將來、venir de，附例句、中文、朗讀與 PDF。',
        'être 的將來是 je serai。avoir 是 j’aurai。aller 是 j’irai。faire 是 je ferai。venir 是 je viendrai。\n簡單將來的詞尾都要發音，和條件式的 -ais 不同。',
        [
            G('aller + 原形', '即將', [
                ['要走', 'je vais partir', '我要走了'],
                ['要吃', 'nous allons manger', '我們要吃了'],
                ['要看', 'elle va regarder', '她要看'],
                ['問', 'tu vas venir ?', '你要來嗎？'],
            ], [
                ['Je vais partir dans dix minutes.', '我十分鐘後要走。'],
                ['Nous allons manger bientôt.', '我們快要吃飯了。'],
                ['Elle va regarder ce film.', '她要看這部電影。'],
                ['Tu vas venir avec nous ?', '你要跟我們一起來嗎？'],
            ]),
            G('簡單將來', '詞尾 -ai、-as、-a', [
                ['工作', 'je travaillerai', '我將會工作'],
                ['去', 'nous irons', '我們將會去'],
                ['來', 'elle viendra', '她將會來'],
                ['是', 'je serai', '我將會是'],
            ], [
                ['Demain, je travaillerai.', '我明天會工作。'],
                ['L’année prochaine, nous irons en France.', '明年我們會去法國。'],
                ['Elle viendra à huit heures.', '她會在八點來。'],
                ['Je serai à la gare à midi.', '我正午會在火車站。'],
            ]),
            G('venir de', '剛剛', [
                ['剛吃完', 'je viens de manger', '我剛吃完'],
                ['剛離開', 'il vient de partir', '他剛離開'],
                ['剛到', 'nous venons d’arriver', '我們剛到'],
                ['問', 'tu viens de finir ?', '你剛做完嗎？'],
            ], [
                ['Je viens de manger.', '我剛吃完。'],
                ['Il vient de partir.', '他剛離開。'],
                ['Nous venons d’arriver.', '我們剛到。'],
                ['Tu viens de finir ?', '你剛做完嗎？'],
            ]),
        ],
    ),
    L(
        'comparatif', 'A2', 'Comparatif', '法文 A2｜比較',
        '比較用 plus、moins、aussi，後面加 que。bon 的比較級是 meilleur，bien 的比較級是 mieux。最高級在比較級前加定冠詞。',
        'plus que、moins que、aussi que、meilleur、mieux，附例句、中文、朗讀與 PDF。',
        'aussi 後面如果是形容詞，直接接形容詞：aussi grand que。如果是副詞 bien，說 aussi bien que。\n最高級：le plus grand、la plus intéressante、le meilleur。',
        [
            G('形容詞', '比…更、較不、一樣', [
                ['更高', 'plus grand que', '比…高'],
                ['較不貴', 'moins cher que', '比…便宜'],
                ['一樣', 'aussi patient que', '和…一樣有耐心'],
                ['更好', 'meilleur que', '比…好'],
            ], [
                ['Marie est plus grande que Paul.', 'Marie 比 Paul 高。'],
                ['Ce sac est moins cher que l’autre.', '這個袋子比另一個便宜。'],
                ['Il est aussi patient que toi.', '他和你一樣有耐心。'],
                ['Ce café est meilleur que l’autre.', '這杯咖啡比另一杯好。'],
            ]),
            G('副詞', 'mieux、aussi bien', [
                ['更好', 'mieux que', '比…做得好'],
                ['一樣好', 'aussi bien que', '和…一樣好'],
                ['較少', 'moins que', '比…少'],
                ['更多', 'plus que', '比…多'],
            ], [
                ['Elle chante mieux que moi.', '她唱得比我好。'],
                ['Il parle aussi bien que toi.', '他說得和你一樣好。'],
                ['Je dors moins que toi.', '我睡得比你少。'],
                ['Nous travaillons plus qu’avant.', '我們比以前工作得多。'],
            ]),
            G('最高級', 'le plus、le meilleur', [
                ['最高', 'le plus grand', '最高的'],
                ['最有趣', 'la plus intéressante', '最有趣的'],
                ['最好', 'le meilleur', '最好的'],
                ['最便宜', 'le moins cher', '最便宜的'],
            ], [
                ['C’est le plus grand musée de la ville.', '這是城裡最大的博物館。'],
                ['C’est la question la plus intéressante.', '這是最有趣的問題。'],
                ['C’est le meilleur café de la rue.', '這是這條街上最好的咖啡館。'],
                ['C’est le livre le moins cher.', '這是最便宜的書。'],
            ]),
        ],
    ),
    L(
        'pronoms', 'A2', 'Pronoms compléments', '法文 A2｜直接與間接受詞代詞',
        '直接受詞代替被動詞直接作用的人或物。間接受詞代替 à 後面的人。代詞放在變位動詞前面。否定時，ne 在代詞前，pas 在動詞後。',
        'le、la、les，以及 lui、leur，附例句、中文、朗讀與 PDF。',
        'le 在母音前寫成 l’。\n兩個代詞同時出現、以及複合過去裡代詞的位置，放到 B1。',
        [
            G('直接', 'le、la、les', [
                ['他（陽）', 'je le vois', '我看見他'],
                ['她（陰）', 'je la connais', '我認識她'],
                ['他們', 'je les aime', '我喜歡它們'],
                ['否定', 'je ne le connais pas', '我不認識他'],
            ], [
                ['Je vois Paul. Je le vois.', '我看見 Paul。我看見他。'],
                ['Je connais Marie. Je la connais.', '我認識 Marie。我認識她。'],
                ['Tu aimes ces livres ? Oui, je les aime.', '你喜歡這些書嗎？對，我喜歡。'],
                ['Je ne le connais pas.', '我不認識他。'],
            ]),
            G('間接', 'lui、leur，代替 à + 人', [
                ['對他／她', 'je lui parle', '我跟他說'],
                ['對他們', 'je leur téléphone', '我打電話給他們'],
                ['給我', 'tu me parles', '你在跟我說'],
                ['否定', 'je ne lui parle pas', '我不跟他說'],
            ], [
                ['Je parle à Marie. Je lui parle.', '我在跟 Marie 說話。我在跟她說。'],
                ['Je téléphone à mes parents. Je leur téléphone.', '我打電話給父母。我打電話給他們。'],
                ['Tu me parles ?', '你在跟我說話嗎？'],
                ['Je ne lui écris pas souvent.', '我不常寫信給他。'],
            ]),
            G('位置', '動詞前，原形前', [
                ['現在', 'je le vois', '我看見他'],
                ['即將', 'je vais le voir', '我要去看他'],
                ['可以', 'tu peux la prendre', '你可以拿它'],
                ['想', 'je veux les voir', '我想看它們'],
            ], [
                ['Je le vois tous les jours.', '我每天看見他。'],
                ['Je vais le voir demain.', '我明天要去看他。'],
                ['Tu peux la prendre.', '你可以拿它。'],
                ['Nous allons leur écrire.', '我們要寫信給他們。'],
            ]),
        ],
    ),
    L(
        'y-en', 'A2', 'Y et en', '法文 A2｜y 與 en',
        'y 代替地點，也代替 à 加上事物。en 代替 de 加上事物，也代替數量。兩個都放在動詞前面。',
        'y、en、il y en a，附例句、中文、朗讀與 PDF。',
        '人不用 y。à Marie 用 lui，不用 y。\n數量留下時，en 仍然要放：J’en ai deux.',
        [
            G('y', '那裡、à + 事物', [
                ['去那裡', 'j’y vais', '我去那裡'],
                ['住那裡', 'j’y habite', '我住那裡'],
                ['想到', 'j’y pense', '我在想那件事'],
                ['否定', 'je n’y vais pas', '我不去那裡'],
            ], [
                ['Tu vas à la bibliothèque ? Oui, j’y vais.', '你去圖書館嗎？對，我去。'],
                ['J’habite à Taipei. J’y habite depuis un an.', '我住台北。我在那裡住了一年。'],
                ['Tu penses à l’examen ? Oui, j’y pense.', '你在想考試嗎？對，我在想。'],
                ['Je n’y vais pas aujourd’hui.', '我今天不去那裡。'],
            ]),
            G('en', 'de + 事物、數量', [
                ['要一些', 'j’en veux', '我要一些'],
                ['有兩個', 'j’en ai deux', '我有兩個'],
                ['需要', 'j’en ai besoin', '我需要'],
                ['否定', 'je n’en veux pas', '我不要'],
            ], [
                ['Tu veux du café ? Oui, j’en veux.', '你要咖啡嗎？好，我要。'],
                ['Combien de frères as-tu ? J’en ai deux.', '你有幾個兄弟？我有兩個。'],
                ['Tu as besoin d’un stylo ? Oui, j’en ai besoin.', '你需要筆嗎？對，我需要。'],
                ['Merci, je n’en veux pas.', '謝謝，我不要了。'],
            ]),
            G('il y en a', '那裡有一些', [
                ['有', 'il y en a', '有一些'],
                ['還有', 'il y en a encore', '還有'],
                ['沒有', 'il n’y en a pas', '沒有'],
                ['有三個', 'il y en a trois', '有三個'],
            ], [
                ['Il y a des chaises ? Oui, il y en a.', '有椅子嗎？有的。'],
                ['Il y en a encore.', '還有一些。'],
                ['Il n’y en a plus.', '已經沒有了。'],
                ['Combien de cafés est-ce qu’il y a ? Il y en a trois.', '有幾家咖啡館？有三家。'],
            ]),
        ],
    ),
    L(
        'partitif', 'A2', 'Article partitif', '法文 A2｜部分冠詞',
        '吃喝、物質、說不出一件一件的東西，用 du、de la、de l’。否定句裡，這些冠詞改成 de 或 d’。avoir besoin de 的 de 也一樣。',
        'du、de la、de l’，以及否定的 de，附例句、中文、朗讀與 PDF。',
        'du café 是一些咖啡。un café 是一杯咖啡。\n否定：Je ne bois pas de café. 母音前：Je ne bois pas d’eau.',
        [
            G('部分冠詞', '一些', [
                ['陽', 'du thé', '一些茶'],
                ['陰', 'de la soupe', '一些湯'],
                ['母音', 'de l’eau', '一些水'],
                ['複數不可數感', 'des pâtes', '一些義大利麵'],
            ], [
                ['Je bois du thé.', '我喝茶。'],
                ['Elle mange de la soupe.', '她喝湯。'],
                ['Nous prenons de l’eau.', '我們喝水。'],
                ['Ils mangent des pâtes.', '他們吃義大利麵。'],
            ]),
            G('否定', '改成 de', [
                ['不喝', 'pas de café', '不喝咖啡'],
                ['不吃', 'pas de viande', '不吃肉'],
                ['沒有水', 'pas d’eau', '沒有水'],
                ['不要', 'pas de sucre', '不要糖'],
            ], [
                ['Je ne bois pas de café.', '我不喝咖啡。'],
                ['Elle ne mange pas de viande.', '她不吃肉。'],
                ['Il n’y a pas d’eau.', '沒有水。'],
                ['Je ne prends pas de sucre.', '我不加糖。'],
            ]),
            G('avoir 的慣用', '需要、餓、渴', [
                ['需要', 'avoir besoin de', '需要'],
                ['餓', 'avoir faim', '餓'],
                ['渴', 'avoir soif', '渴'],
                ['冷', 'avoir froid', '覺得冷'],
            ], [
                ['J’ai besoin d’un stylo.', '我需要一支筆。'],
                ['Tu as faim ?', '你餓了嗎？'],
                ['J’ai soif.', '我渴了。'],
                ['Elles ont froid.', '她們覺得冷。'],
            ]),
        ],
    ),
    L(
        'imperatif', 'A2', 'Impératif', '法文 A2｜命令式',
        '命令式只有 tu、nous、vous。-er 動詞的 tu 不加 -s。否定時 ne…pas 包住動詞。代詞在肯定命令後面，用連字號；在否定命令前面。',
        'parler、finir、être、avoir，以及 vas-y，附例句、中文、朗讀與 PDF。',
        'aller 的 tu 肯定是 va，但 vas-y 要加 s。\nêtre：sois、soyons、soyez。avoir：aie、ayons、ayez。',
        [
            G('肯定', 'tu、nous、vous', [
                ['你說', 'parle', '說吧'],
                ['我們做完', 'finissons', '我們做完吧'],
                ['請您', 'parlez', '請說'],
                ['請慢一點', 'parle plus lentement', '說慢一點'],
            ], [
                ['Parle plus lentement, s’il te plaît.', '請說慢一點。'],
                ['Finissons ce travail.', '我們把這件工作做完吧。'],
                ['Écoutez bien.', '請仔細聽。'],
                ['Ouvre la fenêtre.', '把窗戶打開。'],
            ]),
            G('否定與代詞', '前面或後面', [
                ['不要忘', 'n’oublie pas', '不要忘'],
                ['聽我', 'écoute-moi', '聽我說'],
                ['不要重複', 'ne le répète pas', '不要重複它'],
                ['去那裡', 'vas-y', '去吧'],
            ], [
                ['N’oubliez pas vos clés.', '請不要忘記鑰匙。'],
                ['Écoute-moi.', '聽我說。'],
                ['Ne le répète pas.', '不要重複這件事。'],
                ['Vas-y.', '去吧。'],
            ]),
            G('être、avoir', '不規則命令', [
                ['你要準時', 'sois à l’heure', '要準時'],
                ['請您準時', 'soyez à l’heure', '請準時'],
                ['有耐心', 'sois patient', '要有耐心'],
                ['要有信心', 'aie confiance', '要有信心'],
            ], [
                ['Sois à l’heure.', '要準時。'],
                ['Soyez les bienvenus.', '歡迎你們。'],
                ['Sois patient.', '要有耐心。'],
                ['Aie confiance.', '要有信心。'],
            ]),
        ],
    ),
    L(
        'depuis', 'A2', 'Depuis', '法文 A2｜depuis、pendant、il y a',
        '從過去一直持續到現在，用現在式加 depuis。已經結束的一段時間，用複合過去加 pendant。多久以前，用 il y a。',
        'depuis、pendant、il y a、pour，附例句、中文、朗讀與 PDF。',
        'depuis 問的是 Depuis quand ? 或 Depuis combien de temps ?\npour 常指計畫中的長度：Je vais rester pour deux jours.',
        [
            G('depuis', '從那時起，現在仍是', [
                ['從二〇二〇', 'depuis 2020', '從 2020 年起'],
                ['六個月', 'depuis six mois', '至今六個月'],
                ['問', 'depuis quand', '從什麼時候'],
                ['問多久', 'depuis combien de temps', '至今多久'],
            ], [
                ['J’habite ici depuis 2020.', '我從 2020 年起住在這裡。'],
                ['J’apprends le français depuis six mois.', '我學法文至今六個月。'],
                ['Depuis quand est-ce que tu habites ici ?', '你從什麼時候住在這裡？'],
                ['Depuis combien de temps est-ce que vous travaillez ici ?', '您在這裡工作多久了？'],
            ]),
            G('pendant', '一段已經結束的時間', [
                ['八小時', 'pendant huit heures', '八個小時'],
                ['兩年', 'pendant deux ans', '兩年'],
                ['整個夏天', 'pendant tout l’été', '整個夏天'],
                ['問', 'pendant combien de temps', '多久'],
            ], [
                ['J’ai dormi pendant huit heures.', '我睡了八個小時。'],
                ['Elle a vécu à Paris pendant deux ans.', '她在巴黎住了兩年。'],
                ['Nous avons voyagé pendant tout l’été.', '我們整個夏天都在旅行。'],
                ['Pendant combien de temps est-ce que tu as étudié ?', '你當時學了多久？'],
            ]),
            G('il y a、pour', '以前、計畫的長度', [
                ['一小時前', 'il y a une heure', '一小時前'],
                ['三天前', 'il y a trois jours', '三天前'],
                ['待兩天', 'pour deux jours', '待兩天'],
                ['問以前', 'il y a combien de temps', '多久以前'],
            ], [
                ['Il est parti il y a une heure.', '他一小時前離開了。'],
                ['Marie est partie il y a trois jours.', 'Marie 三天前離開了。'],
                ['Je vais rester pour deux jours.', '我打算待兩天。'],
                ['Il y a combien de temps est-ce que tu es arrivé ?', '你多久以前到的？'],
            ]),
        ],
    ),
    L(
        'parce-que', 'A2', 'Parce que', '法文 A2｜原因',
        'parce que 後面接一個完整的句子，說明原因。pour 加原形，說明目的。donc 把結果放在後面。',
        'parce que、pour、donc，附例句、中文、朗讀與 PDF。',
        'parce que 是原因。pour + 原形是目的，不是原因。\ncar 和 parce que 接近，car 比較常出現在書面。',
        [
            G('parce que', '因為', [
                ['因為累', 'parce que je suis fatigué', '因為我累了'],
                ['因為下雨', 'parce qu’il pleut', '因為下雨'],
                ['因為有課', 'parce que j’ai un cours', '因為我有課'],
                ['問', 'pourquoi', '為什麼'],
            ], [
                ['Je reste à la maison parce que je suis fatigué.', '我留在家裡，因為我累了。'],
                ['Nous ne sortons pas parce qu’il pleut.', '我們不出去，因為下雨。'],
                ['Elle étudie parce qu’elle a un examen.', '她在讀書，因為她有考試。'],
                ['Pourquoi est-ce que tu apprends le français ?', '你為什麼學法文？'],
            ]),
            G('pour', '為了', [
                ['為了工作', 'pour travailler', '為了工作'],
                ['為了懂', 'pour comprendre', '為了弄懂'],
                ['為了買', 'pour acheter', '為了買'],
                ['書面', 'car', '因為'],
            ], [
                ['Il apprend le français pour travailler au Canada.', '他學法文是為了在加拿大工作。'],
                ['Je lis ce texte pour comprendre la question.', '我讀這段文字是為了弄懂問題。'],
                ['Elle économise pour acheter un vélo.', '她在存錢，為了買一輛腳踏車。'],
                ['Je reste, car je suis fatigué.', '我留下，因為我累了。'],
            ]),
            G('donc', '所以', [
                ['所以留下', 'donc je reste', '所以我留下'],
                ['所以搭車', 'donc je prends le bus', '所以我搭公車'],
                ['所以問', 'donc je demande', '所以我問'],
                ['結果', 'alors', '那麼'],
            ], [
                ['Je suis malade, donc je reste à la maison.', '我生病了，所以留在家裡。'],
                ['Il est tard, donc nous prenons un taxi.', '時間晚了，所以我們搭計程車。'],
                ['Je ne comprends pas, donc je pose une question.', '我不懂，所以我問一個問題。'],
                ['Tu es fatigué ? Alors repose-toi.', '你累了嗎？那就休息吧。'],
            ]),
        ],
    ),
]
