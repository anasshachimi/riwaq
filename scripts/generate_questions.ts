import fs from 'fs';
import path from 'path';

interface RawItem {
  q: { ar: string; en: string; fr: string };
  opts: { ar: [string, string, string, string]; en: [string, string, string, string]; fr: [string, string, string, string] };
  ans: number;
  exp: { ar: string; en: string; fr: string };
  diff: 'easy' | 'medium' | 'hard';
}

// We will define generators for each of the 10 categories, each providing 100 distinct questions.
// Total = 1000 questions.
