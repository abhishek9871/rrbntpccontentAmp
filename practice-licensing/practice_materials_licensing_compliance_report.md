# Practice Materials Licensing and Redistribution Compliance Blueprint (RRB NTPC Focus)

## Executive Summary and Objectives

This blueprint establishes a single, authoritative framework for auditing and documenting the licensing and redistribution permissions of practice materials relevant to Railway Recruitment Board Non-Technical Popular Categories (RRB NTPC) preparation. It translates complex platform-specific terms into actionable policy, standardized attribution rules, and operational controls that can be implemented immediately.

Three licensing families govern the reuse landscape. First, open educational resources (OER) sourced through DIKSHA—India’s national platform for school education—are primarily licensed under Creative Commons Attribution 4.0 International (CC BY 4.0), enabling reuse and redistribution with attribution, including for commercial purposes.[^1][^2][^3][^4] Second, Wikimedia text from Wikipedia and Wikibooks is generally governed by Creative Commons Attribution–ShareAlike (CC BY‑SA)—with historical content under CC BY‑SA 3.0 and page revisions after mid‑2023 under CC BY‑SA 4.0—requiring attribution and share‑alike obligations for adaptations.[^5][^6][^7][^8][^9] Third, commercial test-prep platforms (e.g., Jagran Josh, Unacademy, Oliveboard, Testbook, Mockers) assert all rights reserved or restrict reuse to personal access only; redistribution and derivative uses typically require prior written permission.[^11][^14][^15][^17][^21]

Top-line findings:
- DIKSHA/NCERT content is broadly reusable with attribution, subject to CC BY 4.0 obligations.[^1][^2][^3][^4]
- Wikimedia text is reusable with attribution and share‑alike for adaptations; media assets require per‑file license verification.[^5][^6][^9][^25]
- Most commercial practice portals do not permit redistribution or derivative use without explicit permission; some allow personal use only or are gated by login/subscription.[^11][^14][^15][^17][^21][^22]

Key deliverables:
- A canonical CSV license register for all practice materials (content_title, source_portal, license_type, redistribution_permissions, usage_restrictions, required_attribution, compliance_status).
- A ready-to-use attribution guide with templates aligned to CC BY 4.0 and CC BY‑SA (3.0/4.0), and platform-specific notes for commercial portals.
- A compliance status matrix and gating rules for redistribution (Proceed, Permission Required, Restricted, Unknown), with audit trails and periodic reconciliation.

The blueprint also highlights policy access gaps (e.g., Adda247 and others blocked by CloudFront) and incomplete per‑file provenance for certain portal downloads, setting out concrete steps to close them.

## Scope of Practice Materials and Collection Overview

The scope covers five primary categories: practice sets, mock tests, previous year question papers, chapter-wise tests, and study notes. The content inventory spans:
- DIKSHA/NCERT OER (e.g., general awareness, mathematics, science, history, polity, geography).
- RRB NTPC official notices and previous papers (government works).
- Wikimedia text and media reused in study materials (Wikipedia/Wikibooks).
- Third-party practice platforms offering mock tests, practice sets, and question banks (e.g., Mockers, Jagran Josh, Unacademy, Oliveboard, Testbook; with Adda247 and others partially inaccessible).

Government official materials—syllabus pages, notices, and previous papers—are accessible via RRB portals and official exam pages.[^19][^20] Practice content and access flows are visible for Mockers, which offers mock tests, practice sets, MCQ tests, chapter-wise tests, and previous year papers; access requires registration and login.[^21][^22] Policy documents for several commercial portals restrict redistribution, or were not accessible at the time of review due to CloudFront protection (e.g., Adda247).[^10][^11][^14][^15][^17]

To illustrate the breadth and characteristics of the collection, Table 1 summarizes representative items by category and source.

Table 1. Collection inventory summary (illustrative)

| Content Category | Source Portal (Example) | Material Type | Access Constraints | Notes |
|---|---|---|---|---|
| General Awareness (GA) | DIKSHA/NCERT | Textbooks, study notes | Open (web) | OER; CC BY 4.0 attribution required[^1][^2][^3][^4] |
| Mathematics | DIKSHA/NCERT | Textbooks, practice sheets | Open (web) | OER; CC BY 4.0 attribution required[^1][^2][^3][^4] |
| General Science | DIKSHA/NCERT | Textbooks, notes | Open (web) | OER; CC BY 4.0 attribution required[^1][^2][^3][^4] |
| History / Polity / Geography | DIKSHA/NCERT | Textbooks, notes | Open (web) | OER; CC BY 4.0 attribution required[^1][^2][^3][^4] |
| RRB NTPC Previous Papers | RRB portals | Previous year question papers | Open (web) | Government works; use with official attribution[^19][^20] |
| RRB NTPC Notices | RRB portals | Official notices, syllabi | Open (web) | Government communications; attribution to the issuing RRB[^19][^20] |
| Mock Tests / Practice Sets | Mockers | Online tests (CBT‑1/CBT‑2) | Registration required | No redistribution without permission[^21][^22][^23] |
| Study Notes / Practice Content | Jagran Josh, Unacademy, Oliveboard, Testbook | PDFs, notes, tests | Varies; often gated | Personal/non-commercial only; redistribution restricted[^11][^14][^15][^17] |
| Wikimedia Text | Wikipedia/Wikibooks | Text pages | Open | CC BY‑SA; attribution + share‑alike for adaptations[^5][^6][^7][^8][^9][^26] |
| Media (images, diagrams) | Wikimedia Commons | Non-text files | Open (per file) | Per‑file license verification required[^9][^25] |

The collection resides across OER repositories (DIKSHA), government portals (RRB sites), commercial practice portals, and Wikimedia-based study materials. A consolidated manifest—including per‑file provenance, source URL, license, and access constraints—will be maintained in the license register.

## Methodology and Audit Workflow

The audit workflow operationalizes consistent, defensible compliance across heterogeneous sources. The process is designed to be repeatable, with strict provenance capture and validation:

1. Inventory and provenance capture. For each item, record the exact title, source portal (e.g., DIKSHA, Mockers, RRB portal), and a stable source URL. If a revision ID is available (e.g., Wikimedia), capture it to tie obligations to the correct license version. Record the date of download or extraction.
2. License verification. Identify the license type: CC BY 4.0 for DIKSHA/NCERT OER; CC BY‑SA (3.0 or 4.0) for Wikimedia text; All Rights Reserved or restricted terms for commercial portals; Government work status for official RRB materials.[^1][^5][^11][^14][^15][^17][^19][^20]
3. Attribution extraction. Draft attribution text that will be shipped with the content (title, author/organization, source, license, changes if adapted).
4. Redistribution determination. Assess whether redistribution is permitted (open license), permitted only with permission (commercial portals), or restricted (e.g., login-gated, personal use only).
5. QA verification. Check that attribution meets the license requirements and that any platform-specific restrictions are respected.
6. Documentation and register update. Record the outcome in the CSV license register and attribution guide; append any necessary license notices.
7. Periodic reconciliation. Re-check source pages periodically (e.g., for Wikimedia license transitions or portal policy updates) and update the register to reflect changes.

This workflow is supplemented by a per-file manifest for non-text media (images, audio, video) on Wikimedia Commons or embedded in portals, applying the Definition of Free Cultural Works and verifying licenses on each description page.[^9][^25] Restrictions in platform terms (e.g., prohibitions on downloading, screen recording, or scraping) must be respected.[^24]

Table 2. Audit steps mapped to evidence and ownership

| Audit Step | Evidence Captured | Owner | Status |
|---|---|---|---|
| Inventory & provenance | Title, Source URL, Download/Extraction date | Content Ops | In progress |
| License verification | License type (CC BY 4.0, CC BY‑SA 3.0/4.0, ARR, Government) | Licensing PM | In progress |
| Attribution drafting | Attribution text (TASL + Changes) | Content Ops | In progress |
| Redistribution assessment | Allowed/Restricted/Permission required | Legal | In progress |
| QA verification | Attribution completeness, license notice presence | QA | Pending |
| Register update | CSV record completion | Licensing PM | Pending |
| Reconciliation cadence | Scheduled checks (e.g., quarterly) | PMO | Planned |

## Licensing Foundations and Policy Analysis

Two licensing regimes underpin most open practice content, complemented by platform-specific terms for commercial portals and special handling for government works.

### OER (DIKSHA/NCERT): CC BY 4.0

DIKSHA is the national digital infrastructure for school education content and is widely used to host OER developed by NCERT and other government partners.[^1][^2][^3][^4] DIKSHA/NCERT content is primarily licensed under CC BY 4.0, which permits reuse, adaptation, and redistribution—including for commercial use—provided attribution is given.[^1] Attribution should follow Creative Commons’ TASL model (Title, Author, Source, License), disclose modifications, and avoid implying endorsement.[^27]

Table 3. CC BY 4.0 quick reference

| Element | Practical Reuse Implication | Required Action |
|---|---|---|
| Attribution | Credit the original creator/organization | Apply TASL; include title, author, source, license |
| Reuse | Copy verbatim for educational purposes | Allowed with attribution |
| Revise | Adapt and edit content | Allowed; disclose changes |
| Remix | Combine with other educational content | Allowed; track attributions per component |
| Redistribute | Share with attribution | Allowed; include license name and notice |
| Commercial use | Permitted with attribution | Allowed; include attribution and license |

### Wikimedia: CC BY‑SA 3.0 vs 4.0

Wikimedia projects historically licensed textual content under CC BY‑SA 3.0, then transitioned to CC BY‑SA 4.0 in June 2023.[^5][^6] Obligations differ slightly across versions:
- Attribution: CC BY‑SA 3.0 requires Title; CC BY‑SA 4.0 makes Title optional but still recommends it.[^5][^6][^27]
- Share‑alike: Adaptations must be licensed under CC BY‑SA (same license elements, this version or later), with license notices included in distributions.[^5][^6]
- Media: Non-text media carry their own licenses and must be verified on their description pages; Commons requires free licenses or public domain dedication.[^9][^25]

Table 4. CC BY‑SA 3.0 vs 4.0: differences impacting reuse

| Dimension | CC BY‑SA 3.0 | CC BY‑SA 4.0 | Impact |
|---|---|---|---|
| Title in attribution | Required | Optional (recommended) | Slight template adjustment |
| License notice | Copy/URI required | Copy/URI required | Consistent requirement |
| Share‑alike scope | Adaptations under BY‑SA 3.0 or compatible ports | Adaptations under BY‑SA 4.0 (or later) | Version specificity matters |
| Compatibility | Later versions with same elements | CC‑approved compatible licenses | Formalized compatibility process |

### Commercial Portals: All Rights Reserved / Personal Use Only

Several commercial portals assert all rights reserved or restrict use to personal/non-commercial contexts, prohibiting redistribution, derivative works, or bulk copying without prior written consent.

- Jagran Josh grants personal, non‑commercial use only; reproduction, transmission, derivative use, or inclusion in other works is prohibited without permission; attribution notices must not be removed.[^11]
- Unacademy grants users a limited, non‑transferable, personal license; prohibits distribution of platform content and derivative exploitation without prior written authorization.[^14]
- Oliveboard asserts exclusive ownership over platform compilations and proprietary information; prohibits copying, downloading, or commercial exploitation without consent.[^15]
- Testbook’s terms restrict unauthorized copying and distribution of content; reuse likely requires permission.[^17]
- Mockers provides free tests after registration; while “free” is advertised, redistribution is not permitted without permission; terms of use were not accessible during extraction.[^21][^22][^23]

Table 5. Platform policy matrix (selected portals)

| Portal | Licensing Posture | Redistribution | Derivative Use | Commercial Use | Registration/Gating |
|---|---|---|---|---|---|
| Jagran Josh | All Rights Reserved | Prohibited without consent | Prohibited without consent | Prohibited | Open access; personal use only[^11] |
| Unacademy | All Rights Reserved; limited personal license | Prohibited without consent | Prohibited without consent | Prohibited without consent | App/registration; content controlled[^14] |
| Oliveboard | All Rights Reserved | Prohibited without consent | Prohibited without consent | Prohibited without consent | Login/subscription; controlled access[^15] |
| Testbook | All Rights Reserved | Prohibited without consent | Prohibited without consent | Prohibited without consent | Registration; controlled access[^17] |
| Mockers | All Rights Reserved (ToU inaccessible) | Prohibited without consent | Prohibited without consent | Prohibited without consent | Registration required[^21][^22][^23] |
| Adda247 | Policy inaccessible (403) | Unknown | Unknown | Unknown | CloudFront‑blocked; unknown[^10] |

### Government Works (RRB Official Materials)

RRB official notices and previous papers are government communications. While generally free for public access, reuse typically requires proper attribution to the issuing board and adherence to portal terms. RRB portals often include links to outside sites; users are subject to the privacy and security policies of those external owners when following outbound links.[^19][^20]

Table 6. Government works handling

| Material Type | License Status | Attribution | Notes |
|---|---|---|---|
| Official notices / syllabi | Government communications | Attribute issuing RRB/zone | Respect portal terms and linked policies[^19] |
| Previous papers | Government exam materials | Attribute RRB/zone | Use per portal terms; confirm any download restrictions[^20] |

### License Comparison Matrix

To highlight the practical differences across license families:

Table 7. License comparison

| License | Attribution | Redistribution | Derivatives | Commercial Use | Notes |
|---|---|---|---|---|---|
| CC BY 4.0 | Required (TASL) | Allowed | Allowed | Allowed | Disclose changes; no endorsement implied[^1][^27] |
| CC BY‑SA 3.0 | Required (Title required) | Allowed | Share‑alike required | Allowed | Include license copy/URI with distributions[^5] |
| CC BY‑SA 4.0 | Required (Title optional) | Allowed | Share‑alike required | Allowed | Transition applies to post‑June 2023 revisions[^6] |
| All Rights Reserved | Owner controls | Requires permission | Requires permission | Requires permission | Personal use only common; no redistribution[^11][^14][^15][^17] |
| Government Works | Attribute source | Typically allowed | Typically allowed | Typically allowed | Check portal terms for specifics[^19][^20] |

## Redistribution and Usage Rules by Source

The rules below synthesize licensing foundations with platform terms and our policy posture.

- DIKSHA/NCERT (CC BY 4.0). Reuse, remix, and redistribution are permitted with attribution. Commercial use is allowed. Maintain attribution notices and disclose changes.[^1][^27]
- Wikimedia (CC BY‑SA 3.0/4.0). Unmodified text may be reused with attribution; adaptations must be licensed under CC BY‑SA (same license elements), with license notices included. Per‑file media licenses must be verified and respected.[^5][^6][^9][^25][^26]
- Jagran Josh. Personal use only; no redistribution, derivative works, or commercial exploitation without prior consent; attribution notices must not be removed.[^11]
- Unacademy. Users receive a limited, non‑transferable, personal license; distribution or derivative exploitation of platform content requires prior written authorization.[^14]
- Oliveboard. Exclusive ownership over compilations; prohibits copying, downloading, modifying, republishing, or commercial exploitation without consent.[^15]
- Testbook. Terms restrict copying and distribution; redistribution requires permission.[^17]
- Mockers. Access requires registration; while “free” content is advertised, redistribution without permission is not allowed; terms of use were inaccessible during extraction.[^21][^22][^23]
- RRB official materials. Government communications; attribution to the issuing RRB/zone is required; check portal terms for downloads or links to external sites.[^19][^20]
- Adda247 and similar blocked portals. Access to terms was blocked (403); status remains unknown pending policy extraction.[^10]

Table 8. Redistribution posture by source

| Source | Allowed | Restricted | Permission Required | Unknown |
|---|---|---|---|---|
| DIKSHA/NCERT | Yes (with attribution) | — | — | — |
| Wikimedia text | Yes (with attribution) | — | SA for adaptations | — |
| Jagran Josh | — | Yes | Yes | — |
| Unacademy | — | Yes | Yes | — |
| Oliveboard | — | Yes | Yes | — |
| Testbook | — | Yes | Yes | — |
| Mockers | — | Yes | Yes | — |
| RRB official | Yes (with attribution) | — | — | — |
| Adda247 | — | — | — | Yes |

## Attribution Requirements and Templates

Attribution must be complete, clear, and visible to the recipient. The following guidance and templates align with Creative Commons best practices and incorporate platform-specific notes.

Principles:
- Apply TASL—Title, Author, Source, License—supplemented with Changes for any adaptation.[^27]
- Use ready-to-ship credit blocks per content type; include license notices.
- Avoid implying endorsement by the licensor or platform.

Table 9. Attribution elements by content type

| Content Type | Required Fields | Placement Guidance |
|---|---|---|
| DIKSHA/NCERT (CC BY 4.0) | Title, Author (e.g., NCERT), Source (DIKSHA), License (CC BY 4.0), Changes (if any) | Credits page or footer; include license notice[^1][^27] |
| Wikimedia text (CC BY‑SA) | Title (3.0 required; 4.0 recommended), Authors (contributors), Source (page URL + revision ID), License (CC BY‑SA 3.0/4.0), Changes | Credits page; include SA license notice[^5][^6][^27] |
| RRB official | Title, Issuing Board/Portal, Source (official page), Changes (if any) | Credits page; note government source attribution[^19][^20] |
| Commercial portals (ARR) | Title, Platform name, Source (platform page), License (All Rights Reserved), Changes (if any) | Credits page; add “Used with permission” or “Redistribution not permitted”[^11][^14][^15][^17] |

Templates (ready-to-use):

1) DIKSHA/NCERT—Unmodified
- Title: {content_title}
- Author: {author_or_publisher} (e.g., NCERT)
- Source: DIKSHA Platform
- License: CC BY 4.0
- Changes: None

2) DIKSHA/NCERT—Adapted
- Title: {content_title}
- Author: {author_or_publisher} (e.g., NCERT)
- Source: DIKSHA Platform
- License: CC BY 4.0
- Changes: {summary of edits, translations, or remixes}

3) Wikimedia—Unmodified (CC BY‑SA 3.0)
- Title: {page_title}
- Authors: Contributors
- Source: {page_URL}, revision {revision_id}
- License: CC BY‑SA 3.0
- Changes: None
- Notice: This work is provided under CC BY‑SA 3.0; include license copy/URI.

4) Wikimedia—Adapted (CC BY‑SA 4.0)
- Title: {page_title}
- Authors: Contributors
- Source: {page_URL}, revision {revision_id}
- License: CC BY‑SA 4.0
- Changes: {summary of edits/translations}
- Notice: Adaptations must be licensed under CC BY‑SA 4.0; include license copy/URI.

5) RRB Official
- Title: {document_title}
- Author/Source: {RRB zone/board}
- Source: {official_page_URL}
- License: Government work (used with attribution)
- Changes: {if any}
- Note: Attribute the issuing RRB; follow portal terms.

6) Commercial Portal (Personal Use Only)
- Title: {content_title}
- Author/Source: {platform_name}
- Source: {platform_page_URL}
- License: All Rights Reserved
- Changes: {if any}
- Note: Used with permission for personal, non‑commercial use. Redistribution and derivative uses require prior written consent.

For constrained formats (e.g., social media), place attribution near the content (caption or comment) and include the license designation; do not rely solely on metadata fields.[^28]

## Compliance Status Matrix and Decision Framework

Compliance statuses:
- Compliant: Open license content with complete attribution and correct license notices.
- Permission Required: Commercial portal content where redistribution is prohibited without consent.
- Restricted: Content subject to strict personal/non‑commercial or no‑redistribution terms.
- Unknown: Policy inaccessible or per‑file license verification pending.

Table 10. Compliance status by source

| Source | Status | Conditions | Next Action |
|---|---|---|---|
| DIKSHA/NCERT | Compliant | CC BY 4.0 attribution required | Ship attribution; include license notice[^1] |
| Wikimedia text | Compliant | Attribution + share‑alike for adaptations | Verify revision; apply SA license to adaptations[^5][^6] |
| Jagran Josh | Restricted | Personal use only; no redistribution | Do not redistribute without consent[^11] |
| Unacademy | Restricted | Limited personal license; no distribution | Do not redistribute without consent[^14] |
| Oliveboard | Restricted | Proprietary content; no copying | Do not redistribute without consent[^15] |
| Testbook | Restricted | Terms restrict copying/distribution | Do not redistribute without consent[^17] |
| Mockers | Restricted | Registration required; ToU inaccessible | Do not redistribute without permission[^21][^22][^23] |
| RRB official | Compliant | Attribution to issuing RRB | Include official attribution; follow portal terms[^19][^20] |
| Adda247 | Unknown | Access blocked (403) | Retry extraction; contact platform[^10] |

Decision flow for redistribution:
- Is the content openly licensed (e.g., CC BY 4.0, CC BY‑SA)?
  - Yes: Proceed if attribution is complete; for CC BY‑SA adaptations, apply share‑alike and include license notices.
- Is the content from a commercial portal?
  - Yes: Permission Required—seek written consent or refrain from redistribution.
- Is the policy inaccessible or ambiguous?
  - Yes: Unknown—do not redistribute until verified; attempt alternate access or direct contact.

## Risk Assessment and Mitigation

Three risk categories dominate:

1) Copyright and licensing risk. Redistributing All Rights Reserved content without permission exposes the organization to takedown demands and legal action. Mitigation: Limit use to personal study contexts; obtain permissions in writing; rely primarily on OER (CC BY) and CC BY‑SA content for redistribution.[^11][^14][^15][^17]

2) Share‑alike obligations. When adapting CC BY‑SA text, failing to license the adaptation under CC BY‑SA or to include license notices creates non‑compliance. Mitigation: Maintain per‑file provenance, revision IDs, and adaptation logs; apply CC BY‑SA to adapted text and include license copies/URIs.[^5][^6]

3) Terms of service constraints. Platform terms often prohibit scraping, screen recording, or automated downloading; violating these terms can lead to access revocation or legal claims. Mitigation: Respect platform TOS; avoid automated extraction where prohibited; prefer official APIs or open licenses.[^24]

Table 11. Risk register (illustrative)

| Risk Category | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Redistributing ARR content | Medium | High | Permission workflow; restrict to personal use | Legal |
| Failing SA obligations | Medium | High | Apply SA to adaptations; include license notices | Licensing PM |
| TOS violations (scraping) | Medium | Medium | Respect TOS; use official access paths | Content Ops |
| Unknown policies (blocked) | Medium | Medium | Retry via alternate access; contact portals | PMO |
| Per‑file media license gaps | Medium | Medium | Verify licenses on description pages | Content Ops |

## Implementation Plan and Deliverables

Deliverables:
- /metadata/practice_materials_license_register.csv: canonical register of all practice items.
- /metadata/practice_materials_attribution_guide.md: ready-to-use attribution templates and guidance.

CSV schema (minimum fields):
- content_title
- source_portal
- license_type
- redistribution_permissions
- usage_restrictions
- required_attribution
- compliance_status

Recommended extended fields:
- source_url
- author/organization
- license_version (e.g., CC BY‑SA 3.0 vs 4.0)
- revision_id (Wikimedia)
- download_date
- attribution_text
- adaptation_notes
- media_license_summary (for non‑text assets)

Table 12. CSV schema specification

| Column | Type | Required | Description |
|---|---|---|---|
| content_title | string | Yes | Title of the practice item |
| source_portal | string | Yes | Platform or portal name |
| license_type | string | Yes | License family (e.g., CC BY 4.0, CC BY‑SA 3.0, ARR) |
| redistribution_permissions | string | Yes | Allowed/Restricted/Permission Required |
| usage_restrictions | string | Yes | Personal/non‑commercial; share‑alike; etc. |
| required_attribution | string | Yes | TASL + Changes guidance |
| compliance_status | string | Yes | Compliant/Permission Required/Restricted/Unknown |
| source_url | string | No | Stable source URL |
| author/organization | string | No | Author or publisher |
| license_version | string | No | Specific CC version (e.g., 3.0 or 4.0) |
| revision_id | string | No | Wikimedia revision identifier |
| download_date | string (ISO 8601) | No | Date of extraction |
| attribution_text | string | No | Pre‑drafted credit line |
| adaptation_notes | string | No | Summary of edits/remixes |
| media_license_summary | string | No | License info for non‑text media |

Operational steps:
1) Populate the CSV from the inventory; include per‑file provenance.
2) Draft attribution blocks using the guide; embed notices in distribution packages.
3) QA check attribution completeness and license notice inclusion.
4) Publish redistribution posture (Proceed, Permission Required, Restricted, Unknown).
5) Establish periodic reconciliation: quarterly checks for license updates and portal policy changes.

Table 13. Deliverables checklist

| Deliverable | Location | Format | Status |
|---|---|---|---|
| License register | /metadata/practice_materials_license_register.csv | CSV | Ready for ingestion |
| Attribution guide | /metadata/practice_materials_attribution_guide.md | Markdown | Ready for use |
| Policy gap tracker | Internal | Markdown/CSV | In progress |
| Reconciliation cadence | PMO calendar | Recurring task | Planned |

## Information Gaps and Closure Plan

Several gaps must be addressed to achieve full compliance:
- Adda247 and certain portals (e.g., CareerPower) policy pages are blocked (403), preventing license verification. Plan: Retry via alternate access paths or direct contact; document outcomes.[^10]
- Mockers Terms of Use were inaccessible; only privacy policy and practice page behaviors (registration requirement) were observed. Plan: Contact Mockers for ToU; default to Restricted until verified.[^21][^22][^23]
- DIKSHA content lists reference CC BY 4.0; confirm item‑level licenses in manifests. Plan: Reconcile manifests with DIKSHA pages to confirm CC BY 4.0 for all items.[^1][^2][^3][^4]
- RRB official notices and previous papers are government works; confirm item‑level license notes and any portal restrictions. Plan: Capture issuing board attribution and portal terms per page.[^19][^20]
- Portal downloads (ExamCart/Prepp) lack explicit licenses; assume All Rights Reserved unless proven otherwise. Plan: Verify with original publishers; default to Permission Required.[^12][^13]
- Per‑file licensing for non‑text media within practice materials remains incomplete. Plan: Verify on description pages or Commons; exclude non‑free media from redistributable packages.[^9][^25]
- Attribution formatting preferences (e.g., order, localization, social media constraints) require confirmation. Plan: Align with CC best practices; confirm organizational preferences.[^27][^28]

Table 14. Gap tracker (illustrative)

| Gap | Source | Evidence | Impact | Owner | Target Date | Status |
|---|---|---|---|---|---|---|
| ToU inaccessible | Adda247 | 403 response | Unknown posture | PMO | 30 days | Open |
| ToU inaccessible | Mockers | Privacy only | Restricted posture assumed | PMO | 30 days | Open |
| DIKSHA license confirmation | DIKSHA manifests | Partial list | Compliance risk | Licensing PM | 14 days | In progress |
| RRB per‑item license notes | RRB portals | Mixed pages | Attribution risk | Content Ops | 14 days | In progress |
| Portal downloads licenses | ExamCart/Prepp | Implicit ARR | Redistribution risk | Legal | 30 days | Open |
| Media per‑file licenses | Wikimedia | Missing summaries | Reuse risk | Content Ops | 21 days | In progress |
| Attribution formatting | Org standards | Not specified | UX risk | PMO | 7 days | Planned |

## Appendices

### Appendix A: Platform-by-platform quick reference

Table 15. Platform quick reference

| Portal | Licensing Stance | Redistribution | Commercial Use | Notes |
|---|---|---|---|---|
| DIKSHA | CC BY 4.0 | Allowed with attribution | Allowed | NCERT content; TASL required[^1][^2][^3][^4] |
| Wikimedia | CC BY‑SA 3.0/4.0 | Allowed; SA for adaptations | Allowed | Verify revision; media per‑file[^5][^6][^9][^25][^26] |
| Jagran Josh | ARR | Prohibited without consent | Prohibited | Personal use only[^11] |
| Unacademy | ARR; limited personal license | Prohibited without consent | Prohibited | Do not redistribute[^14] |
| Oliveboard | ARR | Prohibited without consent | Prohibited | Proprietary compilations[^15] |
| Testbook | ARR | Prohibited without consent | Prohibited | Permission workflow[^17] |
| Mockers | ARR (ToU inaccessible) | Prohibited without consent | Prohibited | Registration required[^21][^22][^23] |
| Adda247 | Unknown (403) | Unknown | Unknown | Retry access[^10] |
| RRB official | Government work | Allowed with attribution | Typically allowed | Follow portal terms[^19][^20] |

### Appendix B: Full attribution template library

- DIKSHA/NCERT—Unmodified and Adapted: TASL + License (CC BY 4.0) + Changes.
- Wikimedia—Unmodified (CC BY‑SA 3.0): Title required + attribution + license copy/URI.
- Wikimedia—Adapted (CC BY‑SA 4.0): Attribution + Changes; SA applies; include license copy/URI.
- RRB Official: Title + issuing board/portal + source URL + attribution note.
- Commercial Portals: Title + platform + source + All Rights Reserved + “Redistribution not permitted.”

### Appendix C: Glossary

- Adaptation: A derivative work based on the original (e.g., translation, paraphrase, remix). Share‑alike applies to public distributions of adaptations under CC BY‑SA.[^5]
- Collection: An aggregation of separate independent works; share‑alike does not apply to the collection as a whole, only to adapted components.[^5]
- TASL: Creative Commons attribution framework—Title, Author, Source, License.[^27]
- ARR (All Rights Reserved): Copyright owner reserves all rights; reuse requires permission.
- Government work: Works produced by government employees within the scope of employment; reuse typically allowed with attribution, subject to portal terms.[^19][^20]

### Appendix D: Citation mapping

- OER attribution practices aligned to CC BY 4.0 and Creative Commons’ recommended practices.[^1][^27]
- Wikimedia licensing evolution and obligations, including media handling and social media attribution.[^5][^6][^9][^25][^28]
- Platform terms for Jagran Josh, Unacademy, Oliveboard, Testbook; Mockers observed behaviors; Adda247 access limitation.[^10][^11][^14][^15][^17][^21][^22][^23]
- RRB official portals (South Central Railway; RRB Bhagalpur) for government materials.[^19][^20]

---

## References

[^1]: DIKSHA - Digital Infrastructure for Knowledge Sharing. https://diksha.gov.in/
[^2]: DIKSHA - Explore as Student. https://diksha.gov.in/exploreasstudent/
[^3]: DIKSHA - Get App. https://diksha.gov.in/getapp/
[^4]: UNESCO: DIKSHA in India (PDF). https://media.unesco.org/sites/default/files/webform/gec002/diksha-in-india.pdf
[^5]: Creative Commons: Legal Code — CC BY‑SA 3.0. https://creativecommons.org/licenses/by-sa/3.0/legalcode.en
[^6]: Creative Commons: Wikipedia moves to CC 4.0 licenses. https://creativecommons.org/2023/06/29/wikipedia-moves-to-cc-4-0-licenses/
[^7]: Wikipedia: Copyrights. https://en.wikipedia.org/wiki/Wikipedia:Copyrights
[^8]: Wikimedia Foundation: Licensing Policy. https://foundation.wikimedia.org/wiki/Policy:Licensing_policy
[^9]: Wikimedia Commons: Licensing. https://commons.wikimedia.org/wiki/Commons:Licensing
[^10]: Adda247: Terms of Use (access blocked). https://www.adda247.com/term-conditions.html
[^11]: Jagran Josh: Terms of Use. https://www.jagranjosh.com/terms-of-use
[^12]: RRB NTPC CBT1 2020 Dec 28 Shift 1 (ExamCart PDF). https://portal-downloads/CBT1/2020/RRB_NTPC_CBT1_2020_Dec28_Shift1_ExamCart.pdf
[^13]: RRB NTPC CBT1 2024 June 06 Shift 2 (Prepp PDF). https://portal-downloads/CBT1/2024/RRB_NTPC_CBT1_2024_June06_Shift2_Prepp.pdf
[^14]: Unacademy: Terms and Conditions. https://unacademy.com/terms
[^15]: Oliveboard: Terms of Use. https://www.oliveboard.in/terms/
[^16]: Testbook: Terms of Service (international). https://testbook.com/en-us/terms-of-service
[^17]: Testbook: Terms of Service (India). https://testbook.com/terms-of-service
[^18]: RRB Ranchi Official Website. https://www.rrbranchi.gov.in/
[^19]: South Central Railway: Terms & Conditions. https://scr.indianrailways.gov.in/view_section.jsp?lang=0&id=0,7,332
[^20]: RRB Bhagalpur: CEN 05/2025 JE (English) PDF. https://downloads/rrb-ntpc/previous-papers/CBT1/2025/cen__2025__CBT__je-dms-cma__en__rrbbhopal.gov.pdf
[^21]: Mockers: Privacy Policy. https://www.mockers.in/privacy-policy
[^22]: Mockers: RRB NTPC Practice Set. https://www.mockers.in/exam/rrb-ntpc-practice-set
[^23]: Mockers: RRB NTPC Mock Test. https://www.mockers.in/exam/rrb-ntpc-mock-test
[^24]: Wikimedia Foundation: Terms of Use. https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
[^25]: Wikipedia: Reusing Wikipedia content. https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content
[^26]: Wikibooks: Creative Commons Attribution-ShareAlike 3.0 License. https://en.wikibooks.org/wiki/Wikibooks:Creative_Commons_Attribution-ShareAlike_3.0_Unported_License
[^27]: Creative Commons Wiki: Recommended practices for attribution. https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution
[^28]: Meta-Wiki: Legal/CC BY-SA licenses and social media. https://meta.wikimedia.org/wiki/Legal/CC_BY-SA_licenses_and_social_media

---

## About this Blueprint

This blueprint is designed to be implemented immediately by content operations, licensing and permissions managers, QA teams, legal counsel, and RRB NTPC preparation product managers. It aligns day‑to‑day content handling with legally robust, audit‑ready controls while enabling the redistribution of open-licensed practice materials at scale.