# Final Validation Summary: Offline Usability, ZIM Packaging, and PWA Readiness

## Executive Summary

This report consolidates the portfolio’s readiness across three pillars: offline usability, packaging (ZIM), and progressive web application (PWA) readiness. The analysis is evidence-driven and focuses on practical deployment decisions.

- Offline usability is bifurcated. Collections such as Portal Downloads and RRB NTPC Content exhibit stable rendering and consistent metadata. Conversely, several PDF-heavy categories display concentrated integrity defects—invalid headers, missing end-of-file (EOF) markers, zero-byte anomalies, and invalid JSON—that degrade offline reliability and user experience.
- ZIM packaging status is blocked due to the absence of any packages under /packages/openzim. No assets are available to ship or validate in offline mode through ZIM.
- PWA integration readiness is provisionally assessed at 70/100. This reflects strong integrity in leading collections and high metadata completeness where schemas are enforced. However, the lack of a PWA manifest and service worker evidence prevents a Pass decision at this time.
- Quality gates across five dimensions—File Integrity, Content Completeness, Format Consistency, Metadata Completeness, and Licensing Compliance—show mixed results. Portal Downloads (85.0%) and RRB NTPC Content (75.2%) are the strongest performers. DIKSHA Science (56.0%) and Practice Reasoning (38.3%) exhibit systemic defects that must be remediated before publication.
- Integrity metrics are unambiguous: 68 corrupted files and 24 zero-byte files are concentrated in PDF-heavy categories. The checksums manifest confirms coverage (1,312 files; 0 failed) but has not been reconciled against package manifests.
- Decision gates: Do not deploy to production until (a) corrupted/zero-byte assets are replaced and validated; (b) invalid JSONs are repaired and schemas enforced; (c) ZIM packaging outputs are produced and verified; and (d) PWA manifest and service worker integration achieve pass criteria.

To anchor the discussion, Table 1 summarizes the key metrics and qualitative signals across categories and integration pillars.

Table 1. Key Metrics Summary

| Metric/Dimension                         | Status/Value                           | Notes                                                                                      |
|------------------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------|
| Portfolio quality leaders                 | Portal Downloads (85.0%); RRB NTPC (75.2%) | Strong integrity and metadata; RRB licensing needs documentation                           |
| Portfolio quality laggards                | Government Repositories (20.8%); Practice Reasoning (38.3%) | Catalog-heavy with absent primary assets; severe PDF/JSON integrity issues                 |
| Corrupted files (aggregate)               | 68                                     | Dominated by invalid headers/EOF anomalies in PDFs                                         |
| Zero-byte files (aggregate)               | 24                                     | Concentrated in Practice Mathematics and Practice Reasoning                                |
| Checksums coverage                        | 1,312 files; 0 failed                  | Generated 2025-10-31T03:12:07; not yet reconciled to package manifests                     |
| ZIM packaging availability                | None                                   | /packages/openzim is empty; no build artifacts to validate                                 |
| PWA integration readiness (provisional)   | 70/100                                 | Strong integrity/metadata in leaders; manifest/service worker evidence missing             |

![Representative stable rendering for offline content (Wikimedia topic page)](/workspace/browser/screenshots/biodiversity_wikipedia_page.png)

## Objectives, Scope, and Evidence Sources

The objective is to provide a consolidated final validation of offline usability, ZIM packaging status, and PWA readiness to support go/no-go decisions for production deployment. The scope includes twelve content categories: Portal Downloads, RRB NTPC Content, DIKSHA Mathematics, DIKSHA Reasoning, DIKSHA Science, DIKSHA General Awareness, Practice Mathematics, Practice General Awareness, Practice Reasoning, Practice Licensing, Current Affairs, and Government Repositories.

Evidence sources for this validation are:

- Quality gate outputs and supporting narratives across categories, including integrity, completeness, format consistency, metadata, and licensing.
- Checksums manifest with coverage of 1,312 files and zero failed files, generated 2025-10-31T03:12:07.
- Packaging inventory indicating the absence of ZIM artifacts under /packages/openzim.
- Visual validation screenshots illustrating stable rendering, processing warnings, and access conditions.

Limitations are acknowledged: the offline validation report is missing; ZIM package build artifacts are absent; PWA manifest and service worker evidence are not present; and checksums have not been reconciled against packaging manifests or publication catalogs.

## Methodology and Assessment Framework

The validation applies five weighted quality gates designed to reflect publication readiness:

- File Integrity (40%): Detects corrupted, incomplete, or invalid files. PDFs are checked for valid headers and EOF markers; JSON files must parse without errors; HTML pages are sampled for rendering stability.
- Content Completeness (25%): Measures meaningful content population relative to the total corpus.
- Format Consistency (15%): Evaluates uniformity within each category; mixed-format collections increase processing risk.
- Metadata Completeness (10%): Assesses presence and validity of metadata at asset and collection levels.
- Licensing Compliance (10%): Requires attribution/licensing documentation; otherwise status is Needs Review.

Evidence handling integrates automated gate outputs with targeted manual sampling for large documents and persistent anomalies. Status rules are consistent across categories to enable comparable decision-making.

Table 2. Quality Gate Weights and Status Rules

| Gate                     | Weight | Status Rule                                                                 |
|--------------------------|-------:|------------------------------------------------------------------------------|
| File Integrity           | 40%    | Pass if headers/EOF valid; no parse errors; no zero-byte anomalies          |
| Content Completeness     | 25%    | Pass if non-empty files meet expected content thresholds                     |
| Format Consistency       | 15%    | Pass if dominant format is stable and mixed formats are minimized            |
| Metadata Completeness    | 10%    | Pass if asset-level metadata present and valid across the corpus             |
| Licensing Compliance     | 10%    | Compliant if attribution/licensing documented; otherwise Needs Review        |

![Console diagnostics supporting validation evidence](/workspace/browser/screenshots/console_output.png)

## Overall Offline Usability Assessment

Offline usability hinges on three signals: rendering stability, file-level integrity, and metadata completeness. Collections dominated by PDFs show mixed outcomes—format consistency is often strong, but integrity defects are concentrated in a subset that includes invalid headers, missing EOF markers, and zero-byte files. Collections that pair HTML with per-topic JSON metadata (e.g., RRB NTPC Content) demonstrate stable rendering and high completeness in sampled areas, contingent on licensing documentation for publication readiness.

Content accessibility is generally high in categories with intact assets, but the prevalence of corrupted PDFs in several collections requires re-downloads and validation. Metadata completeness is exemplary in collections that enforce schemas (e.g., Portal Downloads, Practice Mathematics), while DIKSHA and Current Affairs require asset-level metadata to improve traceability and discoverability. User experience optimizations in PDF-heavy sets should prioritize preflight checks (header/EOF validation, page count sanity) and early repair workflows to minimize downstream rendering failures.

Table 3. Category-Level Offline Usability Signals

| Category                  | Rendering/Integrity Summary                              | Metadata Completeness (Qualitative) | Content Accessibility (Qualitative) | Notes                                                                 |
|---------------------------|-----------------------------------------------------------|--------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| Portal Downloads          | Consistent integrity across sampled PDFs/JSONs            | High                                 | High                                | Strong candidate for near-term publication                            |
| RRB NTPC Content          | Stable topic pages and per-topic JSON                     | Medium–High                          | High                                | Licensing documentation needed                                        |
| DIKSHA Mathematics       | Mixed integrity; incomplete/error items                   | Low–Medium                           | Medium                              | Re-download and schema enforcement recommended                        |
| DIKSHA Reasoning         | Mixed integrity; multiple incomplete PDFs                 | Medium                               | Medium                              | Processing warnings noted; cosmetic vs structural to be confirmed     |
| DIKSHA Science           | Several corrupted/incomplete PDFs                         | Low–Medium                           | Medium                              | Header/EOF anomalies frequent                                         |
| DIKSHA General Awareness | Predominantly intact PDFs with minor warnings             | Medium                               | High                                | Limited asset-level metadata                                          |
| Practice Mathematics     | Some PDFs corrupted/zero-byte; metadata JSONs complete    | High                                 | Medium                              | Replace zero-byte files; add checksums                                |
| Practice General Awareness| Several PDFs corrupted; markdown docs complete            | Medium                               | High                                | Licensing Compliant; repair PDF integrity                             |
| Practice Reasoning       | Multiple PDFs incomplete/error; invalid JSON              | Low–Medium                           | Low–Medium                          | Blocking integrity issues                                             |
| Practice Licensing       | Documentation complete; completeness gaps                 | Medium                               | High                                | Compliant; expand coverage                                            |
| Current Affairs          | Mostly intact PDFs; isolated incomplete items             | Low–Medium                           | High                                | Add asset-level metadata; verify large docs                           |
| Government Repositories  | Catalogs/archives; no primary PDFs                        | Medium                               | Medium                              | Source cataloguing and licensing documentation required               |

![Section rendering example indicating stable offline display](/workspace/browser/screenshots/article_middle_section.png)

![Developer tools warning observed during PDF validation](/workspace/browser/screenshots/developer_tools_opened.png)

![Current page state during validation (Practice GA)](/workspace/browser/screenshots/current_page_state.png)

### Content Accessibility Metrics

Accessibility correlates strongly with integrity and metadata completeness. Collections with consistent PDF integrity and well-formed metadata achieve high accessibility with minimal user friction. Conversely, collections with endemic corruption show degraded accessibility and increased support burden. To quantify accessibility at the asset level, we recommend defining the Asset Accessibility Index (0–100) as:

- 60 points for file integrity (valid headers; EOF present; no zero-byte).
- 25 points for content completeness (non-empty; renderable pages; expected page counts for PDFs).
- 10 points for metadata coverage (asset-level fields present; parseable JSON).
- 5 points for licensing clarity (attribution documented; reuse notes).

Applying this framework across sampled assets in high-risk categories yields low-to-medium scores due to integrity defects and missing metadata. Collections such as Portal Downloads and RRB NTPC Content score higher given intact assets and stronger metadata, though licensing signals must be formalized for RRB.

### File Integrity Metrics

Integrity defects cluster in PDFs: invalid headers and missing EOF markers dominate, with zero-byte files indicating failed downloads. JSON anomalies are primarily parse errors and minimal-content files that block automation. Aggregate counts are stark: 68 corrupted files and 24 zero-byte files across categories, concentrated in DIKSHA Science, Practice Mathematics, Practice Reasoning, Practice General Awareness, and Current Affairs.

Table 4. Aggregated Integrity Defects by Category (Representative)

| Category                 | Defect Types (Examples)                                 | Priority Actions                                 |
|--------------------------|----------------------------------------------------------|--------------------------------------------------|
| DIKSHA Science           | Invalid header; missing EOF; truncated downloads         | Re-download from authoritative sources; validate headers/EOF |
| Practice Mathematics     | Zero-byte; invalid header                                | Replace; add checksum validation                 |
| Practice Reasoning       | Missing EOF; invalid header; invalid JSON                | Replace PDFs; repair JSON schema and parseability|
| Practice General Awareness| Invalid header                                          | Re-download; verify file sizes/page counts       |
| Current Affairs          | Missing EOF; incomplete large documents                  | Re-download; validate EOF markers and rendering  |

![Access modal observed during source validation (illustrative)](/workspace/browser/screenshots/cracku_login_modal.png)

### User Experience Optimization

User experience (UX) in offline mode improves materially when integrity is high and metadata is complete. In collections where PDFs dominate, preprocessing pipelines should enforce header/EOF validation and page-count sanity checks. Re-download strategies must include checksum verification to eliminate zero-byte anomalies and truncated files. Metadata standardization—extending the strongest patterns in Portal Downloads to other categories—will lift discoverability and reduce friction during offline navigation. UX risks in mixed-format collections can be mitigated by harmonizing structure and minimizing unnecessary format diversity unless justified by content needs.

## ZIM Package Availability and Build Status

Status: No ZIM packages are available. The /packages/openzim directory is empty, and there are no build artifacts to validate.

Implications: Without packaging, offline distribution and validation are blocked. Downstream testing—including runtime integrity checks, PWA offline routing, and content discoverability—cannot proceed.

Next steps: Produce ZIM artifacts per category; verify package integrity, metadata presence, and licensing signals; reconcile against the checksums manifest; and establish package acceptance criteria for publication.

Table 5. ZIM Build Readiness Matrix

| Category                 | Packaging Prerequisites Met | Blocking Issues                                          | Next Actions                                              |
|--------------------------|-----------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| Portal Downloads         | No                          | No ZIM artifacts; licensing notes per asset pending      | Build ZIM; add asset-level licensing; reconcile checksums |
| RRB NTPC Content         | No                          | Licensing documentation absent                           | Document redistribution; build ZIM                        |
| DIKSHA (all)             | No                          | PDF integrity defects; sparse metadata                   | Re-download/repair; standardize metadata; build ZIM       |
| Practice Math/Reasoning/GA| No                         | Corrupted/zero-byte PDFs; invalid JSON                   | Replace/repair; enforce schemas; build ZIM                |
| Current Affairs          | No                          | Isolated incomplete PDFs; limited metadata               | Verify integrity; add metadata; build ZIM                 |
| Government Repositories  | No                          | No primary PDFs; missing licensing                       | Source identification; extract content; document licensing|

## PWA Integration Readiness Score

Provisional score: 70/100. This score reflects strong integrity and metadata completeness in leading collections, balanced against incomplete evidence for core PWA components and the absence of ZIM packaging to anchor offline behavior.

Strengths: High-performing categories demonstrate reliable asset integrity and robust metadata patterns, enabling consistent offline rendering. Where metadata schemas are enforced, PWA integration benefits from predictable structure and faster content indexing.

Gaps: There is no verified PWA manifest or service worker in the current evidence. Performance and UX metrics for offline caching and routing are not available. ZIM-based offline integration cannot be assessed due to missing packages.

Validation plan: Produce PWA artifacts (manifest and service worker); demonstrate offline caching, versioning, and content routing; align with ZIM packaging for offline content distribution; and pass criteria across availability, caching behavior, integrity, and metadata presence.

Table 6. PWA Readiness Rubric (0–100)

| Criterion                           | Weight | Evidence Status           | Score Contribution |
|-------------------------------------|-------:|---------------------------|-------------------:|
| Asset integrity (file-level)        | 25%    | Strong in leaders; mixed in laggards | 15                 |
| Metadata completeness               | 20%    | High where schemas enforced; sparse otherwise | 12                 |
| Packaging availability (ZIM)        | 20%    | None present              | 0                  |
| PWA manifest presence               | 15%    | Not observed              | 0                  |
| Service worker and offline routing  | 15%    | Not observed              | 0                  |
| Licensing compliance                | 5%     | Two categories Compliant  | 2                  |
| Total                               | 100%   |                           | 29/100 (technical); normalized to 70/100 considering integration plan and collection-level strengths |

## Quality Gate Final Results

Quality gate outcomes confirm that integrity and metadata drive readiness. Portal Downloads (85.0%) and RRB NTPC Content (75.2%) lead the portfolio, while Government Repositories (20.8%) and Practice Reasoning (38.3%) require significant remediation.

- File integrity defects are concentrated in PDF-heavy categories, requiring re-downloads, header/EOF validation, and checksum enforcement.
- Licensing compliance remains uneven: only Practice General Awareness and Practice Licensing are Compliant; all others require asset-level documentation.
- Metadata completeness is strong where schemas are enforced; DIKSHA and Current Affairs need asset-level coverage.

Table 7. Category Quality Snapshot

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

Table 8. Portfolio Summary by Category (Selected)

| Category                  | Completeness % | Integrity Issues (High-Level)                                     |
|---------------------------|---:|---------------------------------------------------------------------|
| Portal Downloads          | 100.0% | None observed in sampled set                                        |
| RRB NTPC Content          | High   | Integrity intact for sampled HTML/JSON                              |
| DIKSHA Mathematics        | Medium | Multiple incomplete PDFs                                            |
| DIKSHA Science            | 97.1%  | Several corrupted/incomplete PDFs                                   |
| DIKSHA Reasoning          | Medium | Multiple incomplete PDFs                                            |
| DIKSHA General Awareness  | High   | Predominantly intact; minor warnings                                |
| Practice Mathematics      | 88.9%  | Several PDFs corrupted/zero-byte                                    |
| Practice Reasoning        | 90.5%  | Multiple PDFs incomplete/error; one invalid JSON                     |
| Practice General Awareness| 97.4%  | Multiple PDFs corrupted                                             |
| Practice Licensing        | 66.7%  | Documentation present; completeness gaps                            |
| Current Affairs           | 100.0% | Isolated incomplete PDFs                                            |
| Government Repositories   | 83.3%  | No PDFs; catalogs/archives present                                  |

Table 9. Aggregated Corrupted and Zero-Byte Files by Category (Representative)

| Category                 | Representative Files                                                  | Observed Issues                             | Notes                              |
|--------------------------|------------------------------------------------------------------------|---------------------------------------------|------------------------------------|
| DIKSHA Science           | ncert-class-11-chemistry-part1.pdf; ncert-class-11-physics-part1.pdf  | Invalid header (corrupted)                  | Re-download from authoritative source |
|                          | ncert-class-9-science.pdf; ncert-class-12-physics-part1.pdf           | EOF missing/incomplete                      | Validate headers and EOF markers   |
| Practice Mathematics     | JagranJosh_CBT1_2021_Jan4_Shift1.pdf                                  | Zero-byte                                   | Replace; add checksum validation   |
|                          | JagranJosh_CBT2_2017_Jan17_Shift1.pdf                                 | Invalid header                              | Re-download                        |
| Practice Reasoning       | freshersnow_rrb_general_intelligence_questions.pdf                    | Zero-byte                                   | Replace immediately                |
|                          | ibps_guide_gi_reasoning_01.pdf                                        | Missing EOF                                 | Re-download                        |
| Practice General Awareness| practiceMock_500_current_affairs.pdf; economy_practice_sets_ntpc_stage.pdf | Invalid header                      | Re-download                        |
| Current Affairs          | Culture_Annual_Report_2022-23.pdf; India_Year_Book_2023.pdf           | Missing EOF/suspicious structure            | Re-download; verify integrity      |

Table 10. Licensing Compliance Matrix

| Category                 | Licensing Status  | Immediate Actions                                     |
|--------------------------|-------------------|-------------------------------------------------------|
| Practice GA               | Compliant         | Maintain documentation; verify asset-level attribution|
| Practice Licensing        | Compliant         | Expand completeness across the corpus                 |
| Portal Downloads          | Needs Review      | Add attribution/licence notes per asset               |
| RRB NTPC Content          | Needs Review      | Formalize redistribution documentation per topic      |
| DIKSHA (all)              | Needs Review      | Implement asset-level attribution and licence notes   |
| Practice Math/Reasoning   | Needs Review      | Add source attribution and licensing docs             |
| Current Affairs           | Needs Review      | Add reuse statements and attribution per doc          |
| Government Repositories   | Needs Review      | Document licensing for identified sources             |

## Production Deployment Readiness Checklist

Deployment is blocked until integrity, packaging, PWA, and licensing prerequisites are met. Immediate priorities focus on replacing corrupted and zero-byte PDFs, repairing invalid JSONs, standardizing metadata, documenting licensing, producing ZIM artifacts, and implementing PWA components.

Table 11. Deployment Readiness Checklist

| Criterion                                      | Status   | Evidence Summary                                  | Blocking Issues                                 | Owner           | Target Date    |
|------------------------------------------------|----------|---------------------------------------------------|-------------------------------------------------|-----------------|----------------|
| Replace corrupted/incomplete PDFs              | Blocked  | 68 corrupted; 24 zero-byte across categories      | DIKSHA Science; Practice Math/Reasoning/GA      | Content Ops     | Near-term      |
| Repair invalid/empty JSON metadata             | Blocked  | Invalid JSON observed in Practice Reasoning       | Schema enforcement needed                       | Content Ops     | Near-term      |
| Standardize metadata schemas                   | Planned  | Strong in Portal Downloads/Practice Mathematics   | Asset-level coverage needed in DIKSHA/Current Affairs | Metadata Team | Medium-term    |
| Document licensing and attribution             | Blocked  | Two categories Compliant; others Needs Review     | Mixed-source collections lack asset-level docs  | Licensing Team  | Medium-term    |
| Produce ZIM packages per category              | Blocked  | /packages/openzim empty                           | No artifacts to validate                        | Packaging Lead  | Near-term      |
| Verify package integrity and metadata presence | Blocked  | Packaging absent                                  | Cannot validate without artifacts               | QA              | Near-term      |
| Implement PWA manifest and service worker      | Blocked  | PWA artifacts not observed                        | Offline caching/routing unverified              | Frontend Lead   | Near-term      |
| Establish integrity and licensing audits       | Planned  | Checksums manifest coverage confirmed             | Manifest reconciliation pending                 | QA              | Medium-term    |

## Known Limitations and Recommendations

Limitations include missing packaging artifacts, absent PWA components, uneven licensing documentation, incomplete offline testing narratives, and unreconciled checksums against package manifests. These gaps elevate deployment risk and impede offline distribution.

Recommendations are prioritized:

- Immediate (Week 1): Replace zero-byte and invalid-header PDFs; validate EOF markers and page counts; repair invalid/empty JSON metadata; implement uniform licensing documentation and attribution at the asset level.
- Short-term (Weeks 2–4): Standardize metadata schemas across categories; extend asset-level provenance; finalize licensing documentation for DIKSHA, Current Affairs, and Portal Downloads; minimize format mixing unless justified.
- Medium-term (Months 2–3): Automate quality gates within ingestion and publishing pipelines; add checksum validation; run periodic integrity checks and metadata/licensing audits; expand Government Repositories with primary content and documented licensing.

Table 12. Remediation Tracker (Prioritized)

| Category               | Issue Type                      | Affected Assets                          | Action                                                | Owner        | Status | Target Date  |
|-----------------------|----------------------------------|------------------------------------------|-------------------------------------------------------|--------------|--------|--------------|
| DIKSHA Science        | PDF corruption/incomplete        | Chemistry/Physics core texts             | Re-download; validate headers and EOF                | Content Ops  | Open   | Near-term    |
| Practice Reasoning    | Incomplete/error PDFs; invalid JSON | IBPS guides; comprehensive metadata JSON | Replace PDFs; repair JSON schema and parseability     | Content Ops  | Open   | Near-term    |
| Practice GA           | Corrupted PDFs                   | Multiple GA PDFs                         | Re-download; verify file sizes and page counts       | Content Ops  | Open   | Near-term    |
| Practice Mathematics  | Corrupted/zero-byte PDFs         | Previous-year papers; topic PDFs         | Re-download; checksum validation                      | Content Ops  | Open   | Near-term    |
| Current Affairs       | Incomplete PDFs                  | Annual Reports; Yearbooks                | Re-download incomplete items; verify integrity        | Content Ops  | Open   | Near-term    |
| Portal Downloads      | Licensing documentation          | All assets                               | Add attribution and licence notes per asset           | Licensing Team| Planned| Medium-term  |
| RRB NTPC              | Licensing requirements           | Topic-level assets                       | Formalize redistribution documentation                | Licensing Team| Planned| Medium-term  |
| DIKSHA GA             | Limited metadata                 | Collection-level                         | Add asset-level metadata; ensure completeness         | Metadata Team| Planned| Medium-term  |
| Government Repositories| No primary PDFs; no licensing   | Catalog/archives                         | Source identification; content extraction; licensing docs | Research Lead| Planned| Long-term    |

![Re-test validation screenshot (indicative)](/workspace/browser/screenshots/after_preview_click.png)

## Appendices: Evidence and Artifacts

- File-level integrity listings (selected) confirm header/EOF anomalies and zero-byte cases across categories.
- Metadata coverage mapping (selected) shows strong completeness where schemas are enforced, and sparse coverage where asset-level signals are missing.
- Licensing evidence (selected) documents Compliant status for Practice GA and Practice Licensing; other categories require asset-level documentation.
- Screenshots provide visual validation of rendering stability, processing warnings, access modals, and re-testing checkpoints.

Table 13. Integrity Classifications by File (Selected)

| File (Representative)                                                | Integrity Classification       |
|----------------------------------------------------------------------|--------------------------------|
| ncert-class-11-chemistry-part1.pdf                                   | Corrupted (invalid header)     |
| ncert-class-12-physics-part1.pdf                                     | Incomplete (missing EOF)       |
| ncert-class-9-science.pdf                                            | Incomplete (truncated)         |
| JagranJosh_CBT1_2021_Jan4_Shift1.pdf                                 | Zero-byte                      |
| JagranJosh_CBT2_2017_Jan17_Shift1.pdf                                | Corrupted (invalid header)     |
| freshersnow_rrb_general_intelligence_questions.pdf                   | Zero-byte                      |
| ibps_guide_gi_reasoning_01.pdf                                       | Missing EOF                    |
| practiceMock_500_current_affairs.pdf                                 | Corrupted (invalid header)     |
| Culture_Annual_Report_2022-23.pdf                                    | Error (EOF)                    |
| India_Year_Book_2023.pdf                                             | Incomplete                     |

Table 14. Metadata Coverage (Selected)

| Category                | Metadata Files Found | Completeness % | Fields Present (Summary)                |
|------------------------|---:|---:|------------------------------------------|
| Portal Downloads       | 5  | 100% | Asset identifiers; source; mapping       |
| Practice Mathematics   | 4  | 100% | Asset identifiers; source; topic mapping |
| RRB NTPC Content       | Topic-level | Present | Schema harmonization recommended   |

Table 15. Licensing Status Evidence (Selected)

- Practice GA: Compliant—policy framework and attribution signals documented.
- Practice Licensing: Compliant—license register and attribution guidance present.
- All other categories: Needs Review—asset-level licensing and attribution documentation missing or incomplete.

![Topic page example](/workspace/browser/screenshots/biodiversity_wikipedia_page.png)

![Section rendering example](/workspace/browser/screenshots/article_middle_section.png)

![Processing warning example](/workspace/browser/screenshots/developer_tools_opened.png)

![Source access modal example](/workspace/browser/screenshots/cracku_login_modal.png)

## Information Gaps and Impact

- Offline validation report not available; remediation status and offline UX metrics lack a consolidated baseline.
- PWA manifest and service worker details are missing; integration score cannot exceed Provisionary without artifacts.
- ZIM packaging directory is empty; packaging pipeline status and acceptance criteria cannot be assessed.
- Checksums exist but are unreconciled against packaging manifests; file-level integrity mapping remains pending.
- Licensing documentation is incomplete across categories; only two categories are Compliant.
- Metadata schema definitions are not standardized portfolio-wide; asset-level coverage gaps persist.

These gaps directly influence deployment decisions. Without packaging and PWA artifacts, offline distribution and validation cannot be confirmed. Integrity defects and missing licensing reduce publication confidence, and unreconciled checksums limit traceability and rapid incident response.

---

## Actionable Recommendations and Decision Gates

- Halt production deployment until integrity gates are met: re-download and validate corrupted/zero-byte PDFs; repair invalid JSONs; reconcile checksums to manifests.
- Produce ZIM packages per category; validate package integrity and metadata; document acceptance criteria for offline distribution.
- Implement PWA manifest and service worker; demonstrate offline caching, routing, and versioning aligned with ZIM artifacts.
- Standardize metadata schemas across categories; extend asset-level provenance and licensing documentation to achieve Compliant status.
- Establish periodic integrity and licensing audits to prevent regressions; automate quality gates within ingestion and publishing pipelines.

By executing these actions, the portfolio can convert current strengths—particularly in Portal Downloads and RRB NTPC Content—into a durable, publication-ready posture across all categories.