import { Category } from '../types';

export const CATEGORIES: Category[] = [
  {
    id: 'history',
    icon: 'Landmark',
    color: 'amber',
    title: {
      ar: 'التاريخ والحضارات',
      en: 'History & Civilizations',
      fr: 'Histoire et Civilisations'
    },
    description: {
      ar: 'أحداث تاريخية، شخصيات بارزة، إمبراطوريات ومعارك صنعت العالم',
      en: 'Historic events, influential figures, empires, and pivotal moments',
      fr: 'Événements historiques, figures marquantes, empires et moments charnières'
    }
  },
  {
    id: 'geography',
    icon: 'Globe2',
    color: 'emerald',
    title: {
      ar: 'الجغرافيا والدول',
      en: 'Geography & Nations',
      fr: 'Géographie et Pays'
    },
    description: {
      ar: 'عواصم، أنهار، تضاريس، أعلام ومعالم العالم الجغرافية',
      en: 'Capitals, rivers, terrains, flags, and world geographic landmarks',
      fr: 'Capitales, fleuves, reliefs, drapeaux et repères géographiques'
    }
  },
  {
    id: 'science',
    icon: 'Atom',
    color: 'cyan',
    title: {
      ar: 'العلوم والفيزياء',
      en: 'Science & Physics',
      fr: 'Sciences et Physique'
    },
    description: {
      ar: 'قوانين الكون، الفضاء الخارجي، الكيمياء، والظواهر الطبيعية',
      en: 'Cosmic laws, outer space, chemistry, and physical phenomena',
      fr: 'Lois de l\'univers, espace, chimie et phénomènes physiques'
    }
  },
  {
    id: 'literature',
    icon: 'BookOpenCheck',
    color: 'rose',
    title: {
      ar: 'الأدب والفنون',
      en: 'Literature & Arts',
      fr: 'Littérature et Arts'
    },
    description: {
      ar: 'روايات خالدة، شعراء كبار، لغات العالم، وفنون بصرية ومسرحية',
      en: 'Timeless novels, renowned poets, world languages, and arts',
      fr: 'Romans intemporels, grands poètes, langues du monde et beaux-arts'
    }
  },
  {
    id: 'heritage',
    icon: 'Sparkles',
    color: 'indigo',
    title: {
      ar: 'الحضارة والتراث',
      en: 'Heritage & Culture',
      fr: 'Patrimoine et Culture'
    },
    description: {
      ar: 'آثار إنسانية، عمارة أصيلة، تقاليد الشعوب وحكم الأولين',
      en: 'Monuments, architecture, cultural traditions, and ancient wisdom',
      fr: 'Monuments, architecture, traditions des peuples et sagesse ancienne'
    }
  },
  {
    id: 'sports',
    icon: 'Trophy',
    color: 'orange',
    title: {
      ar: 'الرياضة والألعاب',
      en: 'Sports & Athletics',
      fr: 'Sports et Jeux'
    },
    description: {
      ar: 'كؤوس العالم، الألعاب الأولمبية، أرقام قياسية ونجوم الرياضة',
      en: 'World Cups, Olympic games, records, and legendary champions',
      fr: 'Coupes du monde, Jeux olympiques, records et légendes du sport'
    }
  },
  {
    id: 'technology',
    icon: 'Cpu',
    color: 'blue',
    title: {
      ar: 'التقنية والذكاء الاصطناعي',
      en: 'Technology & AI',
      fr: 'Technologie et IA'
    },
    description: {
      ar: 'الحوسبة، لغات البرمجة، الابتكارات الرقمية، وثورة الذكاء الاصطناعي',
      en: 'Computing, coding languages, digital breakthroughs, and AI revolution',
      fr: 'Informatique, programmation, innovations numériques et révolution IA'
    }
  },
  {
    id: 'nature',
    icon: 'Trees',
    color: 'teal',
    title: {
      ar: 'الطبيعة والبيئة',
      en: 'Nature & Wildlife',
      fr: 'Nature et Faune'
    },
    description: {
      ar: 'عالم الحيوان، النباتات النادرة، المحيطات والأنظمة البيئية',
      en: 'Animal kingdom, rare plants, oceans, and living ecosystems',
      fr: 'Règne animal, flore rare, océans et écosystèmes vivants'
    }
  },
  {
    id: 'medicine',
    icon: 'HeartPulse',
    color: 'red',
    title: {
      ar: 'الصحة والطب',
      en: 'Medicine & Health',
      fr: 'Santé et Médecine'
    },
    description: {
      ar: 'جسم الإنسان، علم الأدوية، التغذية، والاكتشافات الطبية المنقذة للحياة',
      en: 'Human body, pharmacology, nutrition, and life-saving medical discoveries',
      fr: 'Corps humain, pharmacologie, nutrition et découvertes médicales'
    }
  },
  {
    id: 'general',
    icon: 'Compass',
    color: 'violet',
    title: {
      ar: 'معلومات عامة ومنوعات',
      en: 'General Trivia & Curiosities',
      fr: 'Culture Générale et Curiosités'
    },
    description: {
      ar: 'حقائق مدهشة، معلومات غير مألوفة، وأسئلة ذكاء وفضول معرفي',
      en: 'Surprising facts, mind-bending trivia, and intellectual curiosities',
      fr: 'Faits surprenants, énigmes, curiosités intellectuelles et savoirs variés'
    }
  }
];

export const CATEGORY_MAP = new Map(CATEGORIES.map(c => [c.id, c]));
