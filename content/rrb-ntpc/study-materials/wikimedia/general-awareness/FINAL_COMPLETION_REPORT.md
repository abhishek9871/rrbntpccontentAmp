# General Awareness Content Collection for RRB NTPC from Wikipedia/Wikibooks: Reproducible, Offline-first Blueprint

## Executive Summary and Objectives

This blueprint sets out a complete, reproducible plan to build an offline-first General Awareness study corpus for Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC). The corpus will cover the General Awareness (GA) scope specified in the official syllabus and widely circulated preparation guides, and will be compiled exclusively from Wikipedia and Wikibooks sources, with legal compliance and verifiability embedded into every step. The syllabus includes: Indian History (ancient, medieval, modern), Indian Geography (physical, states, mountains, rivers), Polity and Governance (Constitution, Parliament, judiciary), Economy (basic concepts and India-focused entries), Science and Technology (general developments, India’s space and nuclear programmes), Current Affairs (baseline structures and static elements), Static General Knowledge (GK) (important dates, organizations, personalities), as well as broader GA domains like culture, literature, monuments, environment, transport, government schemes, and abbreviations.[^2][^5][^6][^7]

The scope intentionally excludes live crawling. Instead, it prioritizes Wikimedia’s official data access mechanisms—dumps, static exports, and APIs—with a licensing-first approach grounded in the Creative Commons Attribution-ShareAlike (CC BY-SA) license for text and the GNU Free Documentation License (GFDL) for legacy coverage where applicable. Images and media are governed by their own licenses and require per-asset attribution. The blueprint specifies end-to-end workflows, metadata schemas, snapshot and revision documentation, integrity checks, and a storage layout designed for offline-first use in an educational setting. All methods, filenames, checksums, and processing steps will be captured to support future reproducibility.

Primary deliverable: A full, offline-accessible corpus of GA content, organized for RRB NTPC coverage, with per-article HTML bundles, image tarballs, metadata (including dump run identifiers and revision IDs), MD5/SHA checksums, and a CC BY-SA/GFDL-compliant attribution pack.

In addition to the corpus, the blueprint includes verification and audit procedures, long-term maintenance policies, and fallback methods for periods when primary data channels are throttled or unavailable. By aligning with the RRB NTPC GA structure and exam context, the content is designed to be directly useful to content engineers, RRB NTPC aspirants, and Wikimedia合规审查ers alike.[^1][^2][^3][^5][^6][^7]



## Alignment with RRB NTPC General Awareness Syllabus

The RRB NTPC GA section spans an integrated body of knowledge that overlaps across topics and often mixes static facts with domain-specific conceptual understanding. The official syllabus and credible portals converge on the following coverage: Current Events (national and international), Games and Sports, Art and Culture, Indian Literature, Monuments and Places, History and Freedom Struggle, Physical/Social/Economic Geography, Polity and Governance (including constitutional articles, union and state structures, Parliament, judiciary), Economy (banking, finance, markets), General Scientific and Technological Developments (with explicit India space and nuclear programmes), UN and other world organizations, Environmental Issues, Basics of Computers and Applications, Common Abbreviations, Transport Systems, Indian Economy, Famous Personalities (India and world), Flagship Government Programmes, and important government/public sector organizations.[^2][^5][^6][^7]

Because “General Science and Life Science (up to 10th CBSE)” is listed within General Awareness in official enumerations, this blueprint treats General Science as a GA subdomain rather than a standalone section. This prevents duplication and aligns with the exam structure where GA carries 40 questions in CBT 1 and 50 in CBT 2.[^2][^3][^4]

Two practical principles drive the mapping:

- Factual anchors first: For static GK (lists of monarchs, capitals, UNESCO sites) or institutions (UN system, Parliament, RBI), Wikipedia lists and overviews are more stable and complete than ad hoc web picks.  
- Conceptual scaffolding second: For economic concepts, scientific developments, or environmental debates, structured overviews and lead sections provide a stable baseline. Aspirants can layer recent developments via dated snapshots.

To anchor the crosswalk, Table 1 shows the topic taxonomy alignment. It is a living artifact: when multiple pages overlap, the set is pruned to the minimal set that still provides complete syllabus coverage.

Table 1. RRB NTPC General Awareness Topic Taxonomy (source: consolidated from the syllabus and portal mappings)[^2][^5][^6][^7]

| GA Subdomain               | Representative Subtopics                                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Current Affairs           | National/International events; sports; awards; days; government programmes; recent scientific achievements                   |
| Art, Culture & Literature | Indian art forms; dance; music; architecture; languages; Indian literature overview; notable works                          |
| Monuments & Places        | UNESCO World Heritage Sites in India; protected monuments; iconic landmarks                                                 |
| History                   | Ancient India (Indus Valley, Vedic, Mauryan, Gupta); Medieval (Delhi Sultanate, Vijayanagara, Mughals); Modern; Freedom Struggle |
| Geography                 | Physical (mountains, plateaus, coasts); Indian rivers; soils; climate; social and economic geography; states and capitals   |
| Polity & Governance       | Constitution basics; Preamble; Fundamental Rights/Duties; Directive Principles; Parliament; Supreme Court; Union/State; Local governance |
| Economy                   | Basic concepts (GDP, inflation, markets); banking; finance; taxation; planning; Indian economy structure                     |
| Science & Technology      | General science; Indian S&T ecosystem; space programme; nuclear programme; recent missions; common abbreviations            |
| Environment               | Environmental issues; biodiversity; flora and fauna; conservation; climate change (India-focused)                            |
| Organizations             | UN system; specialized agencies; world organizations; Indian government and public sector organizations                      |
| Transport                 | Transport systems in India (railways, roads, ports, aviation)                                                                |
| Personalities             | Famous Indians and global personalities across domains (public life, science, literature)                                   |
| Government Schemes        | Flagship programmes (past and present) with objectives and implementation                                                    |

This taxonomy serves as the selection list for article acquisition and as a checklist during verification.



### Scope Partition with Mathematics and Reasoning

Mathematics and General Intelligence & Reasoning are separate scored sections in CBT 1 and CBT 2 and sit outside GA. Although some reasoning topics (e.g., interpretation of graphs) may share conceptual ground with GA, this blueprint focuses solely on GA as defined above. General Science content (CBSE up to Class 10) is explicitly listed within GA and is treated as a subdomain to avoid duplication and to match the official syllabus presentation.[^2]



## Legal and Licensing Framework (CC BY-SA 3.0, GFDL, Image Assets)

Wikimedia dumps and APIs provide free and legal access to content, but compliance is not automatic. The project adopts a licensing-first posture.

Text licensing. All Wikipedia text is dual-licensed under CC BY-SA 3.0 and GFDL. This requires attribution and ShareAlike obligations. Attribution must credit the original Wikipedia page, list or recognize key contributors where feasible, and include the license name. ShareAlike requires that derivative text be distributed under the same license. GFDL obligations apply to legacy portions and must be preserved.[^14]

Images and media. Individual files on Wikimedia Commons and linked media may carry different licenses (e.g., Creative Commons variants, GNU GPL, or custom licenses). For each asset, the original license name and URL must be captured and displayed in the attribution layer. The corpus must never strip license metadata from images and must avoid embedding files whose license precludes redistribution in an offline educational corpus unless permitted.

Documentation in the corpus. Each HTML file and each media bundle must be accompanied by machine-readable metadata that records the exact source, revision ID, snapshot identifiers, author/contributor hints when available, license text, and attribution notices. These fields support audit and downstream redistribution under the correct terms.[^14][^13]

Table 2 summarizes license obligations by asset type.

Table 2. License obligations by asset type and required attribution fields[^14]

| Asset Type          | License Model (typical)                      | Required Attribution Fields (minimum)                                      |
|---------------------|----------------------------------------------|----------------------------------------------------------------------------|
| Wikipedia text      | CC BY-SA 3.0 (also GFDL for legacy coverage) | Source page title and URL; license name(s); attribution note; revision ID  |
| Page HTML           | Same as text; may include embedded scripts   | As above, plus snapshot identifier (run) and timestamp                     |
| Images/Media        | Per-file (varies)                            | Original file URL; license name; author/creator; license URL               |
| Page metadata       | CC0 where applicable (service-generated)     | Generator; schema version; timestamp; integrity checksums                  |

### Attribution Template Design

Attribution must appear both at the article level (in the HTML head or a prominent banner) and at the media level (as an embedded JSON or sidecar file). The template below captures the minimum required fields:

- Title: <Page Title>  
- Source: <Canonical Wikipedia/Wikibooks URL>  
- Contributors: Wikipedia/Wikibooks contributors (names where available)  
- License: CC BY-SA 3.0 (and GFDL where applicable)  
- Share-alike notice: This work must be distributed under the same license.  
- Revision ID: <lastrevid> (and older revisions when used)  
- Snapshot identifier: <dump-run/enterprise run>  
- Timestamp: <UTC timestamp when captured>  
- Image/media notice: Individual images may carry different licenses; see media.json for per-asset details.

This structure aligns with Wikimedia’s guidance on attribution and ensures downstream users can verify compliance and reproduce the content.[^14][^13]



## Source Acquisition Strategy: Dumps, Snapshots, and Revision IDs

Wikimedia offers several official access methods for bulk and per-article needs. This blueprint prioritizes official dumps and historical archives, using APIs for deltas and on-demand exports.

1) Database backup dumps (XML/SQL). These are the canonical bulk source for page text and metadata, typically generated at least monthly and often twice monthly. SQL dumps provide link tables and basic structure, while XML dumps provide current and historical revisions. File sizes are very large; integrity is validated via MD5 sums.[^1][^2][^3][^8]

2) Static HTML dumps and enterprise HTML archive. Static HTML dumps are not continuously maintained, but historical static HTML dumps and Wikimedia Enterprise HTML archives remain available for specific namespaces and wikis. Enterprise HTML ceased replication in March 2025, but historical archives persist and are accessible; ongoing snapshotting for deltas is available via Enterprise APIs.[^2][^3][^13]

3) On-demand per-article export. Special:Export and the MediaWiki export interface allow single-article retrieval in XML. These are ideal for targeted content and reproducible revision-level exports.[^14]

4) Mirroring and rate limits. Wikimedia servers apply rate limits; mirrors can be used to avoid throttling. Integrity must be checked with MD5/SHA checksums provided with dump directories. Meta’s mirroring guidance is the canonical reference for sustainable access.[^8]

Table 3 compares Wikimedia data access options.

Table 3. Wikimedia data access options and use-cases[^1][^2][^3][^8][^14]

| Access Method                     | Formats                | Frequency/Status                                   | Best Use-Cases                                      | Notes                                                        |
|----------------------------------|------------------------|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------|
| Database backup dumps            | XML, SQL               | At least monthly (often twice monthly)             | Full corpus baseline; historical revisions           | Very large; validate with MD5; do not crawl live             |
| Static HTML dumps                | HTML                   | Discontinued as ongoing; historical archives exist | Quick offline HTML ready-to-serve                   | Namespace-limited; legacy                                   |
| Enterprise HTML archive          | HTML (historical)      | Historical runs available; replication ended 2025-03-24 | Rich snapshots for specific wikis and namespaces   | For deltas, use Snapshot API; on-demand via Enterprise API   |
| Per-article export (Special:Export) | XML                    | On-demand                                          | Targeted topics; specific revision capture          | Includes page history metadata                               |
| Mirrors                          | Same as above          | Mirrored availability                              | Avoiding rate limits; faster regional access         | Use meta’s mirror list and mirroring best practices          |

### Snapshot and Revision Metadata Strategy

For reproducibility, every acquired artifact must carry:

- Wikipedia revision ID (lastrevid), revision timestamp, and page ID (pageid).[^10]
- Wikipedia page history details captured at export time.[^11]
- Dump run identifiers (e.g., enwiki dump date, directory path, enterprise run identifier).[^1][^3]
- Canonical source URL and language code.
- MD5 checksums for each file; where possible, add SHA checksums.

These fields allow an auditor to re-fetch or re-construct the exact snapshot, compare two revisions, and run deterministic validation pipelines.



## Content Identification and Topic-to-Page Mapping

Because GA spans many domains, a disciplined mapping keeps the corpus focused and non-redundant. We combine authoritative overviews with stable list pages and India-focused entries. Table 4 shows the initial seed set; it is expanded iteratively through a QA loop and de-duplicated to minimize overlap.

Table 4. Topic-to-Wikipedia Page mapping (seed set)

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
| Key Personalities                     | Mahatma Gandhi; Subhas Chandra Bose; Bal Gangadhar Tilak; Lala Lajpat Rai; Bhaghat Singh                                   |

The initial page set will expand to cover states and capitals, monuments lists, transport systems, and schemes during the production phase. Cross-checks against the GA taxonomy ensure complete coverage across all subdomains (see Appendix B for the topic checklist).



## Storage Layout and Filenames for Offline Use

The storage layout is designed for predictability, auditability, and offline navigation. Each topic cluster is a directory containing one HTML bundle per article, a media tarball (or folder), and a JSON metadata file. Integrity data (checksums) resides alongside.

Proposed directory layout:

- content/rrb-ntpc/study-materials/wikimedia/general-awareness/  
  - history/  
    - pages/  
      - <Page_Title>/  
        - index.html (or page.html)  
        - media/ (or media.tar.gz)  
        - metadata.json  
    - checksums/  
      - history.md5  
      - history.sha256  
  - geography/  
  - polity/  
  - economy/  
  - organizations/  
  - environment/  
  - science-technology/  
  - personalities/  
  - metadata/ (global manifest, attribution pack, schema versions)  
  - attribution/ (LICENSE files, attribution templates, image license register)

Filename rules:

- Directory per article: sanitized page title (spaces replaced with underscores), preserving the case of the lead heading.  
- HTML file: index.html for the main render; optional page.html for a direct name.  
- Metadata file: metadata.json with schema defined below.  
- Media: media.tar.gz for images and assets; alternative: media/ folder mirroring the source file tree.

Table 5 defines the metadata schema.

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

### Integrity and Validation Checks

The pipeline must verify integrity end-to-end and capture the evidence.

- Validate downloaded files against MD5 sums provided by the dump or enterprise archive. Where MD5 is unavailable, compute and store SHA-256 locally.[^1][^3]  
- After HTML generation (or per-article export), compute file-level checksums and record them in metadata.json.  
- Record dump run identifiers (e.g., enwiki/latest) and enterprise snapshot identifiers for each acquisition.  
- Preserve page history context (revisions, timestamps) in the metadata, enabling change audits and “date of knowledge” framing for exam content.[^11]



## Extraction and Packaging Methodology

The objective is to produce an offline-served HTML bundle per article, with media preserved and attribution retained.

1) From XML dumps to HTML. Use a consistent rendering pipeline to convert the latest revision (or a specified revision) from XML dumps into HTML. Media references should be preserved (not inlined) so that per-asset licensing remains visible. Static HTML bundles must retain the attribution banner and a pointer to the metadata.json file. This approach provides a stable, offline-first user experience while preserving license signals.[^1][^2][^14]

2) Enterprise HTML. Where historical HTML snapshots exist and suffice for scope, extract the run and attach metadata (run_id, timestamp). Validate integrity with checksums.[^3]

3) Per-article export fallback. For small sets or updates, use Special:Export to fetch specific revisions of articles. Recompute HTML if necessary and record the revision ID, timestamp, and export parameters.[^14]

4) Image tarballs and media integrity. Extract the list of images and linked media from the page’s metadata; download assets from Commons with origin URLs captured. Package them into media.tar.gz or preserve as media/. For each media file, retain the license name and URL in a media.json index within the article folder. This ensures compliance and transparency for educators and auditors.[^13]

5) Attribution packaging. Embed attribution in the HTML footer or sidebar, and include a copy of this information in metadata.json. Provide a top-level attribution directory with license texts (CC BY-SA 3.0 and GFDL), attribution template, and image license register.

Table 6 documents conversion steps with traceability fields.

Table 6. Conversion steps and artifacts traceability

| Input Source                       | Tooling/Process                   | Output Artifact                  | Snapshot Fields Captured                                     | Integrity Outputs                         |
|------------------------------------|-----------------------------------|----------------------------------|---------------------------------------------------------------|-------------------------------------------|
| Database backup XML (latest rev)   | XML → HTML render pipeline         | index.html (per article)         | dump_run_id; revision_id; revision_timestamp; page_id         | MD5/SHA checksums of HTML and tarballs    |
| Enterprise HTML snapshot           | Extract run → bundle               | index.html + metadata.json       | enterprise_run_id; snapshot_timestamp                         | Verify against run’s checksum manifest     |
| Special:Export (per-article XML)   | XML → HTML render pipeline         | index.html + metadata.json       | revision_id; export_timestamp; source_url                     | MD5/SHA checksums                          |
| Media list (from page metadata)    | Batch fetch from Commons           | media.tar.gz or media/           | per-asset source URL; license name; license URL                | media.json index; per-asset checksums      |

### HTML Bundle Structure and Linking

- Use index.html or page.html as the entry point.  
- Preserve all local asset references (CSS, JS, images) as relative links. If assets are tarred, ensure the tarball structure maintains relative paths.  
- Embed an attribution footer with source, license, revision ID, and snapshot identifier.  
- Include a small JSON-LD or embedded JSON block with metadata to support programmatic validation and auditing.

This structure mirrors common static dump practices and aids offline navigation.[^2]



## Content Coverage by Domain (RRB NTPC GA)

This section highlights how domain-specific content will be selected and packaged, with representative Wikipedia anchors for each domain.

### Indian History

Objective: Provide complete syllabus coverage of ancient, medieval, and modern Indian history, including the freedom struggle.

Approach: Use the main history pages and timelines as anchors; use lists and overviews to minimize duplication while preserving detail where required.

- Ancient India: Outline of ancient India, Middle kingdoms of India, List of historical regions of India.[^24][^25][^27]  
- Medieval India: Medieval India; History of South India for regional specificity.[^23][^26]  
- Modern and freedom struggle: History of India; Indian independence movement; List of Indian independence activists for quick reference and cross-checking.[^19][^21][^22]

### Indian Geography

Objective: Cover physical, social, and economic geography with an India focus; include mountains, rivers, and physiographic regions.

Approach: Use the Geography of India page for the national overview; integrate major physiographic entries and river lists to anchor static facts.

- Geography of India (overview).[^29]  
- Physical features and mountains: Himalayas; Western Ghats; Eastern Ghats; Indo-Gangetic Plain.[^31][^34][^33][^32]  
- Rivers: List of major rivers of India.[^30]  
- Indian Himalayan Region as a thematic anchor for mountain systems and rivers.[^35]

### Indian Polity and Governance

Objective: Provide constitutional basics, institutional structures, and landmark cases for governance topics.

Approach: Anchor to core institutional pages and constitutional doctrine; use case pages to expose reasoning and context.

- Constitution of India; Government of India; Parliament of India; Supreme Court of India.[^36][^37][^38][^39]  
- Basic structure doctrine and Kesavananda Bharati case for constitutional contours.[^43][^42]  
- Additional context: Judicial review in India.[^41]

### Economy (India-focused and Basics)

Objective: Cover basic economic concepts and India’s financial system and institutions.

Approach: Use high-level economy pages and institution pages; add payments and banking system entries.

- Economy of India (overview and structure).[^45]  
- Institutions: Reserve Bank of India; Banking in India; Finance in India; Payment and settlement systems in India.[^47][^48][^49][^46]

### Science and Technology

Objective: Provide general scientific developments and Indian S&T context; emphasize space and nuclear programmes.

Approach: Use Indian space and nuclear programme pages with institutional anchors.

- ISRO; Department of Space; Chandrayaan programme; Mars Orbiter Mission.[^50][^51][^52][^53]  
- Nuclear power in India and India’s three-stage nuclear programme.[^54][^55]  
- Science and technology in India (overview).[^56]

### International Organizations and Relations

Objective: Provide institutional context for UN and other global organizations often tested in GA.

Approach: Use UN system pages and specialized agencies lists; intergovernmental organizations list for breadth.

- United Nations; United Nations System; List of specialized agencies of the United Nations; List of intergovernmental organizations.[^57][^58][^59][^60]

### Environment

Objective: Cover environmental issues, flora and fauna, and conservation movements.

Approach: Use India-focused environment pages and conservation entries.

- Environment of India; Environmental issues in India; Wildlife of India; Conservation in India; Chipko movement (as a case study).[^61][^62][^63][^64][^65]

### Personalities

Objective: Provide baseline biographical content for key figures that frequently appear in GA sections.

Approach: Use concise biography pages and cross-reference with history and independence movement pages.

- Mahatma Gandhi; Subhas Chandra Bose; Bal Gangadhar Tilak; Lala Lajpat Rai; Bhagat Singh.[^66][^67][^68][^69][^70]



## Quality Assurance and Reproducibility Audit

Quality is enforced through metadata validation, file integrity checks, and licensing verification. The QA process is designed to be runnable as a batch audit before every release.

- Metadata validation. Confirm presence of title, source_url, page_id, revision_id, revision_timestamp, language, dump_run_id or enterprise_run_id, license_text, attribution_text, and both checksums.  
- Integrity checks. Verify file MD5 against the provided manifest; compute and store SHA-256 locally for long-term validation; ensure that image tarballs and media indices match page-level asset lists.[^1][^3]  
- Licensing verification. Spot-check that per-page attribution banners reflect CC BY-SA/GFDL; for a sample of images per domain, verify that the media.json includes license name and URL, and that any GPL or non-redistributable licenses are flagged.  
- Revision audit. Compare captured revision IDs and timestamps against the page history to confirm alignment with snapshot claims. Record discrepancies and retake snapshots if necessary.[^11]  
- Cross-reference coverage. Confirm that every GA subdomain (Table 1) has at least one article present and that the topic checklist in Appendix B is satisfied.

Table 7 lists the QA checklist.

Table 7. QA checklist

| Checkpoint                   | Description                                                                                 | Pass/Fail Notes |
|-----------------------------|---------------------------------------------------------------------------------------------|-----------------|
| Metadata completeness       | All required fields present and parseable                                                   |                 |
| Integrity (MD5/SHA)         | File checksums match; logs stored alongside artifacts                                       |                 |
| Snapshot fields             | Dump run ID or enterprise run ID; revision_id; timestamp present                            |                 |
| Attribution banners         | HTML includes attribution footer and license summary                                        |                 |
| Image licenses              | Per-file license name/URL in media.json; no unlicensed redistribution                       |                 |
| Coverage completeness       | All GA subdomains represented (Appendix B checklist)                                        |                 |
| History audit               | Revision IDs and timestamps validated against page history                                  |                 |



## Maintenance and Update Policy

RRB NTPC aspirants need dependable baselines, not perpetual churn. Maintenance balances stability with currency.

- Cadence. Quarterly snapshots aligned to Wikimedia database dump cycles. Additional snapshots only for major India-related developments (e.g., major space missions, constitutional amendments), with explicit “as-of” dating.[^1]  
- Change management. For each update, record revision deltas and maintain a dated manifest. Maintain a changelog noting new, updated, or retired articles.  
- Deprecation policy. Archive prior snapshots and mark them “superseded” with pointers to the newer manifest. Never silently overwrite prior releases.  
- Legal watch. Monitor licensing metadata changes for images and adjust attribution files accordingly.  
- Access continuity. Use mirrors when rate-limited; avoid peak hours; coordinate downloads according to Meta’s mirroring best practices.[^8]

Table 8 outlines the update log schema.

Table 8. Update log schema

| Field          | Description                                                |
|----------------|------------------------------------------------------------|
| snapshot_date  | ISO date of the snapshot                                   |
| dump_run_id    | Dump directory/run identifier                              |
| changes        | Summary of updates (new/updated/retired pages)             |
| checksums      | MD5/SHA manifest filename                                  |
| notes          | Rationale for out-of-cycle updates                         |



## Risks and Mitigations

- Rate limiting or temporary blocks. Mitigate via Wikimedia mirrors, staggered scheduling, and compliance with access guidelines.[^1][^8]  
- Large file sizes and transfer failures. Use resumable transfers; verify integrity with MD5/SHA; consider partial mirroring by namespace where sufficient.[^1]  
- Licensing misinterpretation. Maintain a licensing-first checklist; centralize attribution and per-media license registers; train staff on CC BY-SA/GFDL obligations.[^14]  
- Coverage gaps. Maintain a live topic checklist (Appendix B) and run periodic coverage audits against the RRB NTPC syllabus maps.[^2][^7]



## Delivery Artifacts and Directory Structure

The corpus will be delivered as a complete, offline-usable study material set. The final structure is self-describing and includes schema versions for long-term maintainability.

- Per-article HTML bundles with embedded attribution and metadata pointers.  
- Media tarballs or media folders with a JSON index of per-asset licenses.  
- Global manifests and schemas in metadata/, alongside the attribution pack.  
- Integrity data (checksums) stored per-domain and per-release.

Table 9 shows the final directory structure.

Table 9. Final directory structure and file inventory schema

| Path (relative)                                                    | Purpose                                                    |
|--------------------------------------------------------------------|------------------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/general-awareness/      | Root of GA corpus                                          |
| ├── pages/                                                         | HTML bundles and media per article                         |
| │   └── <Domain>/pages/<Page_Title>/{index.html, metadata.json, media.tar.gz} |
| ├── metadata/                                                      | Global manifests, schema versions, and per-snapshot logs   |
| ├── attribution/                                                   | License texts, attribution templates, image license register |
| └── checksums/                                                     | MD5/SHA checksum manifests per domain and per release      |



## Appendices

### Appendix A: Master Reference Index with Usage Notes

See References for the full list. The following notes explain the primary role of each source:

- RRB official context and updates.[^1]  
- Official/aligned syllabus lists and framing.[^2][^3][^4][^5][^6][^7]  
- Wikimedia data access mechanisms and mirrors.[^1][^8][^13][^14][^17]  
- Domain content anchors (India-focused articles across history, geography, polity, economy, S&T, environment, organizations).[^19]–[^70]



### Appendix B: Topic Coverage Checklist

Use this checklist to validate completeness before each release.

- Current Affairs  
  - National events; international events; sports and awards; important days  
- Art & Culture  
  - Indian art forms; dance; music; architecture; languages; major cultural sites  
- Literature  
  - Major Indian texts and authors (overview)  
- Monuments & Places  
  - UNESCO World Heritage Sites in India; national heritage list anchors  
- History  
  - Ancient (Indus Valley, Vedic, Mauryan, Gupta); Medieval (Delhi Sultanate, Vijayanagara, Mughals); Modern; Freedom Struggle  
- Geography  
  - Physical geography (mountains, ghats, Indo-Gangetic Plain); Indian rivers; climate; soils; social/economic geography; states & capitals  
- Polity  
  - Constitution basics; Preamble; Fundamental Rights; Directive Principles; Fundamental Duties; Parliament; Supreme Court; Union & State Executive; Local governance; emergency provisions  
- Economy  
  - Basic concepts (GDP, inflation, markets); banking; finance; taxation; planning; Indian economy structure  
- Science & Technology  
  - General science; Indian S&T ecosystem; space programme (missions); nuclear programme; common abbreviations  
- Environment  
  - Environmental issues; biodiversity; flora and fauna; conservation movements (e.g., Chipko)  
- Organizations  
  - UN system; specialized agencies; intergovernmental organizations; Indian government/public sector organizations  
- Transport  
  - Railways; roads; ports; aviation (India focus)  
- Personalities  
  - Freedom fighters and national leaders; global personalities relevant to GA  
- Government Schemes  
  - Flagship programmes; objectives; implementation  
- Static GK  
  - Important dates; awards; organizations and their headquarters; abbreviations



### Appendix C: Example Attribution and License Text Blocks

Text attribution (place in HTML footer and metadata.json):

- Title: <Page Title>  
- Source: <Wikipedia/Wikibooks URL>  
- Contributors: Wikipedia/Wikibooks contributors  
- License: CC BY-SA 3.0 (also GFDL for legacy coverage)  
- Share-alike: This work must be distributed under the same license.  
- Revision ID: <lastrevid>  
- Snapshot: <dump_run_id or enterprise_run_id>  
- Timestamp: <UTC timestamp>

Image/media attribution (per media.json):

- Filename; Original Source URL; License Name; License URL; Author/Creator (where available).

License texts (include in attribution/):

- CC BY-SA 3.0 license summary and deed link.  
- GFDL license summary and text reference (for legacy coverage).



## Information Gaps and Assumptions

- The exact mapping of every GA micro-topic (e.g., “Neighboring Countries” or “Countries, Capitals and Currencies”) to specific Wikipedia pages will be completed during the production phase. The seed mapping above ensures coverage of the main areas; a systematic pass will finalize lists and prune duplicates.  
- Some source URLs in the master references are portal summaries. Where official PDFs are not explicitly accessible, the blueprint anchors to the official RRB page for updates and treats portals as corroborative rather than authoritative.  
- Licensing nuances for images may require per-asset checks. The blueprint’s media.json approach is designed to capture and manage this variability.



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
[^28]: Geography of India – Wikipedia. https://en.wikipedia.org/wiki/Geography_of_India  
[^29]: List of major rivers of India – Wikipedia. https://en.wikipedia.org/wiki/List_of_major_rivers_of_India  
[^30]: Himalayas – Wikipedia. https://en.wikipedia.org/wiki/Himalayas  
[^31]: Western Ghats – Wikipedia. https://en.wikipedia.org/wiki/Western_Ghats  
[^32]: Eastern Ghats – Wikipedia. https://en.wikipedia.org/wiki/Eastern_Ghats  
[^33]: Indo-Gangetic Plain – Wikipedia. https://en.wikipedia.org/wiki/Indo-Gangetic_Plain  
[^34]: Indian Himalayan Region – Wikipedia. https://en.wikipedia.org/wiki/Indian_Himalayan_Region  
[^35]: Constitution of India – Wikipedia. https://en.wikipedia.org/wiki/Constitution_of_India  
[^36]: Government of India – Wikipedia. https://en.wikipedia.org/wiki/Government_of_India  
[^37]: Parliament of India – Wikipedia. https://en.wikipedia.org/wiki/Parliament_of_India  
[^38]: Supreme Court of India – Wikipedia. https://en.wikipedia.org/wiki/Supreme_Court_of_India  
[^39]: Kesavananda Bharati v. State of Kerala – Wikipedia. https://en.wikipedia.org/wiki/Kesavananda_Bharati_v._State_of_Kerala  
[^40]: Judicial review in India – Wikipedia. https://en.wikipedia.org/wiki/Judicial_review_in_India  
[^41]: Economy of India – Wikipedia. https://en.wikipedia.org/wiki/Economy_of_India  
[^42]: Reserve Bank of India – Wikipedia. https://en.wikipedia.org/wiki/Reserve_Bank_of_India  
[^43]: Banking in India – Wikipedia. https://en.wikipedia.org/wiki/Banking_in_India  
[^44]: Finance in India – Wikipedia. https://en.wikipedia.org/wiki/Finance_in_India  
[^45]: Payment and settlement systems in India – Wikipedia. https://en.wikipedia.org/wiki/Payment_and_settlement_systems_in_India  
[^46]: ISRO – Wikipedia. https://en.wikipedia.org/wiki/ISRO  
[^47]: Department of Space – Wikipedia. https://en.wikipedia.org/wiki/Department_of_Space  
[^48]: Chandrayaan programme – Wikipedia. https://en.wikipedia.org/wiki/Chandrayaan_programme  
[^49]: Mars Orbiter Mission – Wikipedia. https://en.wikipedia.org/wiki/Mars_Orbiter_Mission  
[^50]: Nuclear power in India – Wikipedia. https://en.wikipedia.org/wiki/Nuclear_power_in_India  
[^51]: India's three-stage nuclear power programme – Wikipedia. https://en.wikipedia.org/wiki/India%27s_three-stage_nuclear_power_programme  
[^52]: Science and technology in India – Wikipedia. https://en.wikipedia.org/wiki/Science_and_technology_in_India  
[^53]: United Nations – Wikipedia. https://en.wikipedia.org/wiki/United_Nations  
[^54]: United Nations System – Wikipedia. https://en.wikipedia.org/wiki/United_Nations_System  
[^55]: List of specialized agencies of the United Nations – Wikipedia. https://en.wikipedia.org/wiki/List_of_specialized_agencies_of_the_United_Nations  
[^56]: List of intergovernmental organizations – Wikipedia. https://en.wikipedia.org/wiki/List_of_intergovernmental_organizations  
[^57]: Environment of India – Wikipedia. https://en.wikipedia.org/wiki/Environment_of_India  
[^58]: Environmental issues in India – Wikipedia. https://en.wikipedia.org/wiki/Environmental_issues_in_India  
[^59]: Wildlife of India – Wikipedia. https://en.wikipedia.org/wiki/Wildlife_of_India  
[^60]: Conservation in India – Wikipedia. https://en.wikipedia.org/wiki/Conservation_in_India  
[^61]: Chipko movement – Wikipedia. https://en.wikipedia.org/wiki/Chipko_movement  
[^62]: Mahatma Gandhi – Wikipedia. https://en.wikipedia.org/wiki/Mahatma_Gandhi  
[^63]: Subhas Chandra Bose – Wikipedia. https://en.wikipedia.org/wiki/Subhas_Chandra_Bose  
[^64]: Bal Gangadhar Tilak – Wikipedia. https://en.wikipedia.org/wiki/Bal_Gangadhar_Tilak  
[^65]: Lala Lajpat Rai – Wikipedia. https://en.wikipedia.org/wiki/Lala_Lajpat_Rai  
[^66]: Bhagat Singh – Wikipedia. https://en.wikipedia.org/wiki/Bhagat_Singh  
[^67]: RRB NTPC Exam Pattern – EMBIBE. https://www.embibe.com/exams/rrb-ntpc-exam-pattern/