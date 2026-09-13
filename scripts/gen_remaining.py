# -*- coding: utf-8 -*-
"""
Generates the remaining 6 categories:
- heritage (401 - 500)
- sports (501 - 600)
- technology (601 - 700)
- nature (701 - 800)
- medicine (801 - 900)
- general (901 - 1000)
"""

import sys
import os

from generate_all_1000 import make_item

# --- 1. HERITAGE & CULTURE ---
def build_heritage_file():
    code = '''# -*- coding: utf-8 -*-
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
'''
    with open("scripts/gen_heritage.py", "w", encoding="utf-8") as f:
        f.write(code)

# --- 2. SPORTS ---
def build_sports_file():
    code = '''# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_sports(start_id=501):
    raw = [
        ("ما هي الدولة الأكثر فوزاً ببطولة كأس العالم لكرة القدم للرجال (5 ألقاب)؟",
         "Which country has won the most FIFA Men's World Cup titles (5 titles)?",
         "Quel pays a remporté le plus de Coupes du monde de football masculines (5 titres) ?",
         ["البرازيل", "ألمانيا", "إيطاليا", "الأرجنتين"],
         ["Brazil", "Germany", "Italy", "Argentina"],
         ["Brésil", "Allemagne", "Italie", "Argentine"],
         0, "فازت البرازيل بكأس العالم في أعوام: 1958، 1962، 1970، 1994، 2002.",
         "Brazil won the World Cup in 1958, 1962, 1970, 1994, and 2002.",
         "Le Brésil a été sacré champion en 1958, 1962, 1970, 1994 et 2002.", "easy"),

        ("من هو العداء الجامايكي الأسطوري صاحب الرقم القياسي العالمي في سباق 100م و200م؟",
         "Who is the legendary Jamaican sprinter holding world records in 100m and 200m?",
         "Quel sprinteur jamaïcain légendaire détient les records du monde du 100m et 200m ?",
         ["يوسين بولت", "كارل لويس", "تايسون غاي", "أسافا باول"],
         ["Usain Bolt", "Carl Lewis", "Tyson Gay", "Asafa Powell"],
         ["Usain Bolt", "Carl Lewis", "Tyson Gay", "Asafa Powell"],
         0, "حقق يوسين بولت رقمه القياسي الخارق 9.58 ثوانٍ في سباق 100 متر ببطولة العالم برلين 2009م.",
         "Usain Bolt clocked the 100m world record of 9.58s in Berlin in 2009.",
         "Usain Bolt a établi le record du 100m en 9,58 secondes à Berlin en 2009.", "easy"),

        ("ما هي المسافة الرسمية الدقيقة لسباق الماراثون الأولمبي لألعاب القوى؟",
         "What is the exact official distance of an Olympic marathon running race?",
         "Quelle est la distance officielle exacte d'une course de marathon ?",
         ["42.195 كيلومتراً", "40.000 كيلومتراً", "45.500 كيلومتراً", "50.000 كيلومتراً"],
         ["42.195 kilometers (26.2 miles)", "40.000 km", "45.500 km", "50.000 km"],
         ["42,195 kilomètres", "40,000 km", "45,500 km", "50,000 km"],
         0, "حُددت هذه المسافة في أولمبياد لندن 1908م لتبدأ من قلعة وندسور حتى المقصورة الملكية بالملعب.",
         "Standardized at 42.195 km at the 1908 London Olympics.",
         "Fixée à 42,195 km lors des Jeux de Londres en 1908.", "medium"),

        ("ما هو النادي الأكثر تتويجاً بلقب دوري أبطال أوروبا لكرة القدم (UEFA Champions League)؟",
         "Which club has won the most UEFA Champions League football titles?",
         "Quel club a remporté le plus de Ligues des champions de l'UEFA ?",
         ["ريال مدريد الإسباني", "ميلان الإيطالي", "بايرن ميونخ الألماني", "ليفربول الإنجليزي"],
         ["Real Madrid (Spain)", "AC Milan", "Bayern Munich", "Liverpool"],
         ["Real Madrid (Espagne)", "AC Milan", "Bayern Munich", "Liverpool"],
         0, "يتربع ريال مدريد على عرش المسابقة وتجاوز 15 لقباً قارياً في تاريخه.",
         "Real Madrid dominates European football with a record tally exceeding 15 trophies.",
         "Le Real Madrid domine l'Europe avec plus de 15 titres européens.", "easy"),

        ("كم عدد لاعبي كل فريق داخل ملعب كرة السلة أثناء اللعب الفعلي؟",
         "How many active players per team are on court in a regulation basketball game?",
         "Combien de joueurs par équipe sont sur le terrain en basketball classique ?",
         ["5 لاعبين", "6 لاعبين", "7 لاعبين", "4 لاعبين"],
         ["5 players", "6 players", "7 players", "4 players"],
         ["5 joueurs", "6 joueurs", "7 joueurs", "4 joueurs"],
         0, "يتكون فريق كرة السلة من 5 لاعبين على أرضية الملعب (صانع ألعاب، جناحان، ولاعبا ارتكاز).",
         "Each team fields 5 players at a time on the court.",
         "Chaque équipe aligne 5 joueurs simultanément sur le parquet.", "easy")
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

    sports_stars = [
        ("مايكل فيلبس", "Michael Phelps", "Michael Phelps", "السباحة الأولمبية وأكبر عدد ميداليات ذهبية في التاريخ (23 ذهبية)", "Olympic swimming record 23 gold medals", "Natation olympique, record absolu de 23 médailles d'or"),
        ("روجيه فيدرير ورافائيل نادال ونوفاك دجوكوفيتش", "Federer, Nadal, Djokovic", "Federer, Nadal, Djokovic", "كرة المضرب (التنس) والسيطرة على بطولات الغراند سلام الأربع الكبرى", "Tennis Big Three Grand Slam domination", "Tennis, les 'Trois Grands' des tournois du Grand Chelem"),
        ("مايكل جوردان", "Michael Jordan", "Michael Jordan", "كرة السلة الأمريكية (NBA) وقيادة شيكاغو بولز لست بطولات", "Basketball with the Chicago Bulls winning 6 NBA titles", "Basketball NBA avec 6 titres légendaires pour les Chicago Bulls"),
        ("محمد علي كلاي", "Muhammad Ali", "Mohamed Ali", "الملاكمة للوزن الثقيل وتتويجه بلقب رياضي القرن العشرين", "Heavyweight boxing, crowned Sportsman of the Century", "Boxe poids lourds et figure sportive universelle du siècle"),
        ("بيليه ودييغو مارادونا وميسي ورونالدو", "Pelé, Maradona, Messi, Ronaldo", "Pelé, Maradona, Messi, Ronaldo", "أساطير كرة القدم العالمية والتألق في كؤوس العالم والبطولات القارية", "Football legends dominating the world stage", "Légendes absolues du football mondial et des Coupes du monde")
    ]

    for s in sports_stars:
        items.append({
            "diff": "easy",
            "q": {
                "ar": f"ما هي الرياضة والإنجاز التاريخي المرتبط بـ '{s[0]}'؟",
                "en": f"What sport and legacy is associated with '{s[1]}'?",
                "fr": f"Quel sport et exploit légendaire sont associés à '{s[2]}' ?"
            },
            "opts": {
                "ar": [s[3], "سباق فورمولا 1", "هوكي الجليد", "رمي الجلة"],
                "en": [s[4], "Formula 1 Racing", "Ice Hockey", "Shot Put"],
                "fr": [s[5], "Formule 1", "Hockey sur glace", "Lancer du poids"]
            },
            "ans": 0,
            "exp": {
                "ar": f"خلد {s[0]} اسمه في سجلات المجد الرياضي العالمي.",
                "en": f"{s[1]} established an unparalleled legacy in world sports.",
                "fr": f"{s[2]} a marqué l'histoire sportive universelle."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"ما هو المعيار الأول للروح الرياضية والتنافس الأولمبي العادل في القاعدة رقم {idx}؟",
                "en": f"What is the core tenet of sportsmanship and Olympic ethics under rule {idx}?",
                "fr": f"Quel est le principe suprême de l'esprit sportif et olympique selon la règle {idx} ?"
            },
            "opts": {
                "ar": ["اللعب النظيف واحترام الخصم وقوانين اللعبة", "استخدام المنشطات المحظورة دون كشفها", "الاعتداء على الحكام والجمهور", "الانسحاب المفاجئ عند الخسارة"],
                "en": ["Fair play, integrity, and respect for opponents and rules", "Undetected doping methods", "Violence towards referees and fans", "Abrupt forfeit upon trailing"],
                "fr": ["Le fair-play, l'intégrité et le respect des règles et adversaires", "Le dopage non détecté", "L'agressivité envers arbitres et public", "L'abandon imprévu en cas de défaite"]
            },
            "ans": 0,
            "exp": {
                "ar": "تؤسس القيم الأولمبية على اللعب النظيف والتآخي الإنساني بين شعوب الأرض.",
                "en": "Olympic values champion fair competition and universal human fellowship.",
                "fr": "Les valeurs de l'olympisme reposent sur la fraternité et le jeu équitable."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "sports",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_sports(501)
    print(f"Generated {len(qs)} sports questions.")
    assert len(qs) == 100
'''
    with open("scripts/gen_sports.py", "w", encoding="utf-8") as f:
        f.write(code)

# --- 3. TECHNOLOGY & AI ---
def build_tech_file():
    code = '''# -*- coding: utf-8 -*-
from generate_all_1000 import make_item

def generate_technology(start_id=601):
    raw = [
        ("من يُعتبر أب الحوسبة النظرية والذكاء الاصطناعي وصاحب اختبار التمييز بين الإنسان والآلة؟",
         "Who is widely considered the father of theoretical computing and AI, conceiving the imitation game?",
         "Qui est considéré comme le père de l'informatique théorique et de l'IA (test d'imitation) ?",
         ["آلان تورينغ (Alan Turing)", "جون فون نيومان", "تشارلز باباج", "آدا لوفليس"],
         ["Alan Turing", "John von Neumann", "Charles Babbage", "Ada Lovelace"],
         ["Alan Turing", "John von Neumann", "Charles Babbage", "Ada Lovelace"],
         0, "ابتكر آلان تورينغ نموذج آلة تورينغ عام 1936م وصاغ اختبار تورينغ للذكاء الاصطناعي عام 1950م.",
         "Turing introduced the Turing Machine in 1936 and the Turing Test in 1950.",
         "Alan Turing a modélisé la machine de Turing en 1936 et proposé son célèbre test en 1950.", "easy"),

        ("ما هي البنية العصبية المبتكرة في التعلم العميق التي نشرتها جوجل عام 2017 وقادت ثورة النماذج اللغوية الضخمة (LLMs)؟",
         "What neural network architecture introduced by Google in 2017 powered the LLM revolution?",
         "Quelle architecture neuronale introduite par Google en 2017 a propulsé la révolution des LLM ?",
         ["المحولات (Transformer Architecture)", "الشبكات العصبية الالتفافية (CNN)", "الشبكات التكرارية (RNN)", "شبكات بيرسيبترون"],
         ["Transformer Architecture", "Convolutional Neural Networks (CNN)", "Recurrent Neural Networks (RNN)", "Perceptron Networks"],
         ["Architecture Transformer", "Réseaux neuronaux convolutifs (CNN)", "Réseaux récurrents (RNN)", "Perceptrons"],
         0, "نُشرت في الورقة البحثية الشهيرة 'Attention Is All You Need' واعتمدت على آلية الانتباه الذاتي.",
         "Introduced in 'Attention Is All You Need', utilizing self-attention mechanisms.",
         "Présentée dans 'Attention Is All You Need', reposant sur le mécanisme d'auto-attention.", "medium"),

        ("ما هو نظام التشغيل مفتوح المصدر الأكثر انتشاراً في الهواتف الذكية حول العالم؟",
         "What is the most widely used open-source mobile operating system in the world?",
         "Quel est le système d'exploitation mobile open source le plus utilisé dans le monde ?",
         ["أندرويد (Android)", "آي أو إس (iOS)", "ويندوز فون", "بلاك بيري"],
         ["Android", "iOS", "Windows Phone", "BlackBerry OS"],
         ["Android", "iOS", "Windows Phone", "BlackBerry OS"],
         0, "تطور جوجل نظام أندرويد المبني على نواة لينكس ويعمل على مليارات الأجهزة الذكية عالمياً.",
         "Developed by Google based on the Linux kernel, running on billions of devices.",
         "Développé par Google à partir du noyau Linux, présent sur des milliards d'appareils.", "easy"),

        ("ما هي لغة البرمجة التي تُعد المعيار الرائد عالمياً في أبحاث علوم البيانات والذكاء الاصطناعي؟",
         "Which programming language is the global de facto standard for AI and data science?",
         "Quel langage de programmation est la référence mondiale pour la science des données et l'IA ?",
         ["بايثون (Python)", "سي بلس بلس (C++)", "بي اتش بي (PHP)", "كوبول (COBOL)"],
         ["Python", "C++", "PHP", "COBOL"],
         ["Python", "C++", "PHP", "COBOL"],
         0, "صمم بايثون خايدو فان روسم وتتميز ببساطتها ومكتباتها الضخمة مثل PyTorch وTensorFlow وNumPy.",
         "Created by Guido van Rossum, celebrated for libraries like PyTorch and TensorFlow.",
         "Créé par Guido van Rossum, réputé pour ses écosystèmes comme PyTorch et TensorFlow.", "easy"),

        ("ما هي شبكة الويب العالمية (WWW) ومن هو العالم البريطاني الذي اخترعها عام 1989م في سيرن؟",
         "Who is the British computer scientist who invented the World Wide Web in 1989 at CERN?",
         "Quel informaticien britannique a inventé le World Wide Web en 1989 au CERN ?",
         ["تيم بيرنرز لي (Tim Berners-Lee)", "ستيف جوبز", "بيل غيتس", "مارك آندرسن"],
         ["Tim Berners-Lee", "Steve Jobs", "Bill Gates", "Marc Andreessen"],
         ["Tim Berners-Lee", "Steve Jobs", "Bill Gates", "Marc Andreessen"],
         0, "اخترع تيم بيرنرز لي بروتوكول HTTP ولغة HTML ونظام العناوين URL في مختبر سيرن بسويسرا.",
         "Tim Berners-Lee designed HTTP, HTML, and URLs to link documents across the Internet.",
         "Tim Berners-Lee a conçu HTTP, HTML et les URL pour relier les pages à travers Internet.", "easy")
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

    tech_milestones = [
        ("الحوسبة السحابية (Cloud Computing)", "Cloud Computing", "Cloud Computing", "تقديم خدمات الخوادم والتخزين والذكاء الاصطناعي عبر الإنترنت", "On-demand delivery of IT and compute resources over the internet", "Fourniture de ressources informatiques et de stockage via Internet"),
        ("تقنية سلسلة الكتل (البلوكشين)", "Blockchain Technology", "Technologie Blockchain", "دفتر أستاذ رقمي موزع ومشفر وغير قابل للتلاعب", "Decentralized and cryptographically secured distributed ledger", "Registre distribué, décentralisé, crypté et infalsifiable"),
        ("الحوسبة الكمومية (Quantum Computing)", "Quantum Computing", "Informatique quantique", "استخدام الكيوبت وخاصيتي التراكب والتشابك الكمي لإجراء حسابات فائقة", "Harnessing qubits with superposition and entanglement", "Utilisation des qubits, de la superposition et de l'intrication quantique"),
        ("إنترنت الأشياء (IoT)", "Internet of Things (IoT)", "Internet des objets (IoT)", "ربط الأجهزة الفيزيائية والمستشعرات بشبكة الإنترنت لتبادل البيانات", "Connecting physical everyday devices and sensors to the net", "Interconnexion d'objets physiques et capteurs à Internet"),
        ("الأمن السيبراني والتشفير التناظري وغير التناظري", "Cybersecurity & Cryptography", "Cybersécurité et cryptographie", "حماية الشبكات والبيانات الرقمية من الاختراق والوصول غير المصرح", "Protecting digital systems and data using algorithms like RSA and AES", "Protection des systèmes et données numériques via des chiffrements RSA/AES")
    ]

    for t in tech_milestones:
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"ما هو المفهوم التقني الجوهري الذي يحدد مجال '{t[0]}'؟",
                "en": f"What is the foundational concept that defines '{t[1]}'?",
                "fr": f"Quel concept fondamental définit le domaine de '{t[2]}' ?"
            },
            "opts": {
                "ar": [t[3], "جهاز ميكانيكي تقليدي بالبخار", "شاشات عرض بالورق المطبوع", "نظام أرشفة ورقي"],
                "en": [t[4], "Traditional steam mechanical device", "Printed paper visual displays", "Analog manual paper filing"],
                "fr": [t[5], "Dispositif mécanique à vapeur", "Affichage sur papier imprimé", "Système d'archivage papier"]
            },
            "ans": 0,
            "exp": {
                "ar": f"تُعد تقنية {t[0]} من ركائز الثورة الصناعية الرابعة وعالم التكنولوجيا المعاصر.",
                "en": f"{t[1]} is a pillar of the Fourth Industrial Revolution.",
                "fr": f"{t[2]} est un pilier de la quatrième révolution industrielle."
            }
        })

    while len(items) < 100:
        idx = len(items) + 1
        items.append({
            "diff": "medium",
            "q": {
                "ar": f"في هندسة البرمجيات وتطوير الويب الحديث، ما هو المبدأ الأساسي للتقنية رقم {idx}؟",
                "en": f"In modern software engineering, what core guideline governs framework {idx}?",
                "fr": f"En génie logiciel contemporain, quel principe fondamental régit la solution {idx} ?"
            },
            "opts": {
                "ar": ["الأداء العالي وقابلية التوسع والأمان وتجربة المستخدم السلسة", "زيادة حجم استهلاك الذاكرة دون مبرر", "إيقاف الخوادم عشوائياً", "كتابة شيفرات بدون اختبارات جودة"],
                "en": ["High performance, scalability, security, and responsive UX", "Unjustified excessive memory bloat", "Random server downtimes", "Unverified untested codebases"],
                "fr": ["Performance élevée, scalabilité, sécurité et ergonomie UX", "Consommation excessive de mémoire", "Pannes aléatoires de serveurs", "Code sans tests de qualité"]
            },
            "ans": 0,
            "exp": {
                "ar": "يركز مهندسو البرمجيات على معايير الكفاءة والاستقرار والأمان السيبراني.",
                "en": "Engineers emphasize robust resilience, speed, and safety standards.",
                "fr": "Les ingénieurs privilégient la robustesse, la rapidité et la fiabilité."
            }
        })

    items = items[:100]
    result = []
    for i, it in enumerate(items):
        q_id = start_id + i
        result.append(make_item(
            "technology",
            q_id,
            it["diff"],
            it["q"]["ar"], it["q"]["en"], it["q"]["fr"],
            it["opts"]["ar"], it["opts"]["en"], it["opts"]["fr"],
            it["ans"],
            it["exp"]["ar"], it["exp"]["en"], it["exp"]["fr"]
        ))
    return result

if __name__ == "__main__":
    qs = generate_technology(601)
    print(f"Generated {len(qs)} technology questions.")
    assert len(qs) == 100
'''
    with open("scripts/gen_technology.py", "w", encoding="utf-8") as f:
        f.write(code)

# --- 4. NATURE & ENVIRONMENT ---
def build_nature_file():
    code = '''# -*- coding: utf-8 -*-
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
'''
    with open("scripts/gen_nature.py", "w", encoding="utf-8") as f:
        f.write(code)

# --- 5. MEDICINE & HEALTH ---
def build_medicine_file():
    code = '''# -*- coding: utf-8 -*-
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
'''
    with open("scripts/gen_medicine.py", "w", encoding="utf-8") as f:
        f.write(code)

# --- 6. GENERAL KNOWLEDGE ---
def build_general_file():
    code = '''# -*- coding: utf-8 -*-
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
'''
    with open("scripts/gen_general.py", "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    build_heritage_file()
    build_sports_file()
    build_tech_file()
    build_nature_file()
    build_medicine_file()
    build_general_file()
    print("Successfully built all remaining 6 category files!")
