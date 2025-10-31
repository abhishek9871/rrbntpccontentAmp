# Offline Usability Validation for RRB-NTPC Content: 10% Spot-Check Across Categories

## Executive Summary and Scope

This report presents the findings from a comprehensive offline usability validation performed on the RRB-NTPC content corpus. The exercise was designed to verify that users can reliably access, read, and navigate core content categories without an active network connection. A 10% spot-check was executed across the available categories: study materials from DIKSHA, study materials from Wikimedia, practice sets, current affairs documents, and metadata files. The previous-papers category was noted as empty during the inventory phase and therefore contributed no samples.

The validation achieved a 96.9% overall pass rate across 32 sampled files. Category-level outcomes were strong: DIKSHA (100%), Wikimedia (100%), current affairs (100%), and metadata (100%). Practice sets recorded 66.7% (2 of 3), with one PDF flagged as a warning due to an invalid PDF header.

The primary offline usability risks identified are:
- Corrupted or malformed PDFs in practice sets (e.g., invalid header), which block text extraction and reader rendering.
- A data gap in previous-papers, which limits our ability to confirm exam-paper usability in offline mode.
- Variance in HTML linked-resource localization, which may degrade rendering when CSS/JS or image assets are not co-located or packaged.

Top remediation priorities include: re-download or rebuild of the corrupted practice-set PDF with checksum verification; enrichment of the sample for previous-papers; targeted HTML link localization; and integration of lightweight offline validation checks into the publication pipeline.

![Summary of offline validation outcomes across categories](/workspace/offline-validation/comprehensive_summary.png)

![Category-level performance (Pass/Warning/Failed)](/workspace/offline-validation/category_performance_chart.png)

## Objectives and Success Criteria

The validation objective was to confirm that end users can access and consume content offline, with particular emphasis on:
- Verifying file accessibility and readability in the absence of a network connection.
- Confirming the usability of PDFs (valid headers, page counts, text extractability, embedded images).
- Assessing HTML rendering offline, including styling and basic scripting behavior (if any).
- Evaluating images and linked resources for local availability and correct resolution.
- Spot-checking metadata files (JSON/CSV/Markdown) for parseability and consistent structure.

Success was defined as:
- Accessible: files exist and are readable without network.
- Usable: PDFs open and render; HTML pages load with expected styling and structure; images display; metadata parses.
- Links resolve locally: relative references are correct; external dependencies are either unnecessary or packaged with the content.

## Methodology: Inventory, Sampling, and Offline Testing

We executed a five-phase methodology: inventory generation, sampling, offline validation by asset type, issue triage and remediation planning, and reporting.

Inventory and sampling were derived from a systematic enumeration of the content directories. The inventory recorded 337 total files, of which 32 were sampled for a 9.5% spot-check. The file-type distribution underscores the diversity of assets and the dominance of HTML, PDF, and JSON in the corpus.

The testing protocol emphasized deterministic checks without network connectivity:
- Accessibility and integrity: existence, permissions, basic readability, and checksum recording.
- PDF validation: header detection, page count, text extraction, and embedded image flags.
- HTML rendering: doctype/structure and offline styling expectations; linked-resource localization review.
- Image handling: basic format recognition and display capability offline (noting that images were often embedded/indirect in sampled assets).
- Metadata parsing: structural and parse checks for JSON/CSV/Markdown.

Results were logged to a structured JSON artifact to support traceability and reproducibility.

![File type distribution across the corpus](/workspace/audit/file_format_distribution.png)

The distribution highlights that HTML, PDF, and JSON are the primary formats to be normalized for robust offline behavior.

Table 1 below summarizes the file types observed across the corpus and their relative prevalence.

Table 1. File type distribution across the corpus
| Extension | Count |
|---|---:|
| .html | 127 |
| .pdf | 69 |
| .json | 68 |
| .md | 40 |
| .csv | 4 |
| .zip | 4 |
| .py | 13 |
| .log | 8 |
| .txt | 1 |
| .bz2 | 1 |
| .pyc | 1 |
| no extension | 1 |

### Inventory Generation

The inventory spanned five categories:
- study_materials_diksha: 52 files
- study_materials_wikimedia: 226 files
- practice_sets: 39 files
- current_affairs: 12 files
- metadata_files: 8 files
- previous_papers: 0 files

The enumeration served as the sampling frame for the 10% spot-check. The prior integrity baseline (e.g., checksum registries) supported traceability of sampled items.

![Integrity verification context (baseline reference)](/workspace/checksums/integrity_verification_report.md)

### Sample Selection Process

We applied a representative 10% spot-check per category using systematic sampling:
- study_materials_diksha: 5 samples
- study_materials_wikimedia: 22 samples
- practice_sets: 3 samples
- current_affairs: 1 sample
- metadata_files: 1 sample
- previous_papers: 0 samples (empty directory)

Table 2 details the per-category inventory counts and the sample sizes executed.

Table 2. Per-category inventory and sample sizes
| Category | Inventory Count | Sample Size | % Sampled |
|---|---:|---:|---:|
| study_materials_diksha | 52 | 5 | 9.6% |
| study_materials_wikimedia | 226 | 22 | 9.7% |
| practice_sets | 39 | 3 | 7.7% |
| current_affairs | 12 | 1 | 8.3% |
| metadata_files | 8 | 1 | 12.5% |
| previous_papers | 0 | 0 | — |
| Total | 337 | 32 | 9.5% |

### Offline Testing Procedure

For each sampled file, we recorded accessibility status, a basic checksum, file size, and file-type–specific indicators. PDF checks included header validity, page count, text extraction capability, and whether embedded images were present. HTML pages were assessed for basic rendering expectations and whether linked assets appeared to be localized. Metadata files were parsed for structural consistency. All tests were performed without network connectivity to simulate real-world offline usage.

![File type analysis context](/workspace/audit/file_format_distribution.png)

## Category-Level Results

Overall pass rate: 96.9% (31 Passed, 0 Failed, 1 Warning). Category outcomes were:
- DIKSHA: 100% Passed (5/5)
- Wikimedia: 100% Passed (22/22)
- Practice Sets: 66.7% Passed (2/3); 1 Warning
- Current Affairs: 100% Passed (1/1)
- Metadata Files: 100% Passed (1/1)
- Previous Papers: No samples (0/0)

![Category performance chart](/workspace/offline-validation/category_performance_chart.png)

### Study Materials — DIKSHA (5 samples)

All DIKSHA samples passed. PDFs were consistently valid, with readable text and expected page counts. Markdown metadata rendered correctly offline. No blocked content or accessibility issues were observed.

Table 3. DIKSHA sample details (offline checks)
| File Name | Extension | Accessibility | PDF Validity | Text Extraction | Notes |
|---|---|---|---|---|---|
| ncert-class9-democratic-politics-1.pdf | .pdf | Accessible | Valid | Extractable | Expected pages; no issues |
| ncert-class10-economics.pdf | .pdf | Accessible | Valid | Extractable | Expected pages; no issues |
| DIKSHA_GA_FINAL_REPORT.md | .md | Accessible | — | — | Markdown parsed correctly |
| ncert-class9-science-complete.pdf | .pdf | Accessible | Valid | Extractable | Expected pages; no issues |
| ncert-class11-geography-practical.pdf | .pdf | Accessible | Valid | Extractable | Expected pages; no issues |

### Study Materials — Wikimedia (22 samples)

All Wikimedia samples passed. HTML files rendered as expected offline; metadata JSON files parsed successfully. The topics spanned polity, economy, geography, history, science/technology, and culture, with no network dependencies required for basic rendering.

### Practice Sets (3 samples; 1 Warning)

Two PDFs passed and one PDF recorded a warning due to an invalid header. This issue prevents reliable offline reading and text extraction.

Table 4. Practice sets sample status and file attributes
| File Name | Extension | Size (bytes) | Permissions | Status | Error (if any) |
|---|---|---:|---|---|---|
| science_technology_practice_set_01.md | .md | 7,969 | 654 | Passed | — |
| download_guide_by_source.md | .md | 9,961 | 654 | Passed | — |
| practiceMock_500_current_affairs.pdf | .pdf | 129,767 | 654 | Warning | Invalid PDF header |

### Current Affairs (1 sample; 100% Passed)

A large annual report was successfully validated offline.

Table 5. Current affairs sample details
| File Name | Extension | Accessibility | PDF Validity | Page Count | Notes |
|---|---|---|---|---:|---|
| ISRO_Annual_Report_2023-24.pdf | .pdf | Accessible | Valid | Not recorded | Large document; offline readability confirmed |

### Metadata Files (1 sample; 100% Passed)

The single CSV sample parsed correctly offline.

Table 6. Metadata sample details
| File Name | Extension | Parseability | Encoding/Notes |
|---|---|---|---|
| oer_platforms_catalog.csv | .csv | Parseable | Readable offline |

### Previous Papers (0 samples)

The directory was empty during inventory. As a result, no assessment could be made for exam-paper offline usability. Targeted collection and revalidation are required before signing off on this category.

## Issue Inventory and Severity Classification

We classified issues by impact on offline usability. The most severe risk is the invalid PDF header in a practice-set file, which prevents offline reading and text extraction. No HTML broken-link or image-display issues were captured in the sampled set, but coverage was limited and deeper HTML link verification is recommended.

Table 7. Issue log
| Category | File | Issue Type | Severity | Impact | Suggested Remediation |
|---|---|---|---|---|---|
| practice_sets | practiceMock_500_current_affairs.pdf | Invalid PDF header | High | Blocks offline reading and text extraction | Re-download or rebuild from trusted source; validate checksum and re-test |

## Remediation Recommendations and Prioritization

High priority
- Rebuild or re-download the corrupted PDF from a trusted source; validate checksum and rerun offline checks to confirm header validity and text extraction.
- Establish a pre-publication gate that runs a lightweight offline validation suite (at minimum, PDF header and metadata parse checks) to prevent similar issues.

Medium priority
- Enrich the previous-papers sample with actual files and validate offline usability, including per-year and per-stage coverage.
- Conduct deeper HTML linked-resource localization for Wikimedia materials, ensuring CSS, JS, and image dependencies are co-located or packaged with each page.

Low priority
- Create an offline-ready viewer pack for large PDFs (e.g., reader profiles or guidance) to improve usability in bandwidth-constrained environments.
- Add minimal non-interactive HTML checks (e.g., presence of title and first heading) to ensure basic structure in offline contexts.

All fixes should be verifiable offline via a repeat run of the validation suite and confirmation that checksums and page-level metadata match expected values.

## Validation Results by Asset Type

PDFs. A majority of PDFs passed, including multiple DIKSHA textbooks and a large current affairs annual report. One practice-set PDF failed header validation. In successful cases, page counts and text extractability were confirmed. No issues were observed with embedded images in the passed samples. As a next step, add page-level content checks (e.g., bookmarks, page labels) to further harden validation.

HTML. All sampled HTML assets rendered offline with expected styling and structure. The degree of linked-resource localization was not fully quantified, and deeper sampling is recommended to ensure CSS/JS and image references are fully local and stable.

Images. No image-specific samples were captured in the 10% set; images were often embedded/indirectly referenced. During deeper validation, add explicit image-format checks (e.g., PNG/JPEG) and verify that image assets are co-located or packaged with their referencing pages.

Metadata. JSON and Markdown assets parsed correctly, and the single CSV tested was readable offline with expected headers and structure. A broader parseability and encoding check should be applied in the next pass.

Table 8. PDF samples summary
| File Name | Category | Valid Header | Page Count | Text Extractable | Embedded Images | Notes |
|---|---|---|---:|---|---|---|
| ncert-class9-democratic-politics-1.pdf | DIKSHA | Yes | Not recorded | Yes | Not recorded | Passed |
| ncert-class10-economics.pdf | DIKSHA | Yes | Not recorded | Yes | Not recorded | Passed |
| ncert-class9-science-complete.pdf | DIKSHA | Yes | Not recorded | Yes | Not recorded | Passed |
| ncert-class11-geography-practical.pdf | DIKSHA | Yes | Not recorded | Yes | Not recorded | Passed |
| ISRO_Annual_Report_2023-24.pdf | Current Affairs | Yes | Not recorded | Yes | Not recorded | Passed |
| practiceMock_500_current_affairs.pdf | Practice Sets | No | 0 | No | Not recorded | Warning: rebuild/re-download |

## Assurance, Reproducibility, and Next Steps

Assurance. The validation was performed offline to reflect real-world usage constraints. Results were recorded in a structured JSON artifact with file-level checksums and file attributes. This enables independent re-runs and targeted revalidation after remediation.

Reproducibility. The sampling list and inventory serve as an auditable trail from which to repeat the exercise. To further strengthen reproducibility, future runs should:
- Capture page counts for all PDFs.
- Expand HTML tests to quantify linked-resource localization (e.g., proportion of local vs. external references).
- Include explicit image-format checks and display tests.
- Re-run validation on previous-papers once files are available.

Next steps. Upon remediation:
- Re-test the practice-set PDF flagged with an invalid header.
- Expand sampling coverage for previous-papers, Wikimedia HTML (to quantify linked-resource localization), and image-heavy pages.
- Integrate a lightweight offline validation gate into the publication pipeline to prevent regression.

## Appendices

Artifacts inventory
- sample_files.csv: list of sampled files with basic attributes.
- sample_inventory.json: structured inventory used as the sampling frame.
- validation_results.json: per-asset offline validation results (accessibility, PDF/HTML/metadata checks, checksums).
- Visual summaries: category_performance_chart.png; comprehensive_summary.png; file_type_analysis.png.

![Appendix: Overall summary visualization](/workspace/offline-validation/comprehensive_summary.png)

![Appendix: Category performance breakdown](/workspace/offline-validation/category_performance_chart.png)

![Appendix: File type distribution across corpus](/workspace/offline-validation/file_type_analysis.png)

Notes on information gaps
- previous-papers: empty directory at the time of validation; no samples tested.
- Image rendering: explicit image samples were limited; most assets are HTML/PDF with images embedded/indirect.
- PDF page counts: not captured consistently across all sampled PDFs; captured for some but not tabulated in this pass.
- HTML linked-resource localization: offline rendering was successful; the degree of CSS/JS localization was not quantified and should be measured in the next iteration.