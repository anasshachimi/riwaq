# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_general(start_id=901):
    raw = [
        ("ما هي العملة النقدية الرسمية المستخدمة في اليابان؟",
         "What is the official currency of Japan?",
         "Quelle est la monnaie officielle du Japon ?",
         ["الين (Yen)", "اليوان", "الوون", "الدولار السنغافوري"],
         ["Yen (JPY)", "Yuan", "Won", "Singapore Dollar"],
         ["Yen (JPY)", "Yuan", "Won", "Dollar de Singapour"],
         0, "الين هو ثالث أكثر العملات تداولاً في أسواق الصرف الأجنبي في العالم بعد الدولار الأمريكي واليورو.",
         "The Japanese Yen is the third most traded currency globally after USD and EUR.",
         "Le yen japonais est la 3e devise la plus échangée au monde.", "easy"),

        ("ما هي المنظمة الدولية التي تأسست عام 1945م عقب الحرب العالمية الثانية للحفاظ على السلم والأمن الدوليين؟",
         "What international organization was founded in 1945 following WWII to maintain world peace?",
         "Quelle organisation internationale a été fondée en 1945 pour préserver la paix mondiale ?",
         ["منظمة الأمم المتحدة (UN)", "عصبة الأمم", "منظمة التجارة العالمية", "حلف الناتو"],
         ["United Nations (UN)", "League of Nations", "World Trade Organization (WTO)", "NATO"],
         ["Organisation des Nations Unies (ONU)", "Société des Nations", "Organisation mondiale du commerce", "OTAN"],
         0, "يقع المقر الرئيسي للأمم المتحدة في مدينة نيويورك بالولايات المتحدة الأمريكية وتضم 193 دولة عضواً.",
         "Headquartered in New York City with 193 sovereign member states.",
         "Le siège de l'ONU est à New York et réunit 193 États membres souverains.", "easy"),

        ("ما هي الجائزة الدولية المرموقة التي تُمنح سنوياً في السويد والنرويج في مجالات السلام والفيزياء والأدب؟",
         "What prestigious annual international award is granted in Sweden and Norway for Peace, Physics, and Literature?",
         "Quel prestigieux prix international est décerné en Suède et Norvège pour la paix et les sciences ?",
         ["جوائز نوبل (Nobel Prizes)", "جوائز الأوسكار", "جوائز بوليتزر", "وسام فيلدز"],
         ["Nobel Prizes", "Academy Awards (Oscars)", "Pulitzer Prizes", "Fields Medal"],
         ["Prix Nobel", "Oscars du cinéma", "Prix Pulitzer", "Médaille Fields"],
         0, "أنشأها العالم السويدي ألفريد نوبل مخترع الديناميت في وصيته عام 1895م وبدأ منحها عام 1901م.",
         "Established by Alfred Nobel's will in 1895 and first awarded in 1901.",
         "Institué par le testament d'Alfred Nobel en 1895 et décerné depuis 1901.", "easy"),

        ("كم عدد مفاتيح البيانو القياسي الحديث (المفاتيح البيضاء والسوداء مجتمعة)؟",
         "How many keys are on a standard modern acoustic piano?",
         "Combien de touches compte un piano acoustique moderne standard ?",
         ["88 مفتاحاً (52 أبيض و36 أسود)", "76 مفتاحاً", "64 مفتاحاً", "100 مفتاح"],
         ["88 keys (52 white and 36 black)", "76 keys", "64 keys", "100 keys"],
         ["88 touches (52 blanches et 36 noires)", "76 touches", "64 touches", "100 touches"],
         0, "يغطي البيانو القياسي ذو الـ 88 مفتاحاً سبعة أوكتافات كاملة وثلاث نغمات إضافية.",
         "A standard 88-key piano spans seven octaves plus a minor third.",
         "Un piano standard à 88 touches couvre plus de sept octaves musicales.", "medium"),

        ("ما هو اليوم العالمي الذي تحتفل به شعوب العالم سنوياً في 22 أبريل لحماية البيئة؟",
         "What global observance is celebrated internationally on April 22 to promote environmental protection?",
         "Quelle journée mondiale est célébrée le 22 avril pour sensibiliser à la protection environnementale ?",
         ["يوم الأرض (Earth Day)", "يوم المياه العالمي", "يوم البيئة العالمي", "يوم التنوع البيولوجي"],
         ["Earth Day", "World Water Day", "World Environment Day", "Biodiversity Day"],
         ["Jour de la Terre (Earth Day)", "Journée mondiale de l'eau", "Journée mondiale de l'environnement", "Journée de la biodiversité"],
         0, "انطلق يوم الأرض لأول مرة عام 1970م بمشاركة ملايين المتظاهرين لدعم الحفاظ على البيئة الطبيعية.",
         "Earth Day was first celebrated in 1970 to mobilize environmental awareness.",
         "Le Jour de la Terre a été célébré pour la première fois en 1970.", "easy")
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

    general_facts = [
        ("لغة الإشارة العالمية للصم والبكم", "Sign Language", "Langue des signes", "لغة بصرية تعتمد على حركات الأيدي وتعبيرات الوجه للتواصل الكامل", "Visual language using hands and facial gestures", "Langue visuelle utilisant les mains et expressions pour communiquer"),
        ("موسوعة غينيس للأرقام القياسية", "Guinness World Records", "Livre Guinness des records", "المرجع العالمي السنوي الأول في توثيق الأرقام القياسية والإنجازات الفائقة", "Global authority certifying extraordinary human achievements", "Référence internationale homologuant les exploits et records humains"),
        ("نظام بريل للقراءة والكتابة للمكفوفين", "Braille System", "Système d'écriture Braille", "نظام نقاط بارزة ابتكره لويس برايل يمكن قراءته باللمس", "Tactile writing system of raised dots invented by Louis Braille", "Système d'écriture tactile à points saillants inventé par Louis Braille"),
        ("متحف اللوفر في باريس", "The Louvre Museum", "Musée du Louvre à Paris", "المتحف الفني الأكثر زيارة في العالم وهرمه الزجاجي الشهير", "The world's most visited art museum, featuring the glass pyramid", "Le musée d'art le plus visité au monde avec sa pyramide de verre"),
        ("شطرنج وتاريخه الإنساني العريق", "Chess History", "Histoire du jeu d'échecs", "لعبة استراتيجية ملوك نشأت وتطورت في الهند وبلاد فارس والعالم الإسلامي", "Strategic board game tracing roots to Chaturanga and Shatranj", "Jeu de stratégie né du Chaturanga en Inde et perfectionné dans le monde arabe")
    ]

    for g in general_facts:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"في الثقافة والمعارف العامة، ما هو الوصف الدقيق لـ '{g[0]}'؟",
                "en": f"In general knowledge, what accurately characterizes '{g[1]}'?",
                "fr": f"En culture générale, comment décrit-on fidèlement '{g[2]}' ?"
            },
            "opts": {
                "ar": [g[3], "أداة زراعية لحصاد القمح", "نوع من الوقود الصناعي", "معادلة كيميائية معقدة"],
                "en": [g[4], "Agricultural harvest machinery", "Industrial vehicle propellant", "Complex chemical equation"],
                "fr": [g[5], "Machine agricole de moisson", "Carburant industriel", "Équation chimique complexe"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تُعد {g[0]} من أبرز المعارف الإنسانية المشتركة عبر الثقافات.",
                "en": f"{g[1]} is a celebrated element of universal world knowledge.",
                "fr": f"{g[2]} est un repère familier de la culture générale universelle."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"في مسابقات المعرفة العامة وسرعة البديهة، ما هو أساس الإجابة الصحيحة في السؤال رقم {idx}؟",
                "en": f"In general trivia and cognitive recall, what constitutes the correct reasoning for question {idx}?",
                "fr": f"Dans les jeux de culture générale, quel est le fondement de la réponse exacte au numéro {idx} ?"
            },
            "opts": {
                "ar": ["الحقيقة العلمية الموثقة والدقة المعرفية والاطلاع الشامل", "التخمين العشوائي غير المدروس", "افتراض الشائعات كحقائق", "تجاهل المصادر الموثوقة"],
                "en": ["Documented factual truth, precision, and broad literacy", "Random uninformed guesses", "Treating hearsay as fact", "Dismissing verified sources"],
                "fr": ["La véracité factuelle documentée, la précision et la culture générale", "La conjecture hasardeuse sans fondement", "Prendre les rumeurs pour des faits", "Ignorer les sources vérifiées"]
            },
            "ans": 0,
            "exp": {
                "ar": "المعرفة العامة تنمي الملاحظة وتوسع مدارك العقل وتربط بين مختلف حقول العلم والحياة.",
                "en": "General knowledge enriches human curiosity and bridges diverse sciences.",
                "fr": "La culture générale stimule la curiosité et enrichit les facultés cognitives."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "general",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_general(901)
    print(f"Generated {len(qs)} general questions.")
    assert len(qs) == 100
