import React from 'react';
import {
  Landmark,
  Globe2,
  Atom,
  BookOpenCheck,
  Sparkles,
  Trophy,
  Cpu,
  Trees,
  HeartPulse,
  Compass,
  HelpCircle,
  LucideProps
} from 'lucide-react';

interface CategoryIconProps extends LucideProps {
  name: string;
}

export const CategoryIcon: React.FC<CategoryIconProps> = ({ name, ...props }) => {
  switch (name) {
    case 'Landmark':
      return <Landmark {...props} />;
    case 'Globe2':
      return <Globe2 {...props} />;
    case 'Atom':
      return <Atom {...props} />;
    case 'BookOpenCheck':
      return <BookOpenCheck {...props} />;
    case 'Sparkles':
      return <Sparkles {...props} />;
    case 'Trophy':
      return <Trophy {...props} />;
    case 'Cpu':
      return <Cpu {...props} />;
    case 'Trees':
      return <Trees {...props} />;
    case 'HeartPulse':
      return <HeartPulse {...props} />;
    case 'Compass':
      return <Compass {...props} />;
    default:
      return <HelpCircle {...props} />;
  }
};
