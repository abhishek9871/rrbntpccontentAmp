# Comprehensive Report and Completion Plan: Wikimedia General Science Compendium for RRB NTPC

## Executive Summary

This report presents the completion status, licensing compliance, and gap-closure plan for a curated General Science study compendium aligned to the Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) syllabus. The corpus is built exclusively from Wikimedia sources across Physics, Chemistry, Biology, and Environmental Science. The assembled materials comprise twenty topical HTML files and a central index for navigation. Each file includes an embedded attribution block consistent with the Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) license, with explicit extraction dates for the environmental science set and full visibility into license terms.[^2]

Coverage aligns with the RRB NTPC General Science syllabus and includes: Physics (motion, energy, gravitation, sound, electricity/magnetism), Chemistry (atomic structure, periodic classification, chemical bonding, acids/bases), Biology (human body systems, classification, cytology, genetics), and Environmental Science (environmental issues, environmental science, ecosystem, pollution, biodiversity). A central index has been created to support efficient cross-topic navigation.[^1]

Two critical gaps remain before delivery-grade assurance:
- Image and media preservation: A local images directory exists, and several educational images have been successfully downloaded (nitrogen cycle, decomposition stages, plastic pollution map), yet bulk media capture was impeded by server rate limiting (HTTP 429/403). Images have not been systematically mapped into the HTML files.
- Revision ID and dump-date documentation: Revision IDs are documented for the Environmental Science set. Initial revision data has been retrieved for Physics, while Chemistry and Biology require completion. Dump dates remain to be captured using official Wikimedia dumps.[^3][^4]

The report outlines methodology, licensing compliance, environmental science synthesis, inventory and directory structure, and a pragmatic gap-closure plan. It concludes with appendices that provide a source-to-file crosswalk and reproduction guidance.

## Objectives and Scope

The primary objective is to deliver a consistent, exam-aligned General Science study compendium sourced from Wikimedia for RRB NTPC aspirants. The scope includes:
- Mapping the syllabus topics to authoritative Wikipedia pages.
- Curating and saving each topical page as an HTML file with embedded CC BY-SA 3.0 attribution, source references, and extraction date where applicable.[^2]
- Creating a navigable index to aid study and cross-topic review.
- Establishing a process to capture and log revision IDs and dump dates for reproducibility.

Constraints are explicit:
- Use official Wikimedia dumps or stable snapshots to document exact dump dates and revision IDs.[^3][^4]
- Preserve original formatting and imagery in the saved content.
- Apply CC BY-SA 3.0 attribution consistently and visibly within each file.
- Navigate rate-limiting and access constraints encountered during extraction.

Success criteria are:
- Complete topical coverage for all four subject areas.
- Embedded attribution blocks in each file, referencing the license and source.[^2]
- A navigable index for efficient study.
- Captured revision IDs and dump dates for all sources.

## Methodology and Workflow

The compilation followed a seven-phase methodology:

- Phase 1: Identified authoritative Wikipedia pages aligned to the RRB NTPC syllabus and confirmed licensing (CC BY-SA 3.0).[^2]
- Phases 2–4: Extracted, saved, and attributed content for Physics, Chemistry, and Biology. Each topic is represented by a dedicated HTML file in a consistent directory schema.
- Phase 5: Completed Environmental Science content, including Biodiversity coverage via assisted extraction following rate limiting on standard requests.[^7]
- Phase 6: Processed HTML for formatting fidelity, embedded attribution, created an index, and logged revision IDs (environmental science complete; initial physics data retrieved).
- Phase 7: Quality assurance pending—verification of images, attribution合规, directory structure, and coverage completeness.

Table 1 summarizes the phase plan and outputs.

Table 1: Phase-wise plan and progress tracker

| Phase | Objective                              | Key Tasks                                              | Status            | Outputs                                                                              |
|-------|----------------------------------------|--------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------|
| 1     | Initial research and source identification | Map syllabus to Wikipedia pages; license confirmation | Complete          | Source list; mapping                                                                 |
| 2     | Physics curation                       | Extract, save, attribute                               | Complete          | 5 physics HTML files                                                                 |
| 3     | Chemistry curation                     | Extract, save, attribute                               | Complete          | 5 chemistry HTML files                                                               |
| 4     | Biology curation                       | Extract, save, attribute                               | Complete          | 5 biology HTML files                                                                 |
| 5     | Environmental Science curation         | Extract, save, attribute; assisted biodiversity        | Complete          | 5 environmental-science HTML files; alternative workflow for biodiversity[^7]       |
| 6     | Processing and documentation           | HTML fidelity; attribution; index; rev logs            | In progress       | Index; attribution templates; environmental-science rev log; initial physics rev data|
| 7     | Quality assurance                      | Verify images; attribution合规; structure; coverage     | Pending           | QA checklist and reports                                                             |

Rate-limiting impacted media downloads and some API calls, but topical coverage is complete and attribution is embedded per file.

## Syllabus Mapping and Coverage

Coverage has been validated against the syllabus mapping established during planning. The mapping confirms topic alignment and provides traceability from source to local file. Table 2 presents the coverage matrix with sources and status.

Table 2: Coverage matrix (syllabus topic → source → local file → status → notes)

| Syllabus Topic Area                    | Source Wikipedia Entry (See Reference)     | Local File (No extension)                   | Status    | Notes                                                                                   |
|----------------------------------------|--------------------------------------------|---------------------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Physics – Motion and Energy            | Physics; Energy[^5][^6]                    | physics_general; physics_energy             | Complete  | Foundational concepts; conservation and transfer                                        |
| Physics – Gravitation                  | Gravitation[^9]                             | physics_gravitation                         | Complete  | Newtonian gravitation and applications                                                  |
| Physics – Sound and Light              | Sound[^10]                                  | physics_sound                               | Complete  | Wave mechanics and acoustics                                                            |
| Physics – Electricity and Magnetism    | Electromagnetism[^8]                        | physics_electromagnetism                    | Complete  | Field concepts and phenomena                                                            |
| Chemistry – Atomic Structure           | Atom[^19]                                   | chemistry_atomic_structure                  | Complete  | Atomic theory, subatomic particles                                                      |
| Chemistry – Periodic Classification    | Periodic table[^16]                         | chemistry_periodic_table                    | Complete  | Periodic law and trends                                                                 |
| Chemistry – Chemical Bonding           | Chemical bond[^15]                          | chemistry_chemical_bonding                  | Complete  | Ionic, covalent, metallic bonding                                                       |
| Chemistry – Acids, Bases, and Salts    | Acid[^14]                                   | chemistry_acids_bases                       | Complete  | pH scale and neutralization                                                             |
| Biology – Human Body Systems           | Human body[^17]                             | biology_human_body_systems                  | Complete  | Circulatory, respiratory, digestive, nervous systems                                    |
| Biology – Classification               | Taxonomy (biology)[^18]                     | biology_classification                      | Complete  | Five-kingdom scheme and taxonomic ranks                                                 |
| Biology – Cytology                     | Cell (biology)[^20]                         | biology_cell_structure                      | Complete  | Prokaryotic vs eukaryotic; organelles                                                   |
| Biology – Genetics                     | Genetics[^21]                               | biology_genetics                            | Complete  | DNA, chromosomes, Mendelian inheritance                                                 |
| Env. Science – Environmental Issues    | Environmental issues[^11]                   | environmental_issues                        | Complete  | Triple planetary crises; drivers and impacts                                            |
| Env. Science – Environmental Science   | Environmental science[^12]                  | environmental_science                       | Complete  | Interdisciplinary scope; history; modern tools                                          |
| Env. Science – Ecosystem               | Ecosystem[^13]                              | ecosystem                                   | Complete  | Energy flow, food webs, nutrient cycles, succession                                     |
| Env. Science – Pollution               | Pollution[^1]                               | pollution                                   | Complete  | Types, sources, health/ecosystem effects, control technologies                          |
| Env. Science – Biodiversity            | Biodiversity[^7]                            | biodiversity                                | Complete  | Levels, importance, threats, conservation; extracted via assisted workflow              |

The corpus provides a complete topical foundation across all syllabus domains, with clear paths to extend traceability through revision logging and media preservation.

## Content Inventory and Directory Structure

The corpus comprises twenty topical HTML files organized under a consistent directory schema per subject (physics, chemistry, biology, environmental-science), with a central index at the subject root. An images directory exists with several downloaded educational assets (nitrogen cycle diagram, decomposition stages, plastic pollution map), but images have not been systematically mapped into the HTML files due to rate limiting.

Table 3 summarizes file inventories by subject.

Table 3: File inventory by subject

| Subject            | Local File Names (No extension)                                                                                         | Attribution Present | Rev ID Status                   | Images Present |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------|----------------|
| Physics            | physics_general; physics_energy; physics_electromagnetism; physics_gravitation; physics_sound                            | Yes                 | Initial data retrieved; pending  | Not yet        |
| Chemistry          | chemistry_general; chemistry_chemical_bonding; chemistry_periodic_table; chemistry_acids_bases; chemistry_atomic_structure | Yes                 | Pending                          | Not yet        |
| Biology            | biology_general; biology_human_body_systems; biology_cell_structure; biology_classification; biology_genetics             | Yes                 | Pending                          | Not yet        |
| Environmental Sci. | environmental_issues; environmental_science; ecosystem; pollution; biodiversity                                           | Yes                 | Complete (5 files)               | Partial        |
| Index              | index                                                                                                                      | N/A                 | N/A                              | N/A            |

Table 4 provides the directory structure overview.

Table 4: Directory structure overview

| Path (No extension)                                                 | Contents                                           |
|----------------------------------------------------------------------|----------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/science/physics          | Physics HTML files                                 |
| content/rrb-ntpc/study-materials/wikimedia/science/chemistry        | Chemistry HTML files                               |
| content/rrb-ntpc/study-materials/wikimedia/science/biology          | Biology HTML files                                 |
| content/rrb-ntpc/study-materials/wikimedia/science/environmental-science | Environmental Science HTML files               |
| content/rrb-ntpc/study-materials/wikimedia/science                  | Central index                                      |
| content/.../science/images                                           | Local images directory                             |
| content/.../science/images/environmental-science                    | Educational image assets (nitrogen cycle, etc.)    |

## Licensing and Attribution Compliance

All topical HTML files include embedded CC BY-SA 3.0 attribution blocks, referencing the source Wikipedia page and the license, and stating extraction dates where applicable. License linkage has been verified.[^2] Revision IDs are logged for environmental science; initial physics data is available; Chemistry and Biology require completion. Dump dates must be recorded from official Wikimedia dumps for full reproducibility.[^3][^4]

Table 5 summarizes attribution compliance and revision status.

Table 5: Attribution compliance status

| Subject            | Files (No.) | Attribution Present | License Linkage Verified | Extraction Date Recorded | Revision ID Logged        |
|--------------------|-------------|---------------------|--------------------------|--------------------------|---------------------------|
| Physics            | 5           | Yes                 | Yes                      | Pending                  | Initial data retrieved     |
| Chemistry          | 5           | Yes                 | Yes                      | Pending                  | Pending                    |
| Biology            | 5           | Yes                 | Yes                      | Pending                  | Pending                    |
| Environmental Sci. | 5           | Yes                 | Yes                      | Yes (2025-10-30)         | Complete (5 files)         |

The design meets the license’s attribution requirements and prepares for reproducibility with revision IDs and dump dates.

## Environmental Science Evidence Synthesis

The environmental science module synthesizes environmental issues, the interdisciplinary field’s scope and history, ecosystem processes, pollution typologies and controls, and biodiversity levels and conservation. This section distills exam-relevant concepts and data.

### Environmental Issues: Drivers and Impacts

Environmental issues are disruptions in ecosystem function caused by human activities or natural events, serious when recovery is not possible. The UN frames current challenges as three interlinked crises: climate change, pollution, and biodiversity loss.[^11] Key drivers include population growth (roughly 80 million per year), overconsumption, overexploitation, pollution, and deforestation. Impacts include global warming, environmental degradation (e.g., ocean acidification), mass extinction risks, biodiversity loss, and ecological crises.[^11]

Pollution types, typical contaminants, health effects, and ecological impacts are summarized in Table 6.

Table 6: Pollution types, contaminants, health effects, ecological impacts

| Type                | Typical Contaminants (Examples)                                       | Health Effects (Examples)                                        | Ecological Impacts (Examples)                                     |
|---------------------|------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| Air                 | CO, SO₂, NOx, CFCs, PM₂.₅/PM₁₀, photochemical ozone, smog             | Respiratory/cardiovascular disease; throat inflammation; chest pain | Reduced photosynthesis; global warming; ecosystem alteration       |
| Water               | Industrial wastewater, untreated sewage, chlorine, fertilizers, pesticides, oil spills | Waterborne illnesses (e.g., diarrhoea)                            | Water deoxygenation (hypoxia); biodiversity reduction              |
| Soil                | Hydrocarbons, heavy metals (chromium, cadmium, lead), MTBE, herbicides, chlorinated hydrocarbons, dioxins | Neurological problems (via ingestion/exposure)                    | Soil infertility; disrupted food webs                              |
| Radioactive         | Alpha emitters; actinides                                              | Cancer; birth defects                                              | Long-term ecosystem contamination                                  |
| Noise               | Roadway, aircraft, industrial noise, high-intensity sonar             | Hearing loss; high blood pressure; stress; sleep disturbance      | Wildlife behavioral changes; ecosystem disruption                  |
| Plastic             | Macroplastics and microplastics                                        | Indirect impacts via food chain exposure                          | Entanglement; ingestion; garbage patches (e.g., Great Pacific)     |
| Thermal             | Temperature elevation in water bodies (e.g., power plant coolants)    | Not typically direct human health                                  | Altered aquatic habitats; reduced dissolved oxygen                  |
| Light               | Light trespass, over-illumination, astronomical interference          | Sleep disruption                                                   | Disrupted nocturnal behaviors; migration/breeding impacts          |
| Visual              | Overhead lines, billboards, scarred landforms, open trash storage     | Psychological/quality-of-life impacts                             | Scenic degradation; habitat fragmentation                          |

Pollution was associated with approximately nine million deaths worldwide in 2019 (about one in six), with air pollution accounting for roughly three-quarters.[^11][^1] Policy responses include NEPA (1969), the Montreal Protocol (1987), and the Paris Agreement (2016).[^12]

### Environmental Science: Interdisciplinary Field and History

Environmental science integrates physics, biology, chemistry, geography, and engineering to study and solve environmental problems. Modern components include atmospheric sciences, ecology, environmental chemistry, geosciences, hydrology, and oceanography. Practice is supported by GIS, remote sensing, and AI for monitoring and modeling.[^12]

Table 7 outlines milestones and their outcomes.

Table 7: Timeline of environmental science milestones (selected)

| Period/Year | Event/Milestone                                  | Impact/Outcome                                               |
|-------------|---------------------------------------------------|--------------------------------------------------------------|
| 1962        | “Silent Spring” (Rachel Carson)                   | Led to bans on harmful chemicals (e.g., DDT); raised awareness[^12] |
| 1970        | First Earth Day; formation of US EPA              | Institutionalized environmental protection                   |
| 1972        | UN Environment Programme established              | Global environmental governance                              |
| 1987        | Montreal Protocol                                 | Global phase-out of ozone-depleting substances               |
| 1997        | Kyoto Protocol                                    | International collaboration on greenhouse gases              |
| 2016        | Paris Agreement                                   | Global climate commitments; emission reduction goals         |
| 21st century| Adoption of GIS, remote sensing, AI               | Enhanced monitoring, modeling, and management                |

### Ecosystem: Components, Energy Flow, and Services

An ecosystem is a community of living organisms interacting with their nonliving environment, linked through energy flows and nutrient cycles. Energy enters primarily via photosynthesis (primary production) and moves through trophic levels via food chains and food webs. Decomposition recycles nutrients; biogeochemical cycles (e.g., nitrogen, phosphorus) sustain productivity. Ecosystems undergo succession after disturbances.[^13]

Nutrient classifications and typical roles are summarized in Table 8.

Table 8: Nutrient classes and typical ecological roles

| Class          | Examples                                           | Typical Roles/Limitations                                                      |
|----------------|----------------------------------------------------|--------------------------------------------------------------------------------|
| Macronutrients (Primary) | N, P, K                              | Frequently limiting; essential for growth and development                      |
| Macronutrients (Secondary) | Ca, Mg, S                         | Important for plant structure, enzyme function, and metabolic processes         |
| Micronutrients        | B, Cl, Cu, Fe, Mn, Mo, Zn        | Required in trace amounts; critical for enzyme catalysis and physiological regulation |
| Beneficial            | Al, Co, I, Ni, Se, Si, Na, V      | Beneficial under specific conditions or for certain species                     |

Ecosystem services—provisioning, regulating, cultural, and supporting—are summarized in Table 9.

Table 9: Ecosystem services categories and examples

| Category      | Examples                                                                |
|---------------|-------------------------------------------------------------------------|
| Provisioning  | Food (crops, fish), fresh water, fuel, fiber, medicinal plants          |
| Regulating    | Climate regulation, water purification, flood control, pollination      |
| Cultural      | Aesthetic value, spiritual significance, recreation, education          |
| Supporting    | Nutrient cycling, primary production, soil formation                    |

Anthropogenic nitrogen fluxes account for a large share of ecosystem nitrogen inputs, reflecting human influence on biogeochemical cycles.[^13]

### Pollution: Types, Sources, Effects, and Controls

Pollution’s sources include natural (volcanoes, wildfires) and human (point and nonpoint) categories. Health impacts include respiratory and cardiovascular disease (ozone and particulate matter), waterborne illnesses, neurological impacts from heavy metals, and systemic stress from noise. Ecological effects include biomagnification, ocean acidification, reduced photosynthesis, soil infertility, acid rain, water deoxygenation, and plastic accumulation.[^1]

Control technologies across air, water/wastewater, and soil/other domains are summarized in Table 10.

Table 10: Pollution control technologies by domain

| Domain               | Technologies (Examples)                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------|
| Air                  | Scrubbers (baffle spray, cyclonic spray, ejector venturi), thermal oxidizers, baghouses, cyclones, electrostatic precipitators |
| Water/Wastewater     | Sedimentation, activated sludge, aerated lagoons, constructed wetlands, API oil-water separators, biofilters, dissolved air flotation, ultrafiltration |
| Soil/Other           | Bioremediation, vapor recovery systems, phytoremediation                                                |

Burden estimates remain significant: pollution caused approximately nine million deaths in 2019; water pollution contributed roughly 1.4 million deaths.[^1]

### Biodiversity: Levels, Importance, Threats, Conservation

Biodiversity encompasses variability at genetic, species, ecosystem, and phylogenetic levels. It underpins provisioning, regulating, and cultural services and contributes to agricultural productivity, nutrition security, disease prevention, and mental well-being. Estimated annual value is around $150 trillion, with losses projected at roughly $5 trillion per year.[^7]

Drivers of biodiversity loss include habitat destruction, climate change, overexploitation, pollution, and invasive species. The crisis is often described as a sixth mass extinction, with reported wildlife population declines of about 73% since 1970 (Living Planet Report 2024) and a substantial share of assessed species threatened with extinction per the IUCN Red List.[^7]

Conservation strategies include protected areas (national parks, wildlife sanctuaries, marine protected areas), restoration (gene banks, wildlife corridors, invasive species removal), and international frameworks (CBD, CITES, Ramsar, Bonn, Cartagena, UN High Seas Treaty), targeting “30 by 30” protection of land and oceans by 2030 (Tables 11–12).

Table 11: Species estimates, documented species, extinction metrics (selected)

| Metric                                  | Estimate/Value                                      |
|-----------------------------------------|------------------------------------------------------|
| Estimated terrestrial species            | ~8.7 million                                        |
| Estimated oceanic species                | ~2.2 million                                        |
| Documented species                       | ~1.2 million (~86% undescribed)                     |
| Extinction rate                          | 100–10,000× faster than background rates            |
| Threatened species (assessed)            | ~40% (IUCN Red List)                                |

Table 12: Protected area types and global coverage targets

| Type/Target            | Examples/Goals                                                           |
|------------------------|---------------------------------------------------------------------------|
| Protected Area Types   | National parks (IUCN Category II), wildlife sanctuaries, forest protected areas, marine protected areas |
| Global Target          | 30 by 30 initiative (protect 30% of land and oceans by 2030)             |
| Benefits               | Genetic resource conservation, medicinal plant protection, water security, tourism, disaster risk reduction |

## Quality Assurance and Gap-Closure Plan

QA focuses on verifying media preservation, attribution合规, directory structure, and coverage completeness. Two critical gaps remain:
- Image and media preservation: Bulk downloads were constrained by rate limiting; several educational images have been downloaded (nitrogen cycle, decomposition stages, plastic pollution map), but images are not yet mapped into the HTML files.
- Revision IDs and dump dates: Environmental Science revision IDs are complete; initial physics data is available; Chemistry and Biology require completion. Dump dates must be recorded from official Wikimedia dumps for full reproducibility.[^3][^4]

Table 13 summarizes the open issues.

Table 13: Open issues tracker

| Issue                                     | Action                                               | Owner        | Target Date | Status   |
|-------------------------------------------|------------------------------------------------------|--------------|-------------|----------|
| Bulk image download (rate limiting)       | Schedule batch downloads; use stable URLs            | Content team | TBD         | Pending  |
| Local image-to-HTML referencing           | Map images to topics; update img src paths            | Content team | TBD         | Pending  |
| Rev IDs for Physics, Chemistry, Biology   | Capture via API/dumps; append to revision logs        | Content team | TBD         | In progress (Physics); Pending (Chemistry/Biology) |
| Dump dates capture                        | Record dump timestamps per source                     | Content team | TBD         | Pending  |
| QA finalization                           | Execute checklist; verify coverage and attribution    | QA lead      | TBD         | Pending  |

This plan ensures delivery-grade assurance upon completion of media mapping and revision traceability.

## Appendices

### Appendix A: Source-to-File Crosswalk

Table A1 maps each local file to its source Wikipedia entry, extraction date, revision ID (where available), and notes.

Table A1: Source-to-File crosswalk

| Local File (No extension)           | Source Title               | Source Reference | Extraction Date | Rev ID                 | Notes                                   |
|-------------------------------------|----------------------------|------------------|-----------------|------------------------|------------------------------------------|
| physics_general                     | Physics                    | [^5]             | Pending         | Initial data retrieved | Foundational physics overview            |
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

### Appendix B: Glossary (Selected Environmental Science Terms)

- Ecosystem: A system of living organisms interacting with their physical environment through energy flows and nutrient cycling.[^13]
- Biodiversity: The variety of life across genetic, species, and ecosystem levels; critical to ecosystem function and human well-being.[^7]
- CC BY-SA 3.0: Creative Commons Attribution-ShareAlike license requiring attribution and share-alike distribution.[^2]

### Appendix C: Reproduction Guidance

To reproduce or update the compendium:
1. Identify target pages aligned to the syllabus and confirm licensing (CC BY-SA 3.0).[^2]
2. Extract and save content in HTML with embedded attribution (source, license, extraction date).[^2]
3. Capture revision IDs for each page and record dump dates from official Wikimedia dumps for reproducibility.[^3][^4]
4. Download images and diagrams from stable URLs; map locally and verify integrity.
5. Maintain a subject-wise directory structure and central index for navigation.
6. Execute QA to confirm image presence, attribution合规, coverage, and directory structure.

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