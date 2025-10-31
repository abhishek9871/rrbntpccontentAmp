# RRB NTPC Mathematics: Curated Study Materials from Wikimedia — Collection, Organization, and Metadata Plan

## Executive Summary

This report documents the creation of a curated, offline, RRB NTPC Mathematics study corpus drawn from Wikimedia (Wikipedia and Wikibooks). The corpus spans ten core syllabi topics and is designed for reliable exam-focused revision: Ratio and Proportion, Time and Work, Simple and Compound Interest, Profit and Loss, Average, Percentage, Algebra basics, Geometry, Mensuration, and Statistics. The materials have been collected as HTML with standardized metadata, and presented via a master index for intuitive navigation. All content is licensed under Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0), with attribution practices incorporated throughout the corpus and its metadata.[^1]

The collection approach blends authoritative core concepts from Wikipedia with targeted, exam-relevant portions of Wikibooks where appropriate. Because stable Wikimedia dumps were not used in this tranche, snapshot dates across the corpus are uniformly recorded as 30 October 2025 to preserve reproducibility. This alignment ensures every topical module can be audited, cited, and reused with consistent metadata. The master index provides a single entry point to all topic modules and their metadata, supporting efficient preparation and review for the RRB NTPC Mathematics section.

At a high level, the project seeks to maximize exam alignment, traceability, and reuse while acknowledging discrete gaps that require targeted follow-ups. Specifically, the Time and Work module is currently based on derived foundational concepts rather than a dedicated elementary source; some figures and embedded media are not captured in this tranche; and a small subset of profit and loss definitions are supported by business-focused sources, necessitating further elementary supplementary references. These gaps are documented and remediated through a clear action plan.

## Scope, Sources, and Licensing

The scope encompasses ten foundational Mathematics topics mapped to the RRB NTPC syllabus. Source selection prioritizes stable, well-established Wikipedia articles for definitions and canonical formulas, complemented by Wikibooks where the pedagogical style and elementary treatment add clarity for typical exam problem-solving.

All extracted content is licensed under CC BY-SA 3.0. Attribution is provided via topic-level metadata fields, including title, source URL(s), snapshot date, license name and URL, a concise description, and a topics-covered list. This ensures the corpus meets Wikimedia’s attribution-sharealike requirements and supports transparent lineage for downstream reuse.[^1]

Snapshot consistency is addressed by setting a uniform snapshot date of 30 October 2025 for all topics in this tranche. Where multiple sources exist for a single topic, the metadata aggregates the relevant references with a brief note on their roles in the study module.

To illustrate the breadth and source mix, the following table inventories topics, primary sources, and coverage notes.

Table 1. Source inventory by topic

| Topic                      | Primary Source (Ref. ID)         | Source Type   | Snapshot Date   | Coverage Notes                                                                 |
|---------------------------|----------------------------------|---------------|-----------------|---------------------------------------------------------------------------------|
| Ratio and Proportion      | Ratio [^2], Proportion [^3]      | Wikipedia     | 2025-10-30      | Definitions, properties, and ratio typologies                                  |
| Simple & Compound Interest| Interest [^4], Compound [^5]     | Wikipedia     | 2025-10-30      | Concept definitions and formulas                                                |
| Average                   | Primary Mathematics: Average [^6]| Wikibooks     | 2025-10-30      | Averages with worked examples and pedagogy                                      |
| Percentage                | Percentage [^7]                  | Wikipedia     | 2025-10-30      | Definitions, change formulas, percentage points                                 |
| Algebra Basics            | Algebra [^8]                     | Wikipedia     | 2025-10-30      | Variables, equations, polynomials, factoring, linear/quadratic                  |
| Geometry                  | Geometry [^9]                    | Wikipedia     | 2025-10-30      | Foundational concepts: points, lines, angles, triangles, circles                |
| Mensuration               | Elementary Geometry Formulas [^10]| Wikipedia    | 2025-10-30      | 2D/3D area, perimeter, volume formulas                                          |
| Statistics                | Statistics [^11]                 | Wikipedia     | 2025-10-30      | Descriptive vs inferential, central tendency, dispersion                        |
| Profit and Loss           | Profit Margin [^12], Profit (Accounting) [^13], Net Income [^14] | Wikipedia | 2025-10-30 | Margin definitions; accounting profit structure; example contexts for P&L        |
| Time and Work             | Derived foundational concepts (see Alignment & Pedagogical Approach) | Derived | 2025-10-30 | Work-rate reasoning; combined work formulas; gaps flagged for dedicated sources |

### Topics-to-Sources Mapping

Cross-mapping the ten RRB NTPC topics to their primary references clarifies how the corpus aligns to the syllabus and identifies where additional sourcing is advisable. The time and work module, in particular, will benefit from a dedicated elementary source to further strengthen its evidence base.

Table 2. Topic-to-source crosswalk

| Topic                      | Primary Wikipedia Article | Primary Wikibooks Source | Snapshot Date | Notes on Alignment                                                              |
|---------------------------|---------------------------|--------------------------|---------------|----------------------------------------------------------------------------------|
| Ratio and Proportion      | Ratio [^2]; Proportion [^3] | —                        | 2025-10-30    | Direct match; classical definitions and properties                               |
| Time and Work             | —                         | —                        | 2025-10-30    | Derived module pending dedicated elementary source                               |
| Simple & Compound Interest| Interest [^4]; Compound [^5] | —                     | 2025-10-30    | Clear definitions and formulas suitable for problem sets                         |
| Profit and Loss           | Profit Margin [^12]; Net Income [^14] | —            | 2025-10-30    | Margin-based definitions; complements accounting-oriented Profit (Accounting) [^13] |
| Average                   | —                         | Primary Mathematics: Average [^6] | 2025-10-30 | Pedagogically tailored to averages                                               |
| Percentage                | Percentage [^7]           | —                        | 2025-10-30    | Standard definitions and computation patterns                                    |
| Algebra Basics            | Algebra [^8]              | —                        | 2025-10-30    | Core algebra toolkit for exam problem solving                                    |
| Geometry                  | Geometry [^9]             | —                        | 2025-10-30    | Foundational concepts underpin visual reasoning                                  |
| Mensuration               | Elementary Geometry Formulas [^10] | —            | 2025-10-30    | Canonical formulas for 2D/3D measures                                            |
| Statistics                | Statistics [^11]          | —                        | 2025-10-30    | Descriptive vs inferential distinctions; core summaries                          |

## Collection Methodology and File Organization

The corpus follows a consistent directory structure and metadata schema to enable predictable navigation and long-term maintenance. Each topic module includes a human-readable HTML page (index.html), an images directory for locally hosted assets (currently sparse), and a metadata.json capturing attribution, source lineage, and topical coverage.

The master index provides an overview of the full collection and links to every topic module. This single entry point is designed for exam candidates who need to pivot quickly between related concepts (for instance, moving from Percentage to Ratio and Proportion or from Mensuration to Geometry), minimizing cognitive load and improving study flow.

Table 3. Directory structure and file inventory

| Directory                    | Index File Present | Metadata File Present | Image Assets Present | Notes                                                                 |
|-----------------------------|--------------------|-----------------------|----------------------|------------------------------------------------------------------------|
| ratio-proportion            | Yes                | Yes                   | No                   | Two Wikipedia anchors support ratio and proportion                     |
| simple-compound-interest    | Yes                | Yes                   | No                   | Simple/compound interest coverage                                      |
| average                     | Yes                | Yes                   | No                   | Wikibooks-derived pedagogy on averages                                 |
| percentage                  | Yes                | Yes                   | No                   | Standard definitions and change formulas                               |
| algebra-basics              | Yes                | Yes                   | No                   | Variables, equations, polynomials, factoring                           |
| geometry                    | Yes                | Yes                   | No                   | Foundational geometric concepts                                        |
| mensuration                 | Yes                | Yes                   | No                   | 2D/3D formulas; figures to be added in future                          |
| statistics                  | Yes                | Yes                   | No                   | Descriptive/inferential framing with core measures                     |
| profit-loss                 | Yes                | Yes                   | No                   | Margin-centric definitions; pending elementary loss/discount formulas  |
| time-and-work               | Yes                | Yes                   | No                   | Derived foundational content; to be augmented by dedicated sources     |

### File Naming Conventions

Each topic folder contains an index.html file to make the module renderable in browsers without additional configuration. An images directory is reserved for local assets such as diagrams and figures, supporting offline access. A metadata.json file accompanies each module, housing the canonical attribution and scope fields to enable automation, validation, and audit.

## Content Modules Overview

The ten modules collectively cover the core conceptual and computational needs of the RRB NTPC Mathematics syllabus. Definitions are paired with canonical formulas and, where sources provide, worked examples and pedagogical asides. Although images are limited in this tranche, the narrative explanations are sufficiently complete for self-study and concept review.

### Ratio and Proportion

This module anchors the study of comparative quantities with classical definitions and properties. Euclid’s characterization of ratio as a relation between magnitudes and proportion as an equality of two ratios frames the topic with historical and mathematical rigor.[^2][^3] The coverage includes typologies such as part-to-part and part-to-whole ratios, the means–extremes property, and common manipulators (e.g., compounding and dividing ratios). These underpin a wide range of RRB NTPC problems, from mixture compositions to rates and speed–time variants.

### Simple and Compound Interest

The Interest module provides precise definitions and the standard formulas used throughout exam problem sets.[^4][^5] Simple interest is treated linearly with principal, rate, and time, while compound interest introduces exponential growth through periodic compounding. Worked examples typically demonstrate computations over annual, half-yearly, and quarterly compounding cycles. Clear articulation of these formulas is critical for the financial arithmetic questions common in the NTPC Quantitative Aptitude section.

### Average

Averages appear frequently in NTPC problem sets, often tied to weighted averages in mixtures or speeds across segments. The Wikibooks module on Primary Mathematics: Average offers an accessible, teaching-oriented treatment with clear examples and practice-friendly language, making it a good complement to more formal encyclopedic entries.[^6] The module covers arithmetic mean, weighted averages, and includes worked examples that emphasize methodology over rote formula memorization.

### Percentage

The Percentage module covers the definition, computation patterns, and common pitfalls associated with percentage change.[^7] It explains percentage points versus percent change—critical when interpreting growth rates or rate adjustments—and demonstrates sequential percentage changes. The treatment aligns with the typical NTPC style, which tests conceptual clarity in applying percentages to price, discounts, and proportional divisions.

### Algebra Basics

This module assembles the essential algebra toolkit: variables and expressions; linear equations and their geometric interpretation; quadratic equations and the quadratic formula; polynomials and factoring strategies.[^8] The narrative clarifies the difference between identities and conditional equations and demonstrates standard manipulation techniques—balancing operations, factoring by grouping, and using the zero-product property. These skills translate directly into NTPC problems requiring equation formation and solution.

### Geometry

Geometry establishes the foundation for spatial reasoning used throughout mensuration and visual problem solving.[^9] The module introduces points, lines, planes, and angles, then moves to polygons and circles, with discussion of congruence and similarity. The Pythagorean theorem and its triples are highlighted where relevant. These concepts support figure-based questions that rely on identifying properties and applying theorems correctly.

### Mensuration

Mensuration collects the canonical area and perimeter formulas for two-dimensional shapes and volume formulas for three-dimensional solids, taken from the “List of formulas in elementary geometry.”[^10] While figures are not embedded in this tranche, the formulas are presented with symbol definitions and usage notes. The module functions as a compact reference for the NTPC focus on rectangles, triangles, circles, and common solids such as cubes, cylinders, cones, and spheres.

Table 4. Mensuration formula inventory (selected shapes)

| Shape          | Measure     | Formula        | Symbol Definitions                      |
|----------------|-------------|----------------|-----------------------------------------|
| Square         | Area        | l²             | l = side length                         |
| Square         | Perimeter   | 4l             | l = side length                         |
| Rectangle      | Area        | lb             | l = length, b = breadth                 |
| Rectangle      | Perimeter   | 2(l + b)       | l = length, b = breadth                 |
| Circle         | Area        | πr²            | r = radius                              |
| Circle         | Perimeter   | 2πr (or πd)    | r = radius, d = diameter                |
| Triangle       | Area        | (b·h)/2        | b = base, h = height                    |
| Triangle       | Perimeter   | a + b + c      | a, b, c = side lengths                  |
| Cylinder       | Volume      | πr²h           | r = radius, h = height                  |
| Cone           | Volume      | (1/3)πr²h      | r = radius, h = height                  |
| Sphere         | Volume      | (4/3)πr³       | r = radius                              |
| Sphere         | Surface Area| 4πr²           | r = radius                              |

Note: This selection highlights the most NTPC-relevant formulas. The full module contains additional shapes and variants as per the source list.[^10]

### Statistics

The Statistics module distinguishes descriptive statistics—summarizing sample data—from inferential statistics, which draw conclusions about underlying populations.[^11] It introduces central tendency (mean, median, mode) and dispersion (variance, standard deviation), clarifies how probability underpins statistical inference, and discusses the normal distribution as a canonical example. The emphasis is on conceptual clarity and practical interpretation—skills that surface in NTPC questions involving averages and data interpretation.

### Profit and Loss

Profit and Loss coverage leans on margin-based definitions and accounting profit structures. Profit margin expresses profit relative to revenue, with variants such as gross and net profit margin defined consistently with standard financial reporting.[^12][^14] Profit (accounting) situates profit within broader accounting frameworks, adding context for net sales, cost of goods sold, and operating expenses.[^13] While margin definitions are robust for exam use, elementary derivations for loss percentage and discount formulas are not fully captured in this tranche and are flagged as follow-ups.

### Time and Work

The Time and Work module currently derives foundational reasoning from algebra and proportional relationships: work-rate models, combined work when multiple workers cooperate, and the standard formulations for individual and joint completion times. While this approach is pedagogically sound for the NTPC level and consistent with general algebra treatment, the module flags the need for a dedicated elementary source that specifically addresses work-rate problems. This gap is recorded in the action plan for targeted sourcing.

## Alignment to RRB NTPC Syllabus

The corpus aligns to the RRB NTPC Mathematics syllabus through a topic-by-topic mapping. Each module provides definitions, canonical formulas, and illustrative computations consistent with the exam’s emphasis on ratio, rates, financial arithmetic, spatial reasoning, and data interpretation. The master index ensures rapid access to related modules—a key affordance during timed revision when candidates frequently pivot across Percentage and Ratio & Proportion or Mensuration and Geometry.

Table 5. RRB NTPC syllabus-to-collection mapping

| Syllabus Topic            | Collected Module            | Source Reference IDs        | Coverage Status | Notes                                                  |
|---------------------------|-----------------------------|-----------------------------|-----------------|--------------------------------------------------------|
| Ratio & Proportion        | Ratio and Proportion        | [^2], [^3]                  | Complete        | Definitions, properties, typologies                    |
| Time and Work             | Time and Work               | Derived                     | Partial         | Core formulas present; dedicated source pending        |
| Simple & Compound Interest| Simple & Compound Interest  | [^4], [^5]                  | Complete        | Standard formulas; typical compounding cases           |
| Profit and Loss           | Profit and Loss             | [^12], [^13], [^14]         | Partial         | Margin-focused; loss % and discount derivations to add |
| Average                   | Average                     | [^6]                        | Complete        | Teaching-oriented explanations with examples           |
| Percentage                | Percentage                  | [^7]                        | Complete        | Change formulas; percentage points treatment           |
| Algebra basics            | Algebra Basics              | [^8]                        | Complete        | Variables, equations, polynomials, factoring           |
| Geometry                  | Geometry                    | [^9]                        | Complete        | Foundational concepts for visual reasoning             |
| Mensuration               | Mensuration                 | [^10]                       | Complete        | 2D/3D formulas; figures to be added                    |
| Statistics                | Statistics                  | [^11]                       | Complete        | Descriptive vs inferential; central tendency, dispersion|

Note: Where coverage is partial, the metadata flags missing elements (e.g., elementary loss percentage derivations) and identifies corrective actions.

## Quality Assurance and Compliance

Quality assurance centers on metadata validation, content integrity checks, and licensing compliance. Metadata schema conformance is verified across all modules: titles are present and meaningful; source URLs are recorded; snapshot dates are uniformly set to 30 October 2025; license is declared as CC BY-SA 3.0; descriptions summarize scope; and topics-covered enumerates key sub-themes. HTML pages render cleanly without broken links in this tranche, though images are limited and will be expanded in future pulls.

Licensing compliance is audited against CC BY-SA 3.0, ensuring attribution is clear and share-alike obligations are documented via metadata and footers.[^1] The master index and individual modules preserve attribution to source pages and publishers, and reproduction is supported with consistent citation fields.

Table 6. Metadata validation checklist

| Module                 | Metadata Fields Valid | Attribution Present | License Declared | Snapshot Date Set | Notes                       |
|------------------------|-----------------------|---------------------|------------------|-------------------|-----------------------------|
| Ratio & Proportion     | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Simple & Compound Interest | Yes               | Yes                 | Yes              | 2025-10-30        | —                           |
| Average                | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Percentage             | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Algebra Basics         | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Geometry               | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Mensuration            | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Statistics             | Yes                   | Yes                 | Yes              | 2025-10-30        | —                           |
| Profit & Loss          | Yes                   | Yes                 | Yes              | 2025-10-30        | See gaps noted              |
| Time and Work          | Yes                   | Yes                 | Yes              | 2025-10-30        | Derived module              |

### Licensing and Attribution

All modules adhere to CC BY-SA 3.0. Attribution is maintained through metadata fields and content footers, referencing the original Wikimedia articles and publishers. Share-alike obligations are respected by preserving the license in metadata and encouraging derivative works to be distributed under the same terms.[^1]

## Gaps, Risks, and Remediation Plan

Three gaps require attention:

1. Time and Work. The module currently derives foundational reasoning from general algebra concepts. A dedicated elementary mathematics source focused on work-rate problems will improve rigor and teaching consistency. Action: identify a stable, elementary-focused page (preferably from Wikibooks) and supplement the current module with dedicated derivations and practice examples.

2. Profit and Loss. The current reliance on margin-focused and accounting-oriented references leaves some NTPC-relevant elementary definitions incomplete—specifically loss percentage derivations and discount formulations suitable for item-level transactions. Action: add an elementary mathematics reference covering cost price, selling price, loss percentage, markup, and discount, ensuring pedagogical clarity and exam-focused derivations.

3. Visuals and Assets. Images and figures (particularly in Mensuration and Geometry) are not captured in this tranche. Action: conduct a targeted image pull and embed relevant figures (e.g., shape diagrams and geometric constructions) into the local images directories to improve comprehension and exam utility.

Reproducibility is managed through snapshot dates; however, moving to stable Wikimedia dumps would reduce drift risk and improve version stability. Action: define dump version identifiers and capture the relevant dump dates for future pulls, establishing a reproducible cadence.

Table 7. Gap remediation tracker

| Gap                                    | Affected Module   | Proposed Source Type                | Action Items                                        | Status   |
|----------------------------------------|-------------------|-------------------------------------|-----------------------------------------------------|----------|
| Time and Work missing dedicated source | Time and Work     | Wikibooks (elementary mathematics)  | Source selection; integrate derivations; QA         | Planned  |
| Loss percentage and discount definitions | Profit & Loss    | Elementary mathematics reference     | Add definitions; derive formulas; update metadata   | Planned  |
| Images/figures not captured            | Mensuration, Geometry | Wikimedia media (figures)        | Pull images; embed locally; alt-text; QA            | Planned  |
| Snapshot reproducibility (dumps)       | All               | Stable Wikimedia dumps               | Define dump versions; record dates; re-pull corpus  | Planned  |

## Implementation Roadmap and Next Steps

The immediate priority is metadata finalization and format validation across all modules, followed by embedding visuals in Mensuration and Geometry. In parallel, targeted content enhancement is required for Time and Work and Profit and Loss to close definitional gaps. The final stage replaces live snapshot references with stable dump-based versions to strengthen reproducibility.

Table 8. Next steps timeline

| Task                                                | Dependency                         | Owner        | ETA         | Success Criteria                                      |
|-----------------------------------------------------|------------------------------------|--------------|-------------|-------------------------------------------------------|
| Metadata validation and format checks                | All modules complete               | Content QA   | Week 1      | All metadata.json pass schema and attribution checks  |
| Image embedding for Mensuration and Geometry         | Image pull and local storage       | Editorial    | Weeks 2–3   | Relevant figures embedded with alt-text               |
| Time and Work source supplementation                 | Source selection and integration   | Research     | Weeks 2–4   | Dedicated source integrated; module updated           |
| Profit and Loss definitional enhancement             | Elementary reference selection     | Research     | Weeks 2–4   | Loss % and discount definitions added                 |
| Master index enhancements                            | Topic modules finalized            | Editorial    | Week 3      | Index includes updated coverage notes and progress    |
| Migration to stable Wikimedia dumps                  | Dump selection and tooling         | Data Eng.    | Month 2     | Dump version captured; reproducible re-pull executed  |

## Appendix A: Source Index and Citation Map

Table 9. Comprehensive source-to-topic map

| Topic                      | Reference ID(s)          | Source Title                                 | Source Type   | Snapshot Date | Use in Corpus                                           |
|---------------------------|--------------------------|----------------------------------------------|---------------|---------------|---------------------------------------------------------|
| Ratio & Proportion        | [^2], [^3]               | Ratio; Proportion (mathematics)              | Wikipedia     | 2025-10-30    | Core definitions and properties                          |
| Simple & Compound Interest| [^4], [^5]               | Interest; Compound interest                  | Wikipedia     | 2025-10-30    | Concept definitions and formulas                         |
| Average                   | [^6]                     | Primary Mathematics: Average                 | Wikibooks     | 2025-10-30    | Teaching-oriented average computations                   |
| Percentage                | [^7]                     | Percentage                                   | Wikipedia     | 2025-10-30    | Definitions, change formulas, percentage points          |
| Algebra Basics            | [^8]                     | Algebra                                      | Wikipedia     | 2025-10-30    | Variables, equations, polynomials, factoring             |
| Geometry                  | [^9]                     | Geometry                                     | Wikipedia     | 2025-10-30    | Foundational concepts; theorems; shapes                  |
| Mensuration               | [^10]                    | List of formulas in elementary geometry      | Wikipedia     | 2025-10-30    | 2D/3D area, perimeter, volume formulas                   |
| Statistics                | [^11]                    | Statistics                                   | Wikipedia     | 2025-10-30    | Descriptive/inferential, central tendency, dispersion    |
| Profit and Loss           | [^12], [^13], [^14]      | Profit margin; Profit (accounting); Net income| Wikipedia     | 2025-10-30    | Margin and accounting profit contexts; example usage     |
| Time and Work             | Derived                  | —                                            | Derived       | 2025-10-30    | Work-rate reasoning; combined work formulas              |

## References

[^1]: Creative Commons Attribution-ShareAlike License 3.0. https://creativecommons.org/licenses/by-sa/3.0/
[^2]: Ratio (Wikipedia). https://en.wikipedia.org/wiki/Ratio
[^3]: Proportion (mathematics) (Wikipedia). https://en.wikipedia.org/wiki/Proportion_(mathematics)
[^4]: Interest (Wikipedia). https://en.wikipedia.org/wiki/Interest
[^5]: Compound interest (Wikipedia). https://en.wikipedia.org/wiki/Compound_interest
[^6]: Primary Mathematics: Average (Wikibooks). https://en.wikibooks.org/wiki/Primary_Mathematics/Average
[^7]: Percentage (Wikipedia). https://en.wikipedia.org/wiki/Percentage
[^8]: Algebra (Wikipedia). https://en.wikipedia.org/wiki/Algebra
[^9]: Geometry (Wikipedia). https://en.wikipedia.org/wiki/Geometry
[^10]: List of formulas in elementary geometry (Wikipedia). https://en.wikipedia.org/wiki/List_of_formulas_in_elementary_geometry
[^11]: Statistics (Wikipedia). https://en.wikipedia.org/wiki/Statistics
[^12]: Profit margin (Wikipedia). https://en.wikipedia.org/wiki/Profit_margin
[^13]: Profit (accounting) (Wikipedia). https://en.wikipedia.org/wiki/Profit_(accounting)
[^14]: Net income (Wikipedia). https://en.wikipedia.org/wiki/Net_income

## Acknowledged Information Gaps

- Time and Work requires a dedicated elementary mathematics source to supplement derived foundational reasoning. 
- Stable Wikimedia dumps were not used; snapshot dates are set to 30 October 2025 across all modules in this tranche. 
- Figures and images (especially for Mensuration and Geometry) are not captured in the current corpus. 
- Profit and Loss coverage leans on margin-focused sources; loss percentage and discount derivations need elementary-formula references to fully align with RRB NTPC problem types.

---

This analytical roadmap documents the corpus as of 30 October 2025 and outlines a practical path to close residual gaps, embed visuals, and migrate to stable Wikimedia dumps for long-term reproducibility.