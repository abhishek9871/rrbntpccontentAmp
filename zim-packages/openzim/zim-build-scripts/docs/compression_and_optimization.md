# ZIM Package Compression and Optimization Guide

## Table of Contents
1. [Compression Fundamentals](#compression-fundamentals)
2. [ZIM-Specific Compression Options](#zim-specific-compression-options)
3. [Content Optimization Techniques](#content-optimization-techniques)
4. [Image Optimization](#image-optimization)
5. [HTML and CSS Optimization](#html-and-css-optimization)
6. [JavaScript Optimization](#javascript-optimization)
7. [Performance Tuning](#performance-tuning)
8. [Quality Assurance](#quality-assurance)

## Compression Fundamentals

### ZIM File Compression
ZIM packages use zlib compression with configurable cluster sizes. Understanding these fundamentals helps optimize both file size and access performance.

#### Cluster Size Optimization
```bash
# Small clusters (1024 bytes) - Fast access, larger file size
zimwriterfs --minChunkSize=1024 source_dir output.zim

# Medium clusters (2048 bytes) - Balanced performance
zimwriterfs --minChunkSize=2048 source_dir output.zim

# Large clusters (4096 bytes) - Better compression, slower access
zimwriterfs --minChunkSize=4096 source_dir output.zim

# Extra large clusters (8192 bytes) - Maximum compression
zimwriterfs --minChunkSize=8192 source_dir output.zim
```

**Guidelines**:
- **1024 bytes**: For small packages with frequent random access
- **2048 bytes**: Default - good balance for most educational content
- **4096 bytes**: For larger packages where storage is limited
- **8192 bytes**: For very large packages with sequential access patterns

#### Compression Testing Script
```bash
#!/bin/bash
# test_compression_effects.sh - Test different compression settings

CONTENT_DIR="$1"
OUTPUT_DIR="${2:-compression_test}"

mkdir -p "$OUTPUT_DIR"

echo "Testing compression effects for: $CONTENT_DIR"

# Test different cluster sizes
CLUSTER_SIZES=(1024 2048 4096 8192)

for size in "${CLUSTER_SIZES[@]}"; do
    output_file="$OUTPUT_DIR/package_${size}.zim"
    echo "Testing cluster size: $size bytes"
    
    # Create ZIM with specific cluster size
    zimwriterfs \
        --welcome=index.html \
        --favicon=favicon.png \
        --language=eng \
        --title="Compression Test $size" \
        --description="Testing cluster size $size" \
        --minChunkSize=$size \
        --verbose \
        "$CONTENT_DIR" "$output_file"
    
    # Record results
    if [ -f "$output_file" ]; then
        file_size=$(du -h "$output_file" | cut -f1)
        echo "  Cluster size: $size bytes → File size: $file_size"
        echo "$size,$file_size" >> "$OUTPUT_DIR/results.csv"
    fi
done

# Analyze results
echo ""
echo "Compression Analysis Results:"
echo "Cluster Size (bytes) | File Size"
echo "------------------------|--------"
cat "$OUTPUT_DIR/results.csv" | while IFS=',' read -r size size_str; do
    printf "%-18s | %s\n" "$size bytes" "$size_str"
done

echo ""
echo "Results saved to: $OUTPUT_DIR/"
```

## ZIM-Specific Compression Options

### HTML Inflation
```bash
# Enable HTML inflation for better compression
zimwriterfs --inflateHtml source_dir output.zim

# Without inflation
zimwriterfs source_dir output.zim
```

**Benefits of HTML Inflation**:
- Better compression ratios for text-heavy content
- No impact on functionality
- May increase memory usage during access

### Namespace Optimization
```bash
# Use unique namespace for JavaScript-heavy content
zimwriterfs --uniqueNamespace source_dir output.zim

# Standard namespace usage
zimwriterfs source_dir output.zim
```

**When to Use Unique Namespace**:
- Dynamic content with JavaScript
- Content with special characters in URLs
- Complex navigation systems

### Full-Text Indexing Impact
```bash
# With full-text indexing (larger file, better search)
zimwriterfs --withFullTextIndex source_dir output.zim

# Without indexing (smaller file, limited search)
zimwriterfs source_dir output.zim
```

**Indexing Trade-offs**:
- **Benefits**: Fast content search, better user experience
- **Trade-offs**: Larger file size (typically 10-20% increase)
- **Recommendation**: Always enable for educational content

## Content Optimization Techniques

### File Deduplication
```bash
#!/bin/bash
# deduplicate_content.sh - Remove duplicate files before packaging

CONTENT_DIR="$1"

echo "Deduplicating content in: $CONTENT_DIR"

# Find duplicate files based on content hash
duplicates=$(find "$CONTENT_DIR" -type f -exec md5sum {} \; | sort | uniq -w32 -d)

if [ ! -z "$duplicates" ]; then
    echo "Found duplicate files:"
    echo "$duplicates"
    
    # Create backup before removal
    backup_dir="$CONTENT_DIR.backup.$(date '+%Y%m%d_%H%M%S')"
    cp -r "$CONTENT_DIR" "$backup_dir"
    echo "Backup created: $backup_dir"
    
    # Remove duplicates
    echo "$duplicates" | while read -r hash file; do
        echo "Removing duplicate: $file"
        rm "$file"
    done
    
    echo "Deduplication complete. Check backup if needed."
else
    echo "No duplicates found."
fi
```

### Dead Link Removal
```bash
#!/bin/bash
# remove_dead_links.sh - Find and remove references to missing files

CONTENT_DIR="$1"

echo "Checking for dead links in: $CONTENT_DIR"

# Find all HTML files
find "$CONTENT_DIR" -name "*.html" -exec echo "Checking: {}" \; | while read html_file; do
    echo "Analyzing: $html_file"
    
    # Extract all href and src attributes
    grep -oE '(href|src)="[^"]*"' "$html_file" | \
        sed 's/(href|src)="//g' | sed 's/"//g' | \
        while read -r link; do
            # Skip external links and anchors
            if [[ "$link" =~ ^http ]] || [[ "$link" =~ ^# ]] || [[ "$link" =~ ^mailto: ]]; then
                continue
            fi
            
            # Resolve relative path
            link_dir=$(dirname "$html_file")
            full_path=$(cd "$link_dir" && realpath "$link" 2>/dev/null)
            
            if [ ! -z "$full_path" ] && [ ! -f "$full_path" ]; then
                echo "  Dead link found: $link in $html_file"
                # Remove or comment out the link
                sed -i "s|$link|<!-- DEAD_LINK: $link -->|g" "$html_file"
            fi
        done
done

echo "Dead link removal complete."
```

### Unused File Detection
```bash
#!/bin/bash
# find_unused_files.sh - Find files not referenced in HTML

CONTENT_DIR="$1"

echo "Finding unused files in: $CONTENT_DIR"

# Create list of all files (excluding directories)
all_files=$(find "$CONTENT_DIR" -type f | sed "s|$CONTENT_DIR/||")

# Find files referenced in HTML
referenced_files=$(find "$CONTENT_DIR" -name "*.html" -exec grep -hoE 'src="[^"]*"|href="[^"]*"' {} \; | \
    sed 's/src="//g' | sed 's/href="//g' | sed 's/"//g' | \
    grep -v '^#' | grep -v '^http' | grep -v '^mailto:' | sort | uniq)

# Find CSS and JS files
css_files=$(find "$CONTENT_DIR" -name "*.css" | sed "s|$CONTENT_DIR/||")
js_files=$(find "$CONTENT_DIR" -name "*.js" | sed "s|$CONTENT_DIR/||")

# Combine referenced files
referenced_combined=$(echo -e "$referenced_files\n$css_files\n$js_files" | sort | uniq)

# Find unused files
unused_files=$(comm -23 <(echo "$all_files" | sort) <(echo "$referenced_combined" | sort))

if [ ! -z "$unused_files" ]; then
    echo "Found potentially unused files:"
    echo "$unused_files"
    
    # Ask user if they want to remove unused files
    read -p "Remove unused files? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "$unused_files" | while read -r file; do
            full_path="$CONTENT_DIR/$file"
            if [ -f "$full_path" ]; then
                echo "Removing: $file"
                rm "$full_path"
            fi
        done
        echo "Unused files removed."
    fi
else
    echo "No unused files found."
fi
```

## Image Optimization

### Automatic Image Optimization Script
```bash
#!/bin/bash
# optimize_images.sh - Optimize all images in content directory

CONTENT_DIR="$1"
JPEG_QUALITY="${2:-85}"
PNG_OPTIMIZATION_LEVEL="${3:-2}"

echo "Optimizing images in: $CONTENT_DIR"

# Check for optimization tools
check_tools() {
    local missing_tools=()
    
    if ! command -v jpegoptim >/dev/null 2>&1; then
        missing_tools+=("jpegoptim")
    fi
    if ! command -v optipng >/dev/null 2>&1; then
        missing_tools+=("optipng")
    fi
    if ! command -v cwebp >/dev/null 2>&1; then
        missing_tools+=("webp")
    fi
    
    if [ ${#missing_tools[@]} -gt 0 ]; then
        echo "Installing optimization tools: ${missing_tools[*]}"
        
        # Install tools
        if command -v apt >/dev/null 2>&1; then
            sudo apt update
            sudo apt install -y jpegoptim optipng webp
        elif command -v yum >/dev/null 2>&1; then
            sudo yum install -y jpegoptim optipng libwebp-tools
        elif command -v pacman >/dev/null 2>&1; then
            sudo pacman -S jpegoptim optipng webp
        else
            echo "Please install: ${missing_tools[*]}"
            exit 1
        fi
    fi
}

check_tools

# Optimize JPEG files
echo "Optimizing JPEG files..."
find "$CONTENT_DIR" -name "*.jpg" -o -name "*.jpeg" | while read -r img; do
    echo "  Optimizing: $(basename "$img")"
    
    # Get original size
    original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
    
    # Optimize
    jpegoptim --strip-all --max="$JPEG_QUALITY" "$img"
    
    # Get new size
    new_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
    
    # Calculate savings
    savings=$((original_size - new_size))
    if [ $savings -gt 0 ]; then
        echo "    Saved: $savings bytes"
    fi
done

# Optimize PNG files
echo "Optimizing PNG files..."
find "$CONTENT_DIR" -name "*.png" | while read -r img; do
    echo "  Optimizing: $(basename "$img")"
    
    # Get original size
    original_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
    
    # Optimize
    optipng -o"$PNG_OPTIMIZATION_LEVEL" "$img"
    
    # Get new size
    new_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
    
    # Calculate savings
    savings=$((original_size - new_size))
    if [ $savings -gt 0 ]; then
        echo "    Saved: $savings bytes"
    fi
done

# Create WebP versions for modern browsers
echo "Creating WebP versions..."
find "$CONTENT_DIR" -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read -r img; do
    webp_file="${img%.*}.webp"
    if [ ! -f "$webp_file" ]; then
        echo "  Creating WebP: $(basename "$webp_file")"
        cwebp -q 85 "$img" -o "$webp_file"
        
        # Update HTML to use WebP with fallback
        relative_path=$(echo "$img" | sed "s|$CONTENT_DIR/||")
        webp_path=$(echo "$webp_file" | sed "s|$CONTENT_DIR/||")
        
        find "$CONTENT_DIR" -name "*.html" -exec sed -i.bak \
            "s|src=\"$relative_path\"|src=\"$webp_path\"|g" {} \;
    fi
done

echo "Image optimization complete!"
```

### Responsive Image Optimization
```bash
#!/bin/bash
# create_responsive_images.sh - Create multiple sizes for different devices

CONTENT_DIR="$1"

echo "Creating responsive images in: $CONTENT_DIR"

# Check for ImageMagick
if ! command -v convert >/dev/null 2>&1; then
    echo "Installing ImageMagick..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt install imagemagick
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install ImageMagick
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -S imagemagick
    fi
fi

# Define responsive sizes
SIZES=(400 800 1200 1600)

find "$CONTENT_DIR" -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read -r img; do
    filename=$(basename "$img" | sed 's/\.[^.]*$//')
    dir=$(dirname "$img")
    
    echo "Creating responsive versions of: $filename"
    
    # Get original dimensions
    dimensions=$(identify "$img" | awk '{print $3}')
    width=$(echo "$dimensions" | cut -d'x' -f1)
    height=$(echo "$dimensions" | cut -d'x' -f2)
    
    # Create different sizes
    for size in "${SIZES[@]}"; do
        if [ "$width" -gt "$size" ]; then
            output_file="$dir/${filename}_${size}w.${img##*.}"
            convert "$img" -resize "${size}x>" "$output_file"
            echo "  Created: ${filename}_${size}w.${img##*.}"
        fi
    done
    
    # Create srcset attribute for HTML
    srcset=""
    for size in "${SIZES[@]}"; do
        if [ -f "$dir/${filename}_${size}w.${img##*.}" ]; then
            if [ ! -z "$srcset" ]; then
                srcset="$srcset, "
            fi
            srcset="${srcset}${filename}_${size}w.${img##*.} ${size}w"
        fi
    done
    
    if [ ! -z "$srcset" ]; then
        echo "  Srcset: $srcset"
    fi
done

echo "Responsive image creation complete!"
```

## HTML and CSS Optimization

### HTML Minification
```bash
#!/bin/bash
# minify_html.sh - Minify HTML files

CONTENT_DIR="$1"

echo "Minifying HTML files in: $CONTENT_DIR"

# Check for htmlcompressor or tidy
if ! command -v htmlcompressor >/dev/null 2>&1; then
    echo "Installing htmlcompressor..."
    npm install -g htmlcompressor
fi

find "$CONTENT_DIR" -name "*.html" | while read -r html_file; do
    echo "Minifying: $(basename "$html_file")"
    
    # Backup original
    cp "$html_file" "$html_file.backup"
    
    # Minify HTML
    htmlcompressor --type html --remove-intermediate-spaces --remove-quotes "$html_file" > "$html_file.tmp"
    mv "$html_file.tmp" "$html_file"
    
    echo "  Completed: $(basename "$html_file")"
done

echo "HTML minification complete!"
```

### CSS Optimization
```bash
#!/bin/bash
# optimize_css.sh - Optimize CSS files

CONTENT_DIR="$1"

echo "Optimizing CSS files in: $CONTENT_DIR"

# Check for clean-css-cli
if ! command -v cleancss >/dev/null 2>&1; then
    echo "Installing clean-css-cli..."
    npm install -g clean-css-cli
fi

find "$CONTENT_DIR" -name "*.css" | while read -r css_file; do
    echo "Optimizing: $(basename "$css_file")"
    
    # Get original size
    original_size=$(wc -c < "$css_file")
    
    # Backup original
    cp "$css_file" "$css_file.backup"
    
    # Minify CSS
    cleancss -o "$css_file" "$css_file"
    
    # Get new size
    new_size=$(wc -c < "$css_file")
    
    # Calculate savings
    savings=$((original_size - new_size))
    echo "  Saved: $savings bytes"
    
    echo "  Completed: $(basename "$css_file")"
done

echo "CSS optimization complete!"
```

### Combine and Optimize CSS
```bash
#!/bin/bash
# combine_css.sh - Combine multiple CSS files into one

CONTENT_DIR="$1"
OUTPUT_FILE="$2"

if [ -z "$OUTPUT_FILE" ]; then
    OUTPUT_FILE="$CONTENT_DIR/assets/combined.css"
fi

echo "Combining CSS files in: $CONTENT_DIR"

# Find all CSS files
css_files=$(find "$CONTENT_DIR" -name "*.css" -not -name "combined.css")

if [ ! -z "$css_files" ]; then
    echo "Combining CSS files into: $OUTPUT_FILE"
    
    # Create output directory
    mkdir -p "$(dirname "$OUTPUT_FILE")"
    
    # Combine and minify CSS
    echo "/* Combined CSS from multiple files */" > "$OUTPUT_FILE"
    for css_file in $css_files; do
        echo "" >> "$OUTPUT_FILE"
        echo "/* Source: $(basename "$css_file") */" >> "$OUTPUT_FILE"
        cleancss "$css_file" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    done
    
    echo "CSS combination complete: $OUTPUT_FILE"
    
    # Update HTML references
    find "$CONTENT_DIR" -name "*.html" -exec sed -i.bak \
        -e "s|<link rel=\"stylesheet\" href=\"[^\"]*\">|<link rel=\"stylesheet\" href=\"$(basename "$OUTPUT_FILE")\">|g" \
        {} \;
    
    echo "HTML references updated."
else
    echo "No CSS files found to combine."
fi
```

## JavaScript Optimization

### JavaScript Minification
```bash
#!/bin/bash
# minify_js.sh - Minify JavaScript files

CONTENT_DIR="$1"

echo "Minifying JavaScript files in: $CONTENT_DIR"

# Check for terser
if ! command -v terser >/dev/null 2>&1; then
    echo "Installing terser..."
    npm install -g terser
fi

find "$CONTENT_DIR" -name "*.js" | while read -r js_file; do
    echo "Minifying: $(basename "$js_file")"
    
    # Get original size
    original_size=$(wc -c < "$js_file")
    
    # Backup original
    cp "$js_file" "$js_file.backup"
    
    # Minify JavaScript
    terser "$js_file" -c -m -o "$js_file"
    
    # Get new size
    new_size=$(wc -c < "$js_file")
    
    # Calculate savings
    savings=$((original_size - new_size))
    echo "  Saved: $savings bytes"
    
    echo "  Completed: $(basename "$js_file")"
done

echo "JavaScript minification complete!"
```

### Combine JavaScript Files
```bash
#!/bin/bash
# combine_js.sh - Combine JavaScript files

CONTENT_DIR="$1"
OUTPUT_FILE="$2"

if [ -z "$OUTPUT_FILE" ]; then
    OUTPUT_FILE="$CONTENT_DIR/assets/combined.js"
fi

echo "Combining JavaScript files in: $CONTENT_DIR"

# Find all JS files
js_files=$(find "$CONTENT_DIR" -name "*.js" -not -name "combined.js")

if [ ! -z "$js_files" ]; then
    echo "Combining JavaScript files into: $OUTPUT_FILE"
    
    # Create output directory
    mkdir -p "$(dirname "$OUTPUT_FILE")"
    
    # Combine and minify JavaScript
    echo "// Combined JavaScript from multiple files" > "$OUTPUT_FILE"
    for js_file in $js_files; do
        echo "" >> "$OUTPUT_FILE"
        echo "// Source: $(basename "$js_file")" >> "$OUTPUT_FILE"
        terser "$js_file" -c -m >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    done
    
    echo "JavaScript combination complete: $OUTPUT_FILE"
    
    # Update HTML references
    find "$CONTENT_DIR" -name "*.html" -exec sed -i.bak \
        -e "s|<script src=\"[^\"]*\"></script>|<script src=\"$(basename "$OUTPUT_FILE")\"></script>|g" \
        {} \;
    
    echo "HTML references updated."
else
    echo "No JavaScript files found to combine."
fi
```

## Performance Tuning

### ZIM Package Performance Analysis
```bash
#!/bin/bash
# analyze_performance.sh - Analyze ZIM package performance

ZIM_FILE="$1"

if [ -z "$ZIM_FILE" ]; then
    echo "Usage: $0 <zim_file>"
    exit 1
fi

echo "Analyzing performance of: $ZIM_FILE"

# Get basic statistics
FILE_SIZE=$(du -h "$ZIM_FILE" | cut -f1)
TOTAL_ENTRIES=$(zimdump --list "$ZIM_FILE" | wc -l)

echo "File Statistics:"
echo "  Size: $FILE_SIZE"
echo "  Total entries: $TOTAL_ENTRIES"

# Analyze entry types
echo ""
echo "Entry Type Analysis:"
zimdump --list "$ZIM_FILE" | awk '{
    if ($1 ~ /^A/) type = "Articles"
    else if ($1 ~ /^I/) type = "Images"
    else if ($1 ~ /^J/) type = "JavaScript"
    else if ($1 ~ /^C/) type = "CSS"
    else if ($1 ~ /^M/) type = "Media"
    else type = "Other"
    count[type]++
}
END {
    for (t in count) {
        printf "  %-12s: %5d entries\n", t, count[t]
    }
}'

# Analyze file sizes
echo ""
echo "Size Distribution:"
zimdump --list "$ZIM_FILE" | awk '{
    size = $3
    if (size < 1024) size_cat = "< 1KB"
    else if (size < 10240) size_cat = "1-10KB"
    else if (size < 102400) size_cat = "10-100KB"
    else if (size < 1048576) size_cat = "100KB-1MB"
    else size_cat = "> 1MB"
    count[size_cat]++
}
END {
    for (c in count) {
        printf "  %-12s: %5d files\n", c, count[c]
    }
}'

# Performance recommendations
echo ""
echo "Performance Recommendations:"

FILE_SIZE_BYTES=$(stat -c%s "$ZIM_FILE" 2>/dev/null || stat -f%z "$ZIM_FILE")

if [ "$FILE_SIZE_BYTES" -gt 104857600 ]; then  # 100MB
    echo "  • Large file detected (>100MB) - consider splitting into multiple packages"
fi

if [ "$TOTAL_ENTRIES" -gt 10000 ]; then
    echo "  • High entry count - search performance may be affected"
    echo "  • Consider using larger cluster sizes for better compression"
fi

IMAGE_COUNT=$(zimdump --list "$ZIM_FILE" | grep "^I" | wc -l)
if [ "$IMAGE_COUNT" -gt 100 ]; then
    echo "  • Many images detected - consider image optimization before packaging"
fi

echo ""
echo "Analysis complete!"
```

### Memory Usage Optimization
```bash
#!/bin/bash
# optimize_memory_usage.sh - Optimize for memory-constrained devices

CONTENT_DIR="$1"

echo "Optimizing for memory usage in: $CONTENT_DIR"

# Analyze content for memory-heavy elements
echo "Analyzing memory usage patterns..."

# Check for large CSS files
large_css=$(find "$CONTENT_DIR" -name "*.css" -size +50k)
if [ ! -z "$large_css" ]; then
    echo "Found large CSS files (>$((50*1024)) bytes):"
    echo "$large_css"
    echo "Consider breaking into smaller files or removing unused styles"
fi

# Check for large JavaScript files
large_js=$(find "$CONTENT_DIR" -name "*.js" -size +100k)
if [ ! -z "$large_js" ]; then
    echo "Found large JavaScript files (>$((100*1024)) bytes):"
    echo "$large_js"
    echo "Consider code splitting or removing unused functions"
fi

# Check for high-resolution images
echo ""
echo "Checking image resolutions..."
find "$CONTENT_DIR" -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" | while read -r img; do
    dimensions=$(identify "$img" | awk '{print $3}')
    width=$(echo "$dimensions" | cut -d'x' -f1)
    height=$(echo "$dimensions" | cut -d'x' -f2)
    
    if [ "$width" -gt 1920 ] || [ "$height" -gt 1080 ]; then
        echo "High-resolution image found: $img ($dimensions)"
        echo "  Consider resizing for web use"
    fi
done

echo "Memory usage optimization analysis complete!"
```

### Accessibility Optimization
```bash
#!/bin/bash
# optimize_accessibility.sh - Improve accessibility of content

CONTENT_DIR="$1"

echo "Optimizing accessibility in: $CONTENT_DIR"

find "$CONTENT_DIR" -name "*.html" | while read -r html_file; do
    echo "Checking: $html_file"
    
    # Check for alt attributes in images
    missing_alts=$(grep -o '<img[^>]*>' "$html_file" | grep -v 'alt=' | wc -l)
    if [ "$missing_alts" -gt 0 ]; then
        echo "  Found $missing_alts images without alt attributes"
    fi
    
    # Check for heading structure
    headings=$(grep -o '<h[1-6][^>]*>' "$html_file" | wc -l)
    if [ "$headings" -eq 0 ]; then
        echo "  No headings found - add headings for better structure"
    fi
    
    # Check for title attributes
    title_count=$(grep -c 'title=' "$html_file")
    if [ "$title_count" -eq 0 ]; then
        echo "  No title attributes found - consider adding for tooltips"
    fi
    
    # Check for ARIA attributes (advanced accessibility)
    aria_count=$(grep -c 'aria-' "$html_file")
    if [ "$aria_count" -eq 0 ]; then
        echo "  No ARIA attributes found - consider adding for screen readers"
    fi
    
    echo "  Completed accessibility check"
done

echo "Accessibility optimization complete!"
```

## Quality Assurance

### Comprehensive Quality Check
```bash
#!/bin/bash
# comprehensive_quality_check.sh - Complete quality assurance

CONTENT_DIR="$1"
OUTPUT_REPORT="${2:-quality-report.txt}"

echo "Running comprehensive quality check..."
echo "Quality Check Report - $(date)" > "$OUTPUT_REPORT"
echo "========================================" >> "$OUTPUT_REPORT"
echo "" >> "$OUTPUT_REPORT"

# 1. File Structure Check
echo "1. FILE STRUCTURE CHECK" >> "$OUTPUT_REPORT"
echo "------------------------" >> "$OUTPUT_REPORT"

if [ -f "$CONTENT_DIR/index.html" ]; then
    echo "✓ Index page present" >> "$OUTPUT_REPORT"
else
    echo "✗ Index page missing" >> "$OUTPUT_REPORT"
fi

if [ -f "$CONTENT_DIR/favicon.png" ]; then
    echo "✓ Favicon present" >> "$OUTPUT_REPORT"
else
    echo "✗ Favicon missing" >> "$OUTPUT_REPORT"
fi

# Check directory structure
required_dirs=("assets" "content" "metadata")
for dir in "${required_dirs[@]}"; do
    if [ -d "$CONTENT_DIR/$dir" ]; then
        echo "✓ Directory: $dir" >> "$OUTPUT_REPORT"
    else
        echo "⚠ Directory: $dir (optional)" >> "$OUTPUT_REPORT"
    fi
done

# 2. Content Quality Check
echo "" >> "$OUTPUT_REPORT"
echo "2. CONTENT QUALITY CHECK" >> "$OUTPUT_REPORT"
echo "------------------------" >> "$OUTPUT_REPORT"

# Count different file types
html_count=$(find "$CONTENT_DIR" -name "*.html" | wc -l)
css_count=$(find "$CONTENT_DIR" -name "*.css" | wc -l)
js_count=$(find "$CONTENT_DIR" -name "*.js" | wc -l)
img_count=$(find "$CONTENT_DIR" \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" -o -name "*.webp" \) | wc -l)

echo "HTML files: $html_count" >> "$OUTPUT_REPORT"
echo "CSS files: $css_count" >> "$OUTPUT_REPORT"
echo "JavaScript files: $js_count" >> "$OUTPUT_REPORT"
echo "Image files: $img_count" >> "$OUTPUT_REPORT"

# 3. Link Integrity Check
echo "" >> "$OUTPUT_REPORT"
echo "3. LINK INTEGRITY CHECK" >> "$OUTPUT_REPORT"
echo "------------------------" >> "$OUTPUT_REPORT"

broken_links=$(find "$CONTENT_DIR" -name "*.html" -exec grep -l "href=" {} \; | xargs grep -h "href=" | grep -v "^#" | grep -v "^http" | grep -v "^mailto:" | while read link; do
    link_url=$(echo "$link" | sed 's/href="//g' | sed 's/"//g' | cut -d'?' -f1)
    if [ ! -f "$CONTENT_DIR/$link_url" ] && [ ! -f "$link_url" ]; then
        echo "$link_url"
    fi
done | sort | uniq)

if [ ! -z "$broken_links" ]; then
    echo "Broken links found:" >> "$OUTPUT_REPORT"
    echo "$broken_links" >> "$OUTPUT_REPORT"
else
    echo "✓ No broken internal links found" >> "$OUTPUT_REPORT"
fi

# 4. Accessibility Check
echo "" >> "$OUTPUT_REPORT"
echo "4. ACCESSIBILITY CHECK" >> "$OUTPUT_REPORT"
echo "----------------------" >> "$OUTPUT_REPORT"

total_images=$(grep -c '<img' "$CONTENT_DIR"/*.html 2>/dev/null || echo "0")
missing_alts=$(grep -c '<img[^>]*>' "$CONTENT_DIR"/*.html 2>/dev/null | grep -v 'alt=' | wc -l || echo "0")

echo "Images with alt attributes: $(($total_images - $missing_alts))/$total_images" >> "$OUTPUT_REPORT"
if [ $missing_alts -eq 0 ]; then
    echo "✓ All images have alt attributes" >> "$OUTPUT_REPORT"
else
    echo "⚠ $missing_alts images missing alt attributes" >> "$OUTPUT_REPORT"
fi

# 5. Performance Check
echo "" >> "$OUTPUT_REPORT"
echo "5. PERFORMANCE CHECK" >> "$OUTPUT_REPORT"
echo "--------------------" >> "$OUTPUT_REPORT"

total_size=$(du -sh "$CONTENT_DIR" | cut -f1)
echo "Total package size: $total_size" >> "$OUTPUT_REPORT"

# Check for large files
large_files=$(find "$CONTENT_DIR" -size +1M -type f)
if [ ! -z "$large_files" ]; then
    echo "Large files (>1MB):" >> "$OUTPUT_REPORT"
    echo "$large_files" | while read -r file; do
        size=$(du -h "$file" | cut -f1)
        echo "  - $(basename "$file"): $size" >> "$OUTPUT_REPORT"
    done
else
    echo "✓ No large files detected" >> "$OUTPUT_REPORT"
fi

# 6. Recommendations
echo "" >> "$OUTPUT_REPORT"
echo "6. RECOMMENDATIONS" >> "$OUTPUT_REPORT"
echo "------------------" >> "$OUTPUT_REPORT"

recommendations=""

if [ ! -f "$CONTENT_DIR/index.html" ]; then
    recommendations="${recommendations}• Create index.html as main entry point\n"
fi

if [ ! -f "$CONTENT_DIR/favicon.png" ]; then
    recommendations="${recommendations}• Add favicon.png (48x48 PNG) for better branding\n"
fi

if [ "$missing_alts" -gt 0 ]; then
    recommendations="${recommendations}• Add alt attributes to $missing_alts images for accessibility\n"
fi

if [ ! -z "$broken_links" ]; then
    recommendations="${recommendations}• Fix $(echo "$broken_links" | wc -l) broken internal links\n"
fi

if [ ! -z "$large_files" ]; then
    recommendations="${recommendations}• Consider optimizing large files for faster loading\n"
fi

if [ -z "$recommendations" ]; then
    echo "✓ No critical issues found - content is ready for packaging" >> "$OUTPUT_REPORT"
else
    echo -e "$recommendations" >> "$OUTPUT_REPORT"
fi

echo "Quality check complete! Report saved to: $OUTPUT_REPORT"
cat "$OUTPUT_REPORT"
```

This comprehensive guide provides everything needed to optimize ZIM packages for both performance and user experience. The combination of proper compression settings, content optimization, and quality assurance ensures educational packages are efficient, accessible, and user-friendly.
