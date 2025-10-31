# ZIM Package Metadata and File Organization Guide

## Table of Contents
1. [Metadata Fundamentals](#metadata-fundamentals)
2. [Metadata Field Reference](#metadata-field-reference)
3. [File Organization Standards](#file-organization-standards)
4. [Metadata Extraction from Source Content](#metadata-extraction-from-source-content)
5. [Advanced Metadata Handling](#advanced-metadata-handling)
6. [Tools and Scripts](#tools-and-scripts)
7. [Best Practices](#best-practices)

## Metadata Fundamentals

### What is ZIM Metadata?
ZIM metadata provides essential information about the package content, source, and licensing. It enables:
- **Discovery**: Finding packages through catalogs and search
- **Attribution**: Proper credit to content creators and sources
- **Licensing**: Clear understanding of usage rights
- **Versioning**: Tracking updates and changes
- **Quality Assessment**: Evaluating content reliability

### Metadata Categories
1. **Descriptive Metadata**: Title, description, language, creator
2. **Administrative Metadata**: Publisher, creation date, version
3. **Technical Metadata**: File formats, compression, size
4. **Rights Metadata**: Licensing, attribution, usage terms
5. **Content Metadata**: Subject areas, keywords, educational level

## Metadata Field Reference

### Essential Fields

#### Title and Identification
```bash
--title="Package Title"
--name="unique-package-identifier"
```

**Guidelines**:
- Use clear, descriptive titles
- Include version information if applicable
- Avoid special characters that might cause issues
- Keep titles under 100 characters for readability

**Examples**:
```
--title="RRB NTPC General Awareness 2025"
--name="rrb-ntpc-ga-2025"
```

```
--title="Indian History - Ancient Period"
--name="indian-history-ancient"
```

#### Content Description
```bash
--description="Detailed description of the content"
```

**Guidelines**:
- Provide 1-2 sentence description
- Include target audience (e.g., "for competitive exams")
- Mention key topics covered
- Keep under 200 characters for optimal display

**Examples**:
```
--description="Comprehensive study materials covering Indian culture, geography, economy, and polity for RRB NTPC exam preparation"
```

```
--description="Complete coverage of ancient Indian history including dynasties, rulers, and cultural developments"
```

#### Language and Localization
```bash
--language=eng  # ISO639-3 language code
```

**Common ISO639-3 Codes**:
- `eng` - English
- `hin` - Hindi
- `tam` - Tamil
- `tel` - Telugu
- `mar` - Marathi
- `guj` - Gujarati
- `ben` - Bengali
- `kan` - Kannada
- `mal` - Malayalam

**Guidelines**:
- Use ISO639-3 codes for accuracy
- Specify language in metadata even if obvious
- For multilingual content, use primary language code

#### Creator and Attribution
```bash
--creator="Content Creator Name(s)"
--publisher="Package Publisher"
```

**Guidelines**:
- Use full names when possible
- Include organization names for institutional content
- Credit multiple contributors with semicolons
- Be consistent with attribution across packages

**Examples**:
```
--creator="Wikipedia Contributors; RRB NTPC Team"
--publisher="OpenZIM Project"
```

```
--creator="Dr. Rajesh Kumar; Education Ministry"
--publisher="Digital India Initiative"
```

### Optional but Recommended Fields

#### Tags and Keywords
```bash
--tags="education;railway;competitive-exam;general-awareness"
```

**Tag Guidelines**:
- Use semicolons to separate multiple tags
- Keep tags consistent across related packages
- Include educational level tags (e.g., "undergraduate")
- Use subject-specific tags (e.g., "history", "geography")

**Common Tag Categories**:
- **Subject**: history, geography, science, mathematics
- **Educational Level**: primary, secondary, undergraduate, competitive-exam
- **Format**: textbook, study-guide, practice-tests
- **Language**: english, hindi, bilingual
- **Source**: wikipedia, official, educational-institution

#### Version and Date Information
```bash
# Version information is automatically included
# Build date is captured automatically
```

**Versioning Strategy**:
- Use semantic versioning (e.g., 1.0.0, 1.1.0)
- Increment minor versions for content additions
- Increment major versions for significant changes
- Include release notes in package documentation

### Content-Specific Metadata

#### Educational Metadata
```bash
# Add to description or tags
"educational-level: competitive-exam"
"curriculum: RRB NTPC"
"target-audience: railway-aspirants"
```

#### Source and Provenance
```bash
# Include in extended metadata
"source-url": "https://en.wikipedia.org/wiki/Geography_of_India"
"original-source": "Wikipedia"
"collection-date": "2025-10-30"
"license": "CC BY-SA 3.0"
```

## File Organization Standards

### Directory Structure Guidelines

#### Standard Educational Package Structure
```
educational_package/
├── index.html                    # Main landing page (REQUIRED)
├── favicon.png                   # 48x48 PNG icon (REQUIRED)
├── metadata/
│   ├── package-info.json        # Extended metadata
│   ├── source-attribution.json  # Source information
│   └── licensing-info.json      # License details
├── content/
│   ├── subjects/
│   │   ├── history/
│   │   ├── geography/
│   │   ├── science/
│   │   └── mathematics/
│   ├── practice/
│   │   ├── mock-tests/
│   │   └── previous-papers/
│   └── reference/
│       ├── glossaries/
│       └── indexes/
├── assets/
│   ├── css/
│   │   ├── main.css
│   │   ├── navigation.css
│   │   └── print.css
│   ├── js/
│   │   ├── main.js
│   │   ├── search.js
│   │   └── navigation.js
│   └── images/
│       ├── logos/
│       ├── diagrams/
│       └── illustrations/
├── media/
│   ├── audio/
│   ├── video/
│   └── documents/
└── extras/
    ├── redirects.tsv
    ├── search-index.json
    └── changelog.md
```

#### RRB NTPC Specific Structure
```
rrb-ntpc-package/
├── index.html
├── favicon.png
├── metadata/
│   ├── rrb-ntpc-specific.json
│   └── exam-pattern.json
├── general-awareness/
│   ├── culture/
│   ├── economy/
│   ├── geography/
│   ├── history/
│   ├── polity/
│   └── science-technology/
├── practice-materials/
│   ├── mock-tests/
│   ├── previous-papers/
│   └── study-notes/
├── current-affairs/
│   ├── 2024/
│   └── 2025/
└── reference-materials/
    ├── important-dates/
    ├── organizations/
    └── abbreviations/
```

### File Naming Conventions

#### HTML Files
- Use lowercase with hyphens: `indian-history.html`
- Include topic keywords: `geography-physical-features.html`
- Avoid spaces and special characters: ❌ `Indian History.html` → ✅ `indian-history.html`

#### Asset Files
- CSS: `subject-specific-styles.css`
- JavaScript: `search-functionality.js`
- Images: `topic-name-diagram.png`
- Media: `pronunciation-audio.mp3`

#### Directory Names
- Use descriptive names: `ancient-history` not `history1`
- Group related content: `mathematics/algebra/` not `algebra/`
- Include language codes when relevant: `hindi-literature/`

### Content Linking Standards

#### Internal Links
```html
<!-- ✅ GOOD: Relative links -->
<a href="../index.html">Home</a>
<a href="geography/physical-features.html">Physical Geography</a>
<a href="../practice/mock-test-1.html">Practice Test</a>

<!-- ❌ BAD: Absolute or external links -->
<a href="https://example.com">External Link</a>
<a href="/home/user/content/index.html">Absolute Path</a>
```

#### Navigation Structure
```html
<!-- Main navigation -->
<nav class="main-nav">
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="subjects/index.html">Subjects</a></li>
        <li><a href="practice/index.html">Practice</a></li>
        <li><a href="current-affairs/index.html">Current Affairs</a></li>
        <li><a href="reference/index.html">Reference</a></li>
    </ul>
</nav>

<!-- Breadcrumb navigation -->
<nav class="breadcrumb">
    <a href="../index.html">Home</a> > 
    <a href="geography/index.html">Geography</a> > 
    Physical Features
</nav>
```

## Metadata Extraction from Source Content

### Automated Metadata Extraction Script

```bash
#!/bin/bash
# extract_metadata.sh - Extract metadata from source content

CONTENT_DIR="$1"
OUTPUT_DIR="$2"

if [ -z "$CONTENT_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
    echo "Usage: $0 <content_directory> <output_metadata_directory>"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "Extracting metadata from: $CONTENT_DIR"

# Extract basic information
extract_basic_info() {
    echo "Extracting basic information..."
    
    # Get content statistics
    local total_html=$(find "$CONTENT_DIR" -name "*.html" | wc -l)
    local total_images=$(find "$CONTENT_DIR" -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.webp" | wc -l)
    local total_size=$(du -sh "$CONTENT_DIR" | cut -f1)
    
    # Analyze HTML content
    local titles=$(find "$CONTENT_DIR" -name "*.html" -exec grep -o '<title[^>]*>[^<]*</title>' {} \; | sed 's/<[^>]*>//g' | head -10)
    local subjects=$(echo "$titles" | tr ' ' '\n' | sort | uniq -c | sort -nr | head -5)
    
    # Create basic metadata file
    cat > "$OUTPUT_DIR/basic-metadata.json" << EOF
{
    "extraction_date": "$(date -Iseconds)",
    "source_directory": "$CONTENT_DIR",
    "statistics": {
        "total_html_files": $total_html,
        "total_images": $total_images,
        "total_size": "$total_size"
    },
    "sample_titles": [
$(echo "$titles" | sed 's/^/        "/g' | sed 's/$/"/g' | sed '$!s/$/,/' | sed '$s/$//')
    ],
    "subject_analysis": $(echo "$subjects" | awk '{print "[\"" $2 "\" : " $1 "], "}' | sed '$ s/, $//' | sed '1s/^/[\n/' | sed '$s/$/\n    ]/')
}
EOF
}

# Extract source information
extract_source_info() {
    echo "Extracting source information..."
    
    # Look for source attribution files
    local source_files=$(find "$CONTENT_DIR" -name "*source*" -o -name "*attribution*" -o -name "*credits*" 2>/dev/null)
    
    if [ ! -z "$source_files" ]; then
        echo "Found source files:"
        echo "$source_files"
        
        # Extract information from source files
        cat > "$OUTPUT_DIR/source-metadata.json" << EOF
{
    "extraction_date": "$(date -Iseconds)",
    "source_files_found": [
$(echo "$source_files" | sed 's/^/        "/g' | sed 's/$/"/g' | sed '$!s/$/,/' | sed '$s/$//')
    ],
    "extraction_method": "file_analysis"
}
EOF
    else
        echo "No source attribution files found"
        cat > "$OUTPUT_DIR/source-metadata.json" << EOF
{
    "extraction_date": "$(date -Iseconds)",
    "source_files_found": [],
    "extraction_method": "heuristic",
    "notes": "Source attribution not found in files - requires manual verification"
}
EOF
    fi
}

# Extract license information
extract_license_info() {
    echo "Extracting license information..."
    
    # Look for license references
    local license_refs=$(grep -r -i "license\|copyright\|cc\|gpl\|mit\|bsd" "$CONTENT_DIR" --include="*.html" --include="*.txt" --include="*.md" 2>/dev/null | head -10)
    
    cat > "$OUTPUT_DIR/license-metadata.json" << EOF
{
    "extraction_date": "$(date -Iseconds)",
    "license_references_found": [
$(echo "$license_refs" | sed 's/^/        "/g' | sed 's/$/"/g' | sed '$!s/$/,/' | sed '$s/$//')
    ],
    "extraction_method": "text_search",
    "notes": "License information extracted from content text - may require manual verification"
}
EOF
}

# Generate comprehensive metadata
generate_comprehensive_metadata() {
    echo "Generating comprehensive metadata..."
    
    # Determine package type and title
    local package_type="general"
    local package_title="Educational Package"
    
    # Analyze directory structure for package type
    if echo "$CONTENT_DIR" | grep -q "rrb"; then
        package_type="rrb-ntpc"
        package_title="RRB NTPC Study Materials"
    elif echo "$CONTENT_DIR" | grep -q "science"; then
        package_type="science"
        package_title="Science Study Materials"
    elif echo "$CONTENT_DIR" | grep -q "history"; then
        package_type="history"
        package_title="History Study Materials"
    fi
    
    # Generate comprehensive metadata
    cat > "$OUTPUT_DIR/comprehensive-metadata.json" << EOF
{
    "package_metadata": {
        "title": "$package_title",
        "type": "$package_type",
        "language": "eng",
        "extraction_date": "$(date -Iseconds)",
        "source_directory": "$CONTENT_DIR",
        "metadata_version": "1.0"
    },
    "content_analysis": {
        "total_files": $(find "$CONTENT_DIR" -type f | wc -l),
        "html_files": $(find "$CONTENT_DIR" -name "*.html" | wc -l),
        "media_files": $(find "$CONTENT_DIR" \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.webp" \) | wc -l),
        "total_size": "$(du -sh "$CONTENT_DIR" | cut -f1)"
    },
    "subject_coverage": $(analyze_subjects "$CONTENT_DIR"),
    "quality_indicators": {
        "has_index_page": $([ -f "$CONTENT_DIR/index.html" ] && echo "true" || echo "false"),
        "has_favicon": $([ -f "$CONTENT_DIR/favicon.png" ] && echo "true" || echo "false"),
        "relative_links": $(check_relative_links "$CONTENT_DIR" && echo "true" || echo "false"),
        "external_links": $(check_external_links "$CONTENT_DIR" && echo "false" || echo "true")
    }
}
EOF
}

# Helper functions
analyze_subjects() {
    local dir="$1"
    local subjects=$(find "$dir" -type d -name "*" | grep -E "(history|geography|science|math|economics|polity)" | sed 's/.*\///g' | sort | uniq | sed 's/^/"/g' | sed 's/$/"/g' | tr '\n' ',' | sed 's/,$//')
    echo "[$subjects]"
}

check_relative_links() {
    local dir="$1"
    ! grep -r "http" "$dir" --include="*.html" | grep -v "data:" | grep -q . 2>/dev/null
}

check_external_links() {
    local dir="$1"
    grep -r "http" "$dir" --include="*.html" | grep -v "data:" | grep -q . 2>/dev/null
}

# Execute extraction functions
extract_basic_info
extract_source_info
extract_license_info
generate_comprehensive_metadata

echo "Metadata extraction complete!"
echo "Output directory: $OUTPUT_DIR"
echo ""
echo "Generated files:"
ls -la "$OUTPUT_DIR"
```

### Metadata Template Generator

```bash
#!/bin/bash
# generate_metadata_template.sh - Generate ZIM metadata from template

TEMPLATE_FILE="$1"
OUTPUT_FILE="$2"

if [ -z "$TEMPLATE_FILE" ]; then
    echo "Usage: $0 <template_file> [output_file]"
    echo "Template file should contain metadata in key=value format"
    exit 1
fi

OUTPUT_FILE="${OUTPUT_FILE:-metadata-$(date '+%Y%m%d_%H%M%S').json}"

echo "Generating metadata from template: $TEMPLATE_FILE"

# Parse template file and generate JSON metadata
python3 << 'PYTHON_SCRIPT'
import json
import sys
from datetime import datetime

def parse_template(template_file, output_file):
    metadata = {}
    
    # Default values
    metadata['generation_date'] = datetime.now().isoformat()
    metadata['generator'] = 'ZIM Metadata Generator v1.0'
    
    # Parse template file
    try:
        with open(template_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Convert values based on key
                        if key in ['total_files', 'html_files', 'media_files']:
                            try:
                                metadata[key] = int(value)
                            except ValueError:
                                metadata[key] = value
                        elif key in ['has_index_page', 'has_favicon', 'relative_links']:
                            metadata[key] = value.lower() in ['true', '1', 'yes', 'on']
                        else:
                            metadata[key] = value
                    elif ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Store as nested structure
                        if '.' in key:
                            parts = key.split('.')
                            current = metadata
                            for part in parts[:-1]:
                                if part not in current:
                                    current[part] = {}
                                current = current[part]
                            current[parts[-1]] = value
                        else:
                            metadata[key] = value
    except FileNotFoundError:
        print(f"Template file not found: {template_file}")
        return False
    except Exception as e:
        print(f"Error parsing template: {e}")
        return False
    
    # Ensure required fields
    if 'title' not in metadata:
        metadata['title'] = 'Educational Package'
    if 'language' not in metadata:
        metadata['language'] = 'eng'
    if 'creator' not in metadata:
        metadata['creator'] = 'Content Source'
    if 'publisher' not in metadata:
        metadata['publisher'] = 'OpenZIM Project'
    
    # Write output file
    try:
        with open(output_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        print(f"Metadata file generated: {output_file}")
        return True
    except Exception as e:
        print(f"Error writing output file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <template_file> [output_file]")
        sys.exit(1)
    
    template_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'metadata.json'
    
    if parse_template(template_file, output_file):
        print("Metadata generation successful!")
    else:
        print("Metadata generation failed!")
        sys.exit(1)
PYTHON_SCRIPT

# Example template file
cat > template_example.txt << 'EOF'
# RRB NTPC Package Metadata Template
# Lines starting with # are comments
# Use key=value format for simple fields
# Use key: value format for nested fields

# Basic Information
title=RRB NTPC General Awareness Complete
description=Comprehensive general awareness materials for RRB NTPC exam preparation
language=eng
creator=Wikipedia Contributors; RRB NTPC Team
publisher=OpenZIM Project
tags=education;railway;ntpc;general-awareness;competitive-exam

# Content Information
total_files=156
html_files=78
media_files=45
total_size=45M

# Package Details
package.type=rrb-ntpc
package.level=competitive-exam
package.subjects=history;geography;economy;polity;science;culture

# Quality Indicators
has_index_page=true
has_favicon=true
relative_links=true
external_links=false

# Source Information
source.type=wikipedia
source.license=CC BY-SA 3.0
source.attribution=Wikipedia Contributors
source.collection_date=2025-10-30

# Technical Details
content.format=html5
compression.level=standard
indexing.enabled=true
redirects.supported=true
EOF

echo ""
echo "Example template file created: template_example.txt"
echo "To generate metadata: $0 template_example.txt"
```

## Advanced Metadata Handling

### Multi-language Metadata

```bash
#!/bin/bash
# generate_multilingual_metadata.sh - Handle multiple languages

CONTENT_DIR="$1"
LANGUAGES="$2"  # comma-separated list: eng,hin,tam

if [ -z "$CONTENT_DIR" ] || [ -z "$LANGUAGES" ]; then
    echo "Usage: $0 <content_dir> <languages>"
    echo "Example: $0 /path/to/content 'eng,hin,tam'"
    exit 1
fi

IFS=',' read -ra LANG_ARRAY <<< "$LANGUAGES"

echo "Generating multilingual metadata for languages: ${LANG_ARRAY[*]}"

# Create base metadata
BASE_METADATA='{
  "multilingual": true,
  "languages": {'

for i in "${!LANG_ARRAY[@]}"; do
    lang="${LANG_ARRAY[$i]}"
    
    # Language-specific titles and descriptions
    case "$lang" in
        "eng")
            TITLE="General Awareness Study Materials"
            DESCRIPTION="Comprehensive study materials for competitive exams"
            ;;
        "hin")
            TITLE="सामान्य जागरूकता अध्ययन सामग्री"
            DESCRIPTION="प्रतिस्पर्धी परीक्षाओं के लिए व्यापक अध्ययन सामग्री"
            ;;
        "tam")
            TITLE="பொது விழிப்புணர்வு கற்கும் பொருட்கள்"
            DESCRIPTION="போட்டி தேர்வுகளுக்கான விரிவான கற்கும் பொருட்கள்"
            ;;
        *)
            TITLE="Study Materials"
            DESCRIPTION="Comprehensive study materials"
            ;;
    esac
    
    BASE_METADATA+="
    \"$lang\": {
      \"title\": \"$TITLE\",
      \"description\": \"$DESCRIPTION\",
      \"language_code\": \"$lang\",
      \"direction\": \"ltr\"
    }"
    
    if [ $i -lt $((${#LANG_ARRAY[@]} - 1)) ]; then
        BASE_METADATA+=","
    fi
done

BASE_METADATA+="
  },
  \"primary_language\": \"${LANG_ARRAY[0]}\",
  \"fallback_language\": \"${LANG_ARRAY[0]}\"
}"

# Write multilingual metadata
echo "$BASE_METADATA" > "$CONTENT_DIR/metadata/multilingual.json"

echo "Multilingual metadata created: $CONTENT_DIR/metadata/multilingual.json"
```

### Quality Assessment Metadata

```bash
#!/bin/bash
# assess_content_quality.sh - Generate quality assessment metadata

CONTENT_DIR="$1"
OUTPUT_FILE="${2:-quality-assessment.json}"

echo "Assessing content quality for: $CONTENT_DIR"

# Create quality assessment
python3 << 'PYTHON_SCRIPT'
import json
import os
import re
from pathlib import Path

def assess_content_quality(content_dir):
    assessment = {
        "assessment_date": "2025-10-31",
        "content_directory": content_dir,
        "quality_scores": {},
        "issues": [],
        "recommendations": []
    }
    
    # File structure assessment
    structure_score = 0
    if os.path.exists(f"{content_dir}/index.html"):
        structure_score += 30
    if os.path.exists(f"{content_dir}/favicon.png"):
        structure_score += 20
    if os.path.exists(f"{content_dir}/metadata/"):
        structure_score += 10
    if any(f.endswith('.css') for f in os.listdir(f"{content_dir}/assets/") if os.path.isdir(f"{content_dir}/assets/")):
        structure_score += 10
    
    assessment["quality_scores"]["file_structure"] = structure_score
    
    # HTML quality assessment
    html_files = list(Path(content_dir).rglob("*.html"))
    html_quality = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for valid DOCTYPE
                if '<!DOCTYPE html>' in content:
                    html_quality += 10
                
                # Check for proper charset
                if 'charset=' in content:
                    html_quality += 10
                
                # Check for title tag
                if '<title>' in content:
                    html_quality += 10
                
                # Check for meta viewport
                if 'viewport' in content:
                    html_quality += 10
                
                # Check for alt attributes in images
                img_count = len(re.findall(r'<img[^>]*>', content))
                alt_count = len(re.findall(r'<img[^>]*alt=', content))
                if img_count > 0:
                    alt_ratio = alt_count / img_count
                    html_quality += int(alt_ratio * 10)
                
                # Check for relative links
                if 'href="http' not in content:  # No external http links
                    html_quality += 10
                
        except Exception as e:
            assessment["issues"].append(f"Error reading {html_file}: {e}")
    
    if html_files:
        html_quality = html_quality / len(html_files)
    
    assessment["quality_scores"]["html_quality"] = html_quality
    
    # Link validation
    link_score = 0
    broken_links = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find all links
                links = re.findall(r'href=["\']([^"\']*)["\']', content)
                for link in links:
                    if link.startswith('#') or link.startswith('mailto:') or link.startswith('data:'):
                        continue
                    
                    # Check if relative link exists
                    if not link.startswith('http'):
                        target_path = os.path.join(os.path.dirname(html_file), link)
                        if not os.path.exists(target_path):
                            broken_links.append(f"{html_file}: {link}")
        except Exception as e:
            assessment["issues"].append(f"Error checking links in {html_file}: {e}")
    
    if broken_links:
        assessment["issues"].extend(broken_links)
        link_score = max(0, 100 - len(broken_links) * 10)
    else:
        link_score = 100
    
    assessment["quality_scores"]["link_integrity"] = link_score
    
    # Overall score
    overall_score = (structure_score + html_quality + link_score) / 3
    assessment["quality_scores"]["overall"] = overall_score
    
    # Generate recommendations
    if structure_score < 70:
        assessment["recommendations"].append("Improve file structure: ensure index.html, favicon.png, and metadata files are present")
    
    if html_quality < 70:
        assessment["recommendations"].append("Improve HTML quality: add DOCTYPE, charset, title tags, and meta viewport")
    
    if link_score < 90:
        assessment["recommendations"].append("Fix broken internal links and ensure all referenced files exist")
    
    if overall_score < 80:
        assessment["recommendations"].append("Overall quality needs improvement before ZIM package creation")
    
    return assessment

# Execute assessment
content_dir = "$1"
output_file = "$2" if "$2" else "quality-assessment.json"

try:
    assessment = assess_content_quality(content_dir)
    
    with open(output_file, 'w') as f:
        json.dump(assessment, f, indent=2)
    
    print(f"Quality assessment completed: {output_file}")
    print(f"Overall quality score: {assessment['quality_scores']['overall']:.1f}/100")
    
    if assessment['issues']:
        print(f"Found {len(assessment['issues'])} issues")
    if assessment['recommendations']:
        print(f"Generated {len(assessment['recommendations'])} recommendations")
        
except Exception as e:
    print(f"Error during quality assessment: {e}")
    exit(1)
PYTHON_SCRIPT

echo "Quality assessment completed: $OUTPUT_FILE"
```

## Tools and Scripts

### Complete Metadata Management Script

```bash
#!/bin/bash
# manage_zim_metadata.sh - Complete metadata management system

COMMAND="$1"
CONTENT_DIR="$2"
OPTIONS="${3:-}"

case "$COMMAND" in
    "extract")
        echo "Extracting metadata from: $CONTENT_DIR"
        ./extract_metadata.sh "$CONTENT_DIR" "metadata/extracted"
        ;;
    "generate")
        echo "Generating ZIM metadata template..."
        ./generate_metadata_template.sh "$OPTIONS" "metadata/package-metadata.json"
        ;;
    "assess")
        echo "Assessing content quality..."
        ./assess_content_quality.sh "$CONTENT_DIR" "metadata/quality-assessment.json"
        ;;
    "multilingual")
        LANGUAGES="$OPTIONS"
        echo "Generating multilingual metadata for: $LANGUAGES"
        ./generate_multilingual_metadata.sh "$CONTENT_DIR" "$LANGUAGES"
        ;;
    "validate")
        echo "Validating metadata completeness..."
        python3 << 'PYTHON_VALIDATION'
import json
import sys

def validate_metadata(metadata_file):
    required_fields = ['title', 'description', 'language', 'creator', 'publisher']
    missing_fields = []
    
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        for field in required_fields:
            if field not in metadata or not metadata[field]:
                missing_fields.append(field)
        
        if missing_fields:
            print(f"❌ Missing required fields: {missing_fields}")
            return False
        else:
            print("✅ All required metadata fields present")
            return True
            
    except Exception as e:
        print(f"❌ Error reading metadata file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_metadata.py <metadata_file>")
        sys.exit(1)
    
    metadata_file = sys.argv[1]
    if validate_metadata(metadata_file):
        print("Metadata validation passed")
    else:
        print("Metadata validation failed")
        sys.exit(1)
PYTHON_VALIDATION
        ;;
    *)
        echo "Usage: $0 <command> <content_directory> [options]"
        echo ""
        echo "Commands:"
        echo "  extract <dir>           - Extract metadata from content"
        echo "  generate <options>      - Generate metadata template"
        echo "  assess <dir>           - Assess content quality"
        echo "  multilingual <langs>   - Generate multilingual metadata"
        echo "  validate <file>        - Validate metadata completeness"
        echo ""
        echo "Examples:"
        echo "  $0 extract /path/to/content"
        echo "  $0 generate --title='Test Package' --language=eng"
        echo "  $0 assess /path/to/content"
        echo "  $0 multilingual 'eng,hin,tam'"
        echo "  $0 validate metadata/package-metadata.json"
        exit 1
        ;;
esac
```

## Best Practices

### Metadata Quality Standards

1. **Completeness**: Ensure all required fields are populated
2. **Accuracy**: Verify source attribution and licensing information
3. **Consistency**: Use consistent naming conventions and formats
4. **Accessibility**: Include language codes and descriptions in multiple languages where applicable
5. **Maintainability**: Keep metadata organized and versioned

### File Organization Best Practices

1. **Logical Structure**: Organize content in intuitive directory hierarchies
2. **Scalability**: Design structures that can accommodate future content additions
3. **Consistency**: Apply naming conventions uniformly across all files
4. **Efficiency**: Group related files to minimize navigation complexity
5. **Standardization**: Follow established educational content patterns

### Metadata Maintenance

1. **Version Control**: Track metadata changes with versioning
2. **Documentation**: Maintain clear documentation of metadata schemas
3. **Validation**: Regular validation against quality standards
4. **Updates**: Regular updates for licensing and source attribution
5. **Backup**: Regular backups of metadata files and templates

This comprehensive guide ensures high-quality metadata and file organization for ZIM packages, enabling better content discovery, attribution, and user experience.
