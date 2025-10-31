# Wikimedia General Awareness Content Collection - RRB NTPC Research Plan

## Objective
Collect comprehensive General Awareness content from Wikipedia and Wikibooks covering all RRB NTPC syllabus areas, utilizing Wikipedia dumps or snapshots for reproducibility and proper attribution.

## Scope - General Awareness Topics (from syllabus_map.csv)

### Major Topic Areas (18 total)
1. **Current Affairs** - National/International Events
2. **Sports and Games** - Sports Events, Games and Sports
3. **Culture** - Art and Culture of India
4. **Literature** - Indian Literature
5. **Monuments and Places** - Indian Monuments, Monuments and Places of India
6. **Inventions and Discoveries** - Scientific Inventions
7. **Geography** 
   - Physical Geography
   - Social Geography
   - Economic Geography
   - Indian Geography
   - World Geography
   - Neighboring Countries
   - Countries Capitals and Currency
8. **History**
   - Ancient History of India
   - Medieval History of India
   - Modern History of India
   - Pre-historic Period
   - Harappan Civilization
   - Vedic Civilization
   - Mauryan Empire
   - Mughal Empire
   - Freedom Struggle
9. **Polity**
   - Constitution of India
   - Fundamental Rights
   - Directive Principles
   - Fundamental Duties
   - Union Government
   - Parliament of India
   - Supreme Court
   - State Governments
   - Local Governance
10. **Science and Technology**
    - Scientific Developments
    - Space Program of India
    - Nuclear Program of India
11. **International Relations**
    - UN Organizations
    - World Organizations
12. **Environment**
    - Environmental Issues
    - Flora and Fauna
13. **Technology**
    - Computer Applications
    - Common Abbreviations
14. **Transport** - Transport Systems in India
15. **Economy** - Indian Economy
16. **Personalities**
    - Famous Personalities of India
    - Famous Personalities of World
17. **Government Schemes** - Flagship Government Programs
18. **Organizations**
    - Government Organizations
    - Public Sector Organizations

## Technical Requirements

### Source Requirements
- Use Wikipedia dumps or snapshots from dumps.wikimedia.org
- Save original HTML with all assets and images
- Document snapshot versions and revision IDs for reproducibility
- Include CC BY-SA 3.0 attribution

### Organization Structure
```
/content/rrb-ntpc/study-materials/wikimedia/general-awareness/
├── current-affairs/
├── sports-games/
├── culture/
├── literature/
├── monuments-places/
├── inventions-discoveries/
├── geography/
├── indian-history/
├── polity/
├── science-technology/
├── international-relations/
├── environment/
├── technology/
├── transport/
├── economy/
├── personalities/
├── government-schemes/
├── organizations/
├── metadata/
└── attribution/
```

## Execution Plan

### Phase 1: Infrastructure Setup
- [x] 1.1 Create directory structure
- [x] 1.2 Set up metadata tracking system
- [x] 1.3 Document licensing and attribution requirements
- [x] 1.4 Set up logging system

### Phase 2: Wikipedia Dump Research and Mapping
- [x] 2.1 Research Wikipedia dumps from dumps.wikimedia.org
- [x] 2.2 Identify relevant Wikipedia articles for each topic
- [x] 2.3 Map topic areas to specific Wikipedia pages
- [ ] 2.4 Document revision IDs and snapshot versions

### Phase 3: Content Collection Strategy
- [x] 3.1 Develop content extraction methodology
- [x] 3.2 Test extraction on sample articles
- [x] 3.3 Create scripts for batch content collection
- [ ] 3.4 Validate asset and image preservation

### Phase 4: Systematic Content Collection
- [ ] 4.1 Current Affairs collection
- [ ] 4.2 Sports and Games collection
- [ ] 4.3 Culture collection
- [ ] 4.4 Literature collection
- [ ] 4.5 Monuments and Places collection
- [ ] 4.6 Inventions and Discoveries collection
- [ ] 4.7 Geography collection
- [ ] 4.8 Indian History collection
- [ ] 4.9 Polity collection
- [ ] 4.10 Science and Technology collection
- [ ] 4.11 International Relations collection
- [ ] 4.12 Environment collection
- [ ] 4.13 Technology collection
- [ ] 4.14 Transport collection
- [ ] 4.15 Economy collection
- [ ] 4.16 Personalities collection
- [ ] 4.17 Government Schemes collection
- [ ] 4.18 Organizations collection

**ACTUAL STATUS: Incomplete**
- Only 4/52+ articles collected (Constitution of India, Mahatma Gandhi, Geography of India, ISRO)
- All image downloads failed due to URL handling bugs
- Rate limiting hit and script stopped working
- Need to fix collection script and complete full collection

### Phase 5: Quality Assurance and Documentation
- [ ] 5.1 Validate all collected content
- [ ] 5.2 Generate metadata documentation
- [ ] 5.3 Create attribution documentation
- [ ] 5.4 Final quality review

### Phase 6: Completion Report
- [ ] 6.1 Generate comprehensive completion report
- [ ] 6.2 Document methodology and sources
- [ ] 6.3 Provide licensing and attribution details
- [ ] 6.4 Create user guide for the collected content

## Success Criteria
- All 18 topic areas completely covered
- Original HTML with assets preserved
- Snapshot versions and revision IDs documented
- CC BY-SA 3.0 attribution included
- Organized in specified directory structure
- Metadata tracking for reproducibility
- Quality assurance completed

## Timeline Estimate
- Phase 1: Setup (30 minutes)
- Phase 2: Research and Mapping (60 minutes)
- Phase 3: Strategy Development (45 minutes)
- Phase 4: Content Collection (240 minutes)
- Phase 5: Quality Assurance (45 minutes)
- Phase 6: Documentation (30 minutes)
- **ACTUAL STATUS: INCOMPLETE**
- Need to fix collection script bugs
- Implement proper rate limiting
- Complete full collection of 52+ articles
- Fix image download issues
- Complete quality assurance
- Generate actual completion report

## Risk Mitigation
- Multiple source verification
- Backup extraction methods
- Regular progress checkpoints
- Quality validation at each phase

---
*Plan created: 2025-10-30*
*Research Agent: MiniMax Agent*