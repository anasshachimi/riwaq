import React, { useState, useMemo } from 'react';
import {
  Search,
  BookOpen,
  Bookmark,
  BookmarkCheck,
  Eye,
  EyeOff,
  CheckCircle2,
  Sparkles,
  Play
} from 'lucide-react';
import { Question, Language, Difficulty } from '../types';
import { CATEGORIES, CATEGORY_MAP } from '../data/categories';
import { TRANSLATIONS } from '../data/translations';
import { CategoryIcon } from './CategoryIcon';

interface QuestionLibraryProps {
  questions: Question[];
  currentLanguage: Language;
  bookmarks: number[];
  onToggleBookmark: (id: number) => void;
  onPlaySingleQuestion: (q: Question) => void;
}

export const QuestionLibrary: React.FC<QuestionLibraryProps> = ({
  questions,
  currentLanguage,
  bookmarks,
  onToggleBookmark,
  onPlaySingleQuestion
}) => {
  const t = TRANSLATIONS[currentLanguage];

  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [onlyBookmarks, setOnlyBookmarks] = useState(false);
  const [revealedAnswers, setRevealedAnswers] = useState<Record<number, boolean>>({});
  const [page, setPage] = useState(1);
  const itemsPerPage = 20;

  const toggleAnswer = (id: number) => {
    setRevealedAnswers(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const filteredQuestions = useMemo(() => {
    const term = searchTerm.toLowerCase().trim();

    return questions.filter(q => {
      // Category filter
      if (selectedCategory !== 'all' && q.categoryId !== selectedCategory) {
        return false;
      }

      // Difficulty filter
      if (selectedDifficulty !== 'all' && q.difficulty !== selectedDifficulty) {
        return false;
      }

      // Bookmarks filter
      if (onlyBookmarks && !bookmarks.includes(q.id)) {
        return false;
      }

      // Search query
      if (term) {
        const localized = q[currentLanguage];
        const matchesQuestion = localized.question.toLowerCase().includes(term);
        const matchesOptions = localized.options.some(opt => opt.toLowerCase().includes(term));
        const matchesExplanation = localized.explanation.toLowerCase().includes(term);
        if (!matchesQuestion && !matchesOptions && !matchesExplanation) {
          return false;
        }
      }

      return true;
    });
  }, [questions, currentLanguage, selectedCategory, selectedDifficulty, onlyBookmarks, searchTerm, bookmarks]);

  // Pagination
  const totalPages = Math.max(1, Math.ceil(filteredQuestions.length / itemsPerPage));
  const displayedQuestions = useMemo(() => {
    const start = (page - 1) * itemsPerPage;
    return filteredQuestions.slice(start, start + itemsPerPage);
  }, [filteredQuestions, page]);

  const difficultyColors: Record<Difficulty, string> = {
    easy: 'text-emerald-700 bg-emerald-100 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800',
    medium: 'text-amber-700 bg-amber-100 dark:bg-amber-950/60 dark:text-amber-300 border-amber-200 dark:border-amber-800',
    hard: 'text-rose-700 bg-rose-100 dark:bg-rose-950/60 dark:text-rose-300 border-rose-200 dark:border-rose-800'
  };

  return (
    <div className="space-y-6 animate-fade-in pb-12">
      
      {/* Search & Filter Header */}
      <div className="bg-white dark:bg-stone-900 rounded-3xl p-5 sm:p-6 border border-stone-200 dark:border-stone-800 shadow-sm space-y-4">
        
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h2 className="text-xl sm:text-2xl font-black text-stone-900 dark:text-stone-100 tracking-tight flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-amber-600 dark:text-amber-400" />
              <span>{t.browseLibrary}</span>
            </h2>
            <p className="text-xs sm:text-sm text-stone-500 dark:text-stone-400 mt-0.5">
              {filteredQuestions.length} {t.questionsFound} ({questions.length} {t.of} 1000)
            </p>
          </div>

          {/* Bookmarks toggle */}
          <button
            onClick={() => {
              setOnlyBookmarks(!onlyBookmarks);
              setPage(1);
            }}
            className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-bold border transition-all ${
              onlyBookmarks
                ? 'bg-amber-500 text-white border-amber-500 shadow-sm'
                : 'bg-stone-100 dark:bg-stone-800 border-stone-200 dark:border-stone-700 text-stone-700 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700'
            }`}
          >
            <Bookmark className="w-4 h-4" />
            <span>{t.bookmarked} ({bookmarks.length})</span>
          </button>
        </div>

        {/* Search Input Bar */}
        <div className="relative">
          <Search className="w-5 h-5 text-stone-400 absolute top-1/2 -translate-y-1/2 start-3.5 pointer-events-none" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setPage(1);
            }}
            placeholder={t.searchQuestions}
            className="w-full ps-11 pe-4 py-3 rounded-2xl bg-stone-100 dark:bg-stone-800/80 border border-stone-200 dark:border-stone-700 text-sm text-stone-900 dark:text-stone-100 placeholder:text-stone-400 focus:outline-none focus:ring-2 focus:ring-amber-500/30 focus:border-amber-500"
          />
        </div>

        {/* Category Pills Slider */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none pt-1">
          <button
            onClick={() => {
              setSelectedCategory('all');
              setPage(1);
            }}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all ${
              selectedCategory === 'all'
                ? 'bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900 shadow-sm'
                : 'bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-400 hover:bg-stone-200 dark:hover:bg-stone-700'
            }`}
          >
            {t.allCategories}
          </button>
          {CATEGORIES.map(c => (
            <button
              key={c.id}
              onClick={() => {
                setSelectedCategory(c.id);
                setPage(1);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all ${
                selectedCategory === c.id
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-400 hover:bg-stone-200 dark:hover:bg-stone-700'
              }`}
            >
              <CategoryIcon name={c.icon} className="w-3.5 h-3.5" />
              <span>{c.title[currentLanguage]}</span>
            </button>
          ))}
        </div>

        {/* Difficulty Filter */}
        <div className="flex items-center gap-2 pt-1 border-t border-stone-100 dark:border-stone-800 text-xs">
          <span className="font-semibold text-stone-400">{t.difficulty}:</span>
          {(['all', 'easy', 'medium', 'hard'] as const).map(diff => (
            <button
              key={diff}
              onClick={() => {
                setSelectedDifficulty(diff);
                setPage(1);
              }}
              className={`px-2.5 py-1 rounded-lg font-bold transition-all ${
                selectedDifficulty === diff
                  ? 'bg-amber-500/15 text-amber-700 dark:text-amber-300 border border-amber-300 dark:border-amber-700'
                  : 'text-stone-600 dark:text-stone-400 hover:bg-stone-100 dark:hover:bg-stone-800'
              }`}
            >
              {diff === 'all' ? t.allDifficulties : t[diff]}
            </button>
          ))}
        </div>

      </div>

      {/* Questions List */}
      {displayedQuestions.length === 0 ? (
        <div className="bg-white dark:bg-stone-900 rounded-3xl p-12 text-center border border-stone-200 dark:border-stone-800 text-stone-500">
          <Sparkles className="w-10 h-10 mx-auto text-amber-500 mb-3 opacity-60" />
          <p className="font-bold text-base text-stone-800 dark:text-stone-200">
            {t.noQuestionsFound}
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {displayedQuestions.map((q) => {
            const localized = q[currentLanguage];
            const cat = CATEGORY_MAP.get(q.categoryId);
            const isRevealed = revealedAnswers[q.id];
            const isBookmarked = bookmarks.includes(q.id);

            return (
              <div
                key={q.id}
                className="bg-white dark:bg-stone-900 rounded-2xl p-5 border border-stone-200 dark:border-stone-800 shadow-sm hover:border-stone-300 dark:hover:border-stone-700 transition-all space-y-4"
              >
                {/* Header row */}
                <div className="flex items-center justify-between gap-3">
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-bold text-stone-400 bg-stone-100 dark:bg-stone-800 px-2.5 py-1 rounded-md">
                      #{q.id}
                    </span>
                    <span className="text-xs font-semibold px-2.5 py-1 rounded-md bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 flex items-center gap-1.5">
                      {cat && <CategoryIcon name={cat.icon} className="w-3 h-3 text-amber-500" />}
                      {cat?.title[currentLanguage] || q.categoryId}
                    </span>
                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded-md border ${difficultyColors[q.difficulty]}`}>
                      {t[q.difficulty]}
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => onPlaySingleQuestion(q)}
                      className="p-1.5 rounded-lg text-stone-500 hover:text-amber-600 hover:bg-amber-50 dark:hover:bg-stone-800 transition-colors"
                      title={t.playCategory}
                    >
                      <Play className="w-4 h-4" />
                    </button>
                    <button
                      onClick={() => onToggleBookmark(q.id)}
                      className={`p-1.5 rounded-lg transition-colors ${
                        isBookmarked
                          ? 'text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/40'
                          : 'text-stone-400 hover:text-stone-600 dark:hover:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800'
                      }`}
                      title={isBookmarked ? t.bookmarked : t.bookmark}
                    >
                      {isBookmarked ? <BookmarkCheck className="w-4 h-4 fill-current" /> : <Bookmark className="w-4 h-4" />}
                    </button>
                  </div>
                </div>

                {/* Question text */}
                <div className="text-base sm:text-lg font-bold text-stone-900 dark:text-stone-100 leading-snug">
                  {localized.question}
                </div>

                {/* Options 2x2 grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs sm:text-sm">
                  {localized.options.map((opt, optIdx) => {
                    const isCorrect = optIdx === localized.correctIndex;
                    return (
                      <div
                        key={optIdx}
                        className={`p-2.5 rounded-xl border flex items-center justify-between gap-2 transition-all ${
                          isRevealed && isCorrect
                            ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-950 dark:text-emerald-100 font-bold'
                            : 'bg-stone-50 dark:bg-stone-800/60 border-stone-200/80 dark:border-stone-800 text-stone-800 dark:text-stone-200'
                        }`}
                      >
                        <span className="line-clamp-1">{opt}</span>
                        {isRevealed && isCorrect && (
                          <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" />
                        )}
                      </div>
                    );
                  })}
                </div>

                {/* Reveal Answer Toggle */}
                <div className="pt-2 border-t border-stone-100 dark:border-stone-800 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                  <button
                    onClick={() => toggleAnswer(q.id)}
                    className="flex items-center gap-1.5 text-xs font-bold text-amber-600 dark:text-amber-400 hover:text-amber-700 dark:hover:text-amber-300 transition-colors w-fit"
                  >
                    {isRevealed ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
                    <span>{isRevealed ? t.hideAnswer : t.showAnswer}</span>
                  </button>

                  {isRevealed && (
                    <div className="text-xs text-stone-600 dark:text-stone-400 flex items-start gap-1.5 bg-stone-50 dark:bg-stone-800/80 p-2.5 rounded-xl border border-stone-200/80 dark:border-stone-700/80 w-full mt-1">
                      <BookOpen className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400 shrink-0 mt-0.5" />
                      <div>
                        <span className="font-bold text-stone-900 dark:text-stone-100">{t.explanation}: </span>
                        <span>{localized.explanation}</span>
                      </div>
                    </div>
                  )}
                </div>

              </div>
            );
          })}
        </div>
      )}

      {/* Pagination controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 pt-4">
          <button
            onClick={() => setPage(p => Math.max(1, p - 1))}
            disabled={page === 1}
            className="px-3.5 py-2 rounded-xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 text-xs font-bold text-stone-700 dark:text-stone-300 disabled:opacity-30 disabled:cursor-not-allowed hover:bg-stone-50 dark:hover:bg-stone-800"
          >
            Prev
          </button>
          <span className="text-xs font-semibold text-stone-500 px-3">
            {page} / {totalPages}
          </span>
          <button
            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
            className="px-3.5 py-2 rounded-xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 text-xs font-bold text-stone-700 dark:text-stone-300 disabled:opacity-30 disabled:cursor-not-allowed hover:bg-stone-50 dark:hover:bg-stone-800"
          >
            Next
          </button>
        </div>
      )}

    </div>
  );
};
