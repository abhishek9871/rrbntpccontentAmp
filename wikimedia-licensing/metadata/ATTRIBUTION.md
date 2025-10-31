# Wikimedia Licensing and Attribution Compliance Blueprint for CC BY-SA 3.0 Content

## Executive Summary and Scope

This blueprint sets out a practical, legally compliant approach to reusing Wikipedia and Wikibooks content that was originally collected and may remain governed by Creative Commons Attribution–ShareAlike 3.0 Unported (CC BY‑SA 3.0). It explains the attribution obligations that attach to unmodified text, the share‑alike duties that attach when you create adaptations, and the operational controls your teams should implement in a license register and attribution practices. The goal is to enable frictionless reuse while ensuring that downstream redistributors can continue to satisfy the same conditions.

The scope is intentionally narrow and concrete: textual materials from Wikipedia and Wikibooks that are licensed under CC BY‑SA 3.0 (or presented on project pages that reference that license), plus clear handling rules for non‑text media (images, audio, video) whose licenses differ and must be checked on their description pages. The primary deliverable is a data model and implementation guidance for a license register that records per‑file attribution fields, license metadata, and share‑alike requirements. This blueprint also provides a process to keep metadata current as projects transition to CC BY‑SA 4.0, and ready‑to‑use attribution templates that comply with CC BY‑SA 3.0.

Finally, the blueprint takes account of the 2023 move of Wikimedia projects to CC BY‑SA 4.0 and explains how to resolve conflicts if your collection is tied to 3.0 but a newer page revision reflects the 4.0 license. In all cases, the license that applies to the specific revision you reuse governs your obligations; your register must record that provenance precisely.[^2][^7]

## Licensing Foundations: CC BY‑SA 3.0 Core Obligations

CC BY‑SA 3.0 is a “copyleft” license. It grants broad freedoms to reproduce, distribute, and adapt a work, provided two core conditions are met: attribution to the licensor and share‑alike for any adaptations. The license is worldwide, royalty‑free, non‑exclusive, and perpetual for the duration of copyright. For text reused from Wikimedia projects under 3.0, these conditions translate into concrete steps that must be completed at the point of reuse and documented in your systems.

The license’s attribution requirements are precise. For unmodified reuse, you must keep intact any copyright notices, provide the original author’s name (or pseudonym) if supplied, provide the work’s title if supplied, and, to the extent reasonably practicable, provide a Uniform Resource Identifier (URI) specified by the licensor that refers to copyright or licensing information. For adaptations, you must also credit the way the original work was used within your adaptation (for example, “English text adapted from the work by X”). Attribution must appear in a manner at least as prominent as other credits, and you may not imply endorsement by the author or licensor without separate permission.[^1]

Share‑alike under CC BY‑SA 3.0 attaches to adaptations. If you publicly distribute an adaptation, you must license it under the same license (CC BY‑SA 3.0), a later version with the same license elements (for example, CC BY‑SA 3.0 or later), or a Creative Commons jurisdiction port with the same elements (for example, CC BY‑SA 3.0 US). You must include a copy or URI of the applicable license with every distribution of the adaptation. You may not add terms that restrict the license’s effect or apply effective technological measures (such as DRM) that limit recipients’ rights. The share‑alike obligation applies to the adaptation itself and to the adaptation as incorporated in collections; it does not impose the license on the entire collection, apart from the adaptation.[^1]

Creative Commons recommends a clear, transferable attribution pattern commonly summarized as TASL—Title, Author, Source, License. For 3.0, Title is required; for 4.0 it is optional. Reasonable attribution varies by medium, but the underlying principle is consistent: give recipients the information they need to find the original work, know who to credit, identify the license, and understand what changes you made.[^3] Creative Commons’ share‑alike guidance clarifies that the SA condition only applies when an adaptation is publicly shared; private uses and uses covered by copyright exceptions are not forced into share‑alike. The definition of adaptation varies by jurisdiction, which can affect whether a particular transformation is considered an adaptation.[^9]

To anchor these points for operational use, Table 1 summarizes the essential legal conditions and their practical effects.

To illustrate the core requirements succinctly, the following table maps each legal obligation to practical reuser obligations and their operational implications.

Table 1. Summary of CC BY‑SA 3.0 obligations

| Obligation | Legal source (CC BY‑SA 3.0) | Practical effect for reusers | Operational implication |
|---|---|---|---|
| Attribution elements | Section 4(c) | Keep copyright notices; provide Title (required in 3.0), Author (or pseudonym), Source URI if supplied; for Adaptations, credit the use | Implement TASL fields; record Title, Author, Source, and License; ensure adaptation credits are prominent |
| Attribution conduct | Section 4(d) | No implied endorsement without express permission | Avoid marketing statements implying endorsement; legal review for brand positioning |
| License notice for Work | Section 4(a) | Include a copy or URI of the license with distributions | Bundle license text or link; automate in distribution packaging |
| License notice for Adaptations | Section 4(b) | Include a copy or URI of the applicable license with distributions of adaptations | For adapted content, include the adapter’s license text or URI |
| Share‑alike for Adaptations | Section 4(b) | License adaptations under CC BY‑SA 3.0, or same‑element later version, or a compatible CC SA port | Enforce licensing of derivatives under CC BY‑SA; track compatibility |
| No additional/restrictive terms | Sections 4(a) and 4(b) | You may not impose terms that restrict recipients’ rights or sublicense | Review Terms of Service; avoid legal boilerplate that narrows permissions |
| No effective technological measures | Sections 4(a) and 4(b) | Do not apply DRM or similar measures that block rights | Avoid restrictive access controls on shared copies |
| Moral rights | Section 4(e) | No derogatory treatment of the work; respect author’s honor and reputation | Editorial review to avoid distortion; document changes without denigration |

[^1][^3][^9]

## Wikimedia Licensing Context and Evolution

Wikipedia’s textual content has historically been available under Creative Commons Attribution–ShareAlike licenses and the GNU Free Documentation License (GFDL). Many images and other non‑text media carry their own licenses that differ from the text license and must be checked individually on their description pages. The Wikimedia Foundation’s licensing policy requires projects to host free content consistent with the Definition of Free Cultural Works; projects may adopt an Exemption Doctrine Policy (EDP) to permit limited non‑free content under strict conditions, but such content is not freely reusable outside the project’s EDP context.[^4][^5]

In June 2023, Wikimedia projects transitioned to CC BY‑SA 4.0. For reusers, this means that page revisions made after the transition are generally governed by 4.0, while earlier revisions may remain under 3.0 (or dual‑licensed under GFDL and 3.0). If you reuse content from a specific revision, the license applicable to that revision determines your obligations. Your license register must capture the revision identifier and timestamp so you can show which license applied to the exact content reused.[^2]

Wikimedia Commons applies its own licensing standards and accepts only specific free licenses or public domain dedication; media on Commons are either public domain or under a free Creative Commons license suitable for reuse. As with Wikipedia’s media, each file’s license must be verified on its description page before reuse.[^6]

To clarify the version differences, Table 2 compares attribution, share‑alike, and notices across CC BY‑SA 3.0 and 4.0. For reusers of Wikimedia content, the most consequential differences in practice are formalization of “same license elements” in 4.0, the changed status of Title as optional in 4.0, and clarifications to the adapter’s license inclusion requirements.

Table 2. CC BY‑SA 3.0 vs CC BY‑SA 4.0: practical comparison for reusers

| Dimension | CC BY‑SA 3.0 (Unported) | CC BY‑SA 4.0 (International) |
|---|---|---|
| License elements | Attribution + ShareAlike | Attribution + ShareAlike |
| Title in attribution | Required | Optional (recommended by CC best practice) |
| Attribution structure | Maintain notices; provide Title, Author, Source, and adaptation credit as applicable | Maintain notices; provide Author, Source, License; indicate changes; Title optional |
| Share‑alike scope | Adaptations must be licensed under this license, a later version with same elements, or a CC SA jurisdiction port | Adaptations must be licensed under BY‑SA with same elements, this version or later, or a compatible SA license |
| License copy/URI | Required with distributions of Work and Adaptations | Required with distributions of Work and Adaptations |
| Compatibility | CC 3.0 ports recognized; later versions with same elements allowed | CC compatibility process formalizes “compatible licenses” under BY‑SA; only those approved by CC are compatible |

[^1][^2][^3]

## Attribution Requirements for Wikimedia Text (Wikipedia and Wikibooks)

For unmodified text reuse, the minimal compliant attribution under CC BY‑SA 3.0 requires the following: keep any copyright notices intact; provide the title of the work; credit the original author (or pseudonym) if supplied; include a source URI if one has been specified for the work; and include the license name with a copy or URI to the license. You should avoid implying endorsement and must ensure that attribution appears prominently in a way a reasonable recipient would notice.[^1]

For adapted text, attribution must also include a clear statement describing how the original work was used in your adaptation. The adaptation credit should be at least as prominent as any other credits. If you remix multiple sources, you must make clear which attribution belongs to which work; stacking credits without mapping them to their works is not sufficient.[^1][^3]

Creative Commons’ TASL model offers a convenient backbone for implementation. For 3.0, you must include Title; you should include Author, Source, and License; and you must note changes if you created an adaptation. Where practical, provide clickable links to the title, author profile or project page, the exact source URL, and the license deed or legal code. For print or offline distribution, include the full URLs or a printed credit page that maps each attribution to the correct work.[^3]

Wikimedia‑specific nuance matters. Attribution should credit the contributing authors and the project, rather than crediting the platform generically. You should also preserve any author‑requested attribution if it is visible on the page and record the revision identifier to tie the attribution to the correct license version. While Wikipedia’s attribution policy focuses on sourcing content within articles, the copyright page for reusers aligns attribution practices with the applicable license and emphasizes preserving visible attribution signals.[^8][^4]

Table 3 maps TASL to the CC BY‑SA 3.0 obligations and Wikimedia‑specific implementation choices.

Table 3. Attribution field mapping (TASL) to CC BY‑SA 3.0 obligations

| TASL element | CC BY‑SA 3.0 requirement | Implementation for Wikimedia text |
|---|---|---|
| Title (required in 3.0) | Provide the title of the work if supplied | Use the Wikipedia article or Wikibooks page title; capture in register |
| Author | Credit the original author or licensor; use name or pseudonym if provided | Credit contributing authors; avoid crediting the platform generically; record author list where feasible |
| Source | Provide a URI associated with the work’s copyright/licensing info | Link to the exact page revision used; capture URL and revision ID in register |
| License | Provide the license name and copy or URI | State “CC BY‑SA 3.0” and include a copy or link to the license |
| Changes | Indicate modifications for Adaptations | Add an “Changes made” note summarizing edits, translations, or remixes |
| Placement | Prominence and conduct of attribution | Place attribution in a credits section; avoid implying endorsement |

[^1][^3][^4][^8]

## Share‑Alike Compliance for Adaptations

Share‑alike is the mechanism that keeps adaptations free. Under CC BY‑SA 3.0, when you publicly distribute an adaptation, you must license it under CC BY‑SA 3.0 or under a later version with the same license elements, and you must include the license text or URI with your distribution. You may not impose additional terms that restrict the rights granted by the license, and you may not apply effective technological measures that limit recipients’ ability to exercise those rights. These obligations apply to the adaptation and to the adaptation within collections; the license does not require the entire collection to be licensed under CC BY‑SA, apart from the adaptation itself.[^1]

Creative Commons’ share‑alike guidance clarifies that these obligations only arise when you publicly share an adaptation. Private use or uses covered by copyright exceptions (such as criticism or parody) do not trigger a requirement to apply share‑alike. Moreover, whether a given transformation qualifies as an adaptation is a matter of copyright law and can vary across jurisdictions, so teams should consult counsel when unusual transformations are at issue.[^9]

For practical compliance, distinguish adaptations from collections. A collection aggregates separate independent works without modifying them; share‑alike does not apply to the collection as a whole, only to adaptations within it. If you translate, remix, or synthesize text from multiple sources, the output is likely an adaptation; applying CC BY‑SA 3.0 (or later) to the adapted portion is required before you redistribute it publicly. For distribution packaging, you should include the license text or URI and a change log indicating what was modified.[^1]

Table 4 operationalizes these rules by mapping typical transformation scenarios to license obligations.

Table 4. Share‑alike obligation matrix

| Scenario | Is this an Adaptation? | SA obligation | Required notices |
|---|---|---|---|
| Verbatim copy of text | No | None beyond attribution | Attribution (TASL) and CC BY‑SA 3.0 license copy/URI |
| Translation to another language | Yes | License adaptation under CC BY‑SA 3.0 (or later version with same elements) | Attribution for adapted work; include license copy/URI; indicate changes |
| Paraphrase/summary of a page | Yes (derivative work) | License adaptation under CC BY‑SA 3.0 | Attribution; license copy/URI; describe changes |
| Remix of multiple pages into a new text | Yes | License adapted portions under CC BY‑SA 3.0 | Map attributions to sources; license copy/URI; change notes |
| Compilation aggregating unmodified pages | No (Collection) | SA does not apply to the collection as a whole; applies only to any adapted components | Attribution for each included work; license copy/URI for adapted components |
| Internal working paper not shared publicly | No public sharing | SA does not apply | Attribution retained internally; no SA required until public sharing |

[^1][^9]

## Non‑Text Media (Images, Audio, Video) and Per‑File Licensing

Text is only part of the story. Each non‑text file carries its own license. Some files on Wikipedia are co‑licensed with the text; many others are under different Creative Commons licenses or are public domain. Wikimedia Commons maintains stricter licensing准入 and accepts only free licenses or public domain dedication; still, each file must be verified on its description page before reuse. When multiple licenses apply, you must comply with all of them.[^4][^5][^6]

Operationally, you should reject non‑free media unless your project has an EDP that permits specific uses under copyright exceptions. Even then, non‑free media are not freely reusable outside the EDP’s scope and should not be included in redistributable packages that do not replicate the EDP context. As a rule of thumb: if a free alternative exists or becomes available, use it and avoid non‑free media entirely in reusable collections.[^5]

Table 5 illustrates common scenarios and required actions for non‑text media.

Table 5. Media license handling

| License on file | Permissible reuse conditions | Required attribution | SA behavior | Action required |
|---|---|---|---|---|
| CC BY‑SA 3.0 (same as text) | Free reuse with attribution and SA for adaptations | TASL for the file; per‑file Source URI and Author | SA applies to adaptations | Include attribution and license copy/URI; apply CC BY‑SA 3.0 to adaptations |
| CC BY 3.0/4.0 (no SA) | Free reuse with attribution; no SA | TASL; note license is BY not BY‑SA | No SA requirement | Include attribution; do not apply SA |
| Public domain (CC0/PD) | Free reuse without attribution required (citation encouraged) | Credit recommended (source/host) | No SA requirement | Verify status; consider crediting source for integrity |
| Non‑free (EDP context only) | Restricted reuse per project EDP; not freely reusable elsewhere | As required by EDP; label source | SA does not make non‑free content free | Exclude from reusable collections or confine to EDP environment |
| Mixed/ambiguous license | Not clearly free | None | None | Do not use; replace with clearly licensed alternative |

[^4][^5][^6]

## Operationalizing Compliance: License Register Data Model

A license register is the backbone of traceability and audit readiness. It should capture per‑file provenance and obligations so that any downstream request can be satisfied by pointing to your records. The register must bind each item to its exact revision, timestamp, and license, and it must store the attribution text you will ship with the item and the share‑alike obligations that attach if the item is adapted.

Minimum fields for each record:
- page_title
- wikipedia_revision_id
- dump_date
- license_type (e.g., CC BY‑SA 3.0)
- attribution_requirements (brief summary)
- share_alike_obligations (brief summary)
- specific_attribution_text (ready‑to‑use credit line, formatted for your distribution channel)

Recommended provenance fields:
- source_url (to the exact revision or page)
- project (Wikipedia/Wikibooks)
- language
- authorship_notes (for transparency where practical)
- change_log (if you created an adaptation)
- media_license_summary (if the file includes non‑text components)

Governance controls to enforce:
- Completeness and uniqueness constraints (every file has a unique key)
- Record creation and update timestamps (audit trail)
- Immutable history (revisions are never overwritten; new entries capture changes)
- Periodic reconciliation (compare dump metadata with current page revisions)

A CSV schema aligned to these requirements should be used for interchange and audit. Tables 6 and 7 specify the schema and illustrate sample values.

Table 6. License register CSV schema

| Column name | Type | Required | Description | Example |
|---|---|---|---|---|
| page_title | string | Yes | Title of the page or file | “World Wide Web” |
| wikipedia_revision_id | string | Yes | Stable revision identifier used for reuse | “m3r1d1s4” |
| dump_date | date (ISO 8601) | Yes | Date the content was extracted or dumped | “2025‑08‑15” |
| license_type | string (enumeration) | Yes | License applicable to the revision (e.g., CC BY‑SA 3.0) | “CC BY‑SA 3.0” |
| attribution_requirements | string | Yes | Human‑readable summary of TASL and notices | “Provide Title, Author, Source, License; include 3.0 license URI” |
| share_alike_obligations | string | Yes | Human‑readable summary for adaptations | “Adaptations must be licensed under CC BY‑SA 3.0 or later with same elements” |
| specific_attribution_text | string | Yes | Ready‑to‑use credit line for distribution | “Text adapted from ‘World Wide Web’ (Wikipedia). Authors: contributors. License: CC BY‑SA 3.0. Changes: edited for length.” |
| source_url | string | No | URL to the exact page revision | (See References) |
| project | string | No | Project name (Wikipedia/Wikibooks) | “Wikipedia” |
| language | string | No | Language code | “en” |
| authorship_notes | string | No | Notes on authors or contributors where visible | “Multiple contributors; authors listed on page history” |
| change_log | string | No | Summary of modifications made | “Condensed and edited for clarity” |
| media_license_summary | string | No | Summary for non‑text media | “Image under CC BY 4.0; verify description page” |

Table 7. Sample license register rows

| page_title | wikipedia_revision_id | dump_date | license_type | attribution_requirements | share_alike_obligations | specific_attribution_text | source_url | project | language | authorship_notes | change_log | media_license_summary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| World Wide Web | m3r1d1s4 | 2025‑08‑15 | CC BY‑SA 3.0 | Provide Title, Author, Source, License; include license URI | Adaptations under CC BY‑SA 3.0 or later with same elements | “Text adapted from ‘World Wide Web’ (Wikipedia). Authors: contributors. License: CC BY‑SA 3.0. Changes: edited.” | (See References) | Wikipedia | en | Multiple contributors | Edited for brevity | None |
| Algebra | m3r1d1s5 | 2025‑08‑15 | CC BY‑SA 3.0 | Provide Title, Author, Source, License | Adaptations under CC BY‑SA 3.0 | “Text from ‘Algebra’ (Wikibooks). Authors: contributors. License: CC BY‑SA 3.0. Changes: formatting.” | (See References) | Wikibooks | en | Multiple contributors | Formatting only | None |

When designing your register, align the attribution text to Creative Commons’ recommended TASL framing and ensure the license field references the correct legal code (3.0 versus 4.0). For audit readiness, store the license URI in a durable manner and, if practical, keep a copy of the license text alongside your distribution artifacts.[^1][^3]

## Attribution Templates and Ready‑to‑Use Text

Attribution should be simple, consistent, and easy for recipients to verify. The following templates can be dropped into redistribution packages, with placeholders tailored to your items. Always replace placeholders with concrete values from your register and include a copy or URI to the CC BY‑SA 3.0 license with your distribution.

Basic text attribution (unmodified):
- Template: “Title: {title}. Author: {author}. Source: {source_url}. License: CC BY‑SA 3.0. Changes: None.”
- Example: “Title: World Wide Web. Author: Contributors. Source: (see References). License: CC BY‑SA 3.0. Changes: None.”

Adapted text attribution:
- Template: “Adapted from ‘{title}’ ({project}). Authors: {author}. Source: {source_url}. License: CC BY‑SA 3.0. Changes: {change_summary}.”
- Example: “Adapted from ‘Algebra’ (Wikibooks). Authors: Contributors. Source: (see References). License: CC BY‑SA 3.0. Changes: Edited for length and formatting.”

Wikibooks adaptation attribution:
- Template: “Text adapted from {page_title} (Wikibooks). Authors: Contributors. Source: {source_url}. License: CC BY‑SA 3.0. Changes: {change_summary}.”

Multiple sources:
- Template: “This work includes content from:
  - ‘{title1}’ ({project1}). Authors: {author1}. Source: {source_url1}. License: CC BY‑SA 3.0. Changes: {change1}.
  - ‘{title2}’ ({project2}). Authors: {author2}. Source: {source_url2}. License: CC BY‑SA 3.0. Changes: {change2}.”

License notice block (include once per distribution):
- “This work is provided under the Creative Commons Attribution–ShareAlike 3.0 Unported (CC BY‑SA 3.0) license. A copy of the license is available at the Creative Commons legal code (see References).”

For social media posts and other constrained formats, follow platform‑appropriate practices: place the attribution text near the content (for example, in the caption or a comment), include a link to the source, and include the license designation “CC BY‑SA 3.0.” Avoid placing attribution only in metadata fields or alt text; while helpful, these are often not visible to users and do not satisfy the visibility requirement on their own.[^3][^10]

## Compliance Workflow and QA Checklist

A disciplined workflow prevents compliance errors and builds institutional memory. The steps below assume you will populate a license register and maintain attribution templates as the single source of truth for downstream packaging.

Content ingestion and provenance capture:
- Capture page title, revision identifier, timestamp, and source URL.
- Confirm the license applicable to that revision (CC BY‑SA 3.0 versus 4.0).
- Identify any non‑text media and verify their individual licenses on description pages.

Attribution drafting:
- Draft attribution text using TASL and the templates above.
- For adaptations, include a clear “Changes” note and ensure adaptation credits are prominent.

Share‑alike determination:
- Determine if your reuse constitutes an adaptation.
- If yes, license the adaptation under CC BY‑SA 3.0 (or later version with same elements) and include the license copy or URI in the distribution package.

QA verification:
- Confirm all attribution elements are present and reasonably visible.
- Ensure the license copy or URI is included for both unmodified text and adaptations.
- Confirm that no additional or restrictive terms or effective technological measures have been applied.
- Verify that non‑text media licenses are compatible with free reuse; exclude non‑free media unless governed by an EDP relevant to your context.

Redistribution and documentation:
- Publish or ship attribution credits and license notices with the content.
- Keep a changelog for adapted content and update the license register accordingly.

Periodic reconciliation:
- Check for updates to the license version on the source pages; if migrated to CC BY‑SA 4.0, update register entries and templates to reflect the new governing license for later revisions.

Table 8 offers a condensed QA checklist.

Table 8. Compliance QA checklist

| Step | Verification | Status |
|---|---|---|
| Provenance capture | Revision ID, dump date, source URL recorded |  |
| License confirmation | CC BY‑SA 3.0 verified for the revision used |  |
| Attribution completeness | TASL present; adaptation credit where applicable |  |
| License notice included | CC BY‑SA 3.0 license copy or URI present |  |
| Share‑alike assessment | Adaptation identified; correct license applied |  |
| Non‑text media check | Each file’s license verified; free licenses only |  |
| No restrictive terms | No additional terms or DRM applied |  |
| Documentation | Attribution and changelog included in package |  |
| Reconciliation | Register updated for license/version changes |  |

[^1][^4][^5]

## Legal Disclaimers and Risk Controls

CC licenses disclaim warranties; the work is offered “as‑is,” and licensors disclaims liability to the fullest extent permitted by law. Attribution must not imply endorsement without separate, express permission. These standard limitations underscore the importance of accurate attribution, careful documentation, and avoiding statements that could be construed as sponsorship or endorsement claims.[^1]

Respect moral rights. Do not distort, mutilate, or otherwise take derogatory action in relation to the work that would prejudice the original author’s honor or reputation. If your modifications could be seen as derogatory in a given jurisdiction, seek guidance and consider adjusting how changes are presented.[^1]

U.S. government works present a particular edge case. Works produced by U.S. federal government employees within the scope of employment are generally in the public domain in the United States under 17 U.S.C. § 105, but may be copyrighted elsewhere. Not all works republished by U.S. government agencies are public domain; contractor works or stock photography remain under copyright. When in doubt, verify the source and authorship context before reuse.[^14]

Terms of service can sometimes introduce non‑CC terms that conflict with the license. Avoid imposing additional or different terms through your own policies, and do not use Creative Commons trademarks in ways that suggest endorsement if you are applying restrictions beyond the license. Review your legal boilerplate and distribution terms to ensure they do not negate CC permissions.[^11]

## Appendices

### Appendix A: License register schema with required/optional fields and examples

Table A1. License register schema (field‑level specification)

| Field | Type | Required | Notes |
|---|---|---|---|
| page_title | string | Yes | Canonical title for the page |
| wikipedia_revision_id | string | Yes | Stable identifier for the specific revision |
| dump_date | date | Yes | Extraction or dump date |
| license_type | string | Yes | Enumerated values (e.g., CC BY‑SA 3.0) |
| attribution_requirements | string | Yes | Short TASL summary and notices |
| share_alike_obligations | string | Yes | Short SA summary for adaptations |
| specific_attribution_text | string | Yes | Ready‑to‑use credit line |
| source_url | string | No | Exact page or revision URL |
| project | string | No | Wikipedia or Wikibooks |
| language | string | No | Language code |
| authorship_notes | string | No | Optional transparency on contributors |
| change_log | string | No | Summary of modifications |
| media_license_summary | string | No | Non‑text license summary |

### Appendix B: Full attribution template library

Basic unmodified text:
- “Title: {title}. Author: {author}. Source: {source_url}. License: CC BY‑SA 3.0. Changes: None.”

Adapted text:
- “Adapted from ‘{title}’ ({project}). Authors: {author}. Source: {source_url}. License: CC BY‑SA 3.0. Changes: {change_summary}.”

Wikibooks specific:
- “Text adapted from {page_title} (Wikibooks). Authors: Contributors. Source: {source_url}. License: CC BY‑SA 3.0. Changes: {change_summary}.”

Multiple sources:
- “This work includes content from:
  - ‘{title1}’ ({project1}). Authors: {author1}. Source: {source_url1}. License: CC BY‑SA 3.0. Changes: {change1}.
  - ‘{title2}’ ({project2}). Authors: {author2}. Source: {source_url2}. License: CC BY‑SA 3.0. Changes: {change2}.”

License notice block:
- “This work is provided under the Creative Commons Attribution–ShareAlike 3.0 Unported (CC BY‑SA 3.0) license. A copy of the license is available at the Creative Commons legal code (see References).”

### Appendix C: Glossary

- Adaptation: A work based upon the original work (for example, translation, derivative work, arrangement), excluding mere collections.[^1]
- Collection: An aggregation of separate independent works assembled into a collective whole; the original work remains unmodified within it.[^1]
- License Elements: The high‑level attributes of a CC license; for BY‑SA, Attribution and ShareAlike.[^1]
- Licensor: The person or entity offering the work under the license.[^1]
- Original Author: The creator or publisher of the work where no individual can be identified.[^1]
- Share‑Alike: A copyleft condition requiring adaptations to be licensed under the same or compatible license.[^1]
- TASL: Creative Commons recommended attribution framework—Title, Author, Source, License.[^3]

### Appendix D: Citation mapping

- Licensing foundations and legal obligations are supported by CC BY‑SA 3.0 legal code and Creative Commons attribution guidance.[^1][^3]
- Wikipedia licensing evolution and reuser obligations are supported by Wikipedia:Copyrights and the CC 4.0 transition announcement.[^4][^2]
- Non‑text media handling and free content expectations are supported by Wikipedia:Copyrights, Wikimedia Commons:Licensing, and the Wikimedia Foundation licensing policy.[^4][^6][^5]
- Share‑alike interpretation and scope are supported by Creative Commons share‑alike guidance.[^9]
- Social media attribution specifics are supported by Wikimedia’s guidance on CC BY‑SA and social media.[^10]
- U.S. government public domain edge case is supported by 17 U.S.C. § 105.[^14]

## Information Gaps and How to Manage Them

Some variables are not known at the time of writing and must be captured during implementation:
- Exact list of downloaded Wikimedia files (titles, source pages, revision IDs, dump timestamps).
- Language projects involved (English Wikipedia, Wikibooks, etc.) and whether content remains under CC BY‑SA 3.0 or has transitioned to 4.0 for later revisions.
- Presence of non‑text media and per‑file licenses for each downloaded item.
- Final CSV headers/format preferences (minimum fields are specified above; additions can be negotiated).
- Organizational preferences for attribution formatting and localization.
- Workflow tooling and cadence for license reconciliation.

To close these gaps, use the register to capture the missing fields at ingestion, reconcile on a defined schedule, and maintain a change‑control log that reflects updates to license versions or attribution text.

## Maintaining Alignment with CC BY‑SA 4.0 for Newer Revisions

If a page revision is dated after the project’s transition to CC BY‑SA 4.0, your obligations align to 4.0. The attribution text and templates remain similar, with TASL forming the backbone. You should update your register and attribution templates to reference CC BY‑SA 4.0 for those later revisions, include the 4.0 license copy or URI, and note the difference between 3.0 and 4.0 items in your distribution packages. Where both 3.0 and 4.0 items appear in the same collection, maintain clear labeling so recipients can follow the correct license for each item.[^2][^3][^4]

## References

[^1]: Creative Commons. Legal Code — Attribution-ShareAlike 3.0 Unported (CC BY‑SA 3.0). https://creativecommons.org/licenses/by-sa/3.0/legalcode.en

[^2]: Creative Commons. Wikipedia moves to CC 4.0 licenses. https://creativecommons.org/2023/06/29/wikipedia-moves-to-cc-4-0-licenses/

[^3]: Creative Commons Wiki. Recommended practices for attribution. https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution

[^4]: Wikipedia. Wikipedia:Copyrights. https://en.wikipedia.org/wiki/Wikipedia:Copyrights

[^5]: Wikimedia Foundation. Resolution: Licensing policy. https://foundation.wikimedia.org/wiki/Policy:Licensing_policy

[^6]: Wikimedia Commons. Commons:Licensing. https://commons.wikimedia.org/wiki/Commons:Licensing

[^7]: Wikimedia Foundation. Wikipedia — Wikimedia Foundation. https://wikimediafoundation.org/what-we-do/wikimedia-projects/wikipedia/

[^8]: Wikipedia. Wikipedia:Attribution. https://en.wikipedia.org/wiki/Wikipedia:Attribution

[^9]: Creative Commons Wiki. ShareAlike interpretation. https://wiki.creativecommons.org/wiki/ShareAlike_interpretation

[^10]: Meta-Wiki. Legal/CC BY-SA licenses and social media. https://meta.wikimedia.org/wiki/Legal/CC_BY-SA_licenses_and_social_media

[^11]: Wikimedia Foundation. Policy: Terms of Use. https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use

[^12]: Wikipedia. Wikipedia:Image use policy. https://en.wikipedia.org/wiki/Wikipedia:Image_use_policy

[^13]: Wikipedia. Reusing Wikipedia content. https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content

[^14]: Cornell Law School. 17 U.S. Code § 105 - Subject matter of copyright; United States Government works. https://www.law.cornell.edu/uscode/text/17/105

[^15]: Wikibooks. Wikibooks:Creative Commons Attribution-ShareAlike 3.0 Unported License. https://en.wikibooks.org/wiki/Wikibooks:Creative_Commons_Attribution-ShareAlike_3.0_Unported_License

[^16]: Wikibooks. Wikibooks:Copyrights. https://en.wikibooks.org/wiki/Wikibooks:Copyrights