import React, { useState } from 'react';
import {
  Trophy,
  RotateCcw,
  Home,
  CheckCircle2,
  XCircle,
  Flame,
  BookOpen,
  ChevronDown,
  ChevronUp,
  Target,
  Zap,
  Crown,
  Sparkles,
  Award,
  Share2
} from 'lucide-react';
import { Language, QuizState } from '../types';
import { TRANSLATIONS } from '../data/translations';
import { ShareResults } from './ShareResults';

interface QuizResultsProps {
  currentLanguage: Language;
  quizState: QuizState;
  onPlayAgain: () => void;
  onGoHome: () => void;
}

export const QuizResults: React.FC<QuizResultsProps> = ({
  currentLanguage,
  quizState,
  onPlayAgain,
  onGoHome
}) => {
  const t = TRANSLATIONS[currentLanguage];
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);

  const total = quizState.history.length;
  const correctCount = quizState.history.filter(h => h.isCorrect).length;
  const wrongCount = total - correctCount;
  const accuracy = total > 0 ? Math.round((correctCount / total) * 100) : 0;

  const toggleExpand = (idx: number) => {
    setExpandedIndex(expandedIndex === idx ? null : idx);
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6 animate-fade-in pb-12">
      
      {/* Celebration Header Card */}
      <div className="bg-white dark:bg-stone-900 rounded-3xl p-6 sm:p-8 border border-stone-200 dark:border-stone-800 shadow-md text-center relative overflow-hidden">
        
        {/* Daily Challenge Celebration Banner */}
        {quizState.isDailyChallenge && (
          <div className="mb-6 p-4 rounded-2xl bg-gradient-to-r from-amber-500/20 via-amber-500/10 to-amber-500/20 border-2 border-amber-500/50 shadow-sm text-center space-y-2">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500 text-white text-xs font-black uppercase tracking-wider">
              <Zap className="w-3.5 h-3.5 fill-current" />
              <span>{t.doubleXpAwarded}</span>
            </div>
            <div className="text-2xl font-black text-amber-600 dark:text-amber-400">
              +{quizState.earnedXp || 0} XP
            </div>
          </div>
        )}

        {/* Special Daily Badge Award Display */}
        {quizState.isDailyChallenge && quizState.awardedBadge && (
          <div className="mb-6 p-4 rounded-2xl bg-gradient-to-br from-amber-50 via-white to-amber-50 dark:from-stone-800 dark:via-stone-900 dark:to-stone-800 border-2 border-amber-400 dark:border-amber-600 shadow-lg text-start flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-amber-400 to-amber-600 text-white flex items-center justify-center font-bold shrink-0 shadow-md shadow-amber-500/20">
              <Crown className="w-8 h-8 animate-bounce" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-600 dark:text-amber-400">
                  {t.dailyBadgeEarned}
                </span>
                <span className="text-xs px-2 py-0.5 rounded bg-amber-500/20 font-black text-amber-700 dark:text-amber-300">
                  +{quizState.awardedBadge.xpAwarded} Bonus XP
                </span>
              </div>
              <h4 className="text-base font-black text-stone-900 dark:text-stone-100 truncate">
                {quizState.awardedBadge.title[currentLanguage]}
              </h4>
              <p className="text-xs text-stone-600 dark:text-stone-400 line-clamp-1">
                {quizState.awardedBadge.description[currentLanguage]}
              </p>
            </div>
          </div>
        )}

        <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl bg-amber-500/10 text-amber-600 dark:text-amber-400 mx-auto flex items-center justify-center mb-4 border border-amber-500/20 shadow-inner">
          <Trophy className="w-8 h-8 sm:w-10 sm:h-10 animate-bounce" />
        </div>

        <h1 className="text-2xl sm:text-3xl font-black text-stone-900 dark:text-stone-100 tracking-tight">
          {t.quizCompleted}
        </h1>
        <p className="text-sm text-stone-600 dark:text-stone-400 mt-1 font-medium">
          {t.greatJob}
        </p>

        {/* Big Accuracy Ring / Stat */}
        <div className="mt-6 flex items-center justify-center">
          <div className="relative flex items-center justify-center">
            <div className="text-4xl sm:text-5xl font-black text-amber-600 dark:text-amber-400 font-sans">
              {accuracy}%
            </div>
          </div>
        </div>

        {/* 3 Metric Cards */}
        <div className="grid grid-cols-3 gap-3 mt-6 pt-6 border-t border-stone-100 dark:border-stone-800">
          <div className="p-3 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/60">
            <div className="flex items-center justify-center gap-1 text-emerald-600 dark:text-emerald-400 text-xs font-bold mb-1">
              <CheckCircle2 className="w-3.5 h-3.5" />
              <span>{t.correct}</span>
            </div>
            <div className="text-xl font-extrabold text-emerald-800 dark:text-emerald-200">
              {correctCount}
            </div>
          </div>

          <div className="p-3 rounded-2xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/60">
            <div className="flex items-center justify-center gap-1 text-rose-600 dark:text-rose-400 text-xs font-bold mb-1">
              <XCircle className="w-3.5 h-3.5" />
              <span>{t.wrong}</span>
            </div>
            <div className="text-xl font-extrabold text-rose-800 dark:text-rose-200">
              {wrongCount}
            </div>
          </div>

          <div className="p-3 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/60">
            <div className="flex items-center justify-center gap-1 text-amber-600 dark:text-amber-400 text-xs font-bold mb-1">
              <Flame className="w-3.5 h-3.5" />
              <span>{t.streak}</span>
            </div>
            <div className="text-xl font-extrabold text-amber-800 dark:text-amber-200">
              {quizState.bestStreak}
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-3 mt-6">
          {!quizState.isDailyChallenge && (
            <button
              onClick={onPlayAgain}
              className="flex-1 py-3 px-5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-sm shadow-md shadow-amber-600/20 flex items-center justify-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <RotateCcw className="w-4 h-4" />
              <span>{t.playAgain}</span>
            </button>
          )}
          <button
            onClick={() => {
              const el = document.getElementById('share-section');
              if (el) {
                el.scrollIntoView({ behavior: 'smooth' });
              }
              // If native share is supported, try directly
              if (typeof navigator !== 'undefined' && navigator.share) {
                const total = quizState.history.length;
                const correctCount = quizState.history.filter(h => h.isCorrect).length;
                const accuracy = total > 0 ? Math.round((correctCount / total) * 100) : 0;
                const shareTitle = currentLanguage === 'ar' ? 'نتيجتي في رِوَاق (riwaq)' : currentLanguage === 'fr' ? 'Mon score sur riwaq' : 'My Score on riwaq';
                const modeLabel = quizState.isDailyChallenge
                  ? (currentLanguage === 'ar' ? '🌟 التحدي اليومي الموحد' : currentLanguage === 'fr' ? '🌟 Défi Quotidien' : '🌟 Daily Challenge')
                  : (currentLanguage === 'ar' ? '🎯 تحدي المعرفة' : currentLanguage === 'fr' ? '🎯 Quiz du Savoir' : '🎯 Knowledge Quiz');
                const emojiGrid = quizState.history.map(h => (h.isCorrect ? '🟩' : '🟥')).join('');
                const badgeTitle = quizState.awardedBadge ? quizState.awardedBadge.title[currentLanguage] : null;

                const text = [
                  '🏛️ riwaq | رِوَاق',
                  modeLabel,
                  `🎯 Score: ${quizState.score} pts (${accuracy}% - ${correctCount}/${total})`,
                  `🔥 Streak: ${quizState.bestStreak}`,
                  quizState.earnedXp ? `⚡ +${quizState.earnedXp} XP` : '',
                  badgeTitle ? `🏅 ${badgeTitle}` : '',
                  emojiGrid
                ].filter(Boolean).join('\n');

                navigator.share({
                  title: shareTitle,
                  text,
                  url: window.location.href
                }).catch(() => {});
              }
            }}
            className="flex-1 py-3 px-5 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-white font-bold text-sm shadow-md shadow-amber-500/20 transition-all flex items-center justify-center gap-2 hover:scale-[1.02] active:scale-[0.98]"
          >
            <Share2 className="w-4 h-4" />
            <span>{t.shareResults}</span>
          </button>
          <button
            onClick={onGoHome}
            className="flex-1 py-3 px-5 rounded-xl bg-stone-100 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 font-bold text-sm transition-all flex items-center justify-center gap-2"
          >
            <Home className="w-4 h-4" />
            <span>{t.backToHome}</span>
          </button>
        </div>
      </div>

      {/* Review Section */}
      <div className="bg-white dark:bg-stone-900 rounded-3xl p-6 border border-stone-200 dark:border-stone-800 shadow-sm space-y-4">
        <div className="flex items-center justify-between border-b border-stone-100 dark:border-stone-800 pb-3">
          <h2 className="font-extrabold text-base text-stone-900 dark:text-stone-100 flex items-center gap-2">
            <Target className="w-4 h-4 text-amber-600 dark:text-amber-400" />
            <span>{t.reviewMistakes} & {t.explanation}</span>
          </h2>
          <span className="text-xs text-stone-500">
            {correctCount}/{total} {t.correct}
          </span>
        </div>

        <div className="space-y-2.5">
          {quizState.history.map((record, idx) => {
            const q = quizState.questions.find(item => item.id === record.questionId);
            if (!q) return null;
            const localized = q[currentLanguage];
            const isExpanded = expandedIndex === idx;

            return (
              <div
                key={idx}
                className="border border-stone-200 dark:border-stone-800 rounded-2xl overflow-hidden transition-all"
              >
                <button
                  onClick={() => toggleExpand(idx)}
                  className="w-full p-3.5 text-start flex items-center justify-between gap-3 hover:bg-stone-50 dark:hover:bg-stone-800/50 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    {record.isCorrect ? (
                      <CheckCircle2 className="w-5 h-5 text-emerald-500 shrink-0" />
                    ) : (
                      <XCircle className="w-5 h-5 text-rose-500 shrink-0" />
                    )}
                    <span className="text-xs sm:text-sm font-semibold text-stone-800 dark:text-stone-200 line-clamp-1">
                      {localized.question}
                    </span>
                  </div>
                  {isExpanded ? (
                    <ChevronUp className="w-4 h-4 text-stone-400 shrink-0" />
                  ) : (
                    <ChevronDown className="w-4 h-4 text-stone-400 shrink-0" />
                  )}
                </button>

                {isExpanded && (
                  <div className="p-4 bg-stone-50 dark:bg-stone-800/40 border-t border-stone-100 dark:border-stone-800 space-y-3 text-xs sm:text-sm">
                    <div className="font-bold text-stone-900 dark:text-stone-100">
                      {localized.question}
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                      <div className="p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200">
                        <span className="font-bold block text-[11px] text-emerald-700 dark:text-emerald-400 mb-0.5">
                          {t.correctAnswer}:
                        </span>
                        {localized.options[localized.correctIndex]}
                      </div>

                      {!record.isCorrect && record.userAnswer !== -1 && (
                        <div className="p-2.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200">
                          <span className="font-bold block text-[11px] text-rose-700 dark:text-rose-400 mb-0.5">
                            {t.wrongAnswer}:
                          </span>
                          {localized.options[record.userAnswer]}
                        </div>
                      )}
                    </div>

                    <div className="p-3 rounded-xl bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 text-stone-700 dark:text-stone-300 text-xs leading-relaxed flex items-start gap-2">
                      <BookOpen className="w-3.5 h-3.5 text-amber-500 shrink-0 mt-0.5" />
                      <div>
                        <span className="font-bold text-stone-900 dark:text-stone-100">{t.explanation}: </span>
                        {localized.explanation}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Share Section at the end of QuizResults view */}
      <div id="share-section">
        <ShareResults
          quizState={quizState}
          currentLanguage={currentLanguage}
        />
      </div>

    </div>
  );
};
