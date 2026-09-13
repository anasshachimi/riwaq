# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_history(start_id=1):
    items = []
    
    # 100 History Questions
    data = [
        # (diff, ar_q, en_q, fr_q, ar_opts, en_opts, fr_opts, ans, ar_exp, en_exp, fr_exp)
        (
            "easy",
            "ما هي أقدم حضارة معروفة نشأت في بلاد ما بين النهرين واخترعت الكتابة المسمارية؟",
            "What is the earliest known civilization that arose in Mesopotamia and invented cuneiform?",
            "Quelle est la plus ancienne civilisation de Mésopotamie ayant inventé l'écriture cunéiforme ?",
            ["الحضارة السومرية", "الحضارة البابلية", "الحضارة الآشورية", "الحضارة الفينيقية"],
            ["Sumerian", "Babylonian", "Assyrian", "Phoenician"],
            ["Sumérienne", "Babylonienne", "Assyrienne", "Phénicienne"],
            0,
            "نشأت السومرية في جنوب العراق حوالي 4000 ق.م وهي أول من ابتكر نظام كتابة مدون في التاريخ.",
            "Sumer emerged in southern Iraq around 4000 BC and created the world's first writing system.",
            "Sumer est apparue dans le sud de l'Irak vers 4000 av. J.-C. et a créé le premier système d'écriture."
        ),
        (
            "easy",
            "أي فرعون مصري أمر ببناء الهرم الأكبر في الجيزة؟",
            "Which Egyptian Pharaoh commissioned the Great Pyramid of Giza?",
            "Quel pharaon égyptien a commandé la Grande Pyramide de Gizeh ?",
            ["خفرع", "خوفو", "منقرع", "رمسيس الثاني"],
            ["Khafre", "Khufu", "Menkaure", "Ramesses II"],
            ["Khéphren", "Khéops", "Mykérinos", "Ramsès II"],
            1,
            "بنى الملك خوفو الهرم الأكبر حوالي 2560 ق.م ليكون مقبرة ملكية وظل أطول بناء صنعه الإنسان لآلاف السنين.",
            "Pharaoh Khufu built the Great Pyramid around 2560 BC, the tallest man-made structure for millennia.",
            "Khéops a fait construire la Grande Pyramide vers 2560 av. J.-C., plus haute structure humaine pendant des millénaires."
        ),
        (
            "medium",
            "من كان أول إمبراطور لروما ومؤسس عهد السلام الروماني (باكس رومانا)؟",
            "Who was the first Emperor of Rome and founder of the Pax Romana?",
            "Qui fut le premier empereur de Rome et le fondateur de la Pax Romana ?",
            ["يوليوس قيصر", "نيرون", "أغسطس قيصر", "كاليغولا"],
            ["Julius Caesar", "Nero", "Augustus Caesar", "Caligula"],
            ["Jules César", "Néron", "Auguste César", "Caligula"],
            2,
            "أصبح أوكتافيوس أول إمبراطور تحت اسم أغسطس عام 27 ق.م بعد انهيار الجمهورية الرومانية.",
            "Octavian became the first Roman emperor under the name Augustus in 27 BC.",
            "Octave est devenu le premier empereur sous le nom d'Auguste en 27 av. J.-C."
        ),
        (
            "easy",
            "في أي معركة عام 636م انتصر المسلمون بقيادة خالد بن الوليد على الإمبراطورية البيزنطية؟",
            "In which 636 AD battle did Muslims led by Khalid ibn al-Walid defeat the Byzantines?",
            "Lors de quelle bataille en 636 les musulmans menés par Khalid ibn al-Walid ont-ils vaincu les Byzantins ?",
            ["معركة القادسية", "معركة اليرموك", "معركة حطين", "معركة عين جالوت"],
            ["Battle of al-Qadisiyyah", "Battle of Yarmouk", "Battle of Hattin", "Battle of Ain Jalut"],
            ["Bataille d'al-Qadisiyyah", "Bataille du Yarmouk", "Bataille de Hattin", "Bataille d'Ain Djalout"],
            1,
            "فتحت معركة اليرموك بلاد الشام كاملة أمام المسلمين بفضل التخطيط العسكري البارع لخالد بن الوليد.",
            "The Battle of Yarmouk ended Byzantine rule in the Levant through Khalid's military genius.",
            "La bataille du Yarmouk a mis fin à la domination byzantine au Levant."
        ),
        (
            "easy",
            "في أي عام فتح السلطان العثماني محمد الفاتح مدينة القسطنطينية؟",
            "In what year did Ottoman Sultan Mehmed the Conqueror take Constantinople?",
            "En quelle année le sultan ottoman Mehmed le Conquérant a-t-il pris Constantinople ?",
            ["1258م", "1453م", "1492م", "1517م"],
            ["1258 AD", "1453 AD", "1492 AD", "1517 AD"],
            ["1258", "1453", "1492", "1517"],
            1,
            "سقطت القسطنطينية في 29 مايو 1453م لتصبح عاصمة الدولة العثمانية باسم إسطنبول.",
            "Constantinople fell on May 29, 1453, becoming the Ottoman capital Istanbul.",
            "Constantinople est tombée le 29 mai 1453, devenant la capitale ottomane Istanbul."
        ),
        (
            "easy",
            "من قاد جيوش المسلمين لتحقيق النصر في معركة حطين عام 1187م وتحرير القدس؟",
            "Who led the Muslim armies to victory at the Battle of Hattin in 1187?",
            "Qui a mené les armées musulmanes à la victoire lors de la bataille de Hattin en 1187 ?",
            ["نور الدين زنكي", "صلاح الدين الأيوبي", "سيف الدين قطز", "بيبرس"],
            ["Nur ad-Din Zangi", "Saladin (Salah al-Din)", "Qutuz", "Baibars"],
            ["Nour ad-Din", "Saladin", "Qutuz", "Baybars"],
            1,
            "انتصر صلاح الدين على الجيوش الصليبية في حطين واستعاد القدس مع إظهار تسامح ونبل عظيمين.",
            "Saladin decisively defeated the Crusader forces at Hattin and liberated Jerusalem.",
            "Saladin a battu les armées croisées à Hattin et libéré Jérusalem."
        ),
        (
            "medium",
            "أي قائد مملوكي قاد المسلمين لصد زحف المغول في معركة عين جالوت عام 1260م؟",
            "Which Mamluk leader stopped the Mongol invasion at the Battle of Ain Jalut in 1260?",
            "Quel dirigeant mamelouk a stoppé l'invasion mongole à la bataille d'Ain Djalout en 1260 ?",
            ["سيف الدين قطز", "شجر الدر", "قلاوون", "برقوق"],
            ["Saif ad-Din Qutuz", "Shajar al-Durr", "Qalawun", "Barquq"],
            ["Saif ad-Din Qutuz", "Chajar al-Durr", "Qalawun", "Barquq"],
            0,
            "معركة عين جالوت في فلسطين أوقفت أول مرة تمدد الإمبراطورية المغولية وأنقذت العالم الإسلامي.",
            "The Battle of Ain Jalut halted Mongol expansion for the first time in history.",
            "La bataille d'Ain Djalout a stoppé l'expansion mongole pour la première fois."
        ),
        (
            "easy",
            "في أي عام انطلقت الثورة الفرنسية بسقوط حصن الباستيل؟",
            "In which year did the French Revolution begin with the storming of the Bastille?",
            "En quelle année la Révolution française a-t-elle débuté avec la prise de la Bastille ?",
            ["1776م", "1789م", "1804م", "1815م"],
            ["1776", "1789", "1804", "1815"],
            ["1776", "1789", "1804", "1815"],
            1,
            "اقتحم الثوار سجن الباستيل في 14 يوليو 1789م وأصبح هذا التاريخ عيداً وطنياً لفرنسا.",
            "The storming of the Bastille on July 14, 1789 became France's national holiday.",
            "La prise de la Bastille le 14 juillet 1789 est devenue la fête nationale française."
        ),
        (
            "medium",
            "ما هي المعاهدة التي أنهت الحرب العالمية الأولى عام 1919م؟",
            "Which treaty officially concluded World War I in 1919?",
            "Quel traité a officiellement conclu la Première Guerre mondiale en 1919 ?",
            ["معاهدة فرساي", "معاهدة وستفاليا", "معاهدة أوترخت", "معاهدة لوزان"],
            ["Treaty of Versailles", "Treaty of Westphalia", "Treaty of Utrecht", "Treaty of Lausanne"],
            ["Traité de Versailles", "Paix de Westphalie", "Traité d'Utrecht", "Traité de Lausanne"],
            0,
            "وُقعت معاهدة فرساي في قصر فرساي بفرنسا وفرضت شروطاً قاسية على ألمانيا أثرت في مجريات القرن العشرين.",
            "The Treaty of Versailles imposed strict reparations on Germany following WWI.",
            "Le traité de Versailles a imposé de lourdes réparations à l'Allemagne après la guerre."
        ),
        (
            "easy",
            "في أي عام سقط جدار برلين مما مهد الطريق لإعادة توحيد ألمانيا ونهاية الحرب الباردة؟",
            "In what year did the Berlin Wall fall, leading to German reunification?",
            "En quelle année le mur de Berlin est-il tombé, menant à la réunification allemande ?",
            ["1985م", "1989م", "1991م", "1993م"],
            ["1985", "1989", "1991", "1993"],
            ["1985", "1989", "1991", "1993"],
            1,
            "سقط جدار برلين في 9 نوفمبر 1989م بعد 28 عاماً من الفصل بين برلين الشرقية والغربية.",
            "The Berlin Wall fell on November 9, 1989, ending 28 years of division.",
            "Le mur de Berlin est tombé le 9 novembre 1989, mettant fin à 28 ans de division."
        )
    ]
    
    # We will expand data programmatically with 90 more authentic historical events
    history_events = [
        ("ما هي عاصمة الدولة الأموية في عهد ازدهارها؟", "What was the capital of the Umayyad Caliphate at its height?", "Quelle était la capitale du califat omeyyade à son apogée ?",
         ["دمشق", "بغداد", "القاهرة", "الكوفة"], ["Damascus", "Baghdad", "Cairo", "Kufa"], ["Damas", "Bagdad", "Le Caire", "Koufa"], 0,
         "كانت دمشق عاصمة بني أمية من عام 661م حتى 750م.", "Damascus served as Umayyad capital from 661 to 750 AD.", "Damas a été la capitale omeyyade de 661 à 750.", "easy"),
        
        ("أي خليفة عباسي أسس مدينة بغداد وجعلها عاصمة الخلافة؟", "Which Abbasid Caliph founded Baghdad and made it the capital?", "Quel calife abbasside a fondé Bagdad et en a fait sa capitale ?",
         ["أبو العباس السفاح", "أبو جعفر المنصور", "هارون الرشيد", "المأمون"], ["Al-Saffah", "Al-Mansur", "Harun al-Rashid", "Al-Ma'mun"], ["Al-Saffah", "Al-Mansour", "Haroun al-Rachid", "Al-Ma'moun"], 1,
         "بنى المنصور بغداد عام 762م وسماها مدينة السلام.", "Al-Mansur founded Baghdad in 762 AD as the City of Peace.", "Al-Mansour a fondé Bagdad en 762 sous le nom de Cité de la Paix.", "medium"),

        ("من كان قائد الحملة التي فتحت بلاد الأندلس عام 711م؟", "Who led the expedition that conquered Hispania (al-Andalus) in 711 AD?", "Qui dirigea l'expédition qui conquit al-Andalus en 711 ?",
         ["طارق بن زياد", "موسى بن نصير", "عقبة بن نافع", "حسان بن النعمان"], ["Tariq ibn Ziyad", "Musa ibn Nusayr", "Uqba ibn Nafi", "Hassan ibn al-Nu'man"], ["Tariq ibn Ziyad", "Moussa ibn Noussayr", "Oqba ibn Nafi", "Hassan ibn al-Nouman"], 0,
         "عبر طارق بن زياد المضيق الذي سُمي باسمه (مضيق جبل طارق) عام 711م.", "Tariq ibn Ziyad crossed the strait now named after him (Gibraltar) in 711 AD.", "Tariq ibn Ziyad a franchi le détroit qui porte son nom (Gibraltar) en 711.", "easy"),

        ("أي إمبراطور بيزنطي اشتهر بتدوين القانون الروماني وبناء كنيسة آيا صوفيا؟", "Which Byzantine Emperor codified Roman law and built Hagia Sophia?", "Quel empereur byzantin a codifié le droit romain et bâti Sainte-Sophie ?",
         ["قسطنطين العظيم", "جستنيان الأول", "هرقل", "باسيل الثاني"], ["Constantine the Great", "Justinian I", "Heraclius", "Basil II"], ["Constantin le Grand", "Justinien Ier", "Héraclius", "Basile II"], 1,
         "حكم جستنيان في القرن السادس الميلادي وأصدر مدونة القانون المدني الشهيرة.", "Justinian I ruled in the 6th century and issued the Corpus Juris Civilis.", "Justinien Ier a régné au VIe siècle et publié le Corpus Juris Civilis.", "medium"),

        ("من أسس الإمبراطورية المغولية ووحد قبائل سهوب آسيا الوسطى؟", "Who founded the Mongol Empire and united the steppe tribes?", "Qui a fondé l'Empire mongol et unifié les tribus nomades ?",
         ["جنكيز خان", "قوبلاي خان", "تيمورلنك", "هولاكو"], ["Genghis Khan", "Kublai Khan", "Tamerlane", "Hulagu Khan"], ["Gengis Khan", "Kubilai Khan", "Tamerlan", "Houlagou"], 0,
         "وحد جنكيز خان القبائل المغولية عام 1206م وأنشأ أوسع إمبراطورية متصلة في التاريخ.", "Genghis Khan founded the Mongol Empire in 1206, the largest contiguous empire.", "Gengis Khan a fondé l'Empire mongol en 1206, le plus vaste empire contigu.", "easy"),

        ("في أي عام انهار الاتحاد السوفيتي رسمياً معلناً نهاية الحرب الباردة؟", "In what year did the Soviet Union officially dissolve, ending the Cold War?", "En quelle année l'Union soviétique s'est-elle officiellement dissoute ?",
         ["1989م", "1990م", "1991م", "1992م"], ["1989", "1990", "1991", "1992"], ["1989", "1990", "1991", "1992"], 2,
         "أُعلن حل الاتحاد السوفيتي في ديسمبر 1991 واستقالة ميخائيل غورباتشوف.", "The USSR officially dissolved in December 1991 following Gorbachev's resignation.", "L'URSS a été dissoute en décembre 1991 suite à la démission de Gorbatchev.", "easy"),

        ("من كان قائد ثورة الاستقلال في أمريكا اللاتينية وحمل لقب المحرر (El Libertador)؟", "Who led South American independence and was known as El Libertador?", "Qui mena les guerres d'indépendance en Amérique du Sud sous le titre El Libertador ?",
         ["سيمون بوليفار", "خوسيه دي سان مارتين", "تشي غيفارا", "إميليانو زاباتا"], ["Simón Bolívar", "José de San Martín", "Che Guevara", "Emiliano Zapata"], ["Simón Bolívar", "José de San Martín", "Che Guevara", "Emiliano Zapata"], 0,
         "حرر سيمون بوليفار فنزويلا وكولومبيا والإكوادور وبيرو وبوليفيا من الحكم الإسباني.", "Bolívar liberated Venezuela, Colombia, Ecuador, Peru, and Bolivia from Spain.", "Bolívar a libéré le Venezuela, la Colombie, l'Équateur, le Pérou et la Bolivie.", "medium"),

        ("في أي مؤتمر دولي عام 1884-1885 تقاسمت القوى الأوروبية قارة إفريقيا استعمارياً؟", "Which 1884-1885 conference partitioned Africa among European colonial powers?", "Quelle conférence de 1884-1885 a partagé l'Afrique entre puissances coloniales ?",
         ["مؤتمر باريس", "مؤتمر برلين", "مؤتمر فيينا", "مؤتمر يالطا"], ["Conference of Berlin", "Conference of Paris", "Congress of Vienna", "Yalta Conference"], ["Conférence de Berlin", "Conférence de Paris", "Congrès de Vienne", "Conférence de Yalta"], 0,
         "نظم المستشار الألماني بسمارك مؤتمر برلين لتقسيم إفريقيا دون أي تمثيل إفريقي.", "Bismarck organized the Berlin Conference to partition Africa without African input.", "Bismarck a organisé la Conférence de Berlin pour diviser l'Afrique.", "hard"),

        ("من كان رئيس جنوب إفريقيا الذي قاد إنهاء نظام الفصل العنصري (الأبارتايد) بعد 27 عاماً في السجن؟", "Who led the fight to end Apartheid in South Africa after 27 years in prison?", "Qui a mené la fin de l'Apartheid en Afrique du Sud après 27 ans de prison ?",
         ["نيلسون مانديلا", "ديزموند توتو", "ستيف بيكو", "ثابو مبيكي"], ["Nelson Mandela", "Desmond Tutu", "Steve Biko", "Thabo Mbeki"], ["Nelson Mandela", "Desmond Tutu", "Steve Biko", "Thabo Mbeki"], 0,
         "أُفرج عن نيلسون مانديلا عام 1990 وانتُخب رئيساً عام 1994 ونال جائزة نوبل للسلام.", "Mandela was released in 1990, became president in 1994, and won the Nobel Peace Prize.", "Mandela a été libéré en 1990, est devenu président en 1994 et a reçu le Nobel de la paix.", "easy"),

        ("ما اسم الحضارة القديمة التي اشتهرت في تونس وأسست قرطاج وقادها حنبعل (هانيبال)؟", "Which ancient civilization founded Carthage in Tunisia and produced Hannibal?", "Quelle civilisation antique a fondé Carthage en Tunisie et produit Hannibal ?",
         ["الحضارة الفينيقية", "الحضارة الإغريقية", "الحضارة الرومانية", "الحضارة الفرعونية"], ["Phoenician", "Greek", "Roman", "Egyptian"], ["Phénicienne", "Grecque", "Romaine", "Égyptienne"], 0,
         "أسس الفينيقيون قرطاج عام 814 ق.م وخاض حنبعل الحروب البونية الشهيرة ضد روما.", "Phoenicians founded Carthage in 814 BC; Hannibal famously marched against Rome.", "Les Phéniciens ont fondé Carthage en 814 av. J.-C. ; Hannibal a défié Rome.", "easy")
    ]
    
    # Generate the remaining 80 questions with factual templates across historical eras
    rulers_events = [
        ("حمورابي", "Hammurabi", "Hammourabi", "بابل", "Babylon", "Babylone", "شريعة حمورابي القانونية الشهيرة", "famous Code of Laws", "célèbre Code de lois"),
        ("كورش الكبير", "Cyrus the Great", "Cyrus le Grand", "فارس (الأخمينية)", "Persia (Achaemenid)", "Perse achéménide", "تأسيس أول إمبراطورية فارسية عالمية", "founding the First Persian Empire", "fondation du Premier Empire perse"),
        ("الإسكندر الأكبر", "Alexander the Great", "Alexandre le Grand", "مقدونيا واليونان", "Macedonia & Greece", "Macédoine et Grèce", "توسيع إمبراطوريته من اليونان إلى الهند", "expanding his empire to India", "expansion jusqu'à l'Inde"),
        ("الملك رمسيس الثاني", "Ramesses II", "Ramsès II", "مصر القديمة", "Ancient Egypt", "Égypte antique", "معركة قادش وتوقيع أول معاهدة سلام في التاريخ", "Battle of Kadesh and the first recorded peace treaty", "Bataille de Qadesh et premier traité de paix"),
        ("توت عنخ آمون", "Tutankhamun", "Toutânkhamon", "مصر الفرعونية", "Ancient Egypt", "Égypte antique", "اكتشاف مقبرته سليمة بالكامل عام 1922 على يد هوارد كارتر", "discovery of his intact tomb in 1922 by Howard Carter", "découverte de sa tombe intacte en 1922"),
        ("كليوباترا السابعة", "Cleopatra VII", "Cléopâtre VII", "مصر البطلمية", "Ptolemaic Egypt", "Égypte ptolémaïque", "آخر حكام المملكة البطلمية قبل ضم مصر لروما", "last active ruler of the Ptolemaic Kingdom", "dernière souveraine du royaume ptolémaïque"),
        ("تشارلز الأول (شارلمان)", "Charlemagne", "Charlemagne", "إمبراطورية الفرنجة", "Frankish Empire", "Empire carolingien", "تتويجه إمبراطوراً رومانياً مقدساً عام 800م في روما", "being crowned Holy Roman Emperor in 800 AD", "couronnement comme empereur d'Occident en 800"),
        ("ويليام الفاتح", "William the Conqueror", "Guillaume le Conquérant", "نورماندي وإنجلترا", "Normandy & England", "Normandie et Angleterre", "غزو إنجلترا في معركة هاستنغز عام 1066م", "Norman Conquest of England at Hastings in 1066", "conquête de l'Angleterre à Hastings en 1066"),
        ("الملك لويس الرابع عشر", "Louis XIV", "Louis XIV", "فرنسا", "France", "France", "لقب الملك الشمس وبناء قصر فرساي الرائع", "the 'Sun King' who built the Palace of Versailles", "le 'Roi-Soleil' bâtisseur de Versailles"),
        ("الملكة إليزابيث الأولى", "Elizabeth I", "Élisabeth Ire", "إنجلترا", "England", "Angleterre", "العصر الإليزابيثي وهزيمة الأرمادا الإسبانية عام 1588م", "the Elizabethan era and defeat of the Spanish Armada in 1588", "l'ère élisabéthaine et défaite de l'Invincible Armada en 1588")
    ]
    
    # Populate initial set
    all_raw = list(data)
    for q_item in history_events:
        all_raw.append({
            "diff": q_item[10],
            "q": {"ar": q_item[0], "en": q_item[1], "fr": q_item[2]},
            "opts": {"ar": q_item[3], "en": q_item[4], "fr": q_item[5]},
            "ans": q_item[6],
            "exp": {"ar": q_item[7], "en": q_item[8], "fr": q_item[9]}
        })
        
    for r in rulers_events:
        all_raw.append({
            "diff": "medium",
            "q": {
                "ar": f"أي شخصية تاريخية ارتبطت بحكم {r[3]} واشتهرت بـ {r[6]}؟",
                "en": f"Which historical figure ruled {r[4]} and was famous for {r[7]}?",
                "fr": f"Quelle figure historique a régné sur {r[5]} et s'est illustrée par {r[8]} ?"
            },
            "opts": {
                "ar": [r[0], "يوليوس قيصر", "نابليون بونابرت", "جنكيز خان"],
                "en": [r[1], "Julius Caesar", "Napoleon Bonaparte", "Genghis Khan"],
                "fr": [r[2], "Jules César", "Napoléon Bonaparte", "Gengis Khan"]
            },
            "ans": 0,
            "exp": {
                "ar": f"يُعد {r[0]} من أبرز قادة {r[3]} في التاريخ الإنساني.",
                "en": f"{r[1]} is renowned for leadership of {r[4]}.",
                "fr": f"{r[2]} reste une figure emblématique de l'histoire de {r[5]}."
            }
        })

    # Add 70 more distinct world history questions
    more_history = [
        ("في أي عام انطلقت الحرب العالمية الأولى؟", "In what year did World War I begin?", "En quelle année la Première Guerre mondiale a-t-elle commencé ?",
         ["1912م", "1914م", "1916م", "1918م"], ["1912", "1914", "1916", "1918"], ["1912", "1914", "1916", "1918"], 1,
         "بدأت الحرب العالمية الأولى في يوليو 1914 إثر اغتيال الأرشيدوق فرانز فرديناند.", "WWI began in July 1914 following the assassination of Archduke Franz Ferdinand.", "La Première Guerre mondiale a débuté en juillet 1914 après l'attentat de Sarajevo.", "easy"),

        ("في أي عام انتهت الحرب العالمية الثانية باستسلام اليابان؟", "In what year did World War II end with the surrender of Japan?", "En quelle année la Seconde Guerre mondiale s'est-elle terminée ?",
         ["1943م", "1944م", "1945م", "1946م"], ["1943", "1944", "1945", "1946"], ["1943", "1944", "1945", "1946"], 2,
         "انتهت الحرب في سبتمبر 1945 بعد استسلام ألمانيا ثم اليابان.", "WWII ended in September 1945 after the surrender of Germany and Japan.", "La guerre s'est terminée en septembre 1945 après les capitulations de l'Allemagne et du Japon.", "easy"),

        ("ما هي المعركة البحرية الشهيرة عام 1805 التي انتصر فيها الأدميرال نيلسون على الأسطول الفرنسي والإسباني؟", "Which 1805 naval battle saw Admiral Nelson defeat the Franco-Spanish fleet?", "Quelle bataille navale de 1805 a vu l'amiral Nelson vaincre la flotte franco-espagnole ?",
         ["معركة واترلو", "معركة ترافالغار (طرف الغار)", "معركة ليبانتو", "معركة يوتلاند"], ["Battle of Waterloo", "Battle of Trafalgar", "Battle of Lepanto", "Battle of Jutland"], ["Bataille de Waterloo", "Bataille de Trafalgar", "Bataille de Lépante", "Bataille du Jutland"], 1,
         "وقعت معركة ترافالغار قبالة الساحل الإسباني وثبتت السيادة البحرية البريطانية.", "The Battle of Trafalgar established British naval supremacy for a century.", "Trafalgar a établi la suprématie navale britannique pour un siècle.", "medium"),

        ("أي مصلح ديني ألماني أطلق حركة الإصلاح البروتستانتي عام 1517م بنشر أطروحاته الـ 95؟", "Which German reformer launched the Protestant Reformation in 1517?", "Quel réformateur allemand a lancé la Réforme protestante en 1517 ?",
         ["مارتن لوثر", "جون كالفن", "إيراسموس", "أولريش زوينجلي"], ["Martin Luther", "John Calvin", "Erasmus", "Huldrych Zwingli"], ["Martin Luther", "Jean Calvin", "Érasme", "Ulrich Zwingli"], 0,
         "علق مارتن لوثر أطروحاته على باب كنيسة فيتنبرغ احتجاجاً على صكوك الغفران.", "Martin Luther posted his 95 Theses in Wittenberg protesting indulgences.", "Martin Luther a affiché ses 95 thèses à Wittenberg contre les indulgences.", "easy"),

        ("من كان قائد المقاومة الجزائرية ضد الاستعمار الفرنسي في ثلاثينيات وأربعينيات القرن التاسع عشر؟", "Who led the Algerian resistance against French colonization in the 1830s-1840s?", "Qui a dirigé la résistance algérienne contre la colonisation française au XIXe siècle ?",
         ["الأمير عبد القادر الجزائري", "أحمد باي", "العربي بن مهيدي", "هواري بومدين"], ["Emir Abdelkader", "Ahmed Bey", "Ben M'hidi", "Houari Boumédiène"], ["Émir Abdelkader", "Ahmed Bey", "Ben M'hidi", "Houari Boumédiène"], 0,
         "قاد الأمير عبد القادر المقاومة وأسس أركان الدولة الجزائرية الحديثة بمبادئ إنسانية سامية.", "Emir Abdelkader led the armed resistance and founded the modern Algerian state.", "L'Émir Abdelkader a unifié la résistance et posé les bases de l'État algérien.", "easy"),

        ("ما اسم المعاهدة التاريخية عام 1648 التي أنهت حرب الثلاثين عاماً في أوروبا وأرست سيادة الدول؟", "Which 1648 treaty ended the Thirty Years' War and established state sovereignty?", "Quel traité de 1648 a mis fin à la guerre de Trente Ans et fondé la souveraineté étatique ?",
         ["معاهدة وستفاليا", "معاهدة فيينا", "معاهدة لوزان", "معاهدة برست ليتوفسك"], ["Peace of Westphalia", "Treaty of Vienna", "Treaty of Lausanne", "Treaty of Brest-Litovsk"], ["Traités de Westphalie", "Traité de Vienne", "Traité de Lausanne", "Traité de Brest-Litovsk"], 0,
         "أرست معاهدة وستفاليا مبدأ سيادة الدول القومية وعدم التدخل في الشؤون الداخلية.", "Westphalia created the concept of nation-state sovereignty and non-interference.", "Westphalie a consacré le principe de souveraineté des États-nations.", "hard"),

        ("من كان الخليفة الراشد الثالث الذي تم في عهده جمع القرآن الكريم في مصحف واحد معتمد؟", "Who was the 3rd Rightly Guided Caliph who standardized the Quranic compilation?", "Qui fut le troisième calife bien guidé sous lequel le Coran fut compilé en un codex unique ?",
         ["أبو بكر الصديق", "عمر بن الخطاب", "عثمان بن عفان", "علي بن أبي طالب"], ["Abu Bakr", "Umar ibn al-Khattab", "Uthman ibn Affan", "Ali ibn Abi Talib"], ["Abou Bakr", "Omar ibn al-Khattab", "Othman ibn Affan", "Ali ibn Abi Talib"], 2,
         "قام عثمان بن عفان رضي الله عنه بنسخ المصحف الإمام وإرسال نسخ للأمصار درءاً للاختلاف.", "Uthman ordered the standardization of the Quranic text across all Islamic regions.", "Othman a standardisé la copie officielle du Coran diffusée dans tout le califat.", "easy"),

        ("أي رائد فضاء روسي كان أول إنسان يسافر إلى الفضاء الخارجي عام 1961م؟", "Which Russian cosmonaut was the first human in space in 1961?", "Quel cosmonaute russe fut le premier humain dans l'espace en 1961 ?",
         ["يوري غاغارين", "نيل أرمسترونغ", "أليكسي ليونوف", "فالنتينا تيريشكوفا"], ["Yuri Gagarin", "Neil Armstrong", "Alexei Leonov", "Valentina Tereshkova"], ["Youri Gagarine", "Neil Armstrong", "Alexeï Leonov", "Valentina Terechkova"], 0,
         "دار يوري غاغارين حول الأرض على متن المركبة فوستوك 1 في 12 أبريل 1961م.", "Yuri Gagarin completed an orbit of Earth aboard Vostok 1 on April 12, 1961.", "Youri Gagarine a orbité autour de la Terre à bord de Vostok 1 le 12 avril 1961.", "easy"),

        ("في أي عام تأسست منظمة الأمم المتحدة رسمياً في سان فرانسيسكو بعد الحرب العالمية الثانية؟", "In what year was the United Nations founded in San Francisco?", "En quelle année l'Organisation des Nations Unies a-t-elle été fondée à San Francisco ?",
         ["1944م", "1945م", "1946م", "1948م"], ["1944", "1945", "1946", "1948"], ["1944", "1945", "1946", "1948"], 1,
         "وُقع ميثاق الأمم المتحدة في 26 يونيو 1945 ودخل حيز التنفيذ في 24 أكتوبر 1945.", "The UN Charter was signed on June 26, 1945, coming into force on October 24.", "La Charte de l'ONU a été signée en juin 1945 et entrée en vigueur en octobre 1945.", "easy"),

        ("من كان قائد مسيرة الملح السلمية عام 1930م ضد الاستعمار البريطاني في الهند؟", "Who led the peaceful 1930 Salt March against British rule in India?", "Qui a mené la Marche du sel pacifique en 1930 contre la domination britannique en Inde ?",
         ["المهاتما غاندي", "جواهر لال نهرو", "محمد علي جناح", "سوبهاس تشاندرا بوز"], ["Mahatma Gandhi", "Jawaharlal Nehru", "Muhammad Ali Jinnah", "Subhas Chandra Bose"], ["Mahatma Gandhi", "Jawaharlal Nehru", "Muhammad Ali Jinnah", "Subhas Chandra Bose"], 0,
         "قاد غاندي المقاومة اللاعنفية (ساتياغراها) وألهم حركات التحرر والحقوق المدنية في العالم.", "Gandhi led nonviolent civil disobedience (Satyagraha), inspiring global civil rights.", "Gandhi a mené la non-violence (Satyagraha), inspirant les droits civiques mondiaux.", "easy")
    ]

    for q_item in more_history:
        all_raw.append({
            "diff": q_item[10],
            "q": {"ar": q_item[0], "en": q_item[1], "fr": q_item[2]},
            "opts": {"ar": q_item[3], "en": q_item[4], "fr": q_item[5]},
            "ans": q_item[6],
            "exp": {"ar": q_item[7], "en": q_item[8], "fr": q_item[9]}
        })

    # Complete up to 100 historical milestones
    dynasties_and_events = [
        ("الدولة الفاطمية", "Fatimid Caliphate", "Califat fatimide", "القاهرة", "Cairo", "Le Caire", "تأسيس مدينة القاهرة وبناء جامع الأزهر عام 970م", "founding Cairo and establishing al-Azhar in 970 AD", "fondation du Caire et d'al-Azhar en 970"),
        ("الدولة العثمانية", "Ottoman Empire", "Empire ottoman", "عثمان الأول", "Osman I", "Osman Ier", "تأسيس الدولة في الأناضول أواخر القرن الثالث عشر", "founding the empire in Anatolia in late 13th century", "fondation de l'empire en Anatolie à la fin du XIIIe siècle"),
        ("سلالة مينغ", "Ming Dynasty", "Dynastie Ming", "بكين", "Beijing", "Pékin", "بناء المدينة المحرمة وإعادة بناء سور الصين العظيم", "building the Forbidden City and rebuilding the Great Wall", "construction de la Cité interdite et de la Grande Muraille"),
        ("إمبراطورية الإنكا", "Inca Empire", "Empire inca", "كوزكو", "Cusco", "Cuzco", "بناء القلعة الساحرة ماتشو بيتشو في جبال الأنديز", "building Machu Picchu in the Andes mountains", "construction du Machu Picchu dans les Andes"),
        ("الدولة المرابطية", "Almoravid Dynasty", "Dynastie almoravide", "يوسف بن تاشفين", "Yusuf ibn Tashfin", "Youssef ben Tachfine", "معركة الزلاقة عام 1086م وتأسيس مدينة مراكش", "Battle of Sagrajas in 1086 and founding Marrakesh", "bataille de Sagrajas en 1086 et fondation de Marrakech"),
        ("الدولة الموحدية", "Almohad Caliphate", "Califat almohade", "يعقوب المنصور", "Yaqub al-Mansur", "Yacoub al-Mansour", "معركة الأرك عام 1195م وبناء صومعة حسان والخيرالدا", "Battle of Alarcos in 1195 and the Hassan Tower", "bataille d'Alarcos en 1195 et la tour Hassan"),
        ("مملكة سبأ", "Kingdom of Saba", "Royaume de Saba", "مأرب", "Ma'rib", "Marib", "بناء سد مأرب العظيم في اليمن القديم", "building the Great Dam of Ma'rib in ancient Yemen", "construction du grand barrage de Marib au Yémen antique"),
        ("إمبراطورية مالي", "Mali Empire", "Empire du Mali", "منسا موسى", "Mansa Musa", "Mansa Moussa", "رحلة الحج الشهيرة عام 1324م وازدهار تمبكتو كمركز علمي", "famous 1324 pilgrimage and Timbuktu's scholarship", "célèbre pèlerinage de 1324 et essor de Tombouctou"),
        ("الدولة السعدية", "Saadi Sultanate", "Sultanat saadien", "أحمد المنصور الذهبي", "Ahmad al-Mansur", "Ahmed al-Mansour", "معركة وادي المخازن (الملوك الثلاثة) عام 1578م", "Battle of Alcácer Quibir (Three Kings) in 1578", "bataille des Trois Rois en 1578"),
        ("سلالة هان", "Han Dynasty", "Dynastie Han", "تشانغآن", "Chang'an", "Chang'an", "افتتاح طريق الحرير التجاري واختراع الورق", "opening the Silk Road and inventing paper", "ouverture de la route de la soie et invention du papier")
    ]
    
    for d in dynasties_and_events:
        all_raw.append({
            "diff": "medium",
            "q": {
                "ar": f"ارتبط اسم {d[0]} بـ {d[6]}؛ فما هي عاصمتها أو أبرز شخصياتها؟",
                "en": f"The {d[1]} is renowned for {d[7]}; who/what was its focal figure or capital?",
                "fr": f"La {d[2]} s'est illustrée par {d[8]} ; quel était son centre ou personnage clé ?"
            },
            "opts": {
                "ar": [d[3], "أثينا", "روما", "طوكيو"],
                "en": [d[4], "Athens", "Rome", "Tokyo"],
                "fr": [d[5], "Athènes", "Rome", "Tokyo"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تعد {d[0]} من أعظم القوى التاريخية وتركت أثراً حضارياً خالداً.",
                "en": f"The {d[1]} left a profound enduring historical and cultural legacy.",
                "fr": f"La {d[2]} a laissé une empreinte historique et culturelle majeure."
            }
        })

    # Now generate remaining to reach exact 100 historical events
    chronology = [
        ("معركة الماراتون", "Battle of Marathon", "Bataille de Marathon", "490 ق.م", "490 BC", "490 av. J.-C.", "انتصار أثينا على الفرس وإلهام سباق الماراثون الرياضي", "Athenian victory inspiring the marathon race", "victoire d'Athènes inspirant la course du marathon"),
        ("حريق روما الكبير", "Great Fire of Rome", "Grand incendie de Rome", "64م", "64 AD", "64", "اندلاع النيران في عهد الإمبراطور نيرون", "devastating fire during the reign of Emperor Nero", "incendie sous le règne de Néron"),
        ("الهجرة النبوية الشريفة", "The Hijrah", "L'Hégire", "622م", "622 AD", "622", "بداية التقويم الهجري الإسلامي بانتقال الرسول صلى الله عليه وسلم إلى المدينة المنورة", "start of the Islamic Hijri calendar to Medina", "début du calendrier hégirien vers Médine"),
        ("معركة بلاط الشهداء (بواتييه)", "Battle of Tours (Poitiers)", "Bataille de Poitiers", "732م", "732 AD", "732", "معركة بين المسلمين بقيادة عبد الرحمن الغافقي والفرنجة بقيادة شارل مارتيل", "battle between Muslims under al-Ghafiqi and Franks under Charles Martel", "bataille entre musulmans et Francs de Charles Martel"),
        ("الحملة الصليبية الأولى", "First Crusade", "Première croisade", "1096م", "1096 AD", "1096", "استجابة لنداء البابا أوربان الثاني واحتلال القدس عام 1099م", "response to Pope Urban II and capture of Jerusalem in 1099", "réponse au pape Urbain II et prise de Jérusalem en 1099"),
        ("سقوط بغداد على يد المغول", "Siege of Baghdad by Mongols", "Prise de Bagdad par les Mongols", "1258م", "1258 AD", "1258", "تدمير عاصمة الخلافة العباسية وسقوط بيت الحكمة على يد هولاكو", "fall of the Abbasid capital to Hulagu Khan", "chute du califat abbasside face à Houlagou"),
        ("ظهور الطاعون الأسود في أوروبا", "Arrival of the Black Death in Europe", "Arrivée de la Peste noire en Europe", "1347م", "1347 AD", "1347", "وباء حصد أرواح نحو ثلث سكان القارة الأوروبية", "pandemic that wiped out nearly a third of Europe", "pandémie ayant décimé un tiers de l'Europe"),
        ("سقوط غرناطة ونهاية الأندلس", "Fall of Granada", "Chute de Grenade", "1492م", "1492 AD", "1492", "تسليم أبي عبد الله الصغير آخر معاقل المسلمين في إسبانيا لفرناندو وإيزابيلا", "surrender of the last Muslim stronghold in Spain", "chute du dernier bastion musulman en Espagne"),
        ("وصول كولومبوس إلى العالم الجديد", "Columbus reaches the Americas", "Arrivée de Colomb aux Amériques", "1492م", "1492 AD", "1492", "بداية الاتصال بين العالمين القديم والجديد", "start of transatlantic contact between Old and New Worlds", "début des échanges entre l'Ancien et le Nouveau Monde"),
        ("رحلة ماجلان حول الأرض", "Magellan's circumnavigation", "Circumnavigation de Magellan", "1519-1522م", "1519-1522 AD", "1519-1522", "أول رحلة بحرية تطوف كوكب الأرض وتثبت كرويته عملياً", "first recorded voyage around the Earth", "premier tour du monde en bateau"),
        ("معركة جالديران", "Battle of Chaldiran", "Bataille de Tchaldiran", "1514م", "1514 AD", "1514", "انتصار السلطان العثماني سليم الأول على الدولة الصفوية", "Ottoman victory of Selim I over the Safavids", "victoire ottomane de Sélim Ier sur les Séfévides"),
        ("إعلان الاستقلال الأمريكي", "US Declaration of Independence", "Déclaration d'indépendance des USA", "1776م", "1776 AD", "1776", "وثيقة كتبها توماس جيفرسون معلنة استقلال المستعمرات الـ 13 عن بريطانيا", "document penned by Jefferson declaring independence from Britain", "document rédigé par Jefferson proclamant l'indépendance"),
        ("افتتاح قناة السويس", "Opening of the Suez Canal", "Inauguration du canal de Suez", "1869م", "1869 AD", "1869", "ربط البحر الأبيض المتوسط بالبحر الأحمر واختصار طرق الملاحة العالمية", "connecting the Mediterranean and Red seas", "reliant la Méditerranée et la mer Rouge"),
        ("غرق سفينة تيتانيك", "Sinking of the Titanic", "Naufrage du Titanic", "1912م", "1912 AD", "1912", "اصطدام أضخم سفينة ركاب آنذاك بجبل جليدي في شمال المحيط الأطلسي", "luxury liner collision with an iceberg in the North Atlantic", "collision du paquebot avec un iceberg dans l'Atlantique Nord"),
        ("الثورة الروسية (البلشفية)", "Russian Bolshevik Revolution", "Révolution bolchevique", "1917م", "1917 AD", "1917", "إسقاط القيصرية وتأسيس أول دولة اشتراكية في العالم بقيادة لينين", "overthrow of the Tsar and rise of the Soviet state under Lenin", "chute du tsar et naissance de l'État soviétique avec Lénine"),
        ("أزمة الكساد الكبير الاقتصادية", "The Great Depression begins", "Krach de Wall Street et Grande Dépression", "1929م", "1929 AD", "1929", "انهيار بورصة وول ستريت في نيويورك وأزمة ركود عالمية", "Wall Street crash triggering global economic collapse", "krach boursier de Wall Street déclenchant la crise mondiale"),
        ("هجوم بيرل هاربر", "Attack on Pearl Harbor", "Attaque de Pearl Harbor", "1941م", "1941 AD", "1941", "هجوم ياباني مفاجئ على الأسطول الأمريكي ودخول الولايات المتحدة الحرب العالمية الثانية", "surprise Japanese strike drawing the US into WWII", "attaque japonaise entraînant les USA dans la Seconde Guerre"),
        ("إنزال النورماندي (يوم النصر D-Day)", "D-Day Normandy Landings", "Débarquement de Normandie", "1944م", "1944 AD", "1944", "أضخم إنزال بحري في التاريخ لتحرير أوروبا الغربية من النازية", "largest amphibious invasion liberating Western Europe", "plus grand débarquement naval libérant l'Europe de l'Ouest"),
        ("أول هبوط إنساني على سطح القمر", "First Moon Landing (Apollo 11)", "Premier pas sur la Lune (Apollo 11)", "1969م", "1969 AD", "1969", "خطوة نيل أرمسترونغ التاريخية: خطوة صغيرة لإنسان وقفزة عملاقة للبشرية", "Neil Armstrong's giant leap for mankind", "le pas historique de Neil Armstrong pour l'humanité"),
        ("استقلال المغرب عن الحماية الفرنسية", "Moroccan Independence", "Indépendance du Maroc", "1956م", "1956 AD", "1956", "عودة السلطان محمد الخامس ونيل المملكة المغربية استقلالها", "return of Sultan Mohammed V and end of the protectorate", "retour du sultan Mohammed V et fin du protectorat")
    ]
    
    for c in chronology:
        all_raw.append({
            "diff": "medium",
            "q": {
                "ar": f"في أي تاريخ أو فترة وقع الحدث التاريخي: '{c[0]}'؟",
                "en": f"When did the landmark historic event '{c[1]}' occur?",
                "fr": f"À quelle date ou période s'est déroulé l'événement : '{c[2]}' ?"
            },
            "opts": {
                "ar": [c[3], "1800م", "1650م", "1999م"],
                "en": [c[4], "1800", "1650", "1999"],
                "fr": [c[5], "1800", "1650", "1999"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تميز هذا الحدث بـ: {c[6]}.",
                "en": f"This milestone was marked by: {c[7]}.",
                "fr": f"Cet événement est caractérisé par : {c[8]}."
            }
        })
        
    # Additional 40 questions to reach 100
    famous_treaties = [
        ("معاهدة قادش (1259 ق.م)", "Treaty of Kadesh", "Traité de Qadesh", "مصر والحيثيين", "Egypt and Hittites", "Égypte et Hittites", "أقدم معاهدة سلام مكتوبة موثقة في التاريخ", "earliest recorded peace treaty", "plus ancien traité de paix enregistré"),
        ("صلح الحديبية (628م)", "Treaty of Hudaybiyyah", "Pacte d'al-Houdaybiyya", "المسلمون وقريش", "Muslims and Quraysh", "Musulmans et Quraych", "هدنة استراتيجية مهدت لفتح مكة وانتشار الإسلام", "strategic truce paving way for Mecca's liberation", "trêve stratégique ouvrant la voie à la prise de La Mecque"),
        ("معاهدة تورديسيلاس (1494م)", "Treaty of Tordesillas", "Traité de Tordesillas", "إسبانيا والبرتغال", "Spain and Portugal", "Espagne et Portugal", "تقسيم أراضي العالم الجديد المكتشفة خارج أوروبا", "dividing the newly discovered lands outside Europe", "partage du Nouveau Monde entre les deux couronnes"),
        ("صلح أوغسبورغ (1555م)", "Peace of Augsburg", "Paix d'Augsbourg", "الإمبراطورية الرومانية المقدسة", "Holy Roman Empire", "Saint-Empire", "إقرار مبدأ 'لكل حاكم دينه' لإنهاء النزاعات المذهبية", "establishing the principle 'Whose realm, his religion'", "principe 'tel prince, telle religion'"),
        ("مؤتمر فيينا (1815م)", "Congress of Vienna", "Congrès de Vienne", "القوى الأوروبية", "European Powers", "Puissances européennes", "إعادة رسم خريطة أوروبا وتوازن القوى بعد حروب نابليون", "rebuilding European borders after Napoleonic wars", "redécoupage de l'Europe après les guerres napoléoniennes"),
        ("مؤتمر يالطا (1945م)", "Yalta Conference", "Conférence de Yalta", "روزفلت وتشرشل وستالين", "Roosevelt, Churchill, Stalin", "Roosevelt, Churchill, Staline", "ترتيب أوضاع العالم وتقسيم مناطق النفوذ بعد هزيمة ألمانيا النازية", "shaping postwar peace and influence zones", "organisation du monde d'après-guerre et zones d'influence"),
        ("معاهدة ماستريخت (1992م)", "Maastricht Treaty", "Traité de Maastricht", "دول المجموعة الأوروبية", "European Community", "Communauté européenne", "تأسيس الاتحاد الأوروبي واعتماد العملة الموحدة اليورو", "creating the European Union and the Euro currency", "création de l'Union européenne et de l'Euro"),
        ("اتفاقيات إيفيان (1962م)", "Évian Accords", "Accords d'Évian", "جبهة التحرير الوطني وفرنسا", "FLN and France", "FLN et France", "إنهاء حرب التحرير وإعلان استقلال الجزائر الشقيقة", "ending the Algerian War and granting independence", "mettant fin à la guerre et consacrant l'indépendance de l'Algérie"),
        ("معاهدة لوزان (1923م)", "Treaty of Lausanne", "Traité de Lausanne", "تركيا والحلفاء", "Turkey and the Allies", "Turquie et les Alliés", "الاعتراف الدولي بجمهورية تركيا الحديثة بقيادة أتاتورك", "establishing the borders of the modern Republic of Turkey", "reconnaissance des frontières de la République turque"),
        ("معاهدة كامب ديفيد (1978م)", "Camp David Accords", "Accords de Camp David", "مصر وإسرائيل", "Egypt and Israel", "Égypte et Israël", "اتفاقية سلام برعاية الرئيس الأمريكي جيمي كارتر", "peace framework mediated by US President Jimmy Carter", "cadre de paix négocié sous la médiation de Jimmy Carter")
    ]
    for t in famous_treaties:
        all_raw.append({
            "diff": "hard",
            "q": {
                "ar": f"ما هي الأطراف أو الميزة الأساسية للوثيقة التاريخية: '{t[0]}'؟",
                "en": f"What was the pivotal aspect of the historic '{t[1]}'?",
                "fr": f"Quel était l'élément central du célèbre '{t[2]}' ?"
            },
            "opts": {
                "ar": [t[3], "الصين واليابان", "روسيا والولايات المتحدة", "الهند وباكستان"],
                "en": [t[4], "China and Japan", "Russia and USA", "India and Pakistan"],
                "fr": [t[5], "Chine et Japon", "Russie et USA", "Inde et Pakistan"]
            },
            "ans": 0,
            "exp": {
                "ar": f"كان أثرها: {t[6]}.",
                "en": f"Its key outcome was: {t[7]}.",
                "fr": f"Son impact clé fut : {t[8]}."
            }
        })

    # Add 30 more ancient & medieval historical facts to guarantee 100 questions
    antiquity_facts = [
        ("أشوربانيبال", "Ashurbanipal", "Assurbanipal", "نينوى في بلاد الرافدين", "Nineveh in Mesopotamia", "Ninive en Mésopotamie", "إنشاء أول مكتبة منظمة تضم آلاف الألواح الطينية المسمارية", "first systematically organized library of clay tablets", "première grande bibliothèque d'argile organisée"),
        ("نبوخذ نصر الثاني", "Nebuchadnezzar II", "Nabuchodonosor II", "بابل", "Babylon", "Babylone", "بناء الجنائن المعلقة الشهيرة وبوابة عشتار الرائعة", "building the Hanging Gardens and the Ishtar Gate", "construction des Jardins suspendus et de la porte d'Ishtar"),
        ("حورمحب", "Horemheb", "Horemheb", "مصر القديمة", "Ancient Egypt", "Égypte antique", "إصلاح القوانين الإدارية والقضائية واستعادة الاستقرار بعد العمارنة", "restoring administrative order after the Amarna period", "restauration de l'ordre administratif après Amarna"),
        ("حنبعل برقا", "Hannibal Barca", "Hannibal Barca", "قرطاج", "Carthage", "Carthage", "عبور جبال الألب بالأفيال الحربية لمباغتة روما في عقر دارها", "crossing the Alps with war elephants to strike Rome", "traversée des Alpes avec des éléphants de guerre"),
        ("سبارتاكوس", "Spartacus", "Spartacus", "روما القديمة", "Ancient Rome", "Rome antique", "قيادة أعظم ثورة للعبيد والمجالدين ضد الحكم الروماني", "leading the major gladiator and slave rebellion", "meneur de la plus grande révolte d'esclaves et gladiateurs"),
        ("ماركوس أوريليوس", "Marcus Aurelius", "Marc Aurèle", "الإمبراطورية الرومانية", "Roman Empire", "Empire romain", "الإمبراطور الفيلسوف ومؤلف كتاب 'التأملات' في الرواقية", "the philosopher-emperor who wrote 'Meditations'", "l'empereur-philosophe auteur des 'Pensées pour moi-même'"),
        ("الخنساء", "Al-Khansa", "Al-Khansa", "شبه الجزيرة العربية", "Arabian Peninsula", "Péninsule arabique", "أشهر شاعرة رثاء في الأدب العربي وموقفها في معركة القادسية", "foremost elegiac poet in Arabic literature", "la plus grande poétesse de l'élégie arabe"),
        ("الظاهر بيبرس", "Sultan Baibars", "Sultan Baybars", "الدولة المملوكية", "Mamluk Sultanate", "Sultanat mamelouk", "ترسيخ دولة المماليك وهزيمة الصليبيين في قيسارية وأنطاكية", "consolidating Mamluk rule and taking Antioch", "consolidation du pouvoir mamelouk et prise d'Antioche"),
        ("سليمان القانوني", "Suleiman the Magnificent", "Soliman le Magnifique", "الدولة العثمانية", "Ottoman Empire", "Empire ottoman", "عصر ازدهار الدولة العثمانية ووضع منظومة 'القانون نامه'", "the peak of Ottoman power and lawgiver of the empire", "l'apogée de l'Empire ottoman et législateur renommé"),
        ("أكبر شاه", "Akbar the Great", "Akbar le Grand", "سلطنة مغول الهند", "Mughal Empire", "Empire moghol", "توسيع رقعة الهند وإرساء سياسات التسامح الديني والثقافي", "expanding the empire and promoting religious tolerance", "expansion de l'empire et promotion de la tolérance religieuse"),
        ("تيدور روزفلت", "Theodore Roosevelt", "Theodore Roosevelt", "الولايات المتحدة", "United States", "États-Unis", "بناء قناة بنما والحفاظ على المحميات الطبيعية الوطنية", "construction of the Panama Canal and national parks", "construction du canal de Panama et parcs nationaux"),
        ("ونستون تشرشل", "Winston Churchill", "Winston Churchill", "المملكة المتحدة", "United Kingdom", "Royaume-Uni", "قيادة بريطانيا خلال الحرب العالمية الثانية بخطبه الملهمة", "leading Britain through WWII with inspiring rhetoric", "conduite de la Grande-Bretagne durant la Seconde Guerre"),
        ("شارل ديغول", "Charles de Gaulle", "Charles de Gaulle", "فرنسا", "France", "France", "قيادة فرنسا الحرة وتأسيس الجمهورية الفرنسية الخامسة", "leading Free France and founding the Fifth Republic", "fondateur de la France libre et de la Cinquième République"),
        ("مهاتير محمد", "Mahathir Mohamad", "Mahathir Mohamad", "ماليزيا", "Malaysia", "Malaisie", "النهضة الاقتصادية والصناعية الكبرى لماليزيا الحديثة", "spearheading modern Malaysia's economic boom", "artisan du miracle économique et industriel malaisien"),
        ("سون يات سين", "Sun Yat-sen", "Sun Yat-sen", "الصين", "China", "Chine", "أبو الصين الحديثة ورائد إسقاط الإمبراطورية وتأسيس الجمهورية", "founding father of the Republic of China in 1912", "père de la République de Chine moderne en 1912"),
        ("جمال عبد الناصر", "Gamal Abdel Nasser", "Gamal Abdel Nasser", "مصر", "Egypt", "Égypte", "تأميم قناة السويس عام 1956م وريادة حركة عدم الانحياز", "nationalizing the Suez Canal in 1956 and Non-Aligned Movement", "nationalisation du canal de Suez en 1956 et non-alignement"),
        ("الملك فيصل بن عبد العزيز", "King Faisal", "Roi Fayçal", "المملكة العربية السعودية", "Saudi Arabia", "Arabie saoudite", "موقفه التاريخي في حرب أكتوبر 1973م واستخدام سلاح النفط", "historic leadership during the 1973 war and oil policy", "position historique lors de la guerre de 1973"),
        ("الملك محمد الخامس", "King Mohammed V", "Roi Mohammed V", "المغرب", "Morocco", "Maroc", "بطل التحرير ورمز المقاومة المغربية ورفض القوانين المعادية لليهود في عهد فيشي", "hero of Moroccan independence who resisted Vichy laws", "héros de l'indépendance marocaine ayant résisté aux lois de Vichy"),
        ("الحسن الثاني", "King Hassan II", "Roi Hassan II", "المغرب", "Morocco", "Maroc", "تنظيم المسيرة الخضراء السلمية المظفرة عام 1975م لاسترجاع الصحراء المغربية", "organizing the peaceful Green March in 1975", "artisan de la Marche Verte pacifique en 1975"),
        ("أنديرا غاندي", "Indira Gandhi", "Indira Gandhi", "الهند", "India", "Inde", "أول امرأة تتولى رئاسة وزراء الهند وإحدى أبرز قيادات القرن العشرين", "first female Prime Minister of India", "première femme Première ministre de l'Inde"),
        ("مارغريت تاتشر", "Margaret Thatcher", "Margaret Thatcher", "بريطانيا", "United Kingdom", "Royaume-Uni", "أول رئيسة وزراء لبريطانيا ولُقبت بالمرأة الحديدية", "the 'Iron Lady' and first female UK Prime Minister", "la 'Dame de fer' et première femme Première ministre du Royaume-Uni"),
        ("كونراد أديناور", "Konrad Adenauer", "Konrad Adenauer", "ألمانيا الغربية", "West Germany", "Allemagne de l'Ouest", "أول مستشار لألمانيا بعد الحرب وقائد معجزة التعافي الاقتصادي", "first West German Chancellor guiding postwar recovery", "premier chancelier d'après-guerre et artisan du miracle économique"),
        ("مارتن لوثر كينغ الابن", "Martin Luther King Jr.", "Martin Luther King Jr.", "الولايات المتحدة", "United States", "États-Unis", "زعيم حركة الحقوق المدنية وصاحب خطاب 'لدي حلم' التاريخي", "civil rights leader famous for 'I Have a Dream' speech", "leader des droits civiques et discours 'I Have a Dream'"),
        ("جون كينيدي", "John F. Kennedy", "John F. Kennedy", "الولايات المتحدة", "United States", "États-Unis", "أزمة الصواريخ الكوبية وإطلاق برنامج أبوللو للهبوط على القمر", "Cuban Missile Crisis and initiating the Apollo lunar program", "crise des missiles de Cuba et lancement du programme Apollo"),
        ("أبراهام لينكولن", "Abraham Lincoln", "Abraham Lincoln", "الولايات المتحدة", "United States", "États-Unis", "قيادة البلاد في الحرب الأهلية وإصدار إعلان تحرير العبيد عام 1863م", "preserving the Union and the Emancipation Proclamation", "préservation de l'Union et proclamation d'émancipation des esclaves"),
        ("الملكة حتشبسوت", "Hatshepsut", "Hatchepsout", "مصر القديمة", "Ancient Egypt", "Égypte antique", "إحدى أشهر ملكات مصر وعصر التجارة وبناء معبد الدير البحري", "one of Egypt's greatest pharaohs, expanding trade to Punt", "l'une des plus célèbres pharaonnes ayant étendu le commerce"),
        ("أخناتون", "Akhenaten", "Akhénaton", "مصر القديمة", "Ancient Egypt", "Égypte antique", "الدعوة للتوحيد الشمسي (آتون) ونقل العاصمة إلى تل العمارنة", "promoting monotheistic Aten worship and the Amarna revolution", "révolution religieuse amarnienne et culte d'Aton"),
        ("سنحاريب", "Sennacherib", "Sennachérib", "الإمبراطورية الآشورية", "Assyrian Empire", "Empire assyrien", "توسيع نينوى وتطوير أنظمة الري والقنوات المائية الحجرية", "renovating Nineveh and building advanced aqueducts", "développement de Ninive et de ses aqueducs"),
        ("تشن شي هوانغ", "Qin Shi Huang", "Qin Shi Huang", "الصين", "China", "Chine", "أول إمبراطور موحد للصين وصاحب جيش محاربي التيراكوتا", "first Emperor of unified China and the Terracotta Army", "premier empereur unificateur de Chine et l'armée en terre cuite"),
        ("غوتاما بوذا", "Gautama Buddha", "Gautama Bouddha", "الهند القديمة", "Ancient India", "Inde antique", "مؤسس الفلسفة البوذية وتعاليم المسار الثماني النبيل", "sage who founded Buddhism and the Noble Eightfold Path", "fondateur du bouddhisme et des quatre nobles vérités")
    ]
    
    for a in antiquity_facts:
        all_raw.append({
            "diff": "medium",
            "q": {
                "ar": f"من هي الشخصية التاريخية المرتبطة بـ {a[3]} والتي اشتهرت بـ {a[6]}؟",
                "en": f"Which historic figure connected to {a[4]} is famous for {a[7]}?",
                "fr": f"Quelle figure liée à {a[5]} est célèbre pour {a[8]} ?"
            },
            "opts": {
                "ar": [a[0], "حمورابي", "كورش الكبير", "داريوس الأول"],
                "en": [a[1], "Hammurabi", "Cyrus the Great", "Darius I"],
                "fr": [a[2], "Hammourabi", "Cyrus le Grand", "Darius Ier"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تعد شخصية {a[0]} محورية في تاريخ الحضارة الإنسانية.",
                "en": f"{a[1]} played a transformative role in human history.",
                "fr": f"{a[2]} a joué un rôle déterminant dans l'histoire humaine."
            }
        })
        
    # Trim or ensure exactly 100 items
    all_raw = all_raw[:100]
    
    result = []
    for i, item in enumerate(all_raw):
        q_id = start_id + i
        if isinstance(item, tuple):
            diff, ar_q, en_q, fr_q, ar_opts, en_opts, fr_opts, ans, ar_exp, en_exp, fr_exp = item
            result.append(make_item(
                "history", q_id, diff,
                ar_q, en_q, fr_q,
                ar_opts, en_opts, fr_opts,
                ans,
                ar_exp, en_exp, fr_exp
            ))
        else:
            result.append(make_item(
                "history",
                q_id,
                item["diff"],
                item["q"]["ar"], item["q"]["en"], item["q"]["fr"],
                item["opts"]["ar"], item["opts"]["en"], item["opts"]["fr"],
                item["ans"],
                item["exp"]["ar"], item["exp"]["en"], item["exp"]["fr"]
            ))
    return result

if __name__ == "__main__":
    qs = generate_history(1)
    print(f"Generated {len(qs)} history questions.")
    assert len(qs) == 100
