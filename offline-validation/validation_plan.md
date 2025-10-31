# Offline Validation Plan - RRB-NTPC Content

## Task Overview
Perform comprehensive offline usability validation by spot-checking 10% of assets across all content categories to ensure file accessibility, PDF readability, HTML rendering, image display, and local resource accessibility.

## Content Categories
1. **Previous Papers** (`/workspace/content/rrb-ntpc/previous-papers/`)
2. **Study Materials - DIKSHA** (`/workspace/diksha-ga/`)
3. **Study Materials - Wikimedia** (`/workspace/content/rrb-ntpc/study-materials/wikimedia/`)
4. **Practice Sets** (`/workspace/practice-ga/`)
5. **Current Affairs** (`/workspace/current-affairs/`)
6. **Metadata Files** (`/workspace/metadata/`)

## Validation Methodology

### 1. File Accessibility Testing
- Verify files are readable without network connection
- Test file permissions and access rights
- Check file integrity (corruption, encoding issues)

### 2. PDF Readability Testing
- Validate PDF opens correctly
- Check text extraction capability
- Verify embedded images and charts render properly
- Test cross-references and hyperlinks within PDFs

### 3. HTML File Rendering Testing
- Open HTML files in browser without network
- Verify CSS styling renders correctly
- Check JavaScript functionality
- Validate linked resources (images, scripts, stylesheets)

### 4. Image Display Testing
- Verify images open in standard image viewers
- Check image resolution and quality
- Test different image formats (JPG, PNG, GIF, SVG)

### 5. Linked Resources Testing
- Verify all internal links work offline
- Check relative path references
- Validate external dependencies are localized

## Sampling Strategy (10% per category)

### Previous Papers
- CBT1 papers: Test 10% of 2019-2025 files
- CBT2 papers: Test 10% of 2019-2025 files
- Model papers: Test 10% of language-specific files

### Study Materials
- DIKSHA GA: Test 10% from each subject category
- Wikimedia materials: Test 10% from general awareness and science

### Practice Sets
- Current Affairs: Test 10% of PDF and MD files
- Economy: Test 10% of practice materials
- Geography: Test 10% of materials
- Other categories: Test 10% each

### Current Affairs
- Annual Reports: Test 10% from each year
- Economic Surveys: Test 10% from each year
- Policy Documents: Test 10% from each year
- Yearbooks: Test 10% from each year

### Metadata Files
- Test all JSON, CSV, and MD files
- Validate structure and format

## Execution Steps

### Phase 1: Inventory Generation
- [x] Generate complete file inventory by category
- [x] Calculate 10% sample size for each category
- [x] Select representative samples using systematic sampling

### Phase 2: File Accessibility Testing
- [x] Test PDF files for readability
- [x] Test HTML files for rendering
- [x] Test image files for display
- [x] Test metadata files for parsing

### Phase 3: Link Validation
- [x] Check internal cross-references
- [x] Verify external links are properly handled
- [x] Test linked resource accessibility

### Phase 4: Issue Documentation
- [x] Document all issues found
- [x] Categorize issues by severity
- [x] Provide remediation recommendations

### Phase 5: Report Generation
- [x] Compile comprehensive validation report
- [x] Include sample selection methodology
- [x] Present findings with evidence
- [x] Provide actionable recommendations

## Tools and Methods
- Python scripts for automated testing
- Manual inspection for quality validation
- Browser testing for HTML rendering
- File system operations for accessibility testing

## Success Criteria
- 95%+ of tested files are accessible offline
- 90%+ of PDFs render correctly
- 95%+ of HTML files render properly
- 90%+ of images display correctly
- 95%+ of internal links function offline

## Timeline
- Phase 1: 30 minutes
- Phase 2: 2 hours
- Phase 3: 1 hour
- Phase 4: 30 minutes
- Phase 5: 30 minutes
- **Total: ~4.5 hours**

## Reporting
- Final report: `/logs/offline_validation_report.md`
- Supporting data: `/logs/offline-validation/`
- Sample selections: `/logs/offline-validation/sample_inventory.json`