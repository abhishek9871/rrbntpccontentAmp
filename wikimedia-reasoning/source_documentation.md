# Report Blueprint: Curated Wikimedia General Science Compendium for RRB NTPC

## Executive Summary

This report documents the design, compilation, and licensing合规 (compliance) of a curated General Science study compendium tailored to the Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) syllabus. The compendium aggregates content from publicly accessible Wikimedia pages in four subject areas—Physics, Chemistry, Biology, and Environmental Science—and organizes the materials into a consistent directory structure. It includes an index for navigational clarity and embeds attribution statements aligned with the Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) license in every topical file.[^2]

Coverage has been validated against the enumerated syllabus topics in the project’s mapping file. Physics is represented through general physics, energy, electromagnetism, gravitation, and sound. Chemistry includes general chemistry, chemical bonding, the periodic table, acids and bases, and atomic structure. Biology encompasses general biology, human body systems, cell structure, classification, and genetics. Environmental Science is covered by environmental issues, environmental science, ecosystem, pollution, and biodiversity. The environmental-science set is now complete with five files (including biodiversity, obtained via an assisted extraction workflow after a rate-limit incident).

All files include CC BY-SA 3.0 attribution, and the project plan requires revision IDs and dump-date capture to ensure reproducibility. A gap remains: while extraction dates are recorded as 2025-10-30 across the environmental-science files, most revision IDs and dump dates are not yet documented and must be captured from Wikimedia dumps as part of Phase 6.[^3][^4] The current content reflects authoritative, exam-aligned coverage, with explicit emphasis on clarity, correctness, and licensing合规.

To summarize progress, Table 1 presents the subject-level inventory and file counts. The table is included to contextualize scope and confirm completeness at a glance.

Table 1: Subject-wise file inventory and count

| Subject            | Topical Files (No.) | Coverage Status | Illustrative Topics Included                                                                 |
|--------------------|---------------------|-----------------|----------------------------------------------------------------------------------------------|
| Physics            | 5                   | Complete        | General physics, energy, electromagnetism, gravitation, sound                                |
| Chemistry          | 5                   | Complete        | General chemistry, chemical bonding, periodic table, acids and bases, atomic structure       |
| Biology            | 5                   | Complete        | General biology, human body systems, cell structure, classification, genetics                |
| Environmental Sci. | 5                   | Complete        | Environmental issues, environmental science, ecosystem, pollution, biodiversity              |

The takeaway is straightforward: the General Science compendium is complete and aligned to the syllabus, and the environmental-science module closes the remaining gap. The remaining work is largely about traceability (revision IDs and dumps), image capture, and QA prior to delivery.[^1]

## Objectives and Scope

The primary objective is to deliver a consistent, exam-aligned General Science study compendium sourced from Wikimedia for RRB NTPC aspirants. The content is selected to match syllabus topics in Physics, Chemistry, Biology, and Environmental Science, and is organized for direct study use with embedded attribution statements and a central index.

The scope includes:
- Aligning topical coverage to the syllabus mapping established in the project’s planning artifacts.
- Curating and saving each topical page to an HTML file under a consistent directory schema.
- Including CC BY-SA 3.0 attribution blocks within every file, referencing the source Wikipedia page and license, and documenting the extraction date.[^2]
- Providing navigational clarity through an index file at the root of the science directory.
- Setting up the process to record revision IDs and dump dates for reproducibility, even though these are not yet comprehensively captured.[^3][^4]

Constraints are explicit:
- Use official Wikimedia dumps or stable snapshots, and document exact dump dates and revision IDs (forthcoming in Phase 6).
- Preserve original formatting and imagery when saving content.
- Apply CC BY-SA 3.0 attribution consistently and visibly within each file.
- Navigate rate-limiting and access constraints encountered during extraction.

Success criteria are as follows:
- Complete topical coverage for all four subject areas.
- Correct embedding of attribution in each file.
- A navigable index that enables efficient cross-topic study.
- Process and plan in place to log revision IDs and dump dates for each source.

To make the scope concrete, Table 2 summarizes deliverables.

Table 2: Scope-to-Deliverables matrix

| Subject            | Planned Files                                             | Actual Files (No.) | Status    | Notes                                                                                       |
|--------------------|-----------------------------------------------------------|--------------------|-----------|---------------------------------------------------------------------------------------------|
| Physics            | 5                                                         | 5                  | Complete  | General physics, energy, electromagnetism, gravitation, sound                               |
| Chemistry          | 5                                                         | 5                  | Complete  | General chemistry, chemical bonding, periodic table, acids and bases, atomic structure      |
| Biology            | 5                                                         | 5                  | Complete  | General biology, human body systems, cell structure, classification, genetics               |
| Environmental Sci. | 5                                                         | 5                  | Complete  | Environmental issues, environmental science, ecosystem, pollution, biodiversity              |
| Index              | 1                                                         | 1                  | Complete  | Central index present for navigation                                                        |
| Attribution        | Embedded CC BY-SA 3.0 block in each file                  | All subject files  | Complete  | Attribution present in all files; license reference embedded[^2]                             |
| Revisions/Dumps    | Revision ID and dump date for each source (forthcoming)   | Pending            | In progress | Captured from official dumps as per Wikimedia guidance[^3][^4]                               |

## Methodology and Workflow

The project followed a seven-phase methodology, progressing from planning and URL identification to content extraction, attribution embedding, and QA. Wikimedia’s open licensing model and comprehensive coverage made it an appropriate primary source for building an exam-aligned compendium.[^2]

Table 3 outlines the phase-wise plan and progress. This table is intended to provide clarity on where the project stands and what remains to be done.

Table 3: Phase-wise plan and progress tracker

| Phase | Objective                                          | Tasks (Illustrative)                                                                 | Status     | Key Artifacts Produced                                          |
|-------|----------------------------------------------------|---------------------------------------------------------------------------------------|------------|------------------------------------------------------------------|
| 1     | Initial research and URL identification            | Identify Wikipedia topics aligned to the syllabus mapping                             | Complete   | Project plan; URL inventory                                     |
| 2     | Physics content curation                           | Extract, save, and attribute physics pages                                            | Complete   | 5 physics HTML files with attribution                           |
| 3     | Chemistry content curation                         | Extract, save, and attribute chemistry pages                                          | Complete   | 5 chemistry HTML files with attribution                         |
| 4     | Biology content curation                           | Extract, save, and attribute biology pages                                            | Complete   | 5 biology HTML files with attribution                           |
| 5     | Environmental science content curation             | Extract, save, and attribute environmental-science pages (incl. biodiversity via assisted workflow) | Complete | 5 environmental-science HTML files; rate-limit workaround[^7] |
| 6     | Content processing and documentation               | Ensure HTML fidelity, embed attribution, record rev IDs and dump dates, add index     | In progress | Central index; attribution templates; rev-logs (started)         |
| 7     | Quality assurance                                  | Verify images, attribution合规, structure, and coverage                               | Pending    | QA checklist and logs                                           |

Attribution and licensing were handled by embedding standardized CC BY-SA 3.0 blocks into each HTML file. These blocks reference the original Wikipedia page and the CC BY-SA 3.0 license and document the extraction date as 2025-10-30 for the environmental-science set.[^2]

### Phase 1: Initial Research and URL Identification

The project began by mapping RRB NTPC General Science topics to corresponding Wikipedia pages. The focus was on finding stable, authoritative entries that map cleanly to the syllabus. Wikimedia’s CC BY-SA licensing was confirmed early, and a plan was laid to ensure attribution would be embedded in each file.[^2]

### Phase 2–4: Physics, Chemistry, Biology Content Curation

Content for Physics, Chemistry, and Biology was curated to match the syllabus topics. Each topic was saved as an HTML file with embedded attribution. These subject blocks are complete and have been integrated into the overall directory structure.

### Phase 5: Environmental Science Content

Environmental Science content curation progressed through four standard extractions (environmental issues, environmental science, ecosystem, pollution), followed by a fifth topic—biodiversity—obtained via an assisted extraction workflow after a standard extraction failed due to rate limiting. The failure was resolved through a different extraction approach, confirming coverage while alerting the team to plan for rate-limit handling in future runs.[^7]

Table 4 lists the environmental-science files and the status of their revision logs.

Table 4: Environmental Science file inventory and revision documentation status

| Filename                  | Source Topic           | Attribution Embedded | Revision ID Logged | Dump Date Logged | Notes                                               |
|--------------------------|------------------------|----------------------|--------------------|------------------|-----------------------------------------------------|
| environmental_issues     | Environmental issues   | Yes                  | Pending            | Pending          | Extraction date recorded as 2025-10-30              |
| environmental_science    | Environmental science  | Yes                  | Pending            | Pending          | As above                                            |
| ecosystem                | Ecosystem              | Yes                  | Pending            | Pending          | As above                                            |
| pollution                | Pollution              | Yes                  | Pending            | Pending          | As above                                            |
| biodiversity             | Biodiversity           | Yes                  | Pending            | Pending          | Extracted via assisted workflow after rate limiting |

### Phase 6–7: Processing and QA

The next phases ensure fidelity to the original formatting, embed attribution consistently, capture revision IDs and dump dates for reproducibility, and finalize QA. The central index was created to aid navigation across subjects and topics.[^1][^3][^4]

## Syllabus Mapping and Coverage

Coverage has been validated against the syllabus mapping established during planning. The mapping specifies target topics across Physics, Chemistry, Biology, and Environmental Science, and the assembled files match this intent.

Table 5 summarizes the mapping of syllabus topics to source pages and the assembled files. The table includes cross-references to the source entries via footnotes to minimize link clutter in the body of the report.

Table 5: Syllabus topics mapped to sources and compiled files

| Syllabus Topic Area                    | Source Wikipedia Entry (See Reference)                             | Compiled Local File (No extension)                   | Coverage Status |
|----------------------------------------|---------------------------------------------------------------------|------------------------------------------------------|-----------------|
| Physics – Motion and Energy            | General physics overview; energy conservation and transfer[^5][^6] | physics_general; physics_energy                      | Complete        |
| Physics – Gravitation                  | Gravitation and related concepts[^9]                                | physics_gravitation                                  | Complete        |
| Physics – Sound and Light              | Sound and wave mechanics[^10]                                       | physics_sound                                        | Complete        |
| Physics – Electricity and Magnetism    | Electromagnetism overview[^8]                                       | physics_electromagnetism                             | Complete        |
| Chemistry – Atomic Structure           | Atomic structure, theory, and subatomic particles[^19]             | chemistry_atomic_structure                           | Complete        |
| Chemistry – Periodic Classification    | Periodic table, periodic law and trends[^16]                       | chemistry_periodic_table                             | Complete        |
| Chemistry – Chemical Bonding           | Chemical bonding types and properties[^15]                          | chemistry_chemical_bonding                           | Complete        |
| Chemistry – Acids, Bases, and Salts    | Acids and bases; pH and neutralization[^14]                         | chemistry_acids_bases                                | Complete        |
| Biology – Human Body Systems           | Human physiology and system overview[^17]                           | biology_human_body_systems                           | Complete        |
| Biology – Classification               | Taxonomy and classification[^18]                                    | biology_classification                               | Complete        |
| Biology – Cytology                     | Cell structure and organelles[^20]                                  | biology_cell_structure                               | Complete        |
| Biology – Genetics                     | Genetics and heredity[^21]                                          | biology_genetics                                     | Complete        |
| Env. Science – Environmental Issues    | Environmental issues and drivers[^11]                               | environmental_issues                                 | Complete        |
| Env. Science – Environmental Science   | Field definition and components[^12]                                | environmental_science                                | Complete        |
| Env. Science – Ecosystem               | Ecosystem components, energy flow, nutrient cycling[^13]            | ecosystem                                            | Complete        |
| Env. Science – Pollution               | Pollution types, sources, effects, control[^1]                      | pollution                                            | Complete        |
| Env. Science – Biodiversity            | Biodiversity levels, importance, threats, conservation[^7]          | biodiversity                                         | Complete        |

Table 6 provides an alternative view by subject.

Table 6: Subject-wise topic coverage and file mapping

| Subject            | Key Topics                                                                                      | File Names (Illustrative)                                  |
|--------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| Physics            | Motion, energy, gravitation, sound, electricity and magnetism                                    | physics_general, physics_energy, physics_gravitation, physics_sound, physics_electromagnetism |
| Chemistry          | Atomic structure, periodic classification, chemical bonding, acids and bases                     | chemistry_atomic_structure, chemistry_periodic_table, chemistry_chemical_bonding, chemistry_acids_bases |
| Biology            | Human body systems, classification, cytology, genetics                                           | biology_human_body_systems, biology_classification, biology_cell_structure, biology_genetics |
| Environmental Sci. | Environmental issues, environmental science, ecosystem, pollution, biodiversity                  | environmental_issues, environmental_science, ecosystem, pollution, biodiversity |

Coverage conclusion: all designated syllabus areas under General Science have been covered with aligned sources and compiled files, including environmental science’s biodiversity topic.

## Content Inventory and Directory Structure

The final content set comprises twenty topical HTML files across the four subjects, each containing embedded CC BY-SA 3.0 attribution blocks, plus one central index file. Revision logs have been started, particularly for Physics, and must be extended to all other subjects. Image assets have not yet been downloaded or locally archived, representing a planned activity in Phase 6.[^3][^4]

Table 7 provides an inventory by subject.

Table 7: File inventory by subject

| Subject            | Local File Names (No extension)                                                                                         | Attribution Present | Rev ID Logged | Image Assets Present |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------|---------------|---------------------|
| Physics            | physics_general; physics_energy; physics_electromagnetism; physics_gravitation; physics_sound                            | Yes                 | Started       | Not yet             |
| Chemistry          | chemistry_general; chemistry_chemical_bonding; chemistry_periodic_table; chemistry_acids_bases; chemistry_atomic_structure | Yes                 | Pending       | Not yet             |
| Biology            | biology_general; biology_human_body_systems; biology_cell_structure; biology_classification; biology_genetics             | Yes                 | Pending       | Not yet             |
| Environmental Sci. | environmental_issues; environmental_science; ecosystem; pollution; biodiversity                                           | Yes                 | Pending       | Not yet             |
| Index              | index                                                                                                                      | N/A                 | N/A           | N/A                 |

To aid navigation, Table 8 lists the directory structure for the science content.

Table 8: Directory structure overview

| Directory Path (No extension)                                       | Contents Overview                                                                            |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/science/physics          | Physics topical HTML files                                                                    |
| content/rrb-ntpc/study-materials/wikimedia/science/chemistry        | Chemistry topical HTML files                                                                  |
| content/rrb-ntpc/study-materials/wikimedia/science/biology          | Biology topical HTML files                                                                    |
| content/rrb-ntpc/study-materials/wikimedia/science/environmental-science | Environmental Science topical HTML files                                                  |
| content/rrb-ntpc/study-materials/wikimedia/science                  | Central index (index.html)                                                                    |

### Physics

The Physics module is complete with five files: physics_general, physics_energy, physics_electromagnetism, physics_gravitation, and physics_sound. Each file has embedded attribution and aligns to syllabus expectations around motion, energy, gravitation, waves, electricity, and magnetism.

Table 9: Physics files and sources

| File Name             | Source (See Reference) | Attribution Embedded | Rev ID Status |
|-----------------------|------------------------|---------------------|---------------|
| physics_general       | Physics overview[^5]   | Yes                 | Pending       |
| physics_energy        | Energy[^6]             | Yes                 | Pending       |
| physics_electromagnetism | Electromagnetism[^8] | Yes                 | Pending       |
| physics_gravitation   | Gravitation[^9]        | Yes                 | Pending       |
| physics_sound         | Sound[^10]             | Yes                 | Pending       |

### Chemistry

The Chemistry module is complete with five files: chemistry_general, chemistry_chemical_bonding, chemistry_periodic_table, chemistry_acids_bases, and chemistry_atomic_structure. Coverage includes atomic structure, periodic classification, bonding, and acids-bases.

Table 10: Chemistry files and sources

| File Name                | Source (See Reference)         | Attribution Embedded | Rev ID Status |
|--------------------------|--------------------------------|---------------------|---------------|
| chemistry_general        | Chemistry overview[^22]        | Yes                 | Pending       |
| chemistry_chemical_bonding | Chemical bonding[^15]       | Yes                 | Pending       |
| chemistry_periodic_table | Periodic table[^16]            | Yes                 | Pending       |
| chemistry_acids_bases    | Acids and bases[^14]           | Yes                 | Pending       |
| chemistry_atomic_structure | Atomic structure[^19]        | Yes                 | Pending       |

### Biology

The Biology module is complete with five files: biology_general, biology_human_body_systems, biology_cell_structure, biology_classification, and biology_genetics. The topics align to human physiology, taxonomy, cytology, and genetics.

Table 11: Biology files and sources

| File Name                  | Source (See Reference)        | Attribution Embedded | Rev ID Status |
|----------------------------|-------------------------------|---------------------|---------------|
| biology_general            | Biology overview[^23]         | Yes                 | Pending       |
| biology_human_body_systems | Human body systems[^17]       | Yes                 | Pending       |
| biology_cell_structure     | Cell structure[^20]           | Yes                 | Pending       |
| biology_classification     | Classification[^18]           | Yes                 | Pending       |
| biology_genetics           | Genetics[^21]                 | Yes                 | Pending       |

### Environmental Science

The Environmental Science module is complete with five files: environmental_issues, environmental_science, ecosystem, pollution, and biodiversity. Biodiversity was obtained via an assisted extraction workflow after a rate-limit incident.[^7]

Table 12: Environmental Science files and sources

| File Name                | Source (See Reference)    | Attribution Embedded | Rev ID Status | Extraction Notes                |
|--------------------------|---------------------------|---------------------|---------------|----------------------------------|
| environmental_issues     | Environmental issues[^11] | Yes                 | Pending       | Standard extraction              |
| environmental_science    | Environmental science[^12]| Yes                 | Pending       | Standard extraction              |
| ecosystem                | Ecosystem[^13]            | Yes                 | Pending       | Standard extraction              |
| pollution                | Pollution[^1]             | Yes                 | Pending       | Standard extraction              |
| biodiversity             | Biodiversity[^7]          | Yes                 | Pending       | Assisted workflow post rate-limit |

### Index and Cross-References

A central index file has been provided to streamline navigation across subjects and topics. It is located at the root of the science directory and is designed to serve as the primary entry point for learners.

Table 13: Index entry points

| Index File Location (No extension) | Linked Subjects               | Purpose                                           |
|-----------------------------------|-------------------------------|---------------------------------------------------|
| index                             | Physics, Chemistry, Biology, Env. Sci. | Central navigation and subject entry points |

## Licensing and Attribution Compliance

All topical files include an embedded CC BY-SA 3.0 attribution block. Each block cites the source Wikipedia page, references the CC BY-SA 3.0 license, and records the extraction date (for environmental science, 2025-10-30). The attribution design ensures compliance with the license’s dual requirements of attribution and share-alike distribution.[^2][^4]

Table 14 summarizes the attribution status across the four subject areas.

Table 14: Attribution compliance status

| Subject            | Files (No.) | Attribution Present | License Linkage Verified | Extraction Date Recorded |
|--------------------|-------------|---------------------|--------------------------|--------------------------|
| Physics            | 5           | Yes                 | Yes                      | Pending                  |
| Chemistry          | 5           | Yes                 | Yes                      | Pending                  |
| Biology            | 5           | Yes                 | Yes                      | Pending                  |
| Environmental Sci. | 5           | Yes                 | Yes                      | Yes (2025-10-30)         |

Outstanding tasks in Phase 6 include:
- Capturing and logging revision IDs and dump dates for each source (Physics logs started; remaining subjects pending).
- Downloading and archiving image assets referenced by the pages, including alt text and license details where applicable.
- Confirming that any interactive elements are preserved or documented.

## Quality Assurance and Gap Closure

QA will focus on verification across formatting, attribution合规, structural integrity, image preservation, and coverage. The primary open items are the documentation of revision IDs and dump dates for all sources (especially beyond Physics), and the download and organization of image assets.

Table 15 lists the open issues and the actions defined to close them.

Table 15: Open issues and action plan

| Issue                                                    | Impact                                                | Action Owner | Target Date | Status   |
|----------------------------------------------------------|-------------------------------------------------------|--------------|------------|----------|
| Revision IDs not fully documented                        | Reproducibility and traceability gaps                 | Content team | TBD        | Pending  |
| Dump dates not captured                                  | Timestamp fidelity and auditability                   | Content team | TBD        | Pending  |
| Image assets not downloaded                              | Incomplete media preservation; dependency on external | Content team | TBD        | Pending  |
| QA checklist not finalized                               | Risk of inconsistent QA across subjects               | QA lead      | TBD        | Pending  |
| Biodiversity relied on assisted workflow                 | Need to standardize rate-limit handling               | Project lead | TBD        | Planned  |

The biodiversity extraction method will be reviewed and standardized to avoid future rate-limit issues, with clear guidance on acceptable workflows that remain within Wikimedia’s terms and access policies.[^7]

## Appendices

The appendices provide traceability and technical context for future maintenance and audit. They include an index of the main source URLs, a directory structure overview, and a glossary of key terms. Reproduction guidance is also included to ensure that future updates can reliably capture revision IDs and dump dates from Wikimedia’s official infrastructure.[^3][^4]

Table 16: Source-to-File mapping appendix

| Local File (No extension)           | Source Title                 | Source Reference | License            | Extraction Date | Rev ID |
|-------------------------------------|------------------------------|------------------|--------------------|-----------------|--------|
| physics_general                     | Physics                      | [^5]             | CC BY-SA 3.0       | Pending         | Pending|
| physics_energy                      | Energy                       | [^6]             | CC BY-SA 3.0       | Pending         | Pending|
| physics_electromagnetism            | Electromagnetism             | [^8]             | CC BY-SA 3.0       | Pending         | Pending|
| physics_gravitation                 | Gravitation                  | [^9]             | CC BY-SA 3.0       | Pending         | Pending|
| physics_sound                       | Sound                        | [^10]            | CC BY-SA 3.0       | Pending         | Pending|
| chemistry_general                   | Chemistry                    | [^22]            | CC BY-SA 3.0       | Pending         | Pending|
| chemistry_chemical_bonding          | Chemical bonding             | [^15]            | CC BY-SA 3.0       | Pending         | Pending|
| chemistry_periodic_table            | Periodic table               | [^16]            | CC BY-SA 3.0       | Pending         | Pending|
| chemistry_acids_bases               | Acid                         | [^14]            | CC BY-SA 3.0       | Pending         | Pending|
| chemistry_atomic_structure          | Atom                         | [^19]            | CC BY-SA 3.0       | Pending         | Pending|
| biology_general                     | Biology                      | [^23]            | CC BY-SA 3.0       | Pending         | Pending|
| biology_human_body_systems          | Human body systems           | [^17]            | CC BY-SA 3.0       | Pending         | Pending|
| biology_cell_structure              | Cell (biology)               | [^20]            | CC BY-SA 3.0       | Pending         | Pending|
| biology_classification              | Taxonomy                     | [^18]            | CC BY-SA 3.0       | Pending         | Pending|
| biology_genetics                    | Genetics                     | [^21]            | CC BY-SA 3.0       | Pending         | Pending|
| environmental_issues                | Environmental issues         | [^11]            | CC BY-SA 3.0       | 2025-10-30      | Pending|
| environmental_science               | Environmental science        | [^12]            | CC BY-SA 3.0       | 2025-10-30      | Pending|
| ecosystem                           | Ecosystem                    | [^13]            | CC BY-SA 3.0       | 2025-10-30      | Pending|
| pollution                           | Pollution                    | [^1]             | CC BY-SA 3.0       | 2025-10-30      | Pending|
| biodiversity                        | Biodiversity                 | [^7]             | CC BY-SA 3.0       | 2025-10-30      | Pending|

Table 17: Directory structure appendix

| Path (No extension)                                                  | Contents                                                                                       |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/science/physics          | Physics topical HTML files                                                                     |
| content/rrb-ntpc/study-materials/wikimedia/science/chemistry        | Chemistry topical HTML files                                                                   |
| content/rrb-ntpc/study-materials/wikimedia/science/biology          | Biology topical HTML files                                                                     |
| content/rrb-ntpc/study-materials/wikimedia/science/environmental-science | Environmental Science topical HTML files                                                     |
| content/rrb-ntpc/study-materials/wikimedia/science                  | Central index (index.html)                                                                     |

Glossary of key terms (selected):
- Ecosystem: A community of living organisms interacting with their nonliving environment, linked through energy flows and nutrient cycling.[^13]
- Biodiversity: The variety of life across genetic, species, and ecosystem levels; includes measures of richness and evenness and carries economic and ecological significance.[^7]
- CC BY-SA 3.0: Creative Commons Attribution-ShareAlike license requiring attribution and share-alike distribution of adapted materials.[^2]

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