#!/bin/bash

# DIKSHA Mathematics Materials Download Script - Priority Resources
# Focus on RRB NTPC topics: Number System, Algebra, Geometry, Statistics
# Created: 2025-10-30

set -e  # Exit on any error

# Configuration
BASE_DIR="/workspace/diksha-math/study-materials/oer/mathematics"
LOG_FILE="/workspace/diksha-math/logs/download.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Create directories if they don't exist
mkdir -p "${BASE_DIR}/english/number-system"
mkdir -p "${BASE_DIR}/english/algebra"
mkdir -p "${BASE_DIR}/english/geometry"
mkdir -p "${BASE_DIR}/english/statistics"
mkdir -p "${BASE_DIR}/hindi/number-system"
mkdir -p "${BASE_DIR}/hindi/algebra"
mkdir -p "${BASE_DIR}/hindi/geometry"
mkdir -p "${BASE_DIR}/hindi/statistics"

# Logging function
log() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}

# Download function with retry logic
download_with_retry() {
    local url="$1"
    local output="$2"
    local description="$3"
    local retries=3
    local timeout=300
    
    log "Starting download: $description"
    log "URL: $url"
    log "Output: $output"
    
    for ((i=1; i<=retries; i++)); do
        log "Attempt $i of $retries..."
        
        if curl -L -f --max-time "$timeout" --retry 3 --retry-delay 2 \
                --connect-timeout 30 --continue-at - \
                -o "$output" "$url" 2>/dev/null; then
            if [ -f "$output" ] && [ -s "$output" ]; then
                local size=$(du -h "$output" | cut -f1)
                log "✅ SUCCESS: $description (Size: $size)"
                return 0
            else
                log "❌ FAILED: Downloaded file is empty or corrupted"
                rm -f "$output"
            fi
        else
            log "❌ FAILED: Attempt $i failed"
            rm -f "$output"
            sleep 5
        fi
    done
    
    log "💥 FAILED: All attempts exhausted for $description"
    return 1
}

# Priority Downloads
log "=== Starting Priority Downloads for RRB NTPC Topics ==="

# 1. Number System - Class 8 Mathematics
download_with_retry \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/number-system/ncert_class8_number_system.pdf" \
    "NCERT Class 8 Mathematics - Number System"

# 2. Algebra - Class 8 Mathematics
download_with_retry \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/algebra/ncert_class8_algebra.pdf" \
    "NCERT Class 8 Mathematics - Algebra"

# 3. Geometry - Practical Geometry Class 8
download_with_retry \
    "https://askcbse.com/wp-content/uploads/2022/05/14.-PRACTICAL-GEOMETRY.pdf" \
    "${BASE_DIR}/english/geometry/practical_geometry_class8.pdf" \
    "CBSE Practical Geometry - Class 8"

# 4. Statistics - Class 8 Data Handling
download_with_retry \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/statistics/ncert_class8_statistics.pdf" \
    "NCERT Class 8 Statistics - Data Handling"

# 5. Class 9 Number Systems (Advanced)
download_with_retry \
    "https://www.ncert.nic.in/textbook/pdf/hemh111.pdf" \
    "${BASE_DIR}/english/number-system/ncert_class9_number_systems.pdf" \
    "NCERT Class 9 Mathematics - Number Systems"

# 6. Class 9 Algebra (Polynomials)
download_with_retry \
    "https://www.ncert.nic.in/textbook/pdf/hemh113.pdf" \
    "${BASE_DIR}/english/algebra/ncert_class9_polynomials.pdf" \
    "NCERT Class 9 Mathematics - Polynomials"

# 7. Class 10 Trigonometry
download_with_retry \
    "https://www.ncert.nic.in/textbook/pdf/hemh112.pdf" \
    "${BASE_DIR}/english/trigonometry/ncert_class10_trigonometry.pdf" \
    "NCERT Class 10 Mathematics - Trigonometry"

# 8. Class 10 Statistics
download_with_retry \
    "https://www.ncert.nic.in/textbook/pdf/hemh114.pdf" \
    "${BASE_DIR}/english/statistics/ncert_class10_statistics.pdf" \
    "NCERT Class 10 Mathematics - Statistics"

# 9. Class 8 Mensuration
download_with_retry \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/mensuration/ncert_class8_mensuration.pdf" \
    "NCERT Class 8 Mathematics - Mensuration"

# 10. Class 9 Coordinate Geometry
download_with_retry \
    "https://www.ncert.nic.in/textbook/pdf/hemh115.pdf" \
    "${BASE_DIR}/english/geometry/ncert_class9_coordinate_geometry.pdf" \
    "NCERT Class 9 Mathematics - Coordinate Geometry"

log "=== Download Process Completed ==="

# Generate summary
echo ""
echo "=== DOWNLOAD SUMMARY ==="
echo "Files downloaded in: $BASE_DIR"
echo ""
echo "English resources:"
find "${BASE_DIR}/english" -name "*.pdf" -exec echo "  - {}" \; | sort
echo ""
echo "Total downloads completed!"
echo "Check $LOG_FILE for detailed logs."