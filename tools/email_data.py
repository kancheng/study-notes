"""Shared email-writing lesson content for en, de, fr, and ja pages."""

# Shared beginner intro (Chinese). Language-specific tips live in INTRO_BY_LANG.
INTRO_SHARED = [
    (
        '先想清楚目的',
        '寫信前先決定：通知、詢問、請求，還是道謝。目的清楚，主旨與正文才會短而準。',
    ),
    (
        '主旨一行說完',
        '收件人常只看主旨決定是否開啟。寫「誰／什麼事／何時」，避免只有 Hi 或 您好。',
    ),
    (
        '基本結構',
        '常見順序是：主旨 → 稱呼 → 開頭（自我介紹或來意）→ 正文（重點與請求）→ 結尾禮貌語 → 署名。',
    ),
    (
        '一段一件事',
        '一段話只講一個重點。請求要明確，並標出時間、地點或回覆期限，方便對方回答。',
    ),
    (
        '語氣對人',
        '正式場合用較客氣的稱呼與結尾；熟人或同事可用較短、較口語的寫法。寧願稍正式，也不要太隨便。',
    ),
]

INTRO_BY_LANG = {
    'en': [
        (
            '英文常用套語',
            '稱呼多用 Dear Mr./Ms. + 姓；熟識可用 Hi + 名。結尾常見 Best regards、Kind regards；很熟可用 Best。',
        ),
        (
            '開頭怎麼寫',
            '第一次聯絡可先自我介紹：My name is… I am writing to…。回信可用 Thank you for your email. 再接正文。',
        ),
    ],
    'de': [
        (
            '德文常用套語',
            '正式多用 Sehr geehrte Frau / Sehr geehrter Herr + 姓；熟識可用 Hallo + 名。結尾標準是 Mit freundlichen Grüßen（後面通常不加逗號）。',
        ),
        (
            '用 Sie 還是 du',
            '不熟或公事一律用 Sie 與 Ihnen。正文動詞第二位；請求可用 Ich möchte… / Würde … bei Ihnen passen?',
        ),
    ],
    'fr': [
        (
            '法文常用套語',
            '正式多用 Madame / Monsieur；知道姓可寫 Madame Dupont。結尾常見 Cordialement；更客氣可用 Bien cordialement。',
        ),
        (
            '開頭與主旨',
            '主旨欄寫 Objet。第一次聯絡可 Je m’appelle… Je vous écris pour…。回信可 Je vous remercie de votre message.',
        ),
    ],
    'ja': [
        (
            '日文常用套語',
            '稱呼多寫「姓＋様」。結尾常用「よろしくお願いいたします」。署名寫在最後；公司信可能再加所屬與連絡方式。',
        ),
        (
            '敬語與來意',
            '商務信常用丁寧語／謙譲語：申します、いたします、いただけますか。開頭可先報名，再說「〜と思い、メールいたしました」。',
        ),
    ],
}

# Full sample: Hao-Cheng asks Ms. Tanaka for a short meeting next week.
# Latin langs: (part_zh, text, note_zh)
# Japanese: (part_zh, kanji, kana, roma, note_zh)
EXAMPLE = {
    'en': [
        (
            '主旨',
            'Request for a short meeting next week',
            '主旨直接寫請求與時間範圍，收件人一看就懂。',
        ),
        (
            '稱呼',
            'Dear Ms. Tanaka,',
            '正式稱呼：Dear + Ms./Mr. + 姓，後面加逗號。',
        ),
        (
            '開頭・自我介紹',
            'My name is Hao-Cheng, and I work in Taipei.',
            '第一次聯絡先報姓名與工作地，讓對方知道你是誰。',
        ),
        (
            '來意',
            'I am writing to ask if we could meet briefly next week.',
            'I am writing to… 是說明寫信目的的常用句型。',
        ),
        (
            '正文・目的',
            'I would like to discuss the project schedule.',
            'I would like to… 比 I want to… 更客氣，適合公事。',
        ),
        (
            '請求・具體時間',
            'Would Tuesday afternoon work for you?',
            '用問句提出具體時段，方便對方回答 yes／no 或另約。',
        ),
        (
            '結尾禮貌',
            'Thank you for your time.',
            '感謝對方撥空，語氣禮貌且簡短。',
        ),
        (
            '結尾敬語',
            'Best regards,',
            '半正式到正式都常用；也可寫 Kind regards。',
        ),
        (
            '署名',
            'Hao-Cheng',
            '署名單獨一行；商務信可再加職稱與聯絡方式。',
        ),
    ],
    'de': [
        (
            '主旨',
            'Bitte um ein kurzes Treffen nächste Woche',
            'Betreff 寫清楚請求與時間；德文常用 Bitte um…。',
        ),
        (
            '稱呼',
            'Sehr geehrte Frau Tanaka,',
            '女性用 Sehr geehrte Frau + 姓；男性用 Sehr geehrter Herr + 姓。',
        ),
        (
            '開頭・自我介紹',
            'Mein Name ist Hao-Cheng, und ich arbeite in Taipei.',
            '第一次聯絡先報姓名與工作地。正式信裡常用 Sie。',
        ),
        (
            '來意',
            'Ich schreibe Ihnen, weil ich Sie nächste Woche kurz treffen möchte.',
            'Ich schreibe Ihnen, weil… 清楚說明為什麼寫這封信。',
        ),
        (
            '正文・目的',
            'Ich möchte den Projektplan besprechen.',
            'möchte 比 will 客氣，適合提出想討論的事。',
        ),
        (
            '請求・具體時間',
            'Würde Dienstagnachmittag bei Ihnen passen?',
            '用 würde … passen? 禮貌地詢問對方是否方便。',
        ),
        (
            '結尾禮貌',
            'Vielen Dank für Ihre Zeit.',
            '感謝對方的時間；Ihre 對應正式的 Sie。',
        ),
        (
            '結尾敬語',
            'Mit freundlichen Grüßen',
            '標準正式結尾；後面通常不加逗號，下一行直接署名。',
        ),
        (
            '署名',
            'Hao-Cheng',
            '署名單獨一行；必要時可加職稱與電話／電郵。',
        ),
    ],
    'fr': [
        (
            '主旨',
            'Demande d’un court rendez-vous la semaine prochaine',
            'Objet 要具體；Demande de… 適合請求類郵件。',
        ),
        (
            '稱呼',
            'Madame Tanaka,',
            '正式可用 Madame / Monsieur；知道姓就加上姓。後面加逗號。',
        ),
        (
            '開頭・自我介紹',
            'Je m’appelle Hao-Cheng et je travaille à Taipei.',
            '第一次聯絡先報姓名與工作城市。',
        ),
        (
            '來意',
            'Je vous écris pour vous demander si nous pourrions nous rencontrer brièvement la semaine prochaine.',
            'Je vous écris pour… 用來說明寫信目的；conditionnel（pourrions）較客氣。',
        ),
        (
            '正文・目的',
            'Je voudrais parler du calendrier du projet.',
            'Je voudrais… 比 Je veux… 禮貌，適合公事請求。',
        ),
        (
            '請求・具體時間',
            'Est-ce que mardi après-midi vous conviendrait ?',
            '用條件式 conviendrait 詢問時段是否合適。',
        ),
        (
            '結尾禮貌',
            'Je vous remercie de votre temps.',
            '感謝對方撥冗；正式信常用 vous。',
        ),
        (
            '結尾敬語',
            'Cordialement,',
            '通用正式結尾；也可寫 Bien cordialement。',
        ),
        (
            '署名',
            'Hao-Cheng',
            '署名單獨一行；商務信可再加職稱與聯絡方式。',
        ),
    ],
    'ja': [
        (
            '主旨',
            '来週の短い打ち合わせのお願い',
            'らいしゅう の みじかい うちあわせ の おねがい',
            'Raishuu no mijikai uchiawase no onegai',
            '件名寫「什麼事＋お願い」，比只寫「ご連絡」更清楚。',
        ),
        (
            '稱呼',
            '田中様',
            'たなか さま',
            'Tanaka sama',
            '對不熟或公事對象用「姓＋様」。後面通常空一行再寫正文。',
        ),
        (
            '開頭・自我介紹',
            '私はハオチェンと申します。台北で働いています。',
            'わたし は ハオチェン と もうします。 たいぺい で はたらいて います。',
            'Watashi wa haochen to moushimasu. Taipei de hataraite imasu.',
            '「申します」是謙譲語，比「言います」更適合商務自我介紹。',
        ),
        (
            '來意',
            '来週、少しお時間をいただけないかと思い、メールいたしました。',
            'らいしゅう、 すこし おじかん を いただけない か と おもい、 メール いたしました。',
            'Raishuu, sukoshi ojikan o itadakenai ka to omoi, meeru itashimashita.',
            '「〜と思い、メールいたしました」婉轉說明寫信原因；「いただく」表接受對方的時間。',
        ),
        (
            '正文・目的',
            'プロジェクトの予定についてご相談したいです。',
            'プロジェクト の よてい に ついて ごそうだん したい です。',
            'Purojekuto no yotei ni tsuite gosoudan shitai desu.',
            '「ご相談したいです」客氣地說想商量；外來語「プロジェクト」常用片假名。',
        ),
        (
            '請求・具體時間',
            '火曜の午後はご都合いかがでしょうか。',
            'かよう の ごご は ごつごう いかが でしょうか。',
            'Kayou no gogo wa gotsugou ikaga deshou ka.',
            '「ご都合いかがでしょうか」是詢問對方是否方便的常用敬語。',
        ),
        (
            '結尾禮貌',
            'お忙しいところ恐れ入りますが、よろしくお願いいたします。',
            'おいそがしい ところ おそれいります が、 よろしく おねがい いたします。',
            'Oisogashii tokoro osoreirimasu ga, yoroshiku onegai itashimasu.',
            '先致歉佔用忙碌時間，再以「お願いいたします」收束請求。',
        ),
        (
            '署名',
            'ハオチェン',
            'ハオチェン',
            'Haochen',
            '署名寫在最後；商務信可在上方加所屬單位與連絡方式。',
        ),
    ],
}

# Display order of parts when composing the full sample block.
SUBJECT_PART = '主旨'
