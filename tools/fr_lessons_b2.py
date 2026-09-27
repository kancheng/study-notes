"""French B2 grammar aligned with DELF B2 (CECRL)."""
from lesson_util import G, L

LESSONS = [
    L(
        'subjonctif-b2', 'B2', 'Subjonctif passé', '法文 B2｜虛擬式的其他用法',
        'bien que、afin que、avant que 接現在虛擬式。如果 que 後面的事發生得更早，用過去虛擬式：助動詞的虛擬式加過去分詞。',
        'bien que、afin que、avant que，以及過去虛擬式，附例句、中文、朗讀與 PDF。',
        'après que 接直陳式，不接虛擬式。更早的事用 après que + 複合過去或愈過去。\navant que 才接虛擬式。過去虛擬式：que j’aie fait、qu’il soit parti、qu’elle soit allée。',
        [
            G('bien que', '雖然，接虛擬式', [
                ['雖然冷', 'bien qu’il fasse froid', '雖然冷'],
                ['雖然年輕', 'bien qu’elle soit jeune', '雖然她年輕'],
                ['雖然讀了', 'bien qu’elle ait étudié', '雖然她讀了'],
                ['雖然走了', 'bien qu’ils soient partis', '雖然他們走了'],
            ], [
                ['Bien qu’il fasse froid, nous sortons.', '雖然冷，我們還是出門。'],
                ['Bien qu’elle soit jeune, elle dirige l’équipe.', '雖然她年輕，她領導這個團隊。'],
                ['Bien qu’elle ait étudié, elle a échoué.', '雖然她讀了，她還是沒考上。'],
                ['Bien qu’ils soient partis tôt, ils sont arrivés en retard.', '雖然他們很早出發，還是遲到了。'],
            ]),
            G('afin que、avant que', '為了、在…之前', [
                ['為了你懂', 'afin que tu comprennes', '為了讓你懂'],
                ['為了大家聽見', 'pour que tout le monde entende', '為了讓大家都聽見'],
                ['在下雨前', 'avant qu’il pleuve', '在下雨之前'],
                ['在你走之前', 'avant que tu partes', '在你走之前'],
            ], [
                ['Je parle lentement afin que tu comprennes.', '我說得慢，是為了讓你聽懂。'],
                ['Répétez, pour que tout le monde entende.', '請再說一次，好讓大家都聽見。'],
                ['Rentrons avant qu’il pleuve.', '我們在下雨前回去吧。'],
                ['Dis-le-moi avant que tu partes.', '你走之前告訴我。'],
            ]),
            G('過去虛擬', 'que j’aie、qu’il soit + 分詞', [
                ['做過', 'que j’aie fait', '我做過'],
                ['去過', 'qu’elle soit allée', '她去過'],
                ['離開了', 'qu’ils soient partis', '他們已經離開'],
                ['可能走了', 'il est possible qu’ils soient partis', '他們可能已經走了'],
            ], [
                ['Je suis content que tu aies fini.', '我很高興你做完了。'],
                ['Il est possible qu’elle soit déjà partie.', '她可能已經走了。'],
                ['Je ne pense pas qu’ils aient compris.', '我不認為他們懂了。'],
                ['Bien qu’il ait plu, le match a eu lieu.', '雖然下過雨，比賽還是舉行了。'],
            ]),
        ],
    ),
    L(
        'plus-que-parfait', 'B2', 'Plus-que-parfait', '法文 B2｜愈過去',
        '愈過去表示在過去另一件事之前就已經完成。用未完成過去的 avoir 或 être，加上過去分詞。用 être 時，分詞仍要配合主詞。',
        'j’avais fait、elle était partie，附例句、中文、朗讀與 PDF。',
        '時間軸上有兩件過去的事時，更早的那件用愈過去。\nêtre 的配合和複合過去相同：elle était partie、ils étaient arrivés。',
        [
            G('avoir', '更早已經做完', [
                ['已經吃了', 'j’avais déjà mangé', '我已經吃過了'],
                ['已經訂了', 'nous avions réservé', '我們已經訂了'],
                ['已經說了', 'elle avait dit', '她已經說過'],
                ['還沒看', 'je n’avais pas vu', '我還沒看過'],
            ], [
                ['J’avais déjà mangé quand il a appelé.', '他打電話來的時候，我已經吃過了。'],
                ['Nous avions réservé une table.', '我們已經訂了一張桌子。'],
                ['Elle avait dit la vérité.', '她已經說過實話。'],
                ['Je n’avais pas vu ce message.', '我當時還沒看到這則訊息。'],
            ]),
            G('être', '更早的移動，分詞要配合', [
                ['已經離開', 'elle était partie', '她已經離開'],
                ['已經到了', 'ils étaient arrivés', '他們已經到了'],
                ['已經回去', 'nous étions rentrés', '我們已經回去'],
                ['還沒出門', 'je n’étais pas sorti', '我還沒出門'],
            ], [
                ['Elle était partie avant notre arrivée.', '在我們到達之前，她已經離開了。'],
                ['Quand nous sommes entrés, ils étaient déjà arrivés.', '我們進去的時候，他們已經到了。'],
                ['Nous étions rentrés avant minuit.', '我們在午夜前已經回到家。'],
                ['Je n’étais pas encore sorti quand tu as sonné.', '你按鈴的時候，我還沒出門。'],
            ]),
            G('先後', '先…然後…', [
                ['先讀完', 'après avoir lu', '讀完之後'],
                ['先到', 'quand je suis arrivé, le train était parti', '我到時火車已走'],
                ['已經結束', 'le cours avait commencé', '課已經開始了'],
                ['已經決定', 'nous avions décidé', '我們已經決定'],
            ], [
                ['Quand je suis arrivé, le train était déjà parti.', '我到的時候，火車已經走了。'],
                ['Le cours avait déjà commencé.', '課已經開始了。'],
                ['Nous avions décidé de rester, puis il a plu.', '我們已經決定留下，然後下雨了。'],
                ['Elle a compris parce qu’elle avait beaucoup lu.', '她懂了，因為她先前讀了很多。'],
            ]),
        ],
    ),
    L(
        'conditionnel-passe', 'B2', 'Conditionnel passé', '法文 B2｜過去條件式',
        '過去條件式表示過去沒有發生的假設，或事後才看出的「本來應該」。si 後面用愈過去，主句用過去條件式。',
        'j’aurais fait、je serais venu、si j’avais su，附例句、中文、朗讀與 PDF。',
        'avoir 的過去條件是 j’aurais + 分詞。être 是 je serais + 分詞。\nsi 後面仍然不用條件式。tu aurais dû 是「你本來應該」。',
        [
            G('本來會', 'aurais、serais + 分詞', [
                ['本來想', 'j’aurais aimé', '我本來想'],
                ['本來會來', 'elle serait venue', '她本來會來'],
                ['本來會說', 'je t’aurais téléphoné', '我本來會打電話給你'],
                ['本來會留下', 'nous serions restés', '我們本來會留下'],
            ], [
                ['J’aurais aimé venir.', '我本來想來。'],
                ['Elle serait venue si elle avait pu.', '如果她能來，她本來會來。'],
                ['Je t’aurais téléphoné.', '我本來會打電話給你。'],
                ['Nous serions restés plus longtemps.', '我們本來會再待久一點。'],
            ]),
            G('si + 愈過去', '如果當時…', [
                ['如果知道', 'si j’avais su', '如果我當時知道'],
                ['如果有時間', 'si tu avais eu le temps', '如果你當時有時間'],
                ['如果下雨', 's’il avait plu', '如果當時下雨'],
                ['如果是我', 'si j’avais été là', '如果我當時在'],
            ], [
                ['Si j’avais su, je t’aurais téléphoné.', '如果我當時知道，我就會打電話給你。'],
                ['Si tu avais eu le temps, tu aurais fini.', '如果你當時有時間，你就會做完。'],
                ['S’il avait plu, nous serions restés.', '如果當時下雨，我們就會留下。'],
                ['Si j’avais été là, je t’aurais aidé.', '如果我當時在，我就會幫你。'],
            ]),
            G('devoir、pouvoir', '本來應該、本來可以', [
                ['本來應該', 'tu aurais dû', '你本來應該'],
                ['本來可以', 'j’aurais pu', '我本來可以'],
                ['本來不該', 'je n’aurais pas dû', '我本來不該'],
                ['本來願意', 'elle aurait voulu', '她本來願意'],
            ], [
                ['Tu aurais dû me le dire.', '你本來應該告訴我。'],
                ['J’aurais pu t’aider.', '我本來可以幫你。'],
                ['Je n’aurais pas dû partir si tôt.', '我本來不該那麼早走。'],
                ['Elle aurait voulu rester.', '她本來願意留下。'],
            ]),
        ],
    ),
    L(
        'passif', 'B2', 'Voix passive', '法文 B2｜被動',
        '被動把承受動作的人或物放到主詞。用 être 的各種時態，加上過去分詞，分詞配合主詞。動作的做出者用 par。',
        'être + 過去分詞、par、on，附例句、中文、朗讀與 PDF。',
        '時態落在 être 上：est écrit、a été écrit、sera annoncé。\n不需要說出是誰做的時候，也可以用 on：On parle français ici.',
        [
            G('現在與複合', 'est、a été', [
                ['被寫', 'a été écrit', '被寫成'],
                ['被關上', 'a été fermée', '被關上'],
                ['被送出', 'ont été envoyées', '被寄出'],
                ['開著', 'est ouverte', '是開著的'],
            ], [
                ['Ce roman a été écrit en 1990.', '這本小說寫於 1990 年。'],
                ['La porte a été fermée par le gardien.', '門被管理員關上了。'],
                ['Les invitations ont été envoyées hier.', '邀請函昨天寄出了。'],
                ['La fenêtre est ouverte.', '窗戶是開著的。'],
            ]),
            G('將來與必須', 'sera、doit être', [
                ['將被公布', 'seront annoncés', '將被公布'],
                ['必須被簽', 'doit être signé', '必須簽名'],
                ['將被修好', 'sera réparé', '將被修好'],
                ['被邀請', 'ont été invités', '被邀請了'],
            ], [
                ['Les résultats seront annoncés demain.', '結果明天會公布。'],
                ['Ce document doit être signé.', '這份文件必須簽名。'],
                ['L’ascenseur sera réparé ce soir.', '電梯今晚會修好。'],
                ['Nous avons été invités à la réunion.', '我們被邀請參加會議。'],
            ]),
            G('on', '不說出是誰', [
                ['有人說法文', 'on parle français', '這裡說法文'],
                ['有人建', 'on construit', '正在興建'],
                ['有人說', 'on dit que', '據說'],
                ['有人問', 'on m’a demandé', '有人問我'],
            ], [
                ['On parle français dans cette classe.', '這堂課說法文。'],
                ['On construit un pont près de la gare.', '火車站附近正在建一座橋。'],
                ['On dit que le musée est fermé le lundi.', '據說博物館星期一休館。'],
                ['On m’a demandé d’arriver tôt.', '有人要求我早到。'],
            ]),
        ],
    ),
    L(
        'discours', 'B2', 'Discours indirect', '法文 B2｜間接引語',
        '轉述別人現在說的話，動詞往往退一層：現在式變成未完成過去，複合過去變成愈過去，簡單將來變成條件式。命令變成 de 加原形。',
        'il a dit que、elle a demandé si、il m’a dit de，附例句、中文、朗讀與 PDF。',
        '轉述疑問句用 si，不再用 est-ce que。\n時間詞也常改：demain 可改成 le lendemain，aujourd’hui 可改成 ce jour-là。',
        [
            G('陳述', '時態往前退', [
                ['當時累', 'il était fatigué', '他當時累了'],
                ['已經做完', 'elle avait fini', '她已經做完'],
                ['第二天會來', 'il viendrait le lendemain', '他隔天會來'],
                ['不知道', 'il ne savait pas', '他當時不知道'],
            ], [
                ['Il a dit qu’il était fatigué.', '他說他累了。'],
                ['Elle a dit qu’elle avait fini le travail.', '她說她已經把工作做完了。'],
                ['Il a dit qu’il viendrait le lendemain.', '他說他隔天會來。'],
                ['Elle a dit qu’elle ne savait pas.', '她說她不知道。'],
            ]),
            G('疑問', 'si、疑問詞', [
                ['是否來', 'si je venais', '我是否來'],
                ['幾點', 'à quelle heure nous partions', '我們幾點走'],
                ['哪裡', 'où j’habitais', '我住哪裡'],
                ['為什麼', 'pourquoi elle était partie', '她為什麼離開'],
            ], [
                ['Elle m’a demandé si je venais.', '她問我來不來。'],
                ['Il a demandé à quelle heure nous partions.', '他問我們幾點出發。'],
                ['Elle voulait savoir où j’habitais.', '她想知道我住哪裡。'],
                ['Il a demandé pourquoi elle était partie.', '他問她為什麼離開了。'],
            ]),
            G('命令', 'de + 原形', [
                ['叫我等', 'de l’attendre', '等他'],
                ['請我來', 'de venir', '來'],
                ['叫我不要說', 'de ne pas le dire', '不要說'],
                ['請我們坐', 'de nous asseoir', '坐下'],
            ], [
                ['Il m’a dit de l’attendre.', '他叫我等他。'],
                ['Elle m’a demandé de venir plus tôt.', '她請我早一點來。'],
                ['Il m’a dit de ne pas le répéter.', '他叫我不要把這件事說出去。'],
                ['Le professeur nous a dit de nous asseoir.', '老師叫我們坐下。'],
            ]),
        ],
    ),
    L(
        'infinitif', 'B2', 'Infinitif passé', '法文 B2｜過去不定詞與 avant de',
        'après 後面如果還是同一個人，用 avoir 或 être 的不定詞加過去分詞，不用另一個直陳式句子。在做某事之前，用 avant de 加原形。',
        'après avoir、après être、avant de、sans，附例句、中文、朗讀與 PDF。',
        'après être 的分詞配合主詞：Après être arrivée, elle a appelé.\n主詞不同時，不要用這個結構，改成 après que + 直陳式。',
        [
            G('après avoir', '做完之後', [
                ['讀完', 'après avoir lu', '讀完之後'],
                ['吃完', 'après avoir mangé', '吃完之後'],
                ['說了', 'après avoir parlé', '說過之後'],
                ['做完', 'après avoir fini', '做完之後'],
            ], [
                ['Après avoir lu le texte, répondez aux questions.', '讀完文章後，請回答問題。'],
                ['Après avoir mangé, nous sommes sortis.', '吃完之後，我們出門了。'],
                ['Après avoir parlé au médecin, elle était plus calme.', '跟醫生談過之後，她比較冷靜了。'],
                ['Il est parti après avoir fini son travail.', '他做完工作就離開了。'],
            ]),
            G('après être', '到達、離開之後', [
                ['她到了之後', 'après être arrivée', '她到達之後'],
                ['他們離開之後', 'après être partis', '他們離開之後'],
                ['回去之後', 'après être rentrés', '回去之後'],
                ['起床之後', 'après être sorti du lit', '起床之後'],
            ], [
                ['Après être arrivée, elle a appelé.', '她到了之後打了電話。'],
                ['Après être partis, ils ont envoyé un message.', '他們離開之後傳了一則訊息。'],
                ['Nous avons dormi après être rentrés.', '我們回去之後就睡了。'],
                ['Après être sorti, ferme la porte.', '出去之後把門關上。'],
            ]),
            G('avant de、sans', '在…之前、沒有', [
                ['出門前', 'avant de sortir', '出門之前'],
                ['決定前', 'avant de décider', '決定之前'],
                ['沒說', 'sans dire', '沒有說'],
                ['沒看', 'sans avoir lu', '沒讀過就'],
            ], [
                ['Avant de sortir, éteignez la lumière.', '出門前請把燈關掉。'],
                ['Réfléchis avant de décider.', '決定之前先想一想。'],
                ['Il est parti sans dire au revoir.', '他沒說再見就走了。'],
                ['Elle a répondu sans avoir lu toute la question.', '她沒有把整題讀完就回答了。'],
            ]),
        ],
    ),
    L(
        'connecteurs-b2', 'B2', 'Connecteurs écrits', '法文 B2｜書面連接',
        '書面要把轉折和結果說清楚。toutefois 和 néanmoins 是轉折，en revanche 是另一方面，par conséquent 是因此。目的若用 afin que，後面仍是虛擬式。',
        'toutefois、en revanche、par conséquent、néanmoins，附例句、中文、朗讀與 PDF。',
        '這些詞多放在句首，後面加逗號。\nafin que 和 pour que 接虛擬式，afin de 和 pour 接原形，主詞必須相同。',
        [
            G('轉折', 'toutefois、néanmoins', [
                ['然而貴', 'toutefois, il coûte cher', '然而它很貴'],
                ['仍然清楚', 'néanmoins, il reste clair', '仍然清楚'],
                ['另一方面', 'en revanche', '另一方面'],
                ['相反', 'au contraire', '相反'],
            ], [
                ['Le projet est utile. Toutefois, il coûte cher.', '這項計畫有用。然而它花費很高。'],
                ['Le texte est long. Néanmoins, il reste clair.', '文章很長。儘管如此，它仍然清楚。'],
                ['Il aime la ville. En revanche, sa sœur préfère la campagne.', '他喜歡城市。他的姊妹則偏好鄉下。'],
                ['Ce n’est pas plus simple. Au contraire, c’est plus long.', '這並沒有比較簡單。相反，它更花時間。'],
            ]),
            G('結果', 'par conséquent', [
                ['因此成功', 'par conséquent, il a réussi', '因此他成功了'],
                ['因此延後', 'par conséquent, la réunion est reportée', '因此會議延期'],
                ['因此', 'ainsi', '因此'],
                ['所以書面', 'c’est pourquoi', '這就是為什麼'],
            ], [
                ['Il a beaucoup travaillé. Par conséquent, il a réussi.', '他工作得很勤。因此他成功了。'],
                ['Le train est annulé. Par conséquent, la réunion est reportée.', '火車取消了。因此會議延期。'],
                ['Les faits sont clairs. Ainsi, la décision est simple.', '事實很清楚。因此決定很單純。'],
                ['Il pleuvait. C’est pourquoi nous sommes restés.', '當時下雨。這就是我們留下的原因。'],
            ]),
            G('目的', 'afin de、afin que', [
                ['為了懂', 'afin de comprendre', '為了弄懂'],
                ['為了你懂', 'afin que tu comprennes', '為了讓你弄懂'],
                ['為了避免', 'afin de ne pas', '為了不要'],
                ['以便', 'de sorte que', '以便'],
            ], [
                ['Je relis le texte afin de le comprendre.', '我把文章再讀一次，為了把它讀懂。'],
                ['Je parle lentement afin que tout le monde comprenne.', '我說得慢，好讓大家都聽懂。'],
                ['Partez tôt afin de ne pas être en retard.', '早點出發，免得遲到。'],
                ['Expliquez la règle de sorte que les étudiants comprennent.', '請說明這條規則，讓學生聽懂。'],
            ]),
        ],
    ),
    L(
        'mise-en-relief', 'B2', 'Mise en relief', '法文 B2｜強調句',
        'c’est…qui 強調主詞，c’est…que 強調其他成分。ce qui 把一件事當主詞，ce que 把一件事當受詞，ce dont 代替 de。',
        'c’est…qui、c’est…que、ce qui、ce que、ce dont，附例句、中文、朗讀與 PDF。',
        'qui 只在強調主詞時使用。強調地點、時間、受詞都用 que：C’est à Paris que…\nce dont 後面的動詞本來就帶 de：avoir besoin de、parler de。',
        [
            G('c’est…qui / que', '強調是誰、是什麼', [
                ['是 Marie', 'c’est Marie qui', '是 Marie'],
                ['是在巴黎', 'c’est à Paris que', '是在巴黎'],
                ['是這本書', 'c’est ce livre que', '是這本書'],
                ['是昨天', 'c’est hier que', '是昨天'],
            ], [
                ['C’est Marie qui a organisé la fête.', '是 Marie 籌辦了這場聚會。'],
                ['C’est à Paris que nous nous sommes rencontrés.', '我們是在巴黎認識的。'],
                ['C’est ce livre que je cherche.', '我找的就是這本書。'],
                ['C’est hier que la décision a été prise.', '決定是昨天做的。'],
            ]),
            G('ce qui、ce que', '所…的事', [
                ['我所喜歡的', 'ce qui me plaît', '讓我喜歡的'],
                ['我想要的', 'ce que je veux', '我想要的'],
                ['重要的是', 'ce qui est important', '重要的是'],
                ['他說的', 'ce qu’il a dit', '他所說的'],
            ], [
                ['Ce qui me plaît, c’est le calme.', '讓我喜歡的是那份安靜。'],
                ['Ce que je veux, c’est comprendre.', '我想要的是弄懂。'],
                ['Ce qui est important, c’est de pratiquer.', '重要的是練習。'],
                ['Je n’ai pas compris ce qu’il a dit.', '我沒有懂他所說的。'],
            ]),
            G('ce dont', '代替 de', [
                ['我們需要的', 'ce dont nous avons besoin', '我們所需要的'],
                ['我說的', 'ce dont je parle', '我所談的'],
                ['她害怕的', 'ce dont elle a peur', '她所害怕的'],
                ['你記得的', 'ce dont tu te souviens', '你所記得的'],
            ], [
                ['Ce dont nous avons besoin, c’est de temps.', '我們所需要的是時間。'],
                ['Ce dont je parle, c’est de cette règle.', '我所談的是這條規則。'],
                ['Je comprends ce dont elle a peur.', '我理解她所害怕的事。'],
                ['Ce dont tu te souviens est important.', '你所記得的事很重要。'],
            ]),
        ],
    ),
]
