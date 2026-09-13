import React, { useState } from 'react';
import {
  X,
  Trophy,
  Flame,
  CheckCircle2,
  Bookmark,
  Trash2,
  Award,
  Zap,
  Crown,
  Calendar
} from 'lucide-react';
import { Language, UserStats } from '../types';
import { CATEGORIES } from '../data/categories';
import { TRANSLATIONS } from '../data/translations';
import { CategoryIcon } from './CategoryIcon';

interface StatsModalProps {
  isOpen: boolean;
  onClose: () => void;
  userStats: UserStats;
  currentLanguage: Language;
  onResetStats: () => void;
}

export const StatsModal: React.FC<StatsModalProps> = ({
  isOpen,
  onClose,
  userStats,
  currentLanguage,
  onResetStats
}) => {
  const [confirmingReset, setConfirmingReset] = useState(false);
  const t = TRANSLATIONS[currentLanguage];

  if (!isOpen) return null;

  const totalAnswered = userStats.totalAnswered;
  const accuracy = totalAnswered > 0
    ? Math.round((userStats.totalCorrect / totalAnswered) * 100)
    : 0;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/60 backdrop-blur-sm animate-fade-in">
      <div
        className="bg-white dark:bg-stone-900 rounded-3xl max-w-lg w-full p-6 border border-stone-200 dark:border-stone-800 shadow-2xl space-y-6 max-h-[90vh] overflow-y-auto"
        role="dialog"
      >
        {/* Header */}
        <div className="flex items-center justify-between border-b border-stone-100 dark:border-stone-800 pb-4">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center">
              <Trophy className="w-5 h-5" />
            </div>
            <h2 className="text-lg font-black text-stone-900 dark:text-stone-100">
              {t.playerStats}
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-xl text-stone-400 hover:text-stone-600 dark:hover:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Top XP & Daily Challenge Banner */}
        <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-500/15 via-amber-500/10 to-orange-500/15 border border-amber-400/40 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-500 text-white flex items-center justify-center shadow-md">
              <Zap className="w-5 h-5 fill-current" />
            </div>
            <div>
              <div className="text-xs font-bold text-amber-800 dark:text-amber-300">
                {t.totalXp}
              </div>
              <div className="text-2xl font-black text-amber-900 dark:text-amber-100">
                {userStats.totalXp.toLocaleString()} <span className="text-xs font-bold text-amber-600 dark:text-amber-400">XP</span>
              </div>
            </div>
          </div>

          <div className="text-end">
            <div className="text-xs font-semibold text-stone-500 dark:text-stone-400 flex items-center gap-1 justify-end">
              <Flame className="w-3.5 h-3.5 text-orange-500 fill-current" />
              <span>{t.dailyStreak}</span>
            </div>
            <div className="text-xl font-black text-orange-600 dark:text-orange-400">
              {userStats.dailyStreak} <span className="text-xs font-bold">{t.dailyStreakDays}</span>
            </div>
          </div>
        </div>

        {/* 4 Metric Cards */}
        <div className="grid grid-cols-2 gap-3">
          <div className="p-3.5 rounded-2xl bg-stone-50 dark:bg-stone-800/60 border border-stone-200/80 dark:border-stone-700/80">
            <div className="text-xs font-semibold text-stone-500 dark:text-stone-400 mb-1">
              {t.totalAnswered}
            </div>
            <div className="text-2xl font-black text-stone-900 dark:text-stone-100">
              {totalAnswered} <span className="text-xs font-bold text-stone-400">/ 1000</span>
            </div>
          </div>

          <div className="p-3.5 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/80">
            <div className="text-xs font-semibold text-emerald-700 dark:text-emerald-400 mb-1 flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5" />
              <span>{t.accuracy}</span>
            </div>
            <div className="text-2xl font-black text-emerald-700 dark:text-emerald-300">
              {accuracy}%
            </div>
          </div>

          <div className="p-3.5 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/80">
            <div className="text-xs font-semibold text-amber-700 dark:text-amber-400 mb-1 flex items-center gap-1">
              <Flame className="w-3.5 h-3.5" />
              <span>{t.highestStreak}</span>
            </div>
            <div className="text-2xl font-black text-amber-700 dark:text-amber-300">
              {userStats.highestScore}
            </div>
          </div>

          <div className="p-3.5 rounded-2xl bg-stone-50 dark:bg-stone-800/60 border border-stone-200/80 dark:border-stone-700/80">
            <div className="text-xs font-semibold text-stone-500 dark:text-stone-400 mb-1 flex items-center gap-1">
              <Bookmark className="w-3.5 h-3.5" />
              <span>{t.bookmarked}</span>
            </div>
            <div className="text-2xl font-black text-stone-900 dark:text-stone-100">
              {userStats.bookmarks.length}
            </div>
          </div>
        </div>

        {/* Earned Badges Section */}
        {userStats.badges && userStats.badges.length > 0 && (
          <div className="space-y-2.5 pt-2">
            <div className="text-xs font-bold uppercase tracking-wider text-stone-400 flex items-center gap-1.5">
              <Crown className="w-4 h-4 text-amber-500" />
              <span>{t.earnedBadges} ({userStats.badges.length})</span>
            </div>

            <div className="space-y-2 max-h-48 overflow-y-auto pe-1">
              {userStats.badges.map((badge, i) => (
                <div
                  key={`${badge.id}-${i}`}
                  className="p-3 rounded-xl bg-amber-500/10 dark:bg-amber-950/20 border border-amber-400/30 flex items-center justify-between gap-3 text-xs"
                >
                  <div className="flex items-center gap-2.5">
                    <div className="w-8 h-8 rounded-lg bg-amber-500 text-white flex items-center justify-center shrink-0">
                      <Crown className="w-4 h-4" />
                    </div>
                    <div>
                      <div className="font-bold text-stone-900 dark:text-stone-100">
                        {badge.title[currentLanguage]}
                      </div>
                      <div className="text-[11px] text-stone-500 dark:text-stone-400 flex items-center gap-1">
                        <Calendar className="w-3 h-3" />
                        <span>{badge.date}</span>
                      </div>
                    </div>
                  </div>
                  <span className="font-extrabold text-amber-600 dark:text-amber-400 bg-white dark:bg-stone-800 px-2 py-0.5 rounded border border-amber-300 dark:border-amber-700 shrink-0">
                    +{badge.xpAwarded} XP
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Category Mastery Progress Bars */}
        <div className="space-y-3 pt-2">
          <div className="text-xs font-bold uppercase tracking-wider text-stone-400 flex items-center gap-1.5">
            <Award className="w-4 h-4 text-amber-500" />
            <span>{t.categoryMastery}</span>
          </div>

          <div className="space-y-2.5">
            {CATEGORIES.map(c => {
              const stat = userStats.categoryStats[c.id] || { answered: 0, correct: 0 };
              const percent = Math.min(100, Math.round((stat.answered / 100) * 100));

              return (
                <div key={c.id} className="space-y-1">
                  <div className="flex items-center justify-between text-xs font-semibold text-stone-700 dark:text-stone-300">
                    <div className="flex items-center gap-2">
                      <CategoryIcon name={c.icon} className="w-3.5 h-3.5 text-amber-500" />
                      <span>{c.title[currentLanguage]}</span>
                    </div>
                    <span className="text-stone-400">
                      {stat.answered}/100 ({percent}%)
                    </span>
                  </div>
                  <div className="w-full bg-stone-100 dark:bg-stone-800 rounded-full h-1.5 overflow-hidden">
                    <div
                      className="bg-amber-500 h-full rounded-full transition-all duration-300"
                      style={{ width: `${percent}%` }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Reset Stats or Close */}
        <div className="pt-4 border-t border-stone-100 dark:border-stone-800 flex items-center justify-between gap-3">
          {confirmingReset ? (
            <div className="flex items-center gap-2 w-full">
              <button
                onClick={() => {
                  onResetStats();
                  setConfirmingReset(false);
                }}
                className="flex-1 py-2 px-3 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition-colors"
              >
                {t.confirmReset}
              </button>
              <button
                onClick={() => setConfirmingReset(false)}
                className="py-2 px-3 rounded-xl bg-stone-200 dark:bg-stone-800 text-stone-700 dark:text-stone-300 font-bold text-xs"
              >
                {t.close}
              </button>
            </div>
          ) : (
            <button
              onClick={() => setConfirmingReset(true)}
              className="flex items-center gap-1.5 text-xs text-rose-600 dark:text-rose-400 hover:underline font-semibold"
            >
              <Trash2 className="w-3.5 h-3.5" />
              <span>{t.resetStats}</span>
            </button>
          )}

          <button
            onClick={onClose}
            className="py-2 px-5 rounded-xl bg-stone-900 dark:bg-stone-100 text-white dark:text-stone-900 font-bold text-xs hover:opacity-90 transition-opacity ms-auto"
          >
            {t.close}
          </button>
        </div>

      </div>
    </div>
  );
};

