import React from 'react';
import { Play, Sparkles, Award } from 'lucide-react';
import { CATEGORIES } from '../data/categories';
import { Language, UserStats } from '../types';
import { TRANSLATIONS } from '../data/translations';
import { CategoryIcon } from './CategoryIcon';

interface CategoryGridProps {
  currentLanguage: Language;
  userStats: UserStats;
  onSelectCategory: (categoryId: string, count?: number) => void;
}

const COLOR_MAP: Record<string, { bg: string; text: string; border: string; badge: string }> = {
  amber: {
    bg: 'bg-amber-500/10 dark:bg-amber-500/15',
    text: 'text-amber-700 dark:text-amber-400',
    border: 'border-amber-200 dark:border-amber-900/60',
    badge: 'bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-300'
  },
  emerald: {
    bg: 'bg-emerald-500/10 dark:bg-emerald-500/15',
    text: 'text-emerald-700 dark:text-emerald-400',
    border: 'border-emerald-200 dark:border-emerald-900/60',
    badge: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-300'
  },
  cyan: {
    bg: 'bg-cyan-500/10 dark:bg-cyan-500/15',
    text: 'text-cyan-700 dark:text-cyan-400',
    border: 'border-cyan-200 dark:border-cyan-900/60',
    badge: 'bg-cyan-100 text-cyan-800 dark:bg-cyan-900/50 dark:text-cyan-300'
  },
  rose: {
    bg: 'bg-rose-500/10 dark:bg-rose-500/15',
    text: 'text-rose-700 dark:text-rose-400',
    border: 'border-rose-200 dark:border-rose-900/60',
    badge: 'bg-rose-100 text-rose-800 dark:bg-rose-900/50 dark:text-rose-300'
  },
  indigo: {
    bg: 'bg-indigo-500/10 dark:bg-indigo-500/15',
    text: 'text-indigo-700 dark:text-indigo-400',
    border: 'border-indigo-200 dark:border-indigo-900/60',
    badge: 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900/50 dark:text-indigo-300'
  },
  orange: {
    bg: 'bg-orange-500/10 dark:bg-orange-500/15',
    text: 'text-orange-700 dark:text-orange-400',
    border: 'border-orange-200 dark:border-orange-900/60',
    badge: 'bg-orange-100 text-orange-800 dark:bg-orange-900/50 dark:text-orange-300'
  },
  blue: {
    bg: 'bg-blue-500/10 dark:bg-blue-500/15',
    text: 'text-blue-700 dark:text-blue-400',
    border: 'border-blue-200 dark:border-blue-900/60',
    badge: 'bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300'
  },
  teal: {
    bg: 'bg-teal-500/10 dark:bg-teal-500/15',
    text: 'text-teal-700 dark:text-teal-400',
    border: 'border-teal-200 dark:border-teal-900/60',
    badge: 'bg-teal-100 text-teal-800 dark:bg-teal-900/50 dark:text-teal-300'
  },
  red: {
    bg: 'bg-red-500/10 dark:bg-red-500/15',
    text: 'text-red-700 dark:text-red-400',
    border: 'border-red-200 dark:border-red-900/60',
    badge: 'bg-red-100 text-red-800 dark:bg-red-900/50 dark:text-red-300'
  },
  violet: {
    bg: 'bg-violet-500/10 dark:bg-violet-500/15',
    text: 'text-violet-700 dark:text-violet-400',
    border: 'border-violet-200 dark:border-violet-900/60',
    badge: 'bg-violet-100 text-violet-800 dark:bg-violet-900/50 dark:text-violet-300'
  }
};

export const CategoryGrid: React.FC<CategoryGridProps> = ({
  currentLanguage,
  userStats,
  onSelectCategory
}) => {
  const t = TRANSLATIONS[currentLanguage];

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-stone-200 dark:border-stone-800 pb-4">
        <div>
          <h2 className="text-2xl font-black text-stone-900 dark:text-stone-100 tracking-tight flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-amber-600 dark:text-amber-400" />
            <span>{t.categoryDeepDive}</span>
          </h2>
          <p className="text-sm text-stone-600 dark:text-stone-400 mt-1">
            {currentLanguage === 'ar'
              ? '10 أصناف معرفية شاملة، كل صنف يضم 100 سؤال موثق مع الشروحات'
              : currentLanguage === 'fr'
              ? '10 thèmes complets du savoir, chacun renfermant 100 questions détaillées'
              : '10 comprehensive knowledge domains, each featuring 100 verified questions'}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs font-semibold px-3 py-1 rounded-full bg-amber-500/10 text-amber-700 dark:text-amber-400 border border-amber-200 dark:border-amber-900/50">
            {t.tenCategories}
          </span>
          <span className="text-xs font-semibold px-3 py-1 rounded-full bg-stone-200/80 dark:bg-stone-800 text-stone-700 dark:text-stone-300">
            {t.totalQuestionsCount}
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
        {CATEGORIES.map((cat) => {
          const colorStyles = COLOR_MAP[cat.color] || COLOR_MAP.amber;
          const stat = userStats.categoryStats[cat.id] || { answered: 0, correct: 0 };
          const progressPercent = Math.min(100, Math.round((stat.answered / 100) * 100));

          return (
            <div
              key={cat.id}
              className="group relative bg-white dark:bg-stone-900/90 rounded-2xl p-5 border border-stone-200/90 dark:border-stone-800 shadow-sm hover:shadow-md transition-all duration-200 flex flex-col justify-between hover:border-amber-400/80 dark:hover:border-amber-500/50"
            >
              <div>
                <div className="flex items-start justify-between gap-3 mb-3">
                  <div
                    className={`w-12 h-12 rounded-xl flex items-center justify-center ${colorStyles.bg} ${colorStyles.text} transition-transform group-hover:scale-105`}
                  >
                    <CategoryIcon name={cat.icon} className="w-6 h-6" />
                  </div>
                  <span className={`text-[11px] font-bold px-2 py-0.5 rounded-md ${colorStyles.badge}`}>
                    100 Qs
                  </span>
                </div>

                <h3 className="font-bold text-base text-stone-900 dark:text-stone-100 group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors leading-snug">
                  {cat.title[currentLanguage]}
                </h3>

                <p className="text-xs text-stone-500 dark:text-stone-400 mt-2 line-clamp-2 leading-relaxed">
                  {cat.description[currentLanguage]}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-stone-100 dark:border-stone-800/80">
                {/* Mastery progress */}
                <div className="flex items-center justify-between text-[11px] text-stone-500 dark:text-stone-400 mb-1.5 font-medium">
                  <span className="flex items-center gap-1">
                    <Award className="w-3.5 h-3.5 text-amber-500" />
                    {stat.answered}/100
                  </span>
                  <span>{progressPercent}%</span>
                </div>
                <div className="w-full bg-stone-100 dark:bg-stone-800 rounded-full h-1.5 overflow-hidden">
                  <div
                    className="bg-amber-500 h-full rounded-full transition-all duration-300"
                    style={{ width: `${progressPercent}%` }}
                  />
                </div>

                <div className="mt-3 flex gap-2">
                  <button
                    onClick={() => onSelectCategory(cat.id, 10)}
                    className="flex-1 py-2 px-3 rounded-xl bg-stone-100 dark:bg-stone-800 hover:bg-amber-500 hover:text-white dark:hover:bg-amber-600 text-stone-800 dark:text-stone-200 text-xs font-bold transition-all flex items-center justify-center gap-1.5"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>10 Qs</span>
                  </button>
                  <button
                    onClick={() => onSelectCategory(cat.id, 25)}
                    className="py-2 px-2.5 rounded-xl bg-stone-100 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-700 dark:text-stone-300 text-xs font-semibold transition-all"
                    title="25 Questions"
                  >
                    25
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
