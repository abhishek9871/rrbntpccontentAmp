# RRB NTPC General Science from Wikimedia: Evidence-Backed Compendium and Gap-Closure Plan

## Executive Summary and Context

This report documents the creation of an exam-aligned General Science compendium for Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) candidates, built from authoritative Wikimedia sources across Physics, Chemistry, Biology, and Environmental Science. The corpus comprises twenty topical HTML files and a navigable index. Each file incorporates a visible attribution block consistent with the Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) license, and the environmental science set (five files) has been completed using assisted extraction to close a rate-limit gap, with revision IDs now captured for traceability.[^2]

Coverage spans the syllabus essentials: Physics (motion, energy, gravitation, sound, electricity/magnetism), Chemistry (atomic structure, periodic classification, chemical bonding, acids/bases), Biology (human body systems, classification, cytology, genetics), and Environmental Science (environmental issues, environmental science, ecosystem, pollution, biodiversity). A central index at the root of the science directory supports efficient navigation and cross-topic study.[^1]

Two critical gaps remain before delivery-grade quality:
- Image and media preservation: While images/diagrams are present on the source pages and a local images directory has been created, bulk download was impeded by rate limiting (HTTP 429), and images have not yet been archived locally or mapped into the HTML. This limits offline completeness and learner experience.
- Revision IDs and dump dates: Revision IDs are now logged for the environmental science files; however, revision logging for Physics, Chemistry, and Biology has only started and must be completed. Dump dates remain to be captured from official Wikimedia dumps.[^3][^4]

Deliverables produced include:
- 20 topical HTML files (5 per subject), each with embedded CC BY-SA 3.0 attribution and extraction date (environmental science set).
- A navigable index at the subject root.
- Revision logs (environmental science complete; Physics started; Chemistry/Biology pending).
- A local images directory (images/environmental-science created; image archiving pending due to rate limiting).

The remainder of this report details coverage alignment, methodology, licensing, environmental science synthesis, image and revision gaps, and a practical gap-closure plan.

## Coverage Alignment with RRB NTPC General Science

The assembled corpus aligns with RRB NTPC General Science expectations by mapping each subject’s core themes to dedicated topical files derived from Wikipedia. The structure supports efficient study, with each topic distilled into a self-contained file and reinforced by exam-relevant facts, tables, and references.

Table 1 presents a coverage matrix that connects syllabus topics to sources, local files, coverage status, and notes. The matrix is designed to serve as both an audit trail and a study plan.

Table 1: Coverage matrix (syllabus topic → source → local file → status → notes)

| Syllabus Topic Area                    | Source Wikipedia Entry (See Reference)      | Local File (No extension)                   | Status    | Notes                                                                                   |
|----------------------------------------|---------------------------------------------|---------------------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Physics – Motion and Energy            | Physics; Energy[^5][^6]                     | physics_general; physics_energy             | Complete  | Foundational concepts; conservation and transfer emphasized                             |
| Physics – Gravitation                  | Gravitation[^9]                              | physics_gravitation                         | Complete  | Newtonian gravitation and applications                                                  |
| Physics – Sound and Light              | Sound[^10]                                   | physics_sound                               | Complete  | Wave mechanics and acoustic properties                                                  |
| Physics – Electricity and Magnetism    | Electromagnetism[^8]                         | physics_electromagnetism                    | Complete  | Field concepts and electromagnetic phenomena                                            |
| Chemistry – Atomic Structure           | Atom[^19]                                    | chemistry_atomic_structure                  | Complete  | Atomic theory, subatomic particles                                                      |
| Chemistry – Periodic Classification    | Periodic table[^16]                          | chemistry_periodic_table                    | Complete  | Periodic law and trends                                                                 |
| Chemistry – Chemical Bonding           | Chemical bond[^15]                           | chemistry_chemical_bonding                  | Complete  | Ionic, covalent, metallic bonding                                                       |
| Chemistry – Acids, Bases, and Salts    | Acid[^14]                                    | chemistry_acids_bases                       | Complete  | pH scale and neutralization                                                             |
| Biology – Human Body Systems           | Human body[^17]                              | biology_human_body_systems                  | Complete  | Circulatory, respiratory, digestive, nervous systems                                   |
| Biology – Classification               | Taxonomy (biology)[^18]                      | biology_classification                      | Complete  | Five-kingdom scheme and taxonomic ranks                                                 |
| Biology – Cytology                     | Cell (biology)[^20]                          | biology_cell_structure                      | Complete  | Prokaryotic vs eukaryotic; organelles                                                   |
| Biology – Genetics                     | Genetics[^21]                                | biology_genetics                            | Complete  | DNA, chromosomes, Mendelian inheritance                                                 |
| Env. Science – Environmental Issues    | Environmental issues[^11]                    | environmental_issues                        | Complete  | Triple planetary crises; drivers and impacts                                            |
| Env. Science – Environmental Science   | Environmental science[^12]                   | environmental_science                       | Complete  | Interdisciplinary components; history; modern tools                                     |
| Env. Science – Ecosystem               | Ecosystem[^13]                               | ecosystem                                   | Complete  | Energy flow, food webs, nutrient cycling, succession                                    |
| Env. Science – Pollution               | Pollution[^1]                                | pollution                                   | Complete  | Types, sources, health/ecosystem effects, controls                                      |
| Env. Science – Biodiversity            | Biodiversity[^7]                             | biodiversity                                | Complete  | Levels, importance, threats, conservation; extracted via assisted workflow              |

The matrix confirms comprehensive topic alignment and notes dependencies (e.g., biodiversity extraction). It also highlights that the corpus covers conceptual “what,” operational “how,” and strategic “so what,” enabling RRB NTPC candidates to move from definitions to mechanisms to implications.

## Methodology and Workflow

The compilation followed a seven-phase plan to ensure traceability, licensing compliance, and study readiness.

- Phase 1: Identified authoritative Wikipedia sources mapped to syllabus topics and confirmed licensing terms (CC BY-SA 3.0).[^2]
- Phases 2–4: Extracted, saved, and attributed content in Physics, Chemistry, and Biology. Each topical file includes embedded attribution and a consistent directory location.
- Phase 5: Completed Environmental Science content using a combination of standard and assisted extraction. Biodiversity required an alternative workflow due to rate limiting (HTTP 429); successful coverage now closes the subject set.[^7]
- Phase 6: Processed HTML files for formatting fidelity, embedded attribution, added a navigable index, and began revision logging (environmental science complete; others pending).
- Phase 7: Quality assurance is queued to verify image preservation, attribution合规, directory structure, and comprehensive documentation.

The approach prioritizes clarity, correctness, and reproducibility. Rate-limiting events were mitigated by adapting workflows (e.g., assisted extraction for biodiversity), but bulk media capture remains constrained and requires a different technical plan.

Table 2 summarizes phase status and outputs.

Table 2: Phase-wise status and outputs

| Phase | Objective                                   | Key Tasks                                              | Status            | Outputs                                                                              |
|-------|---------------------------------------------|--------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------|
| 1     | Initial research and source identification  | Map syllabus to Wikipedia pages                        | Complete          | Source list and mapping                                                              |
| 2     | Physics curation                            | Extract, save, attribute                               | Complete          | 5 physics HTML files                                                                 |
| 3     | Chemistry curation                          | Extract, save, attribute                               | Complete          | 5 chemistry HTML files                                                               |
| 4     | Biology curation                            | Extract, save, attribute                               | Complete          | 5 biology HTML files                                                                 |
| 5     | Environmental Science curation              | Extract, save, attribute; assisted biodiversity        | Complete          | 5 environmental-science HTML files; alternative workflow for biodiversity[^7]       |
| 6     | Processing and documentation                | HTML fidelity; attribution; index; rev logs            | In progress       | Index; attribution templates; environmental-science rev log                          |
| 7     | Quality assurance                           | Verify images; attribution合规; structure; coverage     | Pending           | QA checklist and reports                                                             |

## Environmental Science Deep Dive (Evidence Synthesis)

The environmental science module synthesizes issues, field components, ecosystem processes, pollution, and biodiversity. Together, these topics reflect the “triple planetary crises” framed by the United Nations—climate change, pollution, and biodiversity loss—and connect them to measurable human and ecological outcomes.[^11][^12][^1][^7]

### Environmental Issues: Drivers and Impacts

Environmental issues are disruptions in ecosystem function caused by human activities or natural events. When the ecosystem cannot recover, such disruptions are considered serious. The UN frames the current moment as defined by three interlinked crises: climate change, pollution, and biodiversity loss.[^11] Key drivers include population growth (roughly 80 million per year), overconsumption, overexploitation, pollution, and deforestation. Consequences include global warming, environmental degradation (e.g., ocean acidification), mass extinction risks, biodiversity loss, and ecological crises.[^11]

Pollution is a central issue, with major forms including air, water, soil, noise, plastic, radioactive, thermal, light, and visual pollution. Pollution killed approximately nine million people worldwide in 2019 (about one in six deaths), with air pollution responsible for roughly three-quarters of those deaths.[^11][^1] Table 3 catalogues major pollution types, typical contaminants, health effects, and ecological impacts.

Table 3: Pollution types, contaminants, health effects, ecological impacts

| Type                | Typical Contaminants (Examples)                                        | Health Effects (Examples)                                        | Ecological Impacts (Examples)                                     |
|---------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| Air                 | CO, SO₂, NOx, CFCs, PM₂.₅/PM₁₀, photochemical ozone, smog              | Respiratory/cardiovascular disease; throat inflammation; chest pain | Reduced photosynthesis; global warming; ecosystem alteration       |
| Water               | Industrial wastewater, untreated sewage, chlorine, fertilizers, pesticides, oil spills | Waterborne illnesses (e.g., diarrhoea)                            | Water deoxygenation (hypoxia); biodiversity reduction              |
| Soil                | Hydrocarbons, heavy metals (chromium, cadmium, lead), MTBE, herbicides, chlorinated hydrocarbons, dioxins | Neurological problems (via ingestion/exposure)                    | Soil infertility; disrupted food webs                              |
| Radioactive         | Alpha emitters; actinides                                               | Cancer; birth defects                                              | Long-term ecosystem contamination                                  |
| Noise               | Roadway, aircraft, industrial noise, high-intensity sonar              | Hearing loss; high blood pressure; stress; sleep disturbance      | Behavioral changes in wildlife; ecosystem disruption               |
| Plastic             | Macroplastics and microplastics                                         | Indirect impacts via food chain exposure                          | Entanglement; ingestion; garbage patches (e.g., Great Pacific)     |
| Thermal             | Temperature elevation in water bodies (e.g., power plant coolants)      | Not typically direct human health                                 | Altered aquatic habitats; reduced dissolved oxygen                  |
| Light               | Light trespass, over-illumination, astronomical interference           | Sleep disruption                                                   | Disrupted nocturnal behaviors; migration/breeding impacts          |
| Visual              | Overhead lines, billboards, scarred landforms, open trash storage      | Psychological/quality-of-life impacts                             | Scenic degradation; habitat fragmentation                          |

Policy and public awareness have been shaped by pivotal moments such as the publication of Rachel Carson’s “Silent Spring” and the formation of the United Nations Environment Programme (UNEP). Contemporary frameworks include the National Environmental Policy Act (NEPA), the Montreal Protocol, and the Paris Agreement, collectively addressing pollution, ozone depletion, and climate change.[^12]

### Environmental Science: Interdisciplinary Field and History

Environmental science is an interdisciplinary field integrating physics, biology, chemistry, geography, and engineering to study and solve environmental problems. Its modern shape emerged in the 1960s and 1970s, catalyzed by visible environmental disasters and growing scientific awareness. Key components include atmospheric sciences, ecology, environmental chemistry, geosciences, hydrology, and oceanography. Modern practice relies on geographic information systems (GIS), remote sensing, and artificial intelligence for monitoring and modeling environmental systems.[^12]

The historical timeline in Table 4 contextualizes key milestones and events that defined the field’s development, linking them to policy outcomes and technological adoption.

Table 4: Timeline of environmental science milestones (selected)

| Period/Year | Event/Milestone                                  | Impact/Outcome                                               |
|-------------|---------------------------------------------------|--------------------------------------------------------------|
| 1962        | “Silent Spring” (Rachel Carson)                   | Led to bans on harmful chemicals (e.g., DDT); raised awareness[^12] |
| 1970        | First Earth Day; formation of US EPA              | Institutionalized environmental protection                   |
| 1972        | UN Environment Programme established              | Global environmental governance                              |
| 1987        | Montreal Protocol                                 | Global phase-out of ozone-depleting substances               |
| 1997        | Kyoto Protocol                                    | International collaboration on greenhouse gases              |
| 2016        | Paris Agreement                                   | Global climate commitments; emission reduction goals         |
| 21st century| Adoption of GIS, remote sensing, AI               | Enhanced monitoring, modeling, and management capabilities   |

These milestones underscore how scientific discovery, public policy, and technology co-evolve to address environmental challenges.

### Ecosystem: Components, Energy Flow, and Services

An ecosystem is a community of living organisms interacting with their nonliving environment, linked through energy flows and nutrient cycles. Energy enters primarily via photosynthesis (primary production) and moves through trophic levels via food chains and food webs. Decomposition recycles nutrients, and biogeochemical cycles (e.g., nitrogen, phosphorus) sustain productivity. Ecosystems undergo succession after disturbances, with primary succession occurring on newly exposed surfaces and secondary succession occurring where soil remains.[^13]

Nutrients are commonly categorized as macronutrients (primary: nitrogen, phosphorus, potassium; secondary: calcium, magnesium, sulfur), micronutrients (e.g., boron, copper, iron, manganese, molybdenum, zinc), and beneficial nutrients (e.g., aluminum, cobalt, iodine, nickel, selenium, silicon, sodium, vanadium). These classifications help diagnose limitations and guide management. Table 5 summarizes nutrient classes and typical roles.

Table 5: Nutrient classes and typical ecological roles

| Class          | Examples                                           | Typical Roles/Limitations                                                      |
|----------------|----------------------------------------------------|--------------------------------------------------------------------------------|
| Macronutrients (Primary) | N, P, K                              | Frequently limiting; essential for growth and development                      |
| Macronutrients (Secondary) | Ca, Mg, S                         | Important for plant structure, enzyme function, and metabolic processes         |
| Micronutrients        | B, Cl, Cu, Fe, Mn, Mo, Zn        | Required in trace amounts; critical for enzyme catalysis and physiological regulation |
| Beneficial            | Al, Co, I, Ni, Se, Si, Na, V      | Beneficial under specific conditions or for certain species                     |

Ecosystem services—the benefits people obtain from ecosystems—include provisioning (food, water, fuel, medicinal plants), regulating (climate regulation, water purification, pollination), cultural (aesthetic, spiritual, recreational), and supporting (nutrient cycling, primary production) services. Table 6 provides examples.

Table 6: Ecosystem services categories and examples

| Category      | Examples                                                                |
|---------------|-------------------------------------------------------------------------|
| Provisioning  | Food (crops, fish), fresh water, fuel, fiber, medicinal plants          |
| Regulating    | Climate regulation, water purification, flood control, pollination      |
| Cultural      | Aesthetic value, spiritual significance, recreation, education          |
| Supporting    | Nutrient cycling, primary production, soil formation                    |

Anthropogenic nitrogen fluxes account for a large share of ecosystem nitrogen inputs (from fertilizer and fossil fuel combustion), reflecting human influence on biogeochemical cycles and ecosystem functioning.[^13]

### Pollution: Types, Sources, Effects, and Controls

Pollution—the introduction of contaminants into the natural environment—has diverse forms and sources. Natural sources include volcanoes and wildfires; human sources range from point sources (e.g., factories, refineries) to nonpoint sources (e.g., agricultural runoff). Health impacts include respiratory and cardiovascular disease from ozone and particulate matter, waterborne illnesses from contaminated water, neurological impacts from heavy metals (e.g., mercury and lead), and systemic stress from noise. Ecological effects include biomagnification, ocean acidification, global warming, reduced photosynthesis, soil infertility, acid rain, water deoxygenation, and plastic accumulation.[^1]

Control approaches combine practices (recycling, reuse, waste minimization, pollution prevention) and technologies (e.g., scrubbers, electrostatic precipitators, activated sludge, constructed wetlands, bioremediation). Table 7 summarizes major control technologies by domain.

Table 7: Pollution control technologies by domain

| Domain               | Technologies (Examples)                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------|
| Air                  | Scrubbers (baffle spray, cyclonic spray, ejector venturi), thermal oxidizers, baghouses, cyclones, electrostatic precipitators |
| Water/Wastewater     | Sedimentation, activated sludge, aerated lagoons, constructed wetlands, API oil-water separators, biofilters, dissolved air flotation, ultrafiltration |
| Soil/Other           | Bioremediation, vapor recovery systems, phytoremediation                                                |

Global burden estimates underline the scale: pollution caused approximately nine million deaths in 2019, with air pollution responsible for about three-quarters; water pollution contributed roughly 1.4 million deaths. Pollution from anthropogenic chemical pollution has been assessed to exceed planetary boundaries, threatening entire ecosystems.[^1]

### Biodiversity: Levels, Importance, Threats, Conservation

Biodiversity encompasses variability at genetic, species, ecosystem, and phylogenetic levels. It is fundamental to ecosystem resilience and stability and underpins provisioning, regulating, and cultural services. Biodiversity supports agricultural productivity, nutrition security, disease prevention, and mental well-being. Economically, estimates place the annual value of biodiversity services around $150 trillion, with losses projected to cost roughly $5 trillion annually.[^7]

The current crisis is often described as a sixth mass extinction, driven primarily by habitat destruction, climate change, overexploitation, pollution, and invasive species. Recent assessments highlight significant wildlife population declines, with roughly 73% average decline since 1970 reported in the Living Planet Report 2024, and a substantial share of assessed species threatened with extinction per the IUCN Red List. Biodiversity remains unevenly distributed, with a pronounced latitudinal gradient and concentrations in forested regions.[^7]

Conservation strategies span protected areas (e.g., national parks, wildlife sanctuaries, marine protected areas), restoration techniques (gene banks, wildlife corridors, invasive species removal), and international frameworks (Convention on Biological Diversity, CITES, Ramsar, Bonn, Cartagena, and the UN High Seas Treaty). The “30 by 30” initiative seeks to protect 30% of land and oceans by 2030. Table 8 summarizes the conservation landscape and coverage targets.

Table 8: Protected area types and global coverage targets

| Type/Target            | Examples/Goals                                                           |
|------------------------|---------------------------------------------------------------------------|
| Protected Area Types   | National parks (IUCN Category II), wildlife sanctuaries, forest protected areas, marine protected areas |
| Global Target          | 30 by 30 initiative (protect 30% of land and oceans by 2030)             |
| Benefits               | Genetic resource conservation, medicinal plant protection, water security, tourism, disaster risk reduction |

A concise summary of species estimates and extinction metrics appears in Table 9.

Table 9: Species estimates, documented species, extinction metrics (selected)

| Metric                                  | Estimate/Value                                      |
|-----------------------------------------|------------------------------------------------------|
| Estimated terrestrial species            | ~8.7 million                                        |
| Estimated oceanic species                | ~2.2 million                                        |
| Documented species                       | ~1.2 million (~86% undescribed)                     |
| Extinction rate                          | 100–10,000× faster than background rates            |
| Threatened species (assessed)            | ~40% (IUCN Red List)                                |

Taken together, the environmental science module explains what the issues are (definitions and typologies), how they operate (ecosystem processes, pollution mechanisms), and why they matter (human health, ecological integrity, economic value), equipping candidates with both factual knowledge and integrative reasoning.

## Licensing, Attribution, and Reproducibility

Attribution is embedded within each topical HTML file, referencing the source Wikipedia page and the CC BY-SA 3.0 license. Extraction dates are recorded for environmental science content (2025-10-30), and revision IDs are now documented for all five environmental science files.[^2] For reproducible snapshots, revision IDs and dump dates must be captured for all other sources via Wikimedia dumps and associated guidance.[^3][^4]

Table 10 summarizes attribution compliance by subject and the status of revision documentation.

Table 10: Attribution and revision status by subject

| Subject            | Files (No.) | Attribution Present | License Linkage Verified | Extraction Date Recorded | Revision ID Logged |
|--------------------|-------------|---------------------|--------------------------|--------------------------|--------------------|
| Physics            | 5           | Yes                 | Yes                      | Pending                  | Started            |
| Chemistry          | 5           | Yes                 | Yes                      | Pending                  | Pending            |
| Biology            | 5           | Yes                 | Yes                      | Pending                  | Pending            |
| Environmental Sci. | 5           | Yes                 | Yes                      | Yes (2025-10-30)         | Complete           |

This design ensures legal compliance and supports future audit and content refresh cycles.

## Inventory and Directory Structure

The corpus is organized under a common directory schema per subject (physics, chemistry, biology, environmental-science), with a central index at the subject root. An images directory has been created and includes a placeholder set for environmental science. Image archiving remains pending due to rate limiting.

Table 11 summarizes file inventories by subject.

Table 11: File inventory by subject

| Subject            | Local File Names (No extension)                                                                                         | Attribution Present | Rev ID Status  | Images Present |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------|----------------|----------------|
| Physics            | physics_general; physics_energy; physics_electromagnetism; physics_gravitation; physics_sound                            | Yes                 | Started        | Not yet        |
| Chemistry          | chemistry_general; chemistry_chemical_bonding; chemistry_periodic_table; chemistry_acids_bases; chemistry_atomic_structure | Yes                 | Pending        | Not yet        |
| Biology            | biology_general; biology_human_body_systems; biology_cell_structure; biology_classification; biology_genetics             | Yes                 | Pending        | Not yet        |
| Environmental Sci. | environmental_issues; environmental_science; ecosystem; pollution; biodiversity                                           | Yes                 | Complete       | Not yet        |
| Index              | index                                                                                                                      | N/A                 | N/A            | N/A            |

Table 12 provides a directory structure overview and the purpose of each path.

Table 12: Directory structure overview

| Path (No extension)                                                 | Contents                                           |
|----------------------------------------------------------------------|----------------------------------------------------|
| content/rrb-ntpc/study-materials/wikimedia/science/physics          | Physics HTML files                                 |
| content/rrb-ntpc/study-materials/wikimedia/science/chemistry        | Chemistry HTML files                               |
| content/rrb-ntpc/study-materials/wikimedia/science/biology          | Biology HTML files                                 |
| content/rrb-ntpc/study-materials/wikimedia/science/environmental-science | Environmental Science HTML files               |
| content/rrb-ntpc/study-materials/wikimedia/science                  | Central index                                      |
| content/.../science/images                                           | Local images directory                             |
| content/.../science/images/environmental-science                    | Environmental science image assets (placeholder)   |

## Quality Assurance and Gap-Closure Plan

Open items are concentrated in media preservation and complete revision capture:
- Images/diagrams: Rate limiting prevented bulk downloads. To close this gap, batch downloads should be orchestrated with conservative request pacing, off-peak scheduling, and adherence to Wikimedia’s guidance for database access and media retrieval.[^3]
- Revision IDs and dump dates: Environmental science revision IDs are captured; Physics, Chemistry, and Biology require completion. Dump dates should be recorded per source using official Wikimedia dumps.[^4]
- QA checklist: Final verification of image presence and local referencing, attribution合规, directory structure, and topic coverage completeness.

Table 13 outlines open issues, actions, ownership, and status.

Table 13: Open issues tracker

| Issue                                     | Action                                               | Owner        | Target Date | Status   |
|-------------------------------------------|------------------------------------------------------|--------------|-------------|----------|
| Bulk image download (rate limiting)       | Schedule batch downloads with pacing; use stable URLs | Content team | TBD         | Pending  |
| Local image-to-HTML referencing           | Map images to topics; update img src paths            | Content team | TBD         | Pending  |
| Rev IDs for Physics, Chemistry, Biology   | Capture via API/dumps; append to revision logs        | Content team | TBD         | Pending  |
| Dump dates capture                        | Record dump timestamps per source                     | Content team | TBD         | Pending  |
| QA finalization                           | Execute checklist; verify coverage and attribution    | QA lead      | TBD         | Pending  |

This plan ensures that once media and revisions are captured, the compendium can be validated as delivery-grade.

## Appendices

### Appendix A: Source-to-File Crosswalk

Table A1 maps each local file to its source Wikipedia entry, extraction date, revision ID (where available), and notes.

Table A1: Source-to-File crosswalk

| Local File (No extension)           | Source Title               | Source Reference | Extraction Date | Rev ID       | Notes                                   |
|-------------------------------------|----------------------------|------------------|-----------------|--------------|------------------------------------------|
| physics_general                     | Physics                    | [^5]             | Pending         | Pending      | Foundational physics overview            |
| physics_energy                      | Energy                     | [^6]             | Pending         | Pending      | Conservation and transfer                |
| physics_electromagnetism            | Electromagnetism           | [^8]             | Pending         | Pending      | Field concepts                           |
| physics_gravitation                 | Gravitation                | [^9]             | Pending         | Pending      | Newtonian gravitation                    |
| physics_sound                       | Sound                      | [^10]            | Pending         | Pending      | Wave mechanics                           |
| chemistry_general                   | Chemistry                  | [^22]            | Pending         | Pending      | General chemistry                        |
| chemistry_chemical_bonding          | Chemical bond              | [^15]            | Pending         | Pending      | Bonding types                            |
| chemistry_periodic_table            | Periodic table             | [^16]            | Pending         | Pending      | Periodic law and trends                  |
| chemistry_acids_bases               | Acid                       | [^14]            | Pending         | Pending      | pH and neutralization                    |
| chemistry_atomic_structure          | Atom                       | [^19]            | Pending         | Pending      | Atomic theory and subatomic particles    |
| biology_general                     | Biology                    | [^23]            | Pending         | Pending      | General biology                          |
| biology_human_body_systems          | Human body                 | [^17]            | Pending         | Pending      | Systems overview                         |
| biology_cell_structure              | Cell (biology)             | [^20]            | Pending         | Pending      | Cytology                                 |
| biology_classification              | Taxonomy (biology)         | [^18]            | Pending         | Pending      | Classification                           |
| biology_genetics                    | Genetics                   | [^21]            | Pending         | Pending      | DNA, chromosomes, inheritance            |
| environmental_issues                | Environmental issues       | [^11]            | 2025-10-30      | 1310975708   | Triple planetary crises; drivers         |
| environmental_science               | Environmental science      | [^12]            | 2025-10-30      | 1314325017   | Interdisciplinary field; history         |
| ecosystem                           | Ecosystem                  | [^13]            | 2025-10-30      | 1313967029   | Components; energy flow; services        |
| pollution                           | Pollution                  | [^1]             | 2025-10-30      | 1317950916   | Types; sources; controls; statistics     |
| biodiversity                        | Biodiversity               | [^7]             | 2025-10-30      | 1317660757   | Levels; importance; threats; conservation |

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