import React from 'react';
import { Moon, Sun, Volume2, VolumeX, BarChart3, BookOpen, Sparkles, Home, Zap, Flame } from 'lucide-react';
import { Language, UserStats } from '../types';
import { TRANSLATIONS } from '../data/translations';

interface NavbarProps {
  currentLanguage: Language;
  onLanguageChange: (lang: Language) => void;
  isDarkMode: boolean;
  onToggleDarkMode: () => void;
  soundEnabled: boolean;
  onToggleSound: () => void;
  onOpenStats: () => void;
  onGoHome: () => void;
  onOpenLibrary: () => void;
  activeView: 'home' | 'quiz' | 'results' | 'library';
  userStats?: UserStats;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentLanguage,
  onLanguageChange,
  isDarkMode,
  onToggleDarkMode,
  soundEnabled,
  onToggleSound,
  onOpenStats,
  onGoHome,
  onOpenLibrary,
  activeView,
  userStats
}) => {
  const t = TRANSLATIONS[currentLanguage];

  return (
    <header className="sticky top-0 z-40 backdrop-blur-md bg-stone-50/90 dark:bg-stone-950/90 border-b border-stone-200/80 dark:border-stone-800 transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        
        {/* Brand Name "riwaq" */}
        <div className="flex items-center gap-3">
          <button
            onClick={onGoHome}
            className="flex items-center gap-2 group text-start focus:outline-none"
            aria-label="Riwaq Home"
          >
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-600 to-amber-500 text-white flex items-center justify-center shadow-md shadow-amber-600/20 group-hover:scale-105 transition-transform duration-200">
              <Sparkles className="w-5 h-5" />
            </div>
            <div className="flex flex-col">
              <span className="text-2xl font-black tracking-tight text-stone-900 dark:text-stone-100 font-serif">
                riwaq
              </span>
              <span className="text-[10px] uppercase font-bold tracking-widest text-amber-700 dark:text-amber-400 -mt-1">
                رِوَاقُ المعرفة
              </span>
            </div>
          </button>
        </div>

        {/* Center navigation shortcuts */}
        <div className="hidden md:flex items-center gap-1 bg-stone-100 dark:bg-stone-900 p-1 rounded-xl border border-stone-200/60 dark:border-stone-800">
          <button
            onClick={onGoHome}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeView === 'home'
                ? 'bg-white dark:bg-stone-800 text-stone-900 dark:text-stone-100 shadow-sm'
                : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
            }`}
          >
            <Home className="w-4 h-4" />
            <span>{t.backToHome}</span>
          </button>

          <button
            onClick={onOpenLibrary}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-medium transition-all ${
              activeView === 'library'
                ? 'bg-white dark:bg-stone-800 text-stone-900 dark:text-stone-100 shadow-sm'
                : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
            }`}
          >
            <BookOpen className="w-4 h-4" />
            <span>{t.browseLibrary}</span>
          </button>
        </div>

        {/* Right Actions: Quick Stats, Language Selector, Sound, Theme, Stats */}
        <div className="flex items-center gap-2 sm:gap-3">
          
          {/* Quick Streak/XP Chip */}
          {userStats && (userStats.totalXp > 0 || userStats.dailyStreak > 0) && (
            <button
              onClick={onOpenStats}
              className="hidden lg:flex items-center gap-2 px-2.5 py-1 rounded-xl bg-amber-500/10 dark:bg-amber-500/15 border border-amber-500/20 text-xs font-bold hover:bg-amber-500/20 transition-all"
              title={t.playerStats}
            >
              {userStats.dailyStreak > 0 && (
                <span className="flex items-center gap-1 text-orange-600 dark:text-orange-400">
                  <Flame className="w-3.5 h-3.5 fill-current" />
                  {userStats.dailyStreak}d
                </span>
              )}
              {userStats.totalXp > 0 && (
                <span className="flex items-center gap-1 text-amber-700 dark:text-amber-300">
                  <Zap className="w-3.5 h-3.5 fill-current text-amber-500" />
                  {userStats.totalXp.toLocaleString()}
                </span>
              )}
            </button>
          )}
          
          {/* Language Picker */}
          <div className="flex items-center bg-stone-100 dark:bg-stone-900 p-1 rounded-xl border border-stone-200/60 dark:border-stone-800">
            <button
              onClick={() => onLanguageChange('ar')}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                currentLanguage === 'ar'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
              }`}
              title="العربية"
            >
              العربية
            </button>
            <button
              onClick={() => onLanguageChange('en')}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                currentLanguage === 'en'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
              }`}
              title="English"
            >
              EN
            </button>
            <button
              onClick={() => onLanguageChange('fr')}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                currentLanguage === 'fr'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
              }`}
              title="Français"
            >
              FR
            </button>
          </div>

          {/* Sound Toggle */}
          <button
            onClick={onToggleSound}
            aria-label={soundEnabled ? t.soundOff : t.soundOn}
            className="p-2 rounded-xl text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800/80 transition-colors"
            title={soundEnabled ? t.soundOff : t.soundOn}
          >
            {soundEnabled ? <Volume2 className="w-5 h-5 text-amber-600 dark:text-amber-400" /> : <VolumeX className="w-5 h-5" />}
          </button>

          {/* Theme Toggle (Light / Dark) */}
          <button
            onClick={onToggleDarkMode}
            aria-label={isDarkMode ? t.lightMode : t.darkMode}
            className="p-2 rounded-xl text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800/80 transition-colors"
            title={isDarkMode ? t.lightMode : t.darkMode}
          >
            {isDarkMode ? (
              <Sun className="w-5 h-5 text-amber-400" />
            ) : (
              <Moon className="w-5 h-5 text-stone-700" />
            )}
          </button>

          {/* Stats Modal Trigger */}
          <button
            onClick={onOpenStats}
            aria-label={t.stats}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-stone-200/70 dark:bg-stone-800 text-stone-800 dark:text-stone-200 hover:bg-stone-300/70 dark:hover:bg-stone-700/80 text-xs font-semibold transition-colors"
          >
            <BarChart3 className="w-4 h-4 text-amber-600 dark:text-amber-400" />
            <span className="hidden sm:inline">{t.stats}</span>
          </button>

        </div>

      </div>
    </header>
  );
};
