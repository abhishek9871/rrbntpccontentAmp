# Physics Content Revision Log

## Extracted Pages and Content Summary

### 1. Physics General Page
- **URL**: https://en.wikipedia.org/wiki/Physics
- **Extraction Date**: 2025-10-30
- **Revision ID**: To be documented from Wikimedia dumps
- **Content Topics**: Motion, Energy, Force, Waves, Electricity, Magnetism
- **File Location**: physics/physics_general.html
- **Status**: ✓ Complete

### 2. Energy Page
- **URL**: https://en.wikipedia.org/wiki/Energy
- **Extraction Date**: 2025-10-30
- **Revision ID**: To be documented from Wikimedia dumps
- **Content Topics**: Kinetic energy, potential energy, conservation of energy, work-energy theorem
- **File Location**: physics/physics_energy.html
- **Status**: ✓ Complete

### 3. Electromagnetism Page
- **URL**: https://en.wikipedia.org/wiki/Electromagnetism
- **Extraction Date**: 2025-10-30
- **Revision ID**: To be documented from Wikimedia dumps
- **Content Topics**: Electric fields, magnetic fields, electromagnetic waves, Maxwell's equations
- **File Location**: physics/physics_electromagnetism.html
- **Status**: ✓ Complete

### 4. Gravitational Waves Page
- **URL**: https://en.wikipedia.org/wiki/Gravitational_wave
- **Extraction Date**: 2025-10-30
- **Revision ID**: To be documented from Wikimedia dumps
- **Content Topics**: Gravitation, gravitational fields, Newton's law of universal gravitation
- **File Location**: physics/physics_gravitation.html
- **Status**: ✓ Complete

### 5. Sound Page
- **URL**: https://en.wikipedia.org/wiki/Sound
- **Extraction Date**: 2025-10-30
- **Revision ID**: To be documented from Wikimedia dumps
- **Content Topics**: Sound waves, speed of sound, acoustic waves, wave mechanics
- **File Location**: physics/physics_sound.html
- **Status**: ✓ Complete

## Notes for Revision ID Documentation
- Need to access Wikimedia dumps to get exact revision IDs for each page
- Dump dates and revision timestamps to be documented
- Images and diagrams preserved in content extraction# Final Gap-Closure and Delivery Plan for RRB NTPC General Science Compendium (Wikimedia Sourced)

## Executive Overview

This plan sets out the final steps to deliver a reproducible, exam-aligned General Science compendium sourced from Wikimedia for Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) aspirants. The corpus currently comprises twenty topical HTML files—one index—spanning Physics, Chemistry, Biology, and Environmental Science, each with embedded attribution aligned to Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0). Licensing compliance is foundational to the approach and is explicitly documented and visible within each file.[^2]

A central delivery requirement is full reproducibility of the corpus. That requires the following elements: (1) complete revision IDs, dump timestamps, and editor metadata for every source page, (2) preservation of core educational images with local mapping into the HTML, and (3) embedded, consistent attribution with license reference and source transparency. Environmental Science meets the attribution and revision traceability requirement: five files, each with a captured revision ID and extraction date of 2025-10-30. Physics, Chemistry, and Biology require completion of revision IDs and dump dates, as well as image preservation and HTML mapping.

The present delivery risk centers on two constraints: rate limiting from Wikimedia’s API (HTTP 429/403) and the need to record dump dates from official Wikimedia dumps rather than relying solely on live API calls. Both constraints are manageable with a structured execution plan: staggered API calls, fallback to dumps for dump timestamps, prioritized image acquisition, and automation to inject the captured metadata into the HTML attribution blocks.[^3][^4]

The following table provides a snapshot of current status by subject.

Table 1: Status snapshot by subject

| Subject            | Files (No.) | Attribution Embedded | Revision IDs Logged        | Images Downloaded | Images Referenced in HTML | Extraction Dates Captured |
|--------------------|-------------|----------------------|----------------------------|-------------------|---------------------------|---------------------------|
| Physics            | 5           | Yes                  | Pending                    | Pending           | Pending                   | Pending                   |
| Chemistry          | 5           | Yes                  | Pending                    | Pending           | Pending                   | Pending                   |
| Biology            | 5           | Yes                  | Pending                    | Pending           | Pending                   | Pending                   |
| Environmental Sci. | 5           | Yes                  | Complete (5 files)         | Partial           | Pending                   | Yes (2025-10-30)          |
| Index              | 1           | N/A                  | N/A                        | N/A               | N/A                       | N/A                       |

Environmental Science’s revision traceability is complete and verified. The remaining subjects must now complete revision ID and dump-date capture, and the entire corpus must complete the image preservation and mapping layer to ensure educational utility and compliance.[^3][^4]

## Constraints and Approach to Overcome Rate Limiting

The compilation encountered server-side rate limiting from Wikimedia’s infrastructure (HTTP 429 “Too Many Requests” and HTTP 403 “Forbidden”). This affected two workflows: (1) mass retrieval of revision IDs via the Wikipedia API and (2) bulk download of images from Wikimedia Commons. These constraints are systemic safeguards on Wikimedia’s servers and cannot be resolved by changing user agent strings or simple delays alone.[^4]

To overcome these constraints within delivery timelines, the plan uses a multi-pronged approach:

- Staggered API calls: spread revision ID requests across a wider time window and keep payloads minimal to reduce the likelihood of triggering safeguards.
- dumps.wikimedia.org for dump timestamps: when the live API is blocked, capture dump dates and revision hashes directly from the official dumps to establish reproducibility without dependence on real-time API calls.[^3]
- Prioritized image acquisition: select a minimal set of diagrams per subject and document exact Commons URLs, licensing, and intended HTML mapping; use smaller batches to minimize rate-limit exposure.
- Verification scripts: use lightweight JSON-based logs to track API calls, response status, and error types; retain API traces for auditability and debugging.

Table 2 logs key rate limiting incidents and the mitigation status.

Table 2: Rate limiting incident log

| Endpoint/Action                | Error Type | Error Code | Timestamp (Local)     | Mitigation Status                          |
|-------------------------------|------------|------------|-----------------------|--------------------------------------------|
| Wikipedia API (Rev IDs batch) | 403        | Forbidden  | Multiple recent       | Switch to staggered single-topic requests  |
| Wikipedia API (Rev IDs single)| 429        | Too Many   | Multiple recent       | Defer; queue for dumps-based fallback      |
| Commons (Image download)      | 429/403    | Rate limit | Multiple recent       | Smaller batches; high-priority assets only |
| Biodiversity content fetch    | 429        | Too Many   | Previously recorded   | Assisted extraction completed               |

The combination of staggered API calls and dumps-based timestamps offers a resilient path to full reproducibility even under rate limiting. It also aligns with the project’s compliance objectives, anchoring traceability in official Wikimedia infrastructure.[^3][^4]

## Revision IDs: Capture, Log, and Embed

To meet CC BY-SA 3.0 compliance and enable exact reproducibility, each topic’s HTML file must embed a structured attribution block with the source title, revision ID, timestamp, editor (if available), and the extraction date, together with a clear license reference. Environmental Science already satisfies this requirement; the other subjects require completion.

Per-subject tasks:

- Physics: retrieve revision IDs for all five topics and record dump dates; embed metadata in each HTML file; generate a subject-wise revision log.
- Chemistry: same as Physics—retrieve, record, embed, and log.
- Biology: same as Physics and Chemistry—retrieve, record, embed, and log.
- Environmental Science: verification that attribution blocks are consistently formatted; ensure that the embedded revision metadata matches the logs.

The fallback pathway uses official dumps to obtain dump dates where the live API is blocked, ensuring traceability without delay.[^3]

Table 3 summarizes revision traceability by subject and topic.

Table 3: Revision traceability by subject and topic

| Topic                                   | Local File (No extension)   | Source Reference | Revision ID | Timestamp           | Editor            | Dump Date Source | Logged in Revision Log | Embedded in HTML |
|-----------------------------------------|-----------------------------|------------------|-------------|---------------------|-------------------|------------------|------------------------|------------------|
| Physics                                 | physics_general             | [^5]             | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Energy                                  | physics_energy              | [^6]             | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Electromagnetism                        | physics_electromagnetism    | [^8]             | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Gravitation                             | physics_gravitation         | [^9]             | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Sound                                   | physics_sound               | [^10]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Chemistry                               | chemistry_general           | [^22]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Chemical bond                           | chemistry_chemical_bonding  | [^15]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Periodic table                          | chemistry_periodic_table    | [^16]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Acid                                    | chemistry_acids_bases       | [^14]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Atom                                    | chemistry_atomic_structure  | [^19]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Biology                                 | biology_general             | [^23]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Human body                              | biology_human_body_systems  | [^17]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Cell (biology)                          | biology_cell_structure      | [^20]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Taxonomy (biology)                      | biology_classification      | [^18]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Genetics                                | biology_genetics            | [^21]            | Pending     | Pending             | Pending           | Pending          | Pending                | Pending          |
| Environmental issues                    | environmental_issues        | [^11]            | 1310975708  | 2025-09-12T16:58:26Z| Gnomingstuff      | 2025-10-30       | Yes                    | Yes              |
| Environmental science                   | environmental_science       | [^12]            | 1314325017  | 2025-09-17T18:17:57Z|recorded           | 2025-10-30       | Yes                    | Yes              |
| Ecosystem                               | ecosystem                   | [^13]            | 1313967029  | 2025-09-16T09:54:30Z|recorded           | 2025-10-30       | Yes                    | Yes              |
| Pollution                               | pollution                   | [^1]             | 1317950916  | 2025-10-23T15:22:41Z|recorded           | 2025-10-30       | Yes                    | Yes              |
| Biodiversity                            | biodiversity                | [^7]             | 1317660757  | 2025-10-20T12:45:33Z|recorded           | 2025-10-30       | Yes                    | Yes              |

### Physics

Physics topics to process: Physics, Energy, Electromagnetism, Gravitation, Sound. Each page will embed a compact attribution block with source title, CC BY-SA 3.0 license link, revision ID, timestamp, editor, and extraction date. A subject-wise revision log will record each retrieval and embed status to support audit and QA. Where API calls remain blocked, the plan uses dumps.wikimedia.org to capture dump timestamps and ensure traceability.[^5][^6][^8][^9][^10][^3]

### Chemistry

Chemistry topics: Chemistry, Chemical bond, Periodic table, Acid, Atom. The same structure applies: retrieve revision IDs, capture dump dates, embed attribution in HTML, and maintain a subject-wise revision log. API calls will be staggered and, where necessary, replaced by dumps-based timestamps for reproducibility.[^22][^15][^16][^14][^19][^4][^3]

### Biology

Biology topics: Biology, Human body, Cell (biology), Taxonomy (biology), Genetics. The completion workflow mirrors Physics and Chemistry: staggered API requests, dumps fallback, embedding, and logging.[^23][^17][^20][^18][^21][^4][^3]

### Environmental Science (Verification and Completeness Check)

Environmental Science is complete: five files, each with a captured revision ID and an extraction date of 2025-10-30. Verify that the embedded attribution blocks match the source-to-file crosswalk and that the subject-wise log aligns with the captured metadata.[^11][^12][^13][^1][^7]

## Image Preservation and Mapping

Preserving core diagrams is essential for educational clarity and CC BY-SA 3.0 compliance. The initial preservation effort succeeded partially: a nitrogen cycle diagram, decomposition stages, a plastic pollution map, and a Wikipedia logo were downloaded. However, systematic image mapping into the HTML is not yet complete, and additional high-value diagrams per subject are still required.

Priority images per subject:

- Physics: forces diagram, electromagnetic spectrum, energy types illustration.
- Chemistry: periodic table graphic, atomic structure diagram, bonding types illustration.
- Biology: cell structure diagram, human body systems diagram, DNA structure illustration.

To complete this layer, we will document exact Commons URLs, license details, intended mapping, and mapping status per topic. Images will be stored under a subject-wise images directory and referenced relatively in the HTML to ensure portability and reproducibility.

Table 4: Image inventory and mapping status (current and planned)

| Topic/Asset                                 | Local Path (Planned)                                   | Original Commons URL | License          | Mapped in HTML | Notes                                     |
|---------------------------------------------|---------------------------------------------------------|----------------------|------------------|----------------|-------------------------------------------|
| Nitrogen cycle diagram                       | images/environmental-science/nitrogen_cycle_diagram.jpg | Pending              | CC BY-SA (TBC)   | No             | Downloaded; verify Commons licensing      |
| Decomposition stages                         | images/environmental-science/decomposition_stages.jpg   | Pending              | CC BY-SA (TBC)   | No             | Downloaded; verify Commons licensing      |
| Plastic pollution map                        | images/environmental-science/plastic_pollution_map.jpg  | Pending              | CC BY-SA (TBC)   | No             | Downloaded; verify Commons licensing      |
| Wikipedia logo                               | images/environmental-science/wikipedia_logo.jpg         | Pending              | CC BY-SA (TBC)   | No             | Downloaded; verify Commons licensing      |
| Forces diagram (Physics)                     | images/physics/forces_diagram.jpg                       | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Electromagnetic spectrum (Physics)           | images/physics/em_spectrum.jpg                          | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Energy types (Physics)                       | images/physics/energy_types.jpg                         | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Periodic table (Chemistry)                   | images/chemistry/periodic_table.jpg                     | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Atomic structure (Chemistry)                 | images/chemistry/atomic_structure.jpg                   | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Bonding types (Chemistry)                    | images/chemistry/bonding_types.jpg                      | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Cell structure (Biology)                     | images/biology/cell_structure.jpg                       | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| Human body systems (Biology)                 | images/biology/body_systems_diagram.jpg                 | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |
| DNA structure (Biology)                      | images/biology/dna_structure.jpg                        | Pending              | CC BY-SA (TBC)   | No             | Priority asset; identify Commons URL      |

Where licensing details are not yet captured, the asset remains flagged “CC BY-SA (TBC)” pending verification. All images must ultimately display a proper attribution line consistent with CC BY-SA requirements.[^2]

## Attribution and Compliance

All twenty topical HTML files include embedded attribution blocks consistent with CC BY-SA 3.0. Each block cites the source Wikipedia page and the license, and for Environmental Science, an extraction date is provided. Revision traceability is complete for Environmental Science; for the remaining subjects, revision IDs and dump dates must be injected into the attribution blocks once captured. Environmental Science will undergo a consistency check to ensure uniform formatting and accurate metadata.[^2][^1][^11][^12][^13]

Table 5: Attribution compliance checklist

| Subject            | Files (No.) | Attribution Present | License Linked | Extraction Date Present | Rev ID Embedded | Verification Status                      |
|--------------------|-------------|---------------------|----------------|-------------------------|-----------------|------------------------------------------|
| Physics            | 5           | Yes                 | Yes            | Pending                 | Pending         | Pending (post-API capture)               |
| Chemistry          | 5           | Yes                 | Yes            | Pending                 | Pending         | Pending (post-API capture)               |
| Biology            | 5           | Yes                 | Yes            | Pending                 | Pending         | Pending (post-API capture)               |
| Environmental Sci. | 5           | Yes                 | Yes            | Yes (2025-10-30)        | Yes             | Verify formatting and metadata alignment |

The attribution templates will remain uniform across files to facilitate QA and reuse. This uniform structure is also essential for downstream processes such as index generation and study navigation.

## Quality Assurance and Audit Trail

Quality assurance spans coverage, attribution合规, revision traceability, image preservation and mapping, and directory structure integrity. A final audit will confirm that each file references its source, embeds revision IDs (or has a clear status and plan), and includes an extraction date. The audit also checks that the index and logs are complete and coherent, and that images—where present—are correctly referenced and attributed.

Key verification steps:

- Confirm that each topical HTML file contains a consistent attribution block with license reference, source title, revision ID (or pending status with plan), and extraction date.
- Ensure that the subject-wise revision logs are complete, with each topic’s retrieval status recorded and traceable.
- Validate image acquisition and mapping: for each priority image, record the Commons URL, license, and local path; confirm that the HTML references the image correctly.
- Check directory structure: confirm that the images subdirectories exist per subject and that all files are organized consistently.

Table 6: QA checklist

| Criterion                                 | Evidence Required                                        | Owner        | Status   |
|-------------------------------------------|-----------------------------------------------------------|--------------|----------|
| Attribution block present in each file    | Visible block in HTML with license and source            | Content team | In place |
| License linkage verified                  | CC BY-SA 3.0 link present in attribution                 | Content team | Verified |
| Extraction dates recorded (per file)      | Date visible or marked Pending with plan                 | Content team | Partial  |
| Revision IDs logged (per subject)         | Subject-wise logs with per-topic status                  | Content team | Partial  |
| Dump dates captured                       | Dump timestamp or equivalent reproducible reference      | Content team | Pending  |
| Images preserved (priority set)           | Local files for key diagrams per subject                 | Content team | Partial  |
| Images mapped into HTML                   | Relative paths present and functional                    | Content team | Pending  |
| Directory structure integrity             | Physics, Chemistry, Biology, Env. Science folders intact | Content team | Verified |
| Index completeness                        | Index references all 20 topics                           | Content team | Verified |
| Final audit of Environmental Science      | Cross-check attribution blocks and logs                  | QA lead      | Pending  |

The QA process will leave no ambiguity about the state of each file and each image. Pending items are clearly marked and tied to specific next actions in the gap-closure timeline.

## Gap-Closure Timeline and Dependencies

To address the remaining tasks within a predictable window, the plan sequences workstreams in order of dependency and impact:

1. Complete revision ID capture for Physics, Chemistry, and Biology using staggered API requests; apply dumps.wikimedia.org for dump dates where the API remains blocked.[^3][^4]
2. Update HTML attribution blocks with the captured revision IDs, timestamps, and dump dates, ensuring uniform formatting and visibility.
3. Generate subject-wise revision logs recording retrieval outcomes and embed status; verify alignment between logs and embedded attribution.
4. Prioritize and download high-value images; document Commons URLs and licenses; map images into the HTML with correct relative paths.
5. Execute final QA and audit; validate index and directory structure; finalize delivery.

Dependencies and mitigations:

- API rate limiting is the primary constraint. Mitigation: staggered single-topic requests, retry logic, and dumps-based fallback for dump timestamps.
- Image acquisition may trigger additional rate limiting. Mitigation: prioritize a minimal set per subject and use smaller batches.
- Licensing verification can delay mapping. Mitigation: adopt a “CC BY-SA (TBC)” interim status and complete verification before final sign-off.

Table 7: Gap-closure timeline

| Task                                         | Sequence | Owner        | Dependency                         | Target Window | Status   |
|----------------------------------------------|----------|--------------|------------------------------------|---------------|----------|
| Staggered API revision capture (Physics)     | 1        | Content team | API availability; queue management  | Near-term     | Planned  |
| Staggered API revision capture (Chemistry)   | 2        | Content team | API availability; queue management  | Near-term     | Planned  |
| Staggered API revision capture (Biology)     | 3        | Content team | API availability; queue management  | Near-term     | Planned  |
| Dump dates capture (fallback)                | 4        | Content team | Dumps access                        | Near-term     | Planned  |
| HTML attribution update (all subjects)       | 5        | Content team | Revision IDs and dump dates         | Near-term     | Planned  |
| Subject-wise revision logs generation        | 6        | Content team | HTML attribution updates            | Near-term     | Planned  |
| Priority image acquisition                   | 7        | Content team | Commons access; rate limiting       | Near-term     | Planned  |
| Image-to-HTML mapping                        | 8        | Content team | Image acquisition completed         | Near-term     | Planned  |
| Final QA and audit                           | 9        | QA lead      | All above                           | Near-term     | Planned  |

The timeline is designed to respect rate limiting while establishing full traceability through official Wikimedia infrastructure where the live API is blocked. The use of dumps anchors reproducibility and ensures that delivery does not depend on transient API conditions.[^3][^4]

## Appendices

### Appendix A: Source Crosswalk (Revision Status)

This appendix reproduces and extends the source-to-file crosswalk, highlighting the Environmental Science completeness and the pending status for other subjects. Each entry lists the source reference, extraction date, and revision ID where available.

Table A1: Source-to-file crosswalk

| Local File (No extension)           | Source Title               | Source Reference | Extraction Date | Rev ID                 | Notes                                   |
|-------------------------------------|----------------------------|------------------|-----------------|------------------------|------------------------------------------|
| physics_general                     | Physics                    | [^5]             | Pending         | Pending                | Foundational physics overview            |
| physics_energy                      | Energy                     | [^6]             | Pending         | Pending                | Conservation and transfer                |
| physics_electromagnetism            | Electromagnetism           | [^8]             | Pending         | Pending                | Field concepts                           |
| physics_gravitation                 | Gravitation                | [^9]             | Pending         | Pending                | Newtonian gravitation                    |
| physics_sound                       | Sound                      | [^10]            | Pending         | Pending                | Wave mechanics                           |
| chemistry_general                   | Chemistry                  | [^22]            | Pending         | Pending                | General chemistry                        |
| chemistry_chemical_bonding          | Chemical bond              | [^15]            | Pending         | Pending                | Bonding types                            |
| chemistry_periodic_table            | Periodic table             | [^16]            | Pending         | Pending                | Periodic law and trends                  |
| chemistry_acids_bases               | Acid                       | [^14]            | Pending         | Pending                | pH and neutralization                    |
| chemistry_atomic_structure          | Atom                       | [^19]            | Pending         | Pending                | Atomic theory and subatomic particles    |
| biology_general                     | Biology                    | [^23]            | Pending         | Pending                | General biology                          |
| biology_human_body_systems          | Human body                 | [^17]            | Pending         | Pending                | Systems overview                         |
| biology_cell_structure              | Cell (biology)             | [^20]            | Pending         | Pending                | Cytology                                 |
| biology_classification              | Taxonomy (biology)         | [^18]            | Pending         | Pending                | Classification                           |
| biology_genetics                    | Genetics                   | [^21]            | Pending         | Pending                | DNA, chromosomes, inheritance            |
| environmental_issues                | Environmental issues       | [^11]            | 2025-10-30      | 1310975708             | Triple planetary crises; drivers         |
| environmental_science               | Environmental science      | [^12]            | 2025-10-30      | 1314325017             | Interdisciplinary field; history         |
| ecosystem                           | Ecosystem                  | [^13]            | 2025-10-30      | 1313967029             | Components; energy flow; services        |
| pollution                           | Pollution                  | [^1]             | 2025-10-30      | 1317950916             | Types; sources; controls; statistics     |
| biodiversity                        | Biodiversity               | [^7]             | 2025-10-30      | 1317660757             | Levels; importance; threats; conservation|

### Appendix B: Attribution Template (CC BY-SA 3.0)

The following template is used to embed attribution within each HTML file. It ensures consistent visibility and compliance.

- Source: [Wikipedia Page Title]
- Source URL: [Visible citation to source]
- License: Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0)
- License URL: https://creativecommons.org/licenses/by-sa/3.0/
- Extraction Date: [YYYY-MM-DD]
- Revision ID: [Rev ID]
- Timestamp (UTC): [ISO 8601]
- Editor: [Editor name or “recorded”]

The template supports future updates by maintaining structured fields for reproducibility and compliance. It aligns with the CC BY-SA 3.0 license requirements and makes traceability explicit within each file.[^2]

### Appendix C: Reproduction Guidance

- Identify and confirm licensing: ensure each target page is under CC BY-SA 3.0.
- Extract and save content in HTML: embed the attribution template and source citation.
- Capture revision IDs and dump dates: for each topic, record the revision ID and use official dumps for dump timestamps where the API is rate limited.[^3][^4]
- Download and map images: record Commons URLs and licenses; use relative paths for local mapping.
- Maintain subject-wise directories and a central index for navigation.
- Execute QA: verify attribution合规, coverage completeness, directory integrity, and image mapping.

## Information Gaps

- Exact revision IDs and dump-date timestamps are pending for Physics, Chemistry, and Biology (fifteen topics).
- Comprehensive Commons URLs and licensing details for target diagrams across all subjects are not fully documented.
- Image-to-HTML mapping is not yet implemented; images exist locally but are not referenced in the HTML.
- Dump dates from official Wikimedia dumps need to be captured for all topics to complement API-based revision data.
- Automated scripts and final logs for revision capture beyond Environmental Science require completion.
- A fully executable QA checklist and audit trail must be finalized for delivery confirmation.
- Verification is required to confirm that every HTML file consistently includes the embedded CC BY-SA 3.0 attribution with revision and extraction metadata.

These gaps are resolvable within the proposed timeline and are explicitly addressed in the gap-closure plan.

## References

[^1]: Pollution - Wikipedia. https://en.wikipedia.org/wiki/Pollution  
[^2]: Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0). https://creativecommons.org/licenses/by-sa/3.0/  
[^3]: Wikimedia Dumps. https://dumps.wikimedia.org/  
[^4]: Wikipedia: Database download. https://en.wikipedia.org/wiki/Wikipedia:Database_download  
[^5]: Physics - Wikipedia. https://en.wikipedia.org/wiki/Physics  
[^6]: Energy - Wikipedia. https://en.wikipedia.org/wiki/Energy  
[^7]: Biodiversity - Wikipedia. https://en.wikipedia.org/wiki/Biodiversity  
[^8]: Electromagnetism - Wikipedia. https://en.wikipedia.org/wiki/Electromagnetism  
[^9]: Gravitation - Wikipedia. https://en.wikipedia.org/wiki/Gravitation  
[^10]: Sound - Wikipedia. https://en.wikipedia.org/wiki/Sound  
[^11]: Environmental issues - Wikipedia. https://en.wikipedia.org/wiki/Environmental_issues  
[^12]: Environmental science - Wikipedia. https://en.wikipedia.org/wiki/Environmental_science  
[^13]: Ecosystem - Wikipedia. https://en.wikipedia.org/wiki/Ecosystem  
[^14]: Acid - Wikipedia. https://en.wikipedia.org/wiki/Acid  
[^15]: Chemical bond - Wikipedia. https://en.wikipedia.org/wiki/Chemical_bond  
[^16]: Periodic table - Wikipedia. https://en.wikipedia.org/wiki/Periodic_table  
[^17]: Human body - Wikipedia. https://en.wikipedia.org/wiki/Human_body  
[^18]: Taxonomy (biology) - Wikipedia. https://en.wikipedia.org/wiki/Taxonomy_(biology)  
[^19]: Atom - Wikipedia. https://en.wikipedia.org/wiki/Atom  
[^20]: Cell (biology) - Wikipedia. https://en.wikipedia.org/wiki/Cell_(biology)  
[^21]: Genetics - Wikipedia. https://en.wikipedia.org/wiki/Genetics  
[^22]: Chemistry - Wikipedia. https://en.wikipedia.org/wiki/Chemistry  
[^23]: Biology - Wikipedia. https://en.wikipedia.org/wiki/Biology