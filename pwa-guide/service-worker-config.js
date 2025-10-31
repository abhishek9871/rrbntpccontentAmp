/**
 * Service Worker Configuration for Offline Educational PWA
 * Implements advanced caching strategies for ZIM content and educational materials
 */

const CACHE_NAME = 'rrb-ntpc-v1.0.0';
const CACHE_VERSION = '1.0.0';

// ZIM packages cache configuration
const ZIM_CACHE_NAME = 'zim-packages-v1';
const ZIM_CACHE_VERSION = '1';

// Static assets cache configuration
const STATIC_CACHE_NAME = 'static-assets-v1';

// Content types and their cache strategies
const CACHE_STRATEGIES = {
  // ZIM files - Cache First strategy (never expire, largest files)
  'zim': {
    cacheName: ZIM_CACHE_NAME,
    strategy: 'cacheFirst',
    maxEntries: 5,
    maxAge: 'unlimited'
  },
  
  // Images - Cache First with compression
  'images': {
    cacheName: STATIC_CACHE_NAME,
    strategy: 'cacheFirst',
    maxEntries: 100,
    maxAge: '7 days'
  },
  
  // JSON data files - Network First
  'json': {
    cacheName: STATIC_CACHE_NAME,
    strategy: 'networkFirst',
    maxEntries: 50,
    maxAge: '1 day'
  },
  
  // CSS and JS files - Cache First
  'static': {
    cacheName: STATIC_CACHE_NAME,
    strategy: 'cacheFirst',
    maxEntries: 30,
    maxAge: '30 days'
  },
  
  // HTML pages - Network First with cache fallback
  'pages': {
    cacheName: STATIC_CACHE_NAME,
    strategy: 'networkFirst',
    maxEntries: 20,
    maxAge: '1 day'
  }
};

// File size thresholds for different strategies
const SIZE_THRESHOLDS = {
  small: 10 * 1024, // 10KB
  medium: 500 * 1024, // 500KB
  large: 5 * 1024 * 1024 // 5MB
};

// Storage quota management
const STORAGE_QUOTAS = {
  zimPackages: 500 * 1024 * 1024, // 500MB
  staticAssets: 100 * 1024 * 1024, // 100MB
  tempCache: 50 * 1024 * 1024 // 50MB
};

// Background sync configuration
const SYNC_CONFIG = {
  contentUpdate: {
    tag: 'content-update',
    options: {
      minInterval: 60 * 60 * 1000 // 1 hour
    }
  },
  healthCheck: {
    tag: 'health-check',
    options: {
      minInterval: 15 * 60 * 1000 // 15 minutes
    }
  }
};

// Cache cleanup policies
const CLEANUP_POLICIES = {
  lru: true,
  maxAge: {
    default: 7 * 24 * 60 * 60 * 1000, // 7 days
    zim: 'unlimited',
    static: 30 * 24 * 60 * 60 * 1000 // 30 days
  }
};

// Error handling configuration
const ERROR_CONFIG = {
  retries: {
    max: 3,
    backoff: 'exponential'
  },
  timeouts: {
    small: 5000, // 5 seconds
    medium: 10000, // 10 seconds
    large: 30000 // 30 seconds
  }
};

// Performance monitoring
const MONITORING_CONFIG = {
  enabled: true,
  metrics: {
    cacheHits: true,
    responseTimes: true,
    storageUsage: true,
    syncSuccess: true
  },
  reporting: {
    interval: 24 * 60 * 60 * 1000, // Daily
    endpoint: '/api/performance-metrics'
  }
};

// Debug configuration
const DEBUG_CONFIG = {
  enabled: process.env.NODE_ENV === 'development',
  logging: {
    cache: false,
    sync: false,
    errors: true,
    performance: false
  },
  devTools: {
    enabled: true,
    showCacheSize: true,
    showStorageUsage: true
  }
};

module.exports = {
  CACHE_NAME,
  CACHE_VERSION,
  CACHE_STRATEGIES,
  SIZE_THRESHOLDS,
  STORAGE_QUOTAS,
  SYNC_CONFIG,
  CLEANUP_POLICIES,
  ERROR_CONFIG,
  MONITORING_CONFIG,
  DEBUG_CONFIG,
  
  // Helper methods
  getCacheConfig: (url) => {
    const pathname = new URL(url).pathname.toLowerCase();
    
    if (pathname.endsWith('.zim') || pathname.includes('/zim/')) {
      return CACHE_STRATEGIES.zim;
    }
    
    if (pathname.match(/\.(png|jpg|jpeg|gif|webp|svg)$/)) {
      return CACHE_STRATEGIES.images;
    }
    
    if (pathname.match(/\.(json|js)$/)) {
      return pathname.endsWith('.json') ? CACHE_STRATEGIES.json : CACHE_STRATEGIES.static;
    }
    
    if (pathname.match(/\.(css)$/)) {
      return CACHE_STRATEGIES.static;
    }
    
    if (pathname.endsWith('.html') || pathname === '/') {
      return CACHE_STRATEGIES.pages;
    }
    
    return CACHE_STRATEGIES.static;
  },
  
  getTimeout: (url) => {
    const urlObj = new URL(url);
    const contentLength = parseInt(urlObj.headers.get('content-length')) || 0;
    
    if (contentLength < SIZE_THRESHOLDS.small) {
      return ERROR_CONFIG.timeouts.small;
    } else if (contentLength < SIZE_THRESHOLDS.medium) {
      return ERROR_CONFIG.timeouts.medium;
    } else {
      return ERROR_CONFIG.timeouts.large;
    }
  },
  
  shouldCache: (request, response) => {
    // Don't cache POST requests
    if (request.method !== 'GET') return false;
    
    // Don't cache error responses
    if (!response || response.status !== 200) return false;
    
    // Don't cache no-store responses
    if (response.headers.get('cache-control')?.includes('no-store')) return false;
    
    return true;
  },
  
  getStorageEstimate: () => {
    if ('storage' in navigator && 'estimate' in navigator.storage) {
      return navigator.storage.estimate();
    }
    return Promise.resolve({});
  }
};
