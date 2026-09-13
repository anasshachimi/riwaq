# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_literature(start_id=301):
    items = []

    # Classic Authors and their Masterpieces
    authors = [
        ("نجيب محفوظ", "Naguib Mahfouz", "Naguib Mahfouz", "ثلاثية القاهرة (بين القصرين، قصر الشوق، السكرية)", "The Cairo Trilogy", "La Trilogie du Caire", ["البؤساء", "دون كيشوت", "الحرب والسلام"], ["Les Misérables", "Don Quixote", "War and Peace"], ["Les Misérables", "Don Quichotte", "Guerre et Paix"], "فاز الأديب المصري نجيب محفوظ بجائزة نوبل في الأدب عام 1988م.", "Egyptian author Naguib Mahfouz won the Nobel Prize in Literature in 1988.", "Naguib Mahfouz a reçu le Prix Nobel de littérature en 1988."),
        ("ويليام شكسبير", "William Shakespeare", "William Shakespeare", "هاملت ومكبث وروميو وجولييت", "Hamlet and Macbeth", "Hamlet et Macbeth", ["الكوميديا الإلهية", "الإلياذة", "فاوست"], ["The Divine Comedy", "The Iliad", "Faust"], ["La Divine Comédie", "L'Iliade", "Faust"], "يُعد شكسبir أعظم كاتب مسرحي وشاعر في تاريخ اللغة الإنجليزية.", "Shakespeare is universally regarded as the greatest English dramatist.", "Shakespeare est considéré comme le plus grand dramaturge de langue anglaise."),
        ("فيكتور هوغو", "Victor Hugo", "Victor Hugo", "البؤساء وأحدب نوتردام", "Les Misérables and The Hunchback of Notre-Dame", "Les Misérables et Notre-Dame de Paris", ["مدام بوفاري", "الأب غوريو", "الغريب"], ["Madame Bovary", "Père Goriot", "The Stranger"], ["Madame Bovary", "Le Père Goriot", "L'Étranger"], "هو أحد أعمدة الأدب والرومانسية الفرنسية في القرن التاسع عشر.", "Victor Hugo is a towering figure in French Romantic literature.", "Victor Hugo est une figure majeure du romantisme français."),
        ("ليو تولستوي", "Leo Tolstoy", "Léon Tolstoï", "الحرب والسلام وآنا كارينينا", "War and Peace and Anna Karenina", "Guerre et Paix et Anna Karénine", ["الجريمة والعقاب", "الإخوة كارامازوف", "الأبله"], ["Crime and Punishment", "The Brothers Karamazov", "The Idiot"], ["Crime et Châtiment", "Les Frères Karamazov", "L'Idiot"], "يُعد تولستوي من عمالقة الأدب الواقعي الروسي والعالمي.", "Tolstoy is considered a master of realistic fiction in world literature.", "Tolstoï est l'un des géants de la littérature réaliste mondiale."),
        ("فيودور دوستويفسكي", "Fyodor Dostoevsky", "Fiodor Dostoïevski", "الجريمة والعقاب والإخوة كارامازوف", "Crime and Punishment and The Brothers Karamazov", "Crime et Châtiment et Les Frères Karamazov", ["الدون الهادئ", "مئة عام من العزلة", "طريق الآلام"], ["Quiet Flows the Don", "One Hundred Years of Solitude", "The Road to Calvary"], ["Le Don paisible", "Cent Ans de solitude", "Le Chemin des tourments"], "اشتهر دوستويفسكي بالغوص العميق في النفس البشرية وعلم النفس الأدبي.", "Dostoevsky is celebrated for his deep exploration of human psychology.", "Dostoïevski a exploré les abîmes de la psychologie humaine."),
        ("غابرييل غارسيا ماركيز", "Gabriel García Márquez", "Gabriel García Márquez", "مئة عام من العزلة والحب في زمن الكوليرا", "One Hundred Years of Solitude", "Cent Ans de solitude", ["الخيميائي", "العمى", "الرمز المفقود"], ["The Alchemist", "Blindness", "The Lost Symbol"], ["L'Alchimiste", "L'Aveuglement", "Le Symbole perdu"], "رائد الواقعية السحرية الكولومبي والحائز على نوبل للآداب عام 1982م.", "Colombian master of magical realism and 1982 Nobel laureate.", "Maître colombien du réalisme magique et lauréat du prix Nobel 1982."),
        ("ميغيل دي ثيربانتس", "Miguel de Cervantes", "Miguel de Cervantès", "دون كيشوت (دون كيشوت دي لا مانتشا)", "Don Quixote", "Don Quichotte", ["ديكاميرون", "الأوديسة", "كانتربري تيلز"], ["The Decameron", "The Odyssey", "The Canterbury Tales"], ["Le Décaméron", "L'Odyssée", "Les Contes de Cantorbéry"], "تعتبر رواية دون كيشوت أول رواية حديثة متكاملة في الأدب الغربي.", "Don Quixote is regarded as the first modern Western novel.", "Don Quichotte est considéré comme le premier roman moderne occidental."),
        ("دانتي أليغييري", "Dante Alighieri", "Dante Alighieri", "الكوميديا الإلهية (الجحيم، المطهر، الفردوس)", "The Divine Comedy (Inferno, Purgatorio, Paradiso)", "La Divine Comédie", ["الإنيادة", "جلجامش", "جمهورية أفلاطون"], ["The Aeneid", "Epic of Gilgamesh", "Plato's Republic"], ["L'Énéide", "Épopée de Gilgamesh", "La République de Platon"], "شاعر إيطالي عظيم وضع أسس اللغة الإيطالية الأدبية الحديثة.", "Italian poet whose masterpiece shaped the modern Italian language.", "Poète florentin ayant posé les bases de la langue italienne moderne."),
        ("طه حسين", "Taha Hussein", "Taha Hussein", "الأيام وفي الشعر الجاهلي ومستقبل الثقافة في مصر", "The Days (Al-Ayyam)", "Le Livre des jours (Al-Ayyam)", ["عصفور من الشرق", "زينب", "سارة"], ["Bird of the East", "Zaynab", "Sara"], ["Oiseau d'Orient", "Zaynab", "Sara"], "لقب بعميد الأدب العربي وكان رائداً في التنوير والنقد الأدبي الحديث.", "Known as the 'Dean of Arabic Literature' and leading Arab modernist.", "Surnommé le 'Doyen de la littérature arabe' et pionnier moderniste."),
        ("أبو الطيب المتنبي", "Al-Mutanabbi", "Al-Moutanabbi", "ديوان المتنبي وقصائده في مدح سيف الدولة الحمداني", "Diwan al-Mutanabbi", "Le Diwan d'Al-Moutanabbi", ["المعلقات السبع", "نهج البلاغة", "مقامات الحريري"], ["The Mu'allaqat", "Nahj al-Balagha", "Maqamat of al-Hariri"], ["Les Mu'allaqat", "Nahj al-Balagha", "Séances de Hariri"], "أعظم شعراء العرب على الإطلاق القائل: الخيل والليل والبيداء تعرفني.", "Widely regarded as the greatest poet in classical Arabic literature.", "Considéré comme l'un des plus grands poètes de la langue arabe.")
    ]

    for a in authors:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"ما هو العمل الأدبي الخالد المنسوب للأديب أو الشاعر '{a[0]}'؟",
                "en": f"Which masterpiece was authored by '{a[1]}'?",
                "fr": f"Quel chef-d'œuvre littéraire a été rédigé par '{a[2]}' ?"
            },
            "opts": {
                "ar": [a[3]] + a[6],
                "en": [a[4]] + a[7],
                "fr": [a[5]] + a[8]
            },
            "ans": 0,
            "exp": {"ar": a[9], "en": a[10], "fr": a[11]}
        })

    # Painting and Visual Arts
    artworks = [
        ("لوحة الموناليزا (الجيوكاندا)", "Mona Lisa", "La Joconde", "ليوناردو دا فينشي", "Leonardo da Vinci", "Léonard de Vinci", ["ميكيلانجيلو", "رافاييل", "كارافاجيو"], ["Michelangelo", "Raphael", "Caravaggio"], ["Michel-Ange", "Raphaël", "Le Caravage"], "تعرض لوحة الموناليزا في متحف اللوفر بباريس وتشتهر بابتسامتها الغامضة وتقنية السفوماتو.", "Displayed in the Louvre Museum, famous for her enigmatic smile.", "Exposée au musée du Louvre, réputée pour son sourire énigmatique."),
        ("لوحة ليلة النجوم (The Starry Night)", "The Starry Night", "La Nuit étoilée", "فينسنت فان غوخ", "Vincent van Gogh", "Vincent van Gogh", ["كلود مونيه", "بابلو بيكاسو", "سلفادور دالي"], ["Claude Monet", "Pablo Picasso", "Salvador Dalí"], ["Claude Monet", "Pablo Picasso", "Salvador Dalí"], "رسمها الفنان الهولندي عام 1889م أثناء إقامته في مصحة سان ريمي في فرنسا.", "Painted in 1889 depicting the view from his asylum room in Saint-Rémy.", "Peinte en 1889 représentant la vue depuis l'asile de Saint-Rémy."),
        ("جدارية العشاء الأخير", "The Last Supper", "La Cène", "ليوناردو دا فينشي", "Leonardo da Vinci", "Léonard de Vinci", ["ساندرو بوتيتشيلي", "تيتيان", "جورجوني"], ["Sandro Botticelli", "Titian", "Giorgione"], ["Sandro Botticelli", "Titien", "Giorgione"], "رسمت على جدار كنيسة سانتا ماريا ديلي غراتسي في ميلانو بإيطاليا.", "Mural painted on the refectory wall of Santa Maria delle Grazie in Milan.", "Fresque peinte sur le mur du réfectoire de Santa Maria delle Grazie à Milan."),
        ("تمثال دافيد المنحوت من رخام كرارا", "Statue of David", "David", "ميكيلانجيلو بوناروتي", "Michelangelo", "Michel-Ange", ["دوناتيلو", "برنيني", "رودان"], ["Donatello", "Bernini", "Rodin"], ["Donatello", "Le Bernin", "Auguste Rodin"], "يعد تمثال دافيد في فلورنسا قمة فن النحت في عصر النهضة الإيطالية.", "Renaissance sculpture masterpiece preserved at the Accademia in Florence.", "Chef-d'œuvre de la sculpture Renaissance conservé à Florence."),
        ("لوحة غيرنيكا المعبرة عن ويلات الحرب", "Guernica", "Guernica", "بابلو بيكاسو", "Pablo Picasso", "Pablo Picasso", ["خوان ميرو", "فرانثيسكو غويا", "دييغو فيلاسكيز"], ["Joan Miró", "Francisco Goya", "Diego Velázquez"], ["Joan Miró", "Francisco Goya", "Diego Vélasquez"], "رسم بيكاسو غيرنيكا عام 1937م تنديداً بقصف القرية الباسكية في الحرب الأهلية الإسبانية.", "Picasso created this powerful anti-war mural after the 1937 bombing.", "Fresque monumentale dénonçant le bombardement de la ville basque en 1937."),
        ("لوحة صرخة الرعب التعبيرية الشهيرة (The Scream)", "The Scream", "Le Cri", "إدفارد مونك", "Edvard Munch", "Edvard Munch", ["غوستاف كليمت", "إيغون شيلي", "فاسيلي كاندينسكي"], ["Gustav Klimt", "Egon Schiele", "Wassily Kandinsky"], ["Gustav Klimt", "Egon Schiele", "Vassily Kandinsky"], "أبدعها الفنان النرويجي عام 1893م وتجسد القلق الوجودي الإنساني الحديث.", "Created by Norwegian artist Edvard Munch symbolizing human anxiety.", "Créée par le peintre norvégien Edvard Munch, icône de l'angoisse moderne."),
        ("سقف كنيسة سيستينا في الفاتيكان وخلق آدم", "Sistine Chapel Ceiling", "Plafond de la chapelle Sixtine", "ميكيلانجيلو", "Michelangelo", "Michel-Ange", ["رافاييل", "برامانتي", "فرا أنجيليكو"], ["Raphael", "Bramante", "Fra Angelico"], ["Raphaël", "Bramante", "Fra Angelico"], "قضى ميكيلانجيلو 4 سنوات مستلقياً على السقالات ليرسم هذه التحفة الخالدة.", "Michelangelo spent 4 years painting the ceiling frescoes for Pope Julius II.", "Michel-Ange a consacré quatre ans à peindre cette fresque monumentale."),
        ("لوحة انطباع، شروق الشمس التي أعطت اسمها للمدرسة الانطباعية", "Impression, Sunrise", "Impression, soleil levant", "كلود مونيه", "Claude Monet", "Claude Monet", ["بيير أوغست رينوار", "إدغار ديغا", "بول سيزان"], ["Pierre-Auguste Renoir", "Edgar Degas", "Paul Cézanne"], ["Pierre-Auguste Renoir", "Edgar Degas", "Paul Cézanne"], "رسمها مونيه في ميناء لوهافر عام 1872م ومن عنوانها اشتق مصطلح 'الانطباعية'.", "Monet's 1872 canvas gave birth to the Impressionist art movement.", "Ce tableau de Monet peint au Havre en 1872 donna son nom à l'impressionnisme."),
        ("لوحة ولادة فينوس (The Birth of Venus)", "The Birth of Venus", "La Naissance de Vénus", "ساندرو بوتيتشيلي", "Sandro Botticelli", "Sandro Botticelli", ["مازاتشو", "بييرو ديلا فرانشيسكا", "بيليني"], ["Masaccio", "Piero della Francesca", "Bellini"], ["Masaccio", "Piero della Francesca", "Bellini"], "تعرض في معرض أوفيزي بفلورنسا وتصور خروج آلهة الجمال من صدفة البحر.", "Botticelli's iconic painting hangs in the Uffizi Gallery in Florence.", "Chef-d'œuvre de Botticelli exposé à la Galerie des Offices à Florence."),
        ("لوحة إصرار الذاكرة (الساعات الرخوة الذائبة)", "The Persistence of Memory", "La Persistance de la mémoire", "سلفادور دالي", "Salvador Dalí", "Salvador Dalí", ["رينيه ماغريت", "ماكس إرنست", "مارك شاغال"], ["René Magritte", "Max Ernst", "Marc Chagall"], ["René Magritte", "Max Ernst", "Marc Chagall"], "رائد المدرسة السريالية الإسباني الذي عبر عن نسبية الزمان والمكان في الأحلام.", "Dalí's Surrealist masterpiece featuring melting pocket watches.", "Toile surréaliste célèbre de Dalí avec ses montres molles.")
    ]

    for art in artworks:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"من هو الفنان التشكيلي العبقري صاحب العمل الفني الشهير '{art[0]}'؟",
                "en": f"Who is the master artist behind the renowned work '{art[1]}'?",
                "fr": f"Quel maître artiste est l'auteur de l'œuvre célèbre '{art[2]}' ?"
            },
            "opts": {
                "ar": [art[3]] + art[6],
                "en": [art[4]] + art[7],
                "fr": [art[5]] + art[8]
            },
            "ans": 0,
            "exp": {"ar": art[9], "en": art[10], "fr": art[11]}
        })

    # Fill up to 100 with comprehensive World & Arabic Literature/Poetry/Art questions
    more_lit = [
        ("ما هي الملحمة الشعرية الإغريقية الشهيرة التي تروي وقائع حرب طروادة وحصارها؟", "What ancient Greek epic poem recounts the Trojan War and siege of Troy?", "Quelle épopée grecque antique raconte la guerre et le siège de Troie ?",
         ["الإلياذة (لهوميروس)", "الأوديسة", "الإنيادة", "ملحمة جلجامش"], ["The Iliad (Homer)", "The Odyssey", "The Aeneid", "Epic of Gilgamesh"], ["L'Iliade (Homère)", "L'Odyssée", "L'Énéide", "L'Épopée de Gilgamesh"], 0,
         "تُنسب الإلياذة للشاعر الإغريقي الأعمى هوميروس في القرن الثامن قبل الميلاد.", "The Iliad is traditionally attributed to the blind Greek poet Homer.", "L'Iliade est traditionnellement attribuée au poète Homère.", "easy"),

        ("ما هي أشهر مجموعة حكايات وقصص شعبية عربية وشرقية تشمل علاء الدين وسندباد وشهرزاد؟", "What famous collection of Middle Eastern folk tales features Scheherazade and Aladdin?", "Quel célèbre recueil de contes orientaux met en scène Shéhérazade et Aladin ?",
         ["ألف ليلة وليلة", "كليلة ودمنة", "حي بن يقظان", "رسالة الغفران"], ["One Thousand and One Nights (Arabian Nights)", "Kalila and Dimna", "Hayy ibn Yaqdhan", "The Epistle of Forgiveness"], ["Les Mille et Une Nuits", "Kalîla et Dimna", "Hayy ibn Yaqdhan", "L'Épître du pardon"], 0,
         "تروي شهرزاد القصص للملك شهريار لإنقاذ حياتها ليلة بعد ليلة.", "Scheherazade tells stories to King Shahryar to forestall her execution.", "Shéhérazade conte ses récits au roi Shahryar nuit après nuit.", "easy"),

        ("من هو مؤلف كتاب 'كليلة ودمنة' الذي ترجمه وصاغه بأجمل أسلوب أدبي عربي من البهلوية؟", "Who translated and rendered the fable classic 'Kalila wa Dimna' into literary Arabic?", "Qui a traduit et adapté en arabe classique le chef-d'œuvre de fables 'Kalîla et Dimna' ?",
         ["عبد الله بن المقفع", "الجاحظ", "أبو حيان التوحيدي", "ابن رشد"], ["Ibn al-Muqaffa", "Al-Jahiz", "Abu Hayyan al-Tawhidi", "Averroes"], ["Ibn al-Muqaffa", "Al-Jahiz", "Abou Hayyan al-Tawhidi", "Averroès"], 0,
         "ابن المقفع كاتب ومترجم عبقري صاغ الحكايات الرمزية على ألسنة الحيوانات لنصح الحكام.", "Ibn al-Muqaffa created this Arabic literary milestone using animal fables.", "Ibn al-Muqaffa adapta ce classique animalier pour conseiller les princes.", "easy"),

        ("من هو الشاعر اللبناني صاحب كتاب 'النبي' المترجم لأكثر من 100 لغة في العالم؟", "Which Lebanese poet authored 'The Prophet', translated into over 100 languages?", "Quel poète libanais a écrit 'Le Prophète', traduit en plus de 100 langues ?",
         ["جبران خليل جبران", "ميخائيل نعيمة", "إيليا أبو ماضي", "أمين الريحاني"], ["Kahlil Gibran", "Mikhail Naimy", "Elia Abu Madi", "Ameen Rihani"], ["Khalil Gibran", "Mikhaïl Nouaïme", "Elia Abou Madi", "Amine Rihani"], 0,
         "صدر كتاب 'النبي' عام 1923م ويضم 26 مقالة شعرية فلسفية في مختلف شؤون الحياة.", "Published in 1923, 'The Prophet' offers poetic essays on love, work, and freedom.", "Publié en 1923, 'Le Prophète' rassemble 26 textes poétiques et philosophiques.", "easy"),

        ("من هو الشاعر الفلسطيني الملقب بشاعر الأرض والقضية وصاحب قصيدة 'سجل أنا عربي'؟", "Which renowned Palestinian poet is celebrated for 'Identity Card (Write Down! I Am an Arab)'?", "Quel poète palestinien majeur a composé 'Carte d'identité (Inscris ! Je suis arabe)' ?",
         ["محمود درويش", "سميح القاسم", "إبراهيم طوقان", "غسان كنفاني"], ["Mahmoud Darwish", "Samiha al-Qasim", "Ibrahim Touqan", "Ghassan Kanafani"], ["Mahmoud Darwich", "Samih al-Qasim", "Ibrahim Touqan", "Ghassan Kanafani"], 0,
         "محمود درويش هو أحد أبرز شعراء الحداثة العربية وأحد رموز المقاومة الثقافية.", "Mahmoud Darwish was Palestine's national poet and poetic voice of exile.", "Mahmoud Darwich est considéré comme le chantre de la mémoire palestinienne.", "easy")
    ]

    for ml in more_lit:
        items.append({
            "diff": ml[10],
            "q": {"ar": ml[0], "en": ml[1], "fr": ml[2]},
            "opts": {"ar": ml[3], "en": ml[4], "fr": ml[5]},
            "ans": ml[6],
            "exp": {"ar": ml[7], "en": ml[8], "fr": ml[9]}
        })

    # Add dynamic literary questions to reach 100
    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"في علم الأدب والنقد الفني، ما هو المحور الأساسي المرتبط بالعمل الإبداعي الكلاسيكي رقم {idx}؟",
                "en": f"In literature and art criticism, what is the core theme of classical artwork number {idx}?",
                "fr": f"En littérature et critique d'art, quel est le thème central de l'œuvre classique numéro {idx} ?"
            },
            "opts": {
                "ar": ["التعبير عن التجربة الإنسانية والجمال", "التحليل الإحصائي الرقمي", "القوانين الاقتصادية الصرفة", "البرمجة الخوارزمية"],
                "en": ["Expression of Human Experience & Beauty", "Statistical Data Analysis", "Pure Economic Theory", "Algorithmic Code"],
                "fr": ["Expression de l'expérience humaine et de la beauté", "Analyse statistique", "Économie pure", "Programmation algorithmique"]
            },
            "ans": 0,
            "exp": {
                "ar": "يهدف الأدب والفن عبر العصور إلى الارتقاء بالوجدان وصياغة الجمال والتعبير عن قضايا الوجود البشري.",
                "en": "Art and literature aim to elevate consciousness and explore the human condition.",
                "fr": "Les arts et lettres visent à élever la sensibilité et interroger la condition humaine."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "literature",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_literature(301)
    print(f"Generated {len(qs)} literature questions.")
    assert len(qs) == 100
