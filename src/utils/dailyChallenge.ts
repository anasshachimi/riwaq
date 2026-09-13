import { Question, DailyBadge } from '../types';
import { CATEGORIES } from '../data/categories';

/**
 * Returns local date string in format YYYY-MM-DD
 */
export function getTodayDateString(date: Date = new Date()): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * 32-bit integer string hasher
 */
function hashString(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash |= 0; // Convert to 32bit integer
  }
  return Math.abs(hash);
}

/**
 * Mulberry32 deterministic pseudo-random number generator
 */
function createPrng(seed: number) {
  let s = seed | 0;
  return function () {
    s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * Deterministically generates today's 10-question Daily Challenge.
 * Selects 1 question from each of the 10 categories, then shuffles them deterministically.
 */
export function getDailyQuestions(allQuestions: Question[], dateStr: string = getTodayDateString()): Question[] {
  const seed = hashString(`riwaq-daily-${dateStr}`);
  const prng = createPrng(seed);

  const selected: Question[] = [];

  // Group questions by category
  const categoryMap = new Map<string, Question[]>();
  for (const q of allQuestions) {
    const list = categoryMap.get(q.categoryId) || [];
    list.push(q);
    categoryMap.set(q.categoryId, list);
  }

  // Pick exactly 1 question from each of the 10 categories
  for (const cat of CATEGORIES) {
    const questionsInCat = categoryMap.get(cat.id);
    if (questionsInCat && questionsInCat.length > 0) {
      const idx = Math.floor(prng() * questionsInCat.length);
      selected.push(questionsInCat[idx]);
    }
  }

  // If for any reason fewer than 10 categories found, backfill deterministically
  if (selected.length < 10 && allQuestions.length >= 10) {
    const remaining = allQuestions.filter(q => !selected.some(s => s.id === q.id));
    while (selected.length < 10 && remaining.length > 0) {
      const idx = Math.floor(prng() * remaining.length);
      selected.push(remaining.splice(idx, 1)[0]);
    }
  }

  // Deterministic Fisher-Yates shuffle
  for (let i = selected.length - 1; i > 0; i--) {
    const j = Math.floor(prng() * (i + 1));
    const temp = selected[i];
    selected[i] = selected[j];
    selected[j] = temp;
  }

  return selected.slice(0, 10);
}

/**
 * Calculates time remaining until next midnight
 */
export function getTimeUntilMidnight(): { hours: number; minutes: number; seconds: number; formatted: string } {
  const now = new Date();
  const midnight = new Date(now);
  midnight.setHours(24, 0, 0, 0);

  const diffMs = Math.max(0, midnight.getTime() - now.getTime());
  const hours = Math.floor(diffMs / (1000 * 60 * 60));
  const minutes = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diffMs % (1000 * 60)) / 1000);

  const pad = (n: number) => String(n).padStart(2, '0');
  return {
    hours,
    minutes,
    seconds,
    formatted: `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`
  };
}

/**
 * Calculates Double XP for the Daily Challenge
 */
export function calculateDailyXp(correctCount: number, bestStreak: number): {
  baseXp: number;
  bonusXp: number;
  totalXp: number;
  isDouble: boolean;
} {
  // Base XP: 200 XP per correct question (Double the normal 100 XP)
  const baseXp = correctCount * 200;
  
  // Bonus XP for streak and perfect completion
  let bonusXp = bestStreak * 25;
  if (correctCount === 10) {
    bonusXp += 500; // Perfect score grand bonus
  } else if (correctCount >= 7) {
    bonusXp += 250;
  }

  return {
    baseXp,
    bonusXp,
    totalXp: baseXp + bonusXp,
    isDouble: true
  };
}

/**
 * Generates an exclusive badge for completing the daily challenge
 */
export function generateDailyBadge(
  dateStr: string,
  correctCount: number,
  streakDays: number
): DailyBadge {
  if (correctCount === 10) {
    return {
      id: `daily-flawless-${dateStr}`,
      date: dateStr,
      title: {
        ar: 'وسام الإتقان التام اليومي',
        en: 'Flawless Daily Scholar',
        fr: 'Grand Maître du Jour'
      },
      description: {
        ar: `أجبت على جميع أسئلة التحدي اليومي (10/10) بنجاح باهر في ${dateStr}`,
        en: `Achieved 100% accuracy in the Daily Challenge on ${dateStr}`,
        fr: `Score parfait de 10/10 au défi quotidien du ${dateStr}`
      },
      icon: 'Crown',
      xpAwarded: 500
    };
  }

  if (streakDays >= 7) {
    return {
      id: `daily-streak-7-${dateStr}`,
      date: dateStr,
      title: {
        ar: 'وسام الأسبوع الذهبي',
        en: '7-Day Champion Streak',
        fr: 'Insigne de la Semaine d\'Or'
      },
      description: {
        ar: `أكملت التحدي اليومي لـ 7 أيام متتالية!`,
        en: `Maintained a 7-day Daily Challenge streak!`,
        fr: `Série de 7 jours consécutifs au défi quotidien !`
      },
      icon: 'Flame',
      xpAwarded: 350
    };
  }

  if (correctCount >= 7) {
    return {
      id: `daily-luminary-${dateStr}`,
      date: dateStr,
      title: {
        ar: 'وسام المعرفة اليومية',
        en: 'Daily Luminary',
        fr: 'Érudit du Jour'
      },
      description: {
        ar: `حققت أكثر من 70% في التحدي اليومي لتاريخ ${dateStr}`,
        en: `Scored 70%+ in the Daily Challenge on ${dateStr}`,
        fr: `Score de 70%+ au défi quotidien du ${dateStr}`
      },
      icon: 'Award',
      xpAwarded: 250
    };
  }

  return {
    id: `daily-challenger-${dateStr}`,
    date: dateStr,
    title: {
      ar: 'وسام المشارك المثابر',
      en: 'Daily Challenger',
      fr: 'Participant Assidu'
    },
    description: {
      ar: `أتممت بنجاح التحدي اليومي لتاريخ ${dateStr}`,
      en: `Successfully completed the Daily Challenge on ${dateStr}`,
      fr: `Participation validée au défi quotidien du ${dateStr}`
    },
    icon: 'Sparkles',
    xpAwarded: 150
  };
}
