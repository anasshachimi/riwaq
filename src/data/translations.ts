import { Language } from '../types';

export interface UIStrings {
  appName: string;
  appSubtitle: string;
  totalQuestionsCount: string;
  tenCategories: string;
  threeLanguages: string;
  startQuiz: string;
  quickChallenge: string;
  quickChallengeDesc: string;
  browseLibrary: string;
  browseLibraryDesc: string;
  marathonMode: string;
  marathonModeDesc: string;
  categoryDeepDive: string;
  playCategory: string;
  stats: string;
  settings: string;
  darkMode: string;
  lightMode: string;
  sound: string;
  soundOn: string;
  soundOff: string;
  language: string;
  question: string;
  of: string;
  score: string;
  streak: string;
  timeRemaining: string;
  nextQuestion: string;
  finishQuiz: string;
  explanation: string;
  correctAnswer: string;
  wrongAnswer: string;
  fiftyFifty: string;
  skipQuestion: string;
  hint: string;
  quizCompleted: string;
  greatJob: string;
  accuracy: string;
  correct: string;
  wrong: string;
  playAgain: string;
  backToHome: string;
  reviewMistakes: string;
  allCategories: string;
  searchQuestions: string;
  difficulty: string;
  easy: string;
  medium: string;
  hard: string;
  allDifficulties: string;
  questionsFound: string;
  bookmark: string;
  bookmarked: string;
  showAnswer: string;
  hideAnswer: string;
  noQuestionsFound: string;
  playerStats: string;
  totalAnswered: string;
  highestStreak: string;
  categoryMastery: string;
  resetStats: string;
  confirmReset: string;
  close: string;
  dailyChallenge: string;
  dailyChallengeDesc: string;
  doubleXpBadge: string;
  dailyStreakDays: string;
  dailyAvailable: string;
  dailyCompleted: string;
  nextChallengeIn: string;
  playDailyChallenge: string;
  dailyBadgeEarned: string;
  doubleXpAwarded: string;
  totalXp: string;
  dailyStreak: string;
  earnedBadges: string;
  todayChallenge: string;
  tenQuestionsAcrossCategories: string;
  shareResults: string;
  shareSubtitle: string;
  copyResult: string;
  copied: string;
  shareVia: string;
  shareOnSocial: string;
  shareScoreTitle: string;
}

export const TRANSLATIONS: Record<Language, UIStrings> = {
  ar: {
    appName: 'riwaq',
    appSubtitle: 'موسوعة المعرفة التفاعلية • 1000 سؤال في 10 أصناف',
    totalQuestionsCount: '1000 سؤال موثق',
    tenCategories: '10 أصناف معرفية',
    threeLanguages: '3 لغات عالمية',
    startQuiz: 'ابدأ الاختبار',
    quickChallenge: 'تحدي سريع',
    quickChallengeDesc: '10 أسئلة مختارة عشوائياً لاختبار معلوماتك العامة في دقائق',
    browseLibrary: 'مكتبة الأسئلة',
    browseLibraryDesc: 'تصفح جميع الأسئلة الألف وابحث فيها وراجع الإجابات والشروحات',
    marathonMode: 'ماراثون المعرفة',
    marathonModeDesc: 'تحدي الصمود اللانهائي: كم سؤالاً متواصلاً تستطيع إجابته بنجاح؟',
    categoryDeepDive: 'اختر صنفاً للتحدي',
    playCategory: 'اختبر نفسك',
    stats: 'إحصائياتي',
    settings: 'الإعدادات',
    darkMode: 'النمط الليلي',
    lightMode: 'النمط النهاري',
    sound: 'المؤثرات الصوتية',
    soundOn: 'مفعل',
    soundOff: 'مكتوم',
    language: 'اللغة',
    question: 'السؤال',
    of: 'من',
    score: 'النقاط',
    streak: 'سلسلة متتالية',
    timeRemaining: 'الوقت المتبقي',
    nextQuestion: 'السؤال التالي',
    finishQuiz: 'إنهاء الاختبار',
    explanation: 'الشرح المعرفي',
    correctAnswer: 'إجابة صحيحة!',
    wrongAnswer: 'إجابة غير صحيحة',
    fiftyFifty: 'حذف إجابتين (50:50)',
    skipQuestion: 'تخطي السؤال',
    hint: 'كشف التوضيح',
    quizCompleted: 'اكتمل التحدي بنجاح!',
    greatJob: 'أداء معرفي متميز',
    accuracy: 'نسبة الدقة',
    correct: 'صحيحة',
    wrong: 'خاطئة',
    playAgain: 'إعادة التحدي',
    backToHome: 'الرئيسية',
    reviewMistakes: 'مراجعة الأخطاء',
    allCategories: 'جميع الأصناف',
    searchQuestions: 'ابحث في الأسئلة أو الإجابات...',
    difficulty: 'المستوى',
    easy: 'سهل',
    medium: 'متوسط',
    hard: 'متقدم',
    allDifficulties: 'جميع المستويات',
    questionsFound: 'سؤال متوفر',
    bookmark: 'حفظ للمراجعة',
    bookmarked: 'محفوظ',
    showAnswer: 'عرض الإجابة',
    hideAnswer: 'إخفاء الإجابة',
    noQuestionsFound: 'لم يتم العثور على أسئلة تطابق بحثك',
    playerStats: 'سجل المعرفة والإحصائيات',
    totalAnswered: 'إجمالي الأسئلة المجابة',
    highestStreak: 'أطول سلسلة إجابات صحيحة',
    categoryMastery: 'إتقان الأصناف المعرفية',
    resetStats: 'إعادة ضبط الإحصائيات',
    confirmReset: 'هل أنت متأكد من مسح جميع إحصائياتك؟',
    close: 'إغلاق',
    dailyChallenge: 'التحدي اليومي',
    dailyChallengeDesc: '10 أسئلة فريدة موحدة يومياً تغطي كافة الأصناف مع مضاعفة نقاط الخبرة (2x XP) وأوسمة حصرية!',
    doubleXpBadge: 'مضاعفة الخبرة 2x XP',
    dailyStreakDays: 'أيام متتالية',
    dailyAvailable: 'جاهز لليوم',
    dailyCompleted: 'تم إنجاز تحدي اليوم',
    nextChallengeIn: 'التحدي القادم خلال',
    playDailyChallenge: 'خوض التحدي اليومي',
    dailyBadgeEarned: 'حصلت على وسام اليوم!',
    doubleXpAwarded: 'تمت مضاعفة نقاط الخبرة (2x XP)',
    totalXp: 'إجمالي نقاط الخبرة (XP)',
    dailyStreak: 'سلسلة التحديات اليومية',
    earnedBadges: 'الأوسمة والشهادات المكتسبة',
    todayChallenge: 'تحدي اليوم الموحد',
    tenQuestionsAcrossCategories: 'سؤال واحد من كل صنف من الأصناف العشرة',
    shareResults: 'مشاركة النتيجة',
    shareSubtitle: 'شارك إنجازك ونقاطك مع أصدقائك عبر وسائل التواصل الاجتماعي',
    copyResult: 'نسخ النتيجة',
    copied: 'تم النسخ بنجاح!',
    shareVia: 'مشاركة عبر',
    shareOnSocial: 'منصات التواصل',
    shareScoreTitle: 'نتيجتي في رِوَاق (riwaq)'
  },
  en: {
    appName: 'riwaq',
    appSubtitle: 'Interactive Knowledge Encyclopedia • 1,000 Questions across 10 Categories',
    totalQuestionsCount: '1,000 Verified Questions',
    tenCategories: '10 Knowledge Domains',
    threeLanguages: '3 World Languages',
    startQuiz: 'Start Quiz',
    quickChallenge: 'Quick Challenge',
    quickChallengeDesc: '10 randomized questions to test your general trivia in minutes',
    browseLibrary: 'Questions Library',
    browseLibraryDesc: 'Explore all 1,000 questions, search topics, and study explanations',
    marathonMode: 'Trivia Marathon',
    marathonModeDesc: 'Endurance challenge: how many questions can you answer in a row?',
    categoryDeepDive: 'Choose a Category',
    playCategory: 'Test Yourself',
    stats: 'My Stats',
    settings: 'Settings',
    darkMode: 'Dark Mode',
    lightMode: 'Light Mode',
    sound: 'Sound Effects',
    soundOn: 'Enabled',
    soundOff: 'Muted',
    language: 'Language',
    question: 'Question',
    of: 'of',
    score: 'Score',
    streak: 'Streak',
    timeRemaining: 'Time Left',
    nextQuestion: 'Next Question',
    finishQuiz: 'Finish Quiz',
    explanation: 'Insight & Context',
    correctAnswer: 'Correct Answer!',
    wrongAnswer: 'Incorrect Answer',
    fiftyFifty: '50:50 Lifeline',
    skipQuestion: 'Skip Question',
    hint: 'Show Hint',
    quizCompleted: 'Quiz Completed!',
    greatJob: 'Outstanding Knowledge Performance',
    accuracy: 'Accuracy',
    correct: 'Correct',
    wrong: 'Incorrect',
    playAgain: 'Play Again',
    backToHome: 'Home',
    reviewMistakes: 'Review Mistakes',
    allCategories: 'All Categories',
    searchQuestions: 'Search across questions and answers...',
    difficulty: 'Difficulty',
    easy: 'Easy',
    medium: 'Medium',
    hard: 'Hard',
    allDifficulties: 'All Difficulties',
    questionsFound: 'questions available',
    bookmark: 'Bookmark',
    bookmarked: 'Bookmarked',
    showAnswer: 'Reveal Answer',
    hideAnswer: 'Hide Answer',
    noQuestionsFound: 'No questions matched your search criteria',
    playerStats: 'Player Stats & History',
    totalAnswered: 'Total Questions Answered',
    highestStreak: 'Best Correct Streak',
    categoryMastery: 'Category Mastery',
    resetStats: 'Reset Statistics',
    confirmReset: 'Are you sure you want to reset all your stats?',
    close: 'Close',
    dailyChallenge: 'Daily Challenge',
    dailyChallengeDesc: '10 unique daily questions covering all 10 categories with Double XP (2x XP) and special badges!',
    doubleXpBadge: 'Double XP (2x)',
    dailyStreakDays: 'Days Streak',
    dailyAvailable: 'Available Today',
    dailyCompleted: 'Completed Today',
    nextChallengeIn: 'Next challenge in',
    playDailyChallenge: 'Play Daily Challenge',
    dailyBadgeEarned: 'Special Daily Badge Awarded!',
    doubleXpAwarded: 'Double XP (2x) Earned',
    totalXp: 'Total Experience (XP)',
    dailyStreak: 'Daily Challenge Streak',
    earnedBadges: 'Earned Badges & Honors',
    todayChallenge: "Today's Curated Challenge",
    tenQuestionsAcrossCategories: '1 question from each of the 10 domains',
    shareResults: 'Share Results',
    shareSubtitle: 'Share your score & achievements with friends on social media',
    copyResult: 'Copy Result',
    copied: 'Copied to clipboard!',
    shareVia: 'Share via',
    shareOnSocial: 'Social Media',
    shareScoreTitle: 'My Score on riwaq'
  },
  fr: {
    appName: 'riwaq',
    appSubtitle: 'Encyclopédie interactive du savoir • 1000 questions en 10 thèmes',
    totalQuestionsCount: '1000 questions certifiées',
    tenCategories: '10 thèmes du savoir',
    threeLanguages: '3 langues internationales',
    startQuiz: 'Démarrer le quiz',
    quickChallenge: 'Défi Rapide',
    quickChallengeDesc: '10 questions aléatoires pour évaluer votre culture générale en quelques minutes',
    browseLibrary: 'Bibliothèque de questions',
    browseLibraryDesc: 'Explorez l\'intégralité des 1000 questions, recherchez et apprenez des explications',
    marathonMode: 'Marathon du Savoir',
    marathonModeDesc: 'Test d\'endurance : combien de questions consécutives réussirez-vous ?',
    categoryDeepDive: 'Choisissez une catégorie',
    playCategory: 'Jouer la catégorie',
    stats: 'Mes statistiques',
    settings: 'Paramètres',
    darkMode: 'Mode sombre',
    lightMode: 'Mode clair',
    sound: 'Effets sonores',
    soundOn: 'Activé',
    soundOff: 'Muet',
    language: 'Langue',
    question: 'Question',
    of: 'sur',
    score: 'Score',
    streak: 'Série',
    timeRemaining: 'Temps restant',
    nextQuestion: 'Question suivante',
    finishQuiz: 'Terminer le quiz',
    explanation: 'Explication & Contexte',
    correctAnswer: 'Bonne réponse !',
    wrongAnswer: 'Mauvaise réponse',
    fiftyFifty: '50:50 (deux options)',
    skipQuestion: 'Passer la question',
    hint: 'Indice',
    quizCompleted: 'Quiz terminé avec succès !',
    greatJob: 'Performance intellectuelle remarquable',
    accuracy: 'Précision',
    correct: 'Correctes',
    wrong: 'Incorrectes',
    playAgain: 'Rejouer',
    backToHome: 'Accueil',
    reviewMistakes: 'Revoir les erreurs',
    allCategories: 'Toutes les catégories',
    searchQuestions: 'Rechercher parmi les questions et réponses...',
    difficulty: 'Difficulté',
    easy: 'Facile',
    medium: 'Moyen',
    hard: 'Difficile',
    allDifficulties: 'Toutes les difficultés',
    questionsFound: 'questions disponibles',
    bookmark: 'Mettre en favori',
    bookmarked: 'Enregistré',
    showAnswer: 'Afficher la réponse',
    hideAnswer: 'Masquer la réponse',
    noQuestionsFound: 'Aucune question ne correspond à vos critères',
    playerStats: 'Statistiques & Progression',
    totalAnswered: 'Questions répondues',
    highestStreak: 'Meilleure série consécutive',
    categoryMastery: 'Maîtrise par thème',
    resetStats: 'Réinitialiser les stats',
    confirmReset: 'Voulez-vous vraiment effacer vos statistiques ?',
    close: 'Fermer',
    dailyChallenge: 'Défi Quotidien',
    dailyChallengeDesc: '10 questions uniques par jour couvrant les 10 thèmes avec Double XP (2x XP) et badges exclusifs !',
    doubleXpBadge: 'Double XP (2x)',
    dailyStreakDays: 'jours consécutifs',
    dailyAvailable: 'Disponible aujourd\'hui',
    dailyCompleted: 'Défi du jour validé',
    nextChallengeIn: 'Prochain défi dans',
    playDailyChallenge: 'Lancer le défi du jour',
    dailyBadgeEarned: 'Insigne exclusif obtenu !',
    doubleXpAwarded: 'Double XP (2x) accordé',
    totalXp: 'Expérience totale (XP)',
    dailyStreak: 'Série de défis quotidiens',
    earnedBadges: 'Insignes et récompenses obtenus',
    todayChallenge: 'Défi exclusif du jour',
    tenQuestionsAcrossCategories: '1 question par thème pour chacun des 10 thèmes',
    shareResults: 'Partager le résultat',
    shareSubtitle: 'Partagez votre score et vos exploits avec vos amis sur les réseaux sociaux',
    copyResult: 'Copier le résultat',
    copied: 'Copié dans le presse-papier !',
    shareVia: 'Partager via',
    shareOnSocial: 'Réseaux sociaux',
    shareScoreTitle: 'Mon score sur riwaq'
  }
};

