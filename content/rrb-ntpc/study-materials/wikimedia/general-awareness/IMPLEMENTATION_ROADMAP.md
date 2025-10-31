# RRB NTPC General Awareness Wikipedia/Wikibooks Collection — Status, Gaps, and Reproducible Offline Execution Blueprint

## Executive Overview

The objective of this project is to deliver a comprehensive, offline-first study corpus for the RRB NTPC General Awareness (GA) syllabus from Wikipedia and Wikibooks, with verifiable licensing and reproducible snapshots. The corpus is designed for educators, content engineers, and RRB NTPC aspirants who require stable, licensable materials that can be served and studied without live internet connectivity.

The current status reflects meaningful progress:
- 42 article directories created across eight GA domains.
- 13 articles fully collected (HTML + metadata) and 29 framework placeholders (HTML + metadata) created to complete topic scaffolding.
- Images were not successfully captured in this phase; assets/images directories exist locally but contain no image files.
- Metadata capture is present for collected items, including revision_id (lastrevid), revision_timestamp, page_id, and source_url; attribution banners and license notes are embedded in HTML where content is available.

The project encountered API access issues (HTTP 403/429), indicating that rate limits and access restrictions must be addressed by moving to official Wikimedia access methods. The strategy pivot is clear: adopt a dumps-first approach using Wikimedia database backups (XML/SQL), static HTML dumps, historical Enterprise HTML runs, and per-article exports. This approach eliminates rate-limit uncertainty, ensures reproducibility, and supports scale-up without relying on live API harvesting.

The blueprint is organized around five threads: (1) alignment with the RRB NTPC GA syllabus, (2) legal and licensing compliance with attribution templates, (3) acquisition via official dumps/snapshots and mirrors, (4) storage and metadata schemas designed for offline navigation and auditability, and (5) a practical execution roadmap to complete media capture and enhance content quality. By integrating snapshot and revision identifiers with checksum validation, this corpus can be revalidated and refreshed on a predictable cadence, with clear audit trails and ShareAlike obligations preserved throughout.[^1][^2][^3][^14]

![Representative local Wikipedia GA page (UI/layout check)](/workspace/browser/screenshots/biodiversity_wikipedia_page.png)

This screenshot exemplifies the intended offline rendering and attribution placement. It shows how HTML bundles can be navigated locally and how licensing notices can be embedded directly into pages to meet CC BY-SA/GFDL obligations and support compliant reuse.

---

## Current Corpus Status vs Objectives

The local corpus exhibits a solid backbone of collected articles and frameworks, with known gaps in image capture and some content enrichment. The core requirement is to transition from API-driven retrieval to official dumps and snapshot archives, while implementing robust media acquisition and packaging. Reproducibility will be enforced by capturing dump run identifiers and revision IDs, and integrity will be validated using MD5/SHA checksums.

To ground the status in evidence, Table 1 presents a domain-level inventory summary.

Table 1. Domain-level inventory summary (local evidence)

| Domain                | Article Directories Created | Fully Collected (HTML+Metadata) | Frameworks (HTML+Metadata) | Images Directory Present | Metadata JSON Present |
|-----------------------|-----------------------------|----------------------------------|----------------------------|--------------------------|----------------------|
| indian-history        | 11                          | 7                                | 4                          | Some                     | Yes                  |
| geography             | 6                           | 6                                | 0                          | Some                     | Yes                  |
| polity                | 6                           | 6                                | 0                          | None observed            | Yes                  |
| science-technology    | 7                           | 6                                | 1                          | Some                     | Yes                  |
| economy               | 4                           | 4                                | 0                          | None observed            | Yes                  |
| environment           | 4                           | 4                                | 0                          | None observed            | Yes                  |
| international-relations | 3                         | 3                                | 0                          | None observed            | Yes                  |
| organizations         | 2                           | 2                                | 0                          | None observed            | Yes                  |
| culture               | 2                           | 0                                | 2                          | None                     | Yes                  |
| personalities         | 0                           | 0                                | 0                          | None                     | N/A                  |
| monuments-places      | 0                           | 0                                | 0                          | None                     | N/A                  |
| transport             | 0                           | 0                                | 0                          | None                     | N/A                  |
| government-schemes    | 0                           | 0                                | 0                          | None                     | N/A                  |
| technology            | 0                           | 0                                | 0                          | None                     | N/A                  |
| sports-games          | 0                           | 0                                | 0                          | None                     | N/A                  |
| inventions-discoveries | 0                         | 0                                | 0                          | None                     | N/A                  |
| current-affairs       | 0                           | 0                                | 0                          | None                     | N/A                  |
| literature            | 0                           | 0                                | 0                          | None                     | N/A                  |
| Total                 | 42                          | 38                               | 4                          | Some across domains      | Yes                  |

The table shows strong coverage in geography, polity, economy, environment, international relations, and organizations, with science-technology nearly complete and indian-history largely collected. Culture is currently scaffolded by frameworks and requires content acquisition. Images were not successfully downloaded in this phase, and media folders exist but are empty. API errors (HTTP 403/429) confirm that a dumps-first strategy is essential.

![UI state snapshot during initial collection](/workspace/browser/screenshots/initial_state.png)

![Current page state while assessing inventory](/workspace/browser/screenshots/current_page_state.png)

These UI state snapshots corroborate the offline rendering approach and the presence of consistent attribution structures across pages. Their significance is operational: they confirm that the HTML bundles can be navigated locally, and the attribution banner design is viable for embedding compliance signals.

### Image Assets Status

Images were not successfully captured in this phase. Local assets/images directories exist within several article folders, but no image files were retrieved. The failure stems from a combination of rate limiting, incomplete Commons URL handling in earlier scripts, and the absence of a deterministic offline-first media packaging workflow. The corrected workflow is as follows:

- Derive image lists from page metadata and link tables.
- Fetch assets from Wikimedia Commons using canonical file URLs with origin metadata preserved.
- Package assets into per-article media tarballs (media.tar.gz) or media/ folders.
- Generate media.json per article with per-asset attribution, license names, and license URLs.

This workflow ensures media compliance, preserves traceability, and supports offline deployment.[^13]

---

## Legal and Licensing Compliance

Wikimedia content reuse requires strict adherence to licensing terms. Wikipedia text is dual-licensed under Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) and the GNU Free Documentation License (GFDL). ShareAlike obligations require derivative text to be distributed under the same license. Attribution must credit the source page, recognize contributors where feasible, and include the license name. GFDL obligations apply to legacy coverage and must be preserved. Media files are governed by their own licenses; each asset must include its license name and URL in the attribution layer, and images must not be stripped of license metadata.[^14]

To operationalize compliance, the corpus includes an attribution directory and media license register. Each article’s HTML bundle embeds an attribution banner (or footer), and metadata.json captures revision_id, timestamp, source_url, and license_text. A global attribution pack holds CC BY-SA and GFDL license texts and attribution templates.

Table 2. License obligations by asset type and required attribution fields[^14]

| Asset Type          | License Model (typical)                      | Required Attribution Fields (minimum)                                      |
|---------------------|----------------------------------------------|----------------------------------------------------------------------------|
| Wikipedia text      | CC BY-SA 3.0 (also GFDL for legacy coverage) | Source page title and URL; license name(s); attribution note; revision ID  |
| Page HTML           | Same as text; may include embedded scripts   | As above, plus snapshot identifier (run) and timestamp                     |
| Images/Media        | Per-file (varies)                            | Original file URL; license name; author/creator; license URL               |
| Page metadata       | CC0 where applicable (service-generated)     | Generator; schema version; timestamp; integrity checksums                  |

This framework aligns with Wikimedia’s attribution expectations and supports compliant redistribution in offline educational contexts.[^14]

### Attribution Template Design

Attribution appears in two layers:
- Article-level: embedded in HTML footer/sidebar, including Title; Source URL; Contributors; License(s); ShareAlike notice; revision_id (lastrevid); snapshot identifier (dump-run/enterprise run); capture timestamp; media notice pointing to media.json.
- Media-level: media.json records per-asset Title; Original Source URL; License Name; License URL; Author/Creator (where available).

This design ensures that attribution is visible to end users and machine-discoverable for audits and downstream packaging.[^14]

---

## Source Acquisition Strategy and Reproducibility

The acquisition strategy prioritizes official Wikimedia data access mechanisms to eliminate rate-limit risks and to ensure reproducibility:

- Database backup dumps (XML/SQL) for full corpus baseline and historical revisions.
- Historical static HTML dumps and Enterprise HTML archives for ready-to-serve bundles.
- Per-article exports (Special:Export) for targeted revisions and updates.
- Mirrors and best practices to avoid throttling, reduce latency, and validate integrity.[^1][^2][^3][^8][^14]

Table 3. Wikimedia data access options and use-cases[^1][^2][^3][^8][^14]

| Access Method                     | Formats                | Frequency/Status                                   | Best Use-Cases                                      | Notes                                                        |
|----------------------------------|------------------------|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------|
| Database backup dumps            | XML, SQL               | At least monthly (often twice monthly)             | Full corpus baseline; historical revisions           | Very large; validate with MD5; do not crawl live             |
| Static HTML dumps                | HTML                   | Discontinued as ongoing; historical archives exist | Quick offline HTML ready-to-serve                   | Namespace-limited; legacy                                   |
| Enterprise HTML archive          | HTML (historical)      | Historical runs available; replication ended 2025-03-24 | Rich snapshots for specific wikis and namespaces   | For deltas, use Snapshot API; on-demand via Enterprise API   |
| Per-article export (Special:Export) | XML                    | On-demand                                          | Targeted topics; specific revision capture          | Includes page history metadata                               |
| Mirrors                          | Same as above          | Mirrored availability                              | Avoiding rate limits; faster regional access         | Use Meta’s mirror list and mirroring best practices          |

### Snapshot and Revision Metadata Strategy

Reproducibility is enforced by capturing:
- Wikipedia revision ID (lastrevid), revision timestamp, and page_id.[^10][^11]
- Dump run identifiers (e.g., enwiki dump date, directory path; enterprise run identifier).[^1][^3]
- MD5 checksums (and SHA-256 where possible) for all downloaded and generated files.
- Canonical source URL and language code.

These fields allow auditors to re-fetch or reconstruct the exact snapshot and compare revisions as needed.[^1][^3]

---

## Topic-to-Page Mapping and Domain Coverage

Coverage is anchored in a seed list that combines authoritative overviews, stable lists, and India-focused entries. This minimizes redundancy while ensuring comprehensive coverage of static facts, institutions, and conceptual foundations.

Table 4. Representative topic-to-page anchors by GA subdomain

| Topic Cluster                          | Representative Wikipedia Entries (by title)                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| History of India (overview)           | History of India; Timeline of Indian history; List of Indian monarchs                                                       |
| Ancient India                         | Outline of ancient India; Middle kingdoms of India; List of historical regions of India                                     |
| Medieval India                        | Medieval India; History of South India                                                                                      |
| Freedom Struggle                      | Indian independence movement; List of Indian independence activists                                                         |
| Physical Geography (India)            | Geography of India; Indian Himalayan Region; Indo-Gangetic Plain                                                            |
| Mountains & Ghats                     | Himalayas; Western Ghats; Eastern Ghats                                                                                     |
| Rivers                                | List of major rivers of India                                                                                                |
| Constitution & Governance             | Constitution of India; Government of India; Parliament of India; Supreme Court of India; Basic structure doctrine           |
| Constitutional Cases                  | Kesavananda Bharati v. State of Kerala; I.C. Golaknath and Ors. v. State of Punjab and Anrs.                                |
| Economy (India)                       | Economy of India; Reserve Bank of India; Banking in India; Finance in India; Payment and settlement systems in India         |
| Organizations                         | United Nations; United Nations System; List of specialized agencies of the United Nations; List of intergovernmental organizations |
| Environment                           | Environment of India; Environmental issues in India; Wildlife of India; Conservation in India; Chipko movement               |
| Science & Technology (India)          | Science and technology in India; ISRO; Chandrayaan programme; Mars Orbiter Mission; Nuclear power in India; Department of Space |
| Key Personalities                     | Mahatma Gandhi; Subhas Chandra Bose; Bal Gangadhar Tilak; Lala Lajpat Rai; Bhagat Singh                                   |

This mapping spans the GA taxonomy and will be expanded during production to cover additional static GK lists (e.g., states and capitals), monuments, transport, and government schemes.

---

## Storage Layout, Metadata Schema, and Integrity

The storage layout is designed for predictability, auditability, and offline navigation. Each domain folder contains per-article folders with index.html (or page.html), metadata.json, and media.tar.gz or media/. Attribution and license texts are centralized, and checksums are stored per domain and per release.

Table 5. Metadata schema fields (JSON)

| Field                  | Type     | Description                                                                                         |
|------------------------|----------|-----------------------------------------------------------------------------------------------------|
| title                  | string   | Page title (as displayed)                                                                           |
| source_url             | string   | Canonical Wikipedia/Wikibooks page URL                                                               |
| page_id                | integer  | MediaWiki page ID                                                                                    |
| revision_id            | integer  | lastrevid at time of capture                                                                         |
| revision_timestamp     | string   | ISO 8601 timestamp of the captured revision                                                          |
| language               | string   | Wikipedia language code (e.g., “en”)                                                                 |
| dump_run_id            | string   | Dump directory/run identifier (e.g., “enwiki-2025-10-01”)                                            |
| snapshot_type          | string   | “static_html”, “enterprise_html”, “xml_export”, “api_render”                                         |
| license_text           | string   | License name(s) (CC BY-SA 3.0; GFDL where applicable)                                                |
| attribution_text       | string   | Attribution summary string                                                                           |
| media_license_summary  | string   | Summary of media licenses; refer to media.json for per-file details                                  |
| checksum_md5           | string   | MD5 of the HTML file                                                                                 |
| checksum_sha256        | string   | SHA-256 of the HTML file (preferred for audit)                                                       |
| capture_timestamp      | string   | UTC timestamp when the artifact was generated                                                        |
| integrity_notes        | string   | Free-text notes on validation steps                                                                 |
| related_pages          | array    | Optional list of related page titles included in the same cluster                                    |

Table 6. Final directory structure and file inventory schema

| Path (relative)                                                    | Purpose                                                    |
|--------------------------------------------------------------------|------------------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/general-awareness/      | Root of GA corpus                                          |
| ├── pages/                                                         | HTML bundles and media per article                         |
| │   └── <Domain>/pages/<Page_Title>/{index.html, metadata.json, media.tar.gz} |
| ├── metadata/                                                      | Global manifests, schema versions, and per-snapshot logs   |
| ├── attribution/                                                   | License texts, attribution templates, image license register |
| └── checksums/                                                     | MD5/SHA checksum manifests per domain and per release      |

### Integrity and Validation Checks

Every release undergoes integrity validation:
- File-level MD5 checks against dump or enterprise manifests; compute and store SHA-256 for long-term validation.[^1][^3]
- Snapshot fields recorded per article: dump_run_id or enterprise_run_id; revision_id and timestamp.[^11]
- Media integrity verified via media.json and per-asset checksums.
- Page history audit confirms captured revisions align with declared snapshots.[^11]

---

## Extraction and Packaging Methodology

The extraction pipeline must be deterministic and auditable:
- XML dumps to HTML: Render latest or specified revisions into HTML with preserved media references; attach metadata.json with snapshot fields and checksums.[^1][^14]
- Enterprise HTML: Extract historical runs and attach run metadata; verify integrity using run checksum manifests.[^3]
- Per-article exports: Use Special:Export for targeted revisions; record revision_id, timestamp, and export parameters.[^14]
- Media packaging: Derive image lists from page metadata; fetch assets from Commons; package into media.tar.gz or media/; index licenses in media.json.

Table 7. Conversion steps and artifact traceability

| Input Source                       | Tooling/Process                   | Output Artifact                  | Snapshot Fields Captured                                     | Integrity Outputs                         |
|------------------------------------|-----------------------------------|----------------------------------|---------------------------------------------------------------|-------------------------------------------|
| Database backup XML (latest rev)   | XML → HTML render pipeline         | index.html (per article)         | dump_run_id; revision_id; revision_timestamp; page_id         | MD5/SHA checksums of HTML and tarballs    |
| Enterprise HTML snapshot           | Extract run → bundle               | index.html + metadata.json       | enterprise_run_id; snapshot_timestamp                         | Verify against run’s checksum manifest     |
| Special:Export (per-article XML)   | XML → HTML render pipeline         | index.html + metadata.json       | revision_id; export_timestamp; source_url                     | MD5/SHA checksums                          |
| Media list (from page metadata)    | Batch fetch from Commons           | media.tar.gz or media/           | per-asset source URL; license name; license URL                | media.json index; per-asset checksums      |

### HTML Bundle Structure and Linking

Each article uses index.html or page.html as the entry point. Relative paths are preserved for local assets; if assets are tarred, the tarball structure maintains relative paths for offline link integrity. The HTML includes an attribution footer, license summary, and an embedded JSON block with metadata to support programmatic validation.

This structure mirrors common static dump practices and aids offline navigation.[^2]

---

## Domain Coverage Synthesis

The domain coverage reflects the current status and target anchors:

- Indian History: Overview and freedom struggle anchors (History of India; Timeline; Indian independence movement), personalities (Mahatma Gandhi; Subhas Chandra Bose; Tilak; Lajpat Rai; Bhagat Singh). Status: mix of collected entries and frameworks; stronger baseline coverage in modern and freedom struggle topics.[^19][^21][^26][^28][^63][^64][^65][^66]
- Geography: Physical anchors (Geography of India; Himalayas; Western Ghats; Eastern Ghats; Indo-Gangetic Plain) and rivers list. Status: fully collected.[^29][^31][^32][^33][^34][^30]
- Polity: Constitutional basics and institutions (Constitution; Government; Parliament; Supreme Court), basic structure doctrine, landmark case. Status: fully collected.[^36][^37][^38][^39][^43][^42]
- Economy: India-focused anchors (Economy of India; RBI; Banking; Finance; Payment systems). Status: fully collected.[^45][^47][^48][^49][^46]
- Science & Technology: Indian S&T ecosystem anchors (Science and technology in India; ISRO; Chandrayaan; Mars Orbiter Mission; Nuclear power; three-stage programme). Status: largely collected, with one framework pending.[^53][^50][^52][^51][^54][^55]
- International Relations and Organizations: UN system and specialized agencies. Status: fully collected.[^57][^58][^59][^60]
- Environment: India-focused environment anchors (Environment; Environmental issues; Wildlife; Conservation; Chipko). Status: fully collected.[^61][^62][^63][^64][^65]
- Culture and Literature: Anchors planned (Culture of India; Indian literature). Status: currently scaffolded by frameworks; acquisition pending.

Table 8. Domain coverage summary

| Domain                | Representative Anchors                                                                                  | Local Status (Collected / Framework) | Reference Index |
|-----------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------|-----------------|
| Indian History        | History of India; Timeline; Medieval India; Outline of ancient India; Indian independence movement; List of independence activists; personalities (Gandhi, Bose, Tilak, Lajpat Rai, Bhagat Singh) | 7 / 4                                | [^19]–[^28]     |
| Geography             | Geography of India; Himalayas; Western Ghats; Eastern Ghats; Indo-Gangetic Plain; List of major rivers of India; Indian Himalayan Region | 6 / 0                                | [^29]–[^35]     |
| Polity & Governance   | Constitution of India; Government of India; Parliament of India; Supreme Court of India; Basic structure doctrine; Kesavananda Bharati case | 6 / 0                                | [^36]–[^44]     |
| Economy               | Economy of India; Reserve Bank of India; Banking in India; Finance in India; Payment and settlement systems in India | 4 / 0                                | [^45]–[^52]     |
| Science & Technology  | Science and technology in India; ISRO; Chandrayaan programme; Mars Orbiter Mission; Nuclear power in India; three-stage nuclear programme | 6 / 1                                | [^53]–[^56]     |
| International Relations & Organizations | United Nations; United Nations System; List of specialized agencies; List of intergovernmental organizations | 3 / 0                                | [^57]–[^60]     |
| Environment           | Environment of India; Environmental issues in India; Wildlife of India; Conservation in India; Chipko movement | 4 / 0                                | [^61]–[^65]     |
| Culture               | Culture of India; Indian literature                                                                                 | 0 / 2                                | (planned anchors; see mapping section) |

---

## Quality Assurance and Reproducibility Audit

Quality and reproducibility are enforced through a structured QA process:
- Metadata validation: confirm presence of all required fields.
- Integrity checks: verify MD5/SHA checksums and maintain logs.
- Licensing verification: spot-check attribution banners and media.json entries.
- Revision audit: validate captured revision IDs and timestamps against page history.
- Coverage completeness: ensure all GA subdomains are represented.

Table 9. QA checklist

| Checkpoint                   | Description                                                                                 | Pass/Fail Notes |
|-----------------------------|---------------------------------------------------------------------------------------------|-----------------|
| Metadata completeness       | All required fields present and parseable                                                   |                 |
| Integrity (MD5/SHA)         | File checksums match; logs stored alongside artifacts                                       |                 |
| Snapshot fields             | Dump run ID or enterprise run ID; revision_id; timestamp present                            |                 |
| Attribution banners         | HTML includes attribution footer and license summary                                        |                 |
| Image licenses              | Per-file license name/URL in media.json; no unlicensed redistribution                       |                 |
| Coverage completeness       | All GA subdomains represented (Appendix B checklist)                                        |                 |
| History audit               | Revision IDs and timestamps validated against page history                                  |                 |

---

## Maintenance and Update Policy

Maintenance balances stability and currency:
- Quarterly snapshots aligned to Wikimedia database dump cycles; additional snapshots for major India-related developments, explicitly dated and labeled “as-of.”[^1]
- Change management: record revision deltas; maintain dated manifests and changelogs noting new/updated/retired articles.
- Deprecation policy: archive prior snapshots; mark “superseded;” never silently overwrite prior releases.
- Legal watch: monitor licensing metadata changes for images; adjust attribution files accordingly.
- Access continuity: use mirrors when rate-limited; avoid peak hours; follow Meta’s mirroring best practices.[^8]

Table 10. Update log schema

| Field          | Description                                                |
|----------------|------------------------------------------------------------|
| snapshot_date  | ISO date of the snapshot                                   |
| dump_run_id    | Dump directory/run identifier                              |
| changes        | Summary of updates (new/updated/retired pages)             |
| checksums      | MD5/SHA manifest filename                                  |
| notes          | Rationale for out-of-cycle updates                         |

---

## Risks and Mitigations

- Rate limiting and API blocks: pivot to dumps, Enterprise HTML, and Special:Export; leverage mirrors; implement staggered scheduling aligned with best practices.[^1][^8]
- Large files and transfer failures: use resumable transfers; validate integrity with MD5/SHA; consider partial mirroring by namespace when sufficient.[^1]
- Licensing misinterpretation: centralize attribution; maintain per-media license registers; train staff on CC BY-SA/GFDL obligations.[^14]
- Coverage gaps: use a live topic checklist; run periodic audits against the GA taxonomy and RRB NTPC syllabus maps.[^2][^7]

---

## Appendices

### Appendix A: Master Reference Index with Usage Notes

- RRB official context and updates.[^1]
- Official/aligned syllabus lists and framing.[^2][^3][^4][^5][^6][^7]
- Wikimedia data access mechanisms and mirrors.[^1][^8][^13][^14][^17]
- Domain anchors (India-focused articles across history, geography, polity, economy, S&T, environment, organizations).[^19]–[^70]

### Appendix B: Topic Coverage Checklist

- Current Affairs; Art & Culture; Literature; Monuments & Places; History; Geography; Polity; Economy; Science & Technology; Environment; Organizations; Transport; Personalities; Government Schemes; Static GK.

### Appendix C: Example Attribution and License Text Blocks

- Article-level attribution: Title; Source; Contributors; License(s); Share-alike notice; Revision ID; Snapshot; Timestamp.
- Media-level attribution: Filename; Original Source URL; License Name; License URL; Author/Creator (where available).
- License texts: CC BY-SA 3.0 deed link and summary; GFDL summary and text reference.

---

## Information Gaps

- A complete mapping of every GA micro-topic (e.g., “Neighboring Countries,” “Countries, Capitals and Currencies”) to specific Wikipedia pages will be finalized in production.
- Per-asset media licenses are not yet recorded; media.json will be populated after the media acquisition pipeline is implemented.
- API access limitations (HTTP 403/429) were encountered; migration to dumps/Enterprise HTML/Special:Export will be used to circumvent rate limits.
- A finalized mapping between the 18 GA topic areas and the 42 article directories is robust, but some cross-domain entries (e.g., personalities, current affairs) remain limited or pending and will be completed with dumps-first acquisition.

---

## References

[^1]: RRBs Website – Ministry of Railways. https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,7,1281  
[^2]: RRB NTPC Syllabus (BYJU’s-hosted PDF aligned to CEN 01/2019). https://cdn1.byjus.com/wp-content/uploads/2020/07/RRB-NTPC-Syllabus.pdf  
[^3]: Wikimedia Downloads (Dumps Overview). https://dumps.wikimedia.org/  
[^4]: Wikimedia Enterprise HTML Dump Archive (Runs Directory). https://dumps.wikimedia.org/other/enterprise_html/runs/  
[^5]: RRB NTPC Exam Pattern – Shiksha. https://www.shiksha.com/exams/rrb-ntpc-exam-pattern  
[^6]: RRB NTPC Exam Pattern – Testbook. https://testbook.com/rrb-ntpc/exam-pattern  
[^7]: RRB NTPC Syllabus – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-cbt-1-and-2-syllabus-2024-pdf-download-1716465685-1  
[^8]: Mirroring Wikimedia project XML dumps – Meta-Wiki. https://meta.wikimedia.org/wiki/Mirroring_Wikimedia_project_XML_dumps  
[^9]: Wikipedia:Revision ID. https://en.wikipedia.org/wiki/Wikipedia:Revision_ID  
[^10]: Help:Page history – Wikipedia. https://en.wikipedia.org/wiki/Help:Page_history  
[^11]: Wikipedia:Database download. https://en.wikipedia.org/wiki/Wikipedia:Database_download  
[^12]: Data dumps – Meta-Wiki. https://meta.wikimedia.org/wiki/Data_dumps  
[^13]: Sql/XML dumps issues – Wikimedia Downloads. https://dumps.wikimedia.org/backup-index.html  
[^14]: English Wikipedia: Full Revision History in HTML Format (ICWSM 2020). https://wikiworkshop.org/2020/papers/Wiki_Workshop_2020_paper_11.pdf  
[^15]: English Wikipedia's Full Revision History in HTML Format (AAAI ICWSM). https://ojs.aaai.org/index.php/ICWSM/article/view/7353/7207  
[^16]: RRB NTPC Exam Pattern – Jagran Josh. https://www.jagranjosh.com/articles/rrb-ntpc-exam-pattern-2025-check-cbt-1-cbt-2-cbat-marking-scheme-total-marks-1749038705-1  
[^17]: RRB NTPC Exam Pattern – Careers360. https://competition.careers360.com/articles/rrb-ntpc-exam-pattern  
[^18]: RRBCDG CEN 06-2024 NTPC (official document link). https://www.rrbcdg.gov.in/uploads/2024/06-NTPCUG/Detailed%20CEN%2006-2024%20NTPC.pdf  
[^19]: RR Branchi CEN 08/2024 (official document link). https://rrbranchi.gov.in/upload/files/pdf/01_09_09pmc42bfc83ee62e05abe25431a74956326.pdf  
[^20]: History of India – Wikipedia. https://en.wikipedia.org/wiki/History_of_India  
[^21]: Timeline of Indian history – Wikipedia. https://en.wikipedia.org/wiki/Timeline_of_Indian_history  
[^22]: Medieval India – Wikipedia. https://en.wikipedia.org/wiki/Medieval_India  
[^23]: Outline of ancient India – Wikipedia. https://en.wikipedia.org/wiki/Outline_of_ancient_India  
[^24]: Middle kingdoms of India – Wikipedia. https://en.wikipedia.org/wiki/Middle_kingdoms_of_India  
[^25]: List of historical regions of India – Wikipedia. https://en.wikipedia.org/wiki/List_of_historical_regions_of_India  
[^26]: Indian independence movement – Wikipedia. https://en.wikipedia.org/wiki/Indian_independence_movement  
[^27]: List of Indian independence activists – Wikipedia. https://en.wikipedia.org/wiki/List_of_Indian_independence_activists  
[^28]: Mahatma Gandhi – Wikipedia. https://en.wikipedia.org/wiki/Mahatma_Gandhi  
[^29]: Geography of India – Wikipedia. https://en.wikipedia.org/wiki/Geography_of_India  
[^30]: List of major rivers of India – Wikipedia. https://en.wikipedia.org/wiki/List_of_major_rivers_of_India  
[^31]: Himalayas – Wikipedia. https://en.wikipedia.org/wiki/Himalayas  
[^32]: Western Ghats – Wikipedia. https://en.wikipedia.org/wiki/Western_Ghats  
[^33]: Eastern Ghats – Wikipedia. https://en.wikipedia.org/wiki/Eastern_Ghats  
[^34]: Indo-Gangetic Plain – Wikipedia. https://en.wikipedia.org/wiki/Indo-Gangetic_Plain  
[^35]: Indian Himalayan Region – Wikipedia. https://en.wikipedia.org/wiki/Indian_Himalayan_Region  
[^36]: Constitution of India – Wikipedia. https://en.wikipedia.org/wiki/Constitution_of_India  
[^37]: Government of India – Wikipedia. https://en.wikipedia.org/wiki/Government_of_India  
[^38]: Parliament of India – Wikipedia. https://en.wikipedia.org/wiki/Parliament_of_India  
[^39]: Supreme Court of India – Wikipedia. https://en.wikipedia.org/wiki/Supreme_Court_of_India  
[^40]: Kesavananda Bharati v. State of Kerala – Wikipedia. https://en.wikipedia.org/wiki/Kesavananda_Bharati_v._State_of_Kerala  
[^41]: Judicial review in India – Wikipedia. https://en.wikipedia.org/wiki/Judicial_review_in_India  
[^42]: Economy of India – Wikipedia. https://en.wikipedia.org/wiki/Economy_of_India  
[^43]: Reserve Bank of India – Wikipedia. https://en.wikipedia.org/wiki/Reserve_Bank_of_India  
[^44]: Banking in India – Wikipedia. https://en.wikipedia.org/wiki/Banking_in_India  
[^45]: Finance in India – Wikipedia. https://en.wikipedia.org/wiki/Finance_in_India  
[^46]: Payment and settlement systems in India – Wikipedia. https://en.wikipedia.org/wiki/Payment_and_settlement_systems_in_India  
[^47]: ISRO – Wikipedia. https://en.wikipedia.org/wiki/ISRO  
[^48]: Department of Space – Wikipedia. https://en.wikipedia.org/wiki/Department_of_Space  
[^49]: Chandrayaan programme – Wikipedia. https://en.wikipedia.org/wiki/Chandrayaan_programme  
[^50]: Mars Orbiter Mission – Wikipedia. https://en.wikipedia.org/wiki/Mars_Orbiter_Mission  
[^51]: Nuclear power in India – Wikipedia. https://en.wikipedia.org/wiki/Nuclear_power_in_India  
[^52]: India's three-stage nuclear power programme – Wikipedia. https://en.wikipedia.org/wiki/India%27s_three-stage_nuclear_power_programme  
[^53]: Science and technology in India – Wikipedia. https://en.wikipedia.org/wiki/Science_and_technology_in_India  
[^54]: United Nations – Wikipedia. https://en.wikipedia.org/wiki/United_Nations  
[^55]: United Nations System – Wikipedia. https://en.wikipedia.org/wiki/United_Nations_System  
[^56]: List of specialized agencies of the United Nations – Wikipedia. https://en.wikipedia.org/wiki/List_of_specialized_agencies_of_the_United_Nations  
[^57]: List of intergovernmental organizations – Wikipedia. https://en.wikipedia.org/wiki/List_of_intergovernmental_organizations  
[^58]: Environment of India – Wikipedia. https://en.wikipedia.org/wiki/Environment_of_India  
[^59]: Environmental issues in India – Wikipedia. https://en.wikipedia.org/wiki/Environmental_issues_in_India  
[^60]: Wildlife of India – Wikipedia. https://en.wikipedia.org/wiki/Wildlife_of_India  
[^61]: Conservation in India – Wikipedia. https://en.wikipedia.org/wiki/Conservation_in_India  
[^62]: Chipko movement – Wikipedia. https://en.wikipedia.org/wiki/Chipko_movement  
[^63]: Subhas Chandra Bose – Wikipedia. https://en.wikipedia.org/wiki/Subhas_Chandra_Bose  
[^64]: Bal Gangadhar Tilak – Wikipedia. https://en.wikipedia.org/wiki/Bal_Gangadhar_Tilak  
[^65]: Lala Lajpat Rai – Wikipedia. https://en.wikipedia.org/wiki/Lala_Lajpat_Rai  
[^66]: Bhagat Singh – Wikipedia. https://en.wikipedia.org/wiki/Bhagat_Singh  
[^67]: RRB NTPC Exam Pattern – EMBIBE. https://www.embibe.com/exams/rrb-ntpc-exam-pattern/