# Offline-First PWA Integration with Kiwix-JS and ZIM Readers: A Complete Implementation Guide

## Executive Summary and Objectives

This guide describes how to integrate large educational content sets into an offline-first Progressive Web App (PWA) using Kiwix‑JS and compatible ZIM readers. It provides a pragmatic, end‑to‑end blueprint spanning packaging strategy, service worker design, caching and storage, content indexing and search, navigation and user experience, performance tuning for constrained devices, licensing and attribution, and content updates and maintenance. The objective is to enable PWAs that function reliably without connectivity, meet accessibility requirements, deliver fast search and navigation, honor licensing obligations, and support long‑term maintainability.

The intended audience includes frontend engineers, PWA developers, technical writers, content operations teams, and product managers. We assume a modern web stack (HTML5, ES modules, a service worker), baseline familiarity with web storage and browser caching primitives, and access to a curated content repository. Where relevant, we reference platform policies and licensing frameworks to anchor compliance decisions across educational content derived from government portals and open educational resources. For example, DIKSHA (Digital Infrastructure for Knowledge Sharing) content typically falls under Creative Commons Attribution 4.0 (CC BY 4.0), whereas many Wikimedia text revisions fall under Creative Commons Attribution–ShareAlike (CC BY‑SA 3.0 or 4.0) depending on revision date and project policy[^1][^2][^3][^4][^5].

To set the context for attribution across mixed sources, the figure below illustrates the attribution emphasis present in our content inventory for DIKSHA and Wikimedia content. This informs both packaging choices and runtime credits presentation.

![High-level attribution context derived from source inventory (local screenshot placeholder).](images/diksha_screenshot_placeholder.png)

The content inventory indicates three primary source families: government sources (e.g., Railway Recruitment Boards and ministry publications), DIKSHA OER (predominantly CC BY 4.0), and Wikimedia text/media (CC BY‑SA with revision‑specific application of 3.0 or 4.0). Practice materials from commercial portals are typically All Rights Reserved (ARR) and require explicit permission; they are excluded from redistribution unless rights are secured. This guide recommends building PWA packages for DIKSHA and government materials out of the box, with Wikimedia handled with share‑alike safeguards where adaptations are involved.

Success will be measured by:
- Completeness of offline coverage (all core content accessible without network).
- Search performance and relevance (fast full‑text and prefix search; good hit ranking).
- Stability under constrained storage and intermittent connectivity (graceful degradation).
- Compliance with licensing and attribution (visible credits; correct notices).
- Maintainability (reproducible builds, verifiable integrity, and safe update strategies).

![Illustrative audit summary to motivate offline-first priorities (local).](audit/comprehensive_audit_summary.png)

This audit snapshot (Figure above) underscores the breadth of subject coverage and the prevalence of CC BY 4.0 and CC BY‑SA content across our sources, thereby guiding the packaging scope, search index design, and credits presentation. It also reveals a subset of ARR content that must be gated or omitted pending rights clearance.

Information gaps and assumptions:
- Kiwix‑JS API surfaces and build variants evolve; verify exact integration points (e.g., init parameters and search APIs).
- Production ZIM packaging parameters (compression levels, index block sizes, metadata schema) should be tuned per corpus.
- Real‑world performance metrics (search latency, memory footprint, IndexedDB growth) require device‑level testing.
- Target device profiles (storage quotas, CPU/RAM, browser versions) must be characterized to finalize tuning.
- Corporate branding and localization (language, accessibility standards) are organization‑specific.
- Definitive redistribution permission is required for ARR practice sets from commercial portals.
- Source media licensing (particularly non‑text media on Commons) must be verified per file.
- Final build output path must be confirmed; this guide defaults to pwa-guide/PWA_INTEGRATION_GUIDE.md pending confirmation.

These gaps are enumerated to ensure follow‑through during implementation and do not block initial architecture and packaging decisions.

## Architectural Overview: Offline-First PWA with ZIM Readers

The recommended architecture is a client‑side PWA that embeds a ZIM reader (e.g., Kiwix‑JS) to access content packaged in ZIM files. ZIM is a read‑only, compressed container format optimized for offline knowledge repositories. Kiwix‑JS provides a JavaScript implementation capable of reading ZIM archives and performing client‑side search using embedded indices. Together, they enable fully offline consumption of large text‑centric educational content sets.

High‑level data flow:
1. Packaging: Source content (Markdown, HTML, PDFs) and metadata are compiled into a ZIM artifact with built‑in indices for full‑text search and optional suggestions.
2. Distribution: The ZIM file(s) are distributed as application assets, with integrity verification via checksums.
3. Runtime: A service worker precaches essential assets and caches the ZIM container. Kiwix‑JS loads and queries the embedded index to resolve requests for pages, images, and media.
4. UI Layer: The PWA exposes a standardized viewer, search bar, breadcrumbs, history, and a credits panel. Where appropriate, it overlays per‑page attribution and license notices.

Primary components:
- Service worker: Controls caching strategies for shell assets and ZIM; manages background fetch and integrity checks.
- Cache storage and IndexedDB: Store ZIM bytes, index shards, and auxiliary metadata. Quota management is critical for large corpora.
- ZIM reader module: Initializes the ZIM archive, resolves URLs, performs search queries, and renders results.
- Search index mapping: Maps queries to entry points, with filters and ranking logic tuned for exam preparation workflows.
- UI components: Search box, result list, article viewer, navigation breadcrumbs, and a credits page.

Storage strategy under constrained quotas:
- Partition content by subject and language (e.g., “Mathematics/Hindi,” “Geography/English”) to allow partial installs and on‑demand fetches.
- Use background fetch to complete downloads when on unmetered connections.
- Implement integrity checks and safe rollback to prior versions on failed updates.
- Consider dynamic eviction of least‑used index shards or image variants in low‑storage scenarios.

This architecture assumes clear licensing boundaries between open educational resources (DIKSHA/CC BY 4.0), government works, and CC BY‑SA content; it treats ARR content as non‑redistributable unless rights are explicitly secured[^2][^3][^4].

## ZIM Packaging Strategy for the Collected Corpus

A robust packaging strategy ensures that the offline reader can efficiently locate, load, and search content, while respecting licensing constraints and update operations.

Source categorization:
- Government sources (e.g., RRB notifications, previous papers, ministry publications): treat as official works with attribution to the issuing body; follow portal terms[^18][^19][^20][^21][^22][^23][^24].
- DIKSHA OER: predominantly CC BY 4.0; suitable for broad reuse and redistribution with attribution[^1][^2][^3][^4][^25].
- Wikimedia text/media: license varies by revision; CC BY‑SA 3.0 or 4.0 applies depending on date and project policy. Non‑text media require per‑file license verification[^5][^6][^7][^8].
- ARR practice sets: default to restricted; do not include without permissions.

Licensing‑aware packaging:
- Package CC BY‑SA content carefully, ensuring adaptations are marked and licensed under CC BY‑SA where applicable. Provide attribution blocks and license notices within the PWA.
- Clearly label per‑source licensing posture in package manifests; embed “About this package” credits content into the ZIM metadata for runtime display.
- Segregate ARR content or gate access based on user‑accepted terms and license checks; do not redistribute without rights.

Metadata and indexing:
- Ensure package metadata includes title, language, source, license, and checksum.
- Generate full‑text search indices and prefix/suggestion indices to accelerate queries.
- Adopt internal redirects (e.g., canonical article paths) to preserve navigation continuity across updates.

Update strategy:
- Use versioned ZIM files with semantic naming (e.g., corpus‑v1.2.0.zim) and checksums.
- Provide differential updates where feasible; otherwise ship full replacements for simplicity.
- Maintain a rollback path to the last known good package if integrity verification fails.

To illustrate how licensing constraints shape packaging decisions, the following matrix consolidates key obligations and the recommended actions.

### License Comparison Matrix

The table below synthesizes the practical obligations across the licenses most commonly encountered in our corpus, guiding packaging decisions and runtime attribution behavior.

| License | Attribution | Redistribution | Derivatives | Commercial Use | Notes |
|---|---|---|---|---|---|
| CC BY 4.0 | Required (TASL) | Allowed | Allowed | Allowed | Disclose changes; include license name and notice; no endorsement implied[^2][^26] |
| CC BY‑SA 3.0 | Required (Title required) | Allowed | Share‑alike required | Allowed | Include license copy/URI with distributions[^4] |
| CC BY‑SA 4.0 | Required (Title optional) | Allowed | Share‑alike required | Allowed | Transition applies to post‑June 2023 revisions[^5] |
| All Rights Reserved (ARR) | Owner controls | Requires permission | Requires permission | Requires permission | Personal use only common; no redistribution |
| Government Works | Attribute source | Typically allowed | Typically allowed | Typically allowed | Check portal terms for specifics[^20][^21] |

![File size distribution from local audits to inform packaging choices.](audit/file_size_distribution.png)

As the distribution indicates (Figure above), large PDFs and text‑heavy archives dominate our corpus. This informs partitioning by subject and language to reduce per‑package size and facilitate partial installs. It also argues for aggressive index tuning and image resizing to minimize storage overhead in the PWA.

### Sample ZIM Package Manifest (JSON)

The following sample illustrates the metadata fields a ZIM package should carry to support runtime licensing display, integrity checks, and package lifecycle management.

```json
{
  "packageId": "corpus-diksha-math-v1",
  "title": "DIKSHA Mathematics (CBSE VIII–X)",
  "language": ["en", "hi"],
  "source": "DIKSHA Platform",
  "license": "CC BY 4.0",
  "checksum": "sha256:950271c1e7e8ad9bf1feeef722b6da5b91b9724a24ddd9e0400fb9d6aec5d7f7",
  "createdAt": "2025-10-31T03:11:17Z",
  "version": "1.0.0",
  "credits": "Content sourced from DIKSHA, an initiative of NCERT, Ministry of Education, Government of India.",
  "notes": "Includes textbooks and teacher training materials.",
  "components": {
    "textIndex": true,
    "suggestIndex": true,
    "images": true,
    "metadataPage": true
  },
  "integrity": {
    "algo": "sha256",
    "value": "950271c1e7e8ad9bf1feeef722b6da5b91b9724a24ddd9e0400fb9d6aec5d7f7"
  }
}
```

#### Sample Package Composition

To illustrate how packaging choices reflect source characteristics and licensing posture, the table below maps representative categories to license signals and inclusion rules.

| Category | License | Inclusion Signals | Exclusion Signals |
|---|---|---|---|
| DIKSHA Textbooks | CC BY 4.0 | Attribution to NCERT/DIKSHA; CC BY notice | None |
| RRB Official PDFs | Government Work | Official RRB/ministry credit line; portal terms adherence | Non‑redistributable markings |
| Wikimedia Text | CC BY‑SA 3.0/4.0 | Attribution; SA notice; revision ID captured | Non‑free media without clear license |
| Practice Sets (Commercial) | ARR | Explicit permission obtained | No redistribution without rights |

## ZIM Package Loading in PWA

Loading ZIM packages within a PWA requires three coordinated steps: initialization, storage, and service worker strategy.

Initialization:
- Place ZIM files under a known assets path and load them via the reader module after the app shell is available.
- Initialize the reader with archive path/handle, preferred language, and optional flags for index loading.
- Verify package metadata (title, language, license) and display a credits panel entry on first run.

Storage and caching:
- Cache ZIM files using the Cache Storage API and store auxiliary metadata in IndexedDB (e.g., last opened page, bookmarks).
- For multi‑gigabyte corpora, use streaming reads and partial loads. Avoid parsing the entire archive upfront.
- Implement integrity verification using checksums (prefer SHA‑256) during both download and runtime startup.

Service worker strategy:
- Precache app shell assets and the smallest feasible “reader bootstrap” bundle.
- Cache‑first for ZIM reads; network‑first for metadata/version manifests when online.
- Provide offline fallback pages and guard against stale service workers via versioned cache names.

Error handling:
- If a ZIM fails integrity checks, prompt the user to re‑download or switch to the prior version.
- Surface licensing gating (e.g., show a credits overlay and a “License requires SA for derivatives” notice if the user requests adapted content derived from CC BY‑SA sources).

### Service Worker Caching Strategy (Pseudocode)

```js
const CACHE_SHELL = 'pwa-shell-v1';
const CACHE_ZIM = 'pwa-zim-v1';
const ZIM_ASSET = '/assets/corpus-diksha-math-v1.zim';

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_SHELL).then((cache) =>
      cache.addAll([
        '/', '/index.html', '/styles.css', '/app.js',
        '/reader/bootstrap.js' // minimal reader init
      ])
    )
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.filter(k => ![CACHE_SHELL, CACHE_ZIM].includes(k))
            .map(k => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // App shell: cache-first
  if (url.pathname.startsWith('/assets/') && !url.pathname.endsWith('.zim')) {
    event.respondWith(
      caches.match(event.request).then(resp => resp || fetch(event.request))
    );
    return;
  }

  // ZIM reads: cache-first with integrity hint (checksum stored in IndexedDB)
  if (url.pathname.endsWith('.zim')) {
    event.respondWith(
      caches.open(CACHE_ZIM).then(async (cache) => {
        const cached = await cache.match(event.request);
        if (cached) return cached;
        const response = await fetch(event.request);
        // Optionally verify sha256 of response before caching
        await cache.put(event.request, response.clone());
        return response;
      })
    );
    return;
  }

  // Default: network-first with offline fallback
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
```

### Recommended Initialized Settings for the Reader Module

The precise API surface of Kiwix‑JS evolves, and build variants differ. The settings below provide a conceptual baseline for initialization and should be adapted to the actual API of the chosen build.

```js
// reader/bootstrap.js (conceptual example; adapt to actual Kiwix‑JS API)
import { initReader } from '/reader/kiwix.js';

const zimArchiveURL = '/assets/corpus-diksha-math-v1.zim';
const langPrefs = navigator.language || 'en';

initReader({
  archive: zimArchiveURL,
  language: langPrefs,
  loadIndex: true,
  suggestions: true,
  showComments: true,
  creditsPage: '/credits.html'
}).then((api) => {
  window.kiwix = api;
  console.log('Reader initialized', api);
}).catch((err) => {
  console.error('Reader failed to initialize', err);
});
```

This pseudocode illustrates intent rather than exact method names. Confirm the specific init signature (archive path/handle, index loading toggles, language codes) against the chosen Kiwix‑JS build before integration.

![Developer tools view for inspecting service worker and caching behavior (local).](browser/screenshots/developer_tools_opened.png)

The figure above shows typical service worker caching behavior under the proposed strategy. Cache‑first for ZIM and shell assets ensures predictable offline behavior; integrity checks and versioning prevent silent corruption.

## Content Indexing and Search

Search is central to the user experience, particularly for exam preparation. ZIM packages should include indices for full‑text search, prefix/suggestion lookup, and synonyms where appropriate. The PWA should implement both quick search and advanced filters (subject, language, year, source), plus safeguards against large result sets.

Index mapping:
- Map terms to entry points (pages) and include ranking by frequency and article length.
- Expose filters for stage/class (e.g., CBSE VI–XII), subject, language, and year.
- Implement synonym handling for common exam synonyms (e.g., “railway” vs. “railways”; “polity” vs. “civics”).

UI behavior:
- Provide instant results with debounced input; degrade to “enter to search” if the device is under heavy load.
- Render result snippets from index metadata; include “open in article” and “copy link” actions.

Performance considerations:
- Limit result count and paginate; memoize frequent queries; prefetch likely next pages.
- For very large corpora, defer loading non‑essential index shards until a query triggers them.

### Index Configuration Example

```json
{
  "indexes": {
    "fullText": true,
    "suggest": true,
    "minQueryLength": 2,
    "maxResults": 100,
    "filters": [
      { "key": "subject", "type": "enum", "values": ["mathematics", "geography", "history", "polity", "economy", "science"] },
      { "key": "language", "type": "enum", "values": ["en", "hi"] },
      { "key": "stage", "type": "enum", "values": ["CBSE_VI-XII", "CBSE_VIII-X", "Competitive_Exam"] },
      { "key": "year", "type": "range", "min": 2015, "max": 2025 }
    ]
  },
  "ranking": {
    "titleWeight": 2.0,
    "headingWeight": 1.5,
    "bodyWeight": 1.0
  }
}
```

This configuration balances responsiveness with breadth. It includes filters aligned to our inventory taxonomy and ensures reasonable result limits for low‑end devices.

### Search UX and Result Display Template

![UI pattern for search results and article loading (local example).](browser/screenshots/biodiversity_wikipedia_page.png)

The pattern above emphasizes clear result lists with snippets, subject tags, and language indicators. The article viewer maintains breadcrumbs and offers quick access to credits for licensed content. In offline contexts, minimize DOM work and prefer lightweight markup to avoid jank on resource‑constrained hardware.

## Offline Navigation and User Experience

Navigation must be predictable, resilient, and discoverable without connectivity. The PWA should provide:
- A home screen with curated categories (subjects, languages, years) and recent items.
- Internal linking and anchors that respect the ZIM namespace; avoid external dependencies.
- Robust history and bookmarks stored locally; optional export to shareable links within the offline domain.
- An accessibility pass: keyboard navigability, ARIA landmarks, high contrast themes, and adequate touch targets.

![Article sectioning pattern to guide anchor navigation (local example).](browser/screenshots/article_middle_section.png)

### Navigation Components Map

| Component | Purpose | Offline Behavior |
|---|---|---|
| Home | Entry point to categories and recent items | Fully functional; backed by cached data |
| Category | Subject/language/year partitions | Works if respective ZIM partitions are cached |
| Article | Render content page | Core viewer works offline |
| Search | Full‑text and prefix search | Uses embedded indices; no network |
| History | Recently visited pages | Local storage; offline |
| Bookmarks | Saved pages | Local storage; export within offline domain |
| Credits | License and attribution display | Static page with dynamic overlays |

## Performance Optimization for Large Content Sets

Performance considerations dominate offline PWAs at scale. Key tactics include:
- Partitioning the corpus by subject and language to reduce initial download size and enable partial installs.
- Lazy loading index shards and images; prioritize above‑the‑fold content.
- Using streaming reads for large PDFs and image downscaling (thumbnail vs. full).
- Minimizing runtime memory by discarding decoded pages not in view and limiting concurrent fetches.
- Implementing preloading heuristics based on navigation patterns and user preferences.

![Performance diagnostics snapshot (local).](browser/screenshots/console_output.png)

### Optimization Techniques vs. Impact vs. Complexity

| Technique | Expected Impact | Complexity | Notes |
|---|---|---|---|
| Partitioning by subject/language | High | Medium | Enables partial installs and targeted updates |
| Lazy load index shards | High | Medium | Reduces upfront memory; minor latency on first queries |
| Image downscaling | Medium | Low | Store thumbnails; fetch full images on demand |
| Streaming reads for PDFs | Medium | Medium | Improves perceived performance; browser support varies |
| Prefetch likely next pages | Medium | Medium | Heuristic based on breadcrumbs and history |
| Memoization of frequent queries | Low | Low | Reduces redundant parsing; small memory cost |

These techniques should be combined and tuned via device‑level profiling. The most effective pairing for constrained devices is partitioning plus lazy index loading; both deliver outsized gains without heavy engineering complexity.

## Licensing and Attribution Display in PWA

Licensing compliance is non‑negotiable. The PWA should make attribution visible through a dedicated Credits page, per‑page overlays where appropriate, and consistent TASL (Title, Author, Source, License) presentation. Different source families require different handling:

- DIKSHA/NCERT content under CC BY 4.0: display attribution and CC BY notice; adaptations must disclose changes[^2][^3][^4][^25].
- Wikimedia text under CC BY‑SA: show attribution and SA notice; for adapted content, indicate share‑alike obligations and include license copy/URI[^4][^5][^6][^7][^26].
- Government works: attribute the issuing body and follow portal terms; include any specific credit lines from the document[^20][^21][^22].
- ARR practice sets: do not redistribute; if a user imports personal files, display an ARR notice and restrict sharing features[^12][^14][^15][^16][^17].

The Creative Commons recommended practices for attribution emphasize clarity, prominence, and completeness. TASL provides a practical structure to embed in both UI and documentation[^26].

![Wikimedia attribution anchor placeholder (local).](images/wikipedia_page_placeholder.png)

### Attribution Template Library

| Source Type | Fields | Example Text |
|---|---|---|
| DIKSHA (CC BY 4.0) | Title, Author, Source, License, Changes | “Title: Mathematics Textbook – Class X. Author: NCERT. Source: DIKSHA Platform. License: CC BY 4.0. Changes: None.” |
| Wikimedia (CC BY‑SA) | Title, Authors, Source (URL + revision), License, Changes | “Adapted from ‘India Contemporary World – 2’ (Wikibooks). Authors: Contributors. Source: page URL, revision ID. License: CC BY‑SA 4.0. Changes: Translation and summary.” |
| RRB Government | Title, Author/Source, Source URL, Changes | “Title: CEN 05/2025 JE (English). Author/Source: RRB Bhopal. Source: official portal page. License: Government work (used with attribution). Changes: None.” |
| ARR Practice Sets | Title, Platform, Source URL, License, Changes | “Title: RRB NTPC Practice Set. Author/Source: Mockers. Source: platform page. License: All Rights Reserved. Changes: None. Note: Personal use only; redistribution requires prior written consent.” |

![Credits entry example aligned to TASL (local screenshot placeholder).](images/diksha_screenshot_placeholder.png)

The credits UI should provide TASL fields for each source type, attach license notices, and include a summary of changes where applicable. For CC BY‑SA adaptations, explicitly state that the adapted portions are licensed under CC BY‑SA with copies or URIs included[^4][^5][^26].

### License Compliance Matrix (Display and Obligations)

| Source | Attribution Display | Notice | SA Obligations | Portal Terms |
|---|---|---|---|---|
| DIKSHA (CC BY 4.0) | Credits + per‑page overlay optional | CC BY 4.0 | N/A | Acknowledge DIKSHA/NCERT/MoE[^1][^2][^3] |
| Wikimedia Text | Credits + per‑article footer | CC BY‑SA 3.0/4.0 | Apply SA to adaptations | Follow project ToU[^6][^7] |
| Wikimedia Media | Per‑file TASL in credits | Per‑file license | SA applies if file is BY‑SA | Verify Commons license[^8] |
| RRB Government | Credits page with official credit line | N/A | N/A | Follow portal terms[^20][^21] |
| ARR Practice Sets | Personal‑use notice only | N/A | N/A | No redistribution[^12][^14][^15][^16][^17] |

## Content Updates and Maintenance

Long‑term maintainability requires predictable update workflows and integrity verification:

Update channels:
- Manifest‑driven updates (versioned ZIM packages) with a “check for updates” action in settings.
- Background fetch for ZIM downloads when on unmetered connections.
- Integrity verification via SHA‑256 checksums; safe rollback to prior packages if checks fail.

Operational procedures:
- Publish changelogs; track package lineage and merges when content is revised.
- Periodically audit content against the inventory taxonomy and source policies.
- Ensure redistribution rules and attribution placements are updated when source licenses or portal terms change.

### Release Update Workflow (Pseudocode)

```js
async function checkForUpdate() {
  const manifest = await fetch('/updates/manifest.json').catch(() => null);
  if (!manifest) return;

  const { latest, checksum } = await manifest.json();
  const current = window.currentPackageVersion;

  if (latest.version !== current.version) {
    const proceed = confirm(`Update available: ${current.version} → ${latest.version}`);
    if (!proceed) return;

    await downloadZIM(latest.url);
    const ok = await verifyIntegrity(latest.url, checksum);
    if (!ok) {
      alert('Integrity check failed. Rolling back.');
      await rollbackToPrevious();
      return;
    }

    await switchToNewPackage(latest);
    alert('Update completed.');
  }
}
```

This workflow relies on version and checksum fields embedded in package manifests and stored checksums in the inventory. It aligns with the integrity practices reflected in our audit and checksum tooling.

### Sample Release Notes Template

```
## v1.1.0 – 2025-11-15
- Added: Geography section, Hindi language pack
- Changed: Updated CC BY‑SA notices for Wikimedia text revised post‑June 2023
- Fixed: Search indexing for Mathematics chapters (CBSE VIII–X)
- Security: SHA‑256 checksums for all ZIM assets
```

### Update Channel Comparison

| Channel | Pros | Cons | When to Use |
|---|---|---|---|
| Manual | Predictable; user control | Slower adoption | Pilot releases; sensitive updates |
| Background Fetch | Seamless; user friendly | Requires quota; reliability | Minor updates; non‑critical content |
| Delta Packages | Efficient bandwidth | Complex merging; risk | Frequent small updates; high‑latency environments |

## Security, Privacy, and Platform Constraints

A privacy‑first PWA avoids collecting personal data; all content remains local. Platform constraints include storage quotas and the availability of Service Workers and Cache Storage on target browsers. Secure distribution relies on checksums and avoiding mixed content. ARR content must be gated or excluded to prevent accidental redistribution.

### Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Storage quota exceeded | Medium | High | Partition packages; lazy loading; user prompts | Engineering |
| Integrity failure | Low | High | SHA‑256 verification; rollback | Engineering |
| Licensing breach (ARR) | Medium | High | Permission workflow; gating; audits | Legal/Content Ops |
| Stale service worker | Low | Medium | Versioned cache; activate claim; testing | Engineering |
| Accessibility gaps | Medium | Medium | WCAG pass; user testing | QA/UX |
| Mixed content | Low | High | Enforce HTTPS; asset pinning | Engineering |

## QA and Rollout Plan

Quality assurance spans functional correctness, offline reliability, and compliance. The test plan should cover package loading, search accuracy, offline navigation, cache behavior, service worker lifecycle, credits correctness, and update flows. Test on a device matrix reflecting low‑end phones and variable connectivity.

![Illustrative QA dashboard from audits (local).](audit/comprehensive_dashboard.png)

### Test Matrix

| Feature | Test Cases | Metrics | Pass Criteria |
|---|---|---|---|
| ZIM Loading | Init with valid/invalid packages; integrity checks | Success rate; time‑to‑first‑page | 100% valid; clear errors for invalid |
| Search | Full‑text, prefix; filters; large result sets | Latency; relevance; stability | <300ms on target devices; accurate hits |
| Offline Nav | Home, categories, article anchors | Navigation success; broken links | 0 broken anchors; full offline coverage |
| Caching | Cache‑first for ZIM; shell precache | Hit ratio; eviction behavior | >95% cache hits; no data loss |
| Service Worker | Install/activate; fetch handlers; update flow | Lifecycle correctness | Clean updates; no stale cache |
| Credits | TASL per source; per‑page overlays | Completeness; visibility | All required fields present; visible |
| Updates | Background fetch; rollback | Success rate; rollback reliability | 100% integrity pass; safe rollback |

Rollout:
- Feature‑flagged activation of new packages; staged user groups.
- Logging limited to non‑personal metrics (e.g., cache hit ratio, update success rate).
- Feedback channel for users to report issues with attribution or access.

## Appendices: Configuration Samples and Snippets

This appendix consolidates practical samples referenced throughout the guide. Where exact Kiwix‑JS APIs are involved, adapt to the chosen build version.

### Kiwix‑JS Initialization Snippet (Conceptual)

```js
// Adapt to the specific Kiwix‑JS build used
import { createReader } from '/reader/kiwix-esm.js';

async function boot() {
  const archiveUrl = '/assets/corpus-diksha-math-v1.zim';
  const reader = await createReader({ archiveUrl, loadIndex: true, lang: 'en' });
  window.reader = reader;

  // Example search
  const results = await reader.search('polynomials', { maxResults: 20 });
  console.log(results);
}
boot();
```

### Service Worker Caching Strategies (Shell, ZIM, Manifest)

```js
const CACHE_APP = 'pwa-app-v2';
const CACHE_ZIM = 'pwa-zim-v2';

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // App shell: cache-first
  if (url.origin === location.origin && url.pathname.startsWith('/assets/') && !url.pathname.endsWith('.zim')) {
    event.respondWith(
      caches.open(CACHE_APP).then(cache =>
        cache.match(event.request).then(resp => resp || fetch(event.request))
      )
    );
  }

  // ZIM: cache-first with integrity
  if (url.pathname.endsWith('.zim')) {
    event.respondWith(
      caches.open(CACHE_ZIM).then(async (cache) => {
        const cached = await cache.match(event.request);
        if (cached) return cached;
        const response = await fetch(event.request);
        // TODO: Verify checksum before caching
        await cache.put(event.request, response.clone());
        return response;
      })
    );
  }
});
```

### Attribution Blocks and Credits Page Template

```html
<section id="credits" aria-labelledby="credits-heading">
  <h2 id="credits-heading">Credits and Licensing</h2>
  <article data-source="DIKSHA" data-license="CC BY 4.0">
    <h3>Mathematics Textbook – Class X</h3>
    <p><strong>Author:</strong> NCERT</p>
    <p><strong>Source:</strong> DIKSHA Platform</p>
    <p><strong>License:</strong> CC BY 4.0</p>
    <p><strong>Changes:</strong> None</p>
  </article>
  <article data-source="Wikimedia" data-license="CC BY-SA 4.0">
    <h3>Adapted: India Contemporary World – 2 (Wikibooks)</h3>
    <p><strong>Authors:</strong> Contributors</p>
    <p><strong>Source:</strong> page URL, revision ID</p>
    <p><strong>License:</strong> CC BY‑SA 4.0</p>
    <p><strong>Changes:</strong> Translation, summary</p>
    <p><em>Adaptations must be licensed under CC BY‑SA 4.0.</em></p>
  </article>
  <article data-source="RRB Government" data-license="Government Work">
    <h3>CEN 05/2025 JE (English)</h3>
    <p><strong>Author/Source:</strong> RRB Bhopal</p>
    <p><strong>Source:</strong> Official portal page</p>
    <p><strong>License:</strong> Government work (used with attribution)</p>
    <p><strong>Changes:</strong> None</p>
  </article>
</section>
```

### Example ZIM Manifest JSON Fields

| Field | Purpose | Example |
|---|---|---|
| packageId | Unique identifier | corpus-diksha-math-v1 |
| title | Package display title | DIKSHA Mathematics (CBSE VIII–X) |
| language | Languages included | ["en", "hi"] |
| source | Originating platform | DIKSHA Platform |
| license | License designation | CC BY 4.0 |
| checksum | Integrity verification | sha256:… |
| version | Semantic version | 1.0.0 |
| credits | Attribution summary | “Content sourced from DIKSHA…” |
| components | Index flags | { textIndex: true, suggestIndex: true } |

---

## References

[^1]: DIKSHA - Digital Infrastructure for Knowledge Sharing. https://diksha.gov.in/
[^2]: DIKSHA - Explore as Student. https://diksha.gov.in/exploreasstudent/
[^3]: DIKSHA - Get App. https://diksha.gov.in/getapp/
[^4]: Creative Commons: Legal Code — CC BY‑SA 3.0. https://creativecommons.org/licenses/by-sa/3.0/legalcode.en
[^5]: Creative Commons: Wikipedia moves to CC 4.0 licenses. https://creativecommons.org/2023/06/29/wikipedia-moves-to-cc-4-0-licenses/
[^6]: Wikimedia Foundation: Licensing Policy. https://foundation.wikimedia.org/wiki/Policy:Licensing_policy
[^7]: Wikimedia Foundation: Terms of Use. https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
[^8]: Wikimedia Commons: Licensing. https://commons.wikimedia.org/wiki/Commons:Licensing
[^9]: Wikipedia: Reusing Wikipedia content. https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content
[^10]: DIKSHA Platform Team, NCERT, Ministry of Education, Government of India (inventory attribution text).
[^11]: RRB NTPC CBT1 2020 Dec 28 Shift 1 (ExamCart PDF). https://portal-downloads/CBT1/2020/RRB_NTPC_CBT1_2020_Dec28_Shift1_ExamCart.pdf
[^12]: RRB NTPC CBT1 2024 June 06 Shift 2 (Prepp PDF). https://portal-downloads/CBT1/2024/RRB_NTPC_CBT1_2024_June06_Shift2_Prepp.pdf
[^13]: Jagran Josh: Terms of Use. https://www.jagranjosh.com/terms-of-use
[^14]: Unacademy: Terms and Conditions. https://unacademy.com/terms
[^15]: Oliveboard: Terms of Use. https://www.oliveboard.in/terms/
[^16]: Testbook: Terms of Service (India). https://testbook.com/terms-of-service
[^17]: Mockers: Privacy Policy. https://www.mockers.in/privacy-policy
[^18]: RRB Ranchi Official Website. https://www.rrbranchi.gov.in/
[^19]: RRB Bhagalpur: CEN 05/2025 JE (English) PDF. https://downloads/rrb-ntpc/previous-papers/CBT1/2025/cen__2025__CBT__je-dms-cma__en__rrbbhopal.gov.pdf
[^20]: South Central Railway: Terms & Conditions. https://scr.indianrailways.gov.in/view_section.jsp?lang=0&id=0,7,332
[^21]: National Education Policy 2020 (Government of India) - PDF. https://www.india.gov.in/sites/default/files/NEP_2020.pdf
[^22]: UNESCO: DIKSHA in India (PDF). https://media.unesco.org/sites/default/files/webform/gec002/diksha-in-india.pdf
[^23]: Creative Commons Wiki: Recommended practices for attribution. https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution
[^24]: Meta-Wiki: Legal/CC BY-SA licenses and social media. https://meta.wikimedia.org/wiki/Legal/CC_BY-SA_licenses_and_social_media
[^25]: DIKSHA Platform attribution baseline and CC BY 4.0 practices (source inventory)