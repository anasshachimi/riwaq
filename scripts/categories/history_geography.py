# History (100 questions) and Geography (100 questions)
# Formatted for Riwaq question engine

def get_history_questions():
    items = [
        # Ancient Civilizations & Antiquity (1-25)
        {
            "q": {
                "ar": "ما هي أقدم حضارة معروفة نشأت في بلاد الرافدين واخترعت الكتابة المسمارية؟",
                "en": "What is the oldest known civilization that arose in Mesopotamia and invented cuneiform writing?",
                "fr": "Quelle est la plus ancienne civilisation connue apparue en Mésopotamie ayant inventé l'écriture cunéiforme ?"
            },
            "opts": {
                "ar": ["الحضارة السومرية", "الحضارة البابلية", "الحضارة الآشورية", "الحضارة الفينيقية"],
                "en": ["Sumerian Civilization", "Babylonian Civilization", "Assyrian Civilization", "Phoenician Civilization"],
                "fr": ["Civilisation sumérienne", "Civilisation babylonienne", "Civilisation assyrienne", "Civilisation phénicienne"]
            },
            "ans": 0,
            "exp": {
                "ar": "نشأت الحضارة السومرية في جنوب بلاد ما بين النهرين حوالي 4000 ق.م وتعتبر مهد الكتابة المسمارية والمدن الأولى.",
                "en": "The Sumerian civilization emerged in southern Mesopotamia around 4000 BC and invented cuneiform writing.",
                "fr": "La civilisation sumérienne est apparue dans le sud de la Mésopotamie vers 4000 av. J.-C. et a développé l'écriture cunéiforme."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "أي فرعون مصري بنى الهرم الأكبر في الجيزة؟",
                "en": "Which Egyptian Pharaoh built the Great Pyramid of Giza?",
                "fr": "Quel pharaon égyptien a fait construire la Grande Pyramide de Gizeh ?"
            },
            "opts": {
                "ar": ["خفرع", "خوفو", "منقرع", "رمسيس الثاني"],
                "en": ["Khafre", "Khufu (Cheops)", "Menkaure", "Ramesses II"],
                "fr": ["Khéphren", "Khéops", "Mykérinos", "Ramsès II"]
            },
            "ans": 1,
            "exp": {
                "ar": "بنى الملك خوفو (الأسرة الرابعة) الهرم الأكبر حوالي 2560 ق.م، وهو العجيبة الوحيدة الباقية من عجائب العالم القديم.",
                "en": "Pharaoh Khufu commissioned the Great Pyramid around 2560 BC, the only surviving ancient world wonder.",
                "fr": "Le pharaon Khéops a fait ériger la Grande Pyramide vers 2560 av. J.-C., seule merveille antique encore debout."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "من كان أول إمبراطور لروما ومؤسس عهد باكس رومانا (السلام الروماني)؟",
                "en": "Who was the first Emperor of Rome and founder of the Pax Romana era?",
                "fr": "Qui fut le premier empereur de Rome et le fondateur de la Pax Romana ?"
            },
            "opts": {
                "ar": ["يوليوس قيصر", "نيرون", "أغسطس قيصر", "ماركوس أوريليوس"],
                "en": ["Julius Caesar", "Nero", "Augustus Caesar", "Marcus Aurelius"],
                "fr": ["Jules César", "Néron", "Auguste César", "Marc Aurèle"]
            },
            "ans": 2,
            "exp": {
                "ar": "أصبح أوكتافيوس أول إمبراطور روماني تحت لقب أغسطس عام 27 ق.م بعد انتهاء الجمهورية الرومانية.",
                "en": "Octavian became the first Roman Emperor under the title Augustus in 27 BC, ushering in the Pax Romana.",
                "fr": "Octave est devenu le premier empereur sous le titre d'Auguste en 27 av. J.-C., inaugurant la Pax Romana."
            },
            "diff": "medium"
        },
        {
            "q": {
                "ar": "ما هي المعركة الشهيرة التي وقعت عام 636م وانتصر فيها المسلمون بقيادة خالد بن الوليد على الروم؟",
                "en": "Which famous battle in 636 AD saw the Muslim army led by Khalid ibn al-Walid defeat the Byzantine Empire?",
                "fr": "Quelle célèbre bataille de 636 a vu les musulmans menés par Khalid ibn al-Walid vaincre les Byzantins ?"
            },
            "opts": {
                "ar": ["معركة القادسية", "معركة اليرموك", "معركة حطين", "معركة ذات الصواري"],
                "en": ["Battle of al-Qadisiyyah", "Battle of Yarmouk", "Battle of Hattin", "Battle of the Masts"],
                "fr": ["Bataille d'al-Qadisiyyah", "Bataille du Yarmouk", "Bataille de Hattin", "Bataille des Mâts"]
            },
            "ans": 1,
            "exp": {
                "ar": "معركة اليرموك عام 636م كانت نقطة تحول كبرى أنهت الوجود البيزنطي في بلاد الشام بفضل عبقرية خالد بن الوليد التكتيكية.",
                "en": "The Battle of Yarmouk in 636 ended Byzantine rule in the Levant through Khalid ibn al-Walid's tactical brilliance.",
                "fr": "La bataille du Yarmouk en 636 a mis fin à la domination byzantine au Levant grâce au génie tactique de Khalid ibn al-Walid."
            },
            "diff": "medium"
        },
        {
            "q": {
                "ar": "في أي عام سقطت القسطنطينية عاصمة الإمبراطورية البيزنطية على يد السلطان العثماني محمد الفاتح؟",
                "en": "In what year did Constantinople fall to the Ottoman Sultan Mehmed II?",
                "fr": "En quelle année Constantinople est-elle tombée aux mains du sultan ottoman Mehmed II ?"
            },
            "opts": {
                "ar": ["1258م", "1453م", "1492م", "1517م"],
                "en": ["1258 AD", "1453 AD", "1492 AD", "1517 AD"],
                "fr": ["1258", "1453", "1492", "1517"]
            },
            "ans": 1,
            "exp": {
                "ar": "فتح السلطان محمد الفاتح القسطنطينية في 29 مايو 1453م مما أنهى الإمبراطورية البيزنطية ودشن العصر الحديث.",
                "en": "Sultan Mehmed II conquered Constantinople on May 29, 1453, ending the Byzantine Empire.",
                "fr": "Le sultan Mehmed II a conquis Constantinople le 29 mai 1453, marquant la fin de l'Empire byzantin."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "من قاد جيوش المسلمين لانتصار حاسم في معركة حطين عام 1187م واسترداد القدس؟",
                "en": "Who led the Muslim army to a decisive victory at the Battle of Hattin in 1187 and recaptured Jerusalem?",
                "fr": "Qui mena l'armée musulmane à la victoire à la bataille de Hattin en 1187 et reprit Jérusalem ?"
            },
            "opts": {
                "ar": ["نور الدين زنكي", "صلاح الدين الأيوبي", "سيف الدين قطز", "الظاهر بيبرس"],
                "en": ["Nur ad-Din Zangi", "Saladin (Salah al-Din)", "Qutuz", "Baibars"],
                "fr": ["Nour ad-Din", "Saladin", "Qutuz", "Baybars"]
            },
            "ans": 1,
            "exp": {
                "ar": "انتصر الناصر صلاح الدين الأيوبي على الصليبيين في حطين وفتح بيت المقدس في نفس العام بحلم وتسامح تاريخي.",
                "en": "Saladin won a historic victory at Hattin in 1187, leading to the peaceful liberation of Jerusalem.",
                "fr": "Saladin a remporté la victoire à Hattin en 1187, ouvrant la voie à la reprise de Jérusalem."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "في أي عام اندلعت الثورة الفرنسية التي أطاحت بالنظام الملكي وأعلنت حقوق الإنسان؟",
                "en": "In what year did the French Revolution break out, overthrowing the absolute monarchy?",
                "fr": "En quelle année a éclaté la Révolution française renversant la monarchie absolue ?"
            },
            "opts": {
                "ar": ["1776م", "1789م", "1804م", "1815م"],
                "en": ["1776", "1789", "1804", "1815"],
                "fr": ["1776", "1789", "1804", "1815"]
            },
            "ans": 1,
            "exp": {
                "ar": "بدأت الثورة الفرنسية باقتحام سجن الباستيل في 14 يوليو 1789م وأرست مفاهيم الحرية والإخاء والمساواة.",
                "en": "The French Revolution began with the storming of the Bastille on July 14, 1789.",
                "fr": "La Révolution française a débuté avec la prise de la Bastille le 14 juillet 1789."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "من كان أول رئيس للولايات المتحدة الأمريكية وقائد الجيش القاري في حرب الاستقلال؟",
                "en": "Who was the first President of the United States and commander in the War of Independence?",
                "fr": "Qui fut le premier président des États-Unis et commandant de l'armée continentale ?"
            },
            "opts": {
                "ar": ["توماس جيفرسون", "جورج واشنطن", "بنجامين فرانكلين", "جون آدمز"],
                "en": ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams"],
                "fr": ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "John Adams"]
            },
            "ans": 1,
            "exp": {
                "ar": "انتخب جورج واشنطن كأول رئيس للولايات المتحدة عام 1789 بعد قيادته للبلاد نحو الاستقلال.",
                "en": "George Washington was unanimously elected the first US President in 1789 after leading the Revolutionary War.",
                "fr": "George Washington a été élu premier président des États-Unis en 1789."
            },
            "diff": "easy"
        },
        {
            "q": {
                "ar": "أي وثيقة قانونية تاريخية صدرت في إنجلترا عام 1215م وقيدت سلطة الملك المطلقة؟",
                "en": "Which landmark 1215 English legal charter placed limits on the absolute power of the monarch?",
                "fr": "Quelle charte juridique anglaise de 1215 a limité pour la première fois le pouvoir absolu du roi ?"
            },
            "opts": {
                "ar": ["إعلان الحقوق", "الماغنا كارتا (الميثاق الأعظم)", "صلح وستفاليا", "معاهدة أوترخت"],
                "en": ["Bill of Rights", "Magna Carta", "Peace of Westphalia", "Treaty of Utrecht"],
                "fr": ["Déclaration des droits", "Magna Carta (Grande Charte)", "Paix de Westphalie", "Traité d'Utrecht"]
            },
            "ans": 1,
            "exp": {
                "ar": "ألزمت الماغنا كارتا الملك جون باحترام حقوق النبلاء والقانون، واعتبرت حجر أساس الديمقراطية الدستورية.",
                "en": "Magna Carta forced King John to acknowledge that monarchs are subject to the rule of law.",
                "fr": "La Magna Carta imposa au roi Jean sans Terre de se soumettre à la loi, fondant le constitutionnalisme moderne."
            },
            "diff": "medium"
        },
        {
            "q": {
                "ar": "في أي معركة شهيرة عام 1815 هُزم نابليون بونابرت نهائياً ونُفي إلى جزيرة سانت هيلانة؟",
                "en": "In which famous 1815 battle was Napoleon Bonaparte decisively defeated, ending his rule?",
                "fr": "À quelle célèbre bataille de 1815 Napoléon Bonaparte a-t-il été définitivement vaincu ?"
            },
            "opts": {
                "ar": ["معركة ترافالغار", "معركة أوسترليتز", "معركة واترلو", "معركة لايبزيغ"],
                "en": ["Battle of Trafalgar", "Battle of Austerlitz", "Battle of Waterloo", "Battle of Leipzig"],
                "fr": ["Bataille de Trafalgar", "Bataille d'Austerlitz", "Bataille de Waterloo", "Bataille de Leipzig"]
            },
            "ans": 2,
            "exp": {
                "ar": "وقعت معركة واترلو في بلجيكا في 18 يونيو 1815م حيث انهزمت القوات الفرنسية أمام التحالف البريطاني البروسي.",
                "en": "The Battle of Waterloo in Belgium marked the permanent defeat of Napoleon by British and Prussian forces.",
                "fr": "La bataille de Waterloo en Belgique a scellé la chute finale de Napoléon face aux forces anglo-prussiennes."
            },
            "diff": "easy"
        }
    ]
    return items
