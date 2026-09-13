// Script to compile exactly 1,000 multilingual questions for Riwaq
import fs from 'fs';
import path from 'path';

export interface QuestionTranslation {
  question: string;
  options: [string, string, string, string];
  correctIndex: number;
  explanation: string;
}

export interface Question {
  id: number;
  categoryId: string;
  difficulty: 'easy' | 'medium' | 'hard';
  ar: QuestionTranslation;
  en: QuestionTranslation;
  fr: QuestionTranslation;
}

console.log("Compiling 1,000 questions across 10 categories in Arabic, English, French...");
