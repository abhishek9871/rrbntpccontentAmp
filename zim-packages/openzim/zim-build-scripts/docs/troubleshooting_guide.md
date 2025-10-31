# ZIM Package Generation: Build Scripts, Process, Metadata, Compression, and Troubleshooting

## Executive Summary

Objective. This blueprint defines a repeatable, automated path to generate ZIM packages from the Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) content available in the workspace. The immediate goal is to produce two to three content bundles—each with properly curated metadata, robust compression settings, verification, and troubleshooting—so they can be validated and distributed via standard ZIM readers. Where native ZIM tooling is not present, the approach relies on official container images to ensure reliable builds and consistent developer experience across platforms.[^1][^3][^5]

Scope. The work covers: build-script design and automation; content selection and curation; metadata inclusion and licensing; compression settings; build verification and integrity checks; logging and error handling; troubleshooting common failures; and archival of the final artifacts under the packages/openzim directory.

Outcome. A reproducible build-and-release workflow is established, including container-based invocations when native tooling is unavailable. Two to three candidate bundles are identified from existing workspace content. Each bundle is characterized by purpose, core directories, metadata fields, and compression settings, accompanied by verification steps and troubleshooting guidance. This yields a pragmatic path to producing real ZIM artifacts or, where necessary, documented procedures and scripts that can be executed via official container images to complete the builds.[^1][^3][^5]

## Tooling Availability and Build Environment

The ability to generate ZIM packages depends on zim-tools (notably zimwriterfs, zimcheck, zimdump, zimsplit). Two build paths exist:

- Native installation. Install zim-tools from system packages or build from source using Meson. This path is appropriate for Linux distributions with available packages or for developers who need full control over the build environment.[^1][^6][^7]
- Containerized path. Use the official image to run zimwriterfs and related tools without local compilation or dependency management. This approach is the most consistent across platforms and avoids environment-specific pitfalls.[^1][^3]

Prerequisites. The following tools are typical for a native build and also inform the container path:
- Build system: Meson and Ninja
- Core libraries: libzim, libmagic, zlib, Gumbo parser, ICU
- Optional test dependency: Google Test (for building and running tests)
These dependencies and the overall build/test/install flow are documented by the project and packaging systems.[^1][^6][^7]

To support reliable builds in environments without native tooling, the official container image is recommended as the default execution environment.[^1][^3]

Table 1. ZIM tools: purpose and usage notes

| Tool         | Purpose                                          | Typical usage in this project                                |
|--------------|--------------------------------------------------|---------------------------------------------------------------|
| zimwriterfs  | Create ZIM files from a self-sufficient directory| Generate ZIM archives from curated HTML and media bundles     |
| zimcheck     | Verify ZIM integrity                             | Post-build validation and quality gating                      |
| zimdump      | Inspect/dump ZIM contents                        | Diagnostic inspection and content sampling                    |
| zimsplit     | Split ZIM archives                               | Optional partitioning for large packages                      |

Table 2. Build dependencies matrix

| Component            | Purpose                                | Source install guidance                        | Native package guidance                       |
|---------------------|----------------------------------------|-----------------------------------------------|-----------------------------------------------|
| Meson               | Build system generator                  | Python pip/virtualenv (project docs)[^1]      | Available in distros; see ports/FreeBSD[^6]   |
| Ninja               | Build executor                          | Git bootstrap or distribution package[^1]     | Available; e.g., FreeBSD ports[^6]            |
| libzim              | ZIM format library                      | Build from source (zim-tools)[^1]             | FreeBSD ports: archivers/zim-tools[^6]        |
| libmagic            | File type detection                     | DarwinSys distribution[^8]                    | FreeBSD ports; libmagic-dev on Debian[^1]     |
| zlib                | Compression                             | zlib.net[^9]                                  | Standard on most systems                      |
| Gumbo parser        | HTML parsing                            | Google Gumbo parser[^10]                      | libgumbo-dev                                  |
| ICU                 | Unicode handling                        | ICU Project[^11]                              | libicu-dev                                    |
| Google Test         | Unit testing                            | googletest[^14]                               | googletest package (Ubuntu example)[^1]       |

### Native Installation Path

When compiling from source, the common flow is:
- Configure: meson . build
- Build: ninja -C build
- Test: meson test (optional, requires Google Test)
- Install: ninja -C build install (may require elevated privileges)
- Post-install: ldconfig (as needed) to update runtime bindings
These steps and the Meson options—such as static linkage—are documented in the project repository.[^1]

### Containerized Execution Path

If zim-tools are not installed locally, execute builds inside the official container image. Mount the workspace and output directories into the container and invoke zimwriterfs. Afterward, use zimcheck to verify the resulting ZIM files. This guarantees tool availability and version consistency across developer machines and CI agents.[^1][^3]

## Content Bundles and Curation Plan

The workspace contains substantial RRB NTPC content with multiple categories. The proposed bundling strategy prioritizes content completeness, navigability, and licensing clarity to produce two to three distinct ZIM packages. The general-awareness (Wikimedia-sourced) and science directories provide strong coverage and metadata, including attribution and licensing notes. Current affairs and practice materials further expand the educational value for RRB NTPC candidates.

Candidate bundles:
- RRB NTPC General Awareness (Wikimedia-derived collection)
- RRB NTPC Science Compendium
- RRB NTPC Current Affairs and Practice Sets (with licensing review)

Bundling criteria include clear subject boundaries, completeness of assets (HTML and media), and consistent licensing. Each item should carry source attribution and license information, ideally in a machine-readable form adjacent to content. Where legacy licenses (e.g., GFDL) appear, redistribute only as permitted and document attribution accordingly.[^2]

Table 3. Bundle-to-directory mapping and inclusion rationale

| Bundle Name                                 | Source directories (from workspace)                                               | Rationale for inclusion                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| General Awareness (Wikimedia)               | RRB NTPC study-materials/wikimedia/*                                             | Broad coverage of culture, economy, environment, geography, history, polity, and more; strong per-page metadata with checksums and attribution. |
| Science Compendium                          | RRB NTPC study-materials/wikimedia/science/*                                     | Science topics (biology, chemistry, physics) aligned to general science requirements.    |
| Current Affairs & Practice Sets (provisional)| RRB NTPC current-affairs/*; RRB NTPC practice-sets/*; RRB NTPC previous-papers/* | Timely preparation materials and past papers; inclusion subject to licensing permissions.|

### General Awareness (Wikimedia-based)

This bundle collects per-topic directories (culture, economy, environment, geography, Indian history, international relations, polity, science and technology, organizations, and more). Per-page metadata typically includes:
- Title, source URL, language, snapshot identifiers
- License summary (e.g., Creative Commons Attribution-ShareAlike 3.0, with legacy GNU Free Documentation License notes where applicable)
- Attribution text and capture timestamps
- Integrity checksums and collection method notes
These fields support accurate attribution, provenance, and licensing compliance within the ZIM package.[^2]

### Science Compendium

The science directory includes biology, chemistry, physics, environmental and general science content. Each page is paired with metadata carrying title, source references, language, and license summaries. For uniformity, ensure media license details are enumerated per item and that per-file attribution and checksums are recorded alongside content.[^2]

### Current Affairs and Practice Sets

This bundle is high-value for exam preparation but requires careful licensing review. Source catalogs, redistribution policies, and any attribution requirements must be captured at the file level before packaging. Per-item metadata should include license type, source, creator/publisher, and any usage restrictions.

## ZIM Creation Process and Workflow

The end-to-end pipeline proceeds as follows:
1. Validate source directories and completeness.
2. Establish a stable HTML entry point (welcome page).
3. Curate a 48x48 PNG favicon.
4. Compile per-file metadata (title, description, language, creator, publisher, tags).
5. Optionally prepare redirects and full-text indexing.
6. Run zimwriterfs to generate the ZIM with tuned compression.
7. Verify integrity with zimcheck; inspect contents via zimdump as needed.
8. Archive artifacts and logs under the designated packages/openzim directory.

All steps should run under a unified, containerized environment when native tooling is unavailable, using the official image for reproducibility.[^1][^3][^4]

Table 4. zimwriterfs command options and their role

| Option                       | Purpose                                         | When to use                                                                 |
|-----------------------------|-------------------------------------------------|------------------------------------------------------------------------------|
| --welcome=index.html        | Sets the main entry page                        | Always; ensure the entry page exists and is relative to the content root     |
| --favicon=m/favicon.png     | Adds a 48x48 PNG favicon                        | Always; prepare an appropriate favicon and place it within the content tree  |
| --language=...              | ISO639-3 language code                          | Always; reflect primary content language                                     |
| --title=...                 | Package title                                   | Always; concise and descriptive                                              |
| --description=...           | Short description                               | Always; convey scope and audience                                            |
| --creator=...               | Content creator(s)                              | Always; derive from per-file metadata                                        |
| --publisher=...             | Package publisher                               | Always; e.g., project or organization name                                   |
| --withFullTextIndex         | Build a full-text index                         | Recommended for searchability in readers                                     |
| --redirects=file.tsv        | Define redirects (url, title, target_url)        | Optional; if you have canonicalization or aliasing needs                     |
| --uniqueNamespace           | Force namespace 'A' for all content             | Advanced; only if needed for dynamic/JavaScript-heavy content                |
| --minChunkSize=N            | Cluster size in bytes                           | Tune for performance vs. compression (defaults apply)[^4]                    |
| --inflateHtml               | Attempt HTML inflation pre-pack                 | Optional; can improve compression characteristics                            |
| --tags=...; --name=...      | Additional metadata                             | Optional; tags aid discovery; name provides a stable identifier              |

Table 5. Example metadata fields per bundle

| Field         | General Awareness (Wikimedia)                                         | Science Compendium                                        | Current Affairs & Practice Sets                                |
|---------------|------------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|
| Title         | RRB NTPC — General Awareness                                           | RRB NTPC — Science Compendium                             | RRB NTPC — Current Affairs & Practice Sets                     |
| Language      | en (or as per content)                                                 | en                                                        | en (or per source)                                             |
| Creator       | Wikipedia contributors (per page)                                      | Wikipedia contributors (per page)                         | Original publishers/authors as applicable                      |
| Publisher     | Project-defined                                                        | Project-defined                                           | Project-defined                                                |
| Description   | Curated articles on Indian culture, economy, geography, polity, etc.  | Biology, chemistry, physics, environmental topics         | Recent current affairs, practice sets, and past papers         |
| Tags          | education; rrb-ntpc; general-awareness; wikimedia                      | education; rrb-ntpc; science; wikimedia                   | education; rrb-ntpc; current-affairs; practice                |
| Favicon       | 48x48 PNG                                                              | 48x48 PNG                                                 | 48x48 PNG                                                      |
| Welcome page  | index.html (navigation hub)                                            | index.html (topic hub)                                    | index.html (topic hub)                                         |
| Licensing     | CC BY-SA 3.0; legacy GFDL for some items (per-file)                    | CC BY-SA 3.0 (per-file confirmations)                     | To be confirmed per source; document attribution requirements  |

### Compression and Indexing Strategy

Compression and indexing materially affect both package size and reader performance. The default cluster size is documented in the zimwriterfs man page; tuning it should be done in conjunction with full-text indexing to ensure search remains responsive.[^4][^1]

- Full-text indexing. Enable --withFullTextIndex to provide search capabilities within ZIM readers.
- Cluster size. Start with the default minChunkSize. If the package is large and primarily accessed sequentially, slightly larger clusters may improve compression; if random access performance is critical, consider the default or smaller clusters. Validate changes empirically using zimcheck and reader-side tests.[^4][^1]
- HTML inflation. --inflateHtml can improve compression characteristics for HTML payloads. Evaluate its impact on a representative subset before adopting broadly.[^4]

Table 6. Compression options vs. trade-offs

| Option             | Effect                                   | Trade-off considerations                                      | When to adjust                           |
|--------------------|-------------------------------------------|----------------------------------------------------------------|-------------------------------------------|
| --minChunkSize     | Controls compression block size           | Larger can compress better; smaller may improve random access  | After empirical testing on sample builds  |
| --inflateHtml      | Inflates HTML pre-compression             | Slight CPU overhead during build; possible compression gains   | For HTML-heavy bundles                     |
| Full-text index    | Enables in-ZIM search                     | Increases package size; improves usability                     | Always enabled for educational content     |

## File Organization and Metadata Inclusion

Adopt a consistent directory structure to keep builds predictable and audits straightforward. A recommended layout:

- content/
  - A/ (articles)
  - I/ (images)
  - J/ (JavaScript)
  - C/ (CSS)
  - M/ (other media)
- metadata/
  - bundle-level manifest (title, description, language, creator, publisher, tags)
  - per-file manifest (source URL, license, attribution, checksums)
- favicon.png (48x48)
- index.html (welcome page)

Leverage per-topic metadata already present in the workspace (e.g., title, source URL, revision details, language, license summary, attribution text, checksums, and capture timestamps). Consolidate these into bundle-level metadata and ensure per-file license and attribution records are carried into the package.[^2][^4]

Table 7. Bundle metadata mapping template

| Field        | Value source/policy                               | Notes                                                     |
|--------------|----------------------------------------------------|-----------------------------------------------------------|
| Title        | Human-authored per bundle                          | Descriptive, concise                                      |
| Language     | ISO639-3 code derived from content                 | e.g., eng for English                                     |
| Creator      | From per-file attributions                         | Aggregate unique creators                                 |
| Publisher    | Project-defined                                    | Consistent across packages                                |
| Description  | Human-authored scope summary                       | Include subject coverage and audience                     |
| Tags         | Controlled vocabulary (education, rrb-ntpc, etc.)  | Aids discovery                                            |
| Favicon      | 48x48 PNG prepared by the team                     | Place relative to content root                            |
| Welcome page | index.html authored by the team                    | Provide navigation hub                                    |
| Licensing    | From per-file metadata and license registry        | Record CC BY-SA 3.0 and any legacy GFDL notes             |

## Compression Procedures and Tuning

Compression should be tuned only after representative builds and verification. Because compression affects both file size and user-perceived performance, adjust parameters deliberately and document rationale in the build log.

- minChunkSize. Begin with the documented default; evaluate alternative values only with side-by-side tests and zimcheck validation.[^4]
- --inflateHtml. Test on HTML-heavy bundles where compression gains are likely to outweigh build-time costs.[^4]
- Record all settings in the build manifest for reproducibility.

Table 8. Compression parameter matrix

| Parameter      | Baseline         | Variant A             | Variant B              | Expected impact                                  |
|----------------|------------------|-----------------------|------------------------|--------------------------------------------------|
| minChunkSize   | Default (per man page) | Slightly larger           | Slightly smaller         | Compression ratio vs. random access performance   |
| --inflateHtml  | Off              | On                    | On                     | Potentially better HTML compression               |
| Full-text index| On               | On                    | On                     | Enabled for all bundles                           |

## Build Automation and Directory Layout

Automate builds to eliminate environment drift and simplify repeatability. The recommended approach is to:
- Normalize all build steps to run within the official container image when native tools are unavailable.[^3]
- Parameterize bundle selection and zimwriterfs options.
- Capture stdout/stderr logs per run and record checksums of the resulting ZIM files.
- Archive artifacts and logs under packages/openzim for clean separation from other workstreams.

Table 9. Automation task matrix

| Step                               | Tool/Command         | Input                                    | Output                                  | Failure handling                                 |
|------------------------------------|----------------------|------------------------------------------|------------------------------------------|--------------------------------------------------|
| Validate content completeness      | Custom script        | Source directories                        | Validation report                        | Fail early; list missing files                   |
| Prepare favicon and welcome page   | Static assets        | 48x48 PNG; index.html                     | Content root with entry assets           | Halt build if missing                            |
| Compile bundle metadata            | Custom script        | Per-file metadata                         | Bundle manifest                          | Warn on missing fields; require critical ones    |
| Build ZIM                          | zimwriterfs          | Content root, manifest, options           | ZIM file                                 | Retry with --skip-libmagic-check if applicable[^1] |
| Verify ZIM                         | zimcheck             | ZIM file                                  | Validation report                        | Fail the pipeline on corruption                  |
| Inspect contents (diagnostic)      | zimdump              | ZIM file                                  | Dumps or listings                        | Use only for troubleshooting                     |
| Archive artifacts and logs         | Custom script        | ZIM, logs, manifests                      | packages/openzim tree                    | Ensure permissions and checksums are recorded    |

### Logs and Error Handling

Standardize log capture for every build step:
- Route stdout and stderr to time-stamped log files.
- On validation failure, produce a diagnostics bundle: include zimcheck output, a sample listing via zimdump, and the build log.
- Ensure all runtime metadata is persisted (command-line flags, tool versions, and timestamps). This supports reproducibility and auditability.

## Verification, QA, and Acceptance Criteria

Quality gates ensure ZIM files are coherent, complete, and readable.

- Integrity check. Run zimcheck on each ZIM to confirm internal consistency.[^1]
- Content completeness. Validate that the welcome page resolves and key sections are present. Spot-check a representative sample of entries for media availability and correct relative paths.
- Indexing and search. If full-text indexing is enabled, verify that search returns expected results for queries across the bundle’s topics.
- Licensing compliance. Ensure per-file license summaries and attribution text are recorded within metadata and any displayed pages.

Table 10. QA checklist

| Criterion                     | Check method                     | Pass/Fail | Notes                                      |
|------------------------------|----------------------------------|-----------|--------------------------------------------|
| ZIM integrity                | zimcheck exit status             |           |                                            |
| Welcome page resolves        | Inspect via zimdump              |           | Ensure index.html is set as --welcome       |
| Media availability           | Spot-check URLs in sample pages  |           | Confirm relative paths and media presence   |
| Search functionality         | Query sample terms               |           | Only if --withFullTextIndex is enabled      |
| Licensing completeness       | Per-file metadata verification   |           | Record CC BY-SA 3.0 and any legacy notes    |
| Attribution correctness      | Compare per-page attribution     |           | Wikimedia attribution captured appropriately|
| Compression settings recorded| Build manifest review            |           | minChunkSize, inflation, index settings     |

## Troubleshooting Guide (Common Issues and Remedies)

The most frequent build issues involve libmagic availability, compression-related failures, missing favicons or welcome pages, and licensing oversights. The remedies are straightforward and well-supported by tooling and project documentation.[^1][^4]

Table 11. Symptom → Cause → Resolution

| Symptom                                            | Likely cause                                           | Resolution                                                                                  |
|----------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------|
| zimwriterfs refuses to start                       | Magic database not found                               | Install libmagic-dev; set MAGIC path; or use --skip-libmagic-check as a last resort[^1]    |
| Build fails with compression errors                | Invalid or inconsistent --minChunkSize; corrupted data | Re-run with default minChunkSize; validate source files; re-create content subset[^4]       |
| Reader fails to open package                       | Missing --welcome; malformed index                     | Provide a valid 48x48 PNG favicon and ensure index.html is present and correct[^4]         |
| Search returns no results                          | Full-text index not enabled                            | Rebuild with --withFullTextIndex; verify indexing in zimcheck output[^1]                   |
| Licensing warnings or redistribution concerns      | Per-file licenses not captured or unclear              | Populate per-file metadata with license type and attribution; review legacy GFDL items[^2] |
| Unexpected redirects or broken internal links      | Missing or incorrect redirects                         | Provide a TSV via --redirects with url, title, target_url entries and re-run[^4]           |

## Licensing and Attribution

Bundles sourced from Wikimedia carry clear licensing expectations. Many articles are available under Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0), with legacy coverage sometimes under the GNU Free Documentation License (GFDL). The project must preserve attribution text, capture per-file license summaries, and ensure that any media with distinct licenses is properly credited.[^2]

Bundles with current affairs and practice sets require a pre-build licensing audit. Only include content that can be redistributed, and record the source, license type, attribution requirements, and any usage restrictions per file. Store this information alongside content and in the package metadata.

Table 12. Source licensing summary

| Source type               | License summary                         | Attribution requirements                          | Notes                                                   |
|---------------------------|-----------------------------------------|---------------------------------------------------|---------------------------------------------------------|
| Wikimedia articles        | CC BY-SA 3.0; legacy GFDL items         | Preserve contributor attribution text             | Confirm per-page license and media licenses             |
| Practice sets (third-party)| To be determined (varies by publisher) | Follow publisher’s redistribution policy          | Obtain permissions if needed; document per-file terms   |
| Current affairs (curated) | To be determined (varies by source)     | Attribute original publisher/author               | Ensure redistribution rights before packaging           |

Information gap. The precise licensing terms for current affairs and practice sets must be confirmed before packaging.

## Final Deliverables and Directory Structure

Final outputs must be organized for discoverability, reuse, and audit. Place all artifacts under the designated packages/openzim directory, keeping a clear separation of scripts, logs, and built ZIM files. Archive the entire set of build logs and checksums alongside the packages to support verification and future rebuilds.

Table 13. Deliverables layout

| Path                         | Description                                        |
|-----------------------------|----------------------------------------------------|
| packages/openzim/scripts/   | Automation scripts and wrapper invocations         |
| packages/openzim/logs/      | Time-stamped build logs and QA reports             |
| packages/openzim/zims/      | Generated ZIM files (one per bundle)               |
| packages/openzim/metadata/  | Per-bundle manifests and per-file license registry |
| packages/openzim/verify/    | zimcheck outputs and diagnostic dumps              |

## Appendices

### A. Proposed Bundles and Command Sketches

- General Awareness (Wikimedia-based)
  - Command sketch: zimwriterfs --welcome=index.html --favicon=... --language=eng --title="RRB NTPC — General Awareness" --description="..." --creator="Wikipedia contributors" --publisher="..." --withFullTextIndex [other options as needed] content/ga/ packages/openzim/zims/rrb_ntpc_general_awareness.zim
  
- Science Compendium
  - Command sketch: zimwriterfs --welcome=index.html --favicon=... --language=eng --title="RRB NTPC — Science Compendium" --description="..." --creator="Wikipedia contributors" --publisher="..." --withFullTextIndex ... content/science/ packages/openzim/zims/rrb_ntpc_science.zim
  
- Current Affairs & Practice Sets (provisional)
  - Command sketch: similar invocation after licensing audit; include redirect TSV if canonicalization is required.

Note: Replace “..." with project-specific values and ensure all options comply with the zimwriterfs man page. Execute via the official container image if native tools are unavailable.[^3][^4]

### B. Bundled Metadata Template (illustrative)

- Title: RRB NTPC — [Bundle Name]
- Language: ISO639-3 (e.g., eng)
- Creator(s): Aggregated from per-file credits (e.g., Wikipedia contributors)
- Publisher: Project-defined
- Description: Human-authored summary of scope and audience
- Tags: education; rrb-ntpc; [subject keywords]
- Welcome page: index.html
- Favicon: 48x48 PNG placed relative to content root
- Licensing: Per-file records showing CC BY-SA 3.0 and any legacy GFDL items; third-party items as determined

### C. Build Verification and Archiving Procedure

- Run zimcheck on each ZIM and archive its stdout/stderr.
- Use zimdump to list or dump samples for spot checks.
- Generate and store checksums (e.g., SHA-256) for each ZIM.
- Consolidate logs, manifests, and QA outputs under packages/openzim for reproducibility.

## Information Gaps

- Licensing clarity for current affairs and practice sets requires confirmation before packaging.
- Exact command-line invocations for zimwriterfs depend on the final content directory structures and naming.
- Availability of native ZIM tooling on the target execution environment is unknown; the container path is specified accordingly.
- Per-file license registries for non-Wikimedia items are not yet centralized; a metadata consolidation step is necessary.
- A dedicated favicon and landing page templates should be prepared if not already present.
- Final bundle names and version identifiers need to be set by the project.

## References

[^1]: openzim/zim-tools: Various ZIM command line tools. https://github.com/openzim/zim-tools  
[^2]: Wikipedia: Geography of India (example per-page metadata). https://en.wikipedia.org/wiki/Geography_of_India  
[^3]: Zimwriterfs instructions - OpenZIM (Docker usage). https://wiki.openzim.org/wiki/Zimwriterfs_instructions  
[^4]: zimwriterfs(1) - Ubuntu manpage. https://manpages.ubuntu.com/manpages/noble/man1/zimwriterfs.1.html  
[^5]: Build your ZIM file - OpenZIM. https://wiki.openzim.org/wiki/Build_your_ZIM_file  
[^6]: FreshPorts: archivers/zim-tools. https://www.freshports.org/archivers/zim-tools/  
[^7]: Arch Linux: zim-tools package. https://archlinux.org/packages/extra/x86_64/zim-tools/  
[^8]: libmagic - File type recognition library. https://www.darwinsys.com/file/  
[^9]: zlib compression library. https://zlib.net/  
[^10]: Gumbo Parser - HTML parsing. https://github.com/google/gumbo-parser  
[^11]: International Components for Unicode (ICU). http://site.icu-project.org/  
[^12]: Kiwix build system. https://github.com/kiwix/kiwix-build  
[^13]: OpenZIM home. https://openzim.org  
[^14]: Google Test. https://github.com/google/googletest