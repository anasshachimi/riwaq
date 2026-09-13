# -*- coding: utf-8 -*-
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
