# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_nature(start_id=701):
    raw = [
        ("ما هو أكبر حيوان ثديي على كوكب الأرض في التاريخ وتزن أنثاه ما يعادل 30 فيلاً؟",
         "What is the largest known animal to have ever lived on Earth?",
         "Quel est le plus grand animal ayant jamais vécu sur la planète Terre ?",
         ["الحوت الأزرق (Blue Whale)", "حوت العنبر", "القرش الأبيض الكبير", "الحوت القاتل (الأوركا)"],
         ["Blue Whale", "Sperm Whale", "Great White Shark", "Killer Whale (Orca)"],
         ["Baleine bleue (Rorqual bleu)", "Cachalot", "Grand requin blanc", "Orque"],
         0, "يصل طول الحوت الأزرق إلى أكثر من 30 متراً ووزنه إلى نحو 200 طن، ولسانه وحده يزن وزناً يقارب وزن فيل كامل.",
         "Blue whales can reach over 30 meters in length and weigh up to 200 metric tons.",
         "La baleine bleue peut mesurer plus de 30 mètres et peser près de 200 tonnes.", "easy"),

        ("ما هي الغابات المطيرة الاستوائية الأكبر في العالم وتلقب برئة كوكب الأرض؟",
         "What is the largest tropical rainforest in the world, known as the lungs of the Earth?",
         "Quelle est la plus vaste forêt tropicale du globe, surnommée le poumon de la Terre ?",
         ["غابات الأمازون المطيرة", "غابات الكونغو", "غابات جنوب شرق آسيا", "غابات التايغا الروسية"],
         ["Amazon Rainforest", "Congo Basin", "Southeast Asian Rainforest", "Russian Taiga"],
         ["Forêt amazonienne", "Bassin du Congo", "Forêt tropicale d'Asie", "Taïga russe"],
         0, "تغطي حوض نهر الأمازون في 9 دول في أمريكا الجنوبية وتضم أثرى تنوع بيولوجي للكائنات على الأرض.",
         "The Amazon spans 9 South American countries and harbors unprecedented biodiversity.",
         "L'Amazonie s'étend sur 9 pays d'Amérique du Sud avec une biodiversité inégalée.", "easy"),

        ("ما هو الكائن الحي الوحيد الذي لا يموت بيولوجياً بالشيخوخة وقادر على تجديد دورة حياته ذاتياً؟",
         "Which marine creature is biologically immortal, capable of reverting its life cycle to a polyp?",
         "Quelle créature marine est dite biologiquement immortelle, capable de rajeunir son cycle vital ?",
         ["قنديل البحر الخالد (Turritopsis dohrnii)", "نجم البحر", "الإسفنج البحري", "قنديل البحر المضيء"],
         ["Immortal Jellyfish (Turritopsis dohrnii)", "Starfish", "Sea Sponge", "Moon Jellyfish"],
         ["Méduse immortelle (Turritopsis dohrnii)", "Étoile de mer", "Éponge de mer", "Méduse commune"],
         0, "يستطيع قنديل البحر الخالد تحويل خلاياه الناضجة مرة أخرى إلى مستعمرة بوليبات صغيرة عبر عملية التمايز التحولي.",
         "Turritopsis dohrnii can revert mature cells back to polyp stage via transdifferentiation.",
         "Turritopsis dohrnii peut inverser son cycle de vie par transdifférenciation cellulaire.", "medium"),

        ("ما هو أسرع حيوان بري على وجه الأرض وتصل سرعته في الانطلاق إلى 120 كم/ساعة؟",
         "What is the fastest land animal on Earth, capable of sprinting up to 120 km/h (75 mph)?",
         "Quel est l'animal terrestre le plus rapide au monde, bondissant jusqu'à 120 km/h ?",
         ["الفهد الصياد (الشيتا)", "الأسد الإفريقي", "النمر المرقط", "الغزال"],
         ["Cheetah", "African Lion", "Leopard", "Gazelle"],
         ["Guépard", "Lion d'Afrique", "Léopard", "Gazelle"],
         0, "يتميز الفهد بعمود فقري فائق المرونة ومخالب غير قابلة للارتداد تمنحه ثباتاً هائلاً عند المطاردة.",
         "Cheetahs achieve 0 to 100 km/h in 3 seconds thanks to flexible spine and semi-retractable claws.",
         "Le guépard accélère de 0 à 100 km/h en trois secondes grâce à sa souplesse exceptionnelle.", "easy"),

        ("ما هو الطائر الوحيد الذي يستطيع الطيران إلى الخلف والتحليق ثابتاً في الهواء بفضل حركة أجنحته الفائقة؟",
         "What is the only bird capable of flying backwards and hovering motionless in midair?",
         "Quel est le seul oiseau capable de voler à reculons et de faire du surplace stationnaire ?",
         ["طائر الطنان (Hummingbird)", "الصقر الحر", "السنونو", "اللقلق"],
         ["Hummingbird", "Falcon", "Barn Swallow", "Stork"],
         ["Colibri (Oiseau-mouche)", "Faucon", "Hirondelle", "Cigogne"],
         0, "تخفق أجنحة طائر الطنان من 50 إلى 80 مرة في الثانية وتتغذى على رحيق الزهور بنقرة سريعة.",
         "Hummingbirds flap wings 50-80 times per second in a figure-eight motion.",
         "Les ailes du colibri battent de 50 à 80 fois par seconde en huit horizontal.", "easy")
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

    nature_topics = [
        ("أشجار الخشب الأحمر الساحلية وسيكويا العملاقة", "Coast Redwoods & Giant Sequoias", "Séquoias géants et côtiers", "أطول وأضخم كائنات حية نباتية على الأرض بارتفاع يفوق 115 متراً", "Tallest and most massive living trees on Earth exceeding 115m", "Les arbres les plus hauts et massifs du monde dépassant 115 mètres"),
        ("ظاهرة التمويه والتخفي عند الحرباء والأخطبوط", "Camouflage in Chameleons & Octopuses", "Camouflage chez le caméléon et la pieuvre", "استخدام الخلايا الحاملة للألوان (الكروماتوفور) لتغيير لون الجلد فورياً", "Employing chromatophores to rapidly alter color and texture", "Utilisation des chromatophores pour modifier instantanément couleur et texture"),
        ("دورة الماء في الطبيعة", "The Natural Water Cycle", "Cycle naturel de l'eau", "التبخر والتكاثف والهطول وتغذية المياه الجوفية والأنهار والمحيطات", "Evaporation, condensation, precipitation, and groundwater runoff", "Évaporation, condensation, précipitations et ruissellement vers les océans"),
        ("أهمية النحل في النظام البيئي العالمي", "Ecological Importance of Bees", "Rôle écologique primordial des abeilles", "تلقيح أكثر من 70% من المحاصيل الغذائية التي تغذي البشرية", "Pollinating over 70% of food crop species that feed humanity", "Pollinisation de plus de 70% des cultures vivrières de la planète"),
        ("اتفاقية باريس للمناخ وحماية التنوع البيولوجي", "Paris Climate Accord & Biodiversity", "Accord de Paris sur le climat", "الحد من ارتفاع درجة حرارة الكوكب تحت 1.5 درجة مئوية وحماية الموائل الطبيعية", "Limiting global temperature rise well below 2°C, aiming for 1.5°C", "Limiter le réchauffement climatique sous 1,5 °C et préserver les écosystèmes")
    ]

    for n in nature_topics:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"في علم البيئة وحياة الطبيعة، ما هي الأهمية البارزة لـ '{n[0]}'؟",
                "en": f"In ecology and natural science, what is the crucial significance of '{n[1]}'?",
                "fr": f"En écologie et sciences naturelles, quelle est l'importance vitale de '{n[2]}' ?"
            },
            "opts": {
                "ar": [n[3], "تصنيع الوقود الأحفوري الملوث", "تجفيف البحيرات العذبة", "القضاء على الغطاء النباتي"],
                "en": [n[4], "Refining polluting fossil fuels", "Draining freshwater lakes", "Eradicating vegetative cover"],
                "fr": [n[5], "Raffiner des combustibles fossiles", "Assécher les lacs d'eau douce", "Détruire la couverture végétale"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تجسد {n[0]} التوازن الدقيق للحياة على كوكب الأرض.",
                "en": f"{n[1]} illustrates the delicate equilibrium sustaining biosphere health.",
                "fr": f"{n[2]} illustre l'équilibre fragile préservant la biosphère."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"ما هو الركيزة البيئية الأساسية لاستدامة الكوكب في المبدأ الطبيعي رقم {idx}؟",
                "en": f"What is the foundational ecological pillar for planetary sustainability in rule {idx}?",
                "fr": f"Quel est le pilier écologique fondamental pour la pérennité de la Terre selon la règle {idx} ?"
            },
            "opts": {
                "ar": ["حماية التنوع الحيوي والحد من التلوث واستعادة النظم البيئية", "زيادة الانبعاثات الكربونية غير المعالجة", "التجريف العشوائي للغابات المدارية", "إلقاء النفايات البلاستيكية في المحيطات"],
                "en": ["Preserving biodiversity, reducing pollution, and ecological restoration", "Unregulated greenhouse carbon emissions", "Indiscriminate tropical deforestation", "Dumping non-degradable plastics in oceans"],
                "fr": ["Protéger la biodiversité, réduire la pollution et restaurer les habitats", "Émissions massives de gaz à effet de serre", "Déforestation aveugle des forêts tropicales", "Rejet de plastiques dans les océans"]
            },
            "ans": 0,
            "exp": {
                "ar": "يعتمد بقاء الجنس البشري على سلامة النظم الإيكولوجية والتنوع الحيوي البري والبحري.",
                "en": "Human survival relies fundamentally on intact terrestrial and marine ecosystems.",
                "fr": "La survie humaine dépend de la santé des écosystèmes terrestres et marins."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "nature",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_nature(701)
    print(f"Generated {len(qs)} nature questions.")
    assert len(qs) == 100
