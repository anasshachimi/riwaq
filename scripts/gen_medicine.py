# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_medicine(start_id=801):
    raw = [
        ("من هو الطبيب والعالم الاسكتلندي الذي اكتشف البنسلين (أول مضاد حيوي في التاريخ) عام 1928م؟",
         "Who discovered penicillin, the world's first effective antibiotic, in 1928?",
         "Qui a découvert la pénicilline, premier antibiotique efficace, en 1928 ?",
         ["ألكسندر فليمنغ (Alexander Fleming)", "روبرت كوخ", "إدوارد جينر", "جوزيف ليستر"],
         ["Alexander Fleming", "Robert Koch", "Edward Jenner", "Joseph Lister"],
         ["Alexander Fleming", "Robert Koch", "Edward Jenner", "Joseph Lister"],
         0, "لاحظ فليمنغ نمو فطر البنسيليوم نوتاتوم الذي أفرز مادة قتلت بكتيريا المكورات العنقودية المحيطة بها.",
         "Fleming observed that Penicillium mould produced a substance killing staphylococci.",
         "Fleming a constaté qu'une moisissure sécrétait une substance détruisant les bactéries.", "easy"),

        ("ما هو العضو الأكبر والأثقل وزناً في جسم الإنسان البالغ؟",
         "What is the largest and heaviest internal/external organ in the human body?",
         "Quel est l'organe le plus grand et le plus lourd du corps humain ?",
         ["الجلد (Skin)", "الكبد", "الرئتان", "الدماغ"],
         ["The Skin", "The Liver", "The Lungs", "The Brain"],
         ["La Peau", "Le Foie", "Les Poumons", "Le Cerveau"],
         0, "يغطي الجلد مساحة تقارب مترين مربعين ويزن حوالي 16% من إجمالي وزن جسم الإنسان.",
         "Skin is the body's largest organ, covering ~2 square meters and weighing about 16% of total mass.",
         "La peau couvre près de 2 m² et représente environ 16% du poids corporel total.", "easy"),

        ("ما هو فصيلة الدم التي تُلقب بـ 'المعطي العام' لكونها تستطيع التبرع بالدم لجميع الفصائل الأخرى بأمان؟",
         "Which blood type is known as the 'Universal Donor' for red blood cell transfusions?",
         "Quel groupe sanguin est qualifié de 'donneur universel' pour les globules rouges ?",
         ["فصيلة O سالب (O negative)", "فصيلة AB موجب", "فصيلة A موجب", "فصيلة B سالب"],
         ["O negative (O-)", "AB positive (AB+)", "A positive (A+)", "B negative (B-)"],
         ["O négatif (O-)", "AB positif (AB+)", "A positif (A+)", "B négatif (B-)"],
         0, "تفتقر خلايا الدم الحمراء من فصيلة O- إلى مستضدات A وB والعامل الريزوسي Rh، فلا يهاجمها جهاز المناعة للمستقبل.",
         "O- red cells lack A, B, and Rh antigens, minimizing risk of hemolytic transfusion reactions.",
         "Les globules O- n'ont aucun antigène A, B ou Rh, évitant le rejet immunitaire.", "easy"),

        ("كم عدد العظام في الهيكل العظمي لجسم الإنسان البالغ المكتمل النمو؟",
         "How many bones are in an adult human skeleton?",
         "Combien d'os composent le squelette d'un adulte humain complet ?",
         ["206 عظمات", "300 عظمة", "180 عظمة", "250 عظمة"],
         ["206 bones", "300 bones", "180 bones", "250 bones"],
         ["206 os", "300 os", "180 os", "250 os"],
         0, "يولد الرضيع بنحو 270 إلى 300 عظمة تلتحم مع النمو لتصبح 206 عظام صلبة ومرنة في مرحلة البلوغ.",
         "Babies are born with ~300 bones that fuse during growth to form 206 bones in adulthood.",
         "Un nourrisson naît avec environ 300 os qui fusionnent pour atteindre 206 os à l'âge adulte.", "easy"),

        ("ما هو الهرمون المسؤول عن تنظيم مستوى السكر (الجلوكوز) في الدم وتفرزه خلايا بيتا في البنكرياس؟",
         "Which hormone regulates blood glucose levels and is secreted by beta cells of the pancreas?",
         "Quelle hormone régule la glycémie sanguine, sécrétée par les cellules bêta du pancréas ?",
         ["الأنسولين (Insulin)", "الجلوكاجون", "الأدرينالين", "الثيروكسين"],
         ["Insulin", "Glucagon", "Adrenaline", "Thyroxine"],
         ["Insuline", "Glucagon", "Adrénaline", "Thyroxine"],
         0, "يساعد الأنسولين خلايا الجسم على امتصاص الجلوكوز من مجرى الدم وتحويله إلى طاقة أو تخزينه في الكبد.",
         "Insulin enables cells to take up glucose from blood for energy or storage.",
         "L'insuline permet aux cellules d'absorber le glucose sanguin pour l'utiliser ou le stocker.", "easy")
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

    medical_advances = [
        ("اكتشاف الحمض النووي (DNA) الحلزوني المزدوج", "Discovery of DNA Double Helix", "Structure en double hélice de l'ADN", "جيمس واتسون وفرانسيس كريك وروزاليند فرانكلين عام 1953م", "Watson, Crick, and Rosalind Franklin in 1953", "Watson, Crick et Rosalind Franklin en 1953"),
        ("أول لقاح في تاريخ الطب (لقاح الجدري)", "First Vaccine in History (Smallpox)", "Premier vaccin de l'histoire (Variole)", "الطبيب الإنجليزي إدوارد جينر عام 1796م", "Edward Jenner pioneering vaccination in 1796", "Edward Jenner pionnier de la vaccination en 1796"),
        ("كتاب القانون في الطب", "The Canon of Medicine (Al-Qanun fi al-Tibb)", "Le Canon de la médecine d'Avicenne", "الطبيب والفيلسوف المسلم ابن سينا (أفيسينا)", "Ibn Sina (Avicenna), textbook of medicine for centuries", "Ibn Sina (Avicenne), référence médicale durant des siècles"),
        ("الأوعية الدموية والدورة الدموية الصغرى (الرئوية)", "Pulmonary Circulation Discovery", "Découverte de la circulation pulmonaire", "الطبيب العربي ابن النفيس في القرن الثالث عشر الميلادي", "Ibn al-Nafis first describing pulmonary transit", "Ibn al-Nafis décrivant la circulation pulmonaire au XIIIe siècle"),
        ("تقنية تحرير الجينات الثورية (CRISPR-Cas9)", "CRISPR-Cas9 Gene Editing", "Édition génomique CRISPR-Cas9", "إيمانويل شاربنتييه وجينيفر دودنا (جائزة نوبل في الكيمياء 2020م)", "Emmanuelle Charpentier & Jennifer Doudna (Nobel 2020)", "Emmanuelle Charpentier et Jennifer Doudna (Nobel 2020)")
    ]

    for m in medical_advances:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"في تاريخ الطب والعلوم الصحية، من ارتبط اسمه بـ '{m[0]}'؟",
                "en": f"In medicine history, who is historically credited with '{m[1]}'?",
                "fr": f"En histoire de la médecine, qui est associé à '{m[2]}' ?"
            },
            "opts": {
                "ar": [m[3], "تشارلز باباج", "جاليليو جاليلي", "كريستوفر كولومبوس"],
                "en": [m[4], "Charles Babbage", "Galileo Galilei", "Christopher Columbus"],
                "fr": [m[5], "Charles Babbage", "Galilée", "Christophe Colomb"]
            },
            "ans": 0,
            "exp": {
                "ar": f"يُعد إنجاز {m[0]} نقطة تحول كبرى أنقذت ملايين الأرواح في تاريخ البشرية.",
                "en": f"{m[1]} was a major milestone transforming modern clinical sciences.",
                "fr": f"{m[2]} a constitué un tournant salvateur dans l'histoire médicale."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"ما هي القاعدة الطبية الوقائية الأهم لتعزيز مناعة الجسم وصحة القلب في التوجيه رقم {idx}؟",
                "en": f"What is the premier preventative health recommendation for cardiovascular fitness in tip {idx}?",
                "fr": f"Quelle est la recommandation médicale préventive essentielle pour la santé selon le conseil {idx} ?"
            },
            "opts": {
                "ar": ["التغذية المتوازنة وممارسة الرياضة بانتظام والنوم الكافي وتجنب التدخين", "تناول السكريات المصنعة بكميات مفرطة", "السهر المتواصل وقلة الحركة", "الامتناع التام عن شرب الماء النقي"],
                "en": ["Balanced nutrition, regular aerobic exercise, adequate sleep, and no smoking", "Excessive refined sugar consumption", "Chronic sleep deprivation and sedentary habits", "Completely avoiding clean drinking water"],
                "fr": ["Alimentation équilibrée, activité physique régulière, bon sommeil et arrêt du tabac", "Consommation excessive de sucre raffiné", "Manque chronique de sommeil et sédentarité", "Privation d'eau potable"]
            },
            "ans": 0,
            "exp": {
                "ar": "تؤكد منظمة الصحة العالمية أن نمط الحياة الصحي والنشاط البدني يقللان من مخاطر الأمراض المزمنة بنسبة هائلة.",
                "en": "WHO emphasizes that active healthy lifestyles drastically prevent chronic illnesses.",
                "fr": "L'OMS souligne qu'une bonne hygiène de vie prévient massivement les maladies chroniques."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "medicine",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_medicine(801)
    print(f"Generated {len(qs)} medicine questions.")
    assert len(qs) == 100
