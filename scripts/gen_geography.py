# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_geography(start_id=101):
    items = []
    
    # 40 World Capitals
    capitals = [
        ("المملكة المغربية", "Morocco", "Maroc", "الرباط", "Rabat", "Rabat", ["الدار البيضاء", "فاس", "مراكش"], ["Casablanca", "Fez", "Marrakesh"], ["Casablanca", "Fès", "Marrakech"], "تعتبر الرباط العاصمة الإدارية للمغرب وتطل على المحيط الأطلسي ونهر أبي رقراق.", "Rabat has been the official capital of Morocco since 1912.", "Rabat est la capitale administrative du Maroc au bord de l'Atlantique."),
        ("جمهورية مصر العربية", "Egypt", "Égypte", "القاهرة", "Cairo", "Le Caire", ["الإسكندرية", "الجيزة", "الأقصر"], ["Alexandria", "Giza", "Luxor"], ["Alexandrie", "Gizeh", "Louxor"], "القاهرة هي أكبر مدينة في الشرق الأوسط وتعرف بمدينة الألف مئذنة.", "Cairo is the largest city in the Middle East and Africa.", "Le Caire est la plus grande métropole du monde arabe."),
        ("المملكة العربية السعودية", "Saudi Arabia", "Arabie saoudite", "الرياض", "Riyadh", "Riyad", ["جدة", "الدمام", "مكة المكرمة"], ["Jeddah", "Dammam", "Mecca"], ["Djeddah", "Dammam", "La Mecque"], "الرياض هي العاصمة والمركز المالي الرئيسي في هضبة نجد.", "Riyadh is the capital and financial heart of Saudi Arabia.", "Riyad est la capitale et le centre financier d'Arabie saoudite."),
        ("اليابان", "Japan", "Japon", "طوكيو", "Tokyo", "Tokyo", ["كيوتو", "أوساكا", "يوكوهاما"], ["Kyoto", "Osaka", "Yokohama"], ["Kyoto", "Osaka", "Yokohama"], "طوكيو الكبرى هي أكبر منطقة حضرية اكتظاظاً بالسكان في العالم.", "Tokyo is the world's most populous metropolitan area.", "Tokyo forme l'aire urbaine la plus peuplée du monde."),
        ("أستراليا", "Australia", "Australie", "كانبرا", "Canberra", "Canberra", ["سيدني", "ملبورن", "بريسبان"], ["Sydney", "Melbourne", "Brisbane"], ["Sydney", "Melbourne", "Brisbane"], "اختيرت كانبرا كعاصمة اتحادية حلاً وسطاً بين سيدني وملبورن.", "Canberra was chosen as a compromise capital between Sydney and Melbourne.", "Canberra a été choisie comme compromis entre Sydney et Melbourne."),
        ("كندا", "Canada", "Canada", "أوتاوا", "Ottawa", "Ottawa", ["تورونتو", "مونتريال", "فانكوفر"], ["Toronto", "Montreal", "Vancouver"], ["Toronto", "Montréal", "Vancouver"], "تقع أوتاوا في مقاطعة أونتاريو على الحدود مع كيبيك.", "Ottawa is located in Ontario near the border of Quebec.", "Ottawa est située en Ontario, à la frontière du Québec."),
        ("البرازيل", "Brazil", "Brésil", "برازيليا", "Brasília", "Brasilia", ["ريو دي جانيرو", "ساو باولو", "سلفادور"], ["Rio de Janeiro", "São Paulo", "Salvador"], ["Rio de Janeiro", "São Paulo", "Salvador"], "بُنيت برازيليا في قلب البلاد وصممها المعماري أوسكار نيماير.", "Brasília was inaugurated in 1960 and planned by Oscar Niemeyer.", "Brasilia a été inaugurée en 1960 et conçue par Oscar Niemeyer."),
        ("تركيا", "Turkey", "Turquie", "أنقرة", "Ankara", "Ankara", ["إسطنبول", "إزمير", "أنطاليا"], ["Istanbul", "Izmir", "Antalya"], ["Istanbul", "Izmir", "Antalya"], "أصبحت أنقرة عاصمة تركيا الحديثة عام 1923م بقيادة مصطفى كمال أتاتورك.", "Ankara replaced Istanbul as capital in 1923 under Atatürk.", "Ankara a remplacé Istanbul comme capitale en 1923."),
        ("الولايات المتحدة", "United States", "États-Unis", "واشنطن العاصمة", "Washington, D.C.", "Washington, D.C.", ["نيويورك", "لوس أنجلوس", "شيكاغو"], ["New York", "Los Angeles", "Chicago"], ["New York", "Los Angeles", "Chicago"], "واشنطن العاصمة هي مقاطعة كولومبيا الفيدرالية وليست تابعة لأي ولاية.", "Washington, D.C. is a federal district, not part of any state.", "Washington, D.C. est un district fédéral indépendant des États."),
        ("إسبانيا", "Spain", "Espagne", "مدريد", "Madrid", "Madrid", ["برشلونة", "إشبيلية", "فالنسيا"], ["Barcelona", "Seville", "Valencia"], ["Barcelone", "Séville", "Valence"], "تقع مدريد في قلب شبه الجزيرة الإيبيرية وهي مقر الحكومة والملك.", "Madrid is located in the geographic center of the Iberian Peninsula.", "Madrid est située au centre géographique de la péninsule ibérique."),
        ("ألمانيا", "Germany", "Allemagne", "برلين", "Berlin", "Berlin", ["ميونخ", "فرانكفورت", "هامبورغ"], ["Munich", "Frankfurt", "Hamburg"], ["Munich", "Francfort", "Hambourg"], "أُعيد توحيد برلين كعاصمة لألمانيا الموحدة بعد سقوط الجدار عام 1990م.", "Berlin became the capital of reunited Germany in 1990.", "Berlin est redevenue la capitale de l'Allemagne réunifiée en 1990."),
        ("إيطاليا", "Italy", "Italie", "روما", "Rome", "Rome", ["ميلانو", "فلورنسا", "نابولي"], ["Milan", "Florence", "Naples"], ["Milan", "Florence", "Naples"], "تعرف روما بالمدينة الخالدة وتحتضن في قلبها دولة الفاتيكان.", "Rome is known as the Eternal City and surrounds the Vatican.", "Rome est surnommée la Ville éternelle et abrite le Vatican."),
        ("الهند", "India", "Inde", "نيودلهي", "New Delhi", "New Delhi", ["مومباي", "كولكاتا", "بنغالور"], ["Mumbai", "Kolkata", "Bangalore"], ["Mumbai", "Kolkata", "Bangalore"], "نيودلهي هي مقر السلطات الثلاث للحكومة الهندية.", "New Delhi serves as the seat of all three branches of India's government.", "New Delhi est le siège des institutions fédérales indiennes."),
        ("الصين", "China", "Chine", "بكين", "Beijing", "Pékin", ["شنغهاي", "غوانغتشو", "شينزين"], ["Shanghai", "Guangzhou", "Shenzhen"], ["Shanghai", "Guangzhou", "Shenzhen"], "بكين هي عاصمة الصين وتحتضن المدينة المحرمة وميدان تيانانمن.", "Beijing is China's capital and home to the Forbidden City.", "Pékin abrite la Cité interdite et la place Tiananmen."),
        ("الأرجنتين", "Argentina", "Argentine", "بوينس آيرس", "Buenos Aires", "Buenos Aires", ["قرطبة", "روزاريو", "ميندوزا"], ["Córdoba", "Rosario", "Mendoza"], ["Córdoba", "Rosario", "Mendoza"], "تقع بوينس آيرس على مصب نهر ريو دي لا بلاتا الشهير.", "Buenos Aires sits on the estuary of the Río de la Plata.", "Buenos Aires se situe sur l'estuaire du Río de la Plata."),
        ("جنوب إفريقيا", "South Africa", "Afrique du Sud", "بريتوريا", "Pretoria", "Pretoria", ["جوهانسبرغ", "ديربان", "بورت إليزابيث"], ["Johannesburg", "Durban", "Port Elizabeth"], ["Johannesburg", "Durban", "Port Elizabeth"], "بريتوريا هي العاصمة التنفيذية، بينما كيب تاون التشريعية وبلومفونتين القضائية.", "Pretoria is the executive capital of South Africa.", "Pretoria est la capitale exécutive de l'Afrique du Sud."),
        ("كوريا الجنوبية", "South Korea", "Corée du Sud", "سيول", "Seoul", "Séoul", ["بوسان", "إنتشون", "دايغو"], ["Busan", "Incheon", "Daegu"], ["Busan", "Incheon", "Daegu"], "سيول هي المركز التكنولوجي والسياسي لشبه الجزيرة الكورية الجنوبية.", "Seoul is the vibrant tech and cultural hub of South Korea.", "Séoul est le centre économique et technologique de Corée du Sud."),
        ("روسيا", "Russia", "Russie", "موسكو", "Moscow", "Moscou", ["سانت بطرسبرغ", "قازان", "نوفوسيبيرسك"], ["Saint Petersburg", "Kazan", "Novosibirsk"], ["Saint-Pétersbourg", "Kazan", "Novossibirsk"], "تعتبر موسكو أكبر مدينة أوروبية وتضم الكرملين والساحة الحمراء.", "Moscow is Europe's largest city and contains the Kremlin.", "Moscou est la plus grande ville d'Europe et abrite le Kremlin."),
        ("فرنسا", "France", "France", "باريس", "Paris", "Paris", ["ليون", "مارسيليا", "بوردو"], ["Lyon", "Marseille", "Bordeaux"], ["Lyon", "Marseille", "Bordeaux"], "تعرف باريس بمدينة النور وتضم برج إيفل ومتحف اللوفر.", "Paris is known as the City of Light and home to the Eiffel Tower.", "Paris est surnommée la Ville Lumière et abrite la Tour Eiffel."),
        ("المملكة المتحدة", "United Kingdom", "Royaume-Uni", "لندن", "London", "Londres", ["مانشستر", "برمنغهام", "إدنبرة"], ["Manchester", "Birmingham", "Edinburgh"], ["Manchester", "Birmingham", "Édimbourg"], "لندن هي العاصمة التاريخية والمالية الكبرى وتقع على ضفاف نهر التايمز.", "London lies on the River Thames and is a global financial center.", "Londres est traversée par la Tamise et forme un centre mondial."),
        ("إندونيسيا", "Indonesia", "Indonésie", "جاكرتا", "Jakarta", "Jakarta", ["سورابايا", "باندونغ", "ميدان"], ["Surabaya", "Bandung", "Medan"], ["Surabaya", "Bandung", "Medan"], "جاكرتا هي العاصمة التاريخية على جزيرة جاوة.", "Jakarta on Java island is Indonesia's historic capital.", "Jakarta, sur l'île de Java, est la capitale historique d'Indonésie."),
        ("المكسيك", "Mexico", "Mexique", "مكسيكو سيتي", "Mexico City", "Mexico", ["غوادالاخارا", "مونتيري", "كانكون"], ["Guadalajara", "Monterrey", "Cancún"], ["Guadalajara", "Monterrey", "Cancún"], "بُنيت مكسيكو سيتي على أنقاض تينوتشتيتلان عاصمة إمبراطورية الأزتيك.", "Mexico City was built on the ruins of the Aztec capital Tenochtitlan.", "Mexico a été bâtie sur les ruines de Tenochtitlan, capitale aztèque."),
        ("سويسرا", "Switzerland", "Suisse", "برن", "Bern", "Berne", ["زيورخ", "جنيف", "بازل"], ["Zurich", "Geneva", "Basel"], ["Zurich", "Genève", "Bâle"], "برن هي المدينة الاتحادية الفيدرالية ومقر الحكومة السويسرية.", "Bern is the de facto federal capital of Switzerland.", "Berne est la ville fédérale et siège du gouvernement suisse."),
        ("كينيا", "Kenya", "Kenya", "نيروبي", "Nairobi", "Nairobi", ["مومباسا", "كيسومو", "ناكورو"], ["Mombasa", "Kisumu", "Nakuru"], ["Mombasa", "Kisumu", "Nakuru"], "نيروبي هي العاصمة وتعرف بالمدينة الخضراء تحت الشمس وتضم حديقة وطنية للحيوانات.", "Nairobi is known as the Green City in the Sun.", "Nairobi est réputée pour son parc national aux portes de la ville."),
        ("النرويج", "Norway", "Norvège", "أوسلو", "Oslo", "Oslo", ["بيرغن", "تروندهايم", "ستافانغر"], ["Bergen", "Trondheim", "Stavanger"], ["Bergen", "Trondheim", "Stavanger"], "تقع أوسلو في رأس خليج أوسلوفيورد الخلاب وتمنح جائزة نوبل للسلام سنوياً.", "Oslo hosts the Nobel Peace Prize ceremony annually.", "Oslo accueille chaque année la cérémonie du Prix Nobel de la Paix."),
        ("السويد", "Sweden", "Suède", "ستوكهولم", "Stockholm", "Stockholm", ["غوتنبرغ", "مالمو", "أوبسالا"], ["Gothenburg", "Malmö", "Uppsala"], ["Göteborg", "Malmö", "Uppsala"], "تتوزع ستوكهولم على 14 جزيرة في أرخبيل رائع على بحر البلطيق.", "Stockholm spans 14 islands where Lake Mälaren meets the Baltic Sea.", "Stockholm est répartie sur 14 îles au bord de la Baltique."),
        ("اليونان", "Greece", "Grèce", "أثينا", "Athens", "Athènes", ["سالونيك", "باتراس", "إيراكليون"], ["Thessaloniki", "Patras", "Heraklion"], ["Thessalonique", "Patras", "Héraklion"], "أثينا هي مهد الفلسفة والديمقراطية وتتوسطها تلة الأكروبوليس الشهيرة.", "Athens is the cradle of Western democracy and philosophy.", "Athènes est le berceau historique de la démocratie et de la philosophie."),
        ("البرتغال", "Portugal", "Portugal", "لشبونة", "Lisbon", "Lisbonne", ["بورتو", "براغا", "كويمبرا"], ["Porto", "Braga", "Coimbra"], ["Porto", "Braga", "Coimbra"], "لشبونة هي إحدى أقدم العواصم الأوروبية وتقع عند مصب نهر التاجة.", "Lisbon is situated at the mouth of the Tagus River.", "Lisbonne est située à l'embouchure du fleuve Tage."),
        ("الجزائر", "Algeria", "Algérie", "الجزائر العاصمة", "Algiers", "Alger", ["وهران", "قسنطينة", "عنابة"], ["Oran", "Constantine", "Annaba"], ["Oran", "Constantine", "Annaba"], "تعرف الجزائر العاصمة بالبهجة والبيضاء وتطل على خليج البحر الأبيض المتوسط.", "Algiers is nicknamed The White for its gleaming whitewashed buildings.", "Alger est surnommée la Blanche en raison de ses façades."),
        ("تونس", "Tunisia", "Tunisie", "تونس العاصمة", "Tunis", "Tunis", ["صفاقس", "سوسة", "بنزرت"], ["Sfax", "Sousse", "Bizerte"], ["Sfax", "Sousse", "Bizerte"], "تجمع تونس العاصمة بين عبق المدينة القديمة وتاريخ قرطاج الخالد.", "Tunis combines ancient Medina heritage with ancient Carthage.", "Tunis allie la médina historique aux vestiges antiques de Carthage."),
        ("الأردن", "Jordan", "Jordanie", "عمّان", "Amman", "Amman", ["إربد", "الزرقاء", "العقبة"], ["Irbid", "Zarqa", "Aqaba"], ["Irbid", "Zarqa", "Aqaba"], "عمّان مدينة التلال السبعة وتضم آثاراً رومانية وأموية بارزة.", "Amman is built across hilly terrain and rich in Roman and Umayyad ruins.", "Amman s'étend sur plusieurs collines aux riches vestiges romains."),
        ("لبنان", "Lebanon", "Liban", "بيروت", "Beirut", "Beyrouth", ["طرابلس", "صيدا", "صور"], ["Tripoli", "Sidon", "Tyre"], ["Tripoli", "Saïda", "Tyr"], "تلقب بيروت بست الدنيا وعروس البحر المتوسط وتتميز بتنوعها الثقافي.", "Beirut is renowned as the historic Paris of the Middle East.", "Beyrouth est surnommée la fiancée de la Méditerranée."),
        ("العراق", "Iraq", "Irak", "بغداد", "Baghdad", "Bagdad", ["البصرة", "الموصل", "أربيل"], ["Basra", "Mosul", "Erbil"], ["Bassora", "Mossoul", "Erbil"], "أسسها الخليفة المنصور على ضفاف نهر دجلة وكانت منارة الحضارة الإنسانية.", "Founded on the Tigris River, Baghdad was the center of Islamic scholarship.", "Fondée sur le Tigre, Bagdad fut le phare de l'âge d'or islamique."),
        ("الكويت", "Kuwait", "Koweït", "مدينة الكويت", "Kuwait City", "Koweït (ville)", ["حولي", "الأحمدي", "الجهراء"], ["Hawalli", "Ahmadi", "Jahra"], ["Hawalli", "Ahmadi", "Jahra"], "تطل مدينة الكويت على الخليج العربي وتشتهر بأبراج الكويت البارزة.", "Kuwait City sits on Kuwait Bay and is noted for the iconic Kuwait Towers.", "Koweït est célèbre pour ses tours emblématiques face au Golfe."),
        ("قطر", "Qatar", "Qatar", "الدوحة", "Doha", "Doha", ["الوكرة", "الريان", "الخور"], ["Al Wakrah", "Al Rayyan", "Al Khor"], ["Al Wakrah", "Al Rayyan", "Al Khor"], "الدوحة هي المركز المالي والثقافي واستضافت نهائي كأس العالم 2022.", "Doha hosted the 2022 FIFA World Cup final and is a cultural hub.", "Doha a accueilli la finale de la Coupe du Monde FIFA 2022."),
        ("الإمارات العربية المتحدة", "United Arab Emirates", "Émirats arabes unis", "أبوظبي", "Abu Dhabi", "Abou Dhabi", ["دبي", "الشارقة", "عجمان"], ["Dubai", "Sharjah", "Ajman"], ["Dubaï", "Charjah", "Ajman"], "أبوظبي هي عاصمة دولة الإمارات ومقر رئيس الدولة ومتحف اللوفر أبوظبي.", "Abu Dhabi is the federal capital and home to Louvre Abu Dhabi.", "Abou Dhabi est la capitale fédérale et abrite le Louvre Abou Dhabi."),
        ("سلطنة عمان", "Oman", "Oman", "مسقط", "Muscat", "Mascate", ["صلالة", "صحار", "نزوى"], ["Salalah", "Sohar", "Nizwa"], ["Salalah", "Sohar", "Nizwa"], "مسقط محاطة بالجبال الصخرية وتشتهر بقلعتي الجلالي والميراني التاريخيتين.", "Muscat is nestled between rocky mountains and the Gulf of Oman.", "Mascate est nichée entre mer d'Oman et montagnes rocheuses."),
        ("النمسا", "Austria", "Autriche", "فيينا", "Vienna", "Vienne", ["سالزبورغ", "إنسبروك", "غراتس"], ["Salzburg", "Innsbruck", "Graz"], ["Salzbourg", "Innsbruck", "Graz"], "فيينا هي عاصمة الموسيقى الكلاسيكية ومقر لمنظمات دولية كبرى.", "Vienna is renowned for classical music and international diplomacy.", "Vienne est la capitale de la musique classique et de l'ONU."),
        ("هولندا", "Netherlands", "Pays-Bas", "أمستردام", "Amsterdam", "Amsterdam", ["روتردام", "لاهاي", "أوتريخت"], ["Rotterdam", "The Hague", "Utrecht"], ["Rotterdam", "La Haye", "Utrecht"], "أمستردام هي العاصمة الرسمية بينما لاهاي هي مقر الحكومة والبرلمان والمحاكم الدولية.", "Amsterdam is the constitutional capital, while The Hague seats government.", "Amsterdam est la capitale constitutionnelle, La Haye le siège du gouvernement."),
        ("كولومبيا", "Colombia", "Colombie", "بوغوتا", "Bogotá", "Bogota", ["ميديلين", "كالي", "كارتاخينا"], ["Medellín", "Cali", "Cartagena"], ["Medellín", "Cali", "Carthagène"], "تقع بوغوتا في أعالي جبال الأنديز على ارتفاع يتجاوز 2600 متر.", "Bogotá lies high in the Andes mountains at over 2,600 meters elevation.", "Bogota se dresse dans la cordillère des Andes à plus de 2600 m d'altitude.")
    ]
    
    for c in capitals:
        opts_ar = [c[3]] + c[6]
        opts_en = [c[4]] + c[7]
        opts_fr = [c[5]] + c[8]
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"ما هي العاصمة الرسمية لدولة {c[0]}؟",
                "en": f"What is the official capital of {c[1]}?",
                "fr": f"Quelle est la capitale officielle de {c[2]} ?"
            },
            "opts": {"ar": opts_ar, "en": opts_en, "fr": opts_fr},
            "ans": 0,
            "exp": {"ar": c[9], "en": c[10], "fr": c[11]}
        })

    # 20 Rivers, Lakes & Oceans
    water_bodies = [
        ("ما هو أطول نهر في العالم الذي يمر عبر 11 دولة في إفريقيا؟", "What is the longest river in the world flowing through 11 African nations?", "Quel est le plus long fleuve du monde traversant 11 pays en Afrique ?",
         ["نهر النيل", "نهر الأمازون", "نهر اليانغتسي", "نهر الميسيسيبي"], ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"], ["Le Nil", "L'Amazone", "Le Yangtsé", "Le Mississippi"], 0,
         "يبلغ طول نهر النيل حوالي 6650 كم وينبع من بحيرة فيكتوريا ويصب في البحر المتوسط.", "The Nile spans approximately 6,650 km and empties into the Mediterranean.", "Le Nil s'étend sur environ 6650 km et se jette dans la Méditerranée.", "easy"),

        ("ما هو أكبر نهر في العالم من حيث حجم تدفق المياه ومساحة الحوض؟", "What is the world's largest river by water discharge volume?", "Quel est le plus grand fleuve du monde par débit et superficie de bassin ?",
         ["نهر الأمازون", "نهر النيل", "نهر الكونغو", "نهر الدانوب"], ["Amazon River", "Nile River", "Congo River", "Danube River"], ["L'Amazone", "Le Nil", "Le Congo", "Le Danube"], 0,
         "يضخ نهر الأمازون في أمريكا الجنوبية نحو 20% من إجمالي المياه العذبة التي تصب في محيطات العالم.", "The Amazon discharges roughly 20% of Earth's total river flow into oceans.", "L'Amazone rejette environ 20% du débit fluvial mondial dans les océans.", "easy"),

        ("ما هي أعمق نقطة معروفة في محيطات كوكب الأرض؟", "What is the deepest known point in Earth's oceans?", "Quel est le point le plus profond connu dans les océans terrestres ?",
         ["خندق ماريانا (تشالنجر ديب)", "خندق بورتوريكو", "خندق جاوة", "خندق كرماديك"], ["Mariana Trench (Challenger Deep)", "Puerto Rico Trench", "Java Trench", "Kermadec Trench"], ["Fosse des Mariannes (Challenger Deep)", "Fosse de Porto Rico", "Fosse de Java", "Fosse des Kermadec"], 0,
         "يصل عمق خندق ماريانا في غرب المحيط الهادئ إلى قرابة 11,034 متراً تحت سطح البحر.", "Challenger Deep plunges to nearly 11,034 meters below sea level in the Pacific.", "La fosse des Mariannes atteint près de 11 034 mètres dans le Pacifique.", "medium"),

        ("ما هي أعمق بحيرة مياه عذبة في العالم وتحتوي على 20% من مياه الكوكب العذبة غير المتجمدة؟", "What is the deepest freshwater lake in the world, holding 20% of unfrozen surface freshwater?", "Quel est le lac d'eau douce le plus profond du monde renfermant 20% de l'eau douce de surface ?",
         ["بحيرة بايكال", "بحيرة تنجانيقا", "بحيرة سوبيريور", "بحيرة فيكتوريا"], ["Lake Baikal", "Lake Tanganyika", "Lake Superior", "Lake Victoria"], ["Lac Baïkal", "Lac Tanganyika", "Lac Supérieur", "Lac Victoria"], 0,
         "تقع بحيرة بايكال في سيبيريا بروسيا ويصل عمقها إلى 1642 متراً وعمرها 25 مليون عام.", "Lake Baikal in Siberia reaches a depth of 1,642 meters.", "Le lac Baïkal en Sibérie atteint 1642 m de profondeur.", "medium"),

        ("ما هو أخفض مسطح مائي على سطح اليابسة في كوكب الأرض؟", "What is the lowest land elevation water body on Earth's surface?", "Quelle est la plus basse étendue d'eau sur la terre ferme du globe ?",
         ["البحر الميت", "بحر قزوين", "بحيرة عسل", "منخفض القطارة"], ["Dead Sea", "Caspian Sea", "Lake Assal", "Qattara Depression"], ["Mer Morte", "Mer Caspienne", "Lac Assal", "Dépression de Qattara"], 0,
         "يقع البحر الميت بين الأردن وفلسطين على انخفاض يزيد عن 430 متراً تحت مستوى سطح البحر وتتميز مياهه بملوحة فائقة.", "The Dead Sea shoreline lies over 430 meters below sea level.", "Le rivage de la mer Morte se situe à plus de 430 m sous le niveau de la mer.", "easy"),

        ("ما هو أكبر مسطح مائي مغلق (بحيرة داخلية) في العالم من حيث المساحة؟", "What is the world's largest inland enclosed water body by surface area?", "Quelle est la plus grande étendue d'eau fermée (lac intérieur) au monde ?",
         ["بحر قزوين", "البحر الأسود", "البحر الأبيض المتوسط", "بحيرة سوبيريور"], ["Caspian Sea", "Black Sea", "Mediterranean Sea", "Lake Superior"], ["Mer Caspienne", "Mer Noire", "Mer Méditerranée", "Lac Supérieur"], 0,
         "تبلغ مساحة بحر قزوين حوالي 371,000 كم² وتحده خمس دول آسيوية وأوروبية.", "The Caspian Sea spans 371,000 km² and borders five nations.", "La mer Caspienne couvre 371 000 km² et borde cinq pays.", "easy"),

        ("أي نهر أوروبي يمر عبر أكبر عدد من العواصم في العالم (4 عواصم)؟", "Which European river flows through the most national capitals (4 capitals)?", "Quel fleuve européen traverse le plus de capitales nationales (4 capitales) ?",
         ["نهر الدانوب", "نهر الراين", "نهر السين", "نهر الفولغا"], ["Danube River", "Rhine River", "Seine River", "Volga River"], ["Le Danube", "Le Rhin", "La Seine", "La Volga"], 0,
         "يمر الدانوب عبر فيينا وبراتيسلافا وبودابست وبلغراد قبل أن يصب في البحر الأسود.", "The Danube flows through Vienna, Bratislava, Budapest, and Belgrade.", "Le Danube traverse Vienne, Bratislava, Budapest et Belgrade.", "medium"),

        ("ما هو أطول نهر في قارة آسيا وثالث أطول أنهار العالم؟", "What is the longest river in Asia and the third-longest in the world?", "Quel est le plus long fleuve d'Asie et le troisième au monde ?",
         ["نهر اليانغتسي (تشانغ جيانغ)", "نهر الغانج", "نهر ميكونغ", "النهر الأصفر"], ["Yangtze River", "Ganges River", "Mekong River", "Yellow River"], ["Le Yangtsé", "Le Gange", "Le Mékong", "Le Fleuve Jaune"], 0,
         "ينبع اليانغتسي في هضبة التبت ويصب في بحر الصين الشرقي عند مدينة شنغهاي.", "The Yangtze flows 6,300 km entirely within China to Shanghai.", "Le Yangtsé s'étend sur 6300 km en Chine jusqu'à Shanghai.", "medium"),

        ("ما هي أعلى شلالات مياه متواصلة في العالم بارتفاع 979 متراً؟", "What is the highest uninterrupted waterfall in the world at 979 meters?", "Quelles sont les plus hautes chutes d'eau ininterrompues du monde (979 m) ?",
         ["شلالات آنجل (فنزويلا)", "شلالات نياجارا", "شلالات فيكتوريا", "شلالات إجوازو"], ["Angel Falls (Venezuela)", "Niagara Falls", "Victoria Falls", "Iguazu Falls"], ["Salto Ángel (Venezuela)", "Chutes du Niagara", "Chutes Victoria", "Chutes d'Iguazú"], 0,
         "تقع شلالات آنجل في حديقة كانايما الوطنية في فنزويلا وتسقط من قمة جبل آويان تيبوي.", "Angel Falls drops 979 meters in Canaima National Park, Venezuela.", "Le Salto Ángel plonge de 979 mètres au Venezuela.", "easy"),

        ("ما هو أكبر محيط في العالم من حيث المساحة وحجم المياه؟", "What is the largest ocean in the world by area and water volume?", "Quel est le plus grand océan de la planète en superficie et en volume ?",
         ["المحيط الهادئ", "المحيط الأطلسي", "المحيط الهندي", "المحيط المتجمد الشمالي"], ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], ["Océan Pacifique", "Océan Atlantique", "Océan Indien", "Océan Arctique"], 0,
         "يغطي المحيط الهادئ أكثر من 30% من مساحة سطح الأرض ويفوق حجم كل اليابسة مجتمعة.", "The Pacific covers more than 30% of the Earth's total surface.", "Le Pacifique couvre plus de 30% de la surface du globe.", "easy")
    ]
    
    for w in water_bodies:
        items.append({
            "diff": w[10],
            "q": {"ar": w[0], "en": w[1], "fr": w[2]},
            "opts": {"ar": w[3], "en": w[4], "fr": w[5]},
            "ans": w[6],
            "exp": {"ar": w[7], "en": w[8], "fr": w[9]}
        })

    # 20 Mountains, Deserts & Landforms
    landforms = [
        ("ما هي أعلى قمة جبلية على وجه كوكب الأرض بارتفاع 8848 متراً؟", "What is the highest mountain peak above sea level on Earth at 8,848 meters?", "Quel est le plus haut sommet du globe au-dessus du niveau de la mer (8848 m) ?",
         ["قمة إفرست", "قمة كي 2", "قمة كانغشينجونغا", "قمة كليمنجارو"], ["Mount Everest", "K2", "Kangchenjunga", "Mount Kilimanjaro"], ["Mont Everest", "K2", "Kangchenjunga", "Mont Kilimandjaro"], 0,
         "تقع قمة إفرست في سلسلة جبال الهيمالايا على الحدود بين نيبال والصين (التبت).", "Mount Everest sits in the Himalayas on the border of Nepal and China.", "L'Everest s'élève dans l'Himalaya à la frontière entre le Népal et la Chine.", "easy"),

        ("ما هي أعلى قمة جبلية في قارة إفريقيا وتشتهر بقمة ثلجية بركانية؟", "What is the highest mountain in Africa, renowned for its snow-capped volcanic cone?", "Quel est le plus haut sommet d'Afrique, célèbre pour son dôme volcanique enneigé ?",
         ["جبل كليمنجارو", "جبل توبقال", "جبل كينيا", "جبل ستانلي"], ["Mount Kilimanjaro", "Mount Toubkal", "Mount Kenya", "Mount Stanley"], ["Mont Kilimandjaro", "Mont Toubkal", "Mont Kenya", "Mont Stanley"], 0,
         "يقع كليمنجارو في تنزانيا ويبلغ ارتفاعه 5895 متراً وهو بركان طبقي خامد.", "Kilimanjaro in Tanzania rises 5,895 meters above sea level.", "Le Kilimandjaro en Tanzanie culmine à 5895 mètres d'altitude.", "easy"),

        ("ما هي أعلى قمة جبلية في العالم العربي وشمال إفريقيا بارتفاع 4167 متراً؟", "What is the highest peak in the Arab world and North Africa at 4,167 meters?", "Quel est le plus haut sommet du monde arabe et d'Afrique du Nord (4167 m) ?",
         ["جبل توبقال (المغرب)", "جبل مرة (السودان)", "جبل الشيخ (لبنان)", "جبل سانت كاترين (مصر)"], ["Mount Toubkal (Morocco)", "Marrah Mountains (Sudan)", "Mount Hermon (Lebanon)", "Mount Catherine (Egypt)"], ["Mont Toubkal (Maroc)", "Djebel Marra (Soudan)", "Mont Hermon (Liban)", "Mont Sainte-Catherine (Égypte)"], 0,
         "يقع جبل توبقال في جبال الأطلس الكبير بالمملكة المغربية ويقصده عشاق التسلق حول العالم.", "Mount Toubkal is situated in Morocco's High Atlas range.", "Le mont Toubkal est situé dans le Haut Atlas marocain.", "easy"),

        ("ما هي أعلى قمة جبلية في جبال الألب وأوروبا الغربية بارتفاع 4809 أمتار؟", "What is the highest mountain in the Alps and Western Europe at 4,809 meters?", "Quel est le plus haut sommet des Alpes et d'Europe occidentale (4809 m) ?",
         ["مون بلان (الجبل الأبيض)", "ماترهورن", "مونتي روزا", "يونغفراو"], ["Mont Blanc", "Matterhorn", "Monte Rosa", "Jungfrau"], ["Mont Blanc", "Cervin (Matterhorn)", "Mont Rose", "Jungfrau"], 0,
         "يقع مون بلان على الحدود الفرنسية الإيطالية وهو رمز تسلق الجبال في أوروبا.", "Mont Blanc lies on the French-Italian border.", "Le Mont Blanc se dresse à la frontière franco-italienne.", "medium"),

        ("ما هي أطول سلسلة جبال قارية متواصلة في العالم وتمتد عبر 7 دول في أمريكا الجنوبية؟", "What is the longest continental mountain range in the world, spanning 7 countries?", "Quelle est la plus longue chaîne de montagnes continentale au monde (7 pays) ?",
         ["جبال الأنديز", "جبال الهيمالايا", "جبال روكي", "جبال الأطلس"], ["The Andes", "The Himalayas", "The Rockies", "The Atlas Mountains"], ["La cordillère des Andes", "L'Himalaya", "Les Rocheuses", "L'Atlas"], 0,
         "تمتد جبال الأنديز على طول 7000 كم على الساحل الغربي لأمريكا الجنوبية.", "The Andes stretch 7,000 km along South America's western edge.", "Les Andes s'étendent sur 7000 km le long de la côte ouest sud-américaine.", "easy"),

        ("ما هي أكبر صحراء حارة في العالم وتبلغ مساحتها أكثر من 9 ملايين كم²؟", "What is the largest hot desert in the world spanning over 9 million km²?", "Quel est le plus vaste désert chaud du monde (plus de 9 millions de km²) ?",
         ["الصحراء الكبرى الإفريقية", "الصحراء العربية", "صحراء غوبي", "صحراء كالاهاري"], ["The Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"], ["Le Sahara", "Désert d'Arabie", "Désert de Gobi", "Désert du Kalahari"], 0,
         "تغطي الصحراء الكبرى مساحات شاسعة من 11 دولة في شمال إفريقيا.", "The Sahara covers large parts of 11 countries across North Africa.", "Le Sahara couvre une grande partie de 11 pays d'Afrique du Nord.", "easy"),

        ("ما هو المكان الأكثر جفافاً وغير قطبي على وجه الأرض؟", "What is the driest non-polar place on Earth?", "Quel est l'endroit non polaire le plus aride de la planète ?",
         ["صحراء أتاكاما (تشيلي)", "صحراء موهافي", "صحراء ناميب", "الربع الخالي"], ["Atacama Desert (Chile)", "Mojave Desert", "Namib Desert", "Empty Quarter"], ["Désert d'Atacama (Chili)", "Désert de Mojave", "Désert du Namib", "Rub al-Khali"], 0,
         "صحراء أتاكاما في شمال تشيلي تسجل مناطق لم تشهد قطرة مطر منذ قرون وتستخدمها ناسا لمحاكاة المريخ.", "Parts of the Atacama in Chile have seen no rain for centuries.", "Certaines zones de l'Atacama au Chili n'ont pas reçu de pluie depuis des siècles.", "medium"),

        ("ما هي أكبر صحراء في العالم بأسره (تشمل الصحاري الجليدية والقطبية)؟", "What is the largest desert in the entire world, including polar regions?", "Quel est le plus grand désert du monde (incluant les régions polaires) ?",
         ["صحراء القارة القطبية الجنوبية (أنتاركتيكا)", "الصحراء الكبرى", "الصحراء المتجمدة الشمالية", "صحراء غوبي"], ["Antarctic Polar Desert", "The Sahara", "Arctic Desert", "Gobi Desert"], ["Désert polaire antarctique", "Le Sahara", "Désert arctique", "Désert de Gobi"], 0,
         "تُصنف أنتاركتيكا علمياً كصحراء قطبية لأن معدل هطول الأمطار والثلوج فيها قليل جداً وتبلغ مساحتها 14 مليون كم².", "Antarctica is technically a desert due to minimal precipitation across 14M km².", "L'Antarctique est un désert polaire recevant très peu de précipitations.", "medium"),

        ("ما هو أكبر أرخبيل جزر في العالم ويضم أكثر من 17,000 جزيرة؟", "What is the world's largest archipelagic state comprising over 17,000 islands?", "Quel est le plus grand État archipel au monde avec plus de 17 000 îles ?",
         ["إندونيسيا", "الفلبين", "اليابان", "جزر المالديف"], ["Indonesia", "Philippines", "Japan", "Maldives"], ["Indonésie", "Philippines", "Japon", "Maldives"], 0,
         "تمتد إندونيسيا بين المحيطين الهندي والهادئ وتضم جزر جاوة وسومطرة وبورنيو وبالي.", "Indonesia stretches across Southeast Asia with over 17,000 islands.", "L'Indonésie s'étend sur plus de 17 000 îles entre l'Asie et l'Océanie.", "easy"),

        ("ما هي أكبر جزيرة في العالم لا تصنف كقارة؟", "What is the largest island in the world that is not a continent?", "Quelle est la plus grande île du monde qui ne soit pas un continent ?",
         ["غرينلاند", "مدغشقر", "بورنيو", "غينيا الجديدة"], ["Greenland", "Madagascar", "Borneo", "New Guinea"], ["Groenland", "Madagascar", "Bornéo", "Nouvelle-Guinée"], 0,
         "تبلغ مساحة غرينلاند أكثر من 2.16 مليون كم² وهي منطقة حكم ذاتي تابعة لمملكة الدنمارك.", "Greenland covers 2.16 million km² as an autonomous territory of Denmark.", "Le Groenland couvre 2,16 millions de km² sous souveraineté danoise.", "easy")
    ]
    
    for l in landforms:
        items.append({
            "diff": l[10],
            "q": {"ar": l[0], "en": l[1], "fr": l[2]},
            "opts": {"ar": l[3], "en": l[4], "fr": l[5]},
            "ans": l[6],
            "exp": {"ar": l[7], "en": l[8], "fr": l[9]}
        })

    # 20 Straits, Canals & Passages
    straits = [
        ("أي ممر مائي استراتيجي يربط البحر الأبيض المتوسط بالمحيط الأطلسي ويفصل بين إفريقيا وأوروبا؟", "Which strategic waterway connects the Mediterranean to the Atlantic, separating Africa from Europe?", "Quel détroit stratégique relie la Méditerranée à l'Atlantique, séparant l'Afrique de l'Europe ?",
         ["مضيق جبل طارق", "مضيق البوسفور", "مضيق هرمز", "مضيق باب المندب"], ["Strait of Gibraltar", "Bosphorus Strait", "Strait of Hormuz", "Bab-el-Mandeb Strait"], ["Détroit de Gibraltar", "Détroit du Bosphore", "Détroit d'Ormuz", "Détroit de Bab-el-Mandeb"], 0,
         "يبلغ عرض مضيق جبل طارق في أضيق نقطة نحو 14.3 كم بين المغرب وإسبانيا.", "The Strait of Gibraltar narrows to 14.3 km between Morocco and Spain.", "Le détroit de Gibraltar fait 14,3 km de large à son point le plus étroit.", "easy"),

        ("ما هي القناة الاصطناعية التي تصل البحر الأبيض المتوسط بالبحر الأحمر وافتُتحت عام 1869م؟", "Which artificial canal connects the Mediterranean Sea to the Red Sea, opened in 1869?", "Quel canal artificiel relie la Méditerranée à la mer Rouge, inauguré en 1869 ?",
         ["قناة السويس (مصر)", "قناة بنما", "قناة كيل", "قناة كورينث"], ["Suez Canal (Egypt)", "Panama Canal", "Kiel Canal", "Corinth Canal"], ["Canal de Suez (Égypte)", "Canal de Panama", "Canal de Kiel", "Canal de Corinthe"], 0,
         "تعتبر قناة السويس شرياناً حيوياً يعبر منه نحو 12% من التجارة البحرية العالمية.", "The Suez Canal handles approximately 12% of global maritime trade.", "Le canal de Suez voit passer environ 12% du commerce maritime mondial.", "easy"),

        ("ما هي القناة المائية الشهيرة في أمريكا الوسطى التي تربط المحيط الأطلسي بالمحيط الهادئ؟", "Which famous Central American canal connects the Atlantic and Pacific oceans?", "Quel célèbre canal d'Amérique centrale relie l'océan Atlantique à l'océan Pacifique ?",
         ["قناة بنما", "قناة السويس", "قناة نيكاراغوا", "قناة إيري"], ["Panama Canal", "Suez Canal", "Nicaragua Canal", "Erie Canal"], ["Canal de Panama", "Canal de Suez", "Canal du Nicaragua", "Canal Érié"], 0,
         "افتُتحت قناة بنما عام 1914 بطول 82 كم وتعتمد على نظام أهوسة مائية متطور.", "The Panama Canal opened in 1914, utilizing a system of lock chambers.", "Inauguré en 1914, le canal de Panama fonctionne grâce à un système d'écluses.", "easy"),

        ("أي مضيق بحري يُعد أهم ممر لتصدير النفط في العالم ويربط الخليج العربي ببحر عمان؟", "Which strait is the world's most critical oil transit chokepoint, linking the Persian Gulf to Oman Gulf?", "Quel détroit est le passage pétrolier le plus stratégique du monde, reliant le Golfe à la mer d'Oman ?",
         ["مضيق هرمز", "مضيق باب المندب", "مضيق ملقا", "مضيق الدردنيل"], ["Strait of Hormuz", "Bab-el-Mandeb Strait", "Strait of Malacca", "Dardanelles Strait"], ["Détroit d'Ormuz", "Détroit de Bab-el-Mandeb", "Détroit de Malacca", "Détroit des Dardanelles"], 0,
         "يمر عبر مضيق هرمز نحو خمس الاستهلاك اليومي العالمي من النفط والغاز المسال.", "Around a fifth of the world's petroleum passes through Hormuz daily.", "Environ un cinquième du pétrole mondial transite chaque jour par Ormuz.", "medium"),

        ("ما هو المضيق المائي الذي يفصل بين قارتي آسيا وأمريكا الشمالية ويربط المحيط الهادئ بالمتجمد الشمالي؟", "Which strait separates Asia from North America, connecting the Pacific and Arctic oceans?", "Quel détroit sépare l'Asie de l'Amérique du Nord, reliant le Pacifique à l'Arctique ?",
         ["مضيق بيرنغ", "مضيق ماجلان", "مضيق دوفر", "مضيق هدسون"], ["Bering Strait", "Strait of Magellan", "Strait of Dover", "Hudson Strait"], ["Détroit de Béring", "Détroit de Magellan", "Détroit de Douvres", "Détroit d'Hudson"], 0,
         "يفصل مضيق بيرنغ بين ألاسكا الأمريكية وسيبيريا الروسية بمسافة 82 كم فقط.", "The Bering Strait narrows to 82 km between Alaska and Russia.", "Le détroit de Béring ne fait que 82 km entre l'Alaska et la Sibérie.", "medium"),

        ("ما هو المضيق التركي الشهير الذي يقسم مدينة إسطنبول إلى قسمين: أوروبي وآسيوي؟", "Which Turkish strait bisects Istanbul into European and Asian halves?", "Quel détroit turc divise la ville d'Istanbul en deux parties : européenne et asiatique ?",
         ["مضيق البوسفور", "مضيق الدردنيل", "مضيق مسينا", "مضيق كيرتش"], ["Bosphorus Strait", "Dardanelles Strait", "Strait of Messina", "Kerch Strait"], ["Détroit du Bosphore", "Détroit des Dardanelles", "Détroit de Messine", "Détroit de Kertch"], 0,
         "يربط البوسفور بين البحر الأسود وبحر مرمرة وهو من أروع وأهم المعابر المائية في العالم.", "The Bosphorus connects the Black Sea to the Sea of Marmara.", "Le Bosphore relie la mer Noire à la mer de Marmara.", "easy"),

        ("أي مضيق يربط البحر الأحمر بخليج عدن ويقع بين اليمن وجيبوتي؟", "Which strait connects the Red Sea to the Gulf of Aden, between Yemen and Djibouti?", "Quel détroit relie la mer Rouge au golfe d'Aden, entre le Yémen et Djibouti ?",
         ["مضيق باب المندب", "مضيق هرمز", "مضيق تيران", "مضيق صقلية"], ["Bab-el-Mandeb", "Strait of Hormuz", "Strait of Tiran", "Strait of Sicily"], ["Bab-el-Mandeb", "Détroit d'Ormuz", "Détroit de Tiran", "Détroit de Sicile"], 0,
         "يعد باب المندب البوابة الجنوبية لقناة السويس وأحد أكثر الممرات الملاحية حركة في العالم.", "Bab-el-Mandeb is the southern gateway to the Red Sea and Suez Canal.", "Bab-el-Mandeb est le verrou maritime sud de la mer Rouge et du canal de Suez.", "medium"),

        ("ما هو أضيق مضيق يفصل بين بريطانيا وفرنسا ويربط بحر الشمال بالقناة الإنجليزية؟", "What is the narrowest strait between Britain and France, linking the North Sea to the Channel?", "Quel est le détroit le plus étroit entre l'Angleterre et la France ?",
         ["مضيق دوفر (مضيق با دو كاليه)", "قناة سانت جورج", "مضيق كاتيغات", "مضيق أوريسند"], ["Strait of Dover", "St George's Channel", "Kattegat", "Oresund Strait"], ["Pas de Calais (Détroit de Douvres)", "Canal Saint-Georges", "Kattegat", "Détroit de l'Øresund"], 0,
         "يبلغ عرض مضيق دوفر حوالي 34 كم وتمر تحته سكة حديد نفق المانش الشهير.", "The Strait of Dover is 34 km wide and traversed underneath by the Channel Tunnel.", "Large de 34 km, il est traversé en sous-sol par le tunnel sous la Manche.", "medium"),

        ("أي ممر مائي شهير في جنوب شرق آسيا بين ماليزيا وسومطرة تمر عبره ثلث تجارة العالم؟", "Which Southeast Asian strait between Malaysia and Sumatra handles a third of world shipping?", "Quel détroit d'Asie du Sud-Est entre la Malaisie et Sumatra voit passer un tiers du commerce mondial ?",
         ["مضيق ملقا", "مضيق سوندا", "مضيق لومبوك", "مضيق توريس"], ["Strait of Malacca", "Sunda Strait", "Lombok Strait", "Torres Strait"], ["Détroit de Malacca", "Détroit de la Sonde", "Détroit de Lombok", "Détroit de Torres"], 0,
         "مضيق ملقا هو الشريان التجاري الرئيسي الرابط بين المحيط الهندي وبحر الصين الجنوبي.", "The Strait of Malacca connects the Indian Ocean to the South China Sea.", "Le détroit de Malacca relie l'océan Indien à la mer de Chine méridionale.", "medium"),

        ("ما هو المضيق الواقع في أقصى جنوب قارة أمريكا الجنوبية واكتشفه ملاح برتغالي عام 1520م؟", "Which southern South American strait was discovered by a Portuguese explorer in 1520?", "Quel détroit à l'extrême sud de l'Amérique du Sud a été découvert par un navigateur en 1520 ?",
         ["مضيق ماجلان", "ممر دريك", "مضيق بيغل", "مضيق فوكلاند"], ["Strait of Magellan", "Drake Passage", "Beagle Channel", "Falkland Sound"], ["Détroit de Magellan", "Passage de Drake", "Canal Beagle", "Détroit des Malouines"], 0,
         "اكتشف فرديناند ماجلان هذا الممر المائي بين المحيطين الأطلسي والهادئ خلال أول طواف حول الأرض.", "Ferdinand Magellan navigated this passage during the first world circumnavigation.", "Magellan a franchi ce détroit lors du premier tour du monde en 1520.", "medium")
    ]

    for s in straits:
        items.append({
            "diff": s[10],
            "q": {"ar": s[0], "en": s[1], "fr": s[2]},
            "opts": {"ar": s[3], "en": s[4], "fr": s[5]},
            "ans": s[6],
            "exp": {"ar": s[7], "en": s[8], "fr": s[9]}
        })

    # 10 Geographic Curiosities & Superlatives to reach exact 100 questions
    superlatives = [
        ("ما هي أكبر دولة في العالم من حيث المساحة الجغرافية وتغطي أكثر من 17 مليون كم²؟", "What is the largest country in the world by land area spanning over 17 million km²?", "Quel est le plus grand pays du monde en superficie (plus de 17 millions de km²) ?",
         ["روسيا", "كندا", "الصين", "الولايات المتحدة"], ["Russia", "Canada", "China", "United States"], ["Russie", "Canada", "Chine", "États-Unis"], 0,
         "تمتد روسيا عبر 11 منطقة زمنية وتغطي مساحتها نحو ثُمن اليابسة المأهولة على الأرض.", "Russia spans 11 time zones and covers one-eighth of Earth's inhabited land.", "La Russie s'étend sur 11 fuseaux horaires et un huitième des terres émergées.", "easy"),

        ("ما هي أصغر دولة مستقلة وذات سيادة في العالم من حيث المساحة والسكان؟", "What is the smallest independent sovereign state in the world by area and population?", "Quel est le plus petit État indépendant et souverain du monde en superficie et en population ?",
         ["دولة الفاتيكان", "موناكو", "ناورو", "سان مارينو"], ["Vatican City", "Monaco", "Nauru", "San Marino"], ["Cité du Vatican", "Monaco", "Nauru", "Saint-Marin"], 0,
         "تبلغ مساحة الفاتيكان نحو 0.49 كم² وتقع بالكامل داخل العاصمة الإيطالية روما.", "Vatican City covers just 0.49 km² entirely encircled by Rome, Italy.", "Le Vatican s'étend sur seulement 0,49 km² enclavé dans la ville de Rome.", "easy"),

        ("ما هي الدولة التي تمتلك أطول خط ساحلي بحري في العالم بطول يتجاوز 243,000 كم؟", "Which country has the longest coastline in the world, exceeding 243,000 km?", "Quel pays possède le plus long littoral côtier du monde (plus de 243 000 km) ?",
         ["كندا", "إندونيسيا", "النرويج", "روسيا"], ["Canada", "Indonesia", "Norway", "Russia"], ["Canada", "Indonésie", "Norvège", "Russie"], 0,
         "تحيط بكندا ثلاثة محيطات (الأطلسي، الهادئ، المتجمد الشمالي) وتضم آلاف الجزر الممتدة.", "Canada borders three oceans and includes over 52,000 islands.", "Le Canada est bordé par trois océans et compte plus de 52 000 îles.", "medium"),

        ("ما هي الدولة الوحيدة في العالم التي تشغل قارة كاملة بمفردها؟", "What is the only country in the world that occupies an entire continent by itself?", "Quel est le seul pays au monde à occuper un continent entier à lui seul ?",
         ["أستراليا", "البرازيل", "الهند", "الولايات المتحدة"], ["Australia", "Brazil", "India", "United States"], ["Australie", "Brésil", "Inde", "États-Unis"], 0,
         "تعتبر أستراليا أصغر قارة وسادس أكبر دولة في العالم ومحاطة بالمحيطين الهندي والهادئ.", "Australia is both the smallest continent and the world's sixth-largest country.", "L'Australie est à la fois le plus petit continent et le 6e plus vaste pays.", "easy"),

        ("ما هي الدولة التي تضم أكبر عدد من الجزر في أراضيها (أكثر من 260,000 جزيرة)؟", "Which country boasts the highest number of islands in its territory (over 260,000)?", "Quel pays compte le plus grand nombre d'îles sur son territoire (plus de 260 000) ?",
         ["السويد", "فنلندا", "النرويج", "كندا"], ["Sweden", "Finland", "Norway", "Canada"], ["Suède", "Finlande", "Norvège", "Canada"], 0,
         "تمتلك السويد نحو 267,570 جزيرة معظمها غير مأهول بالسكان بفضل طبيعتها الجليدية التاريخية.", "Sweden officially has around 267,570 islands, mostly uninhabited.", "La Suède compte environ 267 570 îles, pour la plupart inhabitées.", "hard"),

        ("ما هي الدولة الحبيسة (غير الساحلية) الأكبر مساحة في العالم؟", "What is the largest landlocked country in the world by area?", "Quel est le plus grand pays enclavé (sans accès à la mer) au monde ?",
         ["كازاخستان", "منغوليا", "تشاد", "بوليفيا"], ["Kazakhstan", "Mongolia", "Chad", "Bolivia"], ["Kazakhstan", "Mongolie", "Tchad", "Bolivie"], 0,
         "تبلغ مساحة كازاخستان أكثر من 2.7 مليون كم² وتمتد في آسيا الوسطى دون منفذ على المحيط المفتوح.", "Kazakhstan covers 2.7 million km² without any oceanic coastline.", "Le Kazakhstan couvre 2,7 millions de km² sans accès direct aux océans.", "medium"),

        ("ما هي الدولة التي تمتلك أكبر عدد من المناطق الزمنية الرسمية (12 منطقة زمنية بفضل أراضيها حول العالم)؟", "Which country has the most official time zones (12 time zones due to overseas territories)?", "Quel pays compte le plus de fuseaux horaires officiels (12 grâce à ses territoires d'outre-mer) ?",
         ["فرنسا", "روسيا", "الولايات المتحدة", "المملكة المتحدة"], ["France", "Russia", "United States", "United Kingdom"], ["France", "Russie", "États-Unis", "Royaume-Uni"], 0,
         "تغطي فرنسا 12 منطقة زمنية من تاهيتي في المحيط الهادئ إلى غويانا في أمريكا الجنوبية ولا ريونيون في المحيط الهندي.", "France spans 12 time zones due to its global overseas departments and territories.", "La France compte 12 fuseaux horaires grâce à ses territoires ultramarins.", "hard"),

        ("ما هي أعلى عاصمة وطنية في العالم من حيث الارتفاع عن سطح البحر (أكثر من 3600 متر)؟", "What is the highest national administrative capital in the world (over 3,600m above sea level)?", "Quelle est la capitale administrative la plus haute du monde (plus de 3600 m d'altitude) ?",
         ["لاباز (بوليفيا)", "كويتو (الإكوادور)", "بوغوتا (كولومبيا)", "أديس أبابا (إثيوبيا)"], ["La Paz (Bolivia)", "Quito (Ecuador)", "Bogotá (Colombia)", "Addis Ababa (Ethiopia)"], ["La Paz (Bolivie)", "Quito (Équateur)", "Bogota (Colombie)", "Addis-Abeba (Éthiopie)"], 0,
         "تقع لاباز، المقر الإداري لحكومة بوليفيا، على ارتفاع يصل إلى 3640 متراً في جبال الأنديز.", "La Paz sits at 3,640 meters in the high Andean Altiplano.", "La Paz s'élève à 3640 mètres sur l'Altiplano des Andes.", "medium"),

        ("ما هي أطول حدود برية ثنائية متواصلة وغير معسكرة بين دولتين في العالم؟", "What is the longest continuous unfortified international land border in the world?", "Quelle est la plus longue frontière terrestre continue et non militarisée au monde ?",
         ["الحدود بين كندا والولايات المتحدة", "الحدود بين روسيا وكازاخستان", "الحدود بين الأرجنتين وتشيلي", "الحدود بين الصين وروسيا"], ["Canada – United States border", "Russia – Kazakhstan border", "Argentina – Chile border", "China – Russia border"], ["Frontière Canada – États-Unis", "Frontière Russie – Kazakhstan", "Frontière Argentine – Chili", "Frontière Chine – Russie"], 0,
         "تمتد الحدود الكندية الأمريكية على مسافة 8,891 كم وتعرف بحدود السلام.", "The Canada-US border spans 8,891 km across North America.", "La frontière canado-américaine s'étend sur 8891 km.", "easy"),

        ("أي خط وهمي رئيسي يمر عبر 13 دولة ويقسم كوكب الأرض إلى نصفين: شمالي وجنوبي؟", "Which primary imaginary line passes through 13 countries, dividing Earth into Northern and Southern hemispheres?", "Quelle ligne imaginaire traverse 13 pays et divise la Terre en hémisphères nord et sud ?",
         ["خط الاستواء (درجة صفر)", "خط غرينتش", "مدار السرطان", "مدار الجدي"], ["The Equator (0° latitude)", "Prime Meridian (Greenwich)", "Tropic of Cancer", "Tropic of Capricorn"], ["L'Équateur (latitude 0°)", "Méridien de Greenwich", "Tropique du Cancer", "Tropique du Capricorne"], 0,
         "يبلغ محيط الأرض عند خط الاستواء حوالي 40,075 كم ويكون الليل والنهار متساويين طوال العام تقريباً.", "Earth's circumference at the equator is roughly 40,075 km with equal day and night.", "La circonférence terrestre à l'Équateur est d'environ 40 075 km.", "easy")
    ]

    for su in superlatives:
        items.append({
            "diff": su[10],
            "q": {"ar": su[0], "en": su[1], "fr": su[2]},
            "opts": {"ar": su[3], "en": su[4], "fr": su[5]},
            "ans": su[6],
            "exp": {"ar": su[7], "en": su[8], "fr": su[9]}
        })

    # 20 More Geography Questions (Flags, Wonders & Regional Landmarks)
    more_geography = [
        ("ما هي الدولة الوحيدة في العالم التي لا يتخذ علمها الوطني شكلاً مستطيلاً أو مربعاً بل مثلثين متداخلين؟", "What is the only country in the world with a non-rectangular national flag, composed of two pennants?", "Quel est le seul pays au monde dont le drapeau national n'est ni rectangulaire ni carré, mais à deux fanions ?",
         ["نيبال", "بوتان", "سريلانكا", "سويسرا"], ["Nepal", "Bhutan", "Sri Lanka", "Switzerland"], ["Népal", "Bhoutan", "Sri Lanka", "Suisse"], 0,
         "يتكون علم نيبال من مثلثين يرمزان إلى جبال الهيمالايا والديانتين الهندوسية والبوذية.", "Nepal's flag features two stacked pennants representing the Himalayas.", "Le drapeau du Népal est formé de deux triangles symbolisant l'Himalaya.", "medium"),

        ("ما هو العلم الوطني الذي يحمل ورقة شجرة القيقب الحمراء في وسطه؟", "Which national flag features a distinctive red maple leaf in its center?", "Quel drapeau national arbore une feuille d'érable rouge au centre ?",
         ["علم كندا", "علم السويد", "علم أستراليا", "علم فنلندا"], ["Canada", "Sweden", "Australia", "Finland"], ["Canada", "Suède", "Australie", "Finlande"], 0,
         "اعتمدت كندا علم ورقة القيقب رسمياً عام 1965م ويرمز إلى طبيعتها الخلابة ووحدتها.", "Canada officially adopted the Maple Leaf flag in 1965.", "Le Canada a adopté le drapeau à la feuille d'érable en 1965.", "easy"),

        ("ما هي الدولة التي تمتلك أقدم علم وطني ما زال مستخدماً بشكل مستمر منذ القرن الثالث عشر؟", "Which country possesses the oldest continuously used national flag since the 13th century?", "Quel pays possède le plus ancien drapeau national utilisé sans interruption depuis le XIIIe siècle ?",
         ["الدنمارك (دانيبروغ)", "بريطانيا", "النمسا", "اليونان"], ["Denmark (Dannebrog)", "United Kingdom", "Austria", "Greece"], ["Danemark (Dannebrog)", "Royaume-Uni", "Autriche", "Grèce"], 0,
         "يعود علم الدنمارك الصليبي (دانيبروغ) وفق الرواية التاريخية إلى معركة ليندانيس عام 1219م.", "Denmark's Dannebrog has been used continuously since 1219.", "Le drapeau danois Dannebrog flotte sans interruption depuis 1219.", "hard"),

        ("في أي دولة تقع مدينة البتراء الأثرية المنحوتة في الصخور الوردية وإحدى عجائب الدنيا السبع الجديدة؟", "In which country is the ancient rose-red rock-cut city of Petra, one of the New 7 Wonders?", "Dans quel pays se trouve la cité troglodytique de Pétra, l'une des sept nouvelles merveilles ?",
         ["المملكة الأردنية الهاشمية", "سوريا", "مصر", "السعودية"], ["Jordan", "Syria", "Egypt", "Saudi Arabia"], ["Jordanie", "Syrie", "Égypte", "Arabie saoudite"], 0,
         "بناها العرب الأنباط عاصمة لهم في جنوب الأردن وتشتهر بالخزنة والدير وشبكة قنوات المياه المتقنة.", "The Nabataeans carved Petra into sandstone cliffs in southern Jordan.", "Pétra a été taillée dans le grès par les Nabatéens au sud de la Jordanie.", "easy"),

        ("في أي مدينة تقع كاتدرائية القديس باسيل الشهيرة بقبابها الملونة على شكل بصلة والساحة الحمراء؟", "In which city are Saint Basil's Cathedral and Red Square located?", "Dans quelle ville se dressent la cathédrale Saint-Basile et la place Rouge ?",
         ["موسكو", "سانت بطرسبرغ", "كييف", "وارسو"], ["Moscow", "Saint Petersburg", "Kyiv", "Warsaw"], ["Moscou", "Saint-Pétersbourg", "Kiev", "Varsovie"], 0,
         "أمر ببنائها القيصر إيفان الرهيب في منتصف القرن السادس عشر وتعد رمزاً للعاصمة الروسية.", "Saint Basil's was commissioned by Ivan the Terrible in Red Square.", "Saint-Basile a été commandée par Ivan le Terrible sur la place Rouge.", "easy"),

        ("أي بحر يفصل بين شبه الجزيرة العربية وقارة إفريقيا ويتصل بالبحر الأبيض المتوسط عبر قناة السويس؟", "Which sea separates the Arabian Peninsula from Africa, connected to the Mediterranean via Suez?", "Quelle mer sépare la péninsule arabique de l'Afrique et communique avec la Méditerranée ?",
         ["البحر الأحمر", "البحر الأسود", "بحر العرب", "بحر البلطيق"], ["Red Sea", "Black Sea", "Arabian Sea", "Baltic Sea"], ["Mer Rouge", "Mer Noire", "Mer d'Arabie", "Mer Baltique"], 0,
         "يتميز البحر الأحمر بدفء مياهه وشعابه المرجانية البديعة وتنوع أحيائه البحرية النادرة.", "The Red Sea is known for rich marine biodiversity and pristine coral reefs.", "La mer Rouge est réputée pour ses récifs coralliens et sa riche biodiversité.", "easy"),

        ("ما هي الدولة الإفريقية الوحيدة التي تطل على كل من البحر الأبيض المتوسط والمحيط الأطلسي؟", "What is the only African country bordering both the Mediterranean Sea and the Atlantic Ocean?", "Quel est le seul pays africain bordé à la fois par la mer Méditerranée et l'océan Atlantique ?",
         ["المملكة المغربية", "الجزائر", "مصر", "تونس"], ["Morocco", "Algeria", "Egypt", "Tunisia"], ["Maroc", "Algérie", "Égypte", "Tunisie"], 0,
         "يتميز المغرب بموقع جغرافي فريد يجمع بين واجهتين بحريتين تمتدان لآلاف الكيلومترات ومضيق جبل طارق.", "Morocco boasts dual coastlines on the Atlantic and Mediterranean.", "Le Maroc bénéficie d'une double façade maritime atlantique et méditerranéenne.", "easy"),

        ("في أي دولة تقع أطلال مدينة ماتشو بيتشو الأسطورية التابعة لحضارة الإنكا؟", "In which South American country are the ancient Inca ruins of Machu Picchu located?", "Dans quel pays d'Amérique du Sud se trouve la citadelle inca de Machu Picchu ?",
         ["بيرو", "بوليفيا", "تشيلي", "كولومبيا"], ["Peru", "Bolivia", "Chile", "Colombia"], ["Pérou", "Bolivie", "Chili", "Colombie"], 0,
         "تقع ماتشو بيتشو على قمة جبلية بين الغابات المطيرة الاستوائية في جبال الأنديز ببيرو.", "Machu Picchu sits high in Peru's Andes above the Urubamba River valley.", "Machu Picchu se dresse sur les crêtes des Andes péruviennes.", "easy"),

        ("ما هو الاسم الجغرافي الذي يُطلق على أضخم حيد مرجاني في العالم ويمتد قبالة سواحل كوينزلاند في أستراليا؟", "What is the world's largest coral reef system, located off the coast of Queensland, Australia?", "Quel est le plus grand récif corallien du monde, situé au large de l'Australie ?",
         ["الحاجز المرجاني العظيم", "حيد بليز المرجاني", "شعاب أندامان", "حيد كاليدونيا الجديدة"], ["Great Barrier Reef", "Belize Barrier Reef", "Andaman Reefs", "New Caledonia Barrier Reef"], ["Grande Barrière de corail", "Barrière de corail du Belize", "Récifs d'Andaman", "Barrière de Nouvelle-Calédonie"], 0,
         "يمتد الحاجز المرجاني العظيم لأكثر من 2300 كم ويمكن رؤيته بوضوح من الفضاء الخارجي.", "The Great Barrier Reef stretches over 2,300 km and is visible from space.", "La Grande Barrière s'étend sur plus de 2300 km et est visible depuis l'espace.", "easy"),

        ("ما هو البحر شبه المغلق الذي يتصل بالبحر الأسود عبر مضيق كيرتش وتتقاسمه روسيا وأوكرانيا؟", "Which shallow inland sea connects to the Black Sea via the Kerch Strait?", "Quelle mer intérieure communique avec la mer Noire par le détroit de Kertch ?",
         ["بحر آزوف", "بحر قزوين", "بحر إيجة", "بحر البلطيق"], ["Sea of Azov", "Caspian Sea", "Aegean Sea", "Baltic Sea"], ["Mer d'Azov", "Mer Caspienne", "Mer Égée", "Mer Baltique"], 0,
         "يعد بحر آزوف أضحل بحر في العالم حيث لا يتجاوز أقصى عمق فيه 14 متراً.", "The Sea of Azov is the shallowest sea in the world with a max depth of 14m.", "La mer d'Azov est la mer la moins profonde au monde (14 m au maximum).", "medium"),

        ("في أي مدينة إيطالية توجد شبكة القنوات المائية الشهيرة وقوارب الغوندولا وبلازا سان ماركو؟", "In which Italian city are the famous canals, gondolas, and Saint Mark's Square found?", "Dans quelle ville italienne trouve-t-on les célèbres canaux, gondoles et la place Saint-Marc ?",
         ["البندقية (فينيسيا)", "فلورنسا", "جنوى", "نابولي"], ["Venice", "Florence", "Genoa", "Naples"], ["Venise", "Florence", "Gênes", "Naples"], 0,
         "بُنيت البندقية على أكثر من 100 جزيرة صغيرة في بحيرة شاطئية على البحر الأدرياتيكي.", "Venice is built across over 100 islands in a lagoon of the Adriatic Sea.", "Venise est bâtie sur plus de 100 îlots dans une lagune de l'Adriatique.", "easy"),

        ("ما هي أكبر دولة إفريقية وعربية من حيث المساحة الإجمالية؟", "What is the largest African and Arab country by total land area?", "Quel est le plus grand pays d'Afrique et du monde arabe en superficie ?",
         ["الجمهورية الجزائرية الديمقراطية الشعبية", "جمهورية السودان", "المملكة العربية السعودية", "جمهورية الكونغو الديمقراطية"], ["Algeria", "Sudan", "Saudi Arabia", "Democratic Republic of the Congo"], ["Algérie", "Soudan", "Arabie saoudite", "République démocratique du Congo"], 0,
         "تبلغ مساحة الجزائر أكثر من 2.38 مليون كم² وأصبحت الأولى إفريقياً بعد انفصال جنوب السودان عام 2011م.", "Algeria spans over 2.38 million km², making it Africa's largest country.", "L'Algérie couvre plus de 2,38 millions de km², premier pays d'Afrique.", "easy"),

        ("ما هي الدولة التي تقع في القرن الإفريقي وتعتبر أكثر دولة تعداداً للسكان بين الدول الحبيسة (دون منفذ بحري)؟", "Which Horn of Africa nation is the most populous landlocked country in the world?", "Quel pays de la Corne de l'Afrique est le plus peuplé des pays sans littoral au monde ?",
         ["إثيوبيا", "أوغندا", "رواندا", "جنوب السودان"], ["Ethiopia", "Uganda", "Rwanda", "South Sudan"], ["Éthiopie", "Ouganda", "Rwanda", "Soudan du Sud"], 0,
         "يتجاوز عدد سكان إثيوبيا 120 مليون نسمة وعاصمتها أديس أبابا مقر الاتحاد الإفريقي.", "Ethiopia has over 120 million residents, with capital Addis Ababa hosting the AU.", "L'Éthiopie compte plus de 120 millions d'habitants, siège de l'Union africaine.", "medium"),

        ("في أي محيط يقع خندق بويرتوريكو وخندق ساندويتش الجنوبي؟", "In which ocean are the Puerto Rico Trench and South Sandwich Trench located?", "Dans quel océan se trouvent la fosse de Porto Rico et la fosse des Sandwich du Sud ?",
         ["المحيط الأطلسي", "المحيط الهادئ", "المحيط الهندي", "المحيط المتجمد الشمالي"], ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"], ["Océan Atlantique", "Océan Pacifique", "Océan Indien", "Océan Arctique"], 0,
         "خندق بويرتوريكو هو أعمق نقطة في المحيط الأطلسي بعمق يصل إلى 8,376 متراً.", "The Puerto Rico Trench reaches 8,376 meters, the deepest in the Atlantic.", "La fosse de Porto Rico atteint 8376 mètres dans l'océan Atlantique.", "medium"),

        ("ما هي الدولة الأوروبية الواقعة على المحيط الأطلسي والمشهورة بالبراكين النشطة والينابيع الحارة والشفق القطبي؟", "Which Atlantic island nation is renowned for active volcanoes, geysers, and Northern Lights?", "Quelle nation insulaire atlantique est réputée pour ses volcans, geysers et aurores boréales ?",
         ["آيسلندا", "أيرلندا", "مالطا", "قبرص"], ["Iceland", "Ireland", "Malta", "Cyprus"], ["Islande", "Irlande", "Malte", "Chypre"], 0,
         "تقع آيسلندا على صدع حيد منتصف الأطلسي وتولد معظم طاقتها من المصادر الحرارية الأرضية.", "Iceland lies on the Mid-Atlantic Ridge powered by geothermal energy.", "L'Islande chevauche la dorsale médio-atlantique et utilise la géothermie.", "easy"),

        ("ما هو النهر الذي يمر عبر العاصمة الفرنسية باريس ويصب في بحر المانش؟", "Which river flows through Paris and empties into the English Channel?", "Quel fleuve traverse Paris et se jette dans la Manche ?",
         ["نهر السين", "نهر اللوار", "نهر الرون", "نهر غارون"], ["Seine River", "Loire River", "Rhône River", "Garonne River"], ["La Seine", "La Loire", "Le Rhône", "La Garonne"], 0,
         "يمر نهر السين في قلب باريس وتقع في وسطه جزيرة إيل دو لا سيتي التاريخية حيث بنيت نوتردام.", "The Seine meanders through Paris, dividing it into Left and Right banks.", "La Seine serpente au cœur de Paris et entoure l'île de la Cité.", "easy"),

        ("ما هو النهر الإيطالي الشهير الذي يمر عبر العاصمة روما؟", "Which historic Italian river flows through the capital city of Rome?", "Quel fleuve historique italien traverse la capitale Rome ?",
         ["نهر التيبر", "نهر بو", "نهر أرنو", "نهر أديجي"], ["Tiber River", "Po River", "Arno River", "Adige River"], ["Le Tibre", "Le Pô", "L'Arno", "L'Adige"], 0,
         "نشأت روما القديمة على ضفاف نهر التيبر وتلاله السبعة التاريخية.", "Rome was founded on the banks of the Tiber River.", "Rome a été fondée sur les rives du Tibre.", "easy"),

        ("ما هي البحيرة العظمى الواقعة في إفريقيا وتعد ثاني أكبر بحيرة مياه عذبة في العالم من حيث المساحة؟", "Which African Great Lake is the world's second-largest freshwater lake by surface area?", "Quel grand lac africain est le deuxième plus vaste lac d'eau douce au monde ?",
         ["بحيرة فيكتوريا", "بحيرة تنجانيقا", "بحيرة ملاوي", "بحيرة تشاد"], ["Lake Victoria", "Lake Tanganyika", "Lake Malawi", "Lake Chad"], ["Lac Victoria", "Lac Tanganyika", "Lac Malawi", "Lac Tchad"], 0,
         "تتقاسم بحيرة فيكتوريا كل من تنزانيا وأوغندا وكينيا وهي المنبع الرئيسي لنيل فيكتوريا الأبيض.", "Lake Victoria is shared by Tanzania, Uganda, and Kenya.", "Le lac Victoria est partagé entre la Tanzanie, l'Ouganda et le Kenya.", "easy"),

        ("في أي مدينة أسترالية يقع مبنى دار الأوبرا الشهير بتصميمه المستوحى من الأشرعة البيضاء؟", "In which Australian city is the iconic Opera House located with its shell-sail design?", "Dans quelle ville australienne se trouve l'Opéra au design inspiré de voiles marines ?",
         ["سيدني", "ملبورن", "كانبرا", "بيرث"], ["Sydney", "Melbourne", "Canberra", "Perth"], ["Sydney", "Melbourne", "Canberra", "Perth"], 0,
         "صمم دار أوبرا سيدني المعماري الدنماركي يورن أوتزون وتطل على ميناء سيدني وجسر الميناء الشهير.", "Sydney Opera House was designed by Danish architect Jørn Utzon.", "L'Opéra de Sydney a été conçu par l'architecte danois Jørn Utzon.", "easy"),

        ("ما هو الخليج المائي الذي تطل عليه دول المكسيك والولايات المتحدة وكوبا؟", "Which large body of water is bordered by Mexico, the United States, and Cuba?", "Quelle vaste étendue d'eau est bordée par le Mexique, les États-Unis et Cuba ?",
         ["خليج المكسيك", "البحر الكاريبي", "خليج كاليفورنيا", "خليج هدسون"], ["Gulf of Mexico", "Caribbean Sea", "Gulf of California", "Hudson Bay"], ["Golfe du Mexique", "Mer des Caraïbes", "Golfe de Californie", "Baie d'Hudson"], 0,
         "يعد خليج المكسيك تاسع أكبر مسطح مائي في العالم ويتصل بالمحيط الأطلسي عبر مضيق فلوريدا.", "The Gulf of Mexico is connected to the Atlantic via Straits of Florida.", "Le golfe du Mexique communique avec l'Atlantique par le détroit de Floride.", "easy")
    ]

    for m in more_geography:
        items.append({
            "diff": m[10],
            "q": {"ar": m[0], "en": m[1], "fr": m[2]},
            "opts": {"ar": m[3], "en": m[4], "fr": m[5]},
            "ans": m[6],
            "exp": {"ar": m[7], "en": m[8], "fr": m[9]}
        })

    # Ensure exactly 100 questions
    items = items[:100]
    
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "geography",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_geography(101)
    print(f"Generated {len(qs)} geography questions.")
    assert len(qs) == 100
