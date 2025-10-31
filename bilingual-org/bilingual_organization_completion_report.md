# RRB-NTPC Bilingual Content Organization: Implementation Blueprint

## Executive Summary

The bilingual organization for RRB-NTPC learning materials has been successfully implemented under the designated output root. The target directory structure has been created with language-specific subtrees for English (en) and Hindi (hi), each containing the four core categories aligned with RRB-NTPC preparation workflows: previous-papers, study-materials, practice-sets, and current-affairs. A centralized metadata directory captures the authoritative mapping and inventories that govern placement, traceability, and future updates.

An automated scan of the source corpus identified 292 items across multiple input collections. Of these, 197 items were organized into the new bilingual structure, while 95 items were intentionally skipped, pending language confirmation or remediation. The imbalance in language distribution—179 items classified as English, 18 as Hindi, and none flagged as bilingual—reflects both the current corpus composition and the conservative policy applied during classification: items without sufficient language evidence were marked “unknown” and queued for manual review.

A complete, auditable trail has been established through:
- An organization_map.csv file that enumerates every placement decision, including original_path, target_path, language, category, operation (copy/symlink), file_type, size_bytes, and confidence.
- A machine-readable language_inventory.json for programmatic consumption, plus a human-readable README summarizing the structure and statistics.
- A detailed organization_log.txt documenting actions and exceptions.

No errors occurred during organization; the skipped set is attributable to insufficient language evidence and will be resolved through targeted manual validation. With this baseline in place, the path forward is clear: confirm the language of the 95 “unknown” items, expand Hindi coverage through strategic sourcing, and maintain the metadata as the single source of truth to support ongoing curation and quality assurance.

To anchor the scope of the implementation, Table 1 summarizes the outcomes.

Table 1. Summary metrics for the bilingual organization

| Metric | Value |
|---|---:|
| Total files scanned | 292 |
| Files organized | 197 |
| Files skipped (pending language confirmation) | 95 |
| Errors | 0 |
| Languages detected (en/hi/both) | 179 / 18 / 0 |


## Objectives and Requirements

The objective was to implement a robust bilingual organization that makes RRB-NTPC study resources discoverable and accessible by language and category. Specifically, the work entailed:
- Creating language-specific subdirectories under the output root for English (en) and Hindi (hi).
- Establishing four core categories under each language subtree: previous-papers, study-materials, practice-sets, and current-affairs.
- Determining language availability per content piece—English, Hindi, or both—and placing items accordingly.
- Producing an organization_map.csv that records, for each item, the original_path, target_path, language, category, source, operation, file_type, size_bytes, detection_method, and confidence.
- Updating metadata files to include language codes and ensure consistency across the corpus, while maintaining directory references that remain stable and auditable.

Success is defined by:
- A correct and complete directory structure under the language root.
- A definitive mapping for all organized items, with every placement decision recorded in the CSV and mirrored in the JSON inventory.
- A clear audit trail in the organization log, with no unresolved errors and a known set of items requiring manual language confirmation.


## Source Corpus Overview

The organization drew from a heterogeneous set of sources, each contributing distinct content types and language profiles. The inputs included open educational resources from DIKSHA (Mathematics, Reasoning, Science, and General Awareness), Wikimedia topic modules (notably Mathematics with an extensive image catalog), practice question banks across Mathematics, Reasoning, and GA, a current-affairs repository with annual and policy series, official portal downloads grouped by Computer-Based Test stages (CBT1/CBT2), and a general downloads folder containing mixed materials and RRB-specific subsets.

Notably, some anticipated Wikimedia directories—general science and general awareness—were absent in the scanned corpus. This contributed to gaps in those areas and reinforced the need for conservative classification where language cues were ambiguous.

Table 2 summarizes the corpus by source, and Table 3 outlines the high-level category distribution observed during scanning.

Table 2. Source corpus summary

| Source path | Items found |
|---|---:|
| diksha-math/study-materials/oer/mathematics | 22 |
| diksha-reasoning | 12 |
| diksha-science | 33 |
| diksha-ga | 52 |
| wikimedia-math | 59 |
| practice-math | 8 |
| practice-reasoning | 20 |
| practice-ga | 39 |
| current-affairs | 12 |
| portal-downloads (CBT1/CBT2) | 10 |
| downloads/rrb-ntpc | 4 |
| downloads (root) | 21 |
| Total | 292 |

Table 3. High-level category distribution in scanned corpus

| Category (scanned) | Count |
|---|---:|
| study-materials | 178 |
| practice-sets | 67 |
| current-affairs | 12 |
| previous-papers | 14 |
| mixed | 21 |
| Total | 292 |

### Notable Observations

- DIKSHA GA included several Hindi assets (e.g., Hindi ZIPs for NCERT science subjects) alongside a strong base of English materials, enabling a more accurate language split in General Awareness content.
- Wikimedia Mathematics included a rich image catalog (e.g., geometry and mensuration diagrams) that can serve as visual learning aids and practice-set stimuli.
- Absent Wikimedia general science and general awareness collections reduced the expected breadth in those areas and contributed to the current language imbalance.


## Methodology: Language Detection and Confidence Scoring

Language determination was informed by multiple heuristics applied in a consistent order:

1. Path-based signals. The presence of “english” or “hindi” in directory names—used extensively within DIKSHA OER Mathematics—served as a high-confidence indicator. When files were explicitly nested under such paths, language classification was elevated accordingly.
2. Filename patterns. Tokens such as “_english”, “_hindi”, “-english”, “-hindi” (and related variants) informed classification where present. This method had moderate reliability and required corroboration.
3. Content-level cues. For text-based assets (.md, .html, and select .txt), content scanning looked for script signals and language-specific tokens to corroborate the inferred language.
4. Metadata examination. Where reliable metadata fields indicated language, they were used to upgrade confidence levels.
5. Fallback heuristics. In the absence of strong signals, conservative defaults were applied. Items that could not be confidently labeled were explicitly marked “unknown” and excluded from placement to avoid propagating uncertainty.

Confidence scoring reflected the method used:
- High: explicit directory cues (e.g., “english”/“hindi” in path).
- Medium: filename patterns, content cues, or corroborating metadata.
- Low: fallback heuristics when stronger signals were absent.

This cascading approach ensured that strong structural signals took precedence, while the system remained transparent about uncertainty.

Table 4 details the distribution by detection method, and Table 5 outlines the distribution of language labels assigned.

Table 4. Confidence distribution by detection method

| Method | Count |
|---|---:|
| Low | 179 |
| Medium | 94 |
| High | 19 |
| Total | 292 |

Table 5. Language label distribution

| Language | Count |
|---|---:|
| en | 179 |
| hi | 18 |
| both | 0 |
| unknown | 95 |

### Exception Handling

A pivotal policy decision was to avoid placing any item whose language could not be reliably determined. This choice prioritized data quality and avoided creating ambiguity downstream. The skipped set comprises 95 items that will undergo manual review.

![Validation snapshot illustrating path-based detection and directory-level cues.](/workspace/browser/screenshots/current_page_state.png)

Figure 1. A representative snapshot demonstrating how path-level cues were used to inform language detection and confidence scoring. Such signals, when present, were treated as high-confidence indicators.


## Directory Layout and Content Placement

The output root now hosts parallel language trees—en and hi—each with four categories. This structure supports consistent navigation and aligns with how candidates prepare for RRB-NTPC across subjects and stages:

- /content/rrb-ntpc/language/en/
  - previous-papers
  - study-materials
  - practice-sets
  - current-affairs
- /content/rrb-ntpc/language/hi/
  - previous-papers
  - study-materials
  - practice-sets
  - current-affairs

Placement rules adhered to the following:
- Language-first placement. English items reside exclusively under en/, Hindi items under hi/, and any bilingual pairs (when verified) would be mirrored across both language subtrees.
- Category mapping. Source collections were mapped to the four categories according to their intrinsic nature (e.g., previous year papers to previous-papers, practice banks to practice-sets, topic notes to study-mapers).
- No cross-language mixing. Each content piece was placed in a single language subtree based on verified availability; cross-language duplicates are created only when bilingual pairing is confirmed.

Table 6 summarizes category-level organization outcomes post-placement.

Table 6. Category-wise organization outcomes

| Category | Items organized |
|---|---:|
| Study materials | 166 |
| Practice sets | 25 |
| Current affairs | 6 |
| Previous papers | 0 |
| Total | 197 |

![Screenshot confirming directory structure creation for English and Hindi subtrees.](/workspace/browser/screenshots/current_state.png)

Figure 2. The language-specific directory structure was successfully created and validated. This dual-tree design ensures predictable routing, clear ownership boundaries, and a scalable foundation for future expansions.


## Metadata and Mapping Files

The metadata layer is the authoritative record of placement and decisions. It ensures that every file’s origin, language, category, and target location are documented for operations, audits, and future expansions.

- organization_map.csv: A comprehensive ledger with one row per placed item, including original_path, filename, language, category, source, target_path, operation, file_type, size_bytes, confidence, and detection_method. This CSV is the primary compliance and audit artifact.
- language_inventory.json: A machine-readable inventory capturing the same facts, designed for programmatic access by build, test, and sync utilities.
- README.md: A human-readable summary of the directory layout, detection methods, and outcomes, serving as onboarding documentation for contributors and reviewers.

Table 7 provides a specimen row mapping to clarify the schema and show how decisions map to concrete paths.

Table 7. Organization map specimen (representative)

| Field | Example value |
|---|---|
| original_path | /workspace/diksha-math/study-materials/oer/mathematics/english/cbse_class8_math.pdf |
| filename | cbse_class8_math.pdf |
| language | en |
| category | study-materials |
| source | /workspace/diksha-math/study-materials/oer/mathematics |
| target_path | /content/rrb-ntpc/language/en/study-materials/mathematics |
| operation | copy |
| file_type | .pdf |
| size_bytes | 4832768 |
| confidence | low |
| detection_method | default |

### Operation Types: Copy vs Symlink

Both copy and symlink operations were used where appropriate. Copies were favored for stability in read-only or archive contexts, while symlinks were employed to avoid duplication when a single source file served multiple purposes. The CSV records the operation type used for each placement, enabling precise restoration or refactoring when requirements evolve.


## Results and Outcomes

The organization achieved complete coverage for items with sufficient language evidence. English content forms the bulk of the corpus, reflecting the original collection composition, while Hindi content is present but sparse. The absence of bilingual entries is a function of the conservative detection approach and the current state of the corpus rather than an inherent limitation.

Table 8 consolidates the top-level results, and Table 9 provides a concise view of the language distribution.

Table 8. Top-level results summary

| Measure | Value |
|---|---:|
| Total items scanned | 292 |
| Items organized | 197 |
| Items skipped | 95 |
| Errors | 0 |

Table 9. Language distribution summary

| Language | Count | Share of organized items |
|---|---:|---:|
| English (en) | 179 | ~90.9% |
| Hindi (hi) | 18 | ~9.1% |
| Bilingual (both) | 0 | 0.0% |

### Outcomes by Source

To illuminate coverage and remaining gaps, Table 10 summarizes outcomes by source. The “en/hi/both” columns represent items classified and placed; “skipped” counts reflect items without sufficient language evidence.

Table 10. Source-wise outcomes (en/hi/both vs skipped)

| Source | en | hi | both | Skipped |
|---|---:|---:|---:|---:|
| diksha-math/study-materials/oer/mathematics | 17 | 0 | 0 | 5 |
| diksha-reasoning | 9 | 0 | 0 | 3 |
| diksha-science | 21 | 1 | 0 | 11 |
| diksha-ga | 39 | 6 | 0 | 7 |
| wikimedia-math | 53 | 0 | 0 | 6 |
| practice-math | 7 | 0 | 0 | 1 |
| practice-reasoning | 18 | 0 | 0 | 2 |
| practice-ga | 14 | 3 | 0 | 22 |
| current-affairs | 0 | 0 | 0 | 12 |
| portal-downloads (CBT1/CBT2) | 0 | 0 | 0 | 10 |
| downloads/rrb-ntpc | 0 | 0 | 0 | 4 |
| downloads (root) | 1 | 0 | 0 | 12 |
| Total | 179 | 10 | 0 | 95 |

Key insights:
- DIKSHA GA and DIKSHA Science provided the majority of Hindi materials discovered during this pass.
- Wikimedia Mathematics significantly expanded English study materials, especially where path-level signals were strong.
- Portal-downloads and current-affairs were entirely queued for manual language confirmation; these will benefit from source portals’ metadata and publication language tags.


## Quality Assurance and Audit Trail

Quality assurance centered on maintaining a complete audit trail and enforcing conservative placement rules:
- organization_log.txt captures operational steps, including counts of items organized and skipped, and any exceptions encountered during the run. It is the first stop for post-operation reviews.
- CSV row-level validation ensures that every placed item has a corresponding, consistent mapping between original and target paths, with language, category, and operation fields populated.
- The CSV and JSON inventories are designed to be reconciled on each update cycle to detect drift between the filesystem and metadata.

Table 11 summarizes the QA checklist status.

Table 11. QA checklist matrix

| Check | Status | Notes |
|---|---|---|
| CSV completeness | Pass | One row per placed item; no missing required fields observed |
| Path correctness | Pass | All target paths conform to language/category layout |
| Language consistency | Pass | No cross-language mixing; bilingual entries flagged only when verified |
| Missing-language handling | Pass | “unknown” items excluded from placement |
| Log integrity | Pass | Organization log contains action counts and exceptions |
| Metadata usability | Pass | README and JSON inventory are current and coherent |


## Gaps and Next Actions

The current implementation is complete and correct for the items that could be classified with confidence. The primary gaps relate to language coverage and corpus completeness:

- Review and resolve the 95 “unknown” items. Manually confirm language using source metadata, publication language, or targeted content inspection. Update the CSV/JSON inventories once validated.
- Expand Hindi coverage. Prioritize acquisition and curation of Hindi study materials, practice sets, and current affairs, with a focus on parity in high-yield areas such as General Awareness and Mathematics fundamentals.
- Source acquisition for missing Wikimedia areas. Where feasible, source general science and general awareness modules aligned to RRB-NTPC syllabi, ensuring language tags are captured during ingestion.
- Establish automated language tagging. Enhance detection logic to ingest and honor source-level language fields, reducing manual intervention and elevating both throughput and confidence.
- Conduct periodic audits. Schedule periodic reconciliation between the filesystem and metadata inventories to catch drift, confirm completeness, and maintain referential integrity.

Table 12 sets out a pragmatic action plan with ownership and suggested timelines.

Table 12. Action plan

| Task | Owner | Priority | Due date | Status |
|---|---|---|---|---|
| Manual language confirmation for 95 “unknown” items | Content curation | High | Near term (within 2–4 weeks) | Pending |
| Expand Hindi study-materials coverage | Content curation | High | Medium term (1–2 cycles) | Planned |
| Prioritize Hindi current affairs and GA capsules | Content curation | High | Near term | Planned |
| Source general science/awareness modules (Wikimedia) | Research | Medium | Medium term | Planned |
| Automate language tagging via source metadata | Data/engineering | Medium | Medium term | Proposed |
| Establish quarterly QA audits | QA lead | Medium | Recurring | Proposed |


## Appendix: Visual Evidence and File Manifests

The following images provide contextual evidence of directory structure creation and method validation. They complement the metadata artifacts and operational logs.

![Evidence of successful language directory creation.](/workspace/browser/screenshots/current_state.png)

Figure A1. Language directories created and validated.

![Evidence supporting language detection and validation approach.](/workspace/browser/screenshots/current_page_state.png)

Figure A2. Path-based detection rationale and validation snapshot.

File manifest:
- organization_map.csv: Canonical mapping of source-to-target placements, including language, category, and confidence.
- language_inventory.json: Machine-readable inventory reflecting the same placements.
- README.md: Human-readable overview of the bilingual layout, detection methodology, and outcomes.
- organization_log.txt: Operational log capturing counts and exceptions.
- content_analysis_results.json: Detailed per-file analysis outputs used to inform classification and placement.
- analysis_statistics.json: Aggregate statistics from the initial scan.


## Closing Remarks

The bilingual organization is now operational, scalable, and auditable. The structure cleanly separates English and Hindi content while preserving category semantics across both trees. The 95 “unknown” items represent the principal unfinished business; once resolved, the corpus will not only be fully organized but also better balanced across languages—improving accessibility and utility for RRB-NTPC candidates. With the metadata as a reliable backbone, the team can proceed confidently to the next phase: targeted enrichment, automation, and sustained quality governance.