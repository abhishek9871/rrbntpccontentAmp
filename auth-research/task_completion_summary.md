# Access Methods, Authentication Requirements, and Downloadable Content Across RRB Digital Examination Portals and Related Resources

## Executive Summary

Railway Recruitment Board (RRB) examinations rely on a layered digital ecosystem that blends centralized authentication with regional publication of official information. At the core of candidate-facing services is a TCS iON/Digialm-hosted login, which gates access to personalized examination artifacts. Candidates authenticate with a Registration Number, a password or date of birth (DOB) in page-specific formats, and a captcha, then proceed to services such as admit cards, city intimation, scorecards, and—where configured—answer keys and objection trackers.[^1][^2][^3] Public RRB websites (e.g., RRB Chandigarh and RRB Kolkata) publish notices, results, and shortlists without authentication and serve as the authoritative record for official updates and documents.[^4][^5] In recruitment cycles, RRB portals routinely link candidates to Digialm-hosted services, a pattern reflected in coverage by major education news portals describing login steps to download admit cards and city intimation.[^6][^7]

Within this ecosystem, authentication-protected resources fall into three principal categories: candidate services (admit cards, application viewing), post-examination review (answer keys, objection trackers), and scorecards/results that some boards host post-release. These are uniformly gated behind Digialm candidate login and are not publicly accessible without credentials.[^1][^5][^6] In contrast, public-facing downloads are abundant on official regional sites: for example, RRB Secunderabad publishes a CBT1-to-CBT2 results PDF for CEN 05/2024 and hosts an archive of question papers; RRB Chennai issues official shortlists in PDF form.[^9][^10][^13][^14]

Third-party education platforms offer practice content under diverse access models. Testbook provides numerous previous year paper (PYP) PDFs free and marks some content as “Pro” behind a subscription; Mockers offers free mock tests but requires registration; RRB EXAM PORTAL provides direct downloads while disclaiming any official affiliation.[^15][^16][^17][^18][^19] Candidates should rely on official portals for authentic documents and use third-party sources as practice aids, noting licensing and redistribution constraints.

Immediate implications for candidates are straightforward: use official RRB sites and the Digialm candidate login for authentic artifacts; expect standardized credential entry and captcha challenges; and leverage trusted third-party practice materials with an eye to their licensing. A repeatable flow—Check official CEN page → Follow exam-specific link → Authenticate via Digialm → Download artifact—minimizes friction and reduces exposure to unofficial content.[^4][^5][^1][^6]

## Scope, Sources, and Methodology

This report synthesizes documentation from the TCS iON/Digialm login pages, regional RRB websites, official PDFs, and third-party platforms offering RRB practice content. The research comprised three streams: (1) verification of authentication interfaces and protected services, (2) inventory of publicly accessible official documents, and (3) cross-platform comparison of practice content availability and access requirements. The synthesis relied on authoritative sources: live Digialm login interfaces, RRB Chandigarh and RRB Kolkata as exemplar regional portals, RRB Secunderabad’s results and archives, RRB Chennai’s shortlists, and representative third-party platforms such as Testbook, Mockers, and RRB EXAM PORTAL.[^4][^5][^1][^6]

Ethical boundaries were strictly observed. No attempts were made to access protected content using unauthorized credentials. All protected-resource inferences are based on visible page structures and official descriptions. The scope focused on the dominant RRB digital flow; specialized portals such as document verification (OIRMS) and Aadhaar authentication requirements are noted where referenced in official CEN material but not exhaustively enumerated.[^31][^32]

## Ecosystem Map: Portals, Platforms, and Data Flows

The RRB candidate experience is shaped by four types of portals: the TCS iON/Digialm candidate login, regional RRB websites, the centralized application portal, and document verification services. The Ministry of Railways maintains the authoritative index of RRB regional portals, ensuring consistent navigation and branding across boards.[^8]

Public-facing RRB websites publish CEN notices, schedules, results, and shortlists. During active cycles, these sites link to Digialm-hosted services (e.g., admit card downloads, city intimation), which require candidate authentication. This separation between public information and protected services clarifies the candidate journey: public pages orient and notify; protected pages personalize and deliver artifacts.[^4][^5][^1][^6]

To illustrate the platform context, the following visuals provide an overview of TCS iON’s broader offerings and the exam-preparation sections relevant to government exams.

![TCS iON platform overview (exam hosting context).](browser/screenshots/digialm_main_page.png)

![TCS iON explore categories (indicative services/products).](browser/screenshots/tcs_ion_explore_section.png)

![TCS iON Government Exam Prep (indicative catalog).](browser/screenshots/government_exam_prep.png)

![TCS iON NQT assessment products (indicative catalog).](browser/screenshots/nqt_assessment_products.png)

These images depict a broader assessment and preparation ecosystem that contextualizes Digialm’s role as the secure exam-hosting layer within TCS iON. While the preparation catalogs are not candidate-specific, they help candidates and administrators situate RRB services within a wider set of government exam offerings.

Table 1: Portal Ecosystem Overview

| Portal Type                    | Examples                                  | Public vs Protected                 | Primary Use                                                                 |
|-------------------------------|--------------------------------------------|-------------------------------------|------------------------------------------------------------------------------|
| Candidate Login               | Digialm Candidate Login                    | Protected                           | Candidate authentication; access to admit cards, scorecards, answer keys     |
| Regional RRB Website          | RRB Chandigarh, RRB Kolkata                | Public                              | CEN notices, schedules, results, shortlists                                  |
| Application Portal            | rrbapply.gov.in                            | Protected                           | Application submission and status                                            |
| Document Verification Portal  | OIRMS – RRBDV                              | Protected                           | Aadhaar-authenticated document submission                                    |
| Third-Party Practice Platforms| Testbook, Mockers, RRB EXAM PORTAL         | Public/Registration/Subscription    | Practice tests, PYP PDFs, mock exams (non-official)                          |

## Authentication Requirements and Access Methods (How)

Authentication is consistent and security-focused. Digialm’s candidate login requires a Registration Number, a page-specific password or DOB format, and a captcha. Variants exist: some pages prompt for DOB in ddmmyyyy, others in yyyymmdd; page footers may display a version label (e.g., “Version 10.02.00”). Recovery is supported via a “Get Password” function, and captcha challenges serve as a baseline bot-mitigation control.[^1][^2][^3]

![Candidate login interface (RRB exams via Digialm/TCS iON).](browser/screenshots/rrb_login_interface.png)

This standardized interface simplifies candidate navigation across boards while retaining strong access controls. The reliance on DOB either as password or as an explicit field aligns with common Indian recruitment practices and reduces password-reset friction.

Table 2: Authentication Matrix

| Portal/Service                                 | Required Credentials                 | Captcha | Public/Protected | Typical Artifacts                                             |
|-----------------------------------------------|--------------------------------------|---------|------------------|---------------------------------------------------------------|
| Digialm Candidate Login (1181/2685)           | Registration Number; DOB/password    | Yes     | Protected        | Application form, admit card, city intimation, scorecards     |
| Digialm Admit Card Login (1181/91610)         | Registration Number; DOB/password    | Yes     | Protected        | Admit card downloads                                          |
| Digialm Answer Key Viewing (15/1119/1527)     | Candidate credentials                 | Yes     | Protected        | Official answer keys                                          |
| Digialm Objection Tracker (15/1119/1556)      | Candidate credentials                 | Yes     | Protected        | Objection submission and tracking                             |
| Regional RRB Websites (e.g., Chandigarh, Kolkata)| None                              | No      | Public           | Notices, results, shortlists                                  |
| RRB Application Portal (rrbapply)             | Application credentials               | Yes     | Protected        | Application submission, status                                |
| OIRMS – RRBDV                                 | Aadhaar authentication                | No      | Protected        | Document verification submission                              |

### Primary Candidate Login (Digialm/TCS iON)

Candidates enter credentials through a concise interface designed for scale and security. The captcha requirement deters automated attacks; explicit field labeling (e.g., “Please enter your User Id,” “DOB ddmmyyyy” or “DOB yyyymmdd”) reduces input errors; version markings support operational consistency.[^1][^3]

### Answer Key and Objection Tracker

Post-examination, boards may enable configured Digialm pages to view answer keys and submit objections. These pages are strictly protected; only authenticated candidates associated with a specific examination cycle can access the relevant materials.[^6]

## Content Inventory: What Is Accessible Where (What)

Official public content includes CEN notices, results, and shortlists published by regional boards. These are attested documents suitable for archival reference. Protected content includes candidate-specific artifacts (admit cards, application viewing), answer keys, objection trackers, and scorecards hosted behind Digialm. Third-party content spans previous year papers, memory-based papers, and mock tests under varying access models.

Table 3: Content Inventory Across Official and Third-Party Sources

| Source (Ref ID)                                      | Content Type                         | Access Model         | Notes                                                             |
|------------------------------------------------------|--------------------------------------|----------------------|-------------------------------------------------------------------|
| RRB Chandigarh (23)                                  | Notices, CEN updates                 | Public (No auth)     | Official regional site                                            |
| RRB Kolkata – CEN 05/2024 (24)                       | CEN notices                          | Public (No auth)     | Official regional CEN page                                        |
| RRB Secunderabad – Archives (10)                     | Question papers                      | Public (No auth)     | Historical official papers                                        |
| RRB Secunderabad – Results PDF (13)                  | Official results                     | Public (No auth)     | CBT1 to CBT2 results, CEN 05/2024                                 |
| RRB Chennai – Shortlist PDF (14)                     | Official shortlist                   | Public (No auth)     | CEN 05/2024 CBT2 shortlist                                        |
| Digialm Answer Key Viewing (6)                       | Answer keys                          | Auth required        | Candidate login required                                          |
| Digialm Objection Tracker (7)                        | Objection submission                 | Auth required        | Candidate login required                                          |
| RRB Application Portal (8)                           | Application services                 | Auth required        | Submission, status                                                |
| OIRMS – RRBDV (31)                                   | Document verification                | Aadhaar auth         | Identity verification per CEN guidance                            |
| Testbook – NTPC Previous Year Papers (15)            | PYP PDFs, online tests               | Mixed (free + Pro)   | Many PDFs free; some content requires subscription                |
| RRB EXAM PORTAL – Papers (16)                        | Sample/mock papers                   | No auth              | Direct downloads; not an official site                            |
| RRB EXAM PORTAL – Sample Test (17)                   | Online sample test                   | No auth              | Simulated test instructions                                       |
| Jagran Josh – PYP Article (18)                       | Guidance + links                     | Public (No auth)     |Explains PYP availability                                          |
| Prepp – Practice Papers (19)                         | Practice papers                      | Public (No auth)     |Practice-oriented materials                                        |
| CareerPower – PYP Page (20)                          | Previous year papers                 | Public (No auth)     | Public-facing listing                                             |
| Mockers – NTPC Mock Test (21)                        | Mock tests                           | Registration required| Free tests after account creation                                 |
| ixambee – Free Mock Tests (22)                       | Mock tests                           | Public (No auth)     | Free mock test listing                                            |

### Public RRB Websites (No Authentication)

Regional RRB portals host CEN notices, results, and shortlists. RRB Chandigarh’s official site provides up-to-date notices, while RRB Kolkata’s CEN page consolidates cycle-specific updates. RRB Secunderabad’s archives provide historical official question papers, and RRB Chennai publishes shortlists in PDF form—all without authentication.[^4][^5][^10][^14]

![Regional portal example (RRB Kolkata).](browser/screenshots/rrb_ranchi_homepage.png)

This public layer is the primary source for official documents. Candidates should prefer these sites for verification and archival needs.

### Authentication-Protected RRB Pages (Digialm)

Protected Digialm pages provide candidate-specific services and post-exam tools. Admit card downloads and city intimation are routinely linked through official portals and education coverage; answer key viewing and objection trackers are configured for authenticated access only.[^1][^5][^6][^7]

### Third-Party Platforms (Varying Access Models)

Third-party platforms fill a practice gap with diverse models:
- Testbook offers numerous free PDFs while gating other content (older or comprehensive archives) behind a subscription.[^15]
- RRB EXAM PORTAL provides direct downloads and sample tests but is not affiliated with official RRBs; its disclaimer is explicit.[^16][^17]
- Mockers offers free mock tests contingent on registration; ixambee lists free mock tests accessible without registration.[^21][^22]
- News and prep portals such as Jagran Josh, Prepp, and CareerPower publish guidance and materials with varying access friction.[^18][^19][^20]

## Downloadable Content and Step-by-Step Procedures

Official documents are published as PDFs on regional RRB sites. Third-party practice materials are available under different access models. A repeatable flow reduces friction: identify the official CEN page or notice, follow exam-specific links to Digialm (where applicable), authenticate, and download the artifact.

Table 4: Downloadables and Procedures

| Source (Ref ID)                          | Steps (Simplified)                                      | Auth Needed | File Type | Notes                                                           |
|------------------------------------------|----------------------------------------------------------|-------------|-----------|-----------------------------------------------------------------|
| RRB Secunderabad – Results PDF (13)      | Open results page → Download PDF                         | No          | PDF       | Official results document                                       |
| RRB Chennai – Shortlist PDF (14)         | Open shortlist page → Download PDF                       | No          | PDF       | Official shortlist                                              |
| RRB Secunderabad – Archives (10)         | Open archive → Select paper → Download                   | No          | PDF       | Historical official papers                                      |
| RRB Kolkata – CEN 05/2024 (24)           | Open CEN page → Follow linked PDFs                       | No          | PDF/HTML  | CEN notices and related materials                                |
| Testbook – PYP PDFs (15)                 | Choose shift/year → Download or attempt online           | Mixed       | PDF/Online| Free downloads for many items; Pro for some                      |
| RRB EXAM PORTAL – Papers (16)            | Click paper/test → Download via link                     | No          | PDF/HTML  | Direct downloads; not official                                   |
| RRB EXAM PORTAL – Sample Test (17)       | Open sample test → Review instructions                   | No          | HTML      | Simulated test instructions                                     |
| Mockers – Mock Test (21)                 | Register → Access free mock tests                        | Yes         | Online    | Registration required                                            |
| Jagran Josh – PYP Article (18)           | Follow article guidance → Access provided links          | No          | Article   | Explains availability                                           |
| Prepp – Practice Papers (19)             | Select paper → Download                                  | No          | PDF       | Practice-oriented                                                |
| CareerPower – PYP Page (20)              | Open page → Follow links                                 | No          | PDF       | Public-facing listing                                            |
| RRB Application Portal (8)               | Login → Submit application or check status               | Yes         | Web       | Application submission and status                                |
| OIRMS – RRBDV (31)                       | Aadhaar-authenticated access → Submit documents          | Yes         | Web       | Document verification workflow                                   |

![Illustrative public notice/context (indicative auth-free access).](browser/screenshots/rrb_ranchi_homepage.png)

![Sample test interface (indicative direct-download materials).](browser/screenshots/rrb_ranchi_packages_page.png)

The first image demonstrates public access to official notices, while the second underscores that sample/test interfaces on third-party sites can allow direct downloads or immediate practice without login. Candidates should distinguish official artifacts from third-party practice aids and adhere to licensing terms.

## Regional Variations and Examples

Although the authentication experience is standardized, navigation and content organization differ by region. RRB Kolkata’s CEN page offers cycle-specific notices without requiring login. RRB Chandigarh’s site features live CEN notices. RRB Ranchi provides a packages-oriented notice board. RRB Secunderabad maintains an archive of question papers and publishes official results.[^5][^4][^30][^10]

Table 5: Regional RRB Portal Comparison

| Region/Portal          | Public Content Types                     | Protected Links Presence | Authentication Linkage           | Notable Features                                      |
|------------------------|------------------------------------------|--------------------------|----------------------------------|-------------------------------------------------------|
| RRB Kolkata (24)       | CEN notices, schedules                   | Yes                      | Digialm-linked services          | CEN 05/2024 page consolidates updates                 |
| RRB Chandigarh (23)    | CEN notices, updates                     | Yes                      | Digialm-linked services          | Active notices; shift rescheduling advisories         |
| RRB Ranchi (30)        | Packages (notice groupings), results     | Yes                      | Candidate portal and services    | Structured “packages” navigation                      |
| RRB Secunderabad (10, 13)| Archives, results                      | No (archives/public)     | Links to Digialm for live services| Comprehensive archives; official results PDFs         |

## Access Flow Scenarios (Guided Pathways)

Three common scenarios illustrate the standard candidate pathway.

Table 6: Scenario-Based Access Flow

| Trigger (Notice/Link)                              | Target Portal            | Authentication Steps                                             | Expected Outcome                          | Notes                                           |
|----------------------------------------------------|--------------------------|------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------|
| CEN notice on regional RRB site                    | Regional RRB site        | None (public page)                                               | View notice, schedules                    | Official, attested public information           |
| “Admit Card” or “City Intimation” link from RRB site| Digialm Candidate Login  | Registration Number + DOB/password + captcha                     | Download admit card/city intimation       | Links route to Digialm-hosted services          |
| Post-exam “Answer Key/Objection” link              | Digialm Answer Key/Tracker| Candidate credentials + captcha                                  | View answer key or submit objections      | Access limited to eligible candidates           |

![Access flow starts at regional portal, links to Digialm candidate login.](browser/screenshots/rrb_ranchi_homepage.png)

![Candidate login step (credentials + captcha).](browser/screenshots/rrb_login_interface.png)

This flow ensures candidates transition from public information to protected services without ambiguity. Official coverage from major education portals reiterates the steps for admit card downloads, reinforcing the Digialm login requirement.[^5][^6][^7]

## Security, Compliance, and Ethical Considerations

Authentication mechanisms—captcha challenges and standardized credential entry—are designed to protect candidate data and exam integrity. Candidates must avoid sharing credentials and should rely on official helpdesk channels for support. Third-party platforms vary in provenance; licensing often restricts redistribution and commercial use. Where CEN references Aadhaar-based verification, candidates should complete these steps on authorized portals in compliance with current notices.[^1][^2][^6][^32]

## Recommendations and Best Practices (So What)

Candidates should prioritize official portals for authentic documents and use trusted third-party sources for practice. The following actions simplify access and enhance compliance:

- Start at official RRB sites; use Digialm candidate login for authentic artifacts; expect captcha challenges and standardized credentials.
- Rely on official PDFs for results and shortlists; avoid unverified compilations.
- Use third-party practice materials with clear licensing; prefer platforms offering transparent terms and direct downloads where permissible.
- Keep recovery pathways (e.g., “Get Password”) bookmarked and follow official helpdesk guidance.

Table 7: Best Practices Checklist

| Task                                           | Primary Source            | Access Steps                                            | Key Notes                                              |
|------------------------------------------------|---------------------------|---------------------------------------------------------|--------------------------------------------------------|
| Download admit card/city intimation            | Regional RRB + Digialm    | Follow link → Login (Reg No + DOB/password + captcha)  | Links route to Digialm; save PDFs securely             |
| View official answer keys / submit objections  | Digialm configured pages  | Login → Navigate to key/tracker                         | Access limited to eligible candidates                  |
| Obtain official results/shortlists             | Regional RRB sites        | Open results/shortlist page → Download PDF              | Prefer attested official PDFs                          |
| Practice with previous year papers             | Testbook, RRB EXAM PORTAL | Select shift/year → Download or attempt online          | Note licensing; some content behind subscription       |
| Complete document verification (if applicable) | OIRMS – RRBDV             | Aadhaar-authenticated access → Submit documents         | Follow CEN guidance; ensure identity verification      |

These practices balance security, convenience, and compliance, guiding candidates through official channels while leveraging trusted supplementary resources.[^4][^1][^15]

## Appendices: Source Catalog and Visual Index

A consolidated catalog of sources and visuals used in this report is provided below. Visuals illustrate platform context and public notice navigation.

![Catalog of TCS iON products/services (indicative).](browser/screenshots/tcs_ion_explore_section.png)

![Catalog of Government Exam Prep (indicative).](browser/screenshots/government_exam_prep.png)

![Catalog of NQT assessment products (indicative).](browser/screenshots/nqt_assessment_products.png)

Information gaps acknowledged:
- Digialm login surfaces do not provide public demo/sample papers; protected content remains credential-gated.
- Regional interfaces vary; detailed dashboard navigation inside protected pages was not documented without credentials.
- Third-party licensing terms may evolve; exhaustive capture was not performed.
- A comprehensive list of all RRB portals was not fully enumerated here.
- A complete, up-to-date inventory of public official PDFs across all regions is beyond scope.
- Specialized portals (e.g., OIRMS RRBDV) are referenced; detailed access steps for all candidate scenarios are not exhaustively documented.

---

## References

[^1]: Candidate Login (Digialm/TCS iON) – View/Download Application Form/Admit Card. https://www.digialm.com/EForms/configuredHtml/1181/2685/login.html  
[^2]: RRB Digialm Login – Download Admit Card. https://rrb.digialm.com/EForms/configuredHtml/1181/91610/login.html  
[^3]: Candidate Login (Digialm/TCS iON) – Alternate Version. https://www.digialm.com/EForms/configuredHtml/1181/2683/login.html  
[^4]: RRB Chandigarh – Official Website. https://www.rrbcdg.gov.in/  
[^5]: RRB Kolkata – CEN 05/2024. https://www.rrbkolkata.gov.in/cen052024.php  
[^6]: Shiksha – RRB NTPC Admit Card 2025 Out. https://www.shiksha.com/exams/rrb-ntpc-exam-admit-card  
[^7]: Times of India – RRB NTPC UG 2025 City Intimation Slip Out. https://timesofindia.indiatimes.com/education/news/rrb-ntpc-ug-2025-city-intimation-slip-out-at-rrbapply-gov-in-check-direct-download-link-here/articleshow/122975440.cms  
[^8]: Ministry of Railways – RRBs Website Directory. https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,7,1281  
[^9]: RRB Secunderabad – Official Website. https://rrbsecunderabad.gov.in/  
[^10]: RRB Secunderabad – Question Papers Archive. https://rrbsecunderabad.gov.in/archive_type/question-papers/  
[^11]: RRB EXAM PORTAL – Previous Year Papers, Sample Tests, Mock Papers. https://rrbexamportal.com/papers  
[^12]: RRB EXAM PORTAL – Sample Online Test. https://rrbexamportal.com/papers/online-exams-sample-test  
[^13]: RRB Secunderabad – CBT1 to CBT2 Results CEN 05/2024 NTPC (Graduate) PDF. https://rrbsecunderabad.gov.in/CEN05-2024-CBT1-to-CBT2-Results-CEN-05-2024-NTPC-Graduate.pdf  
[^14]: RRB Chennai – CEN-05-2024 NB Candidates Shortlisted for CBT-2 PDF. https://rrbchennai.gov.in/CEN-05-2024-NB-Candidates-shortlisted-for-CBT-2.pdf  
[^15]: Testbook – RRB NTPC Previous Year Papers (CBT 1 & CBT 2). https://testbook.com/rrb-ntpc/previous-year-papers  
[^16]: RRB EXAM PORTAL – Papers (alternate catalog reference). https://rrbexamportal.com/papers  
[^17]: RRB EXAM PORTAL – Sample Online Test (alternate catalog reference). https://rrbexamportal.com/papers/online-exams-sample-test  
[^18]: Jagran Josh – RRB NTPC Previous Year Question Papers: PDF Download. https://www.jagranjosh.com/articles/rrb-ntpc-previous-year-question-paper-cbt-1-and-cbt-2-pdf-download-1725355852-1  
[^19]: Prepp – RRB NTPC Previous Year Question Papers with Solutions. https://prepp.in/rrb-ntpc-exam/practice-papers  
[^20]: CareerPower – RRB NTPC Previous Year Question Papers PDF. https://www.careerpower.in/rrb-ntpc-previous-year-question-papers.html  
[^21]: Mockers – RRB NTPC Mock Test (Free Online). https://www.mockers.in/exam/rrb-ntpc-mock-test  
[^22]: ixambee – Free Railway RRB Mock Tests. https://www.ixambee.com/free-mock-tests/railways  
[^23]: RRB Chandigarh – Official Website (reference copy). https://www.rrbcdg.gov.in/  
[^24]: RRB Kolkata – Official Website (reference copy). https://www.rrbkolkata.gov.in/  
[^25]: RRB Ranchi – Official Website (reference copy). https://rrbranchi.gov.in/  
[^26]: RRB Chennai – Official Website (reference copy). https://www.rrbchennai.gov.in/  
[^27]: RRB Secunderabad – Official Website (reference copy). https://rrbsecunderabad.gov.in/  
[^28]: RRB Secunderabad – CEN-01-2019 NTPC CBT1 Result Level-5 PDF. https://rrbsecunderabad.gov.in/CEN-01-2019-NTPC-CBT1-Result-Level-5.pdf  
[^29]: RRB Chennai – CEN-03-2015 Shortlisted 18 Candidates 2nd Stage Examination PDF. https://rrbchennai.gov.in/CEN-03-2015-shortlisted-18candidates-2nd-stage-examination.pdf  
[^30]: RRB Ranchi – Packages (Notices & Results page). https://rrbranchi.gov.in/?p=packages  
[^31]: OIRMS – RRB Document Verification Portal. https://oirms-ir.gov.in/rrbdv/  
[^32]: RRB Secunderabad – CEN-03/2025 (English) PDF. https://rrbsecunderabad.gov.in/wp-content/uploads/2025/08/Final-CEN-03_2025-English.pdf  
[^33]: Times of India – RRB NTPC UG Admit Card 2025: Steps to Download. https://timesofindia.indiatimes.com/education/news/rrb-ntpc-ug-admit-card-2025-to-be-released-today-at-rrb-digialm-com-heres-how-to-download/articleshow/123085977.cms