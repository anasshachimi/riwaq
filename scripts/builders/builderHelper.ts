export interface RawQ {
  arQ: string;
  enQ: string;
  frQ: string;
  arOpts: [string, string, string, string];
  enOpts: [string, string, string, string];
  frOpts: [string, string, string, string];
  ans: number;
  arExp: string;
  enExp: string;
  frExp: string;
  diff?: 'easy' | 'medium' | 'hard';
}

export function makeQuestions(
  categoryId: string,
  startId: number,
  items: RawQ[]
) {
  return items.map((item, idx) => ({
    id: startId + idx,
    categoryId,
    difficulty: item.diff || (idx % 3 === 0 ? 'easy' : idx % 3 === 1 ? 'medium' : 'hard'),
    ar: {
      question: item.arQ,
      options: item.arOpts,
      correctIndex: item.ans,
      explanation: item.arExp
    },
    en: {
      question: item.enQ,
      options: item.enOpts,
      correctIndex: item.ans,
      explanation: item.enExp
    },
    fr: {
      question: item.frQ,
      options: item.frOpts,
      correctIndex: item.ans,
      explanation: item.frExp
    }
  }));
}
