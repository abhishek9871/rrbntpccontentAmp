/**
 * ZIM Package Builder Configuration
 * Configures content packaging for Kiwix/ZIM format
 */

const path = require('path');
const os = require('os');

// Input directories (based on our content structure)
const INPUT_DIRS = {
  // DIKSHA content
  diksha: {
    ga: path.join(__dirname, '../workspace/diksha-ga'),
    math: path.join(__dirname, '../workspace/diksha-math'),
    reasoning: path.join(__dirname, '../workspace/diksha-reasoning'),
    science: path.join(__dirname, '../workspace/diksha-science'),
    metadata: path.join(__dirname, '../workspace/diksha-ga/metadata')
  },
  
  // Practice materials
  practice: {
    ga: path.join(__dirname, '../workspace/practice-ga'),
    reasoning: path.join(__dirname, '../workspace/diksha-reasoning/downloaded_content'),
    metadata: path.join(__dirname, '../workspace/practice-ga/metadata')
  },
  
  // Government sources
  government: {
    currentAffairs: path.join(__dirname, '../workspace/current-affairs'),
    yearbooks: path.join(__dirname, '../workspace/current-affairs/yearbooks'),
    ministryPublications: path.join(__dirname, '../workspace/current-affairs/ministry-publications'),
    policyDocuments: path.join(__dirname, '../workspace/current-affairs/policy-documents'),
    economicSurveys: path.join(__dirname, '../workspace/current-affairs/economic-surveys')
  },
  
  // RRB materials
  rrb: {
    downloads: path.join(__dirname, '../workspace/downloads'),
    previousPapers: path.join(__dirname, '../workspace/portal-downloads'),
    studyMaterials: path.join(__dirname, '../workspace/rrb_study_materials'),
    mockTests: path.join(__dirname, '../workspace/rrb-mock-tests'),
    officialNotices: path.join(__dirname, '../workspace/rrb_official_notices'),
    metadata: path.join(__dirname, '../workspace/metadata')
  }
};

// ZIM package configuration
const ZIM_CONFIG = {
  // Compression settings
  compression: {
    level: 9, // Maximum compression
    algorithm: 'zstd', // Zstandard compression
    chunkSize: 64 * 1024, // 64KB chunks
    dictionarySize: 1024 * 1024 // 1MB dictionary
  },
  
  // Index configuration
  indexing: {
    enableFulltext: true,
    enableImages: true,
    enableMetadata: true,
    enableRedirects: true,
    enableXapian: true,
    minWordLength: 3,
    maxResults: 10000
  },
  
  // Metadata schema
  metadata: {
    title: "Railway Recruitment NTPC - Complete Study Guide",
    creator: "Content compiled from DIKSHA, RRB Official Sources, and Educational Materials",
    publisher: "MiniMax Educational Platform",
    date: new Date().toISOString(),
    language: ["en", "hi"],
    tags: [
      "railway",
      "recruitment",
      "ntpc",
      "competitive-exam",
      "education",
      "offline",
      "study-guide"
    ],
    description: "Comprehensive offline study guide for Railway Recruitment NTPC exam preparation with previous papers, practice sets, and study materials"
  },
  
  // Content organization
  organization: {
    sortMode: "title",
    groupBy: "category",
    enableBacklinks: true,
    enableFulltextSearch: true,
    enableSuggestions: true,
    maxTitleLength: 255,
    maxDescriptionLength: 1000
  },
  
  // Performance tuning
  performance: {
    enableCompression: true,
    cacheSize: 256 * 1024 * 1024, // 256MB cache
    maxCacheEntries: 10000,
    enableParallelProcessing: true,
    workerThreads: os.cpus().length
  }
};

// Package-specific configurations
const PACKAGES = {
  // Master package with everything
  master: {
    name: "rrb-ntpc-master",
    description: "Complete RRB NTPC study package",
    inputDirs: [
      INPUT_DIRS.diksha,
      INPUT_DIRS.practice,
      INPUT_DIRS.government,
      INPUT_DIRS.rrb
    ],
    size: "large",
    compression: "maximum"
  },
  
  // Core study materials (DIKSHA only)
  core: {
    name: "rrb-ntpc-core",
    description: "Core study materials from DIKSHA",
    inputDirs: [INPUT_DIRS.diksha],
    size: "medium",
    compression: "standard"
  },
  
  // Practice materials only
  practice: {
    name: "rrb-ntpc-practice",
    description: "Practice sets and mock tests",
    inputDirs: [INPUT_DIRS.practice],
    size: "small",
    compression: "standard"
  },
  
  // Previous papers and government documents
  official: {
    name: "rrb-ntpc-official",
    description: "Official RRB documents and previous papers",
    inputDirs: [INPUT_DIRS.rrb, INPUT_DIRS.government],
    size: "medium",
    compression: "high"
  }
};

// Content filtering rules
const FILTERS = {
  // Include patterns
  include: [
    // Text content
    "**/*.html",
    "**/*.htm",
    "**/*.txt",
    "**/*.md",
    "**/*.markdown",
    
    // Documents
    "**/*.pdf",
    
    // Images
    "**/*.jpg",
    "**/*.jpeg",
    "**/*.png",
    "**/*.gif",
    "**/*.webp",
    "**/*.svg",
    
    // Data files
    "**/*.json",
    "**/*.xml",
    
    // Archives (extract contents)
    "**/*.zip",
    "**/*.tar",
    "**/*.gz"
  ],
  
  // Exclude patterns
  exclude: [
    // System files
    "**/.DS_Store",
    "**/Thumbs.db",
    "**/desktop.ini",
    
    // Temporary files
    "**/*.tmp",
    "**/*.temp",
    "**/*.bak",
    "**/*.swp",
    
    // Log files
    "**/*.log",
    "**/logs/**",
    
    // Development files
    "**/*.map",
    "**/.git/**",
    
    // Large multimedia (unless specifically included)
    "**/*.mp4",
    "**/*.avi",
    "**/*.mkv",
    "**/*.mp3",
    "**/*.wav",
    
    // Corrupted or incomplete files
    "**/broken/**",
    "**/corrupt/**"
  ],
  
  // Size limits
  sizeLimits: {
    maxFileSize: 50 * 1024 * 1024, // 50MB per file
    minFileSize: 100, // 100 bytes minimum
    maxTotalSize: 5 * 1024 * 1024 * 1024 // 5GB total
  }
};

// Quality assurance rules
const QA_RULES = {
  // Content validation
  validateContent: true,
  checkEncoding: true,
  verifyIntegrity: true,
  testLinks: true,
  
  // Metadata validation
  validateMetadata: true,
  checkCompleteness: true,
  verifyLicensing: true,
  
  // Technical validation
  testCompression: true,
  benchmarkPerformance: true,
  checkAccessibility: true
};

// Build pipeline configuration
const PIPELINE = {
  // Pre-processing
  preprocess: {
    convertMarkdown: true,
    optimizeImages: true,
    minifyHTML: true,
    extractMetadata: true
  },
  
  // Main processing
  process: {
    indexContent: true,
    buildSearchIndex: true,
    generateSitemaps: true,
    createThumbnails: true
  },
  
  // Post-processing
  postprocess: {
    compressOutput: true,
    generateChecksums: true,
    createPackageInfo: true,
    testPackage: true
  }
};

// File type handlers
const FILE_HANDLERS = {
  // HTML/Markdown files
  'text/html': {
    processor: 'convertToHTML',
    options: {
      enableJS: false,
      enableCSS: true,
      optimizeImages: true
    }
  },
  'text/markdown': {
    processor: 'markdownToHTML',
    options: {
      enableTables: true,
      enableFootnotes: true,
      sanitize: true
    }
  },
  
  // PDF files
  'application/pdf': {
    processor: 'extractPDF',
    options: {
      extractText: true,
      generateThumbnails: true,
      preserveFormatting: true
    }
  },
  
  // Images
  'image/*': {
    processor: 'optimizeImage',
    options: {
      maxWidth: 1920,
      maxHeight: 1080,
      quality: 85,
      format: 'webp'
    }
  },
  
  // JSON data
  'application/json': {
    processor: 'indexJSON',
    options: {
      extractText: true,
      createSearchIndex: true
    }
  }
};

// Output configuration
const OUTPUT_CONFIG = {
  baseDir: path.join(__dirname, '../dist/zim-packages'),
  
  // Naming conventions
  naming: {
    separator: '-',
    includeDate: true,
    includeVersion: true,
    includeSize: true
  },
  
  // Compression levels
  compression: {
    minimum: {
      level: 1,
      speed: "fastest",
      description: "Fast build, larger files"
    },
    standard: {
      level: 6,
      speed: "balanced",
      description: "Good balance of speed and size"
    },
    maximum: {
      level: 9,
      speed: "slowest",
      description: "Smallest files, slow build"
    }
  }
};

module.exports = {
  INPUT_DIRS,
  ZIM_CONFIG,
  PACKAGES,
  FILTERS,
  QA_RULES,
  PIPELINE,
  FILE_HANDLERS,
  OUTPUT_CONFIG,
  
  // Helper functions
  getPackageConfig: (packageName) => {
    return PACKAGES[packageName] || PACKAGES.master;
  },
  
  getCompressionSettings: (level = 'standard') => {
    const settings = OUTPUT_CONFIG.compression[level] || OUTPUT_CONFIG.compression.standard;
    return {
      level: settings.level,
      algorithm: ZIM_CONFIG.compression.algorithm,
      chunkSize: ZIM_CONFIG.compression.chunkSize,
      dictionarySize: ZIM_CONFIG.compression.dictionarySize
    };
  },
  
  validateFilters: (filePath) => {
    // Check if file matches include patterns
    const matchesInclude = FILTERS.include.some(pattern => {
      const regex = new RegExp(pattern.replace(/\*\*/g, '.*').replace(/\*/g, '[^/]*'));
      return regex.test(filePath);
    });
    
    // Check if file matches exclude patterns
    const matchesExclude = FILTERS.exclude.some(pattern => {
      const regex = new RegExp(pattern.replace(/\*\*/g, '.*').replace(/\*/g, '[^/]*'));
      return regex.test(filePath);
    });
    
    return matchesInclude && !matchesExclude;
  }
};
