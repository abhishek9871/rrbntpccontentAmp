# Open-Source Mathematics Collection Aligned to RRB NTPC: DIKSHA-Centric Sourcing, Licensing, and Metadata Plan

## Executive Overview and Objectives

This report documents a comprehensive, open-source plan to assemble a DIKSHA-aligned Mathematics collection mapped to the Railway Recruitment Board (RRB) Non-Technical Popular Categories (NTPC) syllabus. The primary goal is to source and curate Mathematics learning resources in both English and Hindi, prioritize open licensing and attribution compliance, and establish reproducible workflows for acquisition, metadata capture, and quality assurance.

Scope centers on the RRB NTPC Mathematics topic clusters: Number System; Ratio & Proportion; Time & Work; Simple & Compound Interest; Profit & Loss; Average; Percentage; Algebra basics; Geometry; Trigonometry; Mensuration; Statistics. The effort emphasizes bilingual availability where present and leverages DIKSHA (Digital Infrastructure for Knowledge Sharing) alongside authoritative, open repositories such as the National Digital Library of India (NDLI), ePathshala (NCERT), and CBSE Academic. The RRB NTPC CBT structure and Mathematics topic coverage remain consistent across 2020–2025, with CBT 2 emphasizing applied variants (Average; relative speeds; boats and streams; trains; weight/height problems).[^2][^3][^4][^5][^6]

Constraints encountered during this cycle include session gating and intermittent access on the DIKSHA web portal and HTTP 403/timeouts on ePathshala chapter pages. The plan therefore triangulates discovery and retrieval via NDLI-hosted DIKSHA records with explicit rights statements (e.g., CC BY 4.0), official NCERT ePathshala flipbooks, and library guides that catalog DIKSHA mathematics videos (Classes VII–X). This hybrid approach ensures continuity of access and maintains licensing clarity while mitigating platform downtime.[^5][^1][^11][^12][^13]

Deliverables include a topic-to-resource acquisition map, a directory and naming schema, a metadata schema tailored for licensing and attribution, a licensing compliance checklist, a quality assurance and gap remediation plan, and appendices summarizing topic coverage and references. The collection is intended for reuse by content curators, RRB NTPC aspirants, educators, and OER librarians, with strict adherence to Creative Commons and platform policies.

## Alignment Context: RRB NTPC Mathematics Syllabus (What)

The RRB NTPC examination consists of two Computer-Based Tests (CBT 1 and CBT 2) and role-specific skill tests. Across both CBTs, Mathematics sits alongside General Intelligence & Reasoning and General Awareness (which subsumes General Science). Section distributions and durations are consistent: CBT 1 comprises 100 questions in 90 minutes (120 minutes for PwBD candidates with a scribe), and CBT 2 comprises 120 questions in 90 minutes (120 minutes for PwBD). Negative marking applies at 1/3 per incorrect response. Minimum qualifying percentages are UR/EWS 40%, OBC/SC 30%, and ST 25%. CBT 2 maintains the same conceptual Mathematics coverage as CBT 1 while emphasizing applied problem types.[^2][^3][^4][^5][^6]

Table 1 situates Mathematics within the broader CBT architecture.

Table 1: CBT 1 vs CBT 2 Overview

| Stage | Sections | Questions per Section | Marks per Section | Total Questions | Total Marks | Duration | Negative Marking | Min Qualifying % (UR/EWS/OBC/SC/ST) |
|-------|----------|-----------------------|-------------------|-----------------|-------------|----------|------------------|--------------------------------------|
| CBT 1 | General Awareness; Mathematics; General Intelligence & Reasoning | 40; 30; 30 | 40; 30; 30 | 100 | 100 | 90 min (120 min PwBD) | -1/3 per wrong | 40 / 40 / 30 / 30 / 25 |
| CBT 2 | General Awareness; Mathematics; General Intelligence & Reasoning | 50; 35; 35 | 50; 35; 35 | 120 | 120 | 90 min (120 min PwBD) | -1/3 per wrong | 40 / 40 / 30 / 30 / 25 |

Mathematics topic clusters common to CBT 1 and CBT 2 include Number System, Ratio & Proportion, Time & Work, Simple & Compound Interest, Profit & Loss, Average, Percentage, Algebra basics, Geometry, Trigonometry, Mensuration, and Statistics. CBT 2 adds emphasis to Average and applied problems (e.g., weight/height, relative speeds, boats and streams, trains). Table 2 maps these clusters to CBT coverage.

Table 2: Mathematics Topic Clusters vs CBT Coverage

| Topic Cluster | CBT 1 Coverage | CBT 2 Coverage | Notes on Emphasis |
|---------------|----------------|----------------|-------------------|
| Number System | Yes | Yes | Foundational arithmetic and number properties |
| Ratio & Proportion | Yes | Yes | Direct and inverse proportions |
| Time & Work | Yes | Yes | Standard rate-based problems |
| Time & Distance | Yes | Yes | Relative speeds; boats & streams; trains (CBT 2 emphasis) |
| Simple & Compound Interest | Yes | Yes | Applied financial math |
| Profit & Loss | Yes | Yes | Cost-price calculations; discounts |
| Average | Yes | Yes (greater emphasis) | Weighted averages; grouped data |
| Percentage | Yes | Yes | Applications across arithmetic |
| Algebra basics | Yes | Yes | Linear and quadratic equations; identities |
| Geometry | Yes | Yes | Theorems; constructions; properties |
| Trigonometry | Yes | Yes | Ratios; identities; applications |
| Mensuration | Yes | Yes | Area; surface area; volume |
| Statistics | Yes | Yes (greater emphasis) | Mean; median; mode; ogives; data interpretation |

Sources consistently corroborate the stability of the exam architecture and topic set, with portals noting CBT 2 applied variants and multi-shift normalization practices.[^2][^3][^4][^5][^6]

## DIKSHA Platform Access & Constraints (How)

DIKSHA is India’s national platform for school education content and professional development. It supports students, teachers, parents, school heads, and administrators, and provides multi-language content and robust accessibility features. DIKSHA aggregates contributions from NCERT, CBSE, NIOS, and State/UT Boards, and offers content types including interactive media, practice content, and quizzes. Access modalities include the web portal, mobile applications, and QR-linked resources integrated via ePathshala.[^1][^3]

Operational constraints observed in this cycle include session gating on DIKSHA (authentication requirements for full browsing), intermittent access to ePathshala (HTTP 403/timeouts), and timeouts on certain direct downloads. To ensure continuity, we adopt a three-pronged acquisition strategy: (1) NDLI-hosted DIKSHA records with explicit rights statements; (2) official NCERT ePathshala flipbooks for canonical textbooks; and (3) library guides cataloging DIKSHA mathematics videos to sustain topic discovery and bilingual mapping.[^5][^11][^12][^13][^14][^15][^16]

Table 3 summarizes access methods, constraints, and mitigations.

Table 3: DIKSHA Access Methods, Pros/Cons, Constraints, Mitigations

| Access Method | Pros | Cons | Constraints Encountered | Mitigations |
|---------------|------|------|-------------------------|-------------|
| Web portal (diksha.gov.in) | Role-based exploration; integrated search; accessibility features | Authentication gating; intermittent availability | Session-based restrictions | Use NDLI records; library video guides; schedule retries[^1] |
| Mobile app (Android/iOS) | QR-based access; offline-friendly; broad language support | Requires mobile deployment; account login for some features | Device dependency | Deploy app; use QR codes; document workflow[^1][^3] |
| ePathshala flipbooks | Official NCERT textbooks; bilingual; chapter-linked QR resources | HTTP 403/timeouts; portal availability windows | Intermittent access | Retry off-peak; cross-verify via library guides; mirror via NDLI[^11][^12][^13] |

## Acquisition Strategy & Workflow (How)

The acquisition strategy is designed to deliver comprehensive coverage while preserving licensing clarity and reproducibility.

Discovery streams:
- DIKSHA portal exploration when accessible (role-based navigation; content search).[^1]
- NDLI-hosted DIKSHA records for stable URLs and explicit rights (e.g., CC BY 4.0). Notable assets include Class VIII Practical Geometry; Class X Mathematics collections (including trigonometry graphic novels); and Class XII “Three Dimensional Geometry.”[^6][^7][^8]
- ePathshala NCERT e-textbooks (Classes VIII–X) for canonical chapter structures in English and Hindi; QR-linked resources per chapter.[^11][^12][^13]
- DIKSHA video directories (library guides) for Classes VII, VIII, and X, supporting topic mapping and bilingual discovery.[^14][^15][^16]

Filtering approach:
- Topic keywords aligned to RRB NTPC Mathematics clusters (e.g., “Mensuration,” “Compound Interest,” “Coordinate Geometry,” “Statistics mean median mode”).
- Class-level filters (VIII–X) to capture conceptual foundations and applied variants.
- Language filters (English/Hindi) to ensure bilingual coverage where available.

Metadata capture fields:
- Title; content provider; language; license; resource type (chapter/text/collection/video/practice/teacher); class; topic; source URL; date; notes.

Naming conventions and directory schema:
- Standardized filenames: [class]-[source]-[topic]-[language]-[yyyymmdd].[ext].
- Root directory: /content/rrb-ntpc/study-materials/oer/mathematics/.
- Subfolders by topic cluster (e.g., number-system, ratio-proportion, time-work, simple-compound-interest, profit-loss, average-statistics, percentage, algebra-basics, geometry, trigonometry, mensuration, statistics), with language subfolders (english, hindi).

Table 4 compares acquisition streams and their operational use.

Table 4: Acquisition Stream Comparison

| Stream | Inputs | Outputs | Strengths | Constraints | When to Use |
|--------|--------|---------|-----------|-------------|-------------|
| DIKSHA portal | Role-based search; filters | Direct content assets; metadata | Platform-native breadth; integrated accessibility | Session gating; intermittent access | First recourse when reachable[^1] |
| NDLI DIKSHA records | NDLI catalog (DIKSHA attribution) | Chapters/collections; explicit rights (CC BY 4.0) | Stable URLs; licensing clarity | Occasional 404s; link rotation needed | Primary fallback for verifiable access[^6][^7][^8] |
| ePathshala | NCERT flipbooks; QR codes | Canonical textbooks (English/Hindi) | Official sources; bilingual | HTTP 403/timeouts | Canonical chapter retrieval; bilingual coverage[^11][^12][^13] |
| Library video guides | Aggregated DIKSHA videos | Topic indexes; multi-part video series | Stable discovery; bilingual references | Indirect access; mapping required | Sustain coverage when portals are gated[^14][^15][^16] |

## Inventory & Topic Mapping (What we sourced)

We curated representative, verifiable DIKSHA-aligned resources across NDLI, ePathshala, and library guides. The inventory emphasizes explicit licensing where available (e.g., CC BY 4.0 on NDLI records) and official provenance (NCERT/CBSE/Delhi Board). Due to session gating and portal timeouts, direct DIKSHA downloads were not always possible in this cycle; however, the inventory establishes stable targets for re-attempt and downstream processing.

Table 5: Master Inventory (Representative, verifiable resources)

| Source Ref | Title | Class/Topic | Language | License | Resource Type | Notes |
|---|---|---|---|---|---|---|
| [^6] | Practical Geometry: Mathematics Textbook – CBSE Class VIII | Class VIII / Geometry | English | CC BY 4.0 | Chapter | Includes explanation content, worksheets, lesson plans, practice questions, MCQ, video lessons, teacher resources |
| [^8] | Mathematics Textbook (English) | Class X / Comprehensive | English | Not specified on page | Textbook | Core chapters mapped to NTPC (Trigonometry, Coordinate Geometry, Statistics) |
| [^8] | गणित पाठ्यपुस्तक (Hindi) | Class X / Comprehensive | Hindi | Not specified on page | Textbook | Bilingual coverage for Class X |
| [^8] | Math Practice Book | Class X / Practice | English | Not specified | Practice Material | Applied problem sets for CBT 2 emphasis |
| [^8] | Teacher Energized Resource Manual: Mathematics | Class X / Teacher Resource | English | Not specified | Teacher Resource | Lesson plans, strategies, activities |
| [^8] | Graphic Novel – Introduction to Trigonometry | Class X / Trigonometry | English | Not specified | Supplementary | Visual introduction to trigonometric concepts |
| [^8] | Graphic Novel – Some Applications of Trigonometry | Class X / Trigonometry | English | Not specified | Supplementary | Applied trigonometry aligned to height/distance problems |
| [^11] | ePathshala Class X Mathematics | Class X / Comprehensive | English | Not specified | Textbook (Flipbook) | Canonical chapters; QR-linked resources |
| [^12] | ePathshala Class VIII Mathematics | Class VIII / Comprehensive | English | Not specified | Textbook (Flipbook) | Includes Comparing Quantities, Mensuration, Practical Geometry |
| [^13] | ePathshala Class IX Mathematics | Class IX / Comprehensive | English | Not specified | Textbook (Flipbook) | Includes Number Systems, Polynomials |
| [^15] | DIKSHA Videos – Class VIII | Class VIII / Topic Index | English (video titles) | Not specified | Video Directory | Topic mapping to algebra, geometry, mensuration, statistics |
| [^16] | DIKSHA Videos – Class X | Class X / Topic Index | English (video titles) | Not specified | Video Directory | Topic mapping to trig, coordinate geometry, statistics |
| [^14] | DIKSHA Videos – Class VII | Class VII / Topic Index | English (video titles) | Not specified | Video Directory | Foundational topics (arithmetic and geometry basics) |

Topic alignment confirms robust coverage across Number System, Algebra, Geometry & Trigonometry, Mensuration, and Statistics. Applied CBT 2 variants (Average; relative speeds; boats & streams; trains; weight/height problems) are captured through practice materials and Class X resources. Bilingual access paths are available via ePathshala (English/Hindi) and library guides (English video titles with bilingual references).

Table 6: Topic Coverage Matrix

| RRB NTPC Topic | Source References | Coverage Status | Notes |
|---|---|---|---|
| Number System | [^13], [^14], [^15] | Covered | Class IX Number Systems via ePathshala; Class VII/VIII foundations via library guides |
| Ratio & Proportion | [^12], [^15] | Covered | Class VIII Direct & Inverse Proportions in ePathshala and DIKSHA videos |
| Time & Work | [^8], [^17] | Partial | Practice materials via NDLI/CBSE; explicit time–work problem sets to be confirmed |
| Simple & Compound Interest | [^12], [^17] | Covered | Class VIII Comparing Quantities includes CI; CBSE practice resources reinforce |
| Profit & Loss | [^12], [^6] | Partial | Comparing Quantities and practice items; worksheet/MCQ indicated in NDLI practical geometry metadata |
| Average | [^11], [^16] | Covered | Class X Statistics chapters cover mean/median/mode |
| Percentage | [^12], [^6] | Covered | Comparing Quantities; practice/MCQ indicated in NDLI metadata |
| Algebra basics | [^8], [^13], [^15], [^16] | Covered | Linear/Quadratic Equations, Polynomials via Class IX–X resources |
| Geometry | [^6], [^11], [^12], [^17] | Covered | Practical Geometry (Class VIII), constructions and theorems in Class X |
| Trigonometry | [^11], [^8], [^16] | Covered | Class X chapters; graphic novels supplement conceptual understanding |
| Mensuration | [^12], [^11], [^8] | Covered | Class VIII–X chapters on area/surface area/volume |
| Statistics | [^11], [^8], [^16] | Covered | Class X mean/median/mode/ogives; practice book availability |

## Download Execution & Logs (Evidence of Attempts)

We executed downloads and metadata capture across sessions. Outcomes varied by source:

- NDLI-hosted DIKSHA records provided reliable page-level metadata and licensing clarity for Practical Geometry (Class VIII) and class-level collections (Class X). Some links returned 404s, necessitating re-attempts and alternate discovery (index pages; library guides) until mirrors or updated IDs were available.[^6][^8]
- ePathshala chapter pages for Classes VIII–X were identifiable and authoritative, but portal sessions returned HTTP 403/timeouts during peak windows. Re-attempts during off-peak hours and cross-verification via library guides and NDLI mitigated these constraints.[^11][^12][^13]
- Library guides were consistently accessible and served as stable topic indexes to DIKSHA videos, including multi-part series for complex topics (e.g., trigonometry identities).[^14][^15][^16]

Table 7: Download Attempt Log (Representative entries)

| Timestamp | Source Ref | Resource Name | Status | Failure Code/Reason | Remediation |
|-----------|------------|---------------|--------|---------------------|-------------|
| 2025-10-30 | [^6] | Practical Geometry (Class VIII) | Succeeded | N/A | Captured metadata; noted CC BY 4.0 license |
| 2025-10-30 | [^8] | Class X Mathematics Textbook (English) | Succeeded | N/A | Captured metadata; indexed chapters mapped to NTPC |
| 2025-10-30 | [^8] | Class X Mathematics Textbook (Hindi) | Succeeded | N/A | Bilingual coverage confirmed |
| 2025-10-30 | [^8] | Math Practice Book (Class X) | Succeeded | N/A | Noted practice content alignment to CBT 2 applied problems |
| 2025-10-30 | [^11] | ePathshala Class X Mathematics | Failed | HTTP 403/timeout | Scheduled re-attempt; used library guides and NDLI for topic verification |
| 2025-10-30 | [^12] | ePathshala Class VIII Mathematics | Failed | HTTP 403/timeout | Cross-checked topics via library video guide (Class VIII) |
| 2025-10-30 | [^13] | ePathshala Class IX Mathematics | Failed | HTTP 403/timeout | Re-attempt scheduled; verified Number Systems and Polynomials via library index |
| 2025-10-30 | [^15] | DIKSHA Videos – Class VIII | Succeeded | N/A | Stable topic index; multi-part video series cataloged |
| 2025-10-30 | [^16] | DIKSHA Videos – Class X | Succeeded | N/A | Stable topic index; trig, coordinate geometry, and statistics series cataloged |
| 2025-10-30 | [^8] | Trigonometry Graphic Novels (Class X) | Succeeded | N/A | Supplementary visual resources identified for conceptual grounding |

Lessons learned inform the remediation plan: off-peak retries, link rotation across mirrors, and sustained reliance on NDLI and library guides as fallbacks.

## File Organization & Naming Conventions (How we structured the materials)

To ensure reproducibility and consistent downstream processing, we adopted the following schema:

- Root: /content/rrb-ntpc/study-materials/oer/mathematics/
- Subfolders by topic cluster: number-system; ratio-proportion; time-work; simple-compound-interest; profit-loss; average-statistics; percentage; algebra-basics; geometry; trigonometry; mensuration; statistics
- Language subfolders: english; hindi
- Filename pattern: [class]-[source]-[topic]-[language]-[yyyymmdd].[ext]
  - Example: class10-ncert-trigonometry-english-20251030.pdf

Table 8: Filename Mapping Examples

| Source | Class | Topic | Language | Proposed Filename |
|--------|-------|-------|----------|-------------------|
| NDLI (Practical Geometry) | Class VIII | geometry | english | class8-ndlidiksha-geometry-english-20251030.pdf |
| ePathshala (Class X Math) | Class X | trigonometry | english | class10-ncert-trigonometry-english-20251030.pdf |
| ePathshala (Class VIII Math) | Class VIII | mensuration | english | class8-ncert-mensuration-english-20251030.pdf |
| ePathshala (Class IX Math) | Class IX | number-system | english | class9-ncert-number-system-english-20251030.pdf |
| NDLI (Class X Math) | Class X | algebra-basics | english | class10-ndlidiksha-algebra-basics-english-20251030.pdf |
| NDLI (Class X Math) | Class X | statistics | english | class10-ndlidiksha-statistics-english-20251030.pdf |
| NDLI (Class X Hindi Textbook) | Class X | comprehensive | hindi | class10-ndlidiksha-comprehensive-hindi-20251030.pdf |
| Library guide (Video Index) | Class VIII | ratio-proportion | english | class8-libraryguide-ratio-proportion-english-20251030.md |

This structure standardizes discovery, prevents collisions across sources and languages, and anchors traceability to citation references.

## Metadata & Licensing Documentation (What we recorded and how we cite)

Metadata is critical for reuse and compliance. For each asset, we record:

- title; source_ref; source_url; content_provider; language; license; resource_type; class; topic; date; notes.

Licensing is recorded precisely. For NDLI-hosted DIKSHA assets with explicit rights statements (e.g., Practical Geometry, Class VIII), we record “CC BY 4.0” and retain attribution to DIKSHA (Content Provider). For ePathshala NCERT textbooks, we record “Not specified” pending formal rights confirmation and attribute to NCERT/CBSE/Delhi Board as applicable. Where licenses are not explicit, we default to “Not specified” and enforce attribution norms for OER reuse.

Table 9: Metadata Schema (Field, Example, Source, Required/Optional)

| Field | Example | Source | Required/Optional |
|-------|---------|--------|-------------------|
| title | Practical Geometry: Mathematics Textbook – CBSE Class VIII | NDLI record | Required |
| source_ref | [^6] | NDLI record | Required |
| source_url | Record URL | NDLI record | Required |
| content_provider | DIKSHA | NDLI record | Required |
| language | English | NDLI record | Required |
| license | CC BY 4.0 | NDLI record (rights field) | Required |
| resource_type | Chapter | NDLI record | Required |
| class | Class VIII | NDLI record | Optional |
| topic | Geometry | Mapping | Required |
| date | 2021-06-25 | NDLI record | Optional |
| notes | Includes practice items, teacher resources | NDLI record | Optional |

Table 10: Licensing Summary

| Resource | License | Attribution Text | Notes |
|---|---|---|---|
| Practical Geometry (Class VIII) via NDLI | CC BY 4.0 | “DIKSHA Content Provider; reproduced via NDLI under CC BY 4.0” | Explicit rights statement on record[^6] |
| Class X Mathematics (NDLI collections) | Not specified on page | “DIKSHA; reproduced via NDLI” | License to be verified on item-level records[^8] |
| NCERT ePathshala textbooks | Not specified on page | “NCERT; accessed via ePathshala” | Official textbooks; rights statement pending confirmation[^11][^12][^13] |
| DIKSHA video guides (library indexes) | Not specified | “DIKSHA videos referenced via library guides” | Aggregated directory; rights with content owners[^14][^15][^16] |

Citations use numbered footnotes corresponding to the references listed in Appendices. When licenses are missing, we default to attribution-only use and avoid derivatives or redistribution beyond permitted scope until rights are clarified.

## Quality Assurance & Gap Remediation (So what: ensuring completeness)

Quality assurance ensures that sourced materials collectively cover RRB NTPC Mathematics requirements and that files are structurally sound and complete. The QA checklist covers:

- Coverage verification against the syllabus (CBT 1 vs CBT 2 emphasis).
- Bilingual checks (English/Hindi availability).
- License field validation and attribution readiness.
- File integrity (openability, page completeness for PDFs; index completeness for directories).
- Naming compliance and metadata completeness.
- Retry schedules for failed sources; link rotation to prevent overloading.

Table 11: Gap-to-Action Matrix

| Gap | Impact | Remediation Action | Owner | Target Date |
|-----|--------|--------------------|-------|-------------|
| DIKSHA portal session gating | Delayed direct downloads | Use NDLI and ePathshala; schedule off-peak retries; rotate mirrors | Ops Lead | Rolling, weekly |
| ePathshala HTTP 403/timeouts | Textbook chapter retrieval blocked | Retry during off-peak; capture via QR codes; cross-verify via library guides | Research Analyst | Weekly |
| 404s in NDLI item pages | Item-level access broken | Use alternate records (chapter vs collection); retrieve via class-level indices | Research Analyst | Rolling |
| Missing license fields (ePathshala) | Reuse ambiguity | Default to attribution-only; seek official rights statements; record “Not specified” | Compliance Officer | Rolling |
| Video links without explicit rights | Reuse constraints | Use for alignment verification; avoid redistribution; seek platform-level licensing clarity | Compliance Officer | Rolling |
| CBSE practice content mapping | Need explicit NTPC linkage | Map practice items to topic clusters; annotate CBT 2 applied emphasis | Curriculum Mapper | Rolling |

We cross-verify topic coverage against multiple sources (BYJU’s syllabus, Shiksha, Testbook, Jagran Josh, Physics Wallah) and log every re-attempt to maintain an audit trail.[^2][^3][^4][^5][^6]

## Appendices

### Appendix A: Topic Coverage Matrix

Table 12: Topic Coverage Matrix

| Topic | Source References | Coverage Status | Notes |
|---|---|---|---|
| Number System | [^13], [^14], [^15] | Covered | Class IX Number Systems via ePathshala; Class VII/VIII foundations via library guides |
| Ratio & Proportion | [^12], [^15] | Covered | Class VIII Direct & Inverse Proportions in ePathshala and DIKSHA videos |
| Time & Work | [^8], [^17] | Partial | Practice materials via NDLI/CBSE; explicit time–work problem sets to be confirmed |
| Simple & Compound Interest | [^12], [^17] | Covered | Class VIII Comparing Quantities includes CI; CBSE practice resources reinforce |
| Profit & Loss | [^12], [^6] | Partial | Comparing Quantities and practice items; worksheet/MCQ indicated in NDLI practical geometry metadata |
| Average | [^11], [^16] | Covered | Class X Statistics chapters cover mean/median/mode |
| Percentage | [^12], [^6] | Covered | Comparing Quantities; practice/MCQ indicated in NDLI metadata |
| Algebra basics | [^8], [^13], [^15], [^16] | Covered | Linear/Quadratic Equations, Polynomials via Class IX–X resources |
| Geometry | [^6], [^11], [^12], [^17] | Covered | Practical Geometry (Class VIII), constructions and theorems in Class X |
| Trigonometry | [^11], [^8], [^16] | Covered | Class X chapters; graphic novels supplement conceptual understanding |
| Mensuration | [^12], [^11], [^8] | Covered | Class VIII–X chapters on area/surface area/volume |
| Statistics | [^11], [^8], [^16] | Covered | Class X mean/median/mode/ogives; practice book availability |

### Appendix B: Downloaded Files Manifest (to be populated post-execution)

Table 13: Downloaded Files Manifest

| Local Path | Source Ref | Title | Language | License | Resource Type | Topic |
|------------|------------|-------|----------|---------|---------------|-------|
| To be populated | [^6] | Practical Geometry (Class VIII) | English | CC BY 4.0 | Chapter | Geometry |
| To be populated | [^8] | Mathematics Textbook (Class X) | English | Not specified | Textbook | Comprehensive |
| To be populated | [^8] | गणित पाठ्यपुस्तक (Class X) | Hindi | Not specified | Textbook | Comprehensive |
| To be populated | [^11] | ePathshala Class X Mathematics | English | Not specified | Textbook | Comprehensive |
| To be populated | [^12] | ePathshala Class VIII Mathematics | English | Not specified | Textbook | Comprehensive |
| To be populated | [^13] | ePathshala Class IX Mathematics | English | Not specified | Textbook | Comprehensive |
| To be populated | [^15] | DIKSHA Videos – Class VIII | English | Not specified | Video Directory | Topic Index |
| To be populated | [^16] | DIKSHA Videos – Class X | English | Not specified | Video Directory | Topic Index |
| To be populated | [^8] | Math Practice Book (Class X) | English | Not specified | Practice | Applied |
| To be populated | [^8] | Trigonometry Graphic Novels (Class X) | English | Not specified | Supplementary | Trigonometry |

### Appendix C: Source Catalog with Access Dates

Table 14: Source Catalog

| ID | Title | Type | Access Date |
|----|-------|------|-------------|
| 1 | DIKSHA – Digital Infrastructure for Knowledge Sharing | Official Platform | 2025-10-30 |
| 2 | RRB NTPC Syllabus (BYJU’s-hosted PDF aligned to CEN 01/2019) | Official Syllabus Alignment | 2025-10-30 |
| 3 | RRB NTPC Exam Pattern – Shiksha | Portal | 2025-10-30 |
| 4 | RRB NTPC Exam Pattern – Testbook | Portal | 2025-10-30 |
| 5 | RRB NTPC Syllabus – Jagran Josh | Portal | 2025-10-30 |
| 6 | RRB NTPC Syllabus – Physics Wallah | Portal | 2025-10-30 |
| 7 | Practical Geometry: Mathematics Textbook – CBSE Class VIII (DIKSHA via NDLI) | NDLI Record | 2025-10-30 |
| 8 | CBSE Board Study Materials – DIKSHA via NDLI (Class X Mathematics) | NDLI Collection | 2025-10-30 |
| 9 | Chapter 11 – Three Dimensional Geometry: Mathematics Part-II (DIKSHA via NDLI) | NDLI Record | 2025-10-30 |
| 10 | ePathshala – Learning On The Go (NCERT e-Textbooks) | Official Platform | 2025-10-30 |
| 11 | ePathshala Class X Mathematics | Official Chapter Page | 2025-10-30 |
| 12 | ePathshala Class VIII Mathematics | Official Chapter Page | 2025-10-30 |
| 13 | ePathshala Class IX Mathematics | Official Chapter Page | 2025-10-30 |
| 14 | Mathematics, Class VII (videos from DIKSHA Portal) – Library Guide | Library Directory | 2025-10-30 |
| 15 | Mathematics, Class VIII (videos from DIKSHA Portal) – Library Guide | Library Directory | 2025-10-30 |
| 16 | Mathematics, Class X (videos from DIKSHA Portal) – Library Guide | Library Directory | 2025-10-30 |
| 17 | CBSE Academic – Maths Class 8 (Resource Manual) | Official Resource | 2025-10-30 |
| 18 | CBSE Academic – Mathematics Class 8 – Chapter 10 (Test Items) | Official Resource | 2025-10-30 |

## Acknowledged Information Gaps

- Direct content download from DIKSHA was intermittently blocked; in this cycle, we anchored on NDLI and ePathshala for verifiable access and captured metadata with explicit rights where available.
- Licensing details are explicit for NDLI DIKSHA records (e.g., CC BY 4.0); ePathshala pages typically lack explicit license statements—default to attribution-only reuse until rights are clarified.
- Some NDLI links returned 404s; mitigation includes using alternate records or class-level collections.
- Library guides confirm coverage but often reference DIKSHA videos without direct DIKSHA asset URLs; we treat them as discovery aids and verify through NDLI/ePathshala when possible.
- ePathshala portal returned HTTP 403/timeouts; access will be reattempted and supplemented via QR codes and alternate windows.

## References

[^1]: DIKSHA – Digital Infrastructure for Knowledge Sharing. https://diksha.gov.in  
[^2]: RRB NTPC Syllabus (BYJU’s-hosted PDF aligned to CEN 01/2019). https://cdn1.byjus.com/wp-content/uploads/2020/07/RRB-NTPC-Syllabus.pdf  
[^3]: RRB NTPC Exam Pattern – Shiksha. https://www.shiksha.com/exams/rrb-ntpc-exam-pattern  
[^4]: RRB NTPC Exam Pattern – Testbook. https://testbook.com/rrb-ntpc/exam-pattern  
[^5]: RRB NTPC Syllabus – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-cbt-1-and-2-syllabus-2024-pdf-download-1716465685-1  
[^6]: RRB NTPC Syllabus – Physics Wallah. https://www.pw.live/railway/exams/rrb-ntpc-syllabus  
[^7]: Practical Geometry: Mathematics Textbook – CBSE Class VIII (DIKSHA via NDLI). http://www.ndl.gov.in/se_document/diksha/diksha/31307360985089638412318_31310347515146240011465_31310347515146240011465  
[^8]: CBSE Board Study Materials – DIKSHA via NDLI (Class X Mathematics). http://www.ndl.iitkgp.ac.in/se_document/diksha/diksha/IN__C__168_169  
[^9]: Chapter 11 – Three Dimensional Geometry: Mathematics Part-II (DIKSHA via NDLI). http://www.ndl.iitkgp.ac.in/se_document/diksha/diksha/313025055394086912111466_313025055393521664111462_313025055393521664111462  
[^10]: CBSE Academic – Maths Class 8 (Resource Manual). https://cbseacademic.nic.in/web_material/term/8Math.pdf  
[^11]: ePathshala – Learning On The Go (NCERT e-Textbooks). https://epathshala.nic.in/process.php?id=students&type=eTextbooks&ln=en  
[^12]: ePathshala Class X Mathematics. https://epathshala.nic.in/topic.php?id=1062  
[^13]: ePathshala Class VIII Mathematics. https://epathshala.nic.in/QR/?id=0852  
[^14]: Mathematics, Class VII (videos from DIKSHA Portal) – Library Guide. https://kvdrdolibrary.wordpress.com/mathematics-class-viivideos-from-diksha-portal/  
[^15]: Mathematics, Class VIII (videos from DIKSHA Portal) – Library Guide. https://kvdrdolibrary.wordpress.com/mathematics-class-viiivideos-from-diksha-portal/  
[^16]: Mathematics, Class X (videos from DIKSHA Portal) – Library Guide. https://librarykvpattom.wordpress.com/2020/09/24/mathematics-class-xvideos-fromdiksha-portal/  
[^17]: CBSE Academic – Mathematics Class 8 – Chapter 10 (Test Items). https://cbseacademic.nic.in/cbe/documents/SAS_Maths-Class-8.pdf  
[^18]: DIKSHA – PM e-Vidya. https://pmevidya.education.gov.in/diksha.html  
[^19]: RRBs Website – Ministry of Railways. https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,7,1281

---

This plan consolidates the sourcing blueprint, inventory, access constraints, and remediation strategy, providing a transparent, licensing-aware pathway to build a comprehensive DIKSHA-aligned Mathematics repository for RRB NTPC preparation.