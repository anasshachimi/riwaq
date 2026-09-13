import React, { useState, useEffect } from 'react';
import {
  Calendar,
  Zap,
  Flame,
  Clock,
  CheckCircle2,
  Award,
  ArrowRight,
  ArrowLeft,
  Crown
} from 'lucide-react';
import { Language, UserStats } from '../types';
import { TRANSLATIONS } from '../data/translations';
import { getTodayDateString, getTimeUntilMidnight } from '../utils/dailyChallenge';

interface DailyChallengeCardProps {
  currentLanguage: Language;
  userStats: UserStats;
  onStartDailyChallenge: () => void;
}

export const DailyChallengeCard: React.FC<DailyChallengeCardProps> = ({
  currentLanguage,
  userStats,
  onStartDailyChallenge
}) => {
  const t = TRANSLATIONS[currentLanguage];
  const isRtl = currentLanguage === 'ar';
  const todayStr = getTodayDateString();

  const isCompletedToday = userStats.completedDailyDates.includes(todayStr);

  const [timeLeft, setTimeLeft] = useState(getTimeUntilMidnight());

  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeft(getTimeUntilMidnight());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  // Format today's date according to locale
  const formattedTodayDate = new Intl.DateTimeFormat(
    currentLanguage === 'ar' ? 'ar-EG' : currentLanguage === 'fr' ? 'fr-FR' : 'en-US',
    { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }
  ).format(new Date());

  // Today's badge if completed
  const todayBadge = userStats.badges.find(b => b.date === todayStr);

  return (
    <div
      id="daily-challenge-card"
      className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-amber-500/10 via-amber-600/5 to-transparent dark:from-amber-950/40 dark:via-stone-900 dark:to-stone-900 border-2 border-amber-500/40 dark:border-amber-600/50 p-6 sm:p-8 shadow-md transition-all hover:shadow-lg"
    >
      {/* Glow decorative accent */}
      <div className="absolute top-0 end-0 w-64 h-64 bg-amber-500/15 rounded-full blur-3xl pointer-events-none -mt-16 -me-16" />

      <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        
        {/* Left Info Column */}
        <div className="space-y-3 max-w-2xl">
          
          <div className="flex flex-wrap items-center gap-2.5">
            {/* Main Label */}
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-500 text-white font-extrabold text-xs shadow-sm">
              <Calendar className="w-3.5 h-3.5" />
              <span>{t.dailyChallenge}</span>
            </span>

            {/* Double XP Chip */}
            <span className="inline-flex items-center gap-1 px-3 py-1 rounded-xl bg-amber-500/20 dark:bg-amber-400/20 text-amber-800 dark:text-amber-300 font-black text-xs border border-amber-500/30 animate-pulse">
              <Zap className="w-3.5 h-3.5 fill-current" />
              <span>{t.doubleXpBadge}</span>
            </span>

            {/* Streak Counter Chip */}
            {userStats.dailyStreak > 0 && (
              <span className="inline-flex items-center gap-1 px-3 py-1 rounded-xl bg-orange-500/15 text-orange-700 dark:text-orange-400 font-bold text-xs border border-orange-500/30">
                <Flame className="w-3.5 h-3.5 fill-current" />
                <span>
                  {userStats.dailyStreak} {t.dailyStreakDays}
                </span>
              </span>
            )}
          </div>

          <div>
            <h3 className="text-xl sm:text-2xl font-black text-stone-900 dark:text-stone-100 tracking-tight flex items-center gap-2">
              <span>{t.todayChallenge}</span>
              <span className="text-xs font-semibold text-stone-500 dark:text-stone-400 font-normal">
                • {formattedTodayDate}
              </span>
            </h3>

            <p className="text-sm text-stone-600 dark:text-stone-300 mt-1 leading-relaxed">
              {t.dailyChallengeDesc}
            </p>
          </div>

          {/* Details Row: 10 Qs Across Categories + Countdown */}
          <div className="flex flex-wrap items-center gap-4 text-xs font-semibold text-stone-600 dark:text-stone-400 pt-1">
            <div className="flex items-center gap-1.5">
              <Award className="w-4 h-4 text-amber-600 dark:text-amber-400" />
              <span>{t.tenQuestionsAcrossCategories}</span>
            </div>

            <div className="flex items-center gap-1.5 bg-stone-100 dark:bg-stone-800/80 px-2.5 py-1 rounded-lg border border-stone-200 dark:border-stone-700/60 font-mono text-stone-800 dark:text-stone-200">
              <Clock className="w-3.5 h-3.5 text-amber-500" />
              <span>{t.nextChallengeIn}: {timeLeft.formatted}</span>
            </div>
          </div>

          {/* If already completed, show earned badge summary */}
          {isCompletedToday && todayBadge && (
            <div className="p-3.5 rounded-2xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800/80 text-emerald-900 dark:text-emerald-200 text-xs flex items-center justify-between gap-3">
              <div className="flex items-center gap-2.5">
                <div className="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold shrink-0">
                  <Crown className="w-4 h-4" />
                </div>
                <div>
                  <div className="font-extrabold text-sm">{todayBadge.title[currentLanguage]}</div>
                  <div className="text-emerald-700 dark:text-emerald-400 font-medium">
                    {todayBadge.description[currentLanguage]}
                  </div>
                </div>
              </div>
              <span className="font-black text-emerald-600 dark:text-emerald-400 bg-emerald-100 dark:bg-emerald-900/60 px-2.5 py-1 rounded-lg shrink-0">
                +{todayBadge.xpAwarded} XP
              </span>
            </div>
          )}

        </div>

        {/* Right Action Column */}
        <div className="shrink-0 flex flex-col items-stretch sm:items-end justify-center gap-2">
          {isCompletedToday ? (
            <div className="flex flex-col items-center sm:items-end gap-1.5">
              <div className="px-5 py-3 rounded-2xl bg-emerald-100 dark:bg-emerald-950/50 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800 font-extrabold text-sm flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
                <span>{t.dailyCompleted}</span>
              </div>
              <span className="text-[11px] text-stone-500 dark:text-stone-400 font-mono">
                {t.nextChallengeIn} {timeLeft.formatted}
              </span>
            </div>
          ) : (
            <button
              id="start-daily-challenge-btn"
              onClick={onStartDailyChallenge}
              className="px-6 py-4 rounded-2xl bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-white font-black text-sm sm:text-base shadow-lg shadow-amber-600/25 flex items-center justify-center gap-2.5 transition-all hover:scale-[1.03] active:scale-[0.98] group"
            >
              <Zap className="w-5 h-5 fill-current text-amber-200 group-hover:scale-110 transition-transform" />
              <span>{t.playDailyChallenge}</span>
              {isRtl ? (
                <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
              ) : (
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              )}
            </button>
          )}
        </div>

      </div>

    </div>
  );
};
