import { useState, useEffect, useMemo, useCallback } from 'react';
import {
  Sparkles,
  Zap,
  BookOpen,
  Trophy,
  Flame,
  Globe2,
  Calendar
} from 'lucide-react';
import questionsData from './data/questions.json';
import {
  Language,
  Question,
  QuizState,
  UserStats,
  Difficulty
} from './types';
import { CATEGORIES } from './data/categories';
import { TRANSLATIONS } from './data/translations';
import { soundFx } from './utils/audio';
import {
  getTodayDateString,
  getDailyQuestions,
  calculateDailyXp,
  generateDailyBadge
} from './utils/dailyChallenge';

import { Navbar } from './components/Navbar';
import { CategoryGrid } from './components/CategoryGrid';
import { QuizView } from './components/QuizView';
import { QuizResults } from './components/QuizResults';
import { QuestionLibrary } from './components/QuestionLibrary';
import { StatsModal } from './components/StatsModal';
import { DailyChallengeCard } from './components/DailyChallengeCard';

const ALL_QUESTIONS: Question[] = questionsData as unknown as Question[];

const STATS_STORAGE_KEY = 'riwaq_user_stats_v1';
const LANG_STORAGE_KEY = 'riwaq_language_v1';
const THEME_STORAGE_KEY = 'riwaq_theme_v1';
const SOUND_STORAGE_KEY = 'riwaq_sound_v1';

export default function App() {
  // --- Persisted Preferences ---
  const [currentLanguage, setCurrentLanguage] = useState<Language>(() => {
    const saved = localStorage.getItem(LANG_STORAGE_KEY);
    if (saved === 'en' || saved === 'fr' || saved === 'ar') return saved;
    return 'ar'; // Default Arabic
  });

  const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
    const saved = localStorage.getItem(THEME_STORAGE_KEY);
    if (saved !== null) return saved === 'dark';
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });

  const [soundEnabled, setSoundEnabled] = useState<boolean>(() => {
    const saved = localStorage.getItem(SOUND_STORAGE_KEY);
    return saved !== 'false';
  });

  // --- App View State ---
  const [activeView, setActiveView] = useState<'home' | 'quiz' | 'results' | 'library'>('home');
  const [isStatsOpen, setIsStatsOpen] = useState(false);

  // --- Persisted User Stats ---
  const [userStats, setUserStats] = useState<UserStats>(() => {
    try {
      const savedStr = localStorage.getItem(STATS_STORAGE_KEY);
      if (savedStr) {
        const parsed = JSON.parse(savedStr);
        return {
          totalAnswered: parsed.totalAnswered || 0,
          totalCorrect: parsed.totalCorrect || 0,
          totalQuizzesPlayed: parsed.totalQuizzesPlayed || 0,
          highestScore: parsed.highestScore || 0,
          categoryStats: parsed.categoryStats || {},
          bookmarks: parsed.bookmarks || [],
          mistakes: parsed.mistakes || [],
          totalXp: parsed.totalXp || 0,
          dailyStreak: parsed.dailyStreak || 0,
          lastDailyDate: parsed.lastDailyDate,
          completedDailyDates: parsed.completedDailyDates || [],
          badges: parsed.badges || []
        };
      }
    } catch {
      // Fallback
    }
    return {
      totalAnswered: 0,
      totalCorrect: 0,
      totalQuizzesPlayed: 0,
      highestScore: 0,
      categoryStats: {},
      bookmarks: [],
      mistakes: [],
      totalXp: 0,
      dailyStreak: 0,
      completedDailyDates: [],
      badges: []
    };
  });

  // Save stats to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STATS_STORAGE_KEY, JSON.stringify(userStats));
    } catch {
      // Ignore quota errors
    }
  }, [userStats]);

  // Sync Language and Direction with DOM
  useEffect(() => {
    document.documentElement.lang = currentLanguage;
    document.documentElement.dir = currentLanguage === 'ar' ? 'rtl' : 'ltr';
    localStorage.setItem(LANG_STORAGE_KEY, currentLanguage);
  }, [currentLanguage]);

  // Sync Dark Theme with DOM
  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
      localStorage.setItem(THEME_STORAGE_KEY, 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem(THEME_STORAGE_KEY, 'light');
    }
  }, [isDarkMode]);

  // Sync Sound
  useEffect(() => {
    soundFx.enabled = soundEnabled;
    localStorage.setItem(SOUND_STORAGE_KEY, String(soundEnabled));
  }, [soundEnabled]);

  // --- Quiz Session State ---
  const [quizState, setQuizState] = useState<QuizState>({
    questions: [],
    currentIndex: 0,
    selectedOption: null,
    isAnswered: false,
    score: 0,
    streak: 0,
    bestStreak: 0,
    lifelines: { fiftyFifty: true, skip: true, hint: true },
    eliminatedOptions: [],
    showExplanation: false,
    history: [],
    isComplete: false,
    startTime: Date.now(),
    timeRemaining: 0
  });

  // Helper to start a quiz with a custom question set
  const startQuizWithQuestions = (qs: Question[], isDaily = false) => {
    setQuizState({
      questions: qs,
      currentIndex: 0,
      selectedOption: null,
      isAnswered: false,
      score: 0,
      streak: 0,
      bestStreak: 0,
      lifelines: { fiftyFifty: true, skip: true, hint: true },
      eliminatedOptions: [],
      showExplanation: false,
      history: [],
      isComplete: false,
      startTime: Date.now(),
      timeRemaining: 0,
      isDailyChallenge: isDaily
    });
    setActiveView('quiz');
    soundFx.playClick();
  };

  // Start Daily Challenge (10 deterministic questions across categories with 2x XP & Badge)
  const handleStartDailyChallenge = () => {
    const todayStr = getTodayDateString();
    const dailyQuestions = getDailyQuestions(ALL_QUESTIONS, todayStr);
    startQuizWithQuestions(dailyQuestions, true);
  };

  // Quick Challenge (10 randomized questions)
  const handleStartQuickChallenge = () => {
    const shuffled = [...ALL_QUESTIONS].sort(() => 0.5 - Math.random());
    startQuizWithQuestions(shuffled.slice(0, 10));
  };

  // Marathon Mode (50 questions challenge)
  const handleStartMarathon = () => {
    const shuffled = [...ALL_QUESTIONS].sort(() => 0.5 - Math.random());
    startQuizWithQuestions(shuffled.slice(0, 50));
  };

  // Start Category Quiz
  const handleStartCategoryQuiz = (categoryId: string, count = 10) => {
    const catQuestions = ALL_QUESTIONS.filter(q => q.categoryId === categoryId);
    const shuffled = [...catQuestions].sort(() => 0.5 - Math.random());
    startQuizWithQuestions(shuffled.slice(0, count));
  };

  // Play a single specific question from Library
  const handlePlaySingleQuestion = (q: Question) => {
    startQuizWithQuestions([q]);
  };

  // Answering a question
  const handleAnswerQuestion = (selectedIdx: number) => {
    const currentQ = quizState.questions[quizState.currentIndex];
    if (!currentQ || quizState.isAnswered) return;

    const correctIdx = currentQ[currentLanguage].correctIndex;
    const isCorrect = selectedIdx === correctIdx;

    if (isCorrect) {
      soundFx.playCorrect();
    } else {
      soundFx.playWrong();
    }

    const newStreak = isCorrect ? quizState.streak + 1 : 0;
    const newBestStreak = Math.max(quizState.bestStreak, newStreak);
    
    // Double XP/Points if in Daily Challenge mode!
    const basePts = quizState.isDailyChallenge ? 200 : 100;
    const streakBonus = quizState.streak * (quizState.isDailyChallenge ? 20 : 10);
    const scoreAdd = isCorrect ? basePts + streakBonus : 0;

    const newHistory = [
      ...quizState.history,
      {
        questionId: currentQ.id,
        userAnswer: selectedIdx,
        isCorrect,
        timeSpent: 0
      }
    ];

    setQuizState(prev => ({
      ...prev,
      selectedOption: selectedIdx,
      isAnswered: true,
      score: prev.score + scoreAdd,
      streak: newStreak,
      bestStreak: newBestStreak,
      showExplanation: true,
      history: newHistory
    }));

    // Update global user stats
    setUserStats(prev => {
      const catId = currentQ.categoryId;
      const prevCat = prev.categoryStats[catId] || { answered: 0, correct: 0 };
      const mistakes = isCorrect
        ? prev.mistakes
        : Array.from(new Set([...prev.mistakes, currentQ.id]));

      return {
        ...prev,
        totalAnswered: prev.totalAnswered + 1,
        totalCorrect: prev.totalCorrect + (isCorrect ? 1 : 0),
        highestScore: Math.max(prev.highestScore, newBestStreak),
        mistakes,
        categoryStats: {
          ...prev.categoryStats,
          [catId]: {
            answered: prevCat.answered + 1,
            correct: prevCat.correct + (isCorrect ? 1 : 0)
          }
        }
      };
    });
  };

  // Move to next question or complete quiz
  const handleNextQuestion = () => {
    soundFx.playClick();
    if (quizState.currentIndex + 1 >= quizState.questions.length) {
      // Finished!
      const correctCount = quizState.history.filter(h => h.isCorrect).length;

      if (quizState.isDailyChallenge) {
        const todayStr = getTodayDateString();
        const xpData = calculateDailyXp(correctCount, quizState.bestStreak);

        // Calculate consecutive daily streak
        let updatedStreak = userStats.dailyStreak;
        const alreadyDoneToday = userStats.completedDailyDates.includes(todayStr);

        if (!alreadyDoneToday) {
          if (userStats.lastDailyDate) {
            const yesterday = new Date();
            yesterday.setDate(yesterday.getDate() - 1);
            const yesterdayStr = getTodayDateString(yesterday);
            if (userStats.lastDailyDate === yesterdayStr) {
              updatedStreak += 1;
            } else if (userStats.lastDailyDate !== todayStr) {
              updatedStreak = 1;
            }
          } else {
            updatedStreak = 1;
          }
        }

        const badge = generateDailyBadge(todayStr, correctCount, updatedStreak);

        setQuizState(prev => ({
          ...prev,
          isComplete: true,
          earnedXp: xpData.totalXp,
          awardedBadge: badge
        }));

        setUserStats(prev => {
          const completedDates = prev.completedDailyDates.includes(todayStr)
            ? prev.completedDailyDates
            : [...prev.completedDailyDates, todayStr];
          
          const filteredBadges = prev.badges.filter(b => b.id !== badge.id);

          return {
            ...prev,
            totalQuizzesPlayed: prev.totalQuizzesPlayed + 1,
            totalXp: prev.totalXp + (alreadyDoneToday ? 0 : xpData.totalXp),
            dailyStreak: updatedStreak,
            lastDailyDate: todayStr,
            completedDailyDates: completedDates,
            badges: [badge, ...filteredBadges]
          };
        });
      } else {
        // Standard quiz completion
        setQuizState(prev => ({ ...prev, isComplete: true }));
        setUserStats(prev => ({
          ...prev,
          totalQuizzesPlayed: prev.totalQuizzesPlayed + 1,
          totalXp: prev.totalXp + quizState.score
        }));
      }

      setActiveView('results');
    } else {
      setQuizState(prev => ({
        ...prev,
        currentIndex: prev.currentIndex + 1,
        selectedOption: null,
        isAnswered: false,
        eliminatedOptions: [],
        showExplanation: false
      }));
    }
  };

  // Lifeline: 50:50
  const handleUse5050 = () => {
    const currentQ = quizState.questions[quizState.currentIndex];
    if (!currentQ || !quizState.lifelines.fiftyFifty || quizState.isAnswered) return;

    soundFx.playLifeline();
    const correctIdx = currentQ[currentLanguage].correctIndex;
    const wrongIndices = [0, 1, 2, 3].filter(i => i !== correctIdx);
    // Pick 2 random wrong options to eliminate
    const shuffledWrong = wrongIndices.sort(() => 0.5 - Math.random());
    const toEliminate = shuffledWrong.slice(0, 2);

    setQuizState(prev => ({
      ...prev,
      lifelines: { ...prev.lifelines, fiftyFifty: false },
      eliminatedOptions: toEliminate
    }));
  };

  // Lifeline: Skip
  const handleSkipQuestion = () => {
    if (!quizState.lifelines.skip || quizState.isAnswered) return;
    soundFx.playLifeline();
    setQuizState(prev => ({
      ...prev,
      lifelines: { ...prev.lifelines, skip: false }
    }));
    handleNextQuestion();
  };

  // Toggle Bookmark
  const handleToggleBookmark = useCallback((qId: number) => {
    soundFx.playClick();
    setUserStats(prev => {
      const exists = prev.bookmarks.includes(qId);
      const bookmarks = exists
        ? prev.bookmarks.filter(id => id !== qId)
        : [...prev.bookmarks, qId];
      return { ...prev, bookmarks };
    });
  }, []);

  // Reset Stats
  const handleResetStats = () => {
    setUserStats({
      totalAnswered: 0,
      totalCorrect: 0,
      totalQuizzesPlayed: 0,
      highestScore: 0,
      categoryStats: {},
      bookmarks: [],
      mistakes: []
    });
    localStorage.removeItem(STATS_STORAGE_KEY);
    soundFx.playClick();
  };

  const t = TRANSLATIONS[currentLanguage];

  // Quick stats summary
  const accuracyPercent = userStats.totalAnswered > 0
    ? Math.round((userStats.totalCorrect / userStats.totalAnswered) * 100)
    : 0;

  return (
    <div className="min-h-screen bg-stone-50 dark:bg-stone-950 text-stone-900 dark:text-stone-100 transition-colors duration-200 flex flex-col font-sans selection:bg-amber-500/20 selection:text-amber-700 dark:selection:text-amber-300">
      
      {/* Top Navigation Bar */}
      <Navbar
        currentLanguage={currentLanguage}
        onLanguageChange={setCurrentLanguage}
        isDarkMode={isDarkMode}
        onToggleDarkMode={() => setIsDarkMode(!isDarkMode)}
        soundEnabled={soundEnabled}
        onToggleSound={() => setSoundEnabled(!soundEnabled)}
        onOpenStats={() => setIsStatsOpen(true)}
        onGoHome={() => setActiveView('home')}
        onOpenLibrary={() => setActiveView('library')}
        activeView={activeView}
        userStats={userStats}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
        
        {/* --- VIEW 1: HOME DASHBOARD --- */}
        {activeView === 'home' && (
          <div className="space-y-8 sm:space-y-10 animate-fade-in">
            
            {/* Hero Banner with riwaq branding & 1,000 Questions Highlight */}
            <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-amber-600 via-amber-700 to-stone-900 text-white p-6 sm:p-10 shadow-lg border border-amber-500/20">
              <div className="relative z-10 max-w-3xl space-y-4">
                
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-amber-200 text-xs font-semibold border border-white/15">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>{t.appSubtitle}</span>
                </div>

                <h1 className="text-3xl sm:text-5xl font-black tracking-tight font-serif leading-tight">
                  riwaq <span className="font-sans font-bold text-amber-300 text-2xl sm:text-4xl">رِوَاق</span>
                </h1>

                <p className="text-sm sm:text-base text-amber-100/90 leading-relaxed max-w-2xl font-normal">
                  {currentLanguage === 'ar'
                    ? 'تجربة معرفية رائدة تضم ألف سؤال موثق في عشرة مجالات، بثلاث لغات، مع شروحات علمية مفصلة وإحصائيات دقيقة لتعزيز ثقافتك العامة.'
                    : currentLanguage === 'fr'
                    ? 'Une expérience intellectuelle complète avec 1000 questions vérifiées réparties en dix domaines, disponibles en trois langues avec explications détaillées.'
                    : 'A comprehensive trivia encyclopedia featuring 1,000 verified questions across 10 diverse domains in 3 languages, backed by informative explanations.'}
                </p>

                {/* Hero Stats Badge Row */}
                <div className="flex flex-wrap items-center gap-3 pt-2 text-xs font-semibold">
                  <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-black/20 backdrop-blur-sm border border-white/10">
                    <Trophy className="w-4 h-4 text-amber-300" />
                    <span>{t.totalQuestionsCount}</span>
                  </div>
                  <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-black/20 backdrop-blur-sm border border-white/10">
                    <Globe2 className="w-4 h-4 text-amber-300" />
                    <span>{t.tenCategories}</span>
                  </div>
                  <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-black/20 backdrop-blur-sm border border-white/10">
                    <Sparkles className="w-4 h-4 text-amber-300" />
                    <span>{t.threeLanguages}</span>
                  </div>
                </div>

                {/* Main Action Buttons */}
                <div className="flex flex-wrap items-center gap-3 pt-4">
                  <button
                    onClick={handleStartDailyChallenge}
                    className="py-3 px-6 rounded-2xl bg-gradient-to-r from-amber-400 to-amber-300 text-stone-950 font-black text-sm shadow-md hover:bg-amber-300 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center gap-2"
                  >
                    <Calendar className="w-4 h-4 text-stone-950" />
                    <span>{t.dailyChallenge} (2x XP)</span>
                  </button>

                  <button
                    onClick={handleStartQuickChallenge}
                    className="py-3 px-6 rounded-2xl bg-white text-stone-900 font-bold text-sm shadow-md hover:bg-amber-50 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center gap-2"
                  >
                    <Zap className="w-4 h-4 text-amber-600 fill-amber-600" />
                    <span>{t.quickChallenge} (10 Qs)</span>
                  </button>

                  <button
                    onClick={handleStartMarathon}
                    className="py-3 px-6 rounded-2xl bg-amber-500/20 backdrop-blur-md text-white border border-white/20 font-bold text-sm hover:bg-amber-500/30 transition-all flex items-center gap-2"
                  >
                    <Flame className="w-4 h-4 text-amber-300" />
                    <span>{t.marathonMode}</span>
                  </button>

                  <button
                    onClick={() => setActiveView('library')}
                    className="py-3 px-5 rounded-2xl bg-black/20 backdrop-blur-md text-amber-100 hover:text-white hover:bg-black/30 transition-all text-sm font-semibold flex items-center gap-2"
                  >
                    <BookOpen className="w-4 h-4" />
                    <span>{t.browseLibrary}</span>
                  </button>
                </div>

              </div>

              {/* Background Geometric Accent */}
              <div className="absolute -bottom-16 -end-16 w-80 h-80 rounded-full bg-amber-500/20 blur-3xl pointer-events-none" />
            </div>

            {/* Daily Challenge Card Component */}
            <DailyChallengeCard
              currentLanguage={currentLanguage}
              userStats={userStats}
              onStartDailyChallenge={handleStartDailyChallenge}
            />

            {/* Quick Player Progress Ribbon if questions were played */}
            {userStats.totalAnswered > 0 && (
              <div className="p-4 rounded-2xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 flex items-center justify-between gap-4 flex-wrap">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center font-bold">
                    <Trophy className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="text-xs text-stone-500 font-semibold">{t.playerStats}</div>
                    <div className="text-sm font-bold text-stone-900 dark:text-stone-100">
                      {userStats.totalAnswered} / 1000 {t.question} • {accuracyPercent}% {t.accuracy}
                    </div>
                  </div>
                </div>

                <div className="flex items-center gap-4 flex-wrap">
                  {userStats.totalXp > 0 && (
                    <div className="text-xs font-bold text-amber-600 dark:text-amber-400 flex items-center gap-1 bg-amber-500/10 px-2.5 py-1 rounded-lg">
                      <Zap className="w-3.5 h-3.5 fill-current" />
                      <span>{userStats.totalXp.toLocaleString()} XP</span>
                    </div>
                  )}

                  {userStats.dailyStreak > 0 && (
                    <div className="text-xs font-bold text-orange-600 dark:text-orange-400 flex items-center gap-1 bg-orange-500/10 px-2.5 py-1 rounded-lg">
                      <Flame className="w-3.5 h-3.5 fill-current" />
                      <span>{userStats.dailyStreak} {t.dailyStreakDays}</span>
                    </div>
                  )}

                  <button
                    onClick={() => setIsStatsOpen(true)}
                    className="text-xs font-bold text-amber-600 dark:text-amber-400 hover:underline px-2 py-1"
                  >
                    {t.stats} &rarr;
                  </button>
                </div>
              </div>
            )}

            {/* All 10 Categories Grid */}
            <CategoryGrid
              currentLanguage={currentLanguage}
              userStats={userStats}
              onSelectCategory={handleStartCategoryQuiz}
            />

          </div>
        )}

        {/* --- VIEW 2: ACTIVE QUIZ VIEW --- */}
        {activeView === 'quiz' && (
          <QuizView
            currentLanguage={currentLanguage}
            quizState={quizState}
            onAnswer={handleAnswerQuestion}
            onNextQuestion={handleNextQuestion}
            onUse5050={handleUse5050}
            onSkipQuestion={handleSkipQuestion}
            onToggleBookmark={handleToggleBookmark}
            isBookmarked={userStats.bookmarks.includes(quizState.questions[quizState.currentIndex]?.id || 0)}
            onQuitQuiz={() => setActiveView('home')}
          />
        )}

        {/* --- VIEW 3: QUIZ RESULTS VIEW --- */}
        {activeView === 'results' && (
          <QuizResults
            currentLanguage={currentLanguage}
            quizState={quizState}
            onPlayAgain={() => startQuizWithQuestions(quizState.questions)}
            onGoHome={() => setActiveView('home')}
          />
        )}

        {/* --- VIEW 4: QUESTIONS LIBRARY (1,000 QUESTIONS EXPLORER) --- */}
        {activeView === 'library' && (
          <QuestionLibrary
            questions={ALL_QUESTIONS}
            currentLanguage={currentLanguage}
            bookmarks={userStats.bookmarks}
            onToggleBookmark={handleToggleBookmark}
            onPlaySingleQuestion={handlePlaySingleQuestion}
          />
        )}

      </main>

      {/* Stats Modal */}
      <StatsModal
        isOpen={isStatsOpen}
        onClose={() => setIsStatsOpen(false)}
        userStats={userStats}
        currentLanguage={currentLanguage}
        onResetStats={handleResetStats}
      />

      {/* Minimal Footer */}
      <footer className="border-t border-stone-200/80 dark:border-stone-800/80 py-6 text-center text-xs text-stone-500 dark:text-stone-400">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div className="font-bold text-stone-700 dark:text-stone-300 flex items-center gap-1.5 font-serif text-sm">
            <span>riwaq</span>
            <span className="text-[10px] font-sans px-2 py-0.5 rounded bg-amber-500/10 text-amber-700 dark:text-amber-400 font-bold">1000 Qs</span>
          </div>
          <div>
            العربية • English • Français — 10 Categories • Light & Dark Mode
          </div>
        </div>
      </footer>

    </div>
  );
}
