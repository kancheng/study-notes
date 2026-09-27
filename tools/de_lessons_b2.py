"""German B2 grammar aligned with Goethe-Zertifikat B2 (GER B2)."""
from lesson_util import G, L

LESSONS = [
    L(
        'konjunktiv-i', 'B2', 'Konjunktiv I', '德文 B2｜第一虛擬式',
        '新聞和報告轉述別人的話時，用 Konjunktiv I。如果這個形式和直陳式一樣，就改用 Konjunktiv II。',
        'sei、habe、komme，以及複數必須改成 hätte、wäre 的情況，附例句、中文、朗讀與 PDF。',
        'er ist 寫成 er sei，er hat 寫成 er habe，er kommt 寫成 er komme。\nwir haben 的第一虛擬和直陳式相同，所以寫成 wir hätten。口語轉述仍多用 dass 加直陳式，那是 B1 的說法。',
        [
            G('單數', '和直陳式不同，可以直接用', [
                ['是', 'er sei', '他是（轉述）'],
                ['有', 'er habe', '他有（轉述）'],
                ['來', 'er komme', '他來（轉述）'],
                ['能', 'er könne', '他能（轉述）'],
            ], [
                ['Er sagt, er sei krank.', '他說他生病了。'],
                ['Sie erklärte, sie habe die E-Mail nicht bekommen.', '她解釋說她沒有收到電子郵件。'],
                ['Er meinte, er könne morgen kommen.', '他表示他明天能來。'],
                ['Es hieß, der Zug habe Verspätung.', '據稱火車誤點了。'],
            ]),
            G('必須改用第二虛擬', '形式和直陳式一樣時', [
                ['他們有', 'sie hätten', '他們有（轉述）'],
                ['他們是', 'sie seien', '他們是（第一虛擬仍不同）'],
                ['我們能', 'wir könnten', '我們能（轉述）'],
                ['原則', '相同就改用 hätte、wäre、würde', '避免和直陳式分不出來'],
            ], [
                ['Die Nachbarn sagen, sie hätten nichts gehört.', '鄰居們說他們什麼都沒聽見。'],
                ['Die Preise seien gestiegen, schreibt der Artikel.', '文章寫道，物價上漲了。'],
                ['Sie sagen, sie könnten nicht bleiben.', '他們說他們不能留下。'],
                ['Der Bericht sagt, die Lage sei stabil.', '報告說情況穩定。'],
            ]),
            G('和 B1 的差別', '書面用虛擬，口語用 dass', [
                ['口語', 'Er sagt, dass er krank ist.', '他說他生病了。'],
                ['書面', 'Er sagt, er sei krank.', '他說他生病了。'],
                ['沒有 dass', '虛擬式常省掉 dass', '人稱緊接在動詞後面'],
                ['仍是轉述', '不代表說話者認為它為真', '只表示這是別人的話'],
            ], [
                ['Er sagt, dass er keine Zeit hat.', '他說他沒有時間。'],
                ['Er sagt, er habe keine Zeit.', '他說他沒有時間。'],
                ['Die Firma teilte mit, der Preis sei gestiegen.', '公司表示價格上漲了。'],
                ['Sie behauptet, sie habe davon nichts gewusst.', '她聲稱她對此一無所知。'],
            ]),
        ],
    ),
    L(
        'konjunktiv-ii-perfekt', 'B2', 'Konjunktiv II Perfekt', '德文 B2｜與過去相反',
        '和過去的事實相反時，從句和主句都用 hätte 或 wäre 加過去分詞。',
        'hätte gemacht、wäre gegangen，以及省掉 wenn 的倒裝，附例句、中文、朗讀與 PDF。',
        '移動和 sein、bleiben 用 wäre。其他動詞用 hätte。\n省掉 wenn 時，hätte 或 wäre 放在句首：Hätte ich das gewusst, wäre ich geblieben。',
        [
            G('hätte + 分詞', '大多數動詞', [
                ['知道', 'hätte gewusst', '當時如果知道'],
                ['問', 'hättest du gefragt', '你當時如果問了'],
                ['做', 'hätte gemacht', '當時會做'],
                ['幫忙', 'hätte geholfen', '當時會幫忙'],
            ], [
                ['Wenn ich das gewusst hätte, wäre ich geblieben.', '如果我當時知道，我就會留下。'],
                ['Wenn du mich gefragt hättest, hätte ich dir geholfen.', '如果你當時問我，我就會幫你。'],
                ['Ich hätte das anders gemacht.', '我當時會用別的做法。'],
                ['An deiner Stelle hätte ich nachgefragt.', '如果我是你，我當時會再問一次。'],
            ]),
            G('wäre + 分詞', '移動、sein、bleiben', [
                ['去', 'wäre gegangen', '當時會去'],
                ['來', 'wäre mitgekommen', '當時會一起去'],
                ['留下', 'wäre geblieben', '當時會留下'],
                ['是', 'wäre gewesen', '當時會是'],
            ], [
                ['Wenn ich früher gegangen wäre, hätte ich den Zug erreicht.', '如果我當時早點走，就會趕上火車。'],
                ['Ich wäre gern mitgekommen.', '我當時很想一起去。'],
                ['Sie wäre zu Hause geblieben.', '她當時會留在家裡。'],
                ['Das wäre ein Fehler gewesen.', '那會是一個錯誤。'],
            ]),
            G('沒有 wenn', '助動詞放句首', [
                ['如果知道', 'Hätte ich das gewusst, ...', '我當時如果知道'],
                ['如果早走', 'Wäre ich früher gegangen, ...', '我當時如果早點走'],
                ['主句', 'wäre ich geblieben', '我就會留下'],
                ['逗號', '前後兩句都是虛擬', '中間用逗號'],
            ], [
                ['Hätte ich das gewusst, wäre ich zu Hause geblieben.', '我當時如果知道，就會留在家裡。'],
                ['Wäre ich früher gegangen, hätte ich den Zug noch erreicht.', '我當時如果早點走，還會趕上火車。'],
                ['Hättest du angerufen, wäre ich gekommen.', '你當時如果打了電話，我就會來。'],
                ['Wären wir pünktlich gewesen, hätten wir Plätze bekommen.', '我們當時如果準時，就會有位子。'],
            ]),
        ],
    ),
    L(
        'zustandspassiv', 'B2', 'Passiv und Zustand', '德文 B2｜情態被動與狀態被動',
        'werden 加過去分詞是一個動作正在被做。sein 加過去分詞是做完之後的狀態。情態動詞的被動把 werden 放在句尾。',
        '過程、狀態、kann gemacht werden，以及 von 和 durch，附例句、中文、朗讀與 PDF。',
        'Die Tür wird geschlossen：有人正在關門。Die Tür ist geschlossen：門是關著的。\n人用 von，原因用 durch：von der Autorin，durch den Sturm。',
        [
            G('動作或狀態', 'werden 對 sein', [
                ['動作', 'Die Tür wird geschlossen.', '有人正在關門。'],
                ['狀態', 'Die Tür ist geschlossen.', '門是關著的。'],
                ['動作', 'Das Fenster wird geöffnet.', '有人正在開窗。'],
                ['狀態', 'Das Fenster ist geöffnet.', '窗戶是開著的。'],
            ], [
                ['Die Tür wird gerade geschlossen.', '門正在被關上。'],
                ['Die Tür ist geschlossen.', '門是關著的。'],
                ['Das Geschäft wird um acht geöffnet.', '店八點開門。'],
                ['Das Geschäft ist heute geöffnet.', '店今天開著。'],
            ]),
            G('情態被動', '情態動詞 + 過去分詞 + werden', [
                ['可以', 'kann ausgefüllt werden', '可以被填寫'],
                ['必須', 'muss abgegeben werden', '必須被交出去'],
                ['應該', 'sollte geprüft werden', '應該被檢查'],
                ['句尾', 'werden 用原形', '放在最後'],
            ], [
                ['Das Formular kann online ausgefüllt werden.', '表格可以在線上填寫。'],
                ['Die Aufgabe muss bis Freitag abgegeben werden.', '作業必須在星期五前交。'],
                ['Der Text sollte noch einmal gelesen werden.', '課文應該再讀一次。'],
                ['Die Frage kann nicht so schnell beantwortet werden.', '這個問題沒辦法那麼快回答。'],
            ]),
            G('von 與 durch', '人，或是原因', [
                ['人', 'von einer Autorin', '由一位作者'],
                ['原因', 'durch den Sturm', '由於暴風雨'],
                ['過程', 'wurde geschrieben', '當時被寫下'],
                ['狀態', 'ist zerstört', '處於被毀的狀態'],
            ], [
                ['Der Roman wurde von einer jungen Autorin geschrieben.', '這本小說是一位年輕作者寫的。'],
                ['Die Straße wurde durch den Sturm blockiert.', '道路因暴風雨受阻。'],
                ['Viele Häuser wurden durch das Erdbeben zerstört.', '許多房子因地震被毀。'],
                ['Die Fenster sind seit dem Sturm geschlossen.', '暴風雨之後窗戶一直關著。'],
            ]),
        ],
    ),
    L(
        'relativ-praep', 'B2', 'Relativpräposition', '德文 B2｜介系詞關係子句',
        '介系詞放在關係代名詞前面，格由那個介系詞決定。指整件事或不特定的事物時，用 wo(r)-。',
        'in der、mit dem、worüber、wofür，附例句、中文、朗讀與 PDF。',
        '人用介系詞加關係代名詞：der Kollege, mit dem ich arbeite。\n整件事用 worüber、wofür、womit。元音開頭的介系詞加 r：worüber，不是 woüber。',
        [
            G('人', '介系詞 + 關係代名詞', [
                ['住在', 'die Wohnung, in der ...', '我住的那間公寓'],
                ['一起工作', 'der Kollege, mit dem ...', '和我一起工作的同事'],
                ['等待', 'die Frau, auf die ...', '我等待的那個女人'],
                ['複數', 'die Freunde, mit denen ...', '和我一起的那些朋友'],
            ], [
                ['Die Wohnung, in der ich wohne, ist klein.', '我住的那間公寓很小。'],
                ['Der Kollege, mit dem ich arbeite, ist geduldig.', '和我一起工作的同事很有耐心。'],
                ['Die Frau, auf die ich warte, kommt gleich.', '我等待的那個女人馬上到。'],
                ['Die Freunde, mit denen ich lerne, wohnen in Taipei.', '和我一起學習的朋友住在台北。'],
            ]),
            G('事物', '介系詞可以留在關係代名詞前', [
                ['談論', 'das Thema, über das ...', '我們談論的題目'],
                ['用', 'der Stift, mit dem ...', '我用來寫的筆'],
                ['在……裡', 'die Stadt, in der ...', '我出生的城市'],
                ['格', '由介系詞決定', 'über + 受格，mit + 與格'],
            ], [
                ['Das Thema, über das wir sprechen, ist schwierig.', '我們談論的題目很難。'],
                ['Der Stift, mit dem ich schreibe, ist neu.', '我用來寫字的筆是新的。'],
                ['Taipei ist die Stadt, in der ich geboren bin.', '台北是我出生的城市。'],
                ['Das Problem, an das ich denke, ist die Zeit.', '我想到的問題是時間。'],
            ]),
            G('worüber', '整件事，或不特定的物', [
                ['關於', 'worüber', '關於那件事'],
                ['為了', 'wofür', '為了什麼'],
                ['用', 'womit', '用什麼'],
                ['想到', 'woran', '想到什麼'],
            ], [
                ['Das ist etwas, worüber ich nachdenken muss.', '那是我必須想想的事。'],
                ['Weißt du, wofür dieses Wort steht?', '你知道這個詞代表什麼嗎？'],
                ['Sie erklärt, womit man anfangen soll.', '她說明應該從什麼開始。'],
                ['Das, woran er denkt, sagt er nicht.', '他在想什麼，他沒說。'],
            ]),
        ],
    ),
    L(
        'nominalisierung', 'B2', 'Nominalisierung', '德文 B2｜名詞化',
        '動詞可以變成中性名詞：das Lernen。許多動詞另有一個對應的陰性或陽性名詞，介系詞往往保留。',
        'das Lesen、beim Schreiben，以及 Entscheidung、Vorbereitung、Ankunft，附例句、中文、朗讀與 PDF。',
        '不定詞名詞化是中性，第一個字母大寫：das Lernen。介系詞 an 加 dem 寫成 beim。\n對應名詞要單獨記性別：die Entscheidung，die Vorbereitung，die Ankunft。',
        [
            G('不定詞當名詞', '中性，das', [
                ['讀', 'das Lesen', '閱讀'],
                ['寫', 'das Schreiben', '書寫'],
                ['游泳', 'das Schwimmen', '游泳'],
                ['學習時', 'beim Lernen', '在學習的時候'],
            ], [
                ['Das Lesen fällt mir leicht.', '閱讀對我來說不難。'],
                ['Beim Schreiben mache ich noch Fehler.', '書寫時我還是會出錯。'],
                ['Das Schwimmen macht ihm Spaß.', '他覺得游泳很有趣。'],
                ['Beim Lernen höre ich keine Musik.', '學習時我不聽音樂。'],
            ]),
            G('對應名詞', '性別要一起記', [
                ['決定', 'die Entscheidung', '決定'],
                ['準備', 'die Vorbereitung auf', '對……的準備'],
                ['到達', 'die Ankunft', '到達'],
                ['邀請', 'die Einladung', '邀請'],
            ], [
                ['Seine Entscheidung war richtig.', '他的決定是對的。'],
                ['Die Vorbereitung auf die Prüfung dauert lange.', '準備考試要花很久。'],
                ['Nach der Ankunft rief sie mich an.', '到達之後她打電話給我。'],
                ['Ich habe die Einladung noch nicht bekommen.', '我還沒收到邀請。'],
            ]),
            G('句子怎麼改', '動詞句和名詞片語', [
                ['動詞', 'Ich bereite mich vor.', '我在準備。'],
                ['名詞', 'die Vorbereitung', '準備'],
                ['動詞', 'Sie entscheidet schnell.', '她很快做決定。'],
                ['名詞', 'eine schnelle Entscheidung', '一個迅速的決定'],
            ], [
                ['Ich bereite mich auf den Test vor.', '我在準備考試。'],
                ['Die Vorbereitung auf den Test ist anstrengend.', '準備考試很累。'],
                ['Sie entscheidet sich schnell.', '她很快就做決定。'],
                ['Eine schnelle Entscheidung ist nicht immer gut.', '迅速的決定不一定好。'],
            ]),
        ],
    ),
    L(
        'partizip', 'B2', 'Partizip', '德文 B2｜分詞當形容詞',
        'Partizip I 表示主動、同時發生。Partizip II 表示被動、已經完成。分詞放在名詞前面，詞尾和形容詞一樣。',
        'wartend、geschlossen，以及帶時間或介系詞的擴展分詞，附例句、中文、朗讀與 PDF。',
        'der wartende Gast：正在等的客人。die geschlossene Tür：已經關上的門。\n擴展時，整段都放在冠詞和名詞中間：das gestern gekaufte Buch。',
        [
            G('Partizip I', '正在做的', [
                ['等待', 'der wartende Gast', '正在等的客人'],
                ['笑', 'ein lachendes Kind', '一個正在笑的孩子'],
                ['讀', 'die lesenden Studenten', '正在讀的學生們'],
                ['詞尾', '像形容詞', 'der -e，ein -es，複數 -en'],
            ], [
                ['Der wartende Gast wird ungeduldig.', '正在等的客人變得不耐煩。'],
                ['Ein lachendes Kind kam herein.', '一個笑著的孩子走了進來。'],
                ['Die lesenden Studenten sind leise.', '正在讀書的學生們很安靜。'],
                ['Ich sehe einen schlafenden Hund.', '我看見一隻在睡覺的狗。'],
            ]),
            G('Partizip II', '已經完成的', [
                ['關上', 'die geschlossene Tür', '關上的門'],
                ['寫好', 'der geschriebene Text', '寫好的課文'],
                ['打開', 'ein geöffnetes Fenster', '一扇開著的窗'],
                ['詞尾', '像形容詞', '不是句尾的過去分詞'],
            ], [
                ['Die geschlossene Tür ist alt.', '那扇關上的門很舊。'],
                ['Der geschriebene Text liegt auf dem Tisch.', '寫好的課文放在桌上。'],
                ['Durch ein geöffnetes Fenster kommt Luft herein.', '空氣從一扇開著的窗戶進來。'],
                ['Die korrigierten Aufgaben sind hier.', '改好的作業在這裡。'],
            ]),
            G('擴展', '冠詞和名詞中間可以放一段', [
                ['昨天買的', 'das gestern gekaufte Buch', '昨天買的書'],
                ['坐在窗邊的', 'der am Fenster sitzende Mann', '坐在窗邊的男人'],
                ['我們討論過的', 'die von uns besprochene Frage', '我們討論過的問題'],
                ['改回子句', 'das Buch, das ich gestern gekauft habe', '我昨天買的書'],
            ], [
                ['Das gestern gekaufte Buch liegt hier.', '昨天買的書放在這裡。'],
                ['Der am Fenster sitzende Mann liest Zeitung.', '坐在窗邊的男人在讀報。'],
                ['Die von uns besprochene Frage ist wichtig.', '我們討論過的問題很重要。'],
                ['Das Buch, das ich gestern gekauft habe, ist teuer.', '我昨天買的那本書很貴。'],
            ]),
        ],
    ),
    L(
        'je-desto', 'B2', 'Je und Sodass', '德文 B2｜je ... desto 與 sodass',
        'je 從句的動詞在句尾，desto 後面的動詞在第二位。sodass 表示結果，動詞在句尾。indem 表示做法。',
        '越……就越……、因而、藉由，以及 nicht nur ... sondern auch，附例句、中文、朗讀與 PDF。',
        'Je mehr ich lese, desto besser verstehe ich。desto 後面不要再把動詞送到句尾。\nindem 回答怎麼做。sodass 回答因此發生了什麼。',
        [
            G('je ... desto', '兩邊都是比較級', [
                ['越多', 'je mehr ... desto besser', '越多就越好'],
                ['越久', 'je länger ... desto teurer', '越久就越貴'],
                ['越早', 'je früher ... desto leichter', '越早就越容易'],
                ['詞序', 'je 句尾，desto 第二位', '兩個位置不同'],
            ], [
                ['Je mehr ich lese, desto besser verstehe ich den Text.', '我讀得越多，就越懂這篇課文。'],
                ['Je länger wir warten, desto teurer wird das Ticket.', '我們等得越久，票就越貴。'],
                ['Je früher du anfängst, desto leichter wird es.', '你開始得越早，就越容易。'],
                ['Je öfter man spricht, desto sicherer wird man.', '說得越頻繁，就越有把握。'],
            ]),
            G('indem 與 sodass', '做法，以及結果', [
                ['藉由', 'indem man laut liest', '藉由大聲讀'],
                ['因而', 'sodass ich nichts verstand', '因而我什麼都聽不懂'],
                ['動詞', '兩邊都在從句句尾', 'liest、verstand'],
                ['逗號', '主句之後', 'indem 和 sodass 前都要逗號'],
            ], [
                ['Man verbessert die Aussprache, indem man laut liest.', '藉由大聲讀，可以改善發音。'],
                ['Es war laut, sodass ich nichts verstand.', '聲音很大，因而我什麼都聽不懂。'],
                ['Sie erklärt die Regel, indem sie ein Beispiel gibt.', '她舉一個例子來說明規則。'],
                ['Der Text ist lang, sodass wir ihn teilen.', '課文很長，所以我們把它分開。'],
            ]),
            G('nicht nur ... sondern auch', '兩件事並列', [
                ['兩者', 'nicht nur ... sondern auch', '不僅……而且……'],
                ['名詞', 'nicht nur Grammatik, sondern auch Wortschatz', '不僅文法，還有詞彙'],
                ['動詞', '兩邊形式相同', '學，也說'],
                ['不要只留一邊', 'sondern auch 不能省', '也'],
            ], [
                ['Ich lerne nicht nur Grammatik, sondern auch Aussprache.', '我學的不僅是文法，還有發音。'],
                ['Sie spricht nicht nur Deutsch, sondern auch Englisch.', '她不僅說德文，也說英文。'],
                ['Er hat nicht nur angerufen, sondern auch geschrieben.', '他不僅打了電話，還寫了信。'],
                ['Das ist nicht nur schwer, sondern auch interessant.', '那不僅難，而且有趣。'],
            ]),
        ],
    ),
    L(
        'subjektiv', 'B2', 'Subjektiv', '德文 B2｜情態動詞的推測',
        '同一組情態動詞還可以表示消息從哪裡來：傳聞、本人聲稱、有可能、幾乎可以確定。',
        'sollen、wollen、dürfte、müssen 的推測用法，附例句、中文、朗讀與 PDF。',
        'sollen 是聽說。wollen 是本人聲稱，說話者未必相信。dürfte 是大概。müssen 是根據跡象幾乎可以確定。\n談過去時，後面用分詞加 haben 或 sein：Er muss schon gegangen sein。',
        [
            G('sollen 與 wollen', '聽說，或本人這麼說', [
                ['傳聞', 'Er soll sehr streng sein.', '聽說他很嚴格。'],
                ['本人聲稱', 'Sie will die Chefin kennen.', '她聲稱認識主管。'],
                ['過去', 'Sie will die Prüfung bestanden haben.', '她聲稱通過了考試。'],
                ['差別', 'sollen 不是她自己說的', 'wollen 是她自己說的'],
            ], [
                ['Er soll sehr streng sein.', '聽說他很嚴格。'],
                ['Der Kurs soll interessant sein.', '聽說這堂課很有趣。'],
                ['Sie will die Chefin persönlich kennen.', '她聲稱親自認識主管。'],
                ['Er will davon nichts gewusst haben.', '他聲稱對此一無所知。'],
            ]),
            G('dürfte 與 können', '大概，或有可能', [
                ['大概', 'Das dürfte stimmen.', '那大概是對的。'],
                ['有可能', 'Das kann stimmen.', '那有可能是對的。'],
                ['預期', 'Der Zug müsste gleich kommen.', '火車應該快到了。'],
                ['不確定', 'kann 比 dürfte 更沒把握', '只是有可能'],
            ], [
                ['Das dürfte ein Fehler sein.', '那大概是一個錯誤。'],
                ['Das kann stimmen, aber ich bin nicht sicher.', '那有可能是對的，但我沒有把握。'],
                ['Der Zug müsste gleich kommen.', '火車應該快到了。'],
                ['Sie dürfte die Nachricht schon gelesen haben.', '她大概已經看過那個消息了。'],
            ]),
            G('müssen', '從跡象推出來', [
                ['幾乎確定', 'Er muss zu Hause sein.', '他一定在家。'],
                ['過去', 'Er muss schon gegangen sein.', '他一定已經走了。'],
                ['移動', 'sein 放句尾', 'gegangen sein'],
                ['不是命令', '這裡不是必須', '是推測'],
            ], [
                ['Das Licht ist an. Er muss zu Hause sein.', '燈亮著。他一定在家。'],
                ['Die Tasche ist weg. Sie muss schon gegangen sein.', '袋子不見了。她一定已經走了。'],
                ['Er muss den Zug verpasst haben.', '他一定沒趕上火車。'],
                ['Das muss ein Missverständnis sein.', '那一定是個誤會。'],
            ]),
        ],
    ),
]
