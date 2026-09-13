import React, { useState, useEffect } from 'react';
import {
  Flame,
  CheckCircle2,
  XCircle,
  Bookmark,
  BookmarkCheck,
  Sparkles,
  ArrowRight,
  ArrowLeft,
  HelpCircle,
  Clock,
  BookOpen
} from 'lucide-react';
import { Language, Question, QuizState } from '../types';
import { TRANSLATIONS } from '../data/translations';
import { CATEGORY_MAP } from '../data/categories';
import { soundFx } from '../utils/audio';

interface QuizViewProps {
  currentLanguage: Language;
  quizState: QuizState;
  onAnswer: (selectedIdx: number) => void;
  onNextQuestion: () => void;
  onUse5050: () => void;
  onSkipQuestion: () => void;
  onToggleBookmark: (questionId: number) => void;
  isBookmarked: boolean;
  onQuitQuiz: () => void;
}

export const QuizView: React.FC<QuizViewProps> = ({
  currentLanguage,
  quizState,
  onAnswer,
  onNextQuestion,
  onUse5050,
  onSkipQuestion,
  onToggleBookmark,
  isBookmarked,
  onQuitQuiz
}) => {
  const t = TRANSLATIONS[currentLanguage];
  const isRtl = currentLanguage === 'ar';
  const currentQ: Question | undefined = quizState.questions[quizState.currentIndex];

  const [revealedHint, setRevealedHint] = useState(false);

  useEffect(() => {
    setRevealedHint(false);
  }, [quizState.currentIndex]);

  if (!currentQ) {
    return null;
  }

  const localizedQ = currentQ[currentLanguage];
  const category = CATEGORY_MAP.get(currentQ.categoryId);
  const totalQuestions = quizState.questions.length;
  const progressPercent = Math.round(((quizState.currentIndex) / totalQuestions) * 100);

  const optionLetters = isRtl
    ? ['أ', 'ب', 'ج', 'د']
    : ['A', 'B', 'C', 'D'];

  const handleSelectOption = (idx: number) => {
    if (quizState.isAnswered) return;
    if (quizState.eliminatedOptions.includes(idx)) return;
    onAnswer(idx);
  };

  const getOptionStyles = (idx: number) => {
    const isEliminated = quizState.eliminatedOptions.includes(idx);
    if (isEliminated) {
      return 'opacity-25 pointer-events-none line-through border-stone-200 dark:border-stone-800 bg-stone-100/50 dark:bg-stone-900/50 text-stone-400';
    }

    if (!quizState.isAnswered) {
      return 'bg-white dark:bg-stone-900 border-stone-200 dark:border-stone-800 text-stone-900 dark:text-stone-100 hover:border-amber-500 hover:bg-amber-500/5 dark:hover:border-amber-500/80 shadow-sm';
    }

    // Answered state
    const isCorrect = idx === localizedQ.correctIndex;
    const isSelected = idx === quizState.selectedOption;

    if (isCorrect) {
      return 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 dark:border-emerald-500 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500/30 font-semibold';
    }

    if (isSelected && !isCorrect) {
      return 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 dark:border-rose-500 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500/30';
    }

    return 'opacity-40 border-stone-200 dark:border-stone-800 bg-stone-100/40 dark:bg-stone-900/30 text-stone-500';
  };

  const difficultyColors = {
    easy: 'text-emerald-700 bg-emerald-100 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800',
    medium: 'text-amber-700 bg-amber-100 dark:bg-amber-950/60 dark:text-amber-300 border-amber-200 dark:border-amber-800',
    hard: 'text-rose-700 bg-rose-100 dark:bg-rose-950/60 dark:text-rose-300 border-rose-200 dark:border-rose-800'
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 animate-fade-in">
      
      {/* Daily Challenge Alert Banner */}
      {quizState.isDailyChallenge && (
        <div className="p-3.5 rounded-2xl bg-gradient-to-r from-amber-500/20 via-amber-500/10 to-transparent border-2 border-amber-500/40 text-amber-900 dark:text-amber-200 flex items-center justify-between gap-3 text-xs font-bold shadow-sm">
          <div className="flex items-center gap-2">
            <span className="p-1.5 rounded-lg bg-amber-500 text-white">
              <Sparkles className="w-4 h-4" />
            </span>
            <span>{t.dailyChallenge} • {t.tenQuestionsAcrossCategories}</span>
          </div>
          <span className="px-2.5 py-1 rounded-lg bg-amber-500 text-white text-[11px] font-black uppercase tracking-wider animate-pulse">
            {t.doubleXpBadge}
          </span>
        </div>
      )}

      {/* Top Header Card: Progress, Category, Score & Streak */}
      <div className="bg-white dark:bg-stone-900 rounded-2xl p-4 sm:p-5 border border-stone-200 dark:border-stone-800 shadow-sm">
        <div className="flex items-center justify-between gap-4 mb-3">
          
          {/* Category Tag */}
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold px-3 py-1 rounded-lg bg-stone-100 dark:bg-stone-800 text-stone-800 dark:text-stone-200 border border-stone-200/80 dark:border-stone-700">
              {category?.title[currentLanguage] || currentQ.categoryId}
            </span>
            <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-md border ${difficultyColors[currentQ.difficulty]}`}>
              {t[currentQ.difficulty]}
            </span>
          </div>

          {/* Streak & Score */}
          <div className="flex items-center gap-3">
            {quizState.streak > 1 && (
              <div className="flex items-center gap-1 text-xs font-black text-amber-600 dark:text-amber-400 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-300 dark:border-amber-800 animate-pulse">
                <Flame className="w-4 h-4 fill-amber-500 text-amber-500" />
                <span>{quizState.streak}</span>
              </div>
            )}
            <div className="text-sm font-bold text-stone-700 dark:text-stone-300">
              {t.score}: <span className="text-amber-600 dark:text-amber-400 font-extrabold">{quizState.score}</span>
            </div>
            <button
              onClick={onQuitQuiz}
              className="text-xs font-medium text-stone-400 hover:text-stone-600 dark:hover:text-stone-200 px-2 py-1 rounded-md hover:bg-stone-100 dark:hover:bg-stone-800 transition-colors"
            >
              {isRtl ? 'خروج' : currentLanguage === 'fr' ? 'Quitter' : 'Quit'}
            </button>
          </div>

        </div>

        {/* Progress bar */}
        <div className="space-y-1.5">
          <div className="flex justify-between text-xs font-semibold text-stone-500 dark:text-stone-400">
            <span>
              {t.question} {quizState.currentIndex + 1} {t.of} {totalQuestions}
            </span>
            <span>{progressPercent}%</span>
          </div>
          <div className="w-full bg-stone-100 dark:bg-stone-800 rounded-full h-2 overflow-hidden">
            <div
              className="bg-gradient-to-r from-amber-600 to-amber-400 h-full rounded-full transition-all duration-300"
              style={{ width: `${Math.max(4, progressPercent)}%` }}
            />
          </div>
        </div>

      </div>

      {/* Lifelines Bar */}
      <div className="flex items-center justify-between gap-2 px-1">
        <div className="flex items-center gap-2">
          {/* 50:50 */}
          <button
            onClick={onUse5050}
            disabled={!quizState.lifelines.fiftyFifty || quizState.isAnswered}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold border transition-all ${
              quizState.lifelines.fiftyFifty && !quizState.isAnswered
                ? 'bg-white dark:bg-stone-900 border-amber-300 dark:border-amber-800 text-amber-700 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/30'
                : 'opacity-40 border-stone-200 dark:border-stone-800 bg-stone-100 dark:bg-stone-800/40 text-stone-400 cursor-not-allowed'
            }`}
            title={t.fiftyFifty}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>50:50</span>
          </button>

          {/* Skip */}
          <button
            onClick={onSkipQuestion}
            disabled={!quizState.lifelines.skip || quizState.isAnswered}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold border transition-all ${
              quizState.lifelines.skip && !quizState.isAnswered
                ? 'bg-white dark:bg-stone-900 border-stone-300 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-800'
                : 'opacity-40 border-stone-200 dark:border-stone-800 bg-stone-100 dark:bg-stone-800/40 text-stone-400 cursor-not-allowed'
            }`}
            title={t.skipQuestion}
          >
            <ArrowRight className={`w-3.5 h-3.5 ${isRtl ? 'rotate-180' : ''}`} />
            <span>{t.skipQuestion}</span>
          </button>

          {/* Hint */}
          <button
            onClick={() => {
              setRevealedHint(true);
              soundFx.playLifeline();
            }}
            disabled={revealedHint || quizState.isAnswered}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold border transition-all ${
              !revealedHint && !quizState.isAnswered
                ? 'bg-white dark:bg-stone-900 border-stone-300 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-800'
                : 'opacity-40 border-stone-200 dark:border-stone-800 bg-stone-100 dark:bg-stone-800/40 text-stone-400 cursor-not-allowed'
            }`}
            title={t.hint}
          >
            <HelpCircle className="w-3.5 h-3.5" />
            <span>{t.hint}</span>
          </button>
        </div>

        {/* Bookmark Question */}
        <button
          onClick={() => onToggleBookmark(currentQ.id)}
          className={`p-2 rounded-xl border transition-colors ${
            isBookmarked
              ? 'bg-amber-500/10 border-amber-300 dark:border-amber-700 text-amber-600 dark:text-amber-400'
              : 'bg-white dark:bg-stone-900 border-stone-200 dark:border-stone-800 text-stone-400 hover:text-stone-600 dark:hover:text-stone-200'
          }`}
          title={isBookmarked ? t.bookmarked : t.bookmark}
        >
          {isBookmarked ? <BookmarkCheck className="w-4 h-4 fill-current" /> : <Bookmark className="w-4 h-4" />}
        </button>
      </div>

      {/* Question Main Card */}
      <div className="bg-white dark:bg-stone-900 rounded-3xl p-6 sm:p-8 border border-stone-200 dark:border-stone-800 shadow-sm relative overflow-hidden">
        <div className="flex items-start gap-4">
          <div className="w-10 h-10 rounded-2xl bg-amber-500/10 text-amber-700 dark:text-amber-400 flex items-center justify-center font-bold text-sm shrink-0 border border-amber-500/20">
            #{currentQ.id}
          </div>
          <div className="flex-1">
            <h1 className="text-xl sm:text-2xl font-extrabold text-stone-900 dark:text-stone-100 leading-relaxed font-sans">
              {localizedQ.question}
            </h1>
          </div>
        </div>

        {/* Pre-answer hint if requested */}
        {revealedHint && !quizState.isAnswered && (
          <div className="mt-4 p-3.5 rounded-xl bg-amber-500/10 border border-amber-300 dark:border-amber-800/80 text-amber-900 dark:text-amber-200 text-xs leading-relaxed flex items-start gap-2.5">
            <HelpCircle className="w-4 h-4 shrink-0 text-amber-600 dark:text-amber-400 mt-0.5" />
            <div>
              <span className="font-bold">{t.hint}: </span>
              {localizedQ.explanation.slice(0, 100)}...
            </div>
          </div>
        )}
      </div>

      {/* 4 Interactive Option Buttons */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
        {localizedQ.options.map((opt, idx) => {
          const isCorrect = idx === localizedQ.correctIndex;
          const isSelected = idx === quizState.selectedOption;
          const letter = optionLetters[idx];

          return (
            <button
              key={idx}
              onClick={() => handleSelectOption(idx)}
              disabled={quizState.isAnswered || quizState.eliminatedOptions.includes(idx)}
              className={`text-start p-4 sm:p-5 rounded-2xl border transition-all duration-200 flex items-center justify-between gap-3 group relative ${getOptionStyles(idx)}`}
            >
              <div className="flex items-center gap-3">
                <span className="w-8 h-8 rounded-xl bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 font-bold text-sm flex items-center justify-center border border-stone-200/80 dark:border-stone-700/80 shrink-0 group-hover:bg-amber-500 group-hover:text-white transition-colors">
                  {letter}
                </span>
                <span className="text-sm sm:text-base font-medium leading-normal">
                  {opt}
                </span>
              </div>

              {quizState.isAnswered && (
                <div className="shrink-0">
                  {isCorrect ? (
                    <CheckCircle2 className="w-5 h-5 text-emerald-500 fill-emerald-500/20" />
                  ) : isSelected ? (
                    <XCircle className="w-5 h-5 text-rose-500 fill-rose-500/20" />
                  ) : null}
                </div>
              )}
            </button>
          );
        })}
      </div>

      {/* Answer & Explanation Box (Unfolds upon answering) */}
      {quizState.isAnswered && (
        <div className="bg-stone-50 dark:bg-stone-900/90 rounded-2xl p-5 border border-stone-200 dark:border-stone-800 shadow-sm space-y-4">
          <div className="flex items-center gap-2.5">
            {quizState.selectedOption === localizedQ.correctIndex ? (
              <div className="flex items-center gap-2 text-emerald-700 dark:text-emerald-400 font-bold text-sm">
                <CheckCircle2 className="w-5 h-5 text-emerald-500" />
                <span>{t.correctAnswer}</span>
              </div>
            ) : (
              <div className="flex items-center gap-2 text-rose-700 dark:text-rose-400 font-bold text-sm">
                <XCircle className="w-5 h-5 text-rose-500" />
                <span>{t.wrongAnswer}</span>
              </div>
            )}
          </div>

          <div className="p-4 rounded-xl bg-white dark:bg-stone-800/80 border border-stone-200/70 dark:border-stone-700/60 text-xs sm:text-sm text-stone-700 dark:text-stone-300 leading-relaxed flex items-start gap-3">
            <BookOpen className="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0 mt-0.5" />
            <div>
              <div className="font-bold text-stone-900 dark:text-stone-100 mb-1">
                {t.explanation}
              </div>
              <p>{localizedQ.explanation}</p>
            </div>
          </div>

          <div className="flex justify-end pt-2">
            <button
              onClick={onNextQuestion}
              autoFocus
              className="w-full sm:w-auto px-6 py-3 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-sm shadow-md shadow-amber-600/20 flex items-center justify-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <span>
                {quizState.currentIndex + 1 >= totalQuestions
                  ? t.finishQuiz
                  : t.nextQuestion}
              </span>
              {isRtl ? <ArrowLeft className="w-4 h-4" /> : <ArrowRight className="w-4 h-4" />}
            </button>
          </div>
        </div>
      )}

    </div>
  );
};
