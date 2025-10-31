# OpenZIM Build Manifests for Curated Content Bundles: Blueprint and Compliance Plan

## Executive Summary and Objectives

This blueprint defines a standardized, compliance-first approach to authoring OpenZIM build manifests for six curated content bundles: previous-papers, mathematics-foundations, reasoning-complete, general-science, general-awareness, and practice-sets. The intended outcome is a consistent, automated, and legally sound packaging workflow that yields offline-first Progressive Web App (PWA) integrations suitable for exam preparation and learning contexts. The manifests will specify content sources, metadata inclusion, compression settings, indexing requirements, licensing compliance, and PWA-specific behaviors—including optional Service Worker (SW) hints and ETag/caching strategies—without binding to any external build tool or proprietary runtime.

Deliverables are six build manifests produced as both YAML and JSON for clarity and tooling interoperability, targeting the openzim-manifests/ directory. The dataset sources include DIKSHA content collections for General Awareness and Mathematics, RRB/NTPC exam materials, Wikimedia-based open educational resources (OER), and practice sets from GA and licensing sources. The plan is grounded in licensing constraints documented in the consolidated license register and credible portal catalog, emphasizing Creative Commons attribution requirements and ShareAlike obligations, government work usage, and strict exclusion or permission gates for All Rights Reserved materials.[^2][^3][^1][^4][^5]

OpenZIM build outputs will be discoverable and navigable offline via a combined full-text and field-based index strategy, supporting bilingual content (English and Hindi) and subject taxonomies aligned to exam preparation. Compression defaults will maximize offline usability without compromising attribution fidelity or ShareAlike obligations. The blueprint also defines compliance gates, audit steps, and periodic review to maintain legal alignment over time.

To anchor scope and execution, Table 1 presents the bundle-to-source mapping, licensing posture, and output artifact naming conventions.

### Table 1. Bundle-to-Source Mapping

| Bundle | Primary Local Content Sources | Licensing Class (from register) | Notes on Coverage/Compliance | Output Artifact Naming |
|---|---|---|---|---|
| previous-papers | /workspace/content/rrb-ntpc/previous-papers/ (CBT1, CBT2) | Government Work | Include only official RRB/NTPC papers. Verify attribution and source URLs prior to release. Do not include ARR practice materials. | previous-papers-bundle.{yml,json} |
| mathematics-foundations | /workspace/diksha-math/study-materials/oer/; /workspace/content/rrb-ntpc/study-materials/oer/; /workspace/content/rrb-ntpc/study-materials/wikimedia/ | CC BY 4.0; CC BY-SA 3.0/4.0 | DIKSHA NCERT math is CC BY 4.0; Wikimedia items are CC BY-SA (share-alike required). Prefer bilingual assets when available. | mathematics-foundations-bundle.{yml,json} |
| reasoning-complete | /workspace/diksha-reasoning/downloaded_content/ (logical_reasoning, mental_ability, non_verbal_reasoning, verbal_reasoning) | Mixed (incl. Unknown/ARR) | Exclude Unknown/ARR unless permissions are secured. Include DIKSHA CC BY 4.0 items only; mark others for verification and hold back. | reasoning-complete-bundle.{yml,json} |
| general-science | /workspace/diksha-ga/science-technology/ (NCERT PDFs/ZIPs) | CC BY 4.0 | Include NCERT GA science items; ensure attribution includes Title, Author, Source, License (TASL). | general-science-bundle.{yml,json} |
| general-awareness | /workspace/diksha-ga/ (current-affairs/national/international/sports, polity, geography, indian-history, static-gk, economy) | CC BY 4.0; Government Work | Maintain bilingual coverage; for government portals include attribution and source URLs. Hold back Unknown/ARR GA materials. | general-awareness-bundle.{yml,json} |
| practice-sets | /workspace/practice-ga/ (subject folders), /workspace/content/rrb-ntpc/practice-sets/ | Mixed (CC BY 4.0; Government Work; ARR) | Include only CC BY 4.0 or Government Work items. Exclude ARR sets unless written permission is obtained. | practice-sets-bundle.{yml,json} |

This mapping ensures each manifest anchors to concrete local paths and adopts the licensing posture from the consolidated register and credible portal catalog, enabling automated compliance checks and predictable builds.[^2][^3][^1]

### Bundle Scope Overview

Each bundle represents a clearly bounded collection aligned to competitive exam preparation:

- The previous-papers bundle focuses exclusively on official CBT1/CBT2 RRB/NTPC question papers.
- The mathematics-foundations bundle integrates DIKSHA NCERT mathematics and targeted Wikimedia math content to build conceptual foundations.
- The reasoning-complete bundle consolidates DIKSHA reasoning modules across logical, verbal, non-verbal, and mental ability categories.
- The general-science bundle captures NCERT science resources from DIKSHA GA, including physics, chemistry, and biology PDFs/ZIPs.
- The general-awareness bundle spans current affairs, polity, geography, Indian history, static GK, and economy from DIKSHA GA.
- The practice-sets bundle aggregates exercise materials across subjects while applying strict licensing filters.

In combination, these bundles provide comprehensive coverage for offline exam preparation, with content discoverable and navigable through a unified indexing scheme.

## Data Inventory and Local Input Landscape

The manifests rely on local datasets that reflect mixed licensing: Creative Commons (CC BY 4.0 and CC BY-SA 3.0/4.0), Government Work, and All Rights Reserved (ARR). While DIKSHA-sourced NCERT content is generally CC BY 4.0, Wikimedia content carries ShareAlike obligations. Government works require attribution to the issuing body. Third-party edtech materials frequently restrict redistribution and must be excluded absent explicit permission.[^2][^3][^1]

The practice materials licensing compliance report highlights source categories and constraints that drive the inclusion/exclusion logic in this plan: ARR sources are excluded from redistribution; Wikimedia items require attribution and ShareAlike; DIKSHA NCERT items require attribution under CC BY 4.0; and Government works must be attributed to the issuing body.[^2]

To visualize the compliance landscape, the following dashboard summarizes content categories and licensing signals.

![Licensing compliance dashboard overview](audit/comprehensive_dashboard.png)

The dashboard illustrates the predominance of CC and Government Work categories within DIKSHA and Wikimedia collections, with a meaningful presence of ARR sources in third-party portals. The insight for build governance is clear: prioritize CC BY 4.0 and Government Work sources for default inclusion, and enforce ShareAlike for Wikimedia items. ARR materials should default to exclusion unless permission workflows conclude favorably.

To support field mapping, Table 2 summarizes inventory signals and their implications for manifest metadata fields.

### Table 2. Content Inventory Signals and Field Mapping

| Inventory Signal | Local Example | Implication for Manifest Fields | Notes |
|---|---|---|---|
| License class | CC BY 4.0 (DIKSHA NCERT), CC BY-SA (Wikimedia), Government Work, ARR | license.type, license.attribution_required, license.redistribution_allowed, license.commercial_use_allowed, license.modifications_allowed, license.share_alike_required | Drives compliance rules and metadata enrichment templates.[^2][^3] |
| Source credibility | Government portals, NCERT/DIKSHA, Wikimedia | source.name, source.platform, source.credibility | Credible platforms reduce compliance risk and enable default inclusion.[^3][^1] |
| Bilingual availability | English/Hindi | language.support, language.bilingual | Enhances offline usability for national exam contexts. |
| Content types | PDF, ZIP, HTML, JSON | content.type, content.compression | Dictates extraction, compression approach, and index strategy. |
| ARR constraints | Third-party edtech portals | license.permission_required, include.false | ARR is excluded unless permissions are documented.[^2] |
| ShareAlike obligations | Wikimedia articles and books | license.share_alike_required = true | Derivatives must remain under CC BY-SA; impacts bundle licensing.[^9][^10][^11][^12][^13] |

The inventory confirms that YAML manifests should define path globs conservatively, include licensing checks per source, and enable bilingual indexing where assets permit.

## Licensing Compliance Framework

Manifests are the enforcement point for licensing obligations. The framework aligns source entries to license classes with explicit fields for attribution, redistribution permissions, commercial use allowances, modification rules, and ShareAlike requirements. Central to this is the consolidated license register, which documents the obligations for DIKSHA (NCERT), Wikimedia projects, Government works, and ARR/edtech platforms.[^2]

![Compliance audit checklist visual](audit/comprehensive_dashboard.png)

This visual underscores the need to encode compliance as executable rules inside manifests. For each asset, the manifest must carry the TASL (Title, Author, Source, License) attribution fields, identify ShareAlike obligations when applicable, and mark items requiring permission (ARR) as excluded or held back. Verification and permission requests are recorded and tracked.

### Table 3. License Class Mapping

| License Class | Attribution Required | Redistribution | Commercial Use | Modifications | ShareAlike | Typical Sources |
|---|---|---|---|---|---|---|
| CC BY 4.0 | Yes (TASL) | Yes (with TASL) | Yes | Yes | No | DIKSHA NCERT content.[^1][^6] |
| CC BY-SA 3.0/4.0 | Yes (TASL) | Yes (with TASL) | Yes | Yes (adaptations must remain CC BY-SA) | Yes | Wikimedia projects (Wikipedia, Wikibooks).[^9][^10][^11][^12][^13] |
| Government Work | Yes (to issuing body) | Yes (with attribution) | Typically yes | Typically yes | No | Official RRB and Government portals.[^4][^5] |
| All Rights Reserved (ARR) | Yes | No (without permission) | No (without permission) | No (without permission) | N/A | Third-party edtech portals (Testbook, Mockers, Jagran Josh).[^2] |
| Unknown/To Be Verified | Yes | No (until verified) | No (until verified) | No (until verified) | N/A | Platforms with unclear policies.[^3] |

### Table 4. Attribution Template Fields

| Field | Description | Applies To |
|---|---|---|
| title | Original content title | All sources |
| author | Creator/organization (e.g., NCERT, Wikimedia contributors, issuing government body) | All sources |
| source | Source URL or portal name | All sources |
| license | License designation (e.g., CC BY 4.0, CC BY-SA 3.0/4.0, Government Work) | All sources |
| changes | Description of modifications (if any) | Adapted content |

#### Creative Commons (CC BY 4.0) Rules

CC BY 4.0 permits redistribution, commercial use, and modifications, provided attribution (TASL) is present. Manifests must require TASL fields for each included item and keep license designations intact.[^6]

#### Creative Commons (CC BY-SA 3.0/4.0) Rules

ShareAlike requires that adaptations be licensed under the same CC BY-SA license. For Wikimedia-derived content and adaptations, manifests must enforce ShareAlike obligations and maintain attribution to original authors and platforms.[^7][^8]

#### All Rights Reserved (ARR) Rules

ARR content, typical of some third-party edtech platforms, prohibits redistribution and derivative works without explicit permission. Manifests should exclude ARR items by default and track any permission requests and outcomes in the licensing logs.[^2][^3]

#### Government Work Rules

Government works generally permit use with attribution to the issuing body. Manifests must include TASL-equivalent fields and preserve source credibility by citing official portals.[^4][^5]

#### Unknown/To Be Verified Rules

Until licensing is clarified, content must not be redistributed. Manifests should flag these items, record verification attempts, and update inclusion only upon confirmation.[^2]

## Manifest Design Specification

The manifests follow a structured schema with a top-level namespace, versioning, sources, metadata, compression, indexing, PWA integration, and compliance sections. YAML is used for human readability; JSON is provided for automated consumption. Naming conventions follow the pattern <bundle-name>-bundle.{yml,json}.

Fields at a minimum include:

- Namespace and versioning
- Sources (paths, license checks, inclusion/exclusion)
- Metadata (TASL fields; syllabus mapping where available)
- Compression settings (PDF optimization, ZIP handling, image normalization)
- Indexing (full-text and field-based indices; bilingual support)
- PWA integration (optional SW hints, caching, ETag support)
- Compliance (license class, permissions, audit trail)

### Table 5. Field Schema Summary

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| namespace | string | Yes | n/a | Identifier for bundle family |
| version | string | Yes | 1.0.0 | Semantic version for manifest |
| sources | list | Yes | n/a | Source entries with path globs and license checks |
| metadata | object | Yes | n/a | TASL fields, language, subject/topic, source platform |
| compression | object | Yes | sensible defaults | PDF optimization, ZIP handling, image normalization |
| indexing | object | Yes | n/a | Full-text, field-based indices, bilingual mapping |
| pwa | object | Optional | n/a | SW hints, caching, ETag guidance |
| compliance | object | Yes | n/a | License class, redistribution permissions, ShareAlike flags |
| build | object | Optional | n/a | Output naming, integrity checks, audit flags |

### Table 6. Compression Settings Matrix

| Content Type | Optimization Level | Licensing Constraints | Recommended Tooling |
|---|---|---|---|
| PDF | Medium to High | Preserve attribution metadata; do not strip TASL | Ghostscript or equivalent PDF optimizers |
| ZIP | Default | Do not modify license files inside archives | System unzip; validate internal license files |
| Images (PNG/JPG) | Medium | Avoid lossy recompression for CC BY-SA adaptations | ImageMagick with无损 settings |
| HTML | Default | Maintain license notices and source links | HTML minifiers without altering TASL |
| JSON | Default | Preserve license fields | JSON compressors without schema changes |

#### Compression and Normalization

PDFs are optimized to reduce payload while preserving attribution metadata and license notices. ZIPs are unpacked when necessary for indexing and compliance checks; internal license files are retained and exposed to the indexer. Images are normalized to reduce size without altering license-critical artifacts. HTML and JSON content are cleaned for consistency without removing TASL information.

#### Indexing and Metadata Enrichment

Indexing combines full-text search with field-based indexing for title, subject, topic, license, language, source, and year. Metadata is enriched from available inventories and catalogs. Licensing fields are indexed to support compliance audits and search filtering.

## Bundle Manifest Authoring Plan

The plan is to author six manifests as both YAML and JSON. Each manifest encodes source globs, license checks, inclusion/exclusion rules, compression settings, and indexing strategies. The build process validates compliance via automated checks and flags items for holdback if licensing is unclear or restricted.

### Table 7. Per-Bundle Source Glob and License Mapping

| Bundle | Source Path Globs | License Class | Include? | Notes |
|---|---|---|---|---|
| previous-papers | /workspace/content/rrb-ntpc/previous-papers/CBT1/**; /workspace/content/rrb-ntpc/previous-papers/CBT2/** | Government Work | Yes | Verify government attribution and source URLs.[^4][^5] |
| mathematics-foundations | /workspace/diksha-math/study-materials/oer/**; /workspace/content/rrb-ntpc/study-materials/oer/**; /workspace/content/rrb-ntpc/study-materials/wikimedia/** | CC BY 4.0; CC BY-SA | Yes | CC BY for DIKSHA math; CC BY-SA for Wikimedia (share-alike).[^1][^9][^10] |
| reasoning-complete | /workspace/diksha-reasoning/downloaded_content/** | CC BY 4.0; Unknown/ARR | Conditional | Include CC BY items; exclude Unknown/ARR unless permission.[^1][^2] |
| general-science | /workspace/diksha-ga/science-technology/** | CC BY 4.0 | Yes | NCERT science; include TASL.[^1] |
| general-awareness | /workspace/diksha-ga/current-affairs/**; /workspace/diksha-ga/polity/**; /workspace/diksha-ga/geography/**; /workspace/diksha-ga/indian-history/**; /workspace/diksha-ga/static-gk/**; /workspace/diksha-ga/economy/** | CC BY 4.0; Government Work | Conditional | Include CC BY and Government Work; hold back Unknown/ARR.[^1][^4][^5] |
| practice-sets | /workspace/practice-ga/<subject>/**; /workspace/content/rrb-ntpc/practice-sets/** | CC BY 4.0; Government Work; ARR | Conditional | Include CC BY/Gov Work; exclude ARR without permission.[^2][^3] |

### Bundle 1: previous-papers (CBT1/CBT2)

The previous-papers bundle is scoped strictly to official RRB/NTPC CBT1/CBT2 papers under Government Work licensing. The manifest defines source globs for CBT1 and CBT2 directories, ensures attribution to the issuing body, and confirms source URLs. This bundle excludes third-party ARR materials. Compression optimizes PDFs while preserving attribution metadata, and indexing includes exam stage, year, and subject fields to facilitate targeted retrieval.[^4]

### Bundle 2: mathematics-foundations (DIKSHA + Wikimedia math)

This bundle integrates DIKSHA NCERT mathematics (CC BY 4.0) with targeted Wikimedia math content (CC BY-SA). ShareAlike obligations are explicitly encoded: adaptations must remain under CC BY-SA. The manifest enables bilingual indexing where available, and includes metadata fields for grade level, topic, and source platform. Indexing includes formulas and topic tags to support concept search and syllabus alignment.[^1][^9][^10]

### Bundle 3: reasoning-complete

The reasoning bundle consolidates DIKSHA reasoning content across logical, verbal, non-verbal, and mental ability modules. Licensing filters exclude Unknown/ARR materials unless permissions are secured; only CC BY 4.0 items from DIKSHA are included by default. Indexing focuses on skill type, subtopic, difficulty, and source, with metadata capturing category and language. The compliance section records any permission requests or verification outcomes before inclusion.[^1][^2]

### Bundle 4: general-science

General science is anchored in DIKSHA GA NCERT materials (CC BY 4.0), including physics, chemistry, and biology PDFs/ZIPs. The manifest requires TASL attribution and includes subject and language fields. Indexing captures topic and source, with PDFs marked for full-text extraction while preserving license metadata.[^1]

### Bundle 5: general-awareness

This bundle spans current affairs, polity, geography, Indian history, static GK, and economy from DIKSHA GA. It includes Government Work sources where applicable, but excludes Unknown/ARR materials by default. Indexing emphasizes category and date fields for current affairs, with bilingual support for Hindi and English. Source URLs and attribution are enforced throughout.[^1][^4][^5]

### Bundle 6: practice-sets

Practice sets aggregate exercises across subjects, with strict inclusion rules: only CC BY 4.0 or Government Work items are included; ARR sets are excluded unless written permission exists. The manifest records permission status, and indexing includes subject, difficulty, and source fields to aid practice workflows. Third-party ARR items are tracked for potential future inclusion if permissions materialize.[^2][^3]

## Build and Packaging Workflow

The build pipeline reads manifests, resolves source globs, validates licenses, enriches metadata, applies compression, builds indices, and produces OpenZIM outputs alongside audit artifacts. Integrity is enforced through checksums and licensing audit logs. Each build is versioned, and outputs are validated against the schema before release.

### Table 8. Build Steps and Validation Gates

| Step | Inputs | Outputs | Validation | Gate/Policy |
|---|---|---|---|---|
| Read manifests | YAML/JSON manifests | Resolved source list | Schema check (fields present) | Must pass schema validation |
| Validate licensing | License register mapping | Compliance report per item | License class, permissions, attribution presence | Exclude Unknown/ARR unless permission |
| Metadata enrichment | Catalogs/inventories | TASL fields, language, subject | TASL completeness, language mapping | No release without TASL |
| Compression | Content files | Optimized assets | Attribution retention, license notices preserved | No stripping of license info |
| Indexing | Content + metadata | Full-text and field-based indices | Index completeness | Coverage threshold must be met |
| Packaging | Indices + assets | OpenZIM bundle | Integrity checksums | Checksums recorded |
| Compliance audit | Build artifacts | Audit logs | License register alignment | Quarterly review cadence |
| Release | Validated bundle | Versioned artifact | Final sign-off | Only compliant bundles released |

## PWA Integration for Offline-First Usage

Offline-first behavior is achieved through manifest-driven PWA hints: optional Service Worker registration hooks, cache-first strategies for core assets, and content freshness indicators via ETag support and update cadence fields. Index design supports offline search across title, subject, topic, license, language, source, and year. Navigation emphasizes bilingual access and subject hierarchies aligned to competitive exams, ensuring intuitive browsing even without network connectivity.

## Compliance Verification and Audit

Compliance verification is integral to build governance. Automated checks validate TASL fields for CC items, ensure ShareAlike enforcement for Wikimedia-derived content, and confirm attribution for Government Work items. Unknown/ARR items are flagged, held back, and tracked through permission workflows. The audit process produces licensing logs, verification status, and a monthly compliance dashboard, with quarterly assessments for deeper review and renewal of permissions as needed.[^2]

![Distribution of content credibility and licensing signals](audit/credibility_distribution.png)

This distribution visual highlights the predominance of credible sources (government portals, DIKSHA/NCERT, Wikimedia) that are suitable for default inclusion under correct attribution, contrasted with ARR-heavy third-party portals that require permission or exclusion. The insight reinforces the importance of strict license filtering and well-maintained source catalogs.

### Table 9. Compliance Audit Checklist

| Item | Frequency | Outcome |
|---|---|---|
| Attribution completeness (TASL) | Monthly | All CC BY items carry TASL; no release without it |
| ShareAlike enforcement | Monthly | Wikimedia adaptations remain CC BY-SA |
| Government attribution | Monthly | Issuing body cited; source URLs preserved |
| ARR exclusion/permissions | Monthly | No redistribution without written permission |
| Unknown/To Be Verified | Monthly | Items held back; verification attempts recorded |
| Source catalog updates | Quarterly | Credible source list reviewed and refreshed |
| Permission renewals | Quarterly | Documented and tracked |
| Legal policy monitoring | Quarterly | License register and platform policies reviewed |

## Risks, Constraints, and Mitigations

Licensing ambiguity and redistribution prohibitions present the most significant risks. Third-party ARR materials dominate many practice set ecosystems and cannot be redistributed without explicit permission. DIKSHA policy variability and occasional access issues further complicate verification. Wikimedia’s ShareAlike requirement imposes additional obligations on derivatives, which must be enforced at the manifest level.[^3][^2]

Mitigations include strict license filtering, holdback of Unknown/ARR content, formal permission requests with documentation, robust attribution, and scheduled compliance reviews. The build system must record license checksums and produce an auditable trail.

### Table 10. Risk Register

| Risk | Source | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|---|
| ARR redistribution violation | Third-party edtech portals | Legal action, takedown | Medium | Exclude ARR; obtain written permissions | Legal/Content Ops |
| License ambiguity | Unclear platform policies | Delayed releases | Medium | Hold back; verify; document attempts | Compliance |
| ShareAlike non-compliance | Wikimedia adaptations | License breach | Low | Enforce CC BY-SA at manifest; audits | Compliance |
| DIKSHA access variability | Platform constraints | Verification delays | Medium | Maintain mirrors; document access attempts | Content Ops |
| Attribution omissions | Human error | License breach | Low | Automated TASL checks | Build Eng |
| Metadata inconsistency | Mixed inventories | Search gaps | Medium | Enrichment pipeline; schema validation | Build Eng |

## Implementation Timeline and Work Plan

The plan advances in discrete phases: schema finalization, manifest authoring, validation, build trial, compliance audit, and release. Ownership spans content curation, compliance, and build engineering. Checkpoints ensure licensing audits and source verifications conclude before release.

### Table 11. Milestone Plan

| Phase | Tasks | Dependencies | Outputs | Acceptance Criteria |
|---|---|---|---|---|
| Schema design | Define field schema, defaults | License register | Manifest schema v1 | Approved schema |
| Authoring | Create 6 YAML + 6 JSON manifests | Schema | Draft manifests | Complete source globs and compliance fields |
| Validation | Schema checks, license mapping | Authoring | Validation report | No schema errors; clear license flags |
| Build trial | Generate test bundles | Validation | Trial ZIM artifacts | Indices and compression verified |
| Compliance audit | Run audit checklist | Build trial | Audit log and dashboard | No critical violations |
| Release | Finalize and version bundles | Audit | Release candidates | Signed-off compliant bundles |

## Appendices

### Appendix A: YAML/JSON Field Dictionary

The following table enumerates core fields, descriptions, and example values to standardize manifest authoring.

| Field | Description | Example Value |
|---|---|---|
| namespace | Bundle family identifier | general-awareness |
| version | Manifest semantic version | 1.0.0 |
| sources | List of source entries with path globs and license checks | { path: “/workspace/diksha-ga/polity/**”, license: “CC BY 4.0” } |
| metadata | TASL fields, language, subject/topic | { title: “…”, author: “NCERT”, source: “DIKSHA”, license: “CC BY 4.0”, language: “en/hi” } |
| compression | Content-type specific optimization rules | { pdf: “medium”, zip: “default”, images: “lossless” } |
| indexing | Full-text and field-based index configuration | { full_text: true, fields: [“title”, “subject”, “license”] } |
| pwa | Optional SW hints and caching guidance | { sw_hint: “register”, cache: “cache-first” } |
| compliance | License class, permissions, ShareAlike flags | { license: “CC BY-SA”, share_alike: true } |
| build | Output naming, integrity checks, audit flags | { artifact: “general-awareness-bundle.zim”, checksum: “sha256” } |

### Appendix B: Sample Manifest Snippets

Sample YAML structure (illustrative):

- namespace: mathematics-foundations
- version: 1.0.0
- sources:
  - path: /workspace/diksha-math/study-materials/oer/**
    license: CC BY 4.0
    attribution_required: true
  - path: /workspace/content/rrb-ntpc/study-materials/wikimedia/**
    license: CC BY-SA 4.0
    share_alike_required: true
- metadata:
    title:_required
    author:required
    source:required
    license:required
    language:[en, hi]
- compression:
    pdf:medium
    images:lossless
- indexing:
    full_text:true
    fields:[title, subject, topic, license, language, source, year]
- compliance:
    license:CC BY 4.0 or CC BY-SA 4.0
    share_alike:(as applicable)
- build:
    artifact:mathematics-foundations-bundle.zim
    checksum:sha256

### Appendix C: Source Catalog and License Register References

- Consolidated license register entries for DIKSHA (NCERT), Wikimedia, Government works, and ARR/edtech sources.
- Credible portals catalog documenting access status, policy clarity, and redistribution constraints.

## Information Gaps

Certain details require future resolution to finalize indexing strategies and PWA hints:

- Precise per-asset licensing for all items within diksha-reasoning and practice-ga is not fully enumerated and may include Unknown/ARR categories; manifests hold back such items until verified.
- Local paths for wikimedia-*/math are implied via study-materials/wikimedia/ but not listed in the provided directories; validation is required during build.
- The content_inventory.json schema and fields need confirmation to finalize metadata enrichment mappings.
- File-format distributions (PDF vs HTML vs JSON) per bundle are not quantified; defaults will be adjusted after inventory sampling.
- Wikimedia math coverage depth (topics, languages, license variants) requires validation prior to finalizing indexing scope and ShareAlike enforcement.
- PWA Service Worker file paths and caching strategies are not provided; manifests will include optional hints only.
- Some third-party sources list access restrictions and unclear redistribution policies; permissions or holdback decisions are pending.

## References

[^1]: DIKSHA - National Digital Infrastructure for Teachers. https://diksha.gov.in/
[^2]: Wikimedia Foundation. https://www.wikimedia.org/
[^3]: Railway Recruitment Boards (Official Portal). https://www.rrb.gov.in/
[^4]: Creative Commons Attribution 4.0 International (CC BY 4.0). https://creativecommons.org/licenses/by/4.0/
[^5]: Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0). https://creativecommons.org/licenses/by-sa/3.0/
[^6]: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0). https://creativecommons.org/licenses/by-sa/4.0/
[^7]: Wikipedia: World Wide Web. https://en.wikipedia.org/wiki/World_Wide_Web.
[^8]: Wikipedia: JavaScript. https://en.wikipedia.org/wiki/JavaScript.
[^9]: Wikibooks: Programming Languages. https://en.wikibooks.org/wiki/Programming_Languages.
[^10]: Wikibooks: HTML Programming. https://en.wikibooks.org/wiki/HTML_Programming.
[^11]: Wikipedia: Computer programming. https://en.wikipedia.org/wiki/Computer_programming.
[^12]: Wikipedia: Open source software. https://en.wikipedia.org/wiki/Open_source_software.
[^13]: Wikibooks: Introduction to Programming. https://en.wikibooks.org/wiki/Introduction_to_Programming.
[^14]: Wikibooks: Web Development. https://en.wikibooks.org/wiki/Web_Development.
[^15]: Wikipedia: Web development. https://en.wikipedia.org/wiki/Web_development.
[^16]: Wikipedia: Database management system. https://en.wikipedia.org/wiki/Database_management_system.
[^17]: Testbook Edutech Pvt Ltd. https://testbook.com/
[^18]: Mockers.in Educational Platform. https://www.mockers.in/
[^19]: Jagran Josh. https://www.jagranjosh.com/