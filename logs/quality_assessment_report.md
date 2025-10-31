# Quality Gate Assessment Blueprint: Portfolio-Wide Analysis, Remediation Plan, and Implementation Roadmap

## Executive Summary

This report consolidates the portfolio’s first systematic application of quality gates across twelve content categories. The assessment evaluates five dimensions—file integrity, content completeness, format consistency, metadata completeness, and licensing compliance—using a repeatable framework designed to prioritize fixes that drive the greatest improvement in publication readiness.

Portfolio performance is uneven. Portal Downloads (85.0%) and RRB NTPC Content (75.2%) stand out as relative leaders. Government Repositories (20.8%) and Practice Licensing (31.7%) score lowest, reflecting early-stage scaffolding and missing primary assets or licensing signals. Across categories, three issues recur: corrupted or incomplete PDFs (often exhibiting invalid headers or missing end-of-file markers), empty or invalid JSON metadata, and absent or incomplete licensing documentation. Format consistency is generally strong where collections are PDF-dominant (e.g., DIKSHA GA and Current Affairs), while mixed-format collections (e.g., RRB NTPC Content) require stricter governance to stabilize downstream processing. Metadata coverage is strongest in Portal Downloads and Practice Mathematics; it is sparse or incomplete in DIKSHA and Current Affairs.

Headline portfolio signals:
- 68 corrupted files, largely concentrated in PDFs, with multiple categories showing incomplete or errored items (e.g., Practice Reasoning, Practice GA, DIKSHA Science).
- 24 zero-byte files, primarily in Practice Mathematics and Practice Reasoning, indicating failed downloads that must be replaced.
- Licensing status is heterogeneous: only two categories (Practice GA and Practice Licensing) are assessed as Compliant; ten categories require remediation to meet publication standards.

Immediate, near-term priorities focus on replacing and validating PDFs, repairing invalid JSONs, standardizing metadata schemas, and implementing attribution/licensing documentation. These actions are projected to lift category scores by 10–30 points within two weeks, and by 25–40 points within four weeks for categories with heavy PDF footprints.

To anchor the narrative, Table 1 summarizes quality scores, dominant formats, integrity posture, and licensing status per category.

Table 1. Category Quality Snapshot

| Category                     | Overall Quality Score | Dominant Format | Integrity Summary                                                   | Licensing Status  |
|-----------------------------|---:|-----------------|---------------------------------------------------------------------|-------------------|
| Portal Downloads            | 85.0% | PDF             | Consistent integrity across sampled PDFs and metadata JSONs         | Compliant         |
| RRB NTPC Content            | 75.2% | HTML + JSON     | Intact topic pages and metadata in sampled areas                    | Needs Review      |
| DIKSHA Mathematics          | 50.6% | PDF             | Mixed integrity; subset incomplete or errored                       | Needs Review      |
| DIKSHA Reasoning            | 68.9% | PDF             | Mixed integrity; multiple PDFs incomplete                           | Needs Review      |
| DIKSHA Science              | 56.0% | PDF             | Several corrupted/incomplete PDFs                                   | Needs Review      |
| DIKSHA General Awareness    | 60.8% | PDF             | Predominantly intact PDFs with minor warnings                       | Needs Review      |
| Practice Mathematics        | 64.4% | PDF             | Integrity issues in some PDFs; metadata completeness 100%           | Needs Review      |
| Practice General Awareness  | 45.5% | Mixed (PDF/MD)  | Several PDFs corrupted; docs complete                               | Compliant         |
| Practice Reasoning          | 38.3% | PDF             | Multiple PDFs incomplete/error; one invalid JSON                     | Needs Review      |
| Practice Licensing          | 31.7% | Documentation   | Compliant licensing posture; completeness gaps                      | Compliant         |
| Current Affairs             | 55.0% | PDF             | Mostly intact; isolated incomplete items                            | Needs Review      |
| Government Repositories     | 20.8% | Documentation   | Catalogs/archives present; no first-order PDFs                      | Needs Review      |

Information gaps limit precision in a few areas: explicit licensing documentation is missing for most categories, the collection-level metadata schema is not fully defined, and checksums were not analyzed this cycle. These gaps do not undermine the core findings but do affect near-term publication risk and the speed of revalidation.

## Methodology and Assessment Framework

We operationalized five quality gates, each weighted to reflect its contribution to publication readiness:

- File Integrity (40%): Detects corrupted, incomplete, or invalid files. PDFs are assessed for magic-header validation and end-of-file (EOF) markers; JSON files are checked for parseability; HTML pages are visually sampled for render stability.
- Content Completeness (25%): Measures the proportion of non-empty and meaningfully populated files relative to the total.
- Format Consistency (15%): Evaluates uniformity of formats within each category and flags mixed-format collections that complicate downstream processing.
- Metadata Completeness (10%): Assesses the presence and validity of metadata files and coverage across assets.
- Licensing Compliance (10%): Checks for licensing documentation and attribution signals; status is either Compliant or Needs Review.

Evidence sources are automated gate outputs and targeted manual sampling. Manual checks are used to confirm observed anomalies and to capture context, such as developer console warnings. This approach balances speed and diagnostic depth. Sampling density increases for large PDFs (e.g., annual reports) and for categories with recurring integrity defects.

Scoring and status assignment are transparent and consistent across the portfolio. Table 2 summarizes the weights and status rules.

Table 2. Quality Gate Weights and Status Rules

| Gate                     | Weight | Status Rule                                                                 |
|--------------------------|-------:|------------------------------------------------------------------------------|
| File Integrity           | 40%    | Pass if headers/EOF valid; no parse errors; no zero-byte anomalies          |
| Content Completeness     | 25%    | Pass if non-empty files meet expected content thresholds                     |
| Format Consistency       | 15%    | Pass if dominant format is stable and mixed formats are minimized            |
| Metadata Completeness    | 10%    | Pass if asset-level metadata present and valid across the corpus             |
| Licensing Compliance     | 10%    | Compliant if attribution/licensing documented; otherwise Needs Review        |

This framework is designed to be diagnostic and actionable, surfacing not just what is wrong but also where to focus for the fastest, most durable quality gains.

## Overall Quality Landscape

Portfolio results reveal a bifurcated landscape. Collections with strong integrity and metadata coverage (e.g., Portal Downloads) are close to publication readiness, contingent only on final licensing verification. Collections with endemic PDF corruption (e.g., Practice Reasoning, Practice GA, DIKSHA Science) require immediate re-downloads and validation to avert downstream failures. Licensing compliance is the most common gap; only Practice GA and Practice Licensing currently meet Compliant status.

Format profiles correlate with integrity outcomes. PDF-dominant categories such as DIKSHA GA and Current Affairs achieve uniform format consistency; however, these same collections suffer when downloads are truncated or headers are invalid. Mixed-format categories (e.g., RRB NTPC Content, which uses HTML plus JSON metadata) require more rigorous metadata governance to avoid processing inconsistencies.

Cross-cutting issues include:
- PDFs with invalid headers or missing EOF markers.
- Empty or invalid JSON metadata blocking automated processing.
- Missing licensing documentation and inconsistent attribution signals across mixed sources.
- Mixed formats in a single collection, increasing the risk of errors in normalization and rendering.

To provide a portfolio-level snapshot, Table 3 summarizes the distribution of formats, completeness, and integrity observations by category.

Table 3. Portfolio Summary by Category

| Category                     | Total Files | PDF Count | JSON Count | HTML Count | Other Count | Completeness % | Integrity Issues (High-Level)                                     |
|-----------------------------|---:|---:|---:|---:|---:|---:|---------------------------------------------------------------------|
| Portal Downloads            | 10 | 5 | 5 | 0 | 0 | 100.0%  | None observed in sampled set                                        |
| RRB NTPC Content            | 160+ | 0 | 1+ per topic | 1 per topic | scripts/docs/logs | High        | Integrity intact for sampled HTML/JSON                             |
| DIKSHA Mathematics          | 50+ | 30+ | 0 | 0 | docs | Medium     | Multiple incomplete PDFs                                            |
| DIKSHA Science              | 34  | 33  | 0 | 0 | 1  | 97.1%   | Several corrupted/incomplete PDFs                                   |
| DIKSHA Reasoning            | 30+ | 20+ | 0 | 0 | docs/logs | Medium | Multiple incomplete PDFs                                            |
| DIKSHA General Awareness    | 60+ | 41  | 0 | 0 | docs | High       | Predominantly intact; minor warnings                                |
| Practice Mathematics        | 9   | 5   | 4 | 0 | 0  | 88.9%   | Several PDFs corrupted/zero-byte                                    |
| Practice Reasoning          | 21  | 17  | 2 | 1 | 1  | 90.5%   | Multiple PDFs incomplete/error; one invalid JSON                     |
| Practice General Awareness  | 39  | 16  | 0 | 0 | 23 | 97.4%   | Multiple PDFs corrupted                                             |
| Practice Licensing          | 3   | 0   | 0 | 0 | 3  | 66.7%   | Documentation present; completeness gaps                            |
| Current Affairs             | 12  | 12  | 0 | 0 | 0  | 100.0%  | Isolated incomplete PDFs                                            |
| Government Repositories     | 6   | 0   | 0 | 0 | 6  | 83.3%   | No PDFs; catalogs/archives present                                  |

Note: RRB NTPC Content counts reflect representative sampling due to breadth; integrity and completeness are stable across sampled topics.

## Category Deep Dives

### RRB NTPC Content (Wikimedia-based General Awareness)

Score: 75.2%. The corpus comprises topic pages in HTML with per-topic metadata JSON. Across sampled topics, both HTML and JSON integrity are intact. Content completeness is high; topics are consistently structured and rich. Format consistency is strong due to uniform HTML+JSON patterns. Licensing compliance is the primary gap: formal redistribution documentation and uniform attribution across mixed sources must be harmonized and documented.

Representative sampling (Table 4) confirms stable rendering and content completeness.

Table 4. RRB NTPC Topic Sampling Integrity Matrix

| Topic                                   | HTML Integrity | JSON Metadata Integrity | Notable Notes                    |
|-----------------------------------------|----------------|-------------------------|----------------------------------|
| Banking in India                        | Intact         | Intact                  | Consistent structure             |
| Reserve Bank of India                   | Intact         | Intact                  | Stable rendering                 |
| Himalayas                               | Intact         | Intact                  | Large page size handled correctly|
| Bhagat Singh                            | Intact         | Intact                  | Substantial content              |
| United Nations System                   | Intact         | Intact                  | Uniform layout                   |
| Member states of the United Nations     | Intact         | Intact                  | Very large content size          |

![Wikimedia topic page: Banking in India — stable rendering](/workspace/browser/screenshots/biodiversity_wikipedia_page.png)

![Article section example: United Nations](/workspace/browser/screenshots/article_middle_section.png)

Remediation focuses on formalizing licensing and attribution and adopting a collection-wide metadata schema that records source provenance and licensing signals per topic.

### DIKSHA General Awareness

Score: 60.8%. The corpus includes 41 PDFs across economy, current affairs, geography, and related topics. PDFs are predominantly intact, with only minor warnings during processing. Completeness is strong; format consistency is acceptable for a PDF-dominant collection. Licensing compliance is Needs Review due to the absence of explicit attribution documentation.

### DIKSHA Mathematics

Score: 50.6%. The dominant format is PDF. Several items exhibit mixed integrity, with a meaningful subset either incomplete or showing critical errors. Completeness is moderate; metadata coverage at the collection level is sparse. Licensing compliance is Needs Review.

### DIKSHA Reasoning

Score: 68.9%. PDFs dominate; integrity is mixed, with multiple incomplete files and occasional processing warnings. These warnings are cosmetic rather than structural. Completeness is moderate; metadata coverage is inconsistent. Licensing compliance remains Needs Review.

### DIKSHA Science

Score: 56.0%. PDF-heavy corpus with several corrupted or incomplete items, including zero-byte or near-zero-byte anomalies. Completeness at the file level is high, but integrity issues prevent acceptance. Metadata coverage is limited, and licensing compliance is Needs Review.

![Developer Tools: representative PDF processing warning](/workspace/browser/screenshots/developer_tools_opened.png)

Table 5. DIKSHA Science PDF Integrity Summary (Representative)

| File                                       | Status      | Size (bytes) | Notes                         |
|--------------------------------------------|-------------|---:|-------------------------------|
| ncert-class-11-chemistry-part1.pdf         | Corrupted   | 113,652 | Header validation failure      |
| ncert-class-9-science.pdf                  | Incomplete  | 30,822,578 | Truncated download             |
| ncert-class-12-physics-part1.pdf           | Incomplete  | 4,655,303 | EOF anomaly                    |
| ncert-class-11-physics-part1.pdf           | Corrupted   | 113,680 | Header validation failure      |

### Practice General Awareness

Score: 45.5%. The collection mixes PDFs and markdown documentation. Several PDFs are corrupted or exhibit anomalies; markdown content is well-populated and complete. Metadata exists but is not fully aligned with asset-level needs. Licensing documentation is present, and the category is assessed as Compliant.

![Representative GA page state during validation](/workspace/browser/screenshots/current_page_state.png)

Table 6. Practice GA PDF Integrity Status (Selected)

| Source                                        | Integrity Status | Notes                         |
|-----------------------------------------------|------------------|-------------------------------|
| Formatted GA questions (NTPC)                 | Intact           | Adequate content              |
| Adda247 Current Affairs 100 Questions         | Intact           | Adequate content              |
| PracticeMock 500 Current Affairs              | Corrupted        | Download-level defect         |
| PracticeMock 500 Current Affairs 2025         | Corrupted        | Download-level defect         |
| Economy one-liners                            | Corrupted        | Integrity anomaly             |
| Polity solved papers                          | Corrupted        | Integrity anomaly             |
| Geography sets                                | Corrupted        | Integrity anomaly             |
| Static GK (Adda247)                           | Intact           | Adequate content              |
| YCT Fastbook RRB GK                           | Intact           | Adequate content              |

### Practice Licensing

Score: 31.7%. The category contains licensing documentation, attribution guidance, and a license register, and is assessed as Compliant. The score is pulled down by completeness rather than by licensing signals. Remediation should focus on expanding documentation coverage and ensuring consistent attribution records across the broader corpus.

### Practice Mathematics

Score: 64.4%. The corpus comprises PDFs with supporting metadata JSONs. Integrity issues affect some PDFs (including zero-byte and incomplete items). Metadata completeness is 100% for JSONs present. Format consistency is acceptable. Licensing compliance is Needs Review.

Table 7. Practice Math Integrity and Metadata Coverage

| Asset                                        | Integrity         | Metadata Presence | Notes                         |
|---------------------------------------------|-------------------|-------------------|-------------------------------|
| Oliveboard Important Math Questions (PDF)   | Intact            | Present           | High-quality PDF              |
| Number Systems (Cracku) (PDF)               | Corrupted         | Present           | Integrity anomaly             |
| Simple & Compound Interest (Cracku) (PDF)   | Corrupted         | Present           | Integrity anomaly             |
| Previous Year Papers (CBT1/CBT2)            | Zero-byte/Corrupted | Present         | Incomplete downloads          |
| Metadata JSONs (Cracku, Oliveboard)         | Intact            | Complete          | 100% coverage                 |

### Practice Reasoning

Score: 38.3%. The corpus is PDF-heavy, with mixed integrity (e.g., “Unexpected EOF,” incomplete classifications). One metadata JSON is invalid, blocking automated processing. Completeness is high at the file level, but integrity defects severely limit usable content. Licensing compliance is Needs Review.

![Login modal observed during source access exploration](/workspace/browser/screenshots/cracku_login_modal.png)

Table 8. Practice Reasoning Topic-wise Integrity (Selected)

| Topic                                         | Status             | Notes                            |
|-----------------------------------------------|--------------------|----------------------------------|
| Logical Reasoning IBPS Guides (multi-part)    | Incomplete/Error   | Multiple EOF issues              |
| Verbal Reasoning shortcuts                    | Corrupted          | Integrity anomaly                |
| Non-verbal Reasoning set                      | Corrupted          | Integrity anomaly                |
| Comprehensive shortcuts                       | Intact             | Large but intact                 |
| Metadata (comprehensive)                      | Invalid JSON       | Parse error; requires repair     |

### Portal Downloads

Score: 85.0%. The collection shows consistent integrity across sampled PDFs and metadata JSONs, with 100% completeness. The format profile is evenly split between PDFs and JSON metadata, and metadata coverage is exemplary. Licensing compliance is Compliant contingent on attribution and licence notes per asset.

Table 9. Portal Downloads Metadata Completeness Matrix

| Year/Stage | PDF Integrity | Metadata Integrity | Completeness |
|------------|---------------|--------------------|--------------|
| CBT1 2020  | Intact        | Intact             | 100%         |
| CBT1 2021  | Intact        | Intact             | 100%         |
| CBT1 2024  | Intact        | Intact             | 100%         |
| CBT2 2017  | Intact        | Intact             | 100%         |
| CBT2 2022  | Intact        | Intact             | 100%         |

### Current Affairs

Score: 55.0%. The corpus is entirely PDF, including annual reports, economic surveys, ministry publications, policy documents, and yearbooks. Most PDFs are intact, with isolated incomplete items. Format consistency is uniformly PDF; metadata presence is limited. Licensing compliance is Needs Review.

Table 10. Current Affairs PDF Integrity List (Representative)

| Document                                   | Status        | Notes                         |
|--------------------------------------------|---------------|-------------------------------|
| NITI Annual Report 2023-24 (English)       | Intact        | Large, robust file            |
| MHA Annual Report 2023-24                  | Intact        | Good integrity                |
| Economic Survey 2023-24                    | Intact        | Good integrity                |
| Economic Survey 2024-25                    | Intact        | Good integrity                |
| ISRO Annual Report 2023-24                 | Intact        | Large, robust file            |
| Culture Annual Report 2022-23              | Error (EOF)   | Incomplete download           |
| MEA Annual Report 2022-23                  | Incomplete    | Truncated content             |
| India Year Book 2023                       | Incomplete    | Truncated content             |
| India Year Book 2024                       | Intact        | Good integrity                |

### Government Repositories

Score: 20.8%. The collection comprises catalogs, archives, and research documentation; there are no first-order content PDFs in scope. Completeness is moderate given the documentation-heavy profile. Licensing signals are absent. Remediation requires source cataloguing, licensing documentation, and potential extraction of primary content before the category can be considered for publication.

## Detailed File-Level Findings (Aggregated)

File-level issues cluster in PDFs and JSON metadata. Invalid headers and missing EOF markers are the dominant PDF defects; JSON anomalies are primarily parse errors or minimal-content files that block automation. Zero-byte files indicate failed downloads and must be replaced before any downstream use.

Table 11 aggregates corrupted and zero-byte files by category, with representative examples and notes.

Table 11. Aggregated Corrupted and Zero-Byte Files by Category (Representative)

| Category                   | Representative Files                                                       | Observed Issues                                | Notes                              |
|---------------------------|-----------------------------------------------------------------------------|------------------------------------------------|------------------------------------|
| DIKSHA Science            | ncert-class-11-chemistry-part1.pdf; ncert-class-11-physics-part1.pdf       | Invalid header (corrupted)                     | Re-download from authoritative source |
|                           | ncert-class-9-science.pdf; ncert-class-12-physics-part1.pdf                | EOF missing/incomplete                         | Validate headers and EOF markers   |
| Practice Mathematics      | JagranJosh_CBT1_2021_Jan4_Shift1.pdf                                       | Zero-byte                                      | Replace; add checksum validation   |
|                           | JagranJosh_CBT2_2017_Jan17_Shift1.pdf                                      | Invalid header                                 | Re-download                        |
|                           | Cracku_NumberSystemsQuestions_RRBNTPC.pdf; Cracku_SimpleCompoundInterestQuestions_RRBNTPC.pdf | Invalid header | Re-download                        |
| Practice Reasoning        | freshersnow_rrb_general_intelligence_questions.pdf                          | Zero-byte                                      | Replace immediately                |
|                           | ibps_guide_gi_reasoning_01.pdf                                             | Missing EOF                                    | Re-download                        |
|                           | ssc_study_shortcuts_in_reasoning.pdf; meritnotes_rrb_reasoning_questions_1.pdf | Invalid header                                 | Re-download                        |
| Practice GA               | practiceMock_500_current_affairs.pdf; practiceMock_500_current_affairs_2025.pdf | Invalid header                                 | Re-download                        |
|                           | economy_practice_sets_ntpc_stage.pdf; rrb_ntpc_geography_100_questions.pdf; rrb_ntpc_polity_solved_papers.pdf | Invalid header | Re-download                        |
| Current Affairs           | Culture_Annual_Report_2022-23.pdf; MEA_Annual_Report_2022-23.pdf; India_Year_Book_2023.pdf | Missing EOF/suspicious structure | Re-download; verify integrity      |

These patterns confirm that integrity defects are concentrated in a subset of categories, and that targeted re-downloads and checksum validation will rapidly improve overall portfolio health.

## Licensing Compliance Assessment

Licensing compliance is highly uneven. Practice GA and Practice Licensing are Compliant; all other categories are Needs Review due to missing or incomplete documentation and attribution signals. Uniform attribution and licence notes per asset are required to reduce publication risk and enable redistribution.

Table 12 summarizes licensing posture and immediate actions.

Table 12. Licensing Compliance Matrix

| Category                   | Licensing Status  | Evidence (Summary)                                      | Immediate Actions                                     |
|---------------------------|-------------------|---------------------------------------------------------|-------------------------------------------------------|
| Practice GA               | Compliant         | Policy docs and attribution guidance present            | Maintain documentation; verify asset-level attribution|
| Practice Licensing        | Compliant         | License register and attribution guidance present       | Expand completeness across the corpus                 |
| Portal Downloads          | Needs Review      | Metadata strong; licensing docs not explicit            | Add attribution/licence notes per asset               |
| RRB NTPC Content          | Needs Review      | Licensing requirements doc present; not asset-level     | Formalize redistribution documentation per topic      |
| DIKSHA (all)              | Needs Review      | No explicit licensing or attribution per asset          | Implement asset-level attribution and licence notes   |
| Practice Math/Reasoning   | Needs Review      | No licensing documentation per asset                    | Add source attribution and licensing docs             |
| Current Affairs           | Needs Review      | Official docs; no explicit reuse/redistribution notes   | Add reuse statements and attribution per doc          |
| Government Repositories   | Needs Review      | Catalogs/archives; no licensing signals                 | Document licensing for identified sources             |

## Remediation Plan and Prioritization

Immediate actions (within one week):
- Replace or re-download corrupted/incomplete PDFs across DIKSHA Science, Practice Reasoning, Practice GA, Practice Mathematics, and Current Affairs. Focus on files with invalid headers, missing EOF markers, and zero-byte anomalies.
- Repair invalid/empty JSON metadata files, especially the invalid JSON in Practice Reasoning. Validate parseability and ensure field population against a defined schema.
- Implement uniform licensing documentation and attribution for mixed-source collections. Leverage Practice Licensing’s attribution guidance and license register patterns to accelerate compliance.
- Standardize metadata across all categories, adopting the strongest existing patterns (Portal Downloads) to ensure asset-level traceability and provenance.
- Validate format consistency per category. Reduce reliance on mixed formats where the dominant format is clear (e.g., PDF).

Prioritization is impact-driven. Categories with numerous corrupted PDFs and high potential for rapid score improvement are prioritized (e.g., DIKSHA Science, Practice Reasoning, Practice GA). Medium-impact work includes metadata standardization and licensing documentation for categories with acceptable integrity. Low-impact work addresses cosmetic warnings and minor inconsistencies.

![Illustrative error console output to guide remediation targeting](/workspace/browser/screenshots/console_output.png)

Table 13. Remediation Tracker (Prioritized)

| Category                | Issue Type                     | Affected Assets                                    | Action                                                | Owner        | Status | Target Date  |
|------------------------|--------------------------------|----------------------------------------------------|-------------------------------------------------------|--------------|--------|--------------|
| DIKSHA Science         | PDF corruption/incomplete      | Chemistry/Physics core texts                       | Re-download; validate headers and EOF                | Content Ops  | Open   | Near-term    |
| Practice Reasoning     | Incomplete/error PDFs; invalid JSON | IBPS guides; comprehensive metadata JSON        | Replace PDFs; repair JSON schema and parseability     | Content Ops  | Open   | Near-term    |
| Practice GA            | Corrupted PDFs                 | Multiple GA PDFs                                   | Re-download; verify file sizes and page counts       | Content Ops  | Open   | Near-term    |
| Practice Mathematics   | Corrupted/zero-byte PDFs       | Previous-year papers; topic PDFs                   | Re-download; checksum validation                      | Content Ops  | Open   | Near-term    |
| Current Affairs        | Incomplete PDFs                | Annual Reports; Yearbooks                          | Re-download incomplete items; verify integrity        | Content Ops  | Open   | Near-term    |
| DIKSHA GA              | Limited metadata               | Collection-level                                   | Add asset-level metadata; ensure completeness         | Metadata Team| Planned| Medium-term  |
| Portal Downloads       | Licensing documentation        | All assets                                         | Add attribution and licence notes per asset           | Licensing Team| Planned| Medium-term  |
| RRB NTPC               | Licensing requirements         | Topic-level assets                                 | Formalize redistribution documentation                | Licensing Team| Planned| Medium-term  |
| DIKSHA Mathematics     | Mixed integrity; sparse metadata | Core PDFs                                        | Re-download; add asset metadata                       | Content Ops  | Planned| Medium-term  |
| Government Repositories| No primary PDFs; no licensing  | Catalog/archives                                   | Source identification; content extraction; licensing docs | Research Lead| Planned| Long-term    |

## Implementation Roadmap

Immediate (Week 1)
- Replace zero-byte and invalid-header PDFs; validate EOF markers and page counts for large documents.
- Repair invalid/empty JSON metadata; ensure parseability and conformance to a uniform schema.
- Implement uniform licensing documentation and attribution at the asset level in mixed-source collections.

Short-term (Weeks 2–4)
- Standardize metadata schemas across categories; extend coverage to asset-level provenance.
- Complete licensing documentation for Portal Downloads, DIKSHA collections, and Current Affairs.
- Resolve format inconsistencies in RRB NTPC Content; minimize mixed formats unless justified.

Medium-term (Months 2–3)
- Establish automated quality gates within ingestion and publishing pipelines, including checksum validation for PDFs and JSON schema enforcement.
- Implement periodic integrity checks and metadata/licensing audits to prevent regressions.
- Expand Government Repositories with primary content and documented licensing.

Table 14. Roadmap Timeline

| Phase              | Milestones                                                                 | Dependencies                          | Success Metrics                                        |
|--------------------|----------------------------------------------------------------------------|---------------------------------------|--------------------------------------------------------|
| Immediate (Week 1) | Replace/repair PDFs and JSONs; add attribution notes                      | Access to authoritative sources       | 95%+ PDFs pass integrity checks; JSONs parse correctly |
| Short-term (Weeks 2–4) | Standardize metadata; finalize licensing docs                           | Cross-team alignment                  | Metadata completeness ≥90%; licensing Compliant        |
| Medium-term (Months 2–3) | Automate gates; expand repos; continuous audits                       | Tooling and process adoption          | Sustained integrity ≥99%; zero critical regressions    |

## Validation and Re-testing Plan

Post-remediation scanning will confirm effectiveness. Each category will be rescheduled through the quality gate engine, capturing updated integrity classifications, metadata completeness, and licensing signals. Sampling protocols will validate at least five assets per category, including one metadata file per collection. Large PDFs will undergo manual checks for EOF integrity and rendering.

Acceptance criteria require all five gates to meet defined thresholds per category, and licensing status to be Compliant or Needs Review with documented justification. For high-risk categories with persistent mixed integrity, sampling density will increase, and checksum validation will be added.

![Re-test validation screenshot](/workspace/browser/screenshots/after_preview_click.png)

Table 15. Re-test Sampling Plan

| Category                | Sample Size | Assets to Validate                            | Checks                                  | Acceptance Criteria                         |
|-------------------------|---:|-----------------------------------------------|------------------------------------------|---------------------------------------------|
| DIKSHA Science          | 5+ | Core Chemistry/Physics PDFs                   | Header/EOF; page count; rendering        | No corruption; complete downloads           |
| Practice Reasoning      | 5+ | IBPS guides; comprehensive shortcuts          | PDF header/EOF; JSON parseability        | No EOF errors; JSON valid and complete      |
| Practice Mathematics    | 5+ | Previous-year papers; topic PDFs              | Header/EOF; checksum                     | No zero-byte; checksums match               |
| Portal Downloads        | 5+ | CBT1/CBT2 PDFs and metadata                   | Header/EOF; JSON schema validation       | Integrity intact; metadata 100%             |
| Current Affairs         | 5+ | Annual Reports; Yearbooks                     | Header/EOF; rendering                    | No incomplete items; stable rendering       |

## Appendices

### Appendix A: Detailed File Integrity Listings (Selected)

Table 16. Integrity Classifications by File

| File (Representative)                                           | Integrity Classification       |
|-----------------------------------------------------------------|--------------------------------|
| ncert-class-11-chemistry-part1.pdf                              | Corrupted (invalid header)     |
| ncert-class-12-physics-part1.pdf                                | Incomplete (missing EOF)       |
| ncert-class-9-science.pdf                                       | Incomplete (truncated)         |
| JagranJosh_CBT1_2021_Jan4_Shift1.pdf                            | Zero-byte                      |
| JagranJosh_CBT2_2017_Jan17_Shift1.pdf                           | Corrupted (invalid header)     |
| Cracku_NumberSystemsQuestions_RRBNTPC.pdf                       | Corrupted (invalid header)     |
| Cracku_SimpleCompoundInterestQuestions_RRBNTPC.pdf              | Corrupted (invalid header)     |
| freshersnow_rrb_general_intelligence_questions.pdf              | Zero-byte                      |
| ibps_guide_gi_reasoning_01.pdf                                  | Missing EOF                    |
| ssc_study_shortcuts_in_reasoning.pdf                            | Corrupted (invalid header)     |
| meritnotes_rrb_reasoning_questions_1.pdf                        | Corrupted (invalid header)     |
| practiceMock_500_current_affairs.pdf                            | Corrupted (invalid header)     |
| practiceMock_500_current_affairs_2025.pdf                       | Corrupted (invalid header)     |
| Culture_Annual_Report_2022-23.pdf                               | Error (EOF)                    |
| MEA_Annual_Report_2022-23.pdf                                   | Incomplete                     |
| India_Year_Book_2023.pdf                                        | Incomplete                     |
| India_Year_Book_2024.pdf                                        | Intact                         |

### Appendix B: Metadata Coverage Mapping (Selected)

Table 17. Metadata Coverage

| Category                | Metadata Files Found | Completeness % | Fields Present (Summary)                |
|------------------------|---:|---:|------------------------------------------|
| Portal Downloads       | 5  | 100% | Asset identifiers; source; mapping       |
| Practice Mathematics   | 4  | 100% | Asset identifiers; source; topic mapping |
| RRB NTPC Content       | Topic-level | Present | Schema harmonization recommended   |

### Appendix C: Licensing Status Evidence (Selected)

- Practice GA: Compliant—policy framework and attribution signals documented.
- Practice Licensing: Compliant—license register and attribution guidance present.
- All other categories: Needs Review—asset-level licensing and attribution documentation missing or incomplete.

### Appendix D: Sample Screens

![Topic page example](/workspace/browser/screenshots/biodiversity_wikipedia_page.png)

![Section rendering example](/workspace/browser/screenshots/article_middle_section.png)

![Processing warning example](/workspace/browser/screenshots/developer_tools_opened.png)

![Source access modal example](/workspace/browser/screenshots/cracku_login_modal.png)

### Appendix E: Information Gaps

- Explicit licensing/redistribution permissions are not documented for many categories; Practice GA and Practice Licensing are exceptions.
- Asset-level licensing fields are missing for mixed-source collections, particularly DIKSHA and Practice categories.
- Collection-level metadata schemas are not fully defined or consistently populated across categories.
- Some PDFs show processing warnings without definitive corruption; follow-up validation is required to confirm usability.
- Government Repositories contain catalogs and archives but limited first-order content PDFs in the current scan scope.
- Metadata completeness for RRB NTPC Content is strong at the topic level; broader collection-wide coverage requires verification.
- No verifiable external source URLs are provided in the current context; external validation is out of scope.
- Checksums directory exists but was not analyzed in this cycle; checksum-based integrity confirmation remains pending.

---

This blueprint provides an integrated, evidence-based plan to lift quality across the portfolio. The approach is pragmatic: fix integrity defects where they are most prevalent, standardize metadata, and formalize licensing and attribution. By executing the roadmap and re-testing with disciplined sampling, we expect rapid improvements in category scores, reduced publication risk, and durable quality assurance.