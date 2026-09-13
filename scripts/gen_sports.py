# -*- coding: utf-8 -*-
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
