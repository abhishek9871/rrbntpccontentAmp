# General Awareness Practice Sets and Quiz Materials for RRB NTPC: Source Scan, Licensing Compliance, and Topic-wise Organization Plan

## Executive Summary and Objectives

This blueprint sets out a practical, compliance-first plan to collect, organize, and maintain General Awareness (GA) practice sets and quiz materials for the Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) examination. The immediate objective is to deliver a complete, topic-wise bank aligned to official General Awareness scope—including Indian History, Geography, Polity, Economy, Current Affairs, Static General Knowledge (GK), and Science & Technology—augmented by clear redistribution permissions and bilingual coverage (English/Hindi) wherever available.

The plan is designed around five outcomes:

1) Comprehensive coverage: Build topic-wise practice banks that collectively exhaust the NTPC GA syllabus and mirror likely exam weightages.  
2) Licensing compliance: Pre-screen portals for redistribution policy clarity; default to internal curation from compliant pages and avoid bulk downloads from policy-opaque sources.  
3) Bilingual availability: Prioritize sources that offer both English and Hindi materials and maintain parallel file structures.  
4) Organized structure: Implement a machine-parseable directory layout and metadata schema to support audits, updates, and reproducibility.  
5) Syllabus alignment: Map collected items to CBT 1 vs CBT 2 applicability using an internal taxonomy that consolidates official syllabi and widely used portals.

Governance anchors on two pillars. First, we align our taxonomy and stage mapping to an official-syllabus-aligned BYJU’S-hosted PDF that enumerates GA components such as current events, history, geography, polity, economy, general science and life science (up to 10th CBSE), computers, and abbreviations.[^2] Second, we verify exam structure parameters and shortlisting notes through national education portals.[^3][^4]

Deliverables include:  
- Topic-wise practice banks under the designated collection directory, maintained in parallel English/Hindi subfolders where available.  
- A metadata schema capturing source, licensing, language, topic tags, CBT applicability, and download procedures.  
- Licensing documentation that records allowed uses, required attribution, and any redistribution constraints per source.

Information gaps to address during execution include: explicit redistribution terms for certain portals; confirmation of bilingual availability for each item; and automated retrieval feasibility from sources with anti-bot protections. These are documented with mitigations later in the blueprint.

## RRB NTPC General Awareness: Syllabus and Exam Context

General Awareness is a high-weightage section in both computer-based tests (CBTs). An official-syllabus-aligned document presents GA as a broad umbrella that explicitly includes General Science and Life Science (up to 10th CBSE), current events (national and international), history and freedom struggle, geography (physical, social, and economic of India and the world), polity and governance, economy, computers and common abbreviations, UN and other world organizations, environmental issues, transport systems, famous personalities, and government programmes.[^2] Multiple portals corroborate the same scope and emphasize Static GK and Current Affairs as recurring drivers of GA questions.[^5][^6][^9]

To orient the content plan, we summarize the stage-wise section structure and weightage below and then map GA subtopics to CBT 1 vs CBT 2 applicability.

As a brief orientation, CBT 1 typically features 40 GA questions out of 100 total, while CBT 2 features 50 GA questions out of 120 total, with Mathematics and Reasoning completing the balance.[^3][^4] Both stages carry negative marking at 1/3 per wrong answer, and CBT 2 shortlists are often run at around 20 times the vacancy based on normalized CBT 1 merit.[^2][^3][^4] GA breadth and contextual depth expand in CBT 2, but the underlying topic family remains consistent with official syllabus.

Table 1. GA section overview by stage (CBT 1 vs CBT 2)

| Stage | GA Questions | Total Questions | Key Implications for Content Design |
|-------|--------------|-----------------|------------------------------------|
| CBT 1 | 40           | 100             | Emphasis on fundamentals, Static GK essentials, and recent national/international current affairs; broad factual recall. |
| CBT 2 | 50           | 120             | Greater depth within History, Geography, Polity, Economy; applied GA linking to schemes, organizations, and computers; Current Affairs remain pivotal. |

Sources: Exam pattern corroboration across national portals.[^3][^4]

Table 2. GA topic families mapped to CBT 1 and CBT 2

| Topic Family                   | CBT 1 Applicability | CBT 2 Applicability | Notes |
|--------------------------------|---------------------|---------------------|-------|
| Current Affairs (National/International) | Yes                 | Yes                 | Recency-weighted; 6–12-month window relevant to exam cycle.[^6] |
| Static GK (General Knowledge)  | Yes                 | Yes                 | High-yield facts across awards, important days, personalities, and organizations.[^9] |
| History (Ancient/Medieval/Modern; Freedom Struggle) | Yes                 | Yes (expanded)      | CBT 2 delves deeper into dynasties, battles, and reformers.[^2][^5] |
| Geography (India & World)      | Yes                 | Yes (expanded)      | Physical, social, economic geography with maps and data interpretation in CBT 2.[^2][^5] |
| Polity & Governance            | Yes                 | Yes (expanded)      | Constitution, Articles, Parliament, emergency provisions, and local governance.[^2] |
| Economy                        | Yes                 | Yes                 | Banking, budget, indicators, and basic economic concepts.[^2][^5] |
| Science & Technology           | Yes                 | Yes                 | General science and life science (up to 10th CBSE), Indian space and nuclear programmes, computers.[^2] |
| Computers & Abbreviations      | Yes                 | Yes                 | Basics of computers and common abbreviations feature in GA.[^2] |
| Organizations & UN             | Yes                 | Yes                 | UN and other world organizations; government and public sector organizations.[^2] |
| Environment & Biodiversity     | Yes                 | Yes                 | Environmental issues, flora and fauna.[^2] |
| Art, Culture, Literature, Monuments | Yes              | Yes                 | Indian culture and heritage; monuments and places.[^2] |
| Transport Systems              | Yes                 | Yes                 | Indian transport systems and related infrastructure.[^2] |
| Personalities                  | Yes                 | Yes                 | Famous personalities of India and the world.[^2] |
| Government Schemes             | Yes                 | Yes                 | Flagship programmes and policy updates.[^2] |

This mapping provides the backbone for organizing the practice banks and tagging the metadata.

## Credible Portals Overview and Policy Review

We prioritize portals with demonstrable NTPC coverage, either explicit subject pages or GA-focused practice content, and whose terms of use permit at least personal study and, preferably, educational redistribution with attribution. Bilingual availability further strengthens a source’s inclusion.

Four source types emerge:

- Topic-specific practice pages with free PDFs on signup (e.g., History, Polity, Geography, Science) and an overarching GK page.[^12][^13][^14][^15]  
- Aggregated free PDFs (Current Affairs, Static GK one-liners, sample papers) in English and Hindi, albeit with some items hosted via third-party checkout pages (e.g., Instamojo) that may introduce friction or constraints.[^16][^18][^19][^20][^21][^22][^23][^24]  
- A free bilingual platform offering daily and topic-wise quizzes, notes, and mock tests.[^25]  
- Curated “top questions” lists and weightage guidance to calibrate topic emphasis in the bank.[^6][^9]

Key licensing signals to respect include: “All rights reserved” (no redistribution), “Personal use only” (no commercial redistribution or derivative works), and free access claims without explicit redistribution permissions. In case of ambiguity, we limit to internal use with attribution and avoid bulk hosting of third-party PDFs.

Table 3. Licensing and redistribution policy matrix (selected portals)

| Portal | Stated Policy | Allowed Uses | Redistribution | Bilingual | Notes |
|--------|---------------|--------------|----------------|-----------|-------|
| Testbook | Copyright; free PDF on signup[^12][^13][^14][^15] | Personal study | Not permitted without permission | Yes (English/Hindi) | Topic pages for History, Polity, Geography, GK |
| Jagran Josh | Personal use only[^5][^8][^9] | Personal study | No commercial redistribution | Mixed | Strong Static GK topic lists and mock tests |
| RRB Exam Portal | Copyright notice; many “free” PDFs via checkout[^16][^18][^19][^20][^21][^22][^23][^24] | Personal study | No explicit redistribution; hosting charges may apply | English and Hindi pages | Detailed GA PDFs; some require manual navigation |
| Railway Capsule | Free access; no explicit redistribution clause[^25] | Personal study | Not specified; seek permission | Yes | Daily quizzes, topic notes, mocks |
| PracticeMock | Free Current Affairs PDF (access via platform)[^7][^11] | Personal study | Not specified; attribution advisable | English | Curated one-liner current affairs |
| Oliveboard | Free blog content; registration for full access[^6] | Personal study | Not specified | English/Hindi | Weightage guidance and “top 500 GK” |
| SSC Study | Free RRB study materials in English/Hindi[^10] | Personal study | Not specified | English/Hindi | Aggregation of publishers’ resources |
| Physics Wallah | Syllabus pages; GA topic lists[^26] | Personal study | Not specified | English | Topic structure alignment |

In practice, we will use three primary access modes: direct download where allowed, gated PDFs on signup with internal storage for authorized users, and manual curation of question items from compliant pages when automated downloads are blocked or terms are restrictive.

## Topic-wise Collection Plan: Source Mapping and Bilingual Strategy

The collection plan balances subject depth with licensing prudence. For each topic, we specify candidate sources, material types, language availability, and acquisition method, then outline how items will be tagged in metadata for CBT 1/CBT 2 relevance.

Table 4. Source-to-topic mapping and acquisition plan

| Topic | Primary Sources | Material Type | Language | Acquisition Method | Notes |
|-------|------------------|---------------|----------|--------------------|-------|
| Indian History | Testbook History[^13]; Jagran Josh Static GK pages[^9]; Oliveboard GK[^6] | Practice MCQs, solved PDFs, curated lists | English; Hindi via some portals | Signup-gated PDFs (Testbook); manual curation from articles | Emphasis on Ancient/Medieval/Modern and Freedom Struggle |
| Geography | Testbook Geography[^14]; Jagran Josh Static GK[^9] | Practice MCQs, solved PDFs | English; Hindi via portals | Signup-gated PDFs; manual curation | Include India & World physical/social/economic components |
| Polity | Testbook Polity[^15]; Jagran Josh Static GK[^9] | Practice MCQs, solved PDFs | English; Hindi via portals | Signup-gated PDFs; manual curation | Constitution, Articles, Parliament, emergency provisions |
| Economy | Jagran Josh Static GK[^9]; Oliveboard GK[^6] | MCQs, curated lists | English; Hindi via portals | Manual curation; avoid bulk downloads | Banking, budget, indicators |
| Current Affairs | PracticeMock PDF[^7][^11]; RRB Exam Portal CA PDF[^18]; Oliveboard current affairs[^6] | One-liner PDFs, monthly compilations | English; Hindi via some portals | Direct download where allowed; manual curation | Recency focus (last 6–12 months) |
| Static GK | RRB Exam Portal one-liners[^19]; Jagran Josh Static GK[^9]; Oliveboard GK[^6] | One-liner banks, MCQs | English; Hindi via portals | Direct download where allowed; manual curation | Awards, important days, personalities, organizations |
| Science & Technology | Testbook GK Science items[^12]; Jagran Josh Static GK[^9] | MCQs, solved sets | English; Hindi via portals | Signup-gated PDFs; manual curation | General science (up to 10th CBSE), Indian space/nuclear programmes |

This plan leans on Testbook for solved, topic-specific practice pages where redistribution terms are strict and therefore content is consumed internally (e.g., for metadata tagging and answer explanation styles), while relying on RRB Exam Portal for public GA compilations where access is frictionless enough to capture via manual, item-level curation in compliance with displayed terms. Railway Capsule provides a free bilingual practice feed to diversify item formats and test difficulty over time.[^25] Jagran Josh and Oliveboard offer strategic lists and weightage guidance to prioritize which subtopics to deepen first.[^6][^9]

Table 5. Language availability by topic and source (indicative)

| Topic | English | Hindi | Comments |
|-------|---------|-------|----------|
| History | Yes | Yes (via portals) | Testbook EN; Hindi pages exist on some portals |
| Geography | Yes | Yes (via portals) | Similar pattern to History |
| Polity | Yes | Yes (via portals) | |
| Economy | Yes | Yes (via portals) | |
| Current Affairs | Yes | Partial | PracticeMock EN; RRB Exam Portal CA available in EN; Hindi CA via some pages |
| Static GK | Yes | Yes | One-liners and lists widely available |
| Science & Technology | Yes | Yes (via portals) | |

For each acquired item, the metadata will capture: source, title, language, topic tags aligned to Table 2, CBT 1/CBT 2 applicability, question count, answer key availability, license status, access method, and a note on redistribution. The system will default to internal use for sources that prohibit redistribution and will clearly tag permitted uses to avoid ambiguity.

## Redistribution and Licensing Compliance Plan

Given varied and sometimes ambiguous terms, we will adhere to a conservative compliance posture:

- Respect “All rights reserved” and “No unauthorized redistribution” notices (e.g., Testbook). In such cases, we will not republish PDFs and will instead use metadata referencing and internal curation guidelines.[^12][^13][^14][^15]  
- Honor “Personal use only” restrictions (e.g., Jagran Josh). We will avoid hosting third-party PDFs and will curate question stems and topics internally with attribution, where permitted.[^5][^8][^9]  
- Treat “Free access” claims without explicit redistribution clauses (e.g., Railway Capsule, SSC Study) as permission-required for bulk redistribution. We will seek explicit permission for any external sharing and otherwise restrict to internal use with attribution.[^25][^10]  
- For RRB Exam Portal items that route through Instamojo or similar checkout pages, we will download only those clearly marked as free and limited to personal use, preserving attribution and recording any access constraints in metadata.[^16][^18][^19][^20][^21][^22][^23][^24]

Attribution will be standardized: portal name, article or PDF title, and a link to the source page. Where a download requires signup or a platform flow (e.g., PracticeMock), the metadata will record the access method so audits can verify compliance later.[^7][^11]

Table 6. Allowed uses and restrictions matrix (selected portals)

| Portal | Personal Use | Attribution Required | Redistribution | Notes |
|--------|--------------|----------------------|----------------|-------|
| Testbook | Yes | Yes | Not permitted | Use topic pages for internal curation; do not republish PDFs[^12][^13][^14][^15] |
| Jagran Josh | Yes | Yes | Not permitted | Strong Static GK topic lists; avoid bulk PDF hosting[^5][^8][^9] |
| RRB Exam Portal | Yes | Yes | Not explicit; likely restricted | Many free PDFs require manual steps; record access path[^16][^18][^19][^20][^21][^22][^23][^24] |
| Railway Capsule | Yes | Yes | Not specified | Free bilingual platform; seek permission for redistribution[^25] |
| PracticeMock | Yes | Yes | Not specified | Free Current Affairs PDF via platform flow[^7][^11] |
| Oliveboard | Yes | Yes | Not specified | GK blogs and lists; check terms[^6] |
| SSC Study | Yes | Yes | Not specified | Aggregated materials; confirm source rights[^10] |

The compliance team will retain a change log of terms and will re-validate permissions quarterly, especially before any external sharing beyond internal use.

## Directory Structure and Naming Conventions

We will maintain a bilingual, topic-wise structure that mirrors the GA taxonomy and supports both CBT 1 and CBT 2 items. Each topic folder will contain parallel “english” and “hindi” subfolders where available. File naming will standardize metadata capture, and a top-level metadata index will document the source, licensing, and mapping to CBT 1/CBT 2.

Proposed directory layout:

- practice-ga/
  - indian-history/
    - english/
    - hindi/
  - geography/
    - english/
    - hindi/
  - polity/
    - english/
    - hindi/
  - economy/
    - english/
    - hindi/
  - current-affairs/
    - english/
    - hindi/
  - static-gk/
    - english/
    - hindi/
  - science-technology/
    - english/
    - hindi/
  - metadata/
  - compliance/

File naming standard:  
<topic>-<subtopic>-<source>-<language>-<date>.md

Examples:  
- history-ancient-testbook-en-2025-10.md  
- geography-india-rrbexamportal-hi-2025-10.md

A metadata schema (detailed later) will be embedded as YAML front matter within each file and mirrored in a machine-readable index (e.g., JSON/CSV) for audits and automated reporting.

## Metadata Schema and Syllabus Mapping

Metadata enables traceability to sources and compliance, while simplifying updates and audits. Each practice file will include structured front matter summarizing source and licensing details, topic tags aligned to the GA taxonomy, and CBT applicability. The internal syllabus_map.csv (where used) will be updated to reflect CBT 1/CBT 2 coverage.

Proposed metadata fields:

- title
- source_name
- source_url
- license_type (e.g., personal-use-only, all-rights-reserved, free-with-attribution)
- redistribution_allowed (yes/no/internal-only)
- language (en/hi)
- topics (comma-separated tags aligned to Table 2)
- cbt1_applicable (yes/no)
- cbt2_applicable (yes/no)
- question_count
- answer_key_available (yes/no)
- date_accessed
- notes (e.g., “signup required”, “manual curation”, “anti-bot protection”)

Table 7. Metadata field dictionary (selected fields)

| Field | Description | Example |
|-------|-------------|---------|
| title | Display title of the practice set | “Top 500 GK Questions (CBT 2)” |
| source_name | Portal or publisher | “PracticeMock” |
| license_type | Observed license category | “personal-use-only” |
| redistribution_allowed | Yes/No/Internal-only | “No” |
| language | en/hi | “en” |
| topics | GA taxonomy tags | “current-affairs, static-gk” |
| cbt1_applicable | Yes/No | “Yes” |
| cbt2_applicable | Yes/No | “Yes” |
| question_count | Integer | 500 |
| date_accessed | ISO date | 2025-10-30 |

Table 8. CBT 1 vs CBT 2 applicability matrix by GA topic family

| Topic Family                   | CBT 1 | CBT 2 |
|--------------------------------|-------|-------|
| Current Affairs                | Yes   | Yes   |
| Static GK                      | Yes   | Yes   |
| History                        | Yes   | Yes (expanded) |
| Geography                      | Yes   | Yes (expanded) |
| Polity & Governance            | Yes   | Yes (expanded) |
| Economy                        | Yes   | Yes   |
| Science & Technology           | Yes   | Yes   |
| Computers & Abbreviations      | Yes   | Yes   |
| Organizations & UN             | Yes   | Yes   |
| Environment & Biodiversity     | Yes   | Yes   |
| Art, Culture, Literature, Monuments | Yes | Yes |
| Transport Systems              | Yes   | Yes   |
| Personalities                  | Yes   | Yes   |
| Government Schemes             | Yes   | Yes   |

This schema ensures every item can be audited for source, license, and exam alignment, and simplifies generation of stage-specific practice sheets.

## Download and Organization Workflow

We will apply a source-specific workflow that respects terms, minimizes friction, and leaves a clear audit trail.

- Direct PDFs (free, no gating): capture item-level metadata and store per topic-language subfolder with attribution and license tags.  
- Signup-gated PDFs: record the access method; download only if permitted; otherwise, curate question types and solution styles internally for guidance without redistributing source content.  
- Manual or interactive access (anti-bot/redirects): log access steps; prioritize item-level notes and metadata; avoid scraping; seek permission when necessary.

Validation steps include: confirming license allowability; tagging language; tagging CBT applicability; and updating the metadata index.

Table 9. Portal-wise acquisition checklist and fallback routes

| Portal | Access Method | Gating | Anti-bot/Redirects | Fallback |
|--------|---------------|--------|--------------------|----------|
| Testbook[^12][^13][^14][^15] | Signup to download PDFs | Yes | Possible | Internal curation; do not redistribute |
| Jagran Josh[^5][^8][^9] | Direct article access | No | Occasional | Manual curation; no bulk PDFs |
| RRB Exam Portal[^16][^18][^19][^20][^21][^22][^23][^24] | Mixed: free PDFs via page | Sometimes | Instamojo/redirects | Item-level notes; record access path |
| PracticeMock[^7][^11] | Free PDF via platform | Sometimes | Redirects | Download if permitted; otherwise note |
| Oliveboard[^6] | Free blogs; registration | Sometimes | Possible | Use weightage guidance; avoid redistribution |
| SSC Study[^10] | Direct PDFs | No | Possible | Confirm rights; use per source notes |
| Railway Capsule[^25] | Free online tests/quizzes | No | Possible | Use item formats to design internal sets |

These routes avoid breaching terms, preserve auditability, and still allow a robust practice bank to be assembled.

## Quality Assurance and Update Plan

Quality has two dimensions: content quality and compliance hygiene.

Content QA focuses on accuracy, difficulty alignment, completeness relative to the GA taxonomy, and currency for Current Affairs. We will apply a periodic review cadence:

- Static GK: quarterly refresh to address recurring factual errors and add missing subtopics.  
- Current Affairs: monthly updates to maintain recency; retire outdated items after 12 months or as advised by the exam cycle.  
- Science & Technology: semi-annual review to update Indian space/nuclear programme references and computer basics where applicable.  
- CBT 2 emphasis: semi-annual review of History/Geography/Polity/Economy depth items based on mock-test weightage patterns reported by portals.[^6]

Compliance QA includes license audits, permission checks before any external sharing, and monitoring of policy changes on portals. We will track source modifications via a simple changelog.

Table 10. QA checklist by content type

| Content Type | Checks | Frequency | Owner |
|--------------|--------|-----------|-------|
| Static GK | Factual accuracy; coverage breadth; bilingual parity | Quarterly | Content Lead |
| Current Affairs | Recency; relevance to GA; source attribution | Monthly | Current Affairs Editor |
| Science & Technology | Syllabus alignment; Indian S&T updates;计算机 basics | Semi-annual | Science Editor |
| History/Geography/Polity/Economy | Depth and difficulty for CBT 2; syllabus drift | Semi-annual | Subject Leads |
| Licensing | Terms review; permission status; redistribution logs | Quarterly | Compliance Officer |
| Metadata | Completeness; CBT tags; language tags | Ongoing | Metadata Steward |

Weightage guidance from Oliveboard’s CBT 2 resource will help calibrate emphasis in the bank, while Jagran Josh’s Static GK lists will anchor breadth.[^6][^9] Railway Capsule’s bilingual quizzes will be leveraged for difficulty calibration and language parity checks.[^25]

## Risk Assessment and Information Gaps

- Redistribution ambiguity: Several portals do not state redistribution terms explicitly. Mitigation: default to internal use with attribution, maintain a permissions log, and reach out for clarifications where needed.  
- Anti-bot and gating: Some downloads require signup or redirect via third-party checkout. Mitigation: manual item-level curation and clear documentation of access method; avoid scraping.  
- Bilingual coverage per item: Not all pages confirm Hindi availability. Mitigation: maintain language tags, set a “Hindi parity” QA target, and seek Hindi variants explicitly.  
- Automation feasibility: Sites with HTTP 403 or similar protections will be accessed manually. Mitigation: capture metadata at acquisition and avoid bulk automated downloading.

Table 11. Risk register (selected)

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Unclear redistribution terms | High | Medium | Default to internal use; request permissions; log decisions | Compliance |
| Anti-bot protections | Medium | Medium | Manual access; record steps; avoid scraping | Content Ops |
| Hindi parity gaps | Medium | Medium | Track language tags; seek Hindi variants; QA targets | Metadata |
| Outdated Current Affairs | Medium | High | Monthly refresh; retirement policy | Current Affairs |
| Licensing changes | Low | Medium | Quarterly audit; changelog | Compliance |

These gaps and mitigations will be revisited quarterly, aligned to the QA cadence.

## Appendices

### Appendix A. Source catalog (indicative)

| ID | Title | Type | Access Date |
|----|-------|------|-------------|
| 1 | RRBs Website – Ministry of Railways | Official | 2025-10-30 |
| 2 | RRB NTPC Syllabus (BYJU’S-hosted, aligned to CEN 01/2019) | Official | 2025-10-30 |
| 3 | RRB NTPC Exam Pattern – Shiksha | Portal | 2025-10-30 |
| 4 | RRB NTPC Exam Pattern – Testbook | Portal | 2025-10-30 |
| 5 | RRB NTPC Syllabus – Jagran Josh | Portal | 2025-10-30 |
| 6 | Top 500 Important GK Questions for RRB NTPC CBT 2 – Oliveboard | Portal | 2025-10-30 |
| 7 | 500+ Current Affairs for RRB NTPC CBT 2 2025 – PracticeMock (Blog) | Portal | 2025-10-30 |
| 8 | RRB NTPC Exam Pattern – Jagran Josh | Portal | 2025-10-30 |
| 9 | Important GK Topics for Railway Exams – Jagran Josh | Portal | 2025-10-30 |
| 10 | RRB Study Material PDF Download – SSC Study | Portal | 2025-10-30 |
| 11 | RRB NTPC CBT 2 Current Affairs (PDF) – PracticeMock (Direct) | Portal | 2025-10-30 |
| 12 | RRB NTPC GK Questions – Testbook | Portal | 2025-10-30 |
| 13 | RRB NTPC History Questions – Testbook | Portal | 2025-10-30 |
| 14 | RRB NTPC Geography Questions – Testbook | Portal | 2025-10-30 |
| 15 | RRB NTPC Polity Questions – Testbook | Portal | 2025-10-30 |
| 16 | Download Free E-Books for RRB Exams – RRB Exam Portal | Portal | 2025-10-30 |
| 17 | RRB NTPC (CBT-1 & CBT-2) Exam Papers and Study Notes – RRB Exam Portal | Portal | 2025-10-30 |
| 18 | RRB ALP, NTPC Exams 2025 Current Affairs (GA) PDF – RRB Exam Portal | Portal | 2025-10-30 |
| 19 | RRB GK 1000 One-Liner Questions PDF – RRB Exam Portal | Portal | 2025-10-30 |
| 20 | RRB NTPC Sample Papers (English) – RRB Exam Portal | Portal | 2025-10-30 |
| 21 | RRB NTPC Sample Papers (Hindi) – RRB Exam Portal | Portal | 2025-10-30 |
| 22 | RRB NTPC CBT-1 2021 Papers with Answers (English) – RRB Exam Portal | Portal | 2025-10-30 |
| 23 | RRB NTPC CBT-1 2021 Papers with Answers (Hindi) – RRB Exam Portal | Portal | 2025-10-30 |
| 24 | RRB NTPC CBT Tier-2 Papers (Hindi) – RRB Exam Portal | Portal | 2025-10-30 |
| 25 | Railway Capsule – Free Railway Exam Preparation | Portal | 2025-10-30 |
| 26 | RRB NTPC General Awareness Syllabus 2025 – Physics Wallah | Portal | 2025-10-30 |
| 27 | RRB NTPC Exam Pattern – EMBIBE | Portal | 2025-10-30 |
| 28 | RRB NTPC Exam Pattern – Careers360 | Portal | 2025-10-30 |

Note: Where portals are intermittently blocked or require signup, access is logged and content is curated in line with stated terms.

### Appendix B. Glossary of GA taxonomy and tag synonyms

| Canonical Tag | Synonyms/Examples | Notes |
|---------------|-------------------|-------|
| current-affairs | National Events, International Events, Important Days, Awards, Government Schemes | Keep last 6–12 months current for CBT 2 |
| static-gk | General Knowledge, One-liners, Important Personalities, Organizations | Basis of many CBT 1 questions |
| history | Ancient India, Medieval India, Modern India, Freedom Struggle | CBT 2 adds depth on dynasties and battles |
| geography | Physical Geography, Social Geography, Economic Geography, Maps | Includes India & World |
| polity | Constitution, Articles, Parliament, Supreme Court, Local Governance | Expand for CBT 2 |
| economy | Banking, Budget, Economic Indicators, Five-Year Plans | Applied and conceptual items |
| science-technology | General Science, Space Programme, Nuclear Programme, Computers | Up to 10th CBSE level |
| computers | Basics of Computers, Abbreviations, Applications | GA component, not a full CS paper |
| organizations | UN and Other World Organizations, Government/PSU Organizations | Pair with Static GK |
| environment | Environmental Issues, Flora and Fauna | Pair with Static GK |
| art-culture-literature | Indian Art & Culture, Monuments, Literature | Cultural awareness |
| transport | Transport Systems in India | Infrastructure-focused |
| personalities | Famous Personalities of India and World | Awards, achievements |
| schemes | Flagship Government Programs | Policy-linked GA items |

### Appendix C. Sample metadata record (YAML front matter)

```yaml
---
title: "Current Affairs One-liners (Mar–Aug 2025)"
source_name: "PracticeMock"
source_url: "https://www.practicemock.com/pricing/marketing/files/pdf/rrb-ntpc-cbt-2-current-affairs.pdf"
license_type: "free-with-attribution"
redistribution_allowed: "no"
language: "en"
topics: ["current-affairs", "static-gk"]
cbt1_applicable: "yes"
cbt2_applicable: "yes"
question_count: 500
answer_key_available: "yes"
date_accessed: "2025-10-30"
notes: "Downloaded via platform flow; curated one-liners."
---
```

---

## References

[^1]: RRBs Website – Ministry of Railways. https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,7,1281  
[^2]: RRB NTPC Syllabus (BYJU’S-hosted PDF aligned to CEN 01/2019). https://cdn1.byjus.com/wp-content/uploads/2020/07/RRB-NTPC-Syllabus.pdf  
[^3]: RRB NTPC Exam Pattern – Shiksha. https://www.shiksha.com/exams/rrb-ntpc-exam-pattern  
[^4]: RRB NTPC Exam Pattern – Testbook. https://testbook.com/rrb-ntpc/exam-pattern  
[^5]: RRB NTPC Syllabus – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-cbt-1-and-2-syllabus-2024-pdf-download-1716465685-1  
[^6]: Top 500 Important GK Questions for RRB NTPC CBT 2 Exam – Oliveboard. https://www.oliveboard.in/blog/gk-questions-for-rrb-ntpc-cbt-2-exam/  
[^7]: 500+ Most Expected Current Affairs for RRB NTPC CBT 2 2025 – PracticeMock (Blog). https://www.practicemock.com/blog/500-most-expected-current-affairs-for-rrb-ntpc-2025-exam/  
[^8]: RRB NTPC Exam Pattern – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-exam-pattern-2025-check-cbt-1-cbt-2-cbat-marking-scheme-total-marks-1749038705-1  
[^9]: Important GK Topics for Railway Exams (RRB NTPC/ALP/JE) – Jagran Josh. https://www.jagranjosh.com/articles/important-gk-topics-for-railway-exams-rrb-ntpc-alp-technician-junior-engineer-1729086350-1  
[^10]: RRB Study Material PDF Download – SSC STUDY. https://sscstudy.com/rrb-study-material-pdf-download/  
[^11]: RRB NTPC CBT 2 Current Affairs (PDF) – PracticeMock (Direct). https://www.practicemock.com/pricing/marketing/files/pdf/rrb-ntpc-cbt-2-current-affairs.pdf  
[^12]: RRB NTPC GK Questions – Testbook. https://testbook.com/questions/rrb-ntpc-gk-questions--64b552be2819d5020ab670d1  
[^13]: RRB NTPC History Questions – Testbook. https://testbook.com/questions/rrb-ntpc-history-questions--64b552e25892952591cb974e  
[^14]: RRB NTPC Geography Questions – Testbook. https://testbook.com/questions/rrb-ntpc-geography-questions--64b553035bdbea2b1b26aa19  
[^15]: RRB NTPC Polity Questions – Testbook. https://testbook.com/questions/rrb-ntpc-polity-questions--64b552f31195cc2216ecaa36  
[^16]: Download Free E-Books for RRB Exams – RRB Exam Portal. https://rrbexamportal.com/ebook  
[^17]: RRB NTPC (CBT-1 & CBT-2) Exam Papers and Study Notes – RRB Exam Portal. https://rrbexamportal.com/RRB-NTPC  
[^18]: RRB ALP, NTPC Exams 2025 Current Affairs (General Awareness) PDF – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-exam-current-affairs  
[^19]: RRB GK 1000 One-Liner Questions PDF – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-gk-1000-questions-pdf  
[^20]: RRB NTPC Sample Papers (English) – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-ntpc-exam-sample-papers-pdf  
[^21]: RRB NTPC Sample Papers (Hindi) – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-ntpc-exam-sample-papers-pdf-hindi  
[^22]: RRB NTPC CBT-1 2021 Papers with Answers [English] – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-ntpc-2021-papers-pdf  
[^23]: RRB NTPC CBT-1 2021 Papers with Answers [Hindi] – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-ntpc-2021-papers-pdf-hindi  
[^24]: RRB NTPC CBT Tier-2 Papers with Answers [Hindi] – RRB Exam Portal. https://rrbexamportal.com/ebook/rrb-ntpc-tier-2-papers-pdf-hindi  
[^25]: Railway Capsule – Free Railway Exam Preparation Platform. https://railwaycapsule.com/  
[^26]: RRB NTPC General Awareness Syllabus 2025 – Physics Wallah. https://www.pw.live/railway/exams/rrb-ntpc-general-awareness-syllabus  
[^27]: RRB NTPC Exam Pattern – EMBIBE. https://www.embibe.com/exams/rrb-ntpc-exam-pattern/  
[^28]: RRB NTPC Exam Pattern – Careers360. https://competition.careers360.com/articles/rrb-ntpc-exam-pattern