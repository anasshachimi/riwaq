export type Language = 'ar' | 'en' | 'fr';

export type Difficulty = 'easy' | 'medium' | 'hard';

export interface QuestionTranslation {
  question: string;
  options: [string, string, string, string];
  correctIndex: number; // 0, 1, 2, 3
  explanation: string;
}

export interface Question {
  id: number;
  categoryId: string;
  difficulty: Difficulty;
  ar: QuestionTranslation;
  en: QuestionTranslation;
  fr: QuestionTranslation;
}

export interface Category {
  id: string;
  icon: string;
  color: string;
  title: {
    ar: string;
    en: string;
    fr: string;
  };
  description: {
    ar: string;
    en: string;
    fr: string;
  };
}

export type GameMode = 'quick' | 'category' | 'marathon' | 'library' | 'daily';

export interface DailyBadge {
  id: string;
  date: string;
  title: {
    ar: string;
    en: string;
    fr: string;
  };
  description: {
    ar: string;
    en: string;
    fr: string;
  };
  icon: string;
  xpAwarded: number;
}

export interface QuizSettings {
  questionCount: number;
  timePerQuestion: number; // seconds, 0 = unlimited
  soundEnabled: boolean;
  hapticsEnabled: boolean;
}

export interface QuizState {
  questions: Question[];
  currentIndex: number;
  selectedOption: number | null;
  isAnswered: boolean;
  score: number;
  streak: number;
  bestStreak: number;
  lifelines: {
    fiftyFifty: boolean;
    skip: boolean;
    hint: boolean;
  };
  eliminatedOptions: number[];
  showExplanation: boolean;
  history: {
    questionId: number;
    userAnswer: number;
    isCorrect: boolean;
    timeSpent: number;
  }[];
  isComplete: boolean;
  startTime: number;
  timeRemaining: number;
  isDailyChallenge?: boolean;
  earnedXp?: number;
  awardedBadge?: DailyBadge | null;
}

export interface UserStats {
  totalAnswered: number;
  totalCorrect: number;
  totalQuizzesPlayed: number;
  highestScore: number;
  categoryStats: Record<string, { answered: number; correct: number }>;
  bookmarks: number[]; // question IDs
  mistakes: number[]; // question IDs
  totalXp: number;
  dailyStreak: number;
  lastDailyDate?: string;
  completedDailyDates: string[];
  badges: DailyBadge[];
}

