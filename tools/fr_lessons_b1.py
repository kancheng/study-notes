"""French B1 grammar aligned with DELF B1 (CECRL)."""
from lesson_util import G, L

LESSONS = [
    L(
        'passe-imparfait', 'B1', 'Passé et imparfait', '法文 B1｜複合過去與未完成過去',
        '複合過去是當時做完的一件事。未完成過去是背景、習慣，或那時候正在持續的情況。兩件同時發生時，被打斷的那一件用未完成過去。',
        '完成的事件、當時的背景、以前的習慣，附例句、中文、朗讀與 PDF。',
        'quand 後面如果是突發的事，用複合過去；當時正在做的事用未完成過去。\nTous les jours 這類習慣，用未完成過去。Hier 的單一事件，用複合過去。',
        [
            G('背景與事件', '當時…的時候，發生了…', [
                ['下雨時出門', 'il pleuvait quand je suis sorti', '我出門時正下雨'],
                ['到達時正在吃', 'nous dînions quand elle est arrivée', '她到的時候我們正在吃晚飯'],
                ['讀書時電話響', 'il lisait quand le téléphone a sonné', '他正在讀書，電話響了'],
                ['走路時看見', 'je marchais quand je l’ai vu', '我正在走路時看見了他'],
            ], [
                ['Il pleuvait quand je suis sorti.', '我出門的時候正在下雨。'],
                ['Nous dînions quand elle est arrivée.', '她到的時候，我們正在吃晚飯。'],
                ['Il lisait quand le téléphone a sonné.', '他正在讀書，電話響了。'],
                ['Je marchais quand je l’ai vu.', '我正在走路，就看見了他。'],
            ]),
            G('習慣與一次', '以前總是，昨天那一次', [
                ['以前搭', 'je prenais le bus', '我以前搭公車'],
                ['昨天搭', 'j’ai pris un taxi', '我昨天搭了計程車'],
                ['以前住', 'j’habitais ici', '我以前住這裡'],
                ['昨天去', 'j’y suis allé', '我昨天去了那裡'],
            ], [
                ['Autrefois, je prenais le bus. Hier, j’ai pris un taxi.', '以前我搭公車。昨天我搭了計程車。'],
                ['Quand j’étais étudiant, j’habitais ici.', '我當學生的時候住在這裡。'],
                ['Le dimanche, nous allions au marché.', '以前我們星期天去市場。'],
                ['Dimanche dernier, nous sommes allés au marché.', '上星期天我們去了市場。'],
            ]),
            G('狀態', '當時一直是那樣', [
                ['當時年輕', 'elle était jeune', '她當時年輕'],
                ['當時有', 'il avait un vélo', '他當時有腳踏車'],
                ['當時冷', 'il faisait froid', '當時很冷'],
                ['當時是', 'c’était calme', '當時很安靜'],
            ], [
                ['À cette époque, elle était très jeune.', '那時候她很年輕。'],
                ['Il avait un vélo, mais il l’a vendu.', '他當時有一輛腳踏車，但他把它賣了。'],
                ['Il faisait froid, alors nous sommes rentrés.', '當時很冷，所以我們回家了。'],
                ['C’était calme quand nous sommes arrivés.', '我們到的時候，那裡很安靜。'],
            ]),
        ],
    ),
    L(
        'conditionnel', 'B1', 'Conditionnel', '法文 B1｜條件式',
        '現在條件式用來禮貌地提出要求，也用來假設現在並非如此的情況。si 後面用未完成過去，主句用條件式。si 後面不用條件式。',
        'je voudrais、si + 未完成過去，附例句、中文、朗讀與 PDF。',
        '條件式詞尾和未完成過去一樣：-ais、-ais、-ait、-ions、-iez、-aient，但詞幹用簡單將來的詞幹。\nêtre：je serais。avoir：j’aurais。aller：j’irais。faire：je ferais。',
        [
            G('禮貌', '想要、可否', [
                ['我想要', 'je voudrais', '我想要'],
                ['可否', 'pourriez-vous', '您可否'],
                ['我希望', 'j’aimerais', '我希望'],
                ['應該', 'tu devrais', '你應該'],
            ], [
                ['Je voudrais un café, s’il vous plaît.', '請給我一杯咖啡。'],
                ['Pourriez-vous répéter ?', '您可以再說一次嗎？'],
                ['J’aimerais visiter Lyon.', '我希望去里昂看看。'],
                ['Tu devrais te reposer.', '你應該休息。'],
            ]),
            G('si + 未完成過去', '如果現在不是這樣', [
                ['有時間', 'si j’avais le temps', '如果我有時間'],
                ['有錢', 'si nous avions de l’argent', '如果我們有錢'],
                ['是你', 'si j’étais toi', '如果我是你'],
                ['知道', 'si elle savait', '如果她知道'],
            ], [
                ['Si j’avais le temps, je voyagerais.', '如果我有時間，我就會去旅行。'],
                ['Si nous avions de l’argent, nous achèterions une maison.', '如果我們有錢，我們會買一間房子。'],
                ['Si j’étais toi, je parlerais au professeur.', '如果我是你，我會去跟老師說。'],
                ['Si elle savait la vérité, elle serait triste.', '如果她知道真相，她會難過。'],
            ]),
            G('詞尾', '將來詞幹 + ais', [
                ['說', 'je parlerais', '我就會說'],
                ['去', 'j’irais', '我就會去'],
                ['是', 'je serais', '我就會是'],
                ['有', 'nous aurions', '我們就會有'],
            ], [
                ['À ta place, je parlerais moins vite.', '如果我是你，我會說慢一點。'],
                ['Avec plus de temps, j’irais à pied.', '如果時間多一點，我會走路去。'],
                ['Sans ce travail, je serais en vacances.', '如果沒有這份工作，我就在度假了。'],
                ['Nous aurions besoin d’aide.', '我們會需要幫忙。'],
            ]),
        ],
    ),
    L(
        'subjonctif', 'B1', 'Subjonctif', '法文 B1｜虛擬式',
        '虛擬式用在 que 後面，表示必要、意願或情緒，不是在陳述一個事實。il faut que、vouloir que、高興或害怕，都接虛擬式。',
        'il faut que、vouloir que，以及 être、avoir、aller 的虛擬式，附例句、中文、朗讀與 PDF。',
        'être：que je sois、que nous soyons。avoir：que j’aie、qu’il ait。\naller：que j’aille。faire：que je fasse。規則動詞的 nous、vous 和未完成過去相同：que nous parlions。',
        [
            G('必要與意願', 'il faut que、vouloir que', [
                ['必須準時', 'il faut que tu sois à l’heure', '你必須準時'],
                ['希望懂', 'je veux que vous compreniez', '我希望你們懂'],
                ['必須走', 'il faut que nous partions', '我們必須走'],
                ['希望來', 'je veux qu’il vienne', '我希望他來'],
            ], [
                ['Il faut que tu sois à l’heure.', '你必須準時。'],
                ['Je veux que vous compreniez la question.', '我希望你們弄懂這個問題。'],
                ['Il faut que nous partions maintenant.', '我們必須現在走。'],
                ['Elle veut qu’il vienne avec nous.', '她希望他跟我們一起來。'],
            ]),
            G('情緒', '高興、害怕', [
                ['高興你在', 'content que tu sois là', '高興你在這裡'],
                ['害怕遲到', 'peur qu’il soit en retard', '怕他遲到'],
                ['遺憾', 'dommage que vous ne puissiez pas', '可惜您不能'],
                ['驚訝', 'surpris qu’elle sache', '驚訝她知道'],
            ], [
                ['Je suis content que tu sois là.', '我很高興你在這裡。'],
                ['J’ai peur qu’il soit en retard.', '我怕他會遲到。'],
                ['C’est dommage que vous ne puissiez pas venir.', '可惜您不能來。'],
                ['Je suis surpris qu’elle sache la réponse.', '我很驚訝她知道答案。'],
            ]),
            G('être 與 avoir', 'que je sois、que j’aie', [
                ['是', 'que je sois', '我是'],
                ['您是', 'que vous soyez', '您是'],
                ['有', 'que j’aie', '我有'],
                ['他有', 'qu’il ait', '他有'],
            ], [
                ['Il faut que je sois patient.', '我必須有耐心。'],
                ['Je veux que vous soyez prêts.', '我希望你們準備好。'],
                ['Il faut que j’aie mon passeport.', '我必須帶著護照。'],
                ['Je suis content qu’il ait le temps.', '我很高興他有時間。'],
            ]),
        ],
    ),
    L(
        'relatifs', 'B1', 'Pronoms relatifs', '法文 B1｜關係代詞',
        'qui 當關係子句的主詞。que 當受詞。où 指地方或時間。dont 代替 de，用在 parler de、avoir besoin de 這類說法。',
        'qui、que、où、dont，附例句、中文、朗讀與 PDF。',
        'que 在母音前寫成 qu’。\n主詞即使是物，也用 qui，不用 que：le livre qui est sur la table。',
        [
            G('qui、que', '主詞與受詞', [
                ['誰在說', 'la femme qui parle', '正在說話的那位女士'],
                ['我讀的', 'le livre que je lis', '我正在讀的書'],
                ['你看見的', 'l’homme que tu as vu', '你看見的那位男士'],
                ['在桌上的', 'le livre qui est sur la table', '在桌上的書'],
            ], [
                ['La femme qui parle est ma tante.', '正在說話的那位女士是我的阿姨。'],
                ['Le livre que je lis est à Marie.', '我正在讀的書是 Marie 的。'],
                ['L’homme que tu as vu est professeur.', '你看見的那位男士是老師。'],
                ['Le livre qui est sur la table est à moi.', '桌上的書是我的。'],
            ]),
            G('où', '地方、時間', [
                ['我住的城市', 'la ville où j’habite', '我住的城市'],
                ['我們见面的', 'le café où nous nous sommes rencontrés', '我們見面的咖啡館'],
                ['那天', 'le jour où je suis arrivé', '我到達的那天'],
                ['問', 'l’endroit où', '那個地方'],
            ], [
                ['La ville où j’habite est calme.', '我住的城市很安靜。'],
                ['C’est le café où nous nous sommes rencontrés.', '這是我們見面的那家咖啡館。'],
                ['Je me souviens du jour où je suis arrivé.', '我記得我到達的那天。'],
                ['Montre-moi l’endroit où tu travailles.', '指給我看你工作的地方。'],
            ]),
            G('dont', '代替 de', [
                ['你說的', 'le film dont tu parles', '你說的那部電影'],
                ['我需要的', 'le stylo dont j’ai besoin', '我需要的筆'],
                ['我認識家人的', 'une amie dont je connais la famille', '我認識她家人的朋友'],
                ['你來自的', 'la ville dont tu viens', '你來自的城市'],
            ], [
                ['Le film dont tu parles passe ce soir.', '你說的那部電影今晚上映。'],
                ['Voici le stylo dont j’ai besoin.', '這就是我需要的筆。'],
                ['C’est une amie dont je connais bien la famille.', '這是一位我很熟悉她家人的朋友。'],
                ['Taipei est la ville dont je viens.', '台北是我來自的城市。'],
            ]),
        ],
    ),
    L(
        'ordre-pronoms', 'B1', 'Place des pronoms', '法文 B1｜兩個代詞的順序',
        '兩個代詞一起出現時，me、te、nous、vous 在 le、la、les 前面。le、la、les 又在 lui、leur 前面。複合過去裡，代詞放在助動詞前面。',
        'me le、le lui，以及複合過去的位置，附例句、中文、朗讀與 PDF。',
        '肯定命令式把代詞放在後面，順序不同：Donne-le-moi. 否定命令仍放前面：Ne me le donne pas.\nlui 和 leur 不跟 me 放在肯定命令後面的同一套口訣裡。先記陳述句：Je le lui donne.',
        [
            G('me le', '人在物前面', [
                ['給我它', 'il me le donne', '他把它給我'],
                ['給我們它', 'elle nous la montre', '她把它指給我們看'],
                ['否定', 'ne me le montre pas', '不要把它給我看'],
                ['可以', 'tu peux me le prêter', '你可以把它借我'],
            ], [
                ['Ce livre ? Il me le donne.', '這本書嗎？他把它給我。'],
                ['Cette photo ? Elle nous la montre.', '這張照片嗎？她把它指給我們看。'],
                ['Ne me le montre pas maintenant.', '現在不要把它給我看。'],
                ['Tu peux me le prêter ?', '你可以把它借我嗎？'],
            ]),
            G('le lui', '物在 lui 前面', [
                ['給他它', 'je le lui donne', '我把它給他'],
                ['寄給她', 'je le lui ai envoyé', '我已經把它寄給她'],
                ['對他們說它', 'je la leur explique', '我向他們說明它'],
                ['沒給', 'je ne le lui ai pas donné', '我沒有把它給他'],
            ], [
                ['Je donne le livre à Paul. Je le lui donne.', '我把書給 Paul。我把它給他。'],
                ['Je le lui ai envoyé hier.', '我昨天把它寄給她了。'],
                ['Cette règle, je la leur explique.', '這條規則，我向他們說明。'],
                ['Je ne le lui ai pas encore donné.', '我還沒有把它給他。'],
            ]),
            G('命令', '後面，或否定時在前面', [
                ['給我', 'donne-le-moi', '把它給我'],
                ['不要給', 'ne me le donne pas', '不要把它給我'],
                ['告訴他', 'dis-le-lui', '把這件事告訴他'],
                ['不要告訴', 'ne le lui dis pas', '不要告訴他'],
            ], [
                ['Donne-le-moi, s’il te plaît.', '請把它給我。'],
                ['Ne me le donne pas aujourd’hui.', '今天不要把它給我。'],
                ['Dis-le-lui demain.', '明天再告訴他。'],
                ['Ne le lui dis pas encore.', '先不要告訴他。'],
            ]),
        ],
    ),
    L(
        'gerondif', 'B1', 'Gérondif', '法文 B1｜副動詞',
        'en 加現在分詞，表示同一個人同時做的另一件事，或做某事的方式。現在分詞是 nous 現在式去掉 -ons，加上 -ant。',
        'en parlant、en faisant，附例句、中文、朗讀與 PDF。',
        '主詞必須是同一個人。Il apprend en regardant 的「學」和「看」都是他。\nêtre 的現在分詞是 étant。avoir 是 ayant。例外詞幹：sachant、faisant、disant。',
        [
            G('同時', '一邊…一邊…', [
                ['邊看邊學', 'en regardant', '藉著看'],
                ['邊走邊談', 'en marchant', '邊走'],
                ['邊聽邊寫', 'en écoutant', '邊聽'],
                ['邊笑邊說', 'en souriant', '邊笑'],
            ], [
                ['Il apprend le français en regardant des films.', '他藉著看電影學法文。'],
                ['Nous discutons en marchant.', '我們邊走邊聊。'],
                ['Elle écrit en écoutant de la musique.', '她邊聽音樂邊寫。'],
                ['Il a répondu en souriant.', '他笑著回答。'],
            ]),
            G('方式與時間', '在做…的時候', [
                ['下樓時', 'en descendant', '下樓的時候'],
                ['出門時', 'en sortant', '出門的時候'],
                ['讀的時候', 'en lisant', '讀的時候'],
                ['是…的同時', 'tout en', '儘管同時'],
            ], [
                ['Elle est tombée en descendant l’escalier.', '她下樓時跌倒了。'],
                ['En sortant, fermez la porte.', '出門時請把門關上。'],
                ['J’ai compris l’idée en lisant le texte.', '我讀文章的時候懂了這個想法。'],
                ['Il écoute, tout en regardant son téléphone.', '他在聽，同時卻看著手機。'],
            ]),
            G('詞形', 'nous 去掉 -ons 加 -ant', [
                ['說', 'en parlant', '說的時候'],
                ['做', 'en faisant', '做的時候'],
                ['是', 'en étant', '作為'],
                ['有', 'en ayant', '有了之後'],
            ], [
                ['On apprend en parlant.', '藉著說，才學得會。'],
                ['Il a fait une erreur en faisant ce calcul.', '他做這道計算時出錯了。'],
                ['En étant patient, tu vas comprendre.', '只要有耐心，你就會懂。'],
                ['En ayant les documents, nous pouvons commencer.', '文件到了，我們就可以開始。'],
            ]),
        ],
    ),
    L(
        'opinion', 'B1', 'Opinion', '法文 B1｜看法',
        '肯定地說「我認為是事實」時，que 後面用直陳式。否定或不確定時，常用虛擬式。à mon avis 和 selon moi 後面是一個完整的看法，不必改動詞形式。',
        'je pense que、je ne pense pas que、à mon avis，附例句、中文、朗讀與 PDF。',
        'Je pense qu’il a raison. 用直陳式。\nJe ne pense pas qu’il ait raison. 用虛擬式。douter que 也接虛擬式。',
        [
            G('肯定', '直陳式', [
                ['我認為', 'je pense que', '我認為'],
                ['我相信', 'je crois que', '我相信'],
                ['我覺得', 'je trouve que', '我覺得'],
                ['依我看', 'à mon avis', '依我看'],
            ], [
                ['Je pense que c’est une bonne idée.', '我認為這是個好主意。'],
                ['Je crois qu’il a raison.', '我相信他是對的。'],
                ['Je trouve que ce film est trop long.', '我覺得這部電影太長。'],
                ['À mon avis, il faut partir tôt.', '依我看，必須早點出發。'],
            ]),
            G('否定與懷疑', '虛擬式', [
                ['我不認為', 'je ne pense pas que', '我不認為'],
                ['我不相信', 'je ne crois pas que', '我不相信'],
                ['我懷疑', 'je doute que', '我懷疑'],
                ['不肯定', 'il n’est pas sûr que', '還不肯定'],
            ], [
                ['Je ne pense pas que ce soit difficile.', '我不認為這很難。'],
                ['Je ne crois pas qu’il ait raison.', '我不相信他是對的。'],
                ['Je doute qu’il vienne.', '我懷疑他會來。'],
                ['Il n’est pas sûr que nous ayons le temps.', '還不肯定我們有沒有時間。'],
            ]),
            G('說出立場', 'selon moi、pour moi', [
                ['對我來說', 'pour moi', '對我來說'],
                ['據我', 'selon moi', '據我看來'],
                ['我同意', 'je suis d’accord', '我同意'],
                ['我不同意', 'je ne suis pas d’accord', '我不同意'],
            ], [
                ['Pour moi, le plus important est de pratiquer.', '對我來說，最重要的是練習。'],
                ['Selon moi, cette solution est simple.', '據我看來，這個辦法很簡單。'],
                ['Je suis d’accord avec toi.', '我同意你。'],
                ['Je ne suis pas d’accord avec cette idée.', '我不同意這個想法。'],
            ]),
        ],
    ),
    L(
        'connecteurs', 'B1', 'Connecteurs', '法文 B1｜連接詞',
        '把句子接起來時，alors 和 donc 偏口語的結果，cependant 和 pourtant 表示轉折。敘事可以用 d’abord、ensuite、enfin。',
        'alors、donc、pourtant、cependant、d’abord，附例句、中文、朗讀與 PDF。',
        'pourtant 常帶一點出乎意料。cependant 較中性，書面也常用。\nmais 仍然是最直接的「但是」。',
        [
            G('結果', 'alors、donc', [
                ['那麼留下', 'alors nous restons', '那麼我們留下'],
                ['所以成功', 'donc j’ai réussi', '所以我考上了'],
                ['所以問', 'donc je demande', '所以我問'],
                ['結果', 'du coup', '於是'],
            ], [
                ['Il pleut, alors nous restons à la maison.', '下雨了，那麼我們就留在家裡。'],
                ['J’ai beaucoup étudié, donc j’ai réussi.', '我讀了很多，所以考上了。'],
                ['Je ne comprends pas, donc je pose une question.', '我不懂，所以我提問。'],
                ['Le bus n’est pas venu. Du coup, j’ai marché.', '公車沒來。於是我走路了。'],
            ]),
            G('轉折', 'pourtant、cependant', [
                ['卻很冷靜', 'pourtant elle est calme', '她卻很冷靜'],
                ['然而病了', 'cependant il était malade', '然而他病了'],
                ['但是', 'mais', '但是'],
                ['不過', 'par contre', '不過'],
            ], [
                ['Elle est jeune, pourtant elle est très calme.', '她很年輕，卻非常冷靜。'],
                ['Il voulait venir. Cependant, il était malade.', '他想來。然而他病了。'],
                ['Le film est long, mais il est intéressant.', '電影很長，但很有趣。'],
                ['J’aime cette ville. Par contre, elle est chère.', '我喜歡這座城市。不過它物價高。'],
            ]),
            G('順序', 'd’abord、ensuite、enfin', [
                ['首先', 'd’abord', '首先'],
                ['然後', 'ensuite', '然後'],
                ['最後', 'enfin', '最後'],
                ['之後', 'après', '之後'],
            ], [
                ['D’abord, je lis la question.', '首先，我讀問題。'],
                ['Ensuite, je cherche les mots difficiles.', '然後，我找出難字。'],
                ['Enfin, je réponds.', '最後，我作答。'],
                ['Après le cours, nous allons au café.', '下課之後，我們去咖啡館。'],
            ]),
        ],
    ),
]
