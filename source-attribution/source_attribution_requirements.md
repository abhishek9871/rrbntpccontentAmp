# Source Attribution Requirements and Licensing Blueprint (RRB, Government OER, Educational Portals, Wikimedia)

## Executive Summary and Objectives

This blueprint consolidates licensing and attribution requirements for a diverse content ecosystem that includes official Railway Recruitment Board (RRB) sources, Indian government open educational resources (OER) platforms, private educational portals, and Wikimedia projects. The primary outputs are: a compliance-grade CSV of source attributions and a cross-source attribution requirements guide. Together, they enable content managers, legal and compliance officers, data curators, and editorial teams to apply consistent, audit-ready practices across all content reuse scenarios.

The scope covers four source categories:

- Official/Government: RRB boards, their official domains, and associated notices and archives.
- Government OER: DIKSHA (Digital Infrastructure for Knowledge Sharing) as the national K‑12 platform; NROER noted for historical context despite inactivity.
- Educational Portals: private platforms offering study materials, mock tests, and previous year papers, often with restrictive or unclear licensing terms.
- Wikimedia Projects: primarily Wikipedia and Wikibooks text under Creative Commons Attribution–ShareAlike (CC BY‑SA), with non‑text media governed by per‑file licenses.

The immediate deliverables are:

- A CSV with columns aligned to compliance needs: content_title, source_name, source_type, attribution_required, attribution_text, contact_info, license_type, usage_restrictions.
- A cross-source requirements document specifying attribution patterns, license obligations, and redistribution rules by source type, including ready-to-use templates and compliance workflows.

Key license anchors include DIKSHA’s Creative Commons Attribution framework (CC BY) as documented by Creative Commons and UNESCO, and Wikimedia’s evolution from CC BY‑SA 3.0 to CC BY‑SA 4.0 as announced by Creative Commons.[^1][^2]

Known gaps—such as inaccessible portal policies, incomplete contact information for certain RRB entries, and platform inactivity—are identified and managed via escalation and periodic verification as part of the governance model described herein.

## Methodology and Source Inputs

The methodology consolidates source catalogs and licensing registers into a single, normalized view that prioritizes official government sources, verifiable licensing statements, and platform policies. Records are standardized into the target schema, with license classification, attribution requirements, and usage restrictions captured consistently. Incomplete or inaccessible entries are flagged for verification rather than inferred.

The primary inputs are the RRB boards catalog, credible portals catalog, OER platforms catalog (including DIKSHA and NROER), DIKSHA licensing documentation, and Wikimedia licensing registers and attribution guidance. For OER, DIKSHA serves as the canonical active platform; NROER is recorded as inactive and thus non-viable for ongoing reuse without separate archival verification.

Source classification follows four categories: official/government (e.g., RRB boards), government OER (DIKSHA, NROER), educational portals (private platforms), and wikimedia (Wikimedia projects). The classification determines license type, attribution duties, and redistribution permissions.

To orient the reader to inputs and normalization steps, the following table summarizes how source catalogs are mapped into the target schema.

Table 1. Source input inventory and normalization mapping

| Input catalog/register | Fields available | Key normalization steps | Target schema coverage |
|---|---|---|---|
| RRB boards catalog | Board name, official domain, hosting infrastructure, primary contact email, phone contact, website status, archive/notices page, NTPC exam page availability, question paper links, website structure notes, verification status, last updated | Map “official domain” to source_name; capture archive/notices page and exam page fields in notes; standardize contact info; classify as official/government | source_name, source_type (official/government), contact_info, attribution_required (Yes by default), license_type (Government copyright by default), usage_restrictions, attribution_text (templated) |
| Credible portals catalog | Portal name, domain credibility, content types, licensing policy, redistribution policy, NTPC coverage, bilingual availability, download procedures, pricing model, fallback recommendation, access status, policy clarity, notes | Where policy clarity is “Unknown” or “Blocked,” mark attribution_required=Yes, license_type=All Rights Reserved (unless proven otherwise), usage_restrictions=No redistribution; create placeholder attribution_text requiring rights clearance | source_name, source_type (portal), license_type (ARR/CC), attribution_required (Yes), usage_restrictions (conservative defaults), attribution_text (requires rights clearance) |
| OER platforms catalog | Platform name, URL, status, subject, language, content type, format, access procedure, licensing information, notes | Classify DIKSHA as active OER with CC BY; NROER flagged inactive with CC BY-SA noted but site inaccessible; record CC license details and government acknowledgment | source_name, source_type (government OER), license_type (CC BY/CC BY-SA), attribution_required (Yes), usage_restrictions (per CC), attribution_text (TASL-based templates) |
| DIKSHA licensing documentation | Attribution requirements, usage permissions, redistribution rules, government acknowledgment text | Create TASL-based attribution templates; record CC BY as default; specify government acknowledgment, link requirement, and change disclosure | attribution_text, license_type, usage_restrictions, attribution_required (Yes) |
| Wikimedia licensing registers | Page titles, revision IDs, dump dates, license type (CC BY‑SA 3.0 vs 4.0), attribution requirements, SA obligations, specific attribution text | For each revision, record license version; map TASL fields; apply SA to adaptations; include license URI and attribution visibility | attribution_text, license_type (CC BY‑SA 3.0/4.0), share‑alike obligations, attribution_required (Yes) |

Information gaps are handled conservatively: if portal licensing policies are blocked or unclear, entries default to “All Rights Reserved,” attribution is marked as required, and redistribution is prohibited until policy clarity is obtained. For inactive OER (NROER), entries are marked as non-viable and escalated for archival verification. These defaults minimize risk and ensure transparent, audit-ready records.

## Cross-Source Licensing Foundations and Attribution Principles

Across this ecosystem, two licensing families dominate: Creative Commons for OER and Wikimedia content, and government copyright/All Rights Reserved for official RRB sites and private educational portals without explicit CC licensing. For Creative Commons content, attribution is not optional. The Creative Commons recommended practice—TASL (Title, Author, Source, License)—offers a simple, robust framework to meet legal requirements and to support downstream reuse.[^3] Share‑alike obligations apply to adaptations under CC BY‑SA, including Wikipedia and Wikibooks text. These obligations require licensing adaptations under the same elements (BY‑SA), including the license URI or text in distributions, and avoiding additional terms that restrict recipients’ rights.[^4][^5][^6]

For government OER like DIKSHA, the licensing framework is primarily CC BY, enabling verbatim reuse, revision, and redistribution with attribution and disclosure of changes; commercial use is allowed under CC BY, subject to attribution and moral rights respect.[^1] UNESCO’s documentation of DIKSHA provides important context on government authorship and institutional roles (NCERT, Ministry of Education), which should be reflected in attribution and government acknowledgments.[^2]

Wikimedia projects underwent a transition in 2023 from CC BY‑SA 3.0 to CC BY‑SA 4.0. Critically, the license attached to the specific revision governs reuse. Where an earlier revision remains under 3.0, obligations differ from later revisions under 4.0. The attribution text and templates should therefore be revision-aware, and the license register must bind each record to the correct license version, revision ID, and timestamp.[^7]

To situate Creative Commons obligations against practical implementation, the following table distills the most relevant points.

Table 2. Creative Commons obligations and practical effects

| Obligation | Practical effect | Implementation implication |
|---|---|---|
| Attribution under CC BY/CC BY‑SA | Credit the creator, provide source, and license designation; disclose changes | Apply TASL fields consistently; include license URI; note modifications |
| Share‑alike for adaptations (BY‑SA only) | License adaptations under BY‑SA (same elements) | Apply BY‑SA to adapted text; include license copy/URI; track SA scope |
| License notice inclusion | Provide license name, copy or URI with distributions | Bundle license text or link in packages and documentation |
| No implied endorsement | Avoid statements suggesting creator endorsement | Editorial review of marketing claims; legal checks for branding |
| No additional/restrictive terms | Do not impose terms that limit recipients’ rights | Review platform Terms of Service; avoid DRM that blocks reuse |
| Moral rights | Avoid derogatory treatment; respect creators’ honor | Editorial standards for modifications; document changes transparently |

Attribution remains visible and accessible to recipients. Attribution placed solely in metadata may not satisfy visibility requirements, particularly on social media, where attribution should be in captions or adjacent posts, alongside the license designation.[^8] TASL is a practical backbone across media and channels, including constrained formats.

## Official RRB Boards: Attribution and Redistribution Requirements

RRB boards operate as official government sources. Their websites and official notices are typically protected by government copyright, and redistribution of site content without explicit permission is not permitted. Attribution is required when referencing official notices, question papers, or any site content. Redistribution of PDFs or official documents must respect site terms and any stated restrictions.

Contact information for boards varies in completeness. Where contact emails and phone numbers are provided in the catalog, they should be captured and used for rights clearance. Where information is missing, entries must be flagged for verification before bulk redistribution.

Table 3 summarizes contact fields available and flags for missing data.

Table 3. RRB board contact summary and verification flags

| Board | Official domain (source_name) | Primary email | Phone | Verification status | Missing data flag |
|---|---|---|---|---|---|
| RRB Chandigarh (CDG) | rrbcdg.gov.in | rrbcdg@railnet.gov.in | 0172-2730093 | Verified | None |
| RRB Mumbai | rrbmumbai.gov.in | asrrb-mum@nic.in | 022‑23090422, 022‑67644033 | Verified | None |
| RRB Chennai | rrbchennai.gov.in | office.rrbmas@railnet.gov.in | 044‑2827‑5323 | Verified | None |
| RRB Bangalore | rrbbnc.gov.in | enquiry.rrbsbc@gmail.com | Not specified | Verified | Phone missing |
| RRB Kolkata | rrbkolkata.gov.in | kolrrb@gmail.com | 6291516873 (recruitment), 182 helpline | Verified | None |
| RRB Delhi (RRCB) | rrcb.gov.in | Not specified | Not specified | Verified | Email and phone missing |
| RRB Allahabad (Prayagraj) | rrbpryj.gov.in | rrbpryj@gmail.com | Not specified | Verified | Phone missing |
| RRB Bhopal | rrbbhopal.gov.in | msrrbbpl@gmail.com | 0755‑2746660 | Verified | None |
| RRB Patna | rrbpatna.gov.in | office.rrbpnbe@railnet.gov.in | 0612‑2677011 | Verified | None |
| RRB Ranchi | rrbranchi.gov.in | rrb‑ranchi@gov.in | 0651‑2462429 | Verified | None |
| RRB Thiruvananthapuram | rrbthiruvananthapuram.gov.in | office.rrbtvc@railnet.gov.in | 0471‑2323357 | Verified | None |
| RRB Guwahati | rrbguwahati.gov.in | crrb‑as@nic.in | 0361‑2540813 | Verified | None |
| RRB Siliguri | rrbsiliguri.gov.in | rrb.siliguri‑wb@nic.in | 0353‑2663840 | Verified | None |
| RRB Muzaffarpur | rrbmuzaffarpur.gov.in | rrbmfp‑bih@nic.in | 0621‑2213405 | Verified | None |
| RRB Gorakhpur | rrbgkp.gov.in | asrrb.gr‑up@gov.in | 0551‑2201209 (fax) | Verified | None |

Given these defaults, redistribution rules should be conservative. When in doubt, treat RRB content as “Government copyright” and seek permission before sharing official PDFs or notice documents beyond limited quotation with attribution. This is especially important where contact information is incomplete, and platform-level Terms of Use are not readily accessible.[^9]

### Verified RRB Boards

The verified boards listed above maintain active websites with dedicated employment notices, CEN (Common Employment Notification) pages, and varying structures for question papers and objection trackers. Attribution should reference the board and official domain in any excerpt or summary. Where question paper links are provided, use them only for internal analysis unless explicit redistribution permission is obtained.

### Pending Verification (Contact info incomplete)

For boards without complete contact details (notably Delhi/RRCB, Bangalore, Allahabad/Prayagraj), entries must be flagged for follow-up before any large-scale redistribution. Where phone numbers are missing or only fax lines are available, escalate via official notice board pages and domain registrar contact channels to obtain appropriate permissions.

## Government OER Platforms (DIKSHA, NROER): Licensing and Attribution

DIKSHA is the canonical active OER platform for K‑12 education in India. Its content is generally licensed under Creative Commons Attribution (CC BY), enabling broad educational reuse with attribution, disclosure of changes, and, where feasible, maintaining links to the source. UNESCO’s documentation highlights DIKSHA’s governance by the National Council of Educational Research and Training (NCERT) under the Ministry of Education, and the public interest orientation of the platform. These roles should be acknowledged in attribution text and government source statements.[^1][^2]

Attribution for DIKSHA content should follow TASL: identify the content title, the authoring organization (e.g., NCERT, SCERT, CBSE), the DIKSHA platform as source, and the license designation (CC BY). For adaptations, disclose modifications and maintain a government acknowledgment: “Content sourced from DIKSHA, an initiative of NCERT, Ministry of Education, Government of India.” For mixed resources, map attributions to individual components and maintain the CC license terms.

NROER is recorded as inactive in the OER catalog. Although historical entries may have referenced CC BY‑SA 3.0, site inaccessibility requires verification from authoritative archival sources (e.g., a Wikipedia entry noting inactivity). Until archival licensing is confirmed, treat NROER as non-viable for ongoing reuse. If archival sources confirm licensing terms, attribution may proceed using CC BY‑SA obligations; otherwise, avoid reuse.

Table 4 consolidates platform licensing characteristics.

Table 4. Government OER licensing summary

| Platform | Status | License | Attribution elements | Redistribution |
|---|---|---|---|---|
| DIKSHA | Active | CC BY | Title, author (NCERT/SCERT/CBSE), Source (DIKSHA), License (CC BY), Changes (if any) | Permitted with attribution; commercial use allowed; maintain link to source |
| NROER | Inactive | CC BY‑SA 3.0 (noted historically) | Title, author, Source (NROER), License (CC BY‑SA 3.0), Changes (if any) | Requires archival verification; if confirmed, SA obligations apply to adaptations |

### DIKSHA Attribution and Usage

DIKSHA supports K‑12 content across subjects and formats. For textbooks, interactive content, teacher training materials (e.g., NISHTHA), and assessment resources, attribution must include authoring organizations, the DIKSHA source, and CC BY designation. Redistribution is permitted with attribution, and adaptations should disclose changes and maintain source links. Government acknowledgment should reference DIKSHA’s institutional roles (NCERT, Ministry of Education) for clarity.

### NROER Attribution and Usage

NROER is currently inactive. While historical licensing references may exist, teams should not proceed on assumptions. Escalate to verify licensing via archival records. If confirmed, attribution must follow CC BY‑SA 3.0, including license inclusion and share‑alike obligations for any adaptations. Pending verification, classify NROER entries as non-viable for reuse.

## Educational Portals: Licensing Policies and Attribution Requirements

Private educational portals commonly assert “All Rights Reserved” or restrict reuse via Terms of Service. Where explicit licensing statements are unavailable or access is blocked (e.g., HTTP 403), default to conservative handling: attribution required, redistribution prohibited, and commercial use disallowed without explicit permission. Many portals operate controlled access models requiring login or subscription, further limiting reuse.

Portal-specific considerations:

- Testbook presents comprehensive materials but enforces strict copyright; redistribution is not permitted without rights.
- Adda247 and CareerPower blocked policy access (403); licensing remains unknown; treat as All Rights Reserved until confirmed otherwise.
- Jagran Josh permits personal use only; commercial redistribution and derivative works are restricted; attribution should respect stated terms.
- Unacademy’s platform terms are general; RRB-specific materials require explicit policy confirmation.
- BYJU’S Exam Prep and Oliveboard provide content after registration; licensing for RRB materials is not explicit; assume controlled reuse.
- RRB Exam Portal and Railway Capsule claim ownership and free access but lack explicit redistribution policies; attribution is required, and redistribution should be limited pending rights clearance.

Table 5 summarizes portal licensing posture and handling.

Table 5. Portal licensing summary

| Portal | License posture | Redistribution | Commercial use | Notes |
|---|---|---|---|---|
| Testbook | All Rights Reserved | No unauthorized redistribution | Not permitted without permission | Strict copyright enforcement |
| Adda247 | Unknown (access blocked) | Not determined | Not determined | Escalate for policy access |
| CareerPower | Unknown (access blocked) | Not determined | Not determined | Escalate for policy access |
| Jagran Josh | Personal use only | No commercial redistribution | Restricted | Detailed terms available |
| Unacademy | General platform terms | Unclear for RRB materials | Unclear | Seek explicit permission |
| BYJU’S Exam Prep | Not explicit for RRB materials | Controlled | Controlled | Registration required |
| Oliveboard | Not explicit | Controlled | Controlled | Login/subscription model |
| RRB Exam Portal | Ownership claimed | No explicit guidelines | Unclear | Copyright implied; conservative handling |
| Railway Capsule | Free access claimed | No explicit redistribution policies | Unclear | Bilingual materials; limited policy clarity |

Given these defaults, teams should avoid bulk redistribution of portal content and seek explicit permissions where necessary. Attribution must still be provided when referencing materials, and any quotation should be limited and transparent.

## Wikimedia Projects: Licensing Evolution, Attribution, and Share‑Alike

Wikimedia projects transitioned to CC BY‑SA 4.0 in June 2023. While newer revisions are governed by 4.0, earlier revisions may remain under 3.0 (or dual-licensed under GFDL and 3.0). Reuse must bind to the license of the exact revision used. Attribution practices should follow TASL and Wikimedia’s attribution policy. Share‑alike applies to adaptations: translations, paraphrases, and remixes must be licensed under CC BY‑SA (same elements) and include the license copy or URI in distributions.[^4][^7][^10][^5]

Non‑text media require per‑file license verification. Wikimedia Commons adheres to free licenses or public domain dedication, but each file’s license must be checked on its description page. Wikipedia’s Exemption Doctrine Policy (EDP) allows limited non‑free content within project contexts; however, such content is not freely reusable outside the EDP scope and should be excluded from redistributable packages that do not replicate EDP conditions.[^11][^12]

Social media distribution demands special care: attribution must be visible (e.g., in captions or comments), include the license designation, and avoid implying endorsement. Attribution placed only in metadata fields is often insufficient for compliance.[^8]

Table 6 clarifies attribution elements and share‑alike obligations by license version.

Table 6. Attribution elements and share‑alike obligations (CC BY‑SA 3.0 vs 4.0)

| Dimension | CC BY‑SA 3.0 | CC BY‑SA 4.0 |
|---|---|---|
| Attribution structure | Title required; Author, Source, License; adaptation credit where applicable | Title optional; Author, Source, License; indicate changes |
| Share‑alike scope | Adaptations licensed under BY‑SA 3.0 or later version with same elements | Adaptations licensed under BY‑SA with same elements (this version or later) |
| License notice | Include copy or URI with distributions | Include copy or URI with distributions |
| Compatibility | CC 3.0 ports recognized; later versions with same elements allowed | CC compatibility process; only CC-approved compatible licenses |

### Wikipedia and Wikibooks Text

For unmodified text reuse, maintain copyright notices and provide Title, Author, Source, and License, with a license URI or copy. For adaptations, include an adaptation credit that is at least as prominent as other credits and describe changes made. Record the revision ID and timestamp to ensure the correct license is tied to each record. Avoid crediting the platform generically; attribution should credit contributing authors and the project.[^13][^14][^10]

### Non‑Text Media Handling

Images, audio, and video are governed by their own licenses. Verify each file’s license on its description page. Use free alternatives wherever possible and exclude non‑free media from reusable collections unless your project explicitly replicates the EDP context. Applying SA only to adaptations is not optional; it is a legal condition of reuse under CC BY‑SA.[^11][^12]

## Output Artifacts and Implementation Plan

The first artifact is a CSV with the following columns: content_title, source_name, source_type, attribution_required, attribution_text, contact_info, license_type, usage_restrictions. The second is an attribution requirements guide that sets out instructions for proper attribution across source types, templates for common scenarios, and QA workflows.

The CSV is populated through normalization of source catalogs and registers. For RRB entries, source_name reflects official domains; license_type defaults to Government copyright; attribution_text is templated; and contact_info is captured where available. For government OER, DIKSHA entries are classified under CC BY with TASL-based attribution text; NROER is flagged inactive and non-viable pending archival verification. For educational portals, licensing defaults to All Rights Reserved where policies are blocked or unknown, with redistribution prohibitions and explicit rights clearance requirements. For Wikimedia entries, attribution_text and license_type reflect the specific revision’s license (CC BY‑SA 3.0 or 4.0), and share‑alike obligations are noted where adaptations are involved.

Templates should be embedded in editorial guidance and reused across content packages:

- Basic OER (DIKSHA, CC BY): “Title: {title}. Author: {author}. Source: DIKSHA. License: CC BY 4.0. Changes: {if any}.”
- Government acknowledgment: “Content sourced from DIKSHA, an initiative of NCERT, Ministry of Education, Government of India.”
- Basic Wikimedia (CC BY‑SA): “Title: {title}. Authors: Contributors. Source: {project}. License: CC BY‑SA {version}. Changes: {if any}.”
- Adapted Wikimedia: “Adapted from ‘{title}’ ({project}). Authors: Contributors. Source: {URL}. License: CC BY‑SA {version}. Changes: {summary}.”

Table 7 clarifies field-level implementation.

Table 7. CSV schema mapping and examples

| Column | Definition | Source mapping | Example value |
|---|---|---|---|
| content_title | Title of reused content | From platform pages, OER records, Wikimedia entries | “Mathematics Textbook – Class X” |
| source_name | Name of the source site or platform | Official domain (RRB), platform name (DIKSHA, portals), Wikimedia project | “DIKSHA”, “RRB Chennai”, “Wikipedia” |
| source_type | Categorization of source | official/government, government OER, portal, wikimedia | “government OER” |
| attribution_required | Whether attribution is mandatory | Yes for all except PD where discouraged but citation encouraged | “Yes” |
| attribution_text | Ready-to-use attribution string | TASL templates per source type | “Title: … Author: … Source: … License: CC BY 4.0. Changes: …” |
| contact_info | Rights or support contact | Catalog emails/phones; where missing, flag for verification | “office.rrbmas@railnet.gov.in” |
| license_type | License designation | Government copyright; CC BY (DIKSHA); CC BY‑SA (Wikimedia); ARR (portals) | “CC BY 4.0” |
| usage_restrictions | Redistribution and other limits | No redistribution (ARR); SA for adaptations (BY‑SA); CC BY permissions (OER) | “No redistribution without permission; SA applies to adaptations” |

Wikimedia-specific provenance fields (e.g., revision ID, dump date) should be maintained in a supplemental register to ensure revision-aware compliance, even if not included in the CSV’s minimum schema.[^4][^7][^10]

## Compliance Checklist and QA Workflow

Compliance demands a repeatable, disciplined workflow with auditable outputs. The QA process covers provenance capture, attribution drafting, share‑alike determination, license notice inclusion, media verification, and reconciliation.

Table 8 provides a condensed QA checklist to embed in operations.

Table 8. Compliance QA checklist

| Step | Verification | Status |
|---|---|---|
| Provenance capture | Source name, URL, revision ID (Wikimedia), timestamp recorded |  |
| License confirmation | CC version (3.0 vs 4.0) verified; government/ARR confirmed |  |
| Attribution completeness | TASL present; adaptation credit where applicable |  |
| License notice included | License copy or URI included for CC works |  |
| Share‑alike assessment | Adaptation identified; correct license applied (BY‑SA) |  |
| Non‑text media check | Per‑file licenses verified; free licenses only |  |
| No restrictive terms | No DRM or additional terms that limit rights |  |
| Documentation | Attribution and changelog included in package |  |
| Reconciliation | Register updated for license/version changes |  |

Governance includes periodic reconciliation against source updates, maintaining immutable revision histories, and clear change logs for adaptations. Legal disclaimers and risk controls—particularly avoiding implied endorsements and respecting moral rights—must be embedded in editorial and marketing practices. Teams must also review Terms of Use to avoid introducing non-CC terms that restrict recipients’ rights under CC licenses.[^4][^3][^7]

## Edge Cases and Risk Controls

Non-free media within Wikipedia are governed by an Exemption Doctrine Policy that permits limited uses within project contexts, but such media are not freely reusable outside that context. Redistribution packages intended for open reuse should exclude non-free media unless the EDP is fully replicated, which is typically impractical. Prefer clearly licensed alternatives on Wikimedia Commons.[^11][^12]

Terms of Service can introduce additional, non-CC terms. Avoid imposing terms that contradict CC permissions or that apply effective technological measures restricting recipients’ rights. Review your own platform and distribution boilerplate to ensure it does not negate CC licenses.[^15]

For U.S. government works, works created by federal employees within the scope of employment are generally in the public domain in the United States under 17 U.S.C. § 105, but may be copyrighted elsewhere. Not all works republished by U.S. government agencies are public domain; contractor works or stock photography remain under copyright. Verification of authorship and scope is necessary before reuse.[^16]

When licensing is ambiguous or site access is blocked, default to conservative handling: treat materials as All Rights Reserved, avoid redistribution, and seek rights clearance. This reduces legal exposure while enabling transparent escalation to rights holders.

## Governance, Maintenance, and Update Cadence

Attribution records are living artifacts. Maintain version control for attribution text, changelogs for adaptations, and immutable histories for license register entries. Establish periodic reconciliation against source updates—particularly for Wikimedia revisions that may have transitioned from 3.0 to 4.0—and ensure attribution templates remain aligned with current CC guidance.

Define escalation paths: archive verification for NROER; rights clearance with portals; and missing contact completion for RRB boards. Change control should capture license version transitions, source accessibility updates, and policy changes on portals, with audit trails suitable for compliance reviews.

Table 9 outlines a maintenance cadence.

Table 9. Maintenance cadence and responsibilities

| Activity | Cadence | Responsible role | Audit artifact |
|---|---|---|---|
| License reconciliation (Wikimedia) | Quarterly | Licensing/Content Ops | Revision log; license version map |
| OER policy verification (DIKSHA) | Quarterly | Editorial/Legal | Attribution template review |
| NROER archival check | Quarterly | Legal/Content Ops | Archival source confirmation |
| Portal policy review | Quarterly | Licensing/Content Ops | Policy capture; rights clearance letters |
| RRB contact completion | Quarterly | Data Curator/Legal | Contact registry update |
| QA sampling | Monthly | Compliance | QA checklist reports |
| Template updates | As needed | Legal/Editorial | Change log; approval record |

Wikimedia projects continue to evolve; attribution practices must keep pace with license transitions and policy updates.[^7][^4]

## References

[^1]: Creative Commons. Creative Commons Attribution 4.0 International (CC BY 4.0). https://creativecommons.org/licenses/by/4.0/
[^2]: UNESCO. DIKSHA – Digital Infrastructure for Knowledge Sharing (India Brief). https://media.unesco.org/sites/default/files/webform/gec002/diksha-in-india.pdf
[^3]: Creative Commons Wiki. Recommended practices for attribution. https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution
[^4]: Creative Commons. Legal Code — Attribution-ShareAlike 3.0 Unported (CC BY‑SA 3.0). https://creativecommons.org/licenses/by-sa/3.0/legalcode.en
[^5]: Creative Commons Wiki. ShareAlike interpretation. https://wiki.creativecommons.org/wiki/ShareAlike_interpretation
[^6]: Creative Commons. Attribution-ShareAlike 4.0 International (CC BY‑SA 4.0). https://creativecommons.org/licenses/by-sa/4.0/
[^7]: Creative Commons. Wikipedia moves to CC 4.0 licenses. https://creativecommons.org/2023/06/29/wikipedia-moves-to-cc-4-0-licenses/
[^8]: Meta-Wiki. Legal/CC BY-SA licenses and social media. https://meta.wikimedia.org/wiki/Legal/CC_BY-SA_licenses_and_social_media
[^9]: Wikimedia Foundation. Policy: Terms of Use. https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
[^10]: Wikipedia. Wikipedia:Attribution. https://en.wikipedia.org/wiki/Wikipedia:Attribution
[^11]: Wikimedia Commons. Commons:Licensing. https://commons.wikimedia.org/wiki/Commons:Licensing
[^12]: Wikipedia. Wikipedia:Image use policy. https://en.wikipedia.org/wiki/Wikipedia:Image_use_policy
[^13]: Wikipedia. Wikipedia:Copyrights. https://en.wikipedia.org/wiki/Wikipedia:Copyrights
[^14]: Wikibooks. Wikibooks:Copyrights. https://en.wikibooks.org/wiki/Wikibooks:Copyrights
[^15]: Wikimedia Foundation. Resolution: Licensing policy. https://foundation.wikimedia.org/wiki/Policy:Licensing_policy
[^16]: Cornell Law School. 17 U.S. Code § 105 - Subject matter of copyright; United States Government works. https://www.law.cornell.edu/uscode/text/17/105

---

Acknowledged information gaps: portal licensing policies are partially inaccessible and may require direct engagement; NROER is inactive and site-level licensing confirmation requires archival sources; RRB contact fields vary in completeness; organization-level attribution formatting preferences are not specified; workflow tooling for license reconciliation requires internal definition.