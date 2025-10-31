#!/bin/bash

###############################################################################
# ZIM Package Build Script
# 
# This script automates the creation of ZIM packages from RRB NTPC content.
# Creates 3 distinct content bundles for comprehensive exam preparation.
#
# Usage: ./build_zim_packages.sh [options]
# Options:
#   --all, -a              Build all packages (default)
#   --general-awareness    Build only General Awareness package
#   --science             Build only Science package  
#   --complete            Build only Complete package
#   --clean, -c           Clean build artifacts before building
#   --verbose, -v         Enable verbose output
#   --help, -h            Show this help message
#
# Dependencies: zimwriterfs, zimcheck, tar, gzip
# Source: /workspace/content/rrb-ntpc/
# Output: /workspace/zim-packages/openzim/zim-build-scripts/output/
###############################################################################

set -e  # Exit on any error

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/output"
LOG_DIR="$ROOT_DIR/logs"
BUILD_MANIFESTS="$ROOT_DIR/../build-manifests"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Build options
CLEAN_BUILD=false
VERBOSE=false
BUILD_TARGET="all"

# Source directories
SOURCE_BASE="/workspace/content/rrb-ntpc"
GA_SOURCE="$SOURCE_BASE/study-materials/wikimedia/general-awareness"
SCIENCE_SOURCE="$SOURCE_BASE/study-materials/wikimedia/science"
COMPLETE_SOURCE="$SOURCE_BASE/study-materials"

# Package configuration
PACKAGES=(
    "rrb-ntpc-general-awareness"
    "rrb-ntpc-science"  
    "rrb-ntpc-complete"
)

# ZIM tool commands (will be set after tool detection)
ZIMWRITERFS=""
ZIMCHECK=""

###############################################################################
# Utility Functions
###############################################################################

log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case "$level" in
        "INFO")
            echo -e "${GREEN}[INFO]${NC} $timestamp: $message" | tee -a "$LOG_DIR/build.log"
            ;;
        "WARN")
            echo -e "${YELLOW}[WARN]${NC} $timestamp: $message" | tee -a "$LOG_DIR/build.log"
            ;;
        "ERROR")
            echo -e "${RED}[ERROR]${NC} $timestamp: $message" | tee -a "$LOG_DIR/build.log"
            ;;
        "DEBUG")
            if [ "$VERBOSE" = true ]; then
                echo -e "${BLUE}[DEBUG]${NC} $timestamp: $message"
            fi
            ;;
    esac
}

show_help() {
    cat << EOF
ZIM Package Build Script

Usage: $0 [OPTIONS]

Options:
    --all, -a              Build all packages (default)
    --general-awareness    Build only General Awareness package
    --science             Build only Science package  
    --complete            Build only Complete package
    --clean, -c           Clean build artifacts before building
    --verbose, -v         Enable verbose output
    --help, -h            Show this help message

Dependencies:
    - zimwriterfs: For creating ZIM files
    - zimcheck: For verifying ZIM file integrity
    - Standard Unix tools: tar, gzip, find

Source Directories:
    - $SOURCE_BASE

Output Directory:
    - $OUTPUT_DIR

Examples:
    $0                     # Build all packages
    $0 --general-awareness # Build only General Awareness package
    $0 --clean --verbose   # Clean build with verbose output

EOF
}

check_dependencies() {
    log "INFO" "Checking dependencies..."
    
    # Check for required tools
    local missing_tools=()
    
    # Check for zimwriterfs
    if command -v zimwriterfs >/dev/null 2>&1; then
        ZIMWRITERFS=$(command -v zimwriterfs)
        log "INFO" "Found zimwriterfs: $ZIMWRITERFS"
    else
        missing_tools+=("zimwriterfs")
        log "WARN" "zimwriterfs not found. Please install zim-tools package."
    fi
    
    # Check for zimcheck
    if command -v zimcheck >/dev/null 2>&1; then
        ZIMCHECK=$(command -v zimcheck)
        log "INFO" "Found zimcheck: $ZIMCHECK"
    else
        missing_tools+=("zimcheck")
        log "WARN" "zimcheck not found. Please install zim-tools package."
    fi
    
    # Check for basic Unix tools
    local basic_tools=("tar" "gzip" "find" "md5sum" "sha256sum")
    for tool in "${basic_tools[@]}"; do
        if ! command -v "$tool" >/dev/null 2>&1; then
            missing_tools+=("$tool")
        fi
    done
    
    if [ ${#missing_tools[@]} -gt 0 ]; then
        log "ERROR" "Missing required tools: ${missing_tools[*]}"
        log "ERROR" "Please install missing tools before proceeding."
        return 1
    fi
    
    log "INFO" "All dependencies satisfied."
    return 0
}

setup_directories() {
    log "INFO" "Setting up directories..."
    
    # Create output directories
    mkdir -p "$OUTPUT_DIR"
    mkdir -p "$LOG_DIR"
    mkdir -p "$BUILD_MANIFESTS"
    
    # Create package-specific output directories
    for package in "${PACKAGES[@]}"; do
        mkdir -p "$OUTPUT_DIR/$package"
        mkdir -p "$OUTPUT_DIR/$package/temp"
        mkdir -p "$OUTPUT_DIR/$package/final"
    done
    
    log "INFO" "Directory setup complete."
}

clean_build() {
    log "INFO" "Cleaning previous build artifacts..."
    
    # Clean output directory
    if [ -d "$OUTPUT_DIR" ]; then
        rm -rf "$OUTPUT_DIR"/*
        log "INFO" "Cleaned output directory: $OUTPUT_DIR"
    fi
    
    # Clean log directory (keep the current log)
    if [ -d "$LOG_DIR" ]; then
        find "$LOG_DIR" -name "*.log" -not -name "build.log" -delete 2>/dev/null || true
        log "INFO" "Cleaned old log files."
    fi
    
    # Recreate directories
    setup_directories
}

###############################################################################
# Build Functions
###############################################################################

build_general_awareness_package() {
    local package_name="rrb-ntpc-general-awareness"
    local package_dir="$OUTPUT_DIR/$package_name"
    local temp_dir="$package_dir/temp"
    local final_dir="$package_dir/final"
    
    log "INFO" "Building General Awareness package..."
    
    # Prepare content directory
    local content_dir="$temp_dir/html_content"
    mkdir -p "$content_dir"
    
    # Copy general awareness content
    log "INFO" "Copying General Awareness content from $GA_SOURCE"
    cp -r "$GA_SOURCE"/* "$content_dir/" 2>/dev/null || true
    
    # Create index.html if it doesn't exist
    if [ ! -f "$content_dir/index.html" ]; then
        create_index_page "$content_dir" "RRB NTPC General Awareness"
    fi
    
    # Create favicon
    create_favicon "$temp_dir"
    
    # Generate ZIM file
    generate_zim_file "$content_dir" "$final_dir/${package_name}.zim" "RRB NTPC General Awareness" \
        "Complete general awareness content for RRB NTPC exam preparation" \
        "RRB NTPC Team" "OpenZIM Project"
    
    # Verify ZIM file
    verify_zim_file "$final_dir/${package_name}.zim"
    
    # Generate checksums
    generate_checksums "$final_dir"
    
    # Create package manifest
    create_package_manifest "$package_name" "$final_dir"
    
    log "INFO" "General Awareness package build complete: $final_dir/${package_name}.zim"
}

build_science_package() {
    local package_name="rrb-ntpc-science"
    local package_dir="$OUTPUT_DIR/$package_name"
    local temp_dir="$package_dir/temp"
    local final_dir="$package_dir/final"
    
    log "INFO" "Building Science package..."
    
    # Prepare content directory
    local content_dir="$temp_dir/html_content"
    mkdir -p "$content_dir"
    
    # Copy science content
    log "INFO" "Copying Science content from $SCIENCE_SOURCE"
    cp -r "$SCIENCE_SOURCE"/* "$content_dir/" 2>/dev/null || true
    
    # Create index.html if it doesn't exist
    if [ ! -f "$content_dir/index.html" ]; then
        create_index_page "$content_dir" "RRB NTPC Science & Technology"
    fi
    
    # Create favicon
    create_favicon "$temp_dir"
    
    # Generate ZIM file
    generate_zim_file "$content_dir" "$final_dir/${package_name}.zim" "RRB NTPC Science & Technology" \
        "Science and technology content for RRB NTPC exam preparation" \
        "RRB NTPC Team" "OpenZIM Project"
    
    # Verify ZIM file
    verify_zim_file "$final_dir/${package_name}.zim"
    
    # Generate checksums
    generate_checksums "$final_dir"
    
    # Create package manifest
    create_package_manifest "$package_name" "$final_dir"
    
    log "INFO" "Science package build complete: $final_dir/${package_name}.zim"
}

build_complete_package() {
    local package_name="rrb-ntpc-complete"
    local package_dir="$OUTPUT_DIR/$package_name"
    local temp_dir="$package_dir/temp"
    local final_dir="$package_dir/final"
    
    log "INFO" "Building Complete Study Materials package..."
    
    # Prepare content directory
    local content_dir="$temp_dir/html_content"
    mkdir -p "$content_dir"
    
    # Copy complete study materials content
    log "INFO" "Copying Complete study materials from $COMPLETE_SOURCE"
    cp -r "$COMPLETE_SOURCE"/* "$content_dir/" 2>/dev/null || true
    
    # Create index.html if it doesn't exist
    if [ ! -f "$content_dir/index.html" ]; then
        create_index_page "$content_dir" "RRB NTPC Complete Study Materials"
    fi
    
    # Create favicon
    create_favicon "$temp_dir"
    
    # Generate ZIM file
    generate_zim_file "$content_dir" "$final_dir/${package_name}.zim" "RRB NTPC Complete Study Materials" \
        "Comprehensive study materials for RRB NTPC exam preparation including General Awareness and Science" \
        "RRB NTPC Team" "OpenZIM Project"
    
    # Verify ZIM file
    verify_zim_file "$final_dir/${package_name}.zim"
    
    # Generate checksums
    generate_checksums "$final_dir"
    
    # Create package manifest
    create_package_manifest "$package_name" "$final_dir"
    
    log "INFO" "Complete package build complete: $final_dir/${package_name}.zim"
}

###############################################################################
# Helper Functions
###############################################################################

create_index_page() {
    local content_dir="$1"
    local title="$2"
    
    log "DEBUG" "Creating index page for: $title"
    
    cat > "$content_dir/index.html" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }
        .content-section { margin: 30px 0; }
        .category { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .category h3 { margin-top: 0; color: #333; }
        .footer { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ccc; }
    </style>
</head>
<body>
    <div class="header">
        <h1>$title</h1>
        <p>Comprehensive preparation materials for Railway Recruitment Board NTPC exams</p>
    </div>
    
    <div class="content-section">
        <h2>Content Navigation</h2>
        <p>This package contains carefully curated study materials organized by subject areas. Browse through the categories below to access the content you need.</p>
        
        <div class="category">
            <h3>📚 Study Materials</h3>
            <p>Access organized content by subject areas including culture, economy, geography, history, polity, and science & technology.</p>
        </div>
        
        <div class="category">
            <h3>🎯 Practice Resources</h3>
            <p>Find practice sets, previous papers, and current affairs to test your knowledge.</p>
        </div>
        
        <div class="category">
            <h3>📖 Reference Materials</h3>
            <p>Comprehensive reference materials sourced from authoritative platforms like Wikipedia and educational resources.</p>
        </div>
    </div>
    
    <div class="footer">
        <p>Generated on $(date '+%Y-%m-%d %H:%M:%S') | OpenZIM Project</p>
        <p>Content curated for RRB NTPC exam preparation</p>
    </div>
</body>
</html>
EOF
    
    log "DEBUG" "Index page created successfully"
}

create_favicon() {
    local temp_dir="$1"
    
    log "DEBUG" "Creating favicon..."
    
    # Create a simple favicon (48x48 PNG placeholder)
    cat > "$temp_dir/favicon.png" << 'EOF'
iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==
EOF
    
    # Convert base64 to PNG (this is a minimal 1x1 pixel PNG)
    base64 -d > "$temp_dir/favicon.png" << 'EOF'
iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==
EOF
    
    log "DEBUG" "Favicon created successfully"
}

generate_zim_file() {
    local content_dir="$1"
    local output_file="$2"
    local title="$3"
    local description="$4"
    local creator="$5"
    local publisher="$6"
    
    log "INFO" "Generating ZIM file: $output_file"
    
    if [ -z "$ZIMWRITERFS" ]; then
        log "ERROR" "zimwriterfs not available. Creating placeholder and documentation."
        create_zim_placeholder "$output_file" "$title" "$description"
        return 0
    fi
    
    # Build zimwriterfs command
    local cmd="$ZIMWRITERFS"
    cmd="$cmd --welcome=index.html"
    cmd="$cmd --favicon=favicon.png"
    cmd="$cmd --language=eng"
    cmd="$cmd --title='$title'"
    cmd="$cmd --description='$description'"
    cmd="$cmd --creator='$creator'"
    cmd="$cmd --publisher='$publisher'"
    cmd="$cmd --withFullTextIndex"
    cmd="$cmd --tags='education;railway;ntpc;exam-preparation'"
    cmd="$cmd --name='$title'"
    cmd="$cmd --minChunkSize=2048"
    cmd="$cmd --verbose"
    
    # Add content directory and output file
    cmd="$cmd '$content_dir' '$output_file'"
    
    log "INFO" "Running: $cmd"
    
    # Execute zimwriterfs
    if eval "$cmd"; then
        log "INFO" "ZIM file generated successfully: $output_file"
        
        # Check file size and log it
        if [ -f "$output_file" ]; then
            local size=$(du -h "$output_file" | cut -f1)
            log "INFO" "ZIM file size: $size"
        fi
    else
        log "ERROR" "Failed to generate ZIM file: $output_file"
        create_zim_placeholder "$output_file" "$title" "$description"
    fi
}

create_zim_placeholder() {
    local output_file="$1"
    local title="$2"
    local description="$3"
    
    log "INFO" "Creating ZIM placeholder documentation for: $output_file"
    
    # Create documentation file explaining how to generate the ZIM file
    cat > "${output_file}.build-instructions.txt" << EOF
ZIM Package Build Instructions
==============================

Package: $title
Description: $description
Output File: $output_file

This file should be a ZIM package but zimwriterfs is not available.

To create this ZIM package:

1. Install zim-tools package:
   - Ubuntu/Debian: sudo apt install zim-tools
   - CentOS/RHEL: sudo yum install zim-tools
   - Arch Linux: sudo pacman -S zim-tools

2. Ensure you have a complete HTML content directory ready.

3. Run the zimwriterfs command:
   zimwriterfs --welcome=index.html --favicon=favicon.png --language=eng \\
       --title="$title" --description="$description" \\
       --creator="RRB NTPC Team" --publisher="OpenZIM Project" \\
       --withFullTextIndex --tags="education;railway;ntpc;exam-preparation" \\
       --name="$title" --minChunkSize=2048 --verbose \\
       <source_directory> <output_file>

4. Verify the ZIM file:
   zimcheck <output_file>

For detailed instructions, see: $ROOT_DIR/docs/zim_creation_guide.md

Generated on: $(date '+%Y-%m-%d %H:%M:%S')
EOF
    
    log "INFO" "Build instructions created: ${output_file}.build-instructions.txt"
}

verify_zim_file() {
    local zim_file="$1"
    
    log "INFO" "Verifying ZIM file: $zim_file"
    
    if [ ! -f "$zim_file" ]; then
        log "ERROR" "ZIM file not found: $zim_file"
        return 1
    fi
    
    if [ -z "$ZIMCHECK" ]; then
        log "WARN" "zimcheck not available, skipping verification"
        return 0
    fi
    
    # Run zimcheck
    if "$ZIMCHECK" "$zim_file"; then
        log "INFO" "ZIM file verification passed: $zim_file"
        return 0
    else
        log "ERROR" "ZIM file verification failed: $zim_file"
        return 1
    fi
}

generate_checksums() {
    local output_dir="$1"
    
    log "INFO" "Generating checksums for: $output_dir"
    
    # Create checksums file
    cd "$output_dir"
    
    if [ -f "*.zim" ]; then
        echo "# ZIM Package Checksums" > checksums.txt
        echo "# Generated on: $(date '+%Y-%m-%d %H:%M:%S')" >> checksums.txt
        echo "" >> checksums.txt
        
        for zim_file in *.zim; do
            if [ -f "$zim_file" ]; then
                echo "MD5: $(md5sum "$zim_file" | cut -d' ' -f1)  $zim_file" >> checksums.txt
                echo "SHA256: $(sha256sum "$zim_file" | cut -d' ' -f1)  $zim_file" >> checksums.txt
                echo "" >> checksums.txt
            fi
        done
        
        log "INFO" "Checksums generated: $output_dir/checksums.txt"
    fi
}

create_package_manifest() {
    local package_name="$1"
    local output_dir="$2"
    
    log "INFO" "Creating package manifest for: $package_name"
    
    cat > "$output_dir/package-manifest.json" << EOF
{
    "package_name": "$package_name",
    "version": "1.0.0",
    "build_date": "$(date '+%Y-%m-%d')",
    "build_time": "$(date '+%H:%M:%S')",
    "build_system": "OpenZIM Build Scripts",
    "source_content": "RRB NTPC Study Materials",
    "packages": [
        {
            "name": "$package_name",
            "type": "zim",
            "language": "eng",
            "category": "education",
            "tags": ["education", "railway", "ntpc", "exam-preparation"],
            "creator": "RRB NTPC Team",
            "publisher": "OpenZIM Project"
        }
    ],
    "build_environment": {
        "platform": "$(uname -s) $(uname -r)",
        "shell": "bash",
        "tools": {
            "zimwriterfs": "${ZIMWRITERFS:-not_available}",
            "zimcheck": "${ZIMCHECK:-not_available}"
        }
    },
    "files": $(find "$output_dir" -name "*.zim" -exec basename {} \; | jq -R . | jq -s .),
    "checksums": {
        "file": "checksums.txt",
        "generated": "$(date '+%Y-%m-%d %H:%M:%S')"
    }
}
EOF
    
    log "INFO" "Package manifest created: $output_dir/package-manifest.json"
}

###############################################################################
# Main Script Logic
###############################################################################

main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --all|-a)
                BUILD_TARGET="all"
                shift
                ;;
            --general-awareness)
                BUILD_TARGET="general-awareness"
                shift
                ;;
            --science)
                BUILD_TARGET="science"
                shift
                ;;
            --complete)
                BUILD_TARGET="complete"
                shift
                ;;
            --clean|-c)
                CLEAN_BUILD=true
                shift
                ;;
            --verbose|-v)
                VERBOSE=true
                shift
                ;;
            --help|-h)
                show_help
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Create log file
    LOG_FILE="$LOG_DIR/build_$(date '+%Y%m%d_%H%M%S').log"
    mkdir -p "$(dirname "$LOG_FILE")"
    exec 1> >(tee -a "$LOG_FILE")
    exec 2>&1
    
    log "INFO" "Starting ZIM package build process"
    log "INFO" "Script directory: $SCRIPT_DIR"
    log "INFO" "Root directory: $ROOT_DIR"
    log "INFO" "Output directory: $OUTPUT_DIR"
    log "INFO" "Build target: $BUILD_TARGET"
    log "INFO" "Clean build: $CLEAN_BUILD"
    log "INFO" "Verbose mode: $VERBOSE"
    
    # Check dependencies
    if ! check_dependencies; then
        log "ERROR" "Dependency check failed. Please install required tools."
        exit 1
    fi
    
    # Setup directories
    setup_directories
    
    # Clean build if requested
    if [ "$CLEAN_BUILD" = true ]; then
        clean_build
    fi
    
    # Execute build based on target
    case "$BUILD_TARGET" in
        "all")
            log "INFO" "Building all packages..."
            build_general_awareness_package
            build_science_package
            build_complete_package
            ;;
        "general-awareness")
            build_general_awareness_package
            ;;
        "science")
            build_science_package
            ;;
        "complete")
            build_complete_package
            ;;
        *)
            log "ERROR" "Invalid build target: $BUILD_TARGET"
            show_help
            exit 1
            ;;
    esac
    
    log "INFO" "Build process completed successfully!"
    log "INFO" "Output directory: $OUTPUT_DIR"
    
    # Generate final summary
    echo ""
    echo "========================================"
    echo "    ZIM PACKAGE BUILD COMPLETE"
    echo "========================================"
    echo "Output Directory: $OUTPUT_DIR"
    echo "Log File: $LOG_FILE"
    echo "Build Date: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    
    if [ -f "$OUTPUT_DIR"/*/final/*.zim ]; then
        echo "Generated ZIM Packages:"
        find "$OUTPUT_DIR" -name "*.zim" -exec basename {} \; | while read -r file; do
            echo "  - $file"
        done
        echo ""
    fi
    
    echo "Check the log file for detailed build information."
    echo "========================================"
}

# Run main function if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
