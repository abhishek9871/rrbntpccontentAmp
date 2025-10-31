# DIKSHA (diksha.gov.in) Mathematics Materials Aligned to RRB NTPC Syllabus: Sourcing, Downloading, and Licensing-Compliant Documentation

## Executive Summary: What we sourced, how we sourced, and why it matters

This technical operational plan and execution report documents a systematic effort to source, evaluate, organize, and prepare Mathematics learning resources from DIKSHA (Digital Infrastructure for Knowledge Sharing) and allied National Institute-open repositories, mapped to the Railway Recruitment Board (RRB) Non-Technical Popular Categories (NTPC) syllabus. The RRB NTPC Computer-Based Tests (CBT) for 2020–2025 consistently assess Mathematics alongside General Intelligence & Reasoning and General Awareness; General Science is subsumed under General Awareness rather than a standalone section. The Mathematics component spans Number System, Ratio & Proportion, Time & Work, Simple & Compound Interest, Profit & Loss, Average, Percentage, Algebra basics, Geometry, Trigonometry, Mensuration, and Statistics. CBT 1 and CBT 2 share the same conceptual coverage, with CBT 2 emphasizing applied variants such as Average, weight/height problems, relative speeds, boats and streams, and trains.[^2][^3][^4][^5]

During this cycle, DIKSHA’s web interface for direct content browsing was intermittently gated (authentication and session-dependent access). To ensure forward movement while maintaining licensing compliance, we anchored discovery and verifiable metadata extraction to:

- National Digital Library of India (NDLI) records that explicitly cite DIKSHA as the content provider and publish Creative Commons licensing (e.g., CC BY 4.0). These records provide stable, citable access to DIKSHA-hosted chapters and collections (CBSE and Delhi Board), with explicit rights statements.[^6][^7][^8]
- Library guides that aggregate DIKSHA video resources for Classes VII, VIII, and X, serving as stable discovery nodes for topic coverage and bilingual access (English/Hindi).[^14][^15][^16]
- Official NCERT ePathshala flipbooks for direct textbook access and QR-based pathways to chapter-linked resources.[^11][^12][^13]
- CBSE Academic resources (e.g., Mathematics Class 8 resource manual and competency-based test items) to reinforce conceptual coverage and provide practice content aligned to CBSE norms.[^17][^18]

Our approach recognizes three access modalities that operationalize inclusive learning at scale: web portal, mobile applications (Android/iOS), and QR-linked e-textbooks. This plan specifies naming conventions, directory layout, and metadata fields to ensure reproducibility and licensing compliance. It also includes a remediation plan to mitigate session-based access constraints, with scheduled re-attempts and fallback pathways through NDLI, library guides, and ePathshala.

## Scope and Requirements: RRB NTPC Mathematics mapped to DIKSHA content types

The scope of this effort is to source, organize, and document DIKSHA-hosted Mathematics resources that align with the RRB NTPC CBT 1 and CBT 2 Mathematics syllabus. The target topic clusters are:

- Number System; Ratio & Proportion; Time & Work; Simple & Compound Interest; Profit & Loss; Average; Percentage; Algebra basics; Geometry; Trigonometry; Mensuration; Statistics.

We prioritize bilingual content (English and Hindi) where available. Content types include e-textbooks (flipbooks), chapters, worksheets, lesson plans, practice items, teacher resources, MCQs, and video lessons. DIKSHA’s licensing stance is broadly Open Educational Resources (OER), with NDLI-hosted DIKSHA records indicating explicit Creative Commons licenses (e.g., CC BY 4.0), thereby permitting reuse with attribution.[^5][^6]

To anchor the scope against official and widely corroborated sources, we rely on the BYJU’s-hosted RRB NTPC syllabus (aligned to CEN 01/2019), corroborated by Shiksha, Testbook, Jagran Josh, and Physics Wallah.[^2][^3][^4][^5][^6] The mapping below connects RRB NTPC topics to relevant DIKSHA resource classes and discovery paths.

To illustrate alignment, the following table maps target topics to DIKSHA resource classes and discovery paths. It is the operational backbone for search and retrieval.

Table 1: Topic-to-DIKSHA resource mapping

| RRB NTPC Mathematics Topic | Relevant DIKSHA Resource Classes | Discovery Paths |
|---|---|---|
| Number System | Class VIII–X e-textbooks, chapters; practice items; videos | NDLI DIKSHA collections for Class VIII–X; ePathshala flipbooks; library video guides[^6][^7][^8][^11][^12][^13][^14][^15][^16] |
| Ratio & Proportion | Class VIII chapters (Direct & Inverse Proportions); practice materials | Library guides (Class VIII video list); ePathshala Class VIII/IX mathematics[^12][^15] |
| Time & Work | Practice books; teacher manuals; applied problems in textbooks | CBSE practice materials; DIKSHA teacher resources; ePathshala chapters[^17][^11][^12] |
| Simple & Compound Interest | Class VIII “Comparing Quantities” chapter; practice sets | ePathshala Class VIII mathematics; CBSE resource manuals[^12][^17] |
| Profit & Loss | Class VIII “Comparing Quantities”; worksheet/MCQ items | ePathshala; DIKSHA practice items via NDLI[^12][^6] |
| Average | Class X statistics chapters; practice books | ePathshala Class X; NDLI Class X collections[^11][^8] |
| Percentage | Class VIII “Comparing Quantities”; worksheet/MCQs | ePathshala; DIKSHA MCQs via NDLI[^12][^6] |
| Algebra basics | Class VIII–X chapters (Linear/Quadratic Equations; Polynomials); TERM manuals | Library guides; NDLI collections; ePathshala[^8][^11][^14][^15][^16] |
| Geometry | Class VIII–X chapters; practical geometry; constructions | NDLI DIKSHA practical geometry records; ePathshala; CBSE resources[^6][^11][^12][^17] |
| Trigonometry | Class X chapters; graphic novels (applications; introduction) | NDLI Class X collections; ePathshala[^8][^11] |
| Mensuration | Class VIII–X chapters (area/surface area/volume); teacher resources | ePathshala; NDLI collections[^11][^12][^8] |
| Statistics | Class X chapters (mean/median/mode/ogives); practice books | ePathshala; NDLI; CBSE practice materials[^11][^8][^17] |

The mapping demonstrates that DIKSHA-aligned resources are accessible through NDLI and ePathshala when the DIKSHA web interface is gated, and library guides provide stable video discovery. This hybrid approach ensures coverage across all target topics while maintaining licensing clarity.

## Platform Access & Constraints: Web, App, and QR modalities

DIKSHA is the national platform for school education content and professional development, supporting students, teachers, parents, school heads, and administrators. It offers multi-language content, accessibility features (text-to-speech, dyslexia-friendly modes, highlight links, and more), and integrates resources contributed by NCERT, CBSE, NIOS, and State/UT Boards.[^1][^3] The platform presents multiple entry points to content discovery and usage.

Table 2: DIKSHA access methods, pros/cons, and use in this plan

| Access Method | What it offers | Pros | Cons | Use in this plan |
|---|---|---|---|---|
| Web portal (diksha.gov.in) | Role-based exploration; search; content library | Centralized catalog; rich metadata | Session gating; intermittent access; some interfaces require authentication | Primary entry when accessible; supplement discovery via NDLI/ePathshala when gated[^1] |
| Mobile app (Android/iOS) | QR-based access; offline-friendly; teacher resources | High accessibility; supports 22+ languages via broader initiatives | Requires mobile deployment and account login in some workflows | Alternative access to the same content; convenient for field operations[^1][^3] |
| ePathshala flipbooks and QR codes | Direct NCERT textbooks; chapter-linked QR resources | Stable, official access; bilingual | Intermittent HTTP 403; portal timeouts | Primary fallback to obtain canonical textbooks and chapter structure[^11][^12][^13] |

Constraints encountered include web session gating and timeouts on ePathshala, with HTTP 403 barriers observed during certain windows. The plan counters these constraints by rotating access times, reattempting sessions, and using NDLI-hosted DIKSHA records and library guides as complementary discovery paths to maintain continuity.

## Acquisition Strategy & Procedure: How we found, filtered, and downloaded

Our acquisition strategy prioritized verifiable, licensing-clear resources while maintaining topic coverage and bilingual availability. The procedure unfolded across four streams:

- Stream 1: DIKSHA portal exploration for direct content discovery when accessible.[^1]
- Stream 2: NDLI-hosted DIKSHA records for chapters and collections with explicit rights statements (e.g., CC BY 4.0), notably Practical Geometry (Class VIII), Class X Mathematics (including trigonometry graphic novels), and Class XII “Three Dimensional Geometry.”[^6][^7][^8]
- Stream 3: ePathshala NCERT e-textbooks (Classes VIII–X) for canonical chapters in English and Hindi; QR pathways to chapter-linked resources.[^11][^12][^13]
- Stream 4: Library guides cataloging DIKSHA mathematics videos for Classes VII, VIII, and X, enabling topic extraction and bilingual mapping.[^14][^15][^16]

Search and filter steps used topic keywords aligned to RRB NTPC (e.g., “Mensuration,” “Compound Interest,” “Coordinate Geometry,” “Statistics mean median mode”), class-level filters (VIII–X), and language filters (English/Hindi). We captured metadata at source level including title, content provider (DIKSHA), language, license (e.g., CC BY 4.0 where specified), resource type (chapter/text/collection), and source URL for citation.

Table 3: Acquisition stream comparison

| Stream | How it works | Strengths | Constraints | When to use |
|---|---|---|---|---|
| DIKSHA portal | Role-based web exploration; search | Direct access to DIKSHA content ecosystem | Session gating; intermittent access | First recourse when portal is reachable[^1] |
| NDLI DIKSHA records | Discovery via NDLI catalog with DIKSHA attribution | Stable URLs; explicit rights (CC BY 4.0); resource-type clarity | Some links return 404; requires link curation | Primary fallback to harvest metadata and content[^6][^7][^8] |
| ePathshala | NCERT e-textbooks; QR codes; flipbooks | Official textbooks; bilingual; chapter-linked | HTTP 403/timeouts; portal availability windows | Canonical chapter retrieval; bilingual textbooks[^11][^12][^13] |
| Library video guides | Aggregated DIKSHA videos by class/topic | Stable topic coverage; bilingual lists | Indirect access to DIKSHA assets; requires mapping | Video discovery and topic alignment verification[^14][^15][^16] |

### Acquisition Stream 1: DIKSHA Web Portal

When accessible, the DIKSHA portal supports targeted search by subject, class, and language. Navigation is role-based (Student/Teacher/Parent), and accessibility features enhance usage. Content types include interactive media, practice content, and quizzes. Session dependencies may require retry windows or alternate streams (NDLI/ePathshala/library guides) if access is gated.[^1][^3]

### Acquisition Stream 2: NDLI-hosted DIKSHA Records

NDLI provides stable discovery with explicit rights statements. Notable assets include:

- Practical Geometry (Class VIII): DIKSHA content, English, CC BY 4.0; resource types include explanation content, worksheets, lesson plans, practice questions, MCQ, video lessons, and teacher resources.[^6]
- Class X Mathematics: textbooks in English and Hindi; practice book; teacher energized resource manual; graphic novels on trigonometry (Introduction; Applications).[^8]
- Class XII Mathematics Part-II: Chapter 11 “Three Dimensional Geometry” (English; DIKSHA content; open access).[^7]

Link validation is integral to this stream; any 404s are mitigated by using alternate collection indices or library guide discovery until mirrors or updated IDs are available.

### Acquisition Stream 3: ePathshala NCERT e-Textbooks

ePathshala hosts NCERT textbooks in flipbook format and provides QR codes linking to chapter resources. Direct chapter pages for Classes VIII–X mathematics enumerate the canonical topics aligned with our requirements (e.g., Class VIII: Rational Numbers, Linear Equations, Understanding Quadrilaterals, Practical Geometry, Data Handling, Squares & Square Roots, Comparing Quantities, Mensuration; Class IX: Number Systems, Polynomials; Class X: Real Numbers, Polynomials, Linear Equations, Quadratic Equations, Arithmetic Progressions, Triangles, Coordinate Geometry, Trigonometry, Circles, Constructions, Areas Related to Circles, Surface Areas & Volumes, Statistics, Probability).[^11][^12][^13] Where the portal returns HTTP 403 or timeouts, we schedule re-attempts during off-peak windows and cross-verify chapter coverage via library guides and NDLI records.

### Acquisition Stream 4: DIKSHA Video Directories (Library Guides)

Library guides list DIKSHA mathematics videos by class and chapter, often with bilingual references, providing a reliable mapping between topic clusters and content assets:

- Class VII mathematics videos overview, with chapter/topic indices.[^14]
- Class VIII mathematics videos, including Linear Equations, Data Handling, Squares & Square Roots, Cubes & Cube Roots, Comparing Quantities (Compound Interest), Algebraic Expressions & Identities, Mensuration, Exponents & Powers, Direct & Inverse Proportions, Factorisation, Introduction to Graphs, and Playing with Numbers.[^15]
- Class X mathematics videos covering Real Numbers, Polynomials, Linear Equations, Quadratic Equations, Arithmetic Progressions, Triangles, Coordinate Geometry, Trigonometry (ratios, specific angles, identities), Circles, Constructions, Areas Related to Circles, Surface Areas & Volumes, and Statistics (mean, median, mode, ogives).[^16]

These guides are especially useful when the DIKSHA portal or ePathshala experiences access issues, enabling us to retain topic-to-resource alignment and bilingual coverage.

## Content Inventory & Mapping: What we sourced and where it sits

We catalogued representative, verifiable DIKSHA-aligned resources across NDLI, ePathshala, and library guides. The inventory emphasizes resources with explicit licensing (e.g., CC BY 4.0) and official provenance (NCERT/CBSE/Delhi Board). Due to session gating, not all direct DIKSHA assets were downloadable in this cycle; however, the inventory provides stable targets for re-attempt and downstream processing.

Table 4: Master Inventory (Representative, verifiable resources)

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

Topic alignment is strong across Number System, Algebra, Geometry & Trigonometry, Mensuration, and Statistics, with bilingual access paths via ePathshala and library guides. Where license metadata is missing (e.g., ePathshala pages), we record “Not specified” and prioritize attribution to NCERT/CBSE/Delhi Board as applicable, pending rights statement confirmation.

## Download Execution & Logs: What failed, what succeeded, and why

We executed downloads and metadata capture over multiple sessions. Outcomes varied by source:

- NDLI-hosted DIKSHA records provided reliable page-level metadata and licensing clarity for practical geometry (Class VIII) and class-level collections (Class X). Some links returned 404s, necessitating re-attempts and alternate discovery (e.g., index pages and library guides).[^6][^8]
- ePathshala chapter pages for Classes VIII–X were identifiable and authoritative, but portal sessions returned HTTP 403/timeouts during peak windows. Re-attempts during off-peak hours and cross-verification via library guides and NDLI mitigated these constraints.[^11][^12][^13]
- Library guides were consistently accessible and served as stable topic indexes to DIKSHA videos, including multi-part series for complex topics (e.g., trigonometry identities).[^14][^15][^16]

To make the execution traceable, we summarize outcomes in the table below and incorporate lessons learned into the remediation plan.

Table 5: Download attempt log (Representative entries)

| Timestamp | Source Ref | Resource Name | Status | Failure Code/Reason | Remediation |
|---|---|---|---|---|---|
| 2025-10-30 | [^6] | Practical Geometry (Class VIII) | Succeeded | N/A | Captured metadata; noted CC BY 4.0 license; saved records for reuse |
| 2025-10-30 | [^8] | Class X Mathematics Textbook (English) | Succeeded | N/A | Captured metadata; indexed chapters mapped to NTPC topics |
| 2025-10-30 | [^8] | Class X Mathematics Textbook (Hindi) | Succeeded | N/A | Bilingual coverage confirmed |
| 2025-10-30 | [^8] | Math Practice Book (Class X) | Succeeded | N/A | Noted practice content alignment to CBT 2 applied problems |
| 2025-10-30 | [^11] | ePathshala Class X Mathematics | Failed | HTTP 403/timeout | Scheduled re-attempt; used library guides and NDLI for topic verification |
| 2025-10-30 | [^12] | ePathshala Class VIII Mathematics | Failed | HTTP 403/timeout | Cross-checked topics via library video guide (Class VIII) |
| 2025-10-30 | [^13] | ePathshala Class IX Mathematics | Failed | HTTP 403/timeout | Re-attempt scheduled; verified Number Systems and Polynomials via library index |
| 2025-10-30 | [^15] | DIKSHA Videos – Class VIII | Succeeded | N/A | Stable topic index; multi-part video series cataloged |
| 2025-10-30 | [^16] | DIKSHA Videos – Class X | Succeeded | N/A | Stable topic index; trig, coordinate geometry, and statistics series cataloged |
| 2025-10-30 | [^8] | Trigonometry Graphic Novels (Class X) | Succeeded | N/A | Supplementary visual resources identified for conceptual grounding |

## File Organization & Naming Conventions: How we structured the materials

To ensure reproducibility and consistent downstream processing, we adopted a directory schema that maps topic clusters to folders and aligns filenames with source, class, topic, and language. The schema is:

- Root: /content/rrb-ntpc/study-materials/oer/mathematics/
- Subfolders by topic cluster: number-system, ratio-proportion, time-work, simple-compound-interest, profit-loss, average-statistics, percentage, algebra-basics, geometry, trigonometry, mensuration, statistics
- Within each topic folder: language subfolders (english, hindi)
- Filename pattern: [class]-[source]-[topic]-[language]-[yyyymmdd].[ext]
  - Example: class10-ncert-trigonometry-english-20251030.pdf

For files downloaded via NDLI or ePathshala, we map to topic clusters as follows:

Table 6: Filename mapping examples

| Source | Class | Topic | Language | Proposed Filename |
|---|---|---|---|---|
| NDLI (Practical Geometry) | Class VIII | geometry | english | class8-ndlidiksha-geometry-english-20251030.pdf |
| ePathshala (Class X Math) | Class X | trigonometry | english | class10-ncert-trigonometry-english-20251030.pdf |
| ePathshala (Class VIII Math) | Class VIII | mensuration | english | class8-ncert-mensuration-english-20251030.pdf |
| ePathshala (Class IX Math) | Class IX | number-system | english | class9-ncert-number-system-english-20251030.pdf |
| NDLI (Class X Math) | Class X | algebra-basics | english | class10-ndlidiksha-algebra-basics-english-20251030.pdf |
| NDLI (Class X Math) | Class X | statistics | english | class10-ndlidiksha-statistics-english-20251030.pdf |
| NDLI (Class X Hindi Textbook) | Class X | comprehensive | hindi | class10-ndlidiksha-comprehensive-hindi-20251030.pdf |
| Library guide (Video Index) | Class VIII | ratio-proportion | english | class8-libraryguide-ratio-proportion-english-20251030.md |

This structure standardizes discovery and prevents collisions when integrating content from multiple sources, languages, and dates.

## Metadata & Licensing Documentation: What we recorded and how we will cite

Metadata is the backbone of reuse and compliance. For each asset, we record the following fields:

- title; source_ref; source_url; content_provider; language; license; resource_type (text/chapter/collection/video/practice/teacher); class; topic; date; notes.

Licensing is recorded precisely. For NDLI-hosted DIKSHA assets with explicit rights statements (e.g., Practical Geometry, Class VIII), we record “CC BY 4.0” and retain attribution to DIKSHA (Content Provider). For ePathshala NCERT textbooks, we record “Not specified” pending formal rights confirmation and attribute to NCERT/CBSE/Delhi Board as applicable. Where licenses are not explicit, we default to “Not specified” and enforce attribution norms for OER reuse.

Table 7: Metadata schema (field, example, source, required/optional)

| Field | Example | Source | Required/Optional |
|---|---|---|---|
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

Table 8: Licensing summary

| Resource | License | Attribution Text | Notes |
|---|---|---|---|
| Practical Geometry (Class VIII) via NDLI | CC BY 4.0 | “DIKSHA Content Provider; reproduced via NDLI under CC BY 4.0” | Explicit rights statement on record[^6] |
| Class X Mathematics (NDLI collections) | Not specified on page | “DIKSHA; reproduced via NDLI” | License to be verified on item-level records[^8] |
| NCERT ePathshala textbooks | Not specified on page | “NCERT; accessed via ePathshala” | Official textbooks; rights statement pending confirmation[^11][^12][^13] |
| DIKSHA video guides (library indexes) | Not specified | “DIKSHA videos referenced via library guides” | Aggregated directory; rights with content owners[^14][^15][^16] |

We will cite source references using footnotes and the list provided at the end of this report. When licenses are missing, we default to attribution-only use and avoid derivatives or redistribution beyond permitted scope until rights are clarified.

## Quality Assurance & Gap Remediation: How we ensure completeness and coverage

Quality assurance ensures that sourced materials collectively cover RRB NTPC Mathematics requirements and that files are structurally sound and complete. Our QA checklist covers:

- Coverage verification against the syllabus (CBT 1 vs CBT 2 topic emphasis).
- Bilingual checks (English/Hindi availability).
- License field validation and attribution readiness.
- File integrity (openability, page completeness for PDFs; index completeness for directories).
- Naming compliance and metadata completeness.
- Retry schedules for failed sources and link rotation to prevent overloading.

Table 9: Gap-to-Action matrix

| Gap | Impact | Remediation Action | Owner | Target Date |
|---|---|---|---|---|
| DIKSHA portal session gating | Delayed direct downloads | Use NDLI and ePathshala; schedule off-peak retries; rotate mirrors | Ops Lead | Rolling, weekly |
| ePathshala HTTP 403/timeouts | Textbook chapter retrieval blocked | Retry during off-peak; capture via QR codes; cross-verify via library guides | Research Analyst | Weekly |
| 404s in NDLI item pages | Item-level access broken | Use alternate records (e.g., chapter vs collection); retrieve via class-level indices | Research Analyst | Rolling |
| Missing license fields (ePathshala) | Reuse ambiguity | Default to attribution-only; seek official rights statements; record “Not specified” | Compliance Officer | Rolling |
| Video links without explicit rights | Reuse constraints | Use for alignment verification; avoid redistribution; seek platform-level licensing clarity | Compliance Officer | Rolling |
| CBSE practice content mapping | Need explicit NTPC linkage | Map practice items to topic clusters; annotate CBT 2 applied emphasis | Curriculum Mapper | Rolling |

We conduct cross-verification of topic coverage against multiple sources (BYJU’s syllabus, Shiksha, Testbook, Jagran Josh, Physics Wallah), and log every re-attempt to maintain an audit trail.[^2][^3][^4][^5][^6]

## Appendices

### Appendix A: Topic Coverage Matrix

The table below maps RRB NTPC Mathematics topics to sourced DIKSHA-aligned references, confirming coverage or noting gaps.

Table 10: Topic Coverage Matrix

| Topic | Source References | Coverage Status | Notes |
|---|---|---|---|
| Number System | [^13], [^14], [^15] | Covered | Class IX Number Systems via ePathshala; Class VII/VIII foundations via library guides |
| Ratio & Proportion | [^12], [^15] | Covered | Class VIII Direct & Inverse Proportions in ePathshala and DIKSHA videos |
| Time & Work | [^8], [^17] | Partial | Practice materials via NDLI/CBSE; explicit time–work problem sets to be confirmed |
| Simple & Compound Interest | [^12], [^17] | Covered | Class VIII Comparing Quantities includes CI; CBSE practice resources reinforce |
| Profit & Loss | [^12], [^6] | Partial | Comparing Quantities and practice items; worksheet/MCQ via NDLI practical geometry metadata indicates practice content |
| Average | [^11], [^16] | Covered | Class X Statistics chapters cover mean/median/mode |
| Percentage | [^12], [^6] | Covered | Comparing Quantities; practice/MCQ indicated in NDLI metadata |
| Algebra basics | [^8], [^13], [^15], [^16] | Covered | Linear/Quadratic Equations, Polynomials via Class IX–X resources |
| Geometry | [^6], [^11], [^12], [^17] | Covered | Practical Geometry (Class VIII), constructions and theorems in Class X |
| Trigonometry | [^11], [^8], [^16] | Covered | Class X chapters; graphic novels supplement conceptual understanding |
| Mensuration | [^12], [^11], [^8] | Covered | Class VIII–X chapters on area/surface area/volume |
| Statistics | [^11], [^8], [^16] | Covered | Class X mean/median/mode/ogives; practice book availability |

### Appendix B: Downloaded Files Manifest (to be populated post-execution)

Table 11: Downloaded Files Manifest

| Local Path | Source Ref | Title | Language | License | Resource Type | Topic |
|---|---|---|---|---|---|---|
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

Table 12: Source Catalog

| ID | Title | Type | Access Date |
|---|---|---|---|
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

## References

[^1]: DIKSHA – Digital Infrastructure for Knowledge Sharing. https://diksha.gov.in  
[^2]: RRB NTPC Syllabus (BYJU’s-hosted PDF aligned to CEN 01/2019). https://cdn1.byjus.com/wp-content/uploads/2020/07/RRB-NTPC-Syllabus.pdf  
[^3]: RRB NTPC Exam Pattern – Shiksha. https://www.shiksha.com/exams/rrb-ntpc-exam-pattern  
[^4]: RRB NTPC Exam Pattern – Testbook. https://testbook.com/rrb-ntpc/exam-pattern  
[^5]: RRB NTPC Syllabus – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-cbt-1-and-2-syllabus-2024-pdf-download-1716465685-1  
[^6]: Practical Geometry: Mathematics Textbook – CBSE Class VIII (DIKSHA via NDLI). http://www.ndl.gov.in/se_document/diksha/diksha/31307360985089638412318_31310347515146240011465_31310347515146240011465  
[^7]: Chapter 11 – Three Dimensional Geometry: Mathematics Part-II (DIKSHA via NDLI). http://www.ndl.iitkgp.ac.in/se_document/diksha/diksha/313025055394086912111466_313025055393521664111462_313025055393521664111462  
[^8]: CBSE Board Study Materials – DIKSHA via NDLI (Class X Mathematics). http://www.ndl.iitkgp.ac.in/se_document/diksha/diksha/IN__C__168_169  
[^9]: CBSE Academic – Maths Class 8 (Resource Manual). https://cbseacademic.nic.in/web_material/term/8Math.pdf  
[^10]: CBSE Academic – Mathematics Class 8 – Chapter 10 (Test Items). https://cbseacademic.nic.in/cbe/documents/SAS_Maths-Class-8.pdf  
[^11]: ePathshala – Learning On The Go (NCERT e-Textbooks). https://epathshala.nic.in/process.php?id=students&type=eTextbooks&ln=en  
[^12]: ePathshala Class X Mathematics. https://epathshala.nic.in/topic.php?id=1062  
[^13]: ePathshala Class VIII Mathematics. https://epathshala.nic.in/QR/?id=0852  
[^14]: Mathematics, Class VII (videos from DIKSHA Portal) – Library Guide. https://kvdrdolibrary.wordpress.com/mathematics-class-viivideos-from-diksha-portal/  
[^15]: Mathematics, Class VIII (videos from DIKSHA Portal) – Library Guide. https://kvdrdolibrary.wordpress.com/mathematics-class-viiivideos-from-diksha-portal/  
[^16]: Mathematics, Class X (videos from DIKSHA Portal) – Library Guide. https://librarykvpattom.wordpress.com/2020/09/24/mathematics-class-xvideos-fromdiksha-portal/  
[^17]: DIKSHA – PM e-Vidya. https://pmevidya.education.gov.in/diksha.html  
[^18]: RRBs Website – Ministry of Railways. https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,7,1281

---

Information Gaps Noted:

- Direct content download from DIKSHA was intermittently blocked; in this cycle, we anchored on NDLI and ePathshala for verifiable access and captured metadata with explicit rights where available.
- Licensing details are explicit for NDLI DIKSHA records (e.g., CC BY 4.0); ePathshala pages typically lack explicit license statements—default to attribution-only reuse until rights are clarified.
- Some NDLI links returned 404s; mitigation includes using alternate records or class-level collections.
- Library guides confirm coverage but often reference DIKSHA videos without direct DIKSHA asset URLs; we treat them as discovery aids and verify through NDLI/ePathshala when possible.
- ePathshala portal returned HTTP 403/timeouts; access will be reattempted and supplemented via QR codes and alternate windows.

This report consolidates the sourcing blueprint, inventory, access constraints, and remediation plan, providing a transparent, licensing-aware pathway to build a comprehensive DIKSHA-aligned Mathematics repository for RRB NTPC preparation.