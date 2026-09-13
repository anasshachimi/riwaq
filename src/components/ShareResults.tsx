import React, { useState } from 'react';
import {
  Share2,
  Copy,
  Check,
  MessageCircle,
  Send,
  Sparkles,
  Trophy,
  Flame,
  Zap,
  Crown,
  Eye,
  EyeOff
} from 'lucide-react';
import { Language, QuizState } from '../types';
import { TRANSLATIONS } from '../data/translations';

interface ShareResultsProps {
  quizState: QuizState;
  currentLanguage: Language;
}

export const ShareResults: React.FC<ShareResultsProps> = ({
  quizState,
  currentLanguage
}) => {
  const t = TRANSLATIONS[currentLanguage];
  const [copied, setCopied] = useState(false);
  const [showPreview, setShowPreview] = useState(false);
  const [shareFeedback, setShareFeedback] = useState<string | null>(null);

  const total = quizState.history.length;
  const correctCount = quizState.history.filter(h => h.isCorrect).length;
  const accuracy = total > 0 ? Math.round((correctCount / total) * 100) : 0;

  // Build emoji grid (like Wordle / Trivia games, up to 10-15 icons per row)
  const emojiGrid = quizState.history
    .map(h => (h.isCorrect ? '🟩' : '🟥'))
    .join('');

  // Mode label
  const modeLabel = quizState.isDailyChallenge
    ? (currentLanguage === 'ar' ? '🌟 التحدي اليومي الموحد' : currentLanguage === 'fr' ? '🌟 Défi Quotidien' : '🌟 Daily Challenge')
    : (currentLanguage === 'ar' ? '🎯 تحدي المعرفة' : currentLanguage === 'fr' ? '🎯 Quiz du Savoir' : '🎯 Knowledge Quiz');

  const badgeTitle = quizState.awardedBadge
    ? quizState.awardedBadge.title[currentLanguage]
    : null;

  // Formatted share text
  const buildShareText = () => {
    const url = typeof window !== 'undefined' ? window.location.href : 'https://riwaq.app';
    
    if (currentLanguage === 'ar') {
      return [
        '🏛️ رِوَاق | riwaq',
        modeLabel,
        `🎯 النتيجة: ${quizState.score.toLocaleString()} نقطة`,
        `✅ الدقة: ${accuracy}% (${correctCount}/${total})`,
        `🔥 أطول سلسلة: ${quizState.bestStreak}`,
        quizState.earnedXp ? `⚡ نقاط الخبرة: +${quizState.earnedXp.toLocaleString()} XP` : '',
        badgeTitle ? `🏅 الوسام: ${badgeTitle}` : '',
        '',
        emojiGrid,
        '',
        'تحدّ ثقافتك ومعرفتك في موسوعة رِوَاق!',
        url
      ].filter(Boolean).join('\n');
    }

    if (currentLanguage === 'fr') {
      return [
        '🏛️ riwaq | Encyclopédie du Savoir',
        modeLabel,
        `🎯 Score : ${quizState.score.toLocaleString()} pts`,
        `✅ Précision : ${accuracy}% (${correctCount}/${total})`,
        `🔥 Série max : ${quizState.bestStreak}`,
        quizState.earnedXp ? `⚡ Expérience : +${quizState.earnedXp.toLocaleString()} XP` : '',
        badgeTitle ? `🏅 Insigne : ${badgeTitle}` : '',
        '',
        emojiGrid,
        '',
        'Testez votre culture générale sur riwaq !',
        url
      ].filter(Boolean).join('\n');
    }

    // Default English
    return [
      '🏛️ riwaq | Interactive Knowledge',
      modeLabel,
      `🎯 Score: ${quizState.score.toLocaleString()} pts`,
      `✅ Accuracy: ${accuracy}% (${correctCount}/${total})`,
      `🔥 Best Streak: ${quizState.bestStreak}`,
      quizState.earnedXp ? `⚡ Earned: +${quizState.earnedXp.toLocaleString()} XP` : '',
      badgeTitle ? `🏅 Badge: ${badgeTitle}` : '',
      '',
      emojiGrid,
      '',
      'Test your knowledge across 1,000 questions on riwaq!',
      url
    ].filter(Boolean).join('\n');
  };

  const shareText = buildShareText();
  const shareTitle = currentLanguage === 'ar' ? 'نتيجتي في رِوَاق (riwaq)' : currentLanguage === 'fr' ? 'Mon score sur riwaq' : 'My Score on riwaq';
  const appUrl = typeof window !== 'undefined' ? window.location.href : '';

  // Web Share API Handler
  const handleNativeShare = async () => {
    if (typeof navigator !== 'undefined' && navigator.share) {
      try {
        await navigator.share({
          title: shareTitle,
          text: shareText,
          url: appUrl
        });
        setShareFeedback(t.copied);
        setTimeout(() => setShareFeedback(null), 3000);
      } catch (error: any) {
        // Ignore user cancellation (AbortError)
        if (error?.name !== 'AbortError') {
          // Fallback to copy
          handleCopy();
        }
      }
    } else {
      // Fallback to copy if Web Share API is not supported
      handleCopy();
    }
  };

  // Copy to clipboard
  const handleCopy = async () => {
    try {
      if (navigator?.clipboard?.writeText) {
        await navigator.clipboard.writeText(shareText);
      } else {
        // Fallback for restricted contexts
        const textarea = document.createElement('textarea');
        textarea.value = shareText;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
      }
      setCopied(true);
      setShareFeedback(t.copied);
      setTimeout(() => {
        setCopied(false);
        setShareFeedback(null);
      }, 2500);
    } catch {
      setShareFeedback('Failed to copy');
      setTimeout(() => setShareFeedback(null), 2500);
    }
  };

  // Social Links
  const encodedText = encodeURIComponent(shareText);
  const encodedUrl = encodeURIComponent(appUrl);

  const socialLinks = [
    {
      name: 'WhatsApp',
      url: `https://api.whatsapp.com/send?text=${encodedText}`,
      bg: 'bg-emerald-600 hover:bg-emerald-500 text-white',
      icon: <MessageCircle className="w-4 h-4" />
    },
    {
      name: 'X (Twitter)',
      url: `https://twitter.com/intent/tweet?text=${encodeURIComponent(
        shareText.replace(appUrl, '').trim()
      )}&url=${encodedUrl}`,
      bg: 'bg-stone-900 hover:bg-stone-800 text-white dark:bg-white dark:text-stone-900 dark:hover:bg-stone-200',
      icon: (
        <span className="font-black text-xs">𝕏</span>
      )
    },
    {
      name: 'Telegram',
      url: `https://t.me/share/url?url=${encodedUrl}&text=${encodeURIComponent(
        shareText.replace(appUrl, '').trim()
      )}`,
      bg: 'bg-sky-500 hover:bg-sky-400 text-white',
      icon: <Send className="w-4 h-4" />
    },
    {
      name: 'Facebook',
      url: `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}&quote=${encodeURIComponent(
        shareText
      )}`,
      bg: 'bg-blue-600 hover:bg-blue-500 text-white',
      icon: <span className="font-black text-xs">f</span>
    },
    {
      name: 'LinkedIn',
      url: `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`,
      bg: 'bg-blue-700 hover:bg-blue-600 text-white',
      icon: <span className="font-black text-xs">in</span>
    }
  ];

  const hasNativeShare = typeof navigator !== 'undefined' && typeof navigator.share === 'function';

  return (
    <div className="bg-gradient-to-br from-amber-500/5 via-amber-500/10 to-amber-500/5 dark:from-amber-950/20 dark:via-stone-900 dark:to-amber-950/20 rounded-3xl p-5 sm:p-6 border border-amber-500/20 dark:border-amber-500/30 shadow-sm space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between gap-2 flex-wrap">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-xl bg-amber-500 text-white flex items-center justify-center shadow-sm">
            <Share2 className="w-4 h-4" />
          </div>
          <div>
            <h3 className="font-extrabold text-sm sm:text-base text-stone-900 dark:text-stone-100">
              {t.shareResults}
            </h3>
            <p className="text-xs text-stone-500 dark:text-stone-400">
              {t.shareSubtitle}
            </p>
          </div>
        </div>

        {/* Toggle scorecard preview */}
        <button
          onClick={() => setShowPreview(!showPreview)}
          className="text-xs font-semibold text-stone-600 dark:text-stone-400 hover:text-amber-600 dark:hover:text-amber-400 flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-stone-100 dark:bg-stone-800 transition-colors"
          title="Preview Scorecard"
        >
          {showPreview ? <EyeOff className="w-3.5 h-3.5" /> : <Eye className="w-3.5 h-3.5" />}
          <span>{showPreview ? (currentLanguage === 'ar' ? 'إخفاء البطاقة' : currentLanguage === 'fr' ? 'Masquer' : 'Hide Card') : (currentLanguage === 'ar' ? 'معاينة البطاقة' : currentLanguage === 'fr' ? 'Aperçu' : 'Preview Card')}</span>
        </button>
      </div>

      {/* Main Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-2.5">
        {/* Web Share API Button */}
        <button
          onClick={handleNativeShare}
          className="flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-white font-bold text-xs sm:text-sm shadow-md shadow-amber-500/20 flex items-center justify-center gap-2 transition-all hover:scale-[1.02] active:scale-[0.98]"
        >
          <Share2 className="w-4 h-4" />
          <span>
            {hasNativeShare
              ? (currentLanguage === 'ar' ? 'مشاركة عبر النظام أو التطبيقات' : currentLanguage === 'fr' ? 'Partager via l\'appareil' : 'Share via Device / Apps')
              : t.shareResults}
          </span>
        </button>

        {/* Copy Result Card to Clipboard */}
        <button
          onClick={handleCopy}
          className={`py-3 px-4 rounded-xl font-bold text-xs sm:text-sm transition-all flex items-center justify-center gap-2 border ${
            copied
              ? 'bg-emerald-600 text-white border-emerald-600'
              : 'bg-white dark:bg-stone-900 hover:bg-stone-100 dark:hover:bg-stone-800 text-stone-800 dark:text-stone-200 border-stone-200 dark:border-stone-800'
          }`}
        >
          {copied ? <Check className="w-4 h-4 text-white" /> : <Copy className="w-4 h-4 text-amber-600" />}
          <span>{copied ? t.copied : t.copyResult}</span>
        </button>
      </div>

      {/* Direct Social Media Platform Buttons */}
      <div className="pt-2 border-t border-amber-500/10 dark:border-amber-500/20">
        <div className="text-[11px] font-bold text-stone-500 dark:text-stone-400 uppercase tracking-wider mb-2">
          {t.shareOnSocial}
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {socialLinks.map(platform => (
            <a
              key={platform.name}
              href={platform.url}
              target="_blank"
              rel="noopener noreferrer"
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold transition-transform hover:scale-105 active:scale-95 shadow-sm ${platform.bg}`}
              title={`Share on ${platform.name}`}
            >
              {platform.icon}
              <span>{platform.name}</span>
            </a>
          ))}
        </div>
      </div>

      {/* Sharecard Preview */}
      {showPreview && (
        <div className="p-4 rounded-2xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 shadow-inner space-y-2 animate-fade-in text-start">
          <div className="flex items-center justify-between text-xs text-stone-400 border-b border-stone-100 dark:border-stone-800 pb-2">
            <span className="font-bold">{t.shareScoreTitle}</span>
            <span>{quizState.isDailyChallenge ? '🌟 Daily' : '🎯 Standard'}</span>
          </div>
          <pre className="font-mono text-xs text-stone-800 dark:text-stone-200 whitespace-pre-wrap leading-relaxed select-all">
            {shareText}
          </pre>
        </div>
      )}

      {/* Feedback Notification */}
      {shareFeedback && !copied && (
        <div className="text-center text-xs font-bold text-emerald-600 dark:text-emerald-400 animate-fade-in">
          {shareFeedback}
        </div>
      )}
    </div>
  );
};
