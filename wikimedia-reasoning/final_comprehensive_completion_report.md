# RRB NTPC General Science from Wikimedia: Evidence-Backed Compendium, Licensing Compliance, and Gap-Closure Plan

## Executive Summary and Context

This report documents the design, compilation, and licensing合规 of a General Science study compendium tailored to the Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) syllabus. Content has been assembled from Wikimedia projects with a focus on Physics, Chemistry, Biology, and Environmental Science. The corpus comprises twenty topical HTML files—five per subject—organized under a consistent directory schema, with a central index for navigation and embedded CC BY-SA 3.0 attribution in each file.[^2] A dedicated environmental science sub-compendium has been completed, including Biodiversity coverage obtained via assisted extraction following rate-limiting on standard requests.[^7]

Coverage is aligned to syllabus expectations across the four subjects and includes core topics such as energy, electromagnetism, gravitation, sound, atomic structure, periodic classification, chemical bonding, acids and bases, human body systems, taxonomy, cytology, genetics, environmental issues, environmental science, ecosystem processes, pollution, and biodiversity. The environmental science subset synthesizes issues, field components, ecosystem structure and function, pollution typologies and controls, and biodiversity levels, importance, threats, and conservation.

Two critical gaps remain before delivery-grade assurance:
- Image and media preservation: While images are present on source pages and a local images directory has been created, bulk downloads were impeded by rate limiting (HTTP 429). Images have not yet been locally archived or mapped into the HTML, limiting offline completeness.
- Revision IDs and dump-date traceability: Revision IDs are documented for Environmental Science (five files). Physics, Chemistry, and Biology require completion; dump dates remain to be recorded using official Wikimedia dumps.[^3][^4]

The report outlines licensing compliance, evidence synthesis particularly in Environmental Science, current inventory and directory structure, a targeted gap-closure plan, and pragmatic next steps. The central index has been created for navigation, and attribution blocks are embedded per file.[^1]

## Coverage Alignment with RRB NTPC General Science

The assembled corpus aligns to the RRB NTPC General Science syllabus by mapping each subject’s core conceptual domains to dedicated topical files derived from Wikipedia. The structure supports efficient study and revision, with each topic distilled into a self-contained file and reinforced by exam-relevant facts and references.

Table 1 presents the coverage matrix linking syllabus topics to sources and local files, including status and notes. It is intended to serve as both an audit trail and a study plan.

Table 1: Coverage matrix (syllabus topic → source → local file → status → notes)

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

This matrix confirms comprehensive coverage, with the environmental science set now including biodiversity and environmental issues that close key syllabus dependencies.

## Methodology and Workflow

The compendium followed a disciplined seven-phase methodology:

- Phase 1: Source identification and syllabus mapping, including confirmation of licensing (CC BY-SA 3.0).[^2]
- Phases 2–4: Extraction and attribution for Physics, Chemistry, and Biology, with each topic saved to a consistent directory schema.
- Phase 5: Environmental Science content curation, including assisted extraction for Biodiversity after rate limiting impacted standard requests. This closed critical gaps in environmental coverage.[^7]
- Phase 6: HTML processing for fidelity, embedded attribution, index creation, and revision logging (environmental science complete; others pending).
- Phase 7: Quality assurance is queued to verify images and media preservation, attribution合规, directory structure, and comprehensive documentation.

Table 2 summarizes phase objectives, key tasks, status, and outputs.

Table 2: Phase-wise plan and progress tracker

| Phase | Objective                              | Key Tasks                                              | Status            | Outputs                                                                              |
|-------|----------------------------------------|--------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------|
| 1     | Initial research and source identification | Map syllabus to Wikipedia pages; license confirmation | Complete          | Source list; mapping                                                                 |
| 2     | Physics curation                       | Extract, save, attribute                               | Complete          | 5 physics HTML files                                                                 |
| 3     | Chemistry curation                     | Extract, save, attribute                               | Complete          | 5 chemistry HTML files                                                               |
| 4     | Biology curation                       | Extract, save, attribute                               | Complete          | 5 biology HTML files                                                                 |
| 5     | Environmental Science curation         | Extract, save, attribute; assisted biodiversity        | Complete          | 5 environmental-science HTML files; alternative workflow for biodiversity[^7]       |
| 6     | Processing and documentation           | HTML fidelity; attribution; index; rev logs            | In progress       | Index; attribution templates; environmental-science rev log                          |
| 7     | Quality assurance                      | Verify images; attribution合规; structure; coverage     | Pending           | QA checklist and reports                                                             |

Rate limiting constrained bulk media capture; however, topical coverage is complete and attribution合规 is embedded per file.

## Licensing and Attribution Compliance

All topical HTML files include embedded CC BY-SA 3.0 attribution blocks referencing the source Wikipedia page and license. Extraction dates are recorded for environmental science content (2025-10-30), and revision IDs are documented for the five environmental science files. To ensure full reproducibility, revision IDs and dump dates must be captured for all other sources using Wikimedia’s official dumps and guidance.[^2][^3][^4]

Table 3 summarizes attribution compliance and documentation status by subject.

Table 3: Attribution compliance status

| Subject            | Files (No.) | Attribution Present | License Linkage Verified | Extraction Date Recorded | Revision ID Logged |
|--------------------|-------------|---------------------|--------------------------|--------------------------|--------------------|
| Physics            | 5           | Yes                 | Yes                      | Pending                  | Pending            |
| Chemistry          | 5           | Yes                 | Yes                      | Pending                  | Pending            |
| Biology            | 5           | Yes                 | Yes                      | Pending                  | Pending            |
| Environmental Sci. | 5           | Yes                 | Yes                      | Yes (2025-10-30)         | Complete           |

This approach satisfies license obligations and prepares the ground for audit-ready reproducibility once revision logs are completed for all subjects.

## Environmental Science Evidence Synthesis

Environmental Science content within the corpus spans definitions and typologies (issues), the interdisciplinary field’s scope and history, ecosystem structure and function, pollution categories and controls, and biodiversity levels, importance, threats, and conservation strategies. The synthesis is exam-focused: it explains what the concepts are, how they operate, and why they matter for human and ecological systems.

### Environmental Issues: Drivers and Impacts

Environmental issues are disruptions in ecosystem function caused by human activity or natural events, serious when ecosystems cannot recover. Contemporary framing emphasizes three interlinked crises: climate change, pollution, and biodiversity loss.[^11] Key drivers include population growth (roughly 80 million per year), overconsumption, overexploitation, pollution, and deforestation. Consequences include global warming, environmental degradation (e.g., ocean acidification), mass extinction risks, biodiversity loss, and ecological crises.[^11]

Pollution has major forms—air, water, soil, noise, plastic, radioactive, thermal, light, and visual—and substantial health and ecological impacts. In 2019, pollution was associated with approximately nine million deaths worldwide (about one in six), with air pollution responsible for roughly three-quarters.[^11][^1] Table 4 lists pollution types with typical contaminants, health effects, and ecological impacts.

Table 4: Pollution types, contaminants, health effects, ecological impacts

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

Policy responses and awareness milestones include “Silent Spring” (1962), UNEP (1972), NEPA (1969), the Montreal Protocol (1987), and the Paris Agreement (2016), which collectively address pollution, ozone depletion, and climate change.[^12]

### Environmental Science: Interdisciplinary Field and History

Environmental science integrates physics, biology, chemistry, geography, and engineering to study and solve environmental problems. It emerged in its modern form during the 1960s–1970s, influenced by visible environmental disasters and scientific advances. Components include atmospheric sciences, ecology, environmental chemistry, geosciences, hydrology, and oceanography. Modern practice relies on GIS, remote sensing, and AI for monitoring and modeling systems.[^12]

Table 5 outlines key milestones and their impacts.

Table 5: Timeline of environmental science milestones (selected)

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

An ecosystem is a community of living organisms interacting with their nonliving environment, connected by energy flows and nutrient cycles. Energy enters primarily via photosynthesis (primary production) and moves through trophic levels via food chains and food webs. Decomposition recycles nutrients; biogeochemical cycles (e.g., nitrogen, phosphorus) sustain productivity. Ecosystems respond to disturbances through succession, with primary succession on newly exposed surfaces and secondary succession where soil remains.[^13]

Nutrient classifications and typical roles are summarized in Table 6.

Table 6: Nutrient classes and typical ecological roles

| Class          | Examples                                           | Typical Roles/Limitations                                                      |
|----------------|----------------------------------------------------|--------------------------------------------------------------------------------|
| Macronutrients (Primary) | N, P, K                              | Frequently limiting; essential for growth and development                      |
| Macronutrients (Secondary) | Ca, Mg, S                         | Important for plant structure, enzyme function, and metabolic processes         |
| Micronutrients        | B, Cl, Cu, Fe, Mn, Mo, Zn        | Required in trace amounts; critical for enzyme catalysis and physiological regulation |
| Beneficial            | Al, Co, I, Ni, Se, Si, Na, V      | Beneficial under specific conditions or for certain species                     |

Ecosystem services—the benefits people obtain from ecosystems—include provisioning (food, water, fuel, medicinal plants), regulating (climate regulation, water purification, pollination), cultural (aesthetic, spiritual, recreational), and supporting (nutrient cycling, primary production) services (Table 7).

Table 7: Ecosystem services categories and examples

| Category      | Examples                                                                |
|---------------|-------------------------------------------------------------------------|
| Provisioning  | Food (crops, fish), fresh water, fuel, fiber, medicinal plants          |
| Regulating    | Climate regulation, water purification, flood control, pollination      |
| Cultural      | Aesthetic value, spiritual significance, recreation, education          |
| Supporting    | Nutrient cycling, primary production, soil formation                    |

Anthropogenic nitrogen fluxes account for a large share of ecosystem nitrogen inputs, reflecting human influence on biogeochemical cycles.[^13]

### Pollution: Types, Sources, Effects, and Controls

Pollution’s sources include natural (volcanoes, wildfires) and human (point and nonpoint) categories. Health impacts range from respiratory and cardiovascular disease (ozone and particulate matter) to neurological effects from heavy metals (e.g., mercury and lead). Ecological effects include biomagnification, ocean acidification, reduced photosynthesis, soil infertility, acid rain, water deoxygenation, and plastic accumulation.[^1]

Control approaches combine practices (recycling, reuse, waste minimization, pollution prevention) and technologies (e.g., scrubbers, electrostatic precipitators, activated sludge, constructed wetlands, bioremediation). Table 8 summarizes major technologies by domain.

Table 8: Pollution control technologies by domain

| Domain               | Technologies (Examples)                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------|
| Air                  | Scrubbers (baffle spray, cyclonic spray, ejector venturi), thermal oxidizers, baghouses, cyclones, electrostatic precipitators |
| Water/Wastewater     | Sedimentation, activated sludge, aerated lagoons, constructed wetlands, API oil-water separators, biofilters, dissolved air flotation, ultrafiltration |
| Soil/Other           | Bioremediation, vapor recovery systems, phytoremediation                                                |

Global burden estimates emphasize urgency: pollution caused approximately nine million deaths in 2019, with air pollution responsible for about three-quarters; water pollution contributed roughly 1.4 million deaths.[^1]

### Biodiversity: Levels, Importance, Threats, Conservation

Biodiversity encompasses variability across genetic, species, ecosystem, and phylogenetic levels and is fundamental to ecosystem resilience and human well-being. It supports provisioning, regulating, and cultural services; contributes to agricultural productivity, nutrition security, disease prevention, and mental health; and has been estimated to provide about $150 trillion in annual value, with losses projected at roughly $5 trillion per year.[^7]

The current crisis is often described as a sixth mass extinction, driven primarily by habitat destruction, climate change, overexploitation, pollution, and invasive species. Recent assessments indicate significant wildlife population declines—about 73% average decline since 1970 (Living Planet Report 2024)—and a substantial share of assessed species threatened with extinction per the IUCN Red List.[^7] Biodiversity exhibits a latitudinal gradient, with concentrations in forested regions.

Conservation strategies span protected areas (national parks, wildlife sanctuaries, marine protected areas), restoration techniques (gene banks, wildlife corridors, invasive species removal), and international frameworks (CBD, CITES, Ramsar, Bonn, Cartagena, UN High Seas Treaty). The “30 by 30” initiative seeks to protect 30% of land and oceans by 2030 (Table 9).

Table 9: Species estimates, documented species, extinction metrics (selected)

| Metric                                  | Estimate/Value                                      |
|-----------------------------------------|------------------------------------------------------|
| Estimated terrestrial species            | ~8.7 million                                        |
| Estimated oceanic species                | ~2.2 million                                        |
| Documented species                       | ~1.2 million (~86% undescribed)                     |
| Extinction rate                          | 100–10,000× faster than background rates            |
| Threatened species (assessed)            | ~40% (IUCN Red List)                                |

Table 10: Protected area types and global coverage targets

| Type/Target            | Examples/Goals                                                           |
|------------------------|---------------------------------------------------------------------------|
| Protected Area Types   | National parks (IUCN Category II), wildlife sanctuaries, forest protected areas, marine protected areas |
| Global Target          | 30 by 30 initiative (protect 30% of land and oceans by 2030)             |
| Benefits               | Genetic resource conservation, medicinal plant protection, water security, tourism, disaster risk reduction |

This synthesis equips candidates with both definitional clarity and applied understanding, aligning with RRB NTPC’s emphasis on concepts, mechanisms, and implications.

## Inventory and Directory Structure

The corpus is organized under a common directory schema per subject (physics, chemistry, biology, environmental-science), with a central index at the subject root. A local images directory has been created and includes placeholder assets for environmental science; however, bulk image downloads were rate-limited, and images have not yet been archived locally or mapped into the HTML.

Table 11 summarizes file inventories by subject.

Table 11: File inventory by subject

| Subject            | Local File Names (No extension)                                                                                         | Attribution Present | Rev ID Status  | Images Present |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------|----------------|----------------|
| Physics            | physics_general; physics_energy; physics_electromagnetism; physics_gravitation; physics_sound                            | Yes                 | Pending        | Not yet        |
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

The remaining open items are concentrated in media preservation and complete revision capture:
- Images/diagrams: Rate limiting (HTTP 429) prevented bulk downloads. A gap-closure plan should orchestrate batch downloads with conservative request pacing, off-peak scheduling, and adherence to Wikimedia guidance for database access and media retrieval.[^3]
- Revision IDs and dump dates: Environmental Science revision IDs are captured; Physics, Chemistry, and Biology require completion. Dump dates should be recorded per source using official Wikimedia dumps.[^4]
- QA checklist: Final verification of image presence and local referencing, attribution合规, directory structure, and topic coverage completeness.

Table 13 outlines the open issues, proposed actions, ownership, and target dates.

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
| biodiversity                        | Biodiversity               | [^7]             | 2025-10-30      | 1317660757   | Levels; importance; threats; conservation|

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