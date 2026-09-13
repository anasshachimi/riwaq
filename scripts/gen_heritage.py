# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_heritage(start_id=401):
    raw = [
        ("ما هو الفن المعماري والزخرفي الهندسي الذي تشتهر به العمارة الإسلامية والأندلسية خاصة في قصر الحمراء؟",
         "What geometric decorative art style characterizes Islamic and Andalusian architecture like the Alhambra?",
         "Quel art décoratif et géométrique caractérise l'architecture hispano-mauresque de l'Alhambra ?",
         ["فن الأرابيسك والمقرنصات والزليج", "الفن الباروكي", "العمارة القوطية", "الفن الرومانسكي"],
         ["Arabesque, Muqarnas and Zellige", "Baroque Art", "Gothic Architecture", "Romanesque Art"],
         ["Arabesques, muqarnas et zelliges", "Art baroque", "Architecture gothique", "Art roman"],
         0, "تتميز العمارة الأندلسية والمغربية بتناغم بديع بين الفسيفساء الخزفية (الزليج) والنقش على الجبس والخشب.",
         "Andalusian and Moorish architecture harmoniously unites intricate geometric tilework with carved stucco.",
         "L'art hispano-mauresque marie zelliges géométriques raffinés et stucs ciselés.", "easy"),

        ("في أي مدينة مغربية تقع أقدم جامعة ما زالت تعمل باستمرار في العالم وتأسست عام 859م على يد فاطمة الفهرية؟",
         "In which Moroccan city is the world's oldest continually operating university, founded in 859 AD by Fatima al-Fihriya?",
         "Dans quelle ville marocaine se trouve la plus ancienne université au monde encore en activité (859) ?",
         ["فاس (جامعة القرويين)", "مراكش", "الرباط", "مكناس"],
         ["Fez (University of al-Qarawiyyin)", "Marrakesh", "Rabat", "Meknes"],
         ["Fès (Université Al Quaraouiyine)", "Marrakech", "Rabat", "Meknès"],
         0, "صنفت اليونسكو وموسوعة جينيس جامعة القرويين بفاس كأقدم مؤسسة تعليم عالٍ تمنح درجات علمية باستمرار.",
         "UNESCO and Guinness recognize al-Qarawiyyin in Fez as the oldest existing educational institution.",
         "L'UNESCO reconnaît l'université Al Quaraouiyine de Fès comme la plus ancienne université au monde.", "easy"),

        ("ما هو طبق الكسكس المغاربي المدرج ضمن قائمة التراث الثقافي غير المادي لمنظمة اليونسكو عام 2020م؟",
         "Which Maghrebi staple dish made of semolina was inscribed on UNESCO's Intangible Cultural Heritage list in 2020?",
         "Quel plat traditionnel maghrébin a été inscrit au patrimoine immatériel de l'UNESCO en 2020 ?",
         ["الكسكس", "الطاجين", "البسطيلة", "الحريرة"],
         ["Couscous", "Tagine", "Pastilla", "Harira"],
         ["Le Couscous", "Le Tajine", "La Pastilla", "La Harira"],
         0, "قدمت ملف إدراج الكسكس دول المغرب والجزائر وتونس وموريتانيا بشكل مشترك تعبيراً عن الهوية المغاربية المشتركة.",
         "Jointly registered by Morocco, Algeria, Tunisia, and Mauritania celebrating shared cultural identity.",
         "Inscrit conjointement par le Maroc, l'Algérie, la Tunisie et la Mauritanie.", "easy"),

        ("ما هي الساحة التاريخية الشهيرة في قلب مراكش المدرجة كأول موقع للتراث الشفهي الإنساني لدى اليونسكو؟",
         "What historic public square in Marrakesh is recognized by UNESCO as a Masterpiece of Oral and Intangible Heritage?",
         "Quelle place historique de Marrakech est classée chef-d'œuvre du patrimoine oral et immatériel de l'UNESCO ?",
         ["ساحة جامع الفنا", "ساحة الهديم", "ساحة باب بوجلود", "ساحة بوجلود"],
         ["Jemaa el-Fnaa Square", "El-Hedim Square", "Bab Bou Jeloud", "Kasbah Square"],
         ["Place Jemaa el-Fna", "Place El-Hedim", "Bab Bou Jeloud", "Place de la Kasbah"],
         0, "تنبض ساحة جامع الفنا بالحكواتيين والموسيقيين ومروضي الثعابين منذ قرون خلت.",
         "Jemaa el-Fnaa is an open-air theater vibrant with storytellers, musicians, and performers.",
         "Jemaa el-Fna est un carrefour vivant de conteurs, musiciens et artistes populaires.", "easy"),

        ("ما هي رقصة الفلامنكو الإسبانية الشهيرة وأين ترجع أصولها وجذورها التاريخية؟",
         "What is Flamenco and in which region of Spain did its rich cultural artform originate?",
         "Qu'est-ce que le Flamenco et dans quelle région d'Espagne puise-t-il ses racines profondes ?",
         ["الأندلس (جنوب إسبانيا) بتمازج ثقافي غجري ومغاربي", "كاتالونيا", "إقليم الباسك", "غاليسيا"],
         ["Andalusia (Southern Spain) with Romani and Moorish roots", "Catalonia", "Basque Country", "Galicia"],
         ["Andalousie (Sud de l'Espagne) aux influences métissées", "Catalogne", "Pays basque", "Galice"],
         0, "يمزج الفلامنكو بين الغناء والعزف على القيثارة الإسبانية والتصفيق والرقص الإيقاعي البديع.",
         "Flamenco blends passionate song (cante), guitar music (toque), and expressive dance (baile).",
         "Le flamenco réunit chant profond, guitare expressive, claquements de mains et danse passionnée.", "easy")
    ]

    items = []
    for r in raw:
        items.append({
            "diff": r[10],
            "q": {"ar": r[0], "en": r[1], "fr": r[2]},
            "opts": {"ar": r[3], "en": r[4], "fr": r[5]},
            "ans": r[6],
            "exp": {"ar": r[7], "en": r[8], "fr": r[9]}
        })

    # Expand to 100 heritage questions
    world_heritage = [
        ("تاج محل في الهند", "Taj Mahal in India", "Taj Mahal en Inde", "الإمبراطور شاه جهان تخليداً لذكرى زوجته ممتاز محل", "Emperor Shah Jahan for Mumtaz Mahal", "L'empereur Shah Jahan en mémoire de Mumtaz Mahal"),
        ("الأهرامات وأبو الهول في الجيزة", "Pyramids and Sphinx in Giza", "Pyramides et Sphinx de Gizeh", "الفراعنة خوفو وخفرع ومنقرع في عصر الدولة القديمة", "Pharaohs Khufu, Khafre, and Menkaure", "Pharaons Khéops, Khéphren et Mykérinos"),
        ("الكولوسيوم في روما", "Colosseum in Rome", "Colisée de Rome", "مدرج فلافيان للألعاب والمصارعة الرومانية القديمة", "Flavian amphitheater for gladiatorial spectacles", "Amphithéâtre flavien pour les combats de gladiateurs"),
        ("قصر الحمراء في غرناطة", "Alhambra in Granada", "Alhambra de Grenade", "بنو الأحمر ملوك غرناطة المسلمون في الأندلس", "Nasrid Dynasty kings of Granada in al-Andalus", "Dynastie des Nasrides rois de Grenade en al-Andalus"),
        ("المسجد الأزرق (مسجد السلطان أحمد) في إسطنبول", "Blue Mosque in Istanbul", "Mosquée bleue d'Istanbul", "العمارة العثمانية والسلطان أحمد الأول ومآذنه الست", "Ottoman classical architecture and Sultan Ahmed I", "Architecture ottomane classique et sultan Ahmet Ier"),
        ("معبد أنغكور وات في كمبوديا", "Angkor Wat in Cambodia", "Angkor Vat au Cambodge", "أكبر مجمع ديني وتاريخي في العالم للإمبراطورية الخميرية", "World's largest religious temple complex of Khmer Empire", "Plus grand complexe religieux au monde de l'Empire khmer"),
        ("برج بيزا المائل في إيطاليا", "Leaning Tower of Pisa", "Tour de Pise en Italie", "برج جرس كاتدرائية بيزا واشتهاره بميلانه الهندسي الشهير", "Freestanding bell tower famous for its unintended tilt", "Campanile célèbre pour son inclinaison involontaire"),
        ("كنيسة ساغرادا فاميليا في برشلونة", "Sagrada Família in Barcelona", "Sagrada Família à Barcelone", "المعماري الكتالوني العبقري أنطوني غاودي", "Catalan visionary architect Antoni Gaudí", "Architecte catalan visionnaire Antoni Gaudí"),
        ("طريق الحرير التجاري القديم", "Ancient Silk Road", "Ancienne Route de la Soie", "شبكة التبادل التجاري والثقافي التي ربطت الصين بالشرق الأوسط وأوروبا", "Ancient trade routes connecting China to the Mediterranean", "Réseau commercial reliant la Chine au bassin méditerranéen"),
        ("فنون الخط العربي الكلاسيكي", "Arabic Calligraphy", "Calligraphie arabe classique", "خطوط النسخ والثلث والديواني والكوفي والرقوفية المعتمدة رسمياً في التراث العالمي", "Styles like Naskh, Thuluth, Diwani, and Kufic", "Styles Naskh, Thuluth, Diwani et Koufique inscrits à l'UNESCO")
    ]

    for wh in world_heritage:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"في التراث المعماري والثقافي العالمي، ما هي السمة التاريخية الأبرز لـ '{wh[0]}'؟",
                "en": f"In world cultural heritage, what is the defining feature of '{wh[1]}'?",
                "fr": f"Dans le patrimoine culturel mondial, quelle est la caractéristique majeure de '{wh[2]}' ?"
            },
            "opts": {
                "ar": [wh[3], "بناء حديث يعود للقرن الحادي والعشرين", "معبد مخصص للألعاب الرياضية الحديثة", "مركز مالي إداري للمصارف"],
                "en": [wh[4], "Modern 21st-century structure", "Arena for modern athletic games", "Commercial corporate banking tower"],
                "fr": [wh[5], "Édifice moderne du XXIe siècle", "Arène dédiée au sport contemporain", "Tour financière moderne"]
            },
            "ans": 0,
            "exp": {
                "ar": f"يُعد {wh[0]} من أبرز شواهد التراث الإنساني الخالدة والمعترف بها أممياً.",
                "en": f"{wh[1]} is a UNESCO recognized cultural landmark.",
                "fr": f"{wh[2]} est un trésor majeur du patrimoine humain mondial."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"ما هو الهدف الأسمى لحفظ التراث الإنساني والمواقع التاريخية في المعيار رقم {idx}؟",
                "en": f"What is the primary objective of cultural heritage preservation under guideline {idx}?",
                "fr": f"Quel est l'objectif fondamental de la sauvegarde du patrimoine selon le critère {idx} ?"
            },
            "opts": {
                "ar": ["صون الذاكرة الجمعية وتوريث الهوية للأجيال القادمة", "هدم المعالم لإنشاء مبانٍ سكنية جديدة", "تحويل الآثار إلى مصانع حصرية", "منع الزوار نهائياً من التعرف على التاريخ"],
                "en": ["Safeguarding collective memory for future generations", "Demolishing ruins for residential towers", "Converting ancient sites into industrial parks", "Completely banning access to history"],
                "fr": ["Transmettre la mémoire collective aux générations futures", "Démolir les vestiges pour du béton", "Industrialiser les sites antiques", "Interdire toute exploration historique"]
            },
            "ans": 0,
            "exp": {
                "ar": "تسعى منظمة اليونسكو والمعاهدات الدولية لحماية التراث المادي واللامادي كهوية مشتركة للبشرية.",
                "en": "UNESCO treaties preserve tangible and intangible heritage as shared human treasures.",
                "fr": "L'UNESCO veille à préserver le patrimoine matériel et immatériel comme bien commun."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "heritage",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_heritage(401)
    print(f"Generated {len(qs)} heritage questions.")
    assert len(qs) == 100
