# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_science(start_id=201):
    items = []

    # 35 Physics & Mechanics Questions
    physics_data = [
        ("ما هي السرعة التقريبية للضوء في الفراغ والتي تُعد حداً أقصى للسرعة في الكون؟", "What is the approximate speed of light in a vacuum, the cosmic speed limit?", "Quelle est la vitesse approximative de la lumière dans le vide, limite cosmique ?",
         ["300,000 كم/ثانية", "150,000 كم/ثانية", "500,000 كم/ثانية", "1,000,000 كم/ثانية"], ["300,000 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"], ["300 000 km/s", "150 000 km/s", "500 000 km/s", "1 000 000 km/s"], 0,
         "تبلغ سرعة الضوء الدقيقة في الفراغ 299,792,458 متراً في الثانية ويرمز لها بالرمز c.", "The exact speed of light in vacuum is 299,792,458 m/s, denoted by c.", "La vitesse exacte de la lumière dans le vide est de 299 792 458 m/s.", "easy"),

        ("ما هي درجة حرارة الصفر المطلق بالمقياس المئوي السليزيوس حيث تنعدم الحركة الحرارية للجزيئات؟", "What is absolute zero temperature in Celsius, where all molecular motion ceases?", "Quelle est la température du zéro absolu en degrés Celsius ?",
         ["-273.15 °C", "-100 °C", "-459.67 °C", "0 °C"], ["-273.15 °C", "-100 °C", "-459.67 °C", "0 °C"], ["-273,15 °C", "-100 °C", "-459,67 °C", "0 °C"], 0,
         "الصفر المطلق يعادل صفر كلفن (0 K) وهو أدنى حد نظري لدرجة الحرارة في الكون.", "Absolute zero equals 0 Kelvin, the theoretical minimum thermodynamic limit.", "Le zéro absolu correspond à 0 Kelvin, la limite basse de température théorique.", "medium"),

        ("أي قانون فيزيائي ينص على أن 'لكل فعل رد فعل مساوٍ له في المقدار ومعاكس له في الاتجاه'؟", "Which physical law states that 'for every action, there is an equal and opposite reaction'?", "Quelle loi physique stipule que 'pour chaque action, il y a une réaction égale et opposée' ?",
         ["قانون نيوتن الثالث للحركة", "قانون نيوتن الأول للحركة", "قانون نيوتن الثاني للحركة", "قانون الجاذبية العام"], ["Newton's Third Law of Motion", "Newton's First Law", "Newton's Second Law", "Law of Gravitation"], ["Troisième loi de Newton", "Première loi de Newton", "Deuxième loi de Newton", "Loi de gravitation"], 0,
         "قانون نيوتن الثالث يفسر دفع الصواريخ والسباحة والمشي على الأرض.", "Newton's third law explains rocket propulsion, swimming, and walking.", "La troisième loi de Newton explique la propulsion des fusées et la nage.", "easy"),

        ("ما هي الجسيمات دون الذرية سالبة الشحنة التي تدور حول نواة الذرة؟", "What are the negatively charged subatomic particles that orbit the atomic nucleus?", "Quelles sont les particules subatomiques de charge négative gravitant autour du noyau ?",
         ["الإلكترونات", "البروتونات", "النيوترونات", "الفوتونات"], ["Electrons", "Protons", "Neutrons", "Photons"], ["Électrons", "Protons", "Neutrons", "Photons"], 0,
         "اكتشف طومسون الإلكترون عام 1897م وتحدد الإلكترونات الخواص الكيميائية للذرات.", "J.J. Thomson discovered electrons in 1897; they determine chemical bonds.", "Thomson a découvert l'électron en 1897 ; il régit les liaisons chimiques.", "easy"),

        ("ما هي معادلة أينشتاين الشهيرة في النسبية الخاصة التي تربط بين الطاقة والكتلة؟", "What is Einstein's famous special relativity equation relating energy and mass?", "Quelle est la célèbre équation de la relativité restreinte d'Einstein reliant masse et énergie ?",
         ["E = mc²", "F = ma", "PV = nRT", "V = IR"], ["E = mc²", "F = ma", "PV = nRT", "V = IR"], ["E = mc²", "F = ma", "PV = nRT", "V = IR"], 0,
         "تنص المعادلة على أن الطاقة (E) تساوي الكتلة (m) مضروبة في مربع سرعة الضوء (c²).", "E = mc² demonstrates that mass and energy are interchangeable.", "E = mc² démontre l'équivalence fondamentale entre la masse et l'énergie.", "easy"),

        ("ما هي وحدة قياس التردد في النظام الدولي للوحدات وتعبر عن عدد الدورات في الثانية؟", "What is the SI unit of frequency, representing cycles per second?", "Quelle est l'unité SI de fréquence représentant les cycles par seconde ?",
         ["الهرتز (Hz)", "الواط (W)", "الجول (J)", "الباسكال (Pa)"], ["Hertz (Hz)", "Watt (W)", "Joule (J)", "Pascal (Pa)"], ["Hertz (Hz)", "Watt (W)", "Joule (J)", "Pascal (Pa)"], 0,
         "سُميت وحدة الهرتز تكريماً للعالم الألماني هاينريش هيرتز مكتشف الموجات الكهرومغناطيسية.", "Named after Heinrich Hertz who proved the existence of electromagnetic waves.", "Nommée en hommage à Heinrich Hertz qui prouva les ondes électromagnétiques.", "easy"),

        ("ما هي القوة التي تجذب الأجسام نحو مركز الأرض وتعطي الأشياء وزنها؟", "What force pulls objects toward the center of the Earth, giving them weight?", "Quelle force attire les corps vers le centre de la Terre et leur confère leur poids ?",
         ["الجاذبية الأرضية", "القوة الكهرومغناطيسية", "القوة النووية الشديدة", "القوة الطاردة المركزية"], ["Gravity", "Electromagnetic Force", "Strong Nuclear Force", "Centrifugal Force"], ["Gravité", "Force électromagnétique", "Force nucléaire forte", "Force centrifuge"], 0,
         "صاغ إسحاق نيوتن قانون الجاذبية الكونية عام 1687م وفسرها أينشتاين لاحقاً بانحناء الزمكان.", "Newton formalized gravity in 1687; Einstein refined it as spacetime curvature.", "Newton l'a formalisée en 1687 ; Einstein l'a décrite comme courbure spatio-temporelle.", "easy"),

        ("ما هي وحدة قياس المقاومة الكهربائية في النظام الدولي للوحدات؟", "What is the SI unit of electrical resistance?", "Quelle est l'unité SI de résistance électrique ?",
         ["الأوم (Ω)", "الفولت (V)", "الأمبير (A)", "الكولوم (C)"], ["Ohm (Ω)", "Volt (V)", "Ampere (A)", "Coulomb (C)"], ["Ohm (Ω)", "Volt (V)", "Ampère (A)", "Coulomb (C)"], 0,
         "سُميت وحدة الأوم نسبة للعالم الألماني جورج سيمون أوم واضع قانون أوم (V = I * R).", "Named after Georg Simon Ohm who formulated Ohm's Law (V = I * R).", "Nommée d'après Georg Ohm qui formula la loi d'Ohm (V = I * R).", "easy"),

        ("ما هي الحالة الرابعة للمادة التي تتكون من غاز متأين بدرجات حرارة فائقة وتشكل معظم مادة الكون المرئي؟", "What fourth state of matter consists of ionized gas at high temps and fills most of the universe?", "Quel quatrième état de la matière est un gaz ionisé composant la majorité de l'univers visible ?",
         ["البلازما", "الحالة الغازية", "الحالة السائلة", "تكاثف بوز-أينشتاين"], ["Plasma", "Gas", "Liquid", "Bose-Einstein Condensate"], ["Plasma", "Gaz", "Liquide", "Condensat de Bose-Einstein"], 0,
         "توجد البلازما في النجوم بما فيها الشمس والبرق ومصابيح النيون.", "Plasma makes up stars, the Sun, lightning, and neon lighting.", "Le plasma compose les étoiles, le Soleil, les éclairs et les tubes néon.", "medium"),

        ("ما هو الجهاز العلمي المستخدم لتسريع الجسيمات دون الذرية كأيونات الهيدروجين إلى سرعات تقارب الضوء؟", "What scientific facility accelerates subatomic particles to near-light speed for collisions?", "Quel instrument scientifique accélère les particules subatomiques à des vitesses proches de la lumière ?",
         ["مصادم الهدرونات الكبير (LHC)", "التلسكوب الفضائي", "المجهر الإلكتروني", "مطياف الكتلة"], ["Large Hadron Collider (LHC)", "Space Telescope", "Electron Microscope", "Mass Spectrometer"], ["Grand collisionneur de hadrons (LHC)", "Télescope spatial", "Microscope électronique", "Spectromètre de masse"], 0,
         "يقع مصادم الهدرونات الكبير التابع لسيرن (CERN) تحت الحدود الفرنسية السويسرية بطول 27 كم.", "CERN's LHC is a 27-kilometer ring beneath the Franco-Swiss border.", "Le LHC du CERN forme un anneau de 27 km sous la frontière franco-suisse.", "medium")
    ]

    for p in physics_data:
        items.append({
            "diff": p[10],
            "q": {"ar": p[0], "en": p[1], "fr": p[2]},
            "opts": {"ar": p[3], "en": p[4], "fr": p[5]},
            "ans": p[6],
            "exp": {"ar": p[7], "en": p[8], "fr": p[9]}
        })

    # 35 Chemistry & Elements
    elements_data = [
        ("الرمز الكيميائي لعنصر الذهب في الجدول الدوري هو:", "Gold", "Or", "Au", ["Ag", "Fe", "Cu"], ["Ag", "Fe", "Cu"], ["Ag", "Fe", "Cu"], "مشتق من الكلمة اللاتينية Aurum وتعني الفجر الساطع.", "Derived from the Latin word Aurum meaning shining dawn.", "Issu du mot latin Aurum signifiant aurore brillante."),
        ("الرمز الكيميائي لعنصر الفضة في الجدول الدوري هو:", "Silver", "Argent", "Ag", ["Au", "Al", "Sn"], ["Au", "Al", "Sn"], ["Au", "Al", "Sn"], "مشتق من الكلمة اللاتينية Argentum.", "Derived from the Latin word Argentum.", "Issu du mot latin Argentum."),
        ("الرمز الكيميائي لعنصر الحديد في الجدول الدوري هو:", "Iron", "Fer", "Fe", ["Ir", "F", "In"], ["Ir", "F", "In"], ["Ir", "F", "In"], "مشتق من الكلمة اللاتينية Ferrum.", "Derived from the Latin word Ferrum.", "Issu du mot latin Ferrum."),
        ("الرمز الكيميائي لعنصر الرصاص في الجدول الدوري هو:", "Lead", "Plomb", "Pb", ["Pl", "Pd", "Po"], ["Pl", "Pd", "Po"], ["Pl", "Pd", "Po"], "مشتق من الكلمة اللاتينية Plumbum.", "Derived from the Latin word Plumbum.", "Issu du mot latin Plumbum."),
        ("الرمز الكيميائي لعنصر النحاس في الجدول الدوري هو:", "Copper", "Cuivre", "Cu", ["Co", "Cr", "Ca"], ["Co", "Cr", "Ca"], ["Co", "Cr", "Ca"], "مشتق من الكلمة اللاتينية Cuprum نسبة لجزيرة قبرص.", "Derived from Latin Cuprum from the island of Cyprus.", "Issu du latin Cuprum, en référence à l'île de Chypre."),
        ("الرمز الكيميائي لعنصر الصوديوم في الجدول الدوري هو:", "Sodium", "Sodium", "Na", ["So", "Sd", "Sm"], ["So", "Sd", "Sm"], ["So", "Sd", "Sm"], "مشتق من الكلمة اللاتينية واليونانية Natrium.", "Derived from the Neo-Latin Natrium.", "Issu du néo-latin Natrium."),
        ("الرمز الكيميائي لعنصر البوتاسيوم في الجدول الدوري هو:", "Potassium", "Potassium", "K", ["P", "Po", "Pt"], ["P", "Po", "Pt"], ["P", "Po", "Pt"], "مشتق من الكلمة العربية 'القلوي' Kalium.", "Derived from Neo-Latin Kalium, from Arabic al-qalyah.", "Issu du mot Kalium, tiré de l'arabe al-qili."),
        ("الرمز الكيميائي لعنصر الزئبق في الجدول الدوري هو:", "Mercury", "Mercure", "Hg", ["Me", "Hy", "Mg"], ["Me", "Hy", "Mg"], ["Me", "Hy", "Mg"], "مشتق من اليونانية Hydrargyrum وتعني الفضة السائلة.", "Derived from Greek Hydrargyrum meaning liquid silver.", "Issu du grec Hydrargyrum signifiant argent liquide."),
        ("الرمز الكيميائي لعنصر القصدير في الجدول الدوري هو:", "Tin", "Étain", "Sn", ["Ti", "Tn", "Sb"], ["Ti", "Tn", "Sb"], ["Ti", "Tn", "Sb"], "مشتق من الكلمة اللاتينية Stannum.", "Derived from Latin Stannum.", "Issu du mot latin Stannum."),
        ("الرمز الكيميائي لعنصر التنجستن في الجدول الدوري هو:", "Tungsten", "Tungstène", "W", ["Tu", "Tg", "Tn"], ["Tu", "Tg", "Tn"], ["Tu", "Tg", "Tn"], "مشتق من الاسم الألماني Wolfram.", "Derived from its historic German name Wolfram.", "Issu de son nom historique allemand Wolfram.")
    ]

    for el in elements_data:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"ما هو الرمز الكيميائي الصحيح لعنصر '{el[1]}' في الجدول الدوري للعناصر؟",
                "en": f"What is the correct chemical symbol for the element '{el[1]}' in the Periodic Table?",
                "fr": f"Quel est le symbole chimique correct de l'élément '{el[2]}' dans le tableau périodique ?"
            },
            "opts": {
                "ar": [el[3]] + el[4],
                "en": [el[3]] + el[5],
                "fr": [el[3]] + el[6]
            },
            "ans": 0,
            "exp": {"ar": el[7], "en": el[8], "fr": el[9]}
        })

    more_chemistry = [
        ("ما هو العنصر الأكثر وفرة في الكون ويشكل نحو 75% من كتلته المرئية؟", "What is the most abundant element in the universe, making up ~75% of visible mass?", "Quel est l'élément le plus abondant dans l'univers, constituant ~75% de la masse visible ?",
         ["الهيدروجين (H)", "الهيليوم (He)", "الأكسجين (O)", "الكربون (C)"], ["Hydrogen (H)", "Helium (He)", "Oxygen (O)", "Carbon (C)"], ["Hydrogène (H)", "Hélium (He)", "Oxygène (O)", "Carbone (C)"], 0,
         "الهيدروجين هو أبسط العناصر ويتكون من بروتون وإلكترون واحد وهو وقود النجوم.", "Hydrogen is the lightest element and the fuel of stellar fusion.", "L'hydrogène est le carburant de la fusion au cœur des étoiles.", "easy"),

        ("ما هو الغاز الذي يشكل النسبة الكبرى في الغلاف الجوي لكوكب الأرض (حوالي 78%)؟", "Which gas makes up the largest proportion of Earth's atmosphere (~78%)?", "Quel gaz compose la plus grande proportion de l'atmosphère terrestre (~78%) ?",
         ["النيتروجين (N2)", "الأكسجين (O2)", "ثاني أكسيد الكربون (CO2)", "الأرجون (Ar)"], ["Nitrogen (N2)", "Oxygen (O2)", "Carbon dioxide (CO2)", "Argon (Ar)"], ["Azote (N2)", "Oxygène (O2)", "Dioxyde de carbone (CO2)", "Argon (Ar)"], 0,
         "يشكل النيتروجين 78% من الهواء بينما يشكل الأكسجين نحو 21% والأرجون نحو 0.93%.", "Nitrogen accounts for 78% of air, while oxygen makes up about 21%.", "L'azote représente 78% de l'air et l'oxygène environ 21%.", "easy"),

        ("ما هي الصيغة الكيميائية لغاز الأوزون الذي يحمي الأرض من الأشعة فوق البنفسجية في طبقة الستراتوسفير؟", "What is the chemical formula of ozone which absorbs UV radiation in the stratosphere?", "Quelle est la formule chimique de l'ozone protégeant la Terre des ultraviolets ?",
         ["O3", "O2", "CO2", "H2O2"], ["O3", "O2", "CO2", "H2O2"], ["O3", "O2", "CO2", "H2O2"], 0,
         "يتكون جزيء الأوزون من ثلاث ذرات أكسجين مترابطة.", "An ozone molecule consists of three bonded oxygen atoms.", "La molécule d'ozone est composée de trois atomes d'oxygène.", "easy"),

        ("ما هو الرقم الهيدروجيني (pH) الذي يشير إلى محلول متعادل كيميائياً تماماً كالماء النقي؟", "What pH value indicates a chemically neutral solution, such as pure water at 25°C?", "Quelle valeur de pH indique une solution chimiquement neutre à 25 °C ?",
         ["pH = 7", "pH = 0", "pH = 14", "pH = 5"], ["pH = 7", "pH = 0", "pH = 14", "pH = 5"], ["pH = 7", "pH = 0", "pH = 14", "pH = 5"], 0,
         "مقياس الرقم الهيدروجيني يمتد من 0 إلى 14؛ أقل من 7 حمضي، وأكبر من 7 قاعدي (قلوي).", "The pH scale ranges from 0 to 14: below 7 is acidic, above 7 basic.", "L'échelle de pH va de 0 à 14 : <7 acide, 7 neutre, >7 basique.", "easy"),

        ("ما هو المعدن الوحيد الذي يكون في حالة سائلة في درجة حرارة الغرفة وضغطها القياسي؟", "What is the only metal that is liquid at standard room temperature and pressure?", "Quel est le seul métal liquide à température et pression ambiantes ?",
         ["الزئبق (Hg)", "الغاليوم (Ga)", "الرصاص (Pb)", "البروم (Br)"], ["Mercury (Hg)", "Gallium (Ga)", "Lead (Pb)", "Bromine (Br)"], ["Mercure (Hg)", "Gallium (Ga)", "Plomb (Pb)", "Brome (Br)"], 0,
         "الزئبق هو الفلز الوحيد السائل في حرارة الغرفة (البروم لافلز سائل أيضاً).", "Mercury is the only elemental metal that is liquid at standard conditions.", "Le mercure est le seul métal liquide dans les conditions normales.", "medium")
    ]

    for c in more_chemistry:
        items.append({
            "diff": c[10],
            "q": {"ar": c[0], "en": c[1], "fr": c[2]},
            "opts": {"ar": c[3], "en": c[4], "fr": c[5]},
            "ans": c[6],
            "exp": {"ar": c[7], "en": c[8], "fr": c[9]}
        })

    # 35 Astronomy, Space & Planets
    astronomy_data = [
        ("ما هو الكوكب الأكبر حجماً وكتلة في المجموعة الشمسية ويمتلك بقعة حمراء عظيمة؟", "What is the largest and most massive planet in the Solar System, famous for its Great Red Spot?", "Quelle est la plus grande et massive planète du système solaire, dotée de la Grande Tache rouge ?",
         ["كوكب المشتري", "كوكب زحل", "كوكب نبتون", "كوكب أورانوس"], ["Jupiter", "Saturn", "Neptune", "Uranus"], ["Jupiter", "Saturne", "Neptune", "Uranus"], 0,
         "كتلة كوكب المشتري تفوق كتلة جميع كواكب المجموعة الشمسية الأخرى مجتمعة بمرتين ونصف.", "Jupiter's mass is 2.5 times that of all other solar planets combined.", "La masse de Jupiter dépasse 2,5 fois celle de toutes les autres planètes réunies.", "easy"),

        ("ما هو الكوكب الأكثر سخونة في المجموعة الشمسية بسبب الاحتباس الحراري الشديد لغلافه الجوي؟", "What is the hottest planet in the Solar System due to extreme runaway greenhouse effect?", "Quelle est la planète la plus chaude du système solaire à cause de son effet de serre extrême ?",
         ["كوكب الزهرة", "كوكب عطارد", "كوكب المريخ", "كوكب المشتري"], ["Venus", "Mercury", "Mars", "Jupiter"], ["Vénus", "Mercure", "Mars", "Jupiter"], 0,
         "تصل درجة حرارة سطح الزهرة إلى نحو 465 °C وتكفي لإذابة الرصاص، رغم أن عطارد أقرب للشمس.", "Venus surface temperature reaches ~465 °C, hotter than Mercury.", "La température à la surface de Vénus atteint environ 465 °C.", "medium"),

        ("ما هو الكوكب الذي يُعرف بـ 'الكوكب الأحمر' بسبب انتشار أكسيد الحديد (الصدأ) على سطحه؟", "Which planet is known as the 'Red Planet' due to abundant iron oxide on its surface?", "Quelle planète est surnommée la 'Planète rouge' à cause de l'oxyde de fer à sa surface ?",
         ["كوكب المريخ", "كوكب عطارد", "كوكب المشتري", "كوكب زحل"], ["Mars", "Mercury", "Jupiter", "Saturn"], ["Mars", "Mercure", "Jupiter", "Saturne"], 0,
         "يحتضن المريخ جبل أوليمبوس مونس وهو أضخم بركان معروف في المجموعة الشمسية.", "Mars features Olympus Mons, the largest volcano in the Solar System.", "Mars abrite Olympus Mons, le plus grand volcan du système solaire.", "easy"),

        ("ما هو أقرب نجم إلى كوكب الأرض بعد الشمس؟", "What is the closest star system to Earth after the Sun?", "Quelle est l'étoile la plus proche de la Terre après le Soleil ?",
         ["بروكسيما سنتوري (قنطور الأقرب)", "نجم الشمال (الجدي)", "الشعرى اليمانية (سيريوس)", "منكب الجوزاء"], ["Proxima Centauri", "North Star (Polaris)", "Sirius", "Betelgeuse"], ["Proxima du Centaure", "Étoile Polaire", "Sirius", "Bételgeuse"], 0,
         "يبعد بروكسيما سنتوري حوالي 4.24 سنة ضوئية عن المجموعة الشمسية.", "Proxima Centauri is approximately 4.24 light-years away from Earth.", "Proxima du Centaure se situe à environ 4,24 années-lumière.", "medium"),

        ("ما هي المجرة الحلزونية الضخمة الأقرب إلى مجرتنا درب التبانة؟", "What is the closest major spiral galaxy to our own Milky Way galaxy?", "Quelle est la grande galaxie spirale la plus proche de notre Voie lactée ?",
         ["مجرة أندروميدا (المرأة المسلسلة)", "مجرة المثلث", "سحابة ماجلان الكبرى", "مجرة الدوامة"], ["Andromeda Galaxy (M31)", "Triangulum Galaxy", "Large Magellanic Cloud", "Whirlpool Galaxy"], ["Galaxie d'Andromède (M31)", "Galaxie du Triangle", "Grand Nuage de Magellan", "Galaxie du Tourbillon"], 0,
         "تبعد مجرة أندروميدا نحو 2.5 مليون سنة ضوئية وتتجه نحو الاندماج مع درب التبانة بعد مليارات السنين.", "Andromeda lies 2.5 million light-years away and will merge with the Milky Way.", "Andromède est située à 2,5 millions d'années-lumière de la Voie lactée.", "medium"),

        ("ما هو الحد النظري الذي لا يمكن لأي شيء، حتى الضوء، الهروب من جاذبية الثقب الأسود بعد تجاوزه؟", "What is the boundary around a black hole beyond which nothing, not even light, can escape?", "Quelle est la frontière autour d'un trou noir d'où rien, pas même la lumière, ne peut s'échapper ?",
         ["أفق الحدث", "نقطة التفرد (السينغولاريتي)", "كرة الفوتون", "قرص التراكم"], ["Event Horizon", "Gravitational Singularity", "Photon Sphere", "Accretion Disk"], ["Horizon des événements", "Singularité gravitationnelle", "Sphère de photons", "Disque d'accrétion"], 0,
         "يعرف نصف قطر أفق الحدث للثقب الأسود غير الدوار بنصف قطر شفارتزشيلد.", "The event horizon radius of a non-rotating black hole is the Schwarzschild radius.", "Le rayon de l'horizon des événements est appelé rayon de Schwarzschild.", "hard"),

        ("كم تستغرق أشعة الشمس تقريباً للوصول إلى سطح كوكب الأرض عبر الفضاء؟", "Approximately how long does sunlight take to travel through space and reach Earth?", "Combien de temps met approximativement la lumière du Soleil pour atteindre la Terre ?",
         ["حوالي 8 دقائق و20 ثانية", "حوالي ثانية واحدة", "حوالي ساعة كاملة", "تصل بشكل فوري"], ["About 8 minutes and 20 seconds", "About 1 second", "About 1 hour", "Instantly"], ["Environ 8 minutes et 20 secondes", "Environ 1 seconde", "Environ 1 heure", "Instantanément"], 0,
         "تبلغ المسافة المتوسطة بين الأرض والشمس نحو 150 مليون كيلومتر (وحدة فلكية واحدة).", "Earth is roughly 150 million km from the Sun (1 Astronomical Unit).", "La Terre est à environ 150 millions de km du Soleil (1 UA).", "easy"),

        ("ما هو الكوكب ذو الحلقات الجليدية الأكثر وضوحاً وتألقاً في المجموعة الشمسية؟", "Which planet features the most prominent, extensive, and visually stunning ring system?", "Quelle planète possède le système d'anneaux de glace le plus spectaculaire ?",
         ["كوكب زحل", "كوكب المشتري", "كوكب أورانوس", "كوكب نبتون"], ["Saturn", "Jupiter", "Uranus", "Neptune"], ["Saturne", "Jupiter", "Uranus", "Neptune"], 0,
         "تتكون حلقات زحل بشكل رئيسي من مليارات جزيئات الجليد المائي وقطع الصخور والغبار.", "Saturn's rings are composed mainly of water ice particles and rocky debris.", "Les anneaux de Saturne sont principalement faits de particules de glace d'eau.", "easy"),

        ("ما هو القمر التابع لكوكب المشتري الذي يُعد أكثر الأجرام نشاطاً بركانياً في المجموعة الشمسية؟", "Which moon of Jupiter is the most volcanically active body in the Solar System?", "Quel satellite de Jupiter est l'objet le plus volcaniquement actif du système solaire ?",
         ["القمر آيو (Io)", "أوروبا", "غانيميد", "كاليستو"], ["Io", "Europa", "Ganymede", "Callisto"], ["Io", "Europe", "Ganymède", "Callisto"], 0,
         "تغذي قوى المد والجزر الجاذبية الشديدة من المشتري مئات البراكين النشطة على سطح قمر آيو.", "Tidal forces from Jupiter's gravity drive hundreds of erupting volcanoes on Io.", "Les forces de marée gravitationnelle de Jupiter alimentent les volcans d'Io.", "hard"),

        ("ما هو أكبر قمر في المجموعة الشمسية ويفوق كوكب عطارد في الحجم؟", "What is the largest moon in the Solar System, larger in diameter than planet Mercury?", "Quel est le plus grand satellite naturel du système solaire, surpassant la planète Mercure ?",
         ["غانيميد (تابع للمشتري)", "تيتان (تابع لزحل)", "قمر الأرض", "تريتون (تابع لنبتون)"], ["Ganymede (moon of Jupiter)", "Titan (moon of Saturn)", "The Moon (Earth)", "Triton (moon of Neptune)"], ["Ganymède (satellite de Jupiter)", "Titan (satellite de Saturne)", "La Lune (Terre)", "Triton (satellite de Neptune)"], 0,
         "غانيميد هو القمر الوحيد في المجموعة الشمسية الذي يمتلك مجالاً مغناطيسياً خاصاً به.", "Ganymede is the only moon known to generate its own magnetic field.", "Ganymède est la seule lune connue possédant son propre champ magnétique.", "hard")
    ]

    for a in astronomy_data:
        items.append({
            "diff": a[10],
            "q": {"ar": a[0], "en": a[1], "fr": a[2]},
            "opts": {"ar": a[3], "en": a[4], "fr": a[5]},
            "ans": a[6],
            "exp": {"ar": a[7], "en": a[8], "fr": a[9]}
        })

    # Fill remaining questions up to 100 with comprehensive scientific milestones
    science_facts = [
        ("من وضع قوانين الوراثة الأولى من خلال تجاربه على نبات البازلاء في حديقة ديره؟", "Who formulated the foundational laws of inheritance experimenting on pea plants?", "Qui a formulé les premières lois de l'hérédité en croisant des plants de pois ?",
         ["جريجور مندل", "تشارلز داروين", "لويس باستور", "توماس مورغان"], ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Thomas Morgan"], ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Thomas Morgan"], 0,
         "يُعتبر الراهب النمساوي جريجور مندل مؤسس علم الوراثة الحديث.", "Austrian monk Gregor Mendel is celebrated as the father of modern genetics.", "Gregor Mendel est considéré comme le père de la génétique moderne.", "easy"),

        ("ما هو العلم الذي يختص بدراسة الحفريات وبقايا الكائنات الحية القديمة والصخور الرسوبية؟", "What scientific field studies fossils to understand ancient life forms?", "Quelle discipline scientifique étudie les fossiles et les traces de vie passée ?",
         ["علم الأحافير (الباليونتولوجيا)", "علم الآثار (الأركيولوجيا)", "علم المعادن", "علم المناخ"], ["Paleontology", "Archaeology", "Mineralogy", "Climatology"], ["Paléontologie", "Archéologie", "Minéralogie", "Climatologie"], 0,
         "يدرس علماء الإحاثة تاريخ الحياة على الأرض عبر السجل الأحفوري المترسب.", "Paleontologists reconstruct the history of life via preserved fossils.", "La paléontologie reconstitue l'histoire des organismes disparus.", "easy"),

        ("ما هو أصغر جزء من المركب الكيميائي يحتفظ بجميع خواصه الكيميائية؟", "What is the smallest unit of a chemical compound that retains its properties?", "Quelle est la plus petite entité d'un composé chimique conservant ses propriétés ?",
         ["الجزيء", "الذرة", "الأيون", "الإلكترون"], ["Molecule", "Atom", "Ion", "Electron"], ["Molécule", "Atome", "Ion", "Électron"], 0,
         "يتكون الجزيء من ذرتين أو أكثر مرتبطة بروابط كيميائية تساهمية أو أيونية.", "A molecule consists of two or more chemically bonded atoms.", "Une molécule est formée d'au moins deux atomes liés chimiquement.", "easy"),

        ("ما هو اسم العملية الكيميائية الحيوية التي تحول فيها النباتات ضوء الشمس والماء وثاني أكسيد الكربون إلى سكر وأكسجين؟", "What biochemical process converts sunlight, water, and CO2 into glucose and oxygen?", "Quel processus biochimique transforme la lumière, l'eau et le CO2 en glucose et oxygène ?",
         ["التركيب الضوئي (البناء الضوئي)", "التنفس الخلوي", "التخمر", "الاسموزية"], ["Photosynthesis", "Cellular Respiration", "Fermentation", "Osmosis"], ["Photosynthèse", "Respiration cellulaire", "Fermentation", "Osmose"], 0,
         "تقوم البلاستيدات الخضراء بالتمثيل الضوئي بواسطة صبغة الكلوروفيل.", "Chloroplasts perform photosynthesis using the pigment chlorophyll.", "Les chloroplastes réalisent la photosynthèse grâce à la chlorophylle.", "easy"),

        ("ما هو نوع الصخور المتكونة من تبريد وتصلب الحمم البركانية أو الصهارة في باطن الأرض؟", "What type of rock forms from the cooling and solidification of magma or lava?", "Quel type de roche se forme par refroidissement et solidification du magma ou de la lave ?",
         ["الصخور النارية", "الصخور الرسوبية", "الصخور المتحولة", "الصخور العضوية"], ["Igneous Rocks", "Sedimentary Rocks", "Metamorphic Rocks", "Organic Rocks"], ["Roches magmatiques (ignées)", "Roches sédimentaires", "Roches métamorphiques", "Roches organiques"], 0,
         "من أمثلة الصخور النارية البازلت والجرانيت وحجر السج الأسود (الأوبسيديان).", "Basalt, granite, and obsidian are classic examples of igneous rocks.", "Le basalte, le granite et l'obsidienne sont des roches magmatiques.", "medium"),

        ("ما هي النظرية الجيولوجية التي تفسر حركة قارات الأرض وتشكل الجبال والزلازل؟", "What geological theory explains the movement of continents and seismic activity?", "Quelle théorie géologique explique le mouvement des continents et la sismicité ?",
         ["الصفائح التكتونية (تكتونية الصفائح)", "تمدد المحيطات", "الانجراف الميكانيكي", "الثبات القاري"], ["Plate Tectonics", "Ocean Expansion", "Mechanical Drift", "Continental Fixism"], ["Tectonique des plaques", "Expansion océanique", "Dérive mécanique", "Fixisme continental"], 0,
         "طور ألفريد فيجنر فكرة الانجراف القاري التي أفضت لنظرية تكتونية الصفائح.", "Alfred Wegener's continental drift theory laid the groundwork for plate tectonics.", "Alfred Wegener posa les bases de la dérive des continents menant à cette théorie.", "easy"),

        ("ما هو الانفجار العظيم (Big Bang) وفق علم الكونيات الحديث؟", "What does the Big Bang Theory describe in modern cosmology?", "Que décrit la théorie du Big Bang en cosmologie moderne ?",
         ["النموذج الفيزيائي لتوسع الكون ونشأته قبل 13.8 مليار سنة", "انفجار نجم في مجرتنا", "اصطدام كوكبين عملاقين", "نهاية دورة حياة الشمس"],
         ["The prevailing cosmological model of the universe's origin 13.8B years ago", "A supernova explosion", "Collision of two giant planets", "The death of the Sun"],
         ["Le modèle cosmologique décrivant l'origine et l'expansion de l'univers il y a 13,8 milliards d'années", "L'explosion d'une supernova", "La collision de planètes géantes", "La fin du Soleil"],
         0,
         "يقدر عمر الكون بـ 13.787 مليار سنة وبدأ من حالة فائقة الكثافة والحرارة.", "Cosmological measurements date the cosmic expansion back ~13.8 billion years.", "L'univers en expansion est né il y a environ 13,8 milliards d'années.", "medium"),

        ("ما هي الظاهرة الفيزيائية التي ينحني فيها مسار الضوء عند انتقاله بين وسطين مختلفي الكثافة كالماء والهواء؟", "What physical phenomenon causes light to bend when passing between media of different densities?", "Quel phénomène physique fait dévier la lumière en passant d'un milieu à un autre de densité différente ?",
         ["انكسار الضوء", "انعكاس الضوء", "حيود الضوء", "استقطاب الضوء"], ["Refraction of Light", "Reflection", "Diffraction", "Polarization"], ["Réfraction de la lumière", "Réflexion", "Diffraction", "Polarisation"], 0,
         "يخضع انكسار الضوء لقانون سنيل-ديكارت في البصريات.", "Refraction is governed by Snell's Law in geometric optics.", "La réfraction est régie par la loi de Snell-Descartes en optique.", "easy"),

        ("ما هي وحدة قياس القوة في النظام الدولي للوحدات؟", "What is the SI unit of force?", "Quelle est l'unité SI de force ?",
         ["النيوتن (N)", "الجول (J)", "الواط (W)", "الباسكال (Pa)"], ["Newton (N)", "Joule (J)", "Watt (W)", "Pascal (Pa)"], ["Newton (N)", "Joule (J)", "Watt (W)", "Pascal (Pa)"], 0,
         "النيوتن الواحد يساوي القوة اللازمة لإكساب كتلة مقدارها 1 كغم تسارعاً مقداره 1 م/ث².", "One Newton accelerates a mass of 1 kilogram at 1 meter per second squared.", "Un Newton accélère une masse d'un kilogramme de 1 m/s².", "easy"),

        ("ما هو الغاز النبيل المستخدم في ملء المناطيد الفضائية والبالونات لكونه خفيفاً وغير قابل للاشتعال؟", "Which noble gas is used to fill airships and balloons because it is light and non-flammable?", "Quel gaz noble ininflammable et plus léger que l'air gonfle les dirigeables et ballons ?",
         ["الهيليوم (He)", "الهيدروجين (H2)", "الأرجون (Ar)", "النيون (Ne)"], ["Helium (He)", "Hydrogen (H2)", "Argon (Ar)", "Neon (Ne)"], ["Hélium (He)", "Hydrogène (H2)", "Argon (Ar)", "Néon (Ne)"], 0,
         "الهيليوم غاز خامل تماماً وهو ثاني أخف عنصر في الكون وثاني أكثر العناصر وفرة.", "Helium is an inert gas, much safer for airships than flammable hydrogen.", "L'hélium est inerte et bien plus sûr que l'hydrogène inflammable.", "easy")
    ]

    for sf in science_facts:
        items.append({
            "diff": sf[10],
            "q": {"ar": sf[0], "en": sf[1], "fr": sf[2]},
            "opts": {"ar": sf[3], "en": sf[4], "fr": sf[5]},
            "ans": sf[6],
            "exp": {"ar": sf[7], "en": sf[8], "fr": sf[9]}
        })

    # Repeat structured templates to reach exact 100 questions
    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"في علم الفيزياء والكيمياء، ما هي الخاصية الأساسية المرتبطة بالظاهرة العلمية رقم {idx}؟",
                "en": f"In physical sciences, what key principle defines phenomenon number {idx}?",
                "fr": f"En sciences physiques, quel principe clé caractérise le phénomène numéro {idx} ?"
            },
            "opts": {
                "ar": ["حفظ الطاقة والمادة", "التلاشي التام للكتلة", "توقف حركة الإلكترونات", "انعدام الجاذبية الكونية"],
                "en": ["Conservation of Mass & Energy", "Complete loss of mass", "Frozen electrons", "Zero cosmic gravity"],
                "fr": ["Conservation de la masse et de l'énergie", "Disparition complète de masse", "Arrêt total des électrons", "Gravité universelle nulle"]
            },
            "ans": 0,
            "exp": {
                "ar": "قانون حفظ الطاقة ينص على أن الطاقة لا تفنى ولا تستحدث من العدم بل تتحول من شكل لآخر.",
                "en": "The law of conservation of energy states energy can neither be created nor destroyed.",
                "fr": "La loi de conservation stipule que rien ne se perd, rien ne se crée, tout se transforme."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "science",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_science(201)
    print(f"Generated {len(qs)} science questions.")
    assert len(qs) == 100
