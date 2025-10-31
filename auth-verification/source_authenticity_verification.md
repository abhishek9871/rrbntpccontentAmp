# Source Authenticity Verification: RRB Government Sources and Portal Papers

## Executive Summary

This report provides a forensic assessment of authenticity for official Railway Recruitment Board (RRB) government domains and associated documents, with a parallel audit of portal-collected “previous papers” and practice materials. The goal is to determine which sources are genuine, what evidentiary markers substantiate their authenticity, and how portal materials should be categorized and handled in downstream use.

Sixteen RRB domains were in scope. All sixteen exhibit government branding and National Informatics Centre (NIC) or Government of India affiliations typical of official sites. Seven domains returned verifiable content during this review window: RRB Chandigarh, Chennai, Kolkata, Secunderabad, Bhopal, Ranchi, and Guwahati.[^4][^3][^2][^1][^6][^5][^7] Two major access barriers were observed: RRB Mumbai is currently inaccessible (ERR_CONNECTION_REFUSED), and RRB Bangalore experienced timeouts with unexpected redirects away from the official domain.[^16][^17][^18] A typographical anomaly exists in the official-papers catalog for RRB Malda (non-ASCII characters in the URL), which must be corrected before use.[^30]

On the documents side, authoritative artifacts—including Centralized Employment Notices (CENs), official results PDFs, and the centralized RRB application portal—exhibit consistent government branding, bilingual layouts, CEN identifiers, and explicit references to official RRB websites. Selected CEN PDFs (CEN 05/2025 JE/DMS/CMA) present structured government layouts with “Government of India, Ministry of Railways” headers and detailed annexures, reinforcing authenticity.[^10][^11][^12] By contrast, portal-collected materials from ExamCart and Prepp consistently carry commercial attribution, are explicitly labeled as memory-based or practice content, and cite non-government CDNs as download sources—underscoring that they are not official RRB outputs.[^14][^15]

Key risks include domain inaccessibility (Mumbai, Bangalore), a corrupted URL for Malda in the catalog, and the potential to conflate commercial practice materials with official outputs. Mitigations include: (i) confirming CEN publication and updates via the official RRB application portal and RRB websites; (ii) monitoring and rechecking inaccessible domains for restoration; (iii) correcting catalog typos; and (iv) enforcing clear labeling and usage constraints for portal-collected items.

To contextualize the official artifacts, the following image shows the header/branding of a verified CEN PDF, illustrating the government markers that underpin authenticity.

![CEN 05/2025 JE English PDF header/branding verification](.pdf_temp/viewrange_1_5_1761850891/images/9qfsk9.jpg)

Table 1 summarizes outcomes at a glance and sets the stage for deeper analysis in subsequent sections.

Table 1. Verification outcome summary (domains/documents)

| Category | Count | Notes |
|---|---:|---|
| Official RRB domains verified (accessible) | 7 | Chandigarh, Chennai, Kolkata, Secunderabad, Bhopal, Ranchi, Guwahati[^4][^3][^2][^1][^6][^5][^7] |
| Official RRB domains inaccessible | 2 | Mumbai (ERR_CONNECTION_REFUSED), Bangalore (timeouts/redirect)[^16][^17][^18] |
| Official RRB domains with incomplete extraction | 7 | Patna, Allahabad/Prayagraj, Thiruvananthapuram, Siliguri, Muzaffarpur, Gorakhpur, Malda (catalog anomaly) |
| Official documents verified | 6 | RRB Kolkata CEN page; Secunderabad results PDF; Chennai CBT2 shortlist PDF; answer key/objection tracker; application portal[^2][^8][^9][^13][^12] |
| Portal-collected papers reviewed | 4 | ExamCart (2017 CBT2, 2020 CBT1), Prepp (2024 CBT1)[^14][^15] |

## Scope, Data Sources, and Methodology

The assessment draws from two primary catalogs: (i) an RRB sources catalog covering sixteen RRB domains with fields for official domain, hosting, contact details, notices pages, and exam pages; and (ii) an official papers catalog enumerating government-hosted PDFs and pages. It also reviews local collections of portal-downloaded materials organized by Computer Based Test (CBT) stage and year, alongside selected official CEN PDFs present in the local downloads directory.

Verification followed a layered approach:

- Domain and branding verification: Confirmed government domain patterns (.gov.in), NIC/Government hosting markers, official logos, and anti-fraud disclaimers typical of authentic RRB sites.
- Document-level verification: Validated CENs and results for header/footer structures, government branding, CEN identifiers, bilingual versions, and explicit references to official RRB sites.
- Cross-referencing: Linked portal materials to their origin pages and direct download endpoints; validated that portal items are memory-based/practice content with commercial attribution, not official outputs.
- Controlled comparisons: Contrasted the structure and provenance of government artifacts against portal items, with side-by-side exhibits demonstrating key differences.

All evidence logging has been consolidated for auditability. Where access barriers were encountered, failure modes and next checks are documented for revalidation.

## Government Domain Verification (RRB Boards)

The corpus comprised sixteen RRB domains. Seven domains returned verifiable content with government branding and NIC hosting indicators, two were inaccessible or unstable, and seven require follow-up due to extraction failures or catalog anomalies.

![Official RRB page example: Chandigarh CEN updates](browser/screenshots/current_page.png)

The image above, from the RRB Chandigarh site, exemplifies the standard RRB layout: government branding, CEN updates, and bilingual access, all consistent with official publications.[^4]

Table 2 details domain-by-domain outcomes, infrastructure indicators, and verification status.

Table 2. RRB domain verification matrix

| Board | Official Domain | Hosting | Branding/Seals | Notices/Exam Links | Status | Notes |
|---|---|---|---|---|---|---|
| Chandigarh | rrbcdg.gov.in | NIC/Government | Indian Railways/NIC logos | CEN pages, candidate login | Verified | Recent CEN 05/2025; bilingual site[^4] |
| Mumbai | rrbmumbai.gov.in | NIC/Government | Standard RRB header | Multiple notice sections | Inaccessible | ERR_CONNECTION_REFUSED during session[^16] |
| Chennai | rrbchennai.gov.in | NIC/Government | Government of India, Ministry of Railways | CEN pages; public disclosure | Verified | Image-based navigation; bilingual[^3] |
| Bangalore | rrbbnc.gov.in | NIC/Government | Standard government site | Various CEN notices | Inaccessible | Timeouts; redirect observed[^17][^18] |
| Kolkata | rrbkolkata.gov.in | NIC | Ministry of Railways branding | CEN pages, archives | Verified | Comprehensive CEN coverage[^2] |
| Delhi (RRCB) | rrcb.gov.in | Government | RRCB structure | Employment notices | Pending | Needs live check and extract |
| Prayagraj (Allahabad) | rrbpryj.gov.in | Government | Bilingual support | Notices section | Pending | Extract incomplete; follow-up required |
| Bhopal | rrbbhopal.gov.in | NIC | Official disclaimers | CEN pages, objection tracker | Verified | Extensive CENs; bilingual[^6] |
| Patna | rrbpatna.gov.in | NIC | Standard RRB branding | CEN pages | Pending | Extraction incomplete; re-try needed |
| Ranchi | rrbranchi.gov.in | NIC | Government of India/ MeitY links | Packages-based notices | Verified | Last updated 30-10-2025[^5] |
| Thiruvananthapuram | rrbthiruvananthapuram.gov.in | Government | Government branding | CEN pages; objection tracker | Pending | Extraction incomplete; re-try needed |
| Guwahati | rrbguwahati.gov.in | NIC | Government of India/ NIC logos | Employment notices | Verified | Bilingual; anti-fraud warning[^7] |
| Siliguri | rrbsiliguri.gov.in | NIC | Government branding | Employment notices | Pending | Extraction incomplete; re-try needed |
| Muzaffarpur | rrbmuzaffarpur.gov.in | NIC | Portal-based notices | Notice board | Pending | Extraction incomplete; re-try needed |
| Gorakhpur | rrbgkp.gov.in | NIC | Table-based navigation | CEN pages | Pending | Extraction incomplete; re-try needed |
| Malda | rrbmaldain.gov.in (catalog) | NIC (catalog) | Government branding | Employment notices | Anomalous | URL contains non-ASCII characters; correction needed[^30] |

### Accessible and Verified Domains

RRB Chandigarh returns a fully featured official site with CEN 05/2025 and candidate services. RRB Chennai and Kolkata present extensive CEN coverage with bilingual content. RRB Secunderabad provides a deep archive including question papers, results, and centralized employment notices. RRB Bhopal displays comprehensive CEN coverage, objection tracker links, and anti-fraud messaging. RRB Ranchi uses a package-based notice structure with clear CEN postings. RRB Guwahati exhibits typical government branding with bilingual navigation and anti-fraud warnings.[^4][^3][^2][^1][^6][^5][^7]

### Inaccessible or Problematic Domains

RRB Mumbai refused connections during this session, and RRB Bangalore experienced timeouts with an unexpected offsite redirect—both indicative of hosting instability or maintenance windows.[^16][^17][^18] These sites require re-access attempts and confirmation of official status. Additionally, a typographical anomaly in the official-papers catalog for RRB Malda (non-ASCII characters in the domain) must be corrected to avoid link rot and misdirection.[^30]

## Official Papers and Documents Verification

Official artifacts display consistent, government-grade branding, explicit CEN identifiers, and routine references to official RRB sites for application and updates. The RRB application portal centralizes candidate services and links to CENs, reinforcing provenance.[^12] Answer key and objection tracker endpoints exist behind authenticated candidate logins—another hallmark of official processes.[^13]

![CEN document header/branding verification example](.pdf_temp/viewrange_1_5_1761850891/images/xbp7fc.jpg)

The header/branding shown above (CEN 05/2025) presents “Government of India, Ministry of Railways” and a structured CEN format with annexures—a repeatable pattern across official notifications.[^10][^11]

Table 3 catalogs verified official documents and the evidentiary markers supporting authenticity.

Table 3. Verified official documents

| Board/Portal | Year | Type | Format | Evidence/Markers | Ref |
|---|---|---|---|---|---|
| RRB Kolkata CEN page | 2024 | CEN 05/2024 | HTML | Official CEN page, government branding, archives | [^2] |
| RRB Secunderabad results | 2024 | CBT1→CBT2 results | PDF | CEN 05/2024 branding, multi-page result document | [^8] |
| RRB Chennai shortlist | 2024 | CBT2 shortlist | PDF | CEN 05/2024 branding, shortlisted candidates list | [^9] |
| RRB (centralized) answer key | 2019 | CBT1 key viewing | HTML | Authenticated viewing portal; official domain | [^13] |
| RRB (centralized) objection tracker | 2019 | CBT1 objections | HTML | Authenticated tracker; official domain | [^13] |
| RRB application portal | 2019–2025 | Applications | HTML | Centralized application site; official government portal | [^12] |

### CEN 05/2025 (JE/DMS/CMA) Authenticity Assessment

CEN 05/2025 is present and verified through both RRB Chandigarh and RRB Secunderabad, with bilingual English/Hindi PDFs and an application window scheduled to open 31 October 2025. The document structure includes “Government of India, Ministry of Railways” headers, a detailed table of contents, annexures (e.g., vacancy distributions and syllabi), and explicit references to applying via official RRB websites—coherent with standardized CEN formatting.[^10][^11][^4]

![CEN 05/2025 first page text block](.pdf_temp/viewrange_1_5_1761850891/images/0luc60.jpg)

The formatted text block above highlights consistent government document styling, standardized numbering, and bilingual dissemination, all of which serve as strong authenticity markers.[^11]

## Portal-Collected Papers Verification

Four portal-collected items were examined: ExamCart (2017 CBT2 and 2020 CBT1) and Prepp (2024 CBT1). Across these files, evidence of commercial provenance is explicit: origin pages from exam-preparation portals, CDNs affiliated with those portals, and labeling that identifies the content as memory-based or practice sets. None present government seals or CEN identifiers. These attributes categorically mark them as non-official.

Table 4 contrasts portal items against official artifacts, emphasizing source, markers, and labeling.

Table 4. Portal papers vs official artifacts

| Item | Source Domain | Year/Stage | Content Labeling | Markers (gov. seals/CEN IDs) | Notes | Ref |
|---|---|---|---|---|---|---|
| CBT2 2017 Jan 17 Shift 1 | ExamCart/Collegedunia CDN | 2017 CBT2 | Question paper (practice) | None | Commercial portal; non-government CDN | [^14] |
| CBT1 2020 Dec 28 Shift 1 | ExamCart/Prepp CDN | 2020 CBT1 | Question paper (practice) | None | Explicit portal branding and CDN | [^14] |
| CBT1 2024 Jun 06 Shift 2 | Prepp | 2024 CBT1 | Memory-based questions | None | Practice/memory-based labeling | [^15] |

### ExamCart (2017 CBT2, 2020 CBT1)

Origin pages confirm ExamCart as the source. Direct downloads route through non-government CDNs. Files lack government seals or CEN identifiers and use branding consistent with commercial exam-prep publishers rather than official RRB outputs.[^14]

### Prepp (2024 CBT1)

The Prepp item is explicitly labeled “memory-based questions,” signaling that it is a reconstruction or recollect-ion rather than an official release. The CDN and portal branding further reinforce non-official provenance.[^15]

## Cross-Reference and Pattern Analysis

Authentic RRB artifacts share consistent patterns: “Government of India, Ministry of Railways” headers; CEN identifiers; bilingual versions; structured annexures; and explicit directions to apply via official RRB websites. Navigation commonly features “Employment Notices,” “Archives,” and “Results,” alongside anti-fraud disclaimers and helplines. These attributes align with NIC-hosted sites and the centralized application portal.[^1][^2][^12]

Portal items do not mirror these markers. Instead, they present commercial branding, memory-based or practice labels, and non-government CDNs. These differences are diagnostic: official CEN PDFs and results are identifiable by header structure, CEN numbering, and government provenance; portal materials should never be treated as official releases.

Table 5 provides a side-by-side comparison that underscores these distinctions.

Table 5. Pattern comparison—official vs portal

| Feature | Official RRB artifacts | Portal-collected papers |
|---|---|---|
| Header/branding | Government of India, Ministry of Railways; RRB branding | Commercial portal branding |
| CEN identifiers | Explicit CEN numbers and annexures | None |
| Language | Bilingual (English/Hindi) | Often English only |
| Hosting | Government/NIC domains (.gov.in) | Commercial portals and CDNs |
| Content labeling | CEN, results, schedules, FAQs | Memory-based, practice sets |
| Access | Public CEN PDFs; authenticated candidate services for keys/objections | Public downloads from portal CDNs |

## Findings: Authenticity Status and Risk Assessment

The evidence supports a high-confidence determination of authenticity for verified government domains and documents. Simultaneously, several medium-risk items require remediation or monitoring.

Table 6. Risk register

| Item | Category | Risk Level | Evidence | Recommended Action |
|---|---|---|---|---|
| RRB Mumbai domain | Domain | High | ERR_CONNECTION_REFUSED | Monitor and recheck; confirm official status post-restoration[^16] |
| RRB Bangalore domain | Domain | High | Timeouts; redirect to offsite | Retry access; validate DNS/hosting; confirm official status[^17][^18] |
| Malda URL anomaly | Catalog | Medium | Non-ASCII characters in URL | Correct catalog entry; verify live domain[^30] |
| Patna, Prayagraj, Thiruvananthapuram, Siliguri, Muzaffarpur, Gorakhpur | Domain | Medium | Incomplete extraction | Re-visit with browser interaction; capture CEN snapshots |
| Portal materials (ExamCart/Prepp) | Document | Medium | Commercial attribution, memory-based labeling | Label as non-official; restrict usage to practice; avoid redistribution |
| Authenticated portals (answer key/objection tracker) | Access | Low | Login required | Accept as official endpoints; document access constraints[^13] |

### High-Risk Issues

Two domains are currently inaccessible or unstable. The RRB Mumbai site refused connections, and RRB Bangalore exhibited timeouts and unexpected redirects. These failure modes demand follow-up checks to restore confidence in domain integrity and to ensure candidates can access official notices and services.[^16][^17][^18]

### Medium-Risk Issues

Seven domains showed incomplete extraction and require re-verification. Additionally, the Malda URL anomaly in the official-papers catalog must be corrected to avoid user confusion and link failures.[^30] Portal materials should be handled with clear labeling and usage restrictions to prevent misinterpretation as official releases.

## Recommendations and Next Steps

To consolidate authenticity assurance and ensure reliable use of materials, the following steps are advised:

1. Immediate re-attempts for domains with extraction failures or access issues—using browser-based interaction where necessary—to capture CEN snapshots and verify branding and hosting.
2. Correction of the Malda URL anomaly in the official-papers catalog, with a live-domain verification pass.
3. Explicit labeling of portal-collected papers as non-official practice/memory-based materials and application of usage constraints to prevent conflation with official outputs.
4. Integration of the centralized RRB application portal as the authoritative anchor for cross-referencing CEN publication status and application windows.
5. Documentation and periodic revalidation of domain status, with particular attention to stability and potential redirections.

Table 7 outlines an action plan to close open items and institutionalize ongoing checks.

Table 7. Action plan tracker

| Task | Target | Evidence Required | Owner | Due Date |
|---|---|---|---|---|
| Re-attempt extraction for Patna, Prayagraj, Thiruvananthapuram, Siliguri, Muzaffarpur, Gorakhpur | Domain-level snapshots and CEN confirmations | Screenshots, extracted content, CEN links | Verification Team | Within 5 business days |
| Restore and verify RRB Mumbai | Domain restoration confirmation | Successful load, government branding, CENs | Verification Team | Within 3 business days |
| Restore and verify RRB Bangalore | Domain restoration and DNS validation | Successful load; no redirects; CENs | Verification Team | Within 3 business days |
| Correct Malda URL | Catalog entry | Verified live domain and notices page | Catalog Maintainer | Immediate |
| Portal materials labeling | All portal files | Labels and usage constraints applied | Content Operations | Immediate |
| CEN cross-reference via rrbapply | Active CENs | Portal links and CEN confirmations | Verification Team | Ongoing, weekly during recruitment cycles |

## Appendix A: Evidence Index

Table 8 maps major artifacts to their reference markers and the authenticity markers observed.

Table 8. Evidence index

| Artifact | Reference(s) | Authenticity Markers |
|---|---|---|
| RRB Secunderabad archives (notices, question papers) | [^1] | Government domain; archives for CENs; results; official branding |
| RRB Kolkata CEN pages | [^2] | Official CEN pages; government branding; archives and panels |
| RRB Chandigarh CEN 05/2025 updates | [^4] | Government branding; bilingual CEN updates; candidate services |
| RRB application portal | [^12] | Centralized government portal; explicit CEN/application integration |
| RRB answer key/objection tracker | [^13] | Authenticated candidate portals; official endpoints |
| CEN 05/2025 JE/DMS/CMA (English PDF) | [^10] | Government header; structured CEN; annexures |
| CEN 05/2025 JE/DMS/CMA (Hindi PDF) | [^11] | Bilingual version; consistent government structure |
| Portal ExamCart origin | [^14] | Commercial attribution; non-government CDN endpoints |
| Portal Prepp origin | [^15] | Memory-based labeling; commercial attribution |

## Appendix B: Verification Log Excerpts

- RRB Mumbai: Complete connection refusal (ERR_CONNECTION_REFUSED) recorded; no content accessible; retry scheduled.[^16]
- RRB Bangalore: Timeouts observed; unexpected redirect to an offsite domain noted; restoration check and DNS validation recommended.[^17][^18]
- RRB Chandigarh: Verified government branding; CEN 05/2025 bilingual PDFs and application window announcements accessible.[^4]
- RRB Kolkata: Verified CEN 05/2024 page and comprehensive notices/archives structure.[^2]
- RRB Chennai: Verified site with extensive CEN listings and public disclosure sections.[^3]
- RRB Bhopal: Verified CEN pages, objection tracker references, and anti-fraud disclaimers.[^6]
- RRB Ranchi: Verified package-based notices and last-updated stamp (30-10-2025).[^5]
- RRB Guwahati: Verified NIC hosting, bilingual content, and anti-fraud messaging.[^7]
- CEN 05/2025 JE/DMS/CMA PDFs: Verified government headers, structured annexures, and bilingual publication.[^10][^11]
- Portal materials: Verified commercial provenance and memory-based/practice labeling; non-government CDNs; no official seals or CEN identifiers.[^14][^15]

---

## References

[^1]: RRB Secunderabad Archives - Employment Notices. https://rrbsecunderabad.gov.in/archive_type/employment-notices/
[^2]: RRB Kolkata CEN 05/2024. https://rrbkolkata.gov.in/cen052024.php
[^3]: RRB Chennai Official Website. https://rrbchennai.gov.in/
[^4]: RRB Chandigarh Official Website. https://www.rrbcdg.gov.in/
[^5]: RRB Ranchi Official Website. https://rrbranchi.gov.in/
[^6]: RRB Bhopal Official Website. https://rrbbhopal.gov.in/
[^7]: RRB Guwahati Official Website. https://www.rrbguwahati.gov.in/
[^8]: RRB Secunderabad CEN 05/2024 NTPC Graduate CBT1 to CBT2 Results. https://rrbsecunderabad.gov.in/CEN05-2024-CBT1-to-CBT2-Results-CEN-05-2024-NTPC-Graduate.pdf
[^9]: RRB Chennai CEN 05/2024 NB Candidates Shortlisted for CBT-2. https://rrbchennai.gov.in/CEN-05-2024-NB-Candidates-shortlisted-for-CBT-2.pdf
[^10]: CEN 05/2025 JE/DMS/CMA - English (Official PDF). https://rrbsecunderabad.gov.in/wp-content/uploads/2025/10/CEN-5_2025_JE_DMS_CMA_-English_-28.10.2025.pdf
[^11]: CEN 05/2025 JE/DMS/CMA - Hindi (Official PDF). https://rrbsecunderabad.gov.in/wp-content/uploads/2025/10/CEN-5_2025_JE_DMS_CMA_-Hindi_-28.10.2025.pdf
[^12]: RRB Application Portal. https://rrbapply.gov.in/
[^13]: RRB Answer Key Viewing Portal. https://rrb.digialm.com/EForms/configuredHtml/15/1119/1527/Form_AnsKey.html
[^14]: ExamCart RRB NTPC Previous Year Question Papers (CBT 1 & 2). https://examcart.in/community/blogs/rrb-ntpc-previous-year-question-paper-download-pdf-for-cbt-1-and-2
[^15]: Prepp RRB NTPC Memory Based Questions CBT 1 (June 2024). https://prepp.in/news/e-769-rrb-ntpc-memory-based-questions-cbt-1-for-june-2025
[^16]: RRB Mumbai Official Website. https://www.rrbmumbai.gov.in/
[^17]: RRB Bangalore Official Website (HTTP). http://www.rrbbnc.gov.in/
[^18]: RRB Bangalore Official Website (HTTPS). https://rrbbnc.gov.in/
[^19]: RRB Patna Official Website. https://www.rrbpatna.gov.in/
[^20]: RRB Allahabad (Prayagraj) Official Website. https://rrbpryj.gov.in/
[^21]: RRB Thiruvananthapuram Official Website. https://www.rrbthiruvananthapuram.gov.in/
[^22]: RRB Siliguri Official Website. https://www.rrbsiliguri.gov.in/
[^23]: RRB Muzaffarpur Official Website (HTTP). http://www.rrbmuzaffarpur.gov.in/
[^24]: RRB Muzaffarpur Official Website (HTTPS). https://rrbmuzaffarpur.gov.in/
[^25]: RRB Gorakhpur Official Website. https://www.rrbgkp.gov.in/
[^26]: RRB Bilaspur Official Website. https://rrbbilaspur.gov.in/
[^27]: RRB Ahmedabad Official Website. https://rrbahmedabad.gov.in/
[^28]: RRB Secunderabad Official Website. https://rrbsecunderabad.gov.in/
[^29]: RRB Chennai CEN 03/2015 Shortlisted Candidates 2nd Stage Examination. https://rrbchennai.gov.in/CEN-03-2015-shortlisted-18candidates-2nd-stage-examination.pdf
[^30]: Official Papers Catalog (Local File). /workspace/metadata/official_papers_catalog.csv
[^31]: RRB Sources Catalog (Local File). /workspace/metadata/rrb_sources_catalog.csv
[^32]: RRB Ranchi Packages/Notices. https://rrbranchi.gov.in/?p=packages
[^33]: RRB Guwahati Employment Notices. https://www.rrbguwahati.gov.in/
[^34]: RRB Secunderabad Question Papers Archive. https://rrbsecunderabad.gov.in/archive_type/question-papers/
[^35]: RRB Kolkata CEN 05/2024 (duplicate reference). https://rrbkolkata.gov.in/cen052024.php
[^36]: RRB Chandigarh CEN 05/2025 JE/DMS/CMA English PDF (local copy). /workspace/downloads/CEN_05_2025_JE_English.pdf