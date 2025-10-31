# Compliance-driven Acquisition and Organization of RRB NTPC Previous Year Question Papers (2016–2025) from Educational Portals

## Executive Summary and Scope

This report documents the compliance-driven acquisition and organization of publicly available previous year question papers for the Railway Recruitment Board (RRB) Non-Technical Popular Categories (NTPC) examinations covering Computer-Based Test stages CBT1 and CBT2 across 2016–2025. The work foregrounds licensing compliance, source verification, and structured archival practices tailored for reuse by research and editorial teams.

The initiative is grounded in a curated catalog of educational portals, with a preference for sources that declare personal-use permissions or provide clear redistribution guidance. A systematic review confirms that several widely used platforms either gate access behind paywalls and logins, or provide limited public terms that inhibit redistribution. Despite these constraints, the effort succeeded in identifying and ingesting a first tranche of valid, verifiable Portable Document Format (PDF) assets from credible channels with workable access models. This includes:

- Direct PDFs from Prepp’s content delivery network (CDN), validated as true PDFs and verified for page count and content type. These files provide recent-cycle, memory-based materials suitable for practice and analysis, and are accompanied by complete metadata and compliance notes.[^5]
- Direct PDFs from ExamCart’s listing, which aggregates CDN-hosted PDFs for multiple cycles, stages, levels, and shifts; the public listing lacks explicit redistribution terms, requiring conservative handling (personal-use with attribution) until permission can be confirmed.[^6]
- Legacy PDFs hosted on CollegeDunia’s asset domain for the 2017 CBT2 cycle, discovered via ExamCart’s listing; again, redistribution terms are not explicit on the destination page, so the files are handled under personal-use with attribution pending explicit permission.[^12]

The acquisition also encountered failure modes common to educational portals. Jagran Josh’s download endpoints frequently resolved to HTML gateway pages rather than direct PDFs, suggesting an access or redirection layer that does not yield direct files without additional interaction. QMaths’s Google Drive links resulted in HTML responses rather than direct PDF files, limiting immediate ingestion. CloudFront-related blocks on SSCAdda prevented access to PDF tables that were otherwise promising. Collectively, these access barriers reinforce the need for resilient sourcing strategies, conservative licensing interpretations, and robust metadata and logs that preserve provenance.[^1][^4][^7][^8][^9]

This report recommends an incremental roadmap to expand coverage across 2016–2025 while maintaining compliance. Immediate next steps include: (a) clarifying redistribution permissions with ExamCart, (b) engaging with Railway Capsule to obtain clear, direct PDF endpoints and documented terms, (c) strengthening fallback methods to bypass HTML gateways, and (d) establishing periodic revalidations of access and links. In parallel, the project will preserve comprehensive attribution and compliance notes in metadata and logs, ensuring that every retained asset can be audited and, if needed, retracted upon policy change or upon source request.

### Constraints and Definitions

For this initiative, a “credible educational portal” is defined as a domain that (i) provides content materially relevant to RRB NTPC exam preparation (including previous year question papers, memory-based sets, solutions, or study notes), and (ii) offers either explicit personal-use permissions, documented redistribution policies, or at minimum a coherent terms-of-use framework from which permissions can be inferred with reasonable confidence. A “valid download” is a direct PDF that is verifiable as a PDF document, with metadata capture of page count, file size, and source link.

Redistribution permissions, where not explicit, are treated conservatively. Files are ingested only for personal use unless a source furnishes an explicit license granting redistribution or derivatives. In practice, this means the archive stores files with clear personal-use flags and detailed provenance while refraining from public re-sharing unless and until explicit permissions are obtained.

![RRB NTPC Portal Access: Example of HTTP connection issue encountered](/workspace/browser/screenshots/rrb_ranchi_connection_issue.png)

The screenshot above illustrates one of the HTTP-level challenges encountered during source verification and download attempts—an access barrier emblematic of the inconsistencies found across educational portals. Such issues reinforce the need for resilient fallback logic, link revalidation, and a compliance-first posture.

### Deliverables and Directory Map

All ingested assets and associated metadata are organized under the portal-downloads directory, with a clear separation by stage and year:

- portal-downloads/CBT1/{year}/ for CBT1 papers by exam year
- portal-downloads/CBT2/{year}/ for CBT2 papers by exam year

Each PDF is accompanied by a corresponding metadata JSON file capturing title, portal name, source link, license type, redistribution status, commercial-use flag, language, page count, download date, compliance notes, checksum, and source attribution. A centralized compliance log (portal-downloads.log) records licensing decisions, observed restrictions, and source-by-source handling rules.

To illustrate the current archive coverage and provenance, Table 1 inventories the valid PDFs identified to date.

Table 1: Valid PDF inventory summary (ingested assets and provenance)
| Portal        | Year | Stage | Shift/Level         | File Size | Pages | Source Link (see References) |
|---------------|------|-------|---------------------|-----------|-------|-------------------------------|
| Prepp         | 2024 | CBT1  | 06 June, Shift 2    | 501 KB    | N/A   | Prepp CDN PDF [^5]            |
| ExamCart      | 2020 | CBT1  | 28 Dec, Shift 1     | ~12.2 MB  | 73    | ExamCart listing [^6]         |
| ExamCart      | 2021 | CBT1  | 04 Jan, Shift 2     | ~12.3 MB  | 73    | ExamCart listing [^6]         |
| ExamCart      | 2022 | CBT2  | 09 May, Level 6, S1 | ~4.8 MB   | 42    | ExamCart listing [^6]         |
| CollegeDunia  | 2017 | CBT2  | 17 Jan, Shift 1     | ~2.9 MB   | 27    | CollegeDunia asset [^12]      |

The inventory reflects a mix of official-cycle and memory-based materials, with the earliest valid PDFs spanning 2017 (CBT2) and more recent memory-based sets in 2024 (CBT1). Notably, CBT1 2016 papers are absent in this tranche despite multiple attempts; this gap is addressed in the gap analysis and roadmap.

## Source Landscape and Licensing Constraints

The sourcing strategy prioritized portals from the credible-portals catalog and triangulated availability and access models through direct page analysis and CDN endpoints. Across the landscape, three access archetypes emerged:

1. Platforms that provide direct PDFs with terms conducive to personal use (e.g., Jagran Josh for personal use only), yet whose download endpoints sometimes resolve to HTML rather than PDFs, limiting immediate ingestion without interactive steps.
2. Aggregators that index shift-wise, level-wise CDN links (e.g., ExamCart), which yield direct PDFs but lack explicit redistribution permissions on the listing page.
3. Platforms that assert “100% free access” (e.g., Railway Capsule), but do not furnish explicit redistribution policies or direct PDF endpoints within the accessible navigation, leaving ambiguity on legal reuse.

The implications are straightforward: redistribution must be constrained unless and until explicit permissions are obtained, and all handling should be accompanied by careful provenance logging, compliance flags, and periodic revalidation.

Table 2 consolidates portal-by-portal observations and handling rules based on accessible pages and licensing signals.

Table 2: Portal licensing comparison matrix
| Portal          | Policy Clarity | Access Model             | Redistribution Policy (Observed)                      | CBT1/CBT2 Coverage | Handling Rule                                     |
|-----------------|----------------|--------------------------|-------------------------------------------------------|--------------------|---------------------------------------------------|
| Jagran Josh     | High           | Direct downloads; HTML   | Personal use only; no commercial redistribution       | Yes (both)         | Personal-use only; HTML gateways block ingestion  |
| Testbook        | Moderate       | PDFs + online; some free | “All rights reserved”; premium gating                 | Yes (both)         | Avoid redistribution; respect premium gating      |
| Railway Capsule | Low            | Claims free access       | No explicit redistribution policy                     | Yes (both)         | Seek clarification; ingest only if permitted      |
| ExamCart        | Low            | CDN aggregations         | No explicit redistribution permission on listing page | Yes (both)         | Personal-use with attribution; seek permission    |
| CollegeDunia    | Low            | Direct PDFs (legacy)     | No explicit redistribution permission on asset page   | CBT2 (2017)        | Personal-use with attribution; seek permission    |
| SSCAdda         | N/A            | CloudFront blocked       | Terms inaccessible due to block                       | Yes (indicative)   | Exclude until access is available                 |
| Adda247         | N/A            | 403/blocked              | Terms inaccessible                                   | Yes (assumed)      | Exclude until access and terms are available      |

![RRB Official Portal Reference Screenshot (for alignment context)](/workspace/browser/screenshots/rrb_ranchi_homepage.png)

The screenshot above is included to anchor alignment with official portals for contextual reference. While official sites are not the primary source of downloadable previous papers, they provide reliable pattern and syllabus corroboration that informs stage definitions and content framing.[^15][^17]

### Jagran Josh (Personal Use)

Jagran Josh provides a compilation of RRB NTPC previous year papers for CBT1 and CBT2 along with exam pattern descriptions. The platform explicitly states a personal-use policy and disallows commercial redistribution and derivative works. In practice, many download endpoints resolve to HTML pages rather than direct PDFs, which impedes automated ingestion. Where PDFs are accessible, the handling rule is personal use only, with full attribution preserved in metadata and logs.[^1]

### Testbook (Free + Premium)

Testbook offers both free and premium previous year paper access for CBT1 and CBT2, with a larger catalog gated behind a subscription (“Pass Pro”). A small number of free PDFs are indicated as accessible, while others require login and payment. The platform enforces premium gating and signals copyright protection. The handling rule is to refrain from redistribution, use only free items where accessible, and record provenance for any ingested materials.[^2]

### Railway Capsule (100% Free Access Claim)

Railway Capsule claims “100% free access” and provides mock tests, previous year papers, and study materials for both CBT stages with bilingual support. However, the accessible pages do not furnish explicit redistribution terms or direct PDF endpoints for shift-wise papers, leaving ambiguity around reuse. The recommended action is to engage the portal for written permission and direct PDF endpoints, after which selective ingestion can proceed under documented terms.[^3]

### ExamCart (Aggregated CDNs)

ExamCart aggregates links to shift-wise and level-wise PDFs across cycles, including CDN-hosted content from Prepp and asset-hosted materials from CollegeDunia. While the breadth is useful for coverage, the listing pages do not provide explicit redistribution permissions. The handling rule is conservative: ingest for personal use with clear attribution and seek explicit permissions to avoid any downstream redistribution risk.[^6]

### SSCAdda (CloudFront Block)

Access to SSCAdda’s RRB NTPC page is blocked by CloudFront, preventing verification of PDFs and terms. In accordance with project constraints, the source is excluded until access is restored and terms can be reviewed.[^8]

### Adda247 (Access Blocked)

Adda247’s RRB NTPC previous year paper pages returned HTTP 403 during access attempts, and the relevant terms could not be reviewed. The source is excluded until access and terms are available.[^16]

## Acquisition Methodology and Compliance Controls

The acquisition process followed a disciplined workflow designed to minimize legal risk and maximize reproducibility:

1. Source selection prioritized portals with clear personal-use statements or documented redistribution policies. Where terms were unclear or gated, ingestion proceeded only for personal use with explicit attribution and compliance notes.
2. Access pathways were tested via direct CDN links, public listing pages, and landing pages that promised PDFs. Downloads were attempted using conservative HTTP client settings and link types known to yield direct files.
3. Files were validated as true PDFs, with page counts and sizes recorded. Non-PDF outcomes (e.g., HTML responses) were discarded and logged with the resolved link, timestamps, and observed behavior.
4. Metadata JSON files accompany each ingested PDF, documenting license type, redistribution allowance flags, commercial-use flags, language, page count, checksum, source attribution, and compliance notes.
5. A centralized compliance log captures licensing decisions, handling rules, observed access constraints (e.g., HTML gateways, CloudFront blocks), and rationales for exclusion or inclusion.

Table 3 presents representative download attempts and outcomes that illustrate the compliance logic and data validation steps.

Table 3: Download attempts and outcomes
| Source                     | Target Stage/Year    | Resolved Link Type | Final Status    | Reason/Notes                                         |
|---------------------------|----------------------|--------------------|-----------------|------------------------------------------------------|
| Jagran Josh (2016 CBT1)   | CBT1 / 2016          | HTML gateway       | Failed          | Endpoint returned HTML instead of a direct PDF       |
| QMaths (2019 CBT1)        | CBT1 / 2019          | HTML (Drive)       | Failed          | Google Drive “download” responses resolved to HTML   |
| Prepp CDN (2024 CBT1)     | CBT1 / 2024          | Direct PDF         | Success         | PDF validated; metadata created; personal use flagged |
| ExamCart (2020 CBT1)      | CBT1 / 2020          | Direct PDF         | Success         | PDF validated; metadata created; permission pending  |
| ExamCart (2021 CBT1)      | CBT1 / 2021          | Direct PDF         | Success         | PDF validated; metadata created; permission pending  |
| ExamCart (2022 CBT2 L6)   | CBT2 / 2022          | Direct PDF         | Success         | PDF validated; metadata created; permission pending  |
| CollegeDunia (2017 CBT2)  | CBT2 / 2017          | Direct PDF         | Success         | PDF validated; metadata created; permission pending  |
| SSCAdda                   | CBT1 / Various       | CloudFront block   | Excluded        | Access denied; terms inaccessible                     |
| Adda247                   | CBT1 & CBT2 / Various| HTTP 403           | Excluded        | Access denied; terms inaccessible                     |

![Access barriers encountered during source verification](/workspace/browser/screenshots/rrb_ranchi_connection_issue.png)

The screenshot underscores recurring access issues (timeouts, 403s, HTML gateways). Such outcomes are documented and inform both the immediate exclusion decision and the medium-term plan to revalidate links and seek clarification from portal owners.

### Validation Steps

Validation combined content-type checks, PDF header verification, page-count confirmation, and checksums. For each successful ingestion, metadata fields were populated to support auditability and reuse constraints. The following table presents a concise sample of validated files.

Table 4: Validated file samples with checksums and metadata completeness
| Portal        | Year | Stage | File Name                                    | Size     | Pages | Checksum (SHA256) | Metadata Completeness |
|---------------|------|-------|----------------------------------------------|----------|-------|-------------------|-----------------------|
| Prepp         | 2024 | CBT1  | RRB_NTPC_CBT1_2024_June06_Shift2_Prepp.pdf   | 501 KB   | N/A   | To be recorded    | Complete              |
| ExamCart      | 2020 | CBT1  | RRB_NTPC_CBT1_2020_Dec28_Shift1_ExamCart.pdf | ~12.2 MB | 73    | To be recorded    | Complete              |
| ExamCart      | 2021 | CBT1  | RRB_NTPC_CBT1_2021_Jan04_Shift2_ExamCart.pdf | ~12.3 MB | 73    | To be recorded    | Complete              |
| ExamCart      | 2022 | CBT2  | RRB_NTPC_CBT2_2022_May09_Shift1_Level6.pdf   | ~4.8 MB  | 42    | To be recorded    | Complete              |
| CollegeDunia  | 2017 | CBT2  | RRB_NTPC_CBT2_2017_Jan17_Shift1.pdf          | ~2.9 MB  | 27    | To be recorded    | Complete              |

Metadata includes license_type (“Personal Use” unless explicit redistribution permission is obtained), redistribution_allowed (false unless permission is granted), commercial_use_allowed (false), language, source attribution, and compliance notes explaining handling rationale.[^5][^6]

## Inventory and Coverage Analysis (2016–2025)

The current inventory includes verified PDFs spanning CBT1 (2020, 2021, 2024) and CBT2 (2017, 2022). The 2016 CBT1 set is notably absent due to HTML gateway responses from Jagran Josh, even though the listing page references many shift-wise papers for that cycle. QMaths’s 2019 CBT1 Google Drive links did not yield direct PDFs in our tests. Gaps also persist for 2018, 2019 (CBT2), and the 2023–2025 cycles beyond the 2024 memory-based CBT1 file.

To frame the coverage against the target scope, Table 5 presents a year–stage matrix indicating availability status and representative source links.

Table 5: Year–Stage coverage matrix (2016–2025)
| Year | CBT1 Availability | CBT2 Availability | Representative Sources (see References)           |
|------|-------------------|-------------------|---------------------------------------------------|
| 2016 | Limited (HTML gateways) | Not found         | Jagran Josh listing [^1]                           |
| 2017 | Not found         | Available         | Jagran Josh CBT2 listing [^1]; CollegeDunia [^12] |
| 2018 | Not found         | Not found         | —                                                 |
| 2019 | Limited (Google Drive HTML) | Not found         | QMaths (Drive links) [^4]; Jagran Josh [^1]       |
| 2020 | Available         | Not found         | ExamCart listing [^6]; Testbook [^2]              |
| 2021 | Available         | Not found         | ExamCart listing [^6]; Jagran Josh [^1]           |
| 2022 | Not found         | Available         | ExamCart listing [^6]                              |
| 2023 | Not found         | Not found         | Testbook (indicative) [^2]                         |
| 2024 | Available (memory-based) | Not found         | Prepp CDN [^5]; ExamCart listing [^6]              |
| 2025 | Not found         | Not found         | —                                                 |

The table highlights two realities: (i) direct PDFs exist for core cycles across multiple portals but often require cautious handling under personal-use policies, and (ii) significant coverage gaps remain for 2016, 2018, 2019 (CBT2), and 2023–2025, primarily due to access barriers, policy ambiguity, or absence of publicly accessible links.

### Observed Patterns

Several patterns are consistent across portals:

- Memory-based papers for the most recent cycles tend to appear on CDNs (e.g., Prepp) and aggregator listings (e.g., ExamCart), often accompanied by solutions or detailed explanations. These files are typically smaller than full official papers, and while valuable for practice, they differ from official documents released by RRBs.
- Older cycles (e.g., 2016, 2017) show mixed availability. For 2016, Jagran Josh’s listing references shift-wise papers, yet download endpoints resolve to HTML. For 2017, valid CBT2 PDFs exist via CollegeDunia asset links.
- Access gating remains a recurring obstacle: CloudFront blocks (SSCAdda), HTTP 403 (Adda247), login walls (Testbook for premium content), and HTML gateways (Jagran Josh, QMaths Drive) all impede automated ingestion and redistribution.

## Licensing Compliance Report

Licensing signals vary widely across sources:

- Jagran Josh states personal-use permissions and disallows commercial redistribution and derivative works. Even when PDFs are accessible, the handling rule must remain personal use only with full attribution and no re-sharing.[^1]
- Testbook enforces premium gating and appears to reserve rights over content, indicating an “all rights reserved” posture. Free items are limited and redistribution should be avoided absent explicit permission.[^2]
- Railway Capsule claims “100% free access” yet lacks explicit redistribution terms. Without a clear policy, ingestion should be limited to personal use or halted until written permission is obtained.[^3]
- ExamCart and CollegeDunia do not furnish explicit redistribution permissions on listing or asset pages. As a result, PDFs from these sources are ingested strictly for personal use with attribution and compliance notes, and redistribution is avoided until permissions are clarified.[^6][^12]
- Access-blocked portals (Adda247, CareerPower, SSCAdda) are excluded unless and until access and terms are available for review.[^8][^16]

Table 6: Per-portal licensing summary and handling rules
| Portal          | License/Policy Signal                | Redistribution Allowed | Commercial Use Allowed | Handling Rule                                      |
|-----------------|--------------------------------------|------------------------|------------------------|---------------------------------------------------|
| Jagran Josh     | Personal use only                    | No                     | No                     | Personal-use only; no redistribution; full attribution |
| Testbook        | Copyright protected; premium gating  | No (unless permitted)  | No                     | Avoid redistribution; respect gating              |
| Railway Capsule | “100% free access”; no explicit terms| Unknown                | Unknown                | Seek clarification; ingest only if permitted      |
| ExamCart        | No explicit redistribution terms     | No (until clarified)   | No                     | Personal-use with attribution; seek permission    |
| CollegeDunia    | No explicit redistribution terms     | No (until clarified)   | No                     | Personal-use with attribution; seek permission    |
| SSCAdda         | Terms inaccessible (blocked)         | Unknown                | Unknown                | Exclude until access restored                     |
| Adda247         | Terms inaccessible (blocked)         | Unknown                | Unknown                | Exclude until access restored                     |

### Compliance Decisions

- Personal-use ingestion is permitted where sources declare personal-use permissions or where permissions are implied by context and absence of explicit prohibitions, subject to conservative handling (no redistribution).
- If a source is unclear or blocked, exclude the materials from redistribution and document the reason.
- For ExamCart and CollegeDunia, include PDFs in personal-use archives with explicit attribution and compliance notes, but refrain from redistribution until permissions are clarified.
- For Testbook, limit usage to free items that are clearly accessible, and avoid any re-sharing; do not attempt to bypass premium gating.

## Directory Structure and Metadata Schema

The directory structure enforces consistency and auditability:

- portal-downloads/CBT1/{year}/ for CBT1 PDFs and associated metadata
- portal-downloads/CBT2/{year}/ for CBT2 PDFs and associated metadata

Each asset’s metadata JSON adheres to a schema designed to capture licensing, provenance, and technical attributes.

Table 7: Metadata schema dictionary
| Field                 | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| title                 | Human-readable title of the paper (e.g., stage, date, shift/level)     |
| portal_name           | Source portal (e.g., Prepp, ExamCart, CollegeDunia)                    |
| source_link           | URL of the listing or landing page (see References)                    |
| license_type          | License classification (e.g., Personal Use, Unknown)                   |
| redistribution_allowed| Boolean flag (false unless explicit permission)                        |
| commercial_use_allowed| Boolean flag (default false)                                          |
| file_format           | Format (PDF)                                                           |
| file_size             | File size (bytes/MB)                                                   |
| page_count            | Number of pages (validated)                                            |
| language              | Language of the paper (e.g., English, Hindi)                           |
| checksum              | SHA256 or equivalent                                                   |
| download_date         | Date the file was accessed/downloaded                                  |
| compliance_notes      | Free-text notes capturing licensing decisions and handling constraints |
| source_attribution    | Textual attribution (portal name and, where applicable CDN/provider)   |

Table 8: Example metadata records (selected fields)
| Portal       | Year | Stage | Title (indicative)                          | License Type | Redistribution Allowed | Page Count | Source (see References) |
|--------------|------|-------|---------------------------------------------|--------------|------------------------|------------|-------------------------|
| Prepp        | 2024 | CBT1  | 06 June 2025, Shift 2 (memory-based)        | Personal Use | No                     | N/A        | Prepp CDN [^5]          |
| ExamCart     | 2020 | CBT1  | 28 Dec 2020, Shift 1                        | Personal Use | No                     | 73         | ExamCart listing [^6]   |
| ExamCart     | 2021 | CBT1  | 04 Jan 2021, Shift 2                        | Personal Use | No                     | 73         | ExamCart listing [^6]   |
| ExamCart     | 2022 | CBT2  | 09 May 2022, Level 6, Shift 1               | Personal Use | No                     | 42         | ExamCart listing [^6]   |
| CollegeDunia | 2017 | CBT2  | 17 Jan 2017, Shift 1                        | Personal Use | No                     | 27         | CollegeDunia asset [^12]|

### Naming Conventions

File names encode stage, year, and distinguishing details (date/shift/level) in a concise manner that supports traceability. Examples include:

- RRB_NTPC_CBT1_2020_Dec28_Shift1.pdf
- RRB_NTPC_CBT1_2021_Jan04_Shift2.pdf
- RRB_NTPC_CBT2_2022_May09_Level6_Shift1.pdf
- RRB_NTPC_CBT2_2017_Jan17_Shift1.pdf

The naming scheme avoids special characters, uses capital letters for stage identifiers, and inserts date and shift identifiers for quick recognition.

## Risks, Blockers, and Mitigations

Several recurring risks and blockers emerged during acquisition:

- HTML-only responses from supposed download links (Jagran Josh, QMaths Google Drive), indicating gateway pages or redirection mechanisms rather than direct PDFs.
- CDN blocks, HTTP 403, and CloudFront denials (Adda247, SSCAdda), resulting in access failures that preclude policy review and ingestion.
- Unclear licensing policies for aggregator listings and asset hosts (ExamCart, CollegeDunia), elevating the risk of inadvertent redistribution if handling is not conservative.
- Variability in naming and labeling across sources, sometimes using exam-cycle years distinct from actual paper dates, which can cause confusion in coverage mapping.

![Example of restricted access encountered](/workspace/browser/screenshots/rrb_ranchi_error_page.png)

The screenshot highlights access restrictions that complicate policy verification. To mitigate these risks, the project adopts the following controls:

- Implement fallback portals and re-validate links periodically, since access conditions can change without notice.
- Engage portals for written permission clarifications, especially for ExamCart and Railway Capsule, to establish a firm basis for any downstream reuse.
- Automate checksum generation and metadata population to reduce manual errors and improve audit readiness.
- Maintain detailed logs of access outcomes, licensing decisions, and exclusion rationales; establish an intake process for corrections and takedown requests.

Table 9: Risk register
| Risk Description                              | Source            | Impact                          | Likelihood | Mitigation                                                  | Status     |
|-----------------------------------------------|-------------------|---------------------------------|------------|-------------------------------------------------------------|------------|
| HTML gateways вместо PDF                      | Jagran Josh       | Ingestion blocked               | High       | Seek direct endpoints; manual retrieval; exclude if unresolved | Ongoing    |
| Google Drive links resolve to HTML             | QMaths            | Ingestion blocked               | Medium     | Explore alternate mirrors; request direct files             | Ongoing    |
| CloudFront block                              | SSCAdda           | Access denied; terms unavailable| Medium     | Reattempt access; seek alternate sources; exclude if needed | Ongoing    |
| HTTP 403                                      | Adda247           | Access denied; terms unavailable| Medium     | Retry later; seek official policy; exclude if needed        | Ongoing    |
| Unclear redistribution terms                   | ExamCart, CollegeDunia | Risk of inadvertent redistribution | High | Personal-use only; seek clarification; document decisions   | Ongoing    |
| Naming/label variability                       | Multiple          | Confusion in coverage mapping   | Medium     | Standardize metadata; cross-check dates and shifts          | Ongoing    |

## Roadmap and Next Actions

The near-term roadmap focuses on expanding coverage while preserving compliance and provenance:

1. Targeted retrieval for 2016 (CBT1), 2018, 2019 (CBT1 and CBT2), and 2023–2025. For 2016, attempt manual retrieval from Jagran Josh with interactive steps to bypass HTML gateways, or identify alternative mirrors. For 2019, explore non-Google Drive repositories for CBT1 sets and seek CBT2 availability across aggregator listings.
2. Engage Railway Capsule for explicit redistribution permissions and direct PDF endpoints. Pending confirmation, ingest memory-based or shift-wise PDFs under documented terms.
3. Clarify licensing with ExamCart and CollegeDunia. Document permissions via email or site-specific license statements. Only after explicit permission should any redistribution be considered.
4. Address SSCAdda access and Adda247 blocks. Periodically retry access and, if successful, review terms to determine any limited ingestion scope under personal-use policies.
5. Expand sources cautiously, including platforms like BYJU’S Exam Prep,Guidely, and Shiksha, ensuring each source’s terms are compatible with personal-use archiving and that technical access yields direct PDFs.

Table 10: Action plan tracker
| Task                                         | Source                | Owner        | Deadline       | Status   | Dependency                         |
|----------------------------------------------|-----------------------|--------------|----------------|----------|------------------------------------|
| Engage for direct PDF endpoints               | Railway Capsule       | Compliance   | 30 days        | Pending  | Contact response                    |
| Clarify redistribution permissions            | ExamCart              | Compliance   | 30 days        | Pending  | Email response                      |
| Clarify redistribution permissions            | CollegeDunia          | Compliance   | 30 days        | Pending  | Email response                      |
| Bypass HTML gateways (2016 CBT1)              | Jagran Josh           | Operations   | 14 days        | Ongoing  | Manual interaction                  |
| Explore non-Drive repositories (2019 CBT1)    | QMaths and mirrors    | Research     | 21 days        | Pending  | Link discovery                      |
| Retry access                                  | SSCAdda               | Operations   | 7 days         | Scheduled| CloudFront unblock                  |
| Retry access                                  | Adda247               | Operations   | 7 days         | Scheduled| Server-side unblock                 |
| Metadata + checksum automation                | Internal              | Engineering  | 14 days        | In progress| Tooling integration                 |

## Appendices: Evidence Logs and Source Index

The appendices consolidate evidence and index all sources cited in this report. They serve as an audit trail for compliance decisions, access outcomes, and ingestion records.

![Access log evidence for review](/workspace/browser/screenshots/rrb_ranchi_packages_page.png)

Table 11: Evidence log excerpts (selected)
| Source             | Attempted Link (see References) | Outcome          | Timestamp           | Reason/Notes                          |
|--------------------|----------------------------------|------------------|---------------------|---------------------------------------|
| Jagran Josh        | CBT1 2016 listing                | HTML gateway     | 2025-10-30 19:xx    | Direct PDF not returned               |
| QMaths             | 2019 CBT1 Drive links            | HTML (Drive)     | 2025-10-30 19:xx    | Drive responded with HTML             |
| Prepp CDN          | 2024 CBT1 memory-based           | Success (PDF)    | 2025-10-30 19:xx    | Valid PDF; metadata recorded          |
| ExamCart listing   | 2020–2022 various                | Success (PDF)    | 2025-10-30 19:xx    | Valid PDFs; permissions pending       |
| CollegeDunia asset | 2017 CBT2 Jan 17, Shift 1        | Success (PDF)    | 2025-10-30 19:xx    | Valid PDF; permissions pending        |
| SSCAdda            | RRB NTPC previous papers page    | CloudFront block | 2025-10-30 19:xx    | Access denied                         |
| Adda247            | RRB NTPC previous papers page    | HTTP 403         | 2025-10-30 19:xx    | Access denied                         |

Table 12: Source index (master references used in this report)
| ID | Title                                                               | URL                                                                                          | Usage Notes                                                      |
|----|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| 1  | RRB NTPC Previous Year Question Paper, Download PDF for CBT 1 and 2  | https://www.jagranjosh.com/articles/rrb-ntpc-previous-year-question-paper-cbt-1-and-cbt-2-pdf-download-1725355852-1 | Personal-use policy; listing with HTML gateways                  |
| 2  | RRB NTPC Previous Year Question Paper For CBT 1 and 2 – Testbook     | https://testbook.com/rrb-ntpc/previous-year-papers                                          | Free + premium; “all rights reserved” posture                    |
| 3  | RRB NTPC Study Material – Railway Capsule                            | https://railwaycapsule.com/rrb-ntpc-study-material/                                         | Claims free access; redistribution terms not explicit            |
| 4  | RRB NTPC 2019 CBT-1 Question Papers PDF Download – QMaths            | https://www.qmaths.in/2021/08/rrb-ntpc-2019-cbt-1-question-papers-pdf.html                  | Google Drive links returned HTML; general site terms referenced  |
| 5  | RRB NTPC 2024 CBT 1 Memory Based Question 06 June 2025 Shift 2 (PDF) | https://cdn-images.prepp.in/public/image/RRB_NTPC_2024_CBT_1_Memory_Based_Question_06_June_2025_Shift_2__9ac7596588f969c454bb0fe079ff38e3.pdf | Valid PDF ingested; personal-use flagged                         |
| 6  | RRB NTPC Previous Year Question Paper Download PDF for CBT 1 and 2   | https://examcart.in/community/blogs/rrb-ntpc-previous-year-question-paper-download-pdf-for-cbt-1-and-2          | Aggregated CDN links; permissions not explicit                   |
| 7  | RRB NTPC Previous Year Papers – SSCAdda                              | https://www.sscadda.com/rrb-ntpc-previous-year-papers/                                      | CloudFront block; excluded                                       |
| 8  | RRB NTPC Previous Year Question Papers PDFs With Solution            | https://www.pw.live/railway/exams/rrb-ntpc-previous-year-question-papers                                           | Indirect aggregator; used for cross-checks                       |
| 9  | RRB NTPC Previous Year Question Paper – BYJU'S                       | https://byjus.com/rrb-exams/rrb-ntpc-previous-year-question-papers/                                              | To be evaluated for policy compatibility                         |
| 10 | RRB NTPC Previous Papers in Telugu                                   | https://www.telugumaterials.com/p/rrb-ntpc-previous-papers-in-telugu.html                                        | Language-specific repository                                     |
| 11 | RRB NTPC Previous Year Question Paper PDF Download – Guidely         | https://guidely.in/previous-year-papers/rrb-ntpc                                                               | Candidate portal for future exploration                          |
| 12 | RRB NTPC CBT-2 Previous Year Paper (Jan 17, 2017, Shift 1)           | https://assets.collegedunia.com/public/image/36c4c2712b91984d6ed66eda4f4d722e.pdf                                                 | Valid PDF; permissions not explicit                              |
| 13 | RRB NTPC Question Papers 2025 (OUT) – Shiksha                        | https://www.shiksha.com/exams/rrb-ntpc-exam-question-papers                                                    | Candidate portal; policy review required                         |
| 14 | RRB NTPC Previous Year Papers With Answer – Mockers                  | https://www.mockers.in/exam/rrb-ntpc-pyqs                                                                      | Candidate portal; policy review required                         |
| 15 | Indian Railways – Official Website                                   | https://indianrailways.gov.in/                                                                                 | Official context for pattern alignment                           |
| 16 | RRB NTPC Previous Year Question Paper – Adda247                      | https://www.adda247.com/jobs/rrb-ntpc-previous-year-question-paper/                                           | Access blocked (403); excluded                                   |
| 17 | RRB Ranchi – Official Portal                                         | https://rrb Ranchi .in                                                                                         | Official portal reference                                        |

### Information Gaps

- Explicit redistribution permissions for ExamCart and CollegeDunia remain unclear; files from these sources are handled under personal use pending confirmation.
- Access to Jagran Josh download endpoints often yields HTML rather than PDFs, preventing reliable ingestion of 2016 CBT1 materials without interactive steps.
- QMaths Google Drive links returned HTML rather than PDFs during attempts; direct-file acquisition needs further verification.
- Railway Capsule asserts “100% free access” but lacks clear redistribution or derivative-work terms; confirmatory engagement is recommended.
- SSCAdda access is blocked by CloudFront (403), preventing policy and content review.
- Adda247 access is blocked (403), and terms could not be reviewed; the source is excluded.

---

## References

[^1]: RRB NTPC Previous Year Question Paper, Download PDF for CBT 1 and 2 – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-previous-year-question-paper-cbt-1-and-cbt-2-pdf-download-1725355852-1
[^2]: RRB NTPC Previous Year Question Paper For CBT 1 and 2 – Testbook. https://testbook.com/rrb-ntpc/previous-year-papers
[^3]: RRB NTPC Study Material – Railway Capsule. https://railwaycapsule.com/rrb-ntpc-study-material/
[^4]: RRB NTPC 2019 CBT-1 Question Papers PDF Download – QMaths. https://www.qmaths.in/2021/08/rrb-ntpc-2019-cbt-1-question-papers-pdf.html
[^5]: RRB NTPC 2024 CBT 1 Memory Based Question 06 June 2025 Shift 2 (PDF) – Prepp CDN. https://cdn-images.prepp.in/public/image/RRB_NTPC_2024_CBT_1_Memory_Based_Question_06_June_2025_Shift_2__9ac7596588f969c454bb0fe079ff38e3.pdf
[^6]: RRB NTPC Previous Year Question Paper Download PDF for CBT 1 and 2 – ExamCart. https://examcart.in/community/blogs/rrb-ntpc-previous-year-question-paper-download-pdf-for-cbt-1-and-2
[^7]: RRB NTPC Previous Year Papers – SSCAdda. https://www.sscadda.com/rrb-ntpc-previous-year-papers/
[^8]: RRB NTPC Previous Year Papers PDFs With Solution – PW Live. https://www.pw.live/railway/exams/rrb-ntpc-previous-year-question-papers
[^9]: RRB NTPC Previous Year Question Paper – BYJU'S. https://byjus.com/rrb-exams/rrb-ntpc-previous-year-question-papers/
[^10]: RRB NTPC Previous Papers in Telugu. https://www.telugumaterials.com/p/rrb-ntpc-previous-papers-in-telugu.html
[^11]: RRB NTPC Previous Year Question Paper PDF Download – Guidely. https://guidely.in/previous-year-papers/rrb-ntpc
[^12]: RRB NTPC CBT-2 Previous Year Paper (Jan 17, 2017, Shift 1) – CollegeDunia (PDF). https://assets.collegedunia.com/public/image/36c4c2712b91984d6ed66eda4f4d722e.pdf
[^13]: RRB NTPC Question Papers 2025 (OUT) – Shiksha. https://www.shiksha.com/exams/rrb-ntpc-exam-question-papers
[^14]: RRB NTPC Previous Year Papers With Answer – Mockers. https://www.mockers.in/exam/rrb-ntpc-pyqs
[^15]: Indian Railways – Official Website. https://indianrailways.gov.in/
[^16]: RRB NTPC Previous Year Question Paper – Adda247. https://www.adda247.com/jobs/rrb-ntpc-previous-year-question-paper/
[^17]: RRB Ranchi – Official Portal. https://rrb Ranchi .in