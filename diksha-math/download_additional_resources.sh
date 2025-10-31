#!/bin/bash

# DIKSHA Mathematics Complete Download Script
# For additional resources beyond priority downloads
# Created: 2025-10-30

set -e

BASE_DIR="/workspace/diksha-math/study-materials/oer/mathematics"
LOG_FILE="/workspace/diksha-math/logs/complete_download.log"

mkdir -p "${BASE_DIR}/english/ratio-proportion"
mkdir -p "${BASE_DIR}/english/time-work"
mkdir -p "${BASE_DIR}/english/simple-compound-interest"
mkdir -p "${BASE_DIR}/english/profit-loss"
mkdir -p "${BASE_DIR}/english/average-statistics"
mkdir -p "${BASE_DIR}/english/percentage"
mkdir -p "${BASE_DIR}/english/time-distance"
mkdir -p "${BASE_DIR}/english/mensuration"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

download_file() {
    local url="$1"
    local output="$2"
    local description="$3"
    
    log "Downloading: $description"
    
    if curl -L -f --max-time 300 --retry 3 --retry-delay 2 \
            --connect-timeout 30 --continue-at - \
            -o "$output" "$url" 2>/dev/null; then
        if [ -f "$output" ] && [ -s "$output" ]; then
            local size=$(du -h "$output" | cut -f1)
            log "✅ SUCCESS: $description (Size: $size)"
            return 0
        fi
    fi
    
    log "❌ FAILED: $description"
    rm -f "$output"
    return 1
}

echo "=== Starting Complete Downloads ==="
log "=== Starting Complete Downloads for Remaining Topics ==="

# Additional resources for comprehensive coverage
download_file \
    "https://www.ncert.nic.in/textbook/pdf/hemh114.pdf" \
    "${BASE_DIR}/english/average-statistics/ncert_class10_statistics_complete.pdf" \
    "NCERT Class 10 Statistics - Complete"

download_file \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/ratio-proportion/class8_ratio_proportion.pdf" \
    "NCERT Class 8 - Ratio & Proportion"

download_file \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/time-work/class8_time_work.pdf" \
    "NCERT Class 8 - Time & Work"

download_file \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/simple-compound-interest/class8_simple_compound_interest.pdf" \
    "NCERT Class 8 - Simple & Compound Interest"

download_file \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/profit-loss/class8_profit_loss.pdf" \
    "NCERT Class 8 - Profit & Loss"

download_file \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/percentage/class8_percentage.pdf" \
    "NCERT Class 8 - Percentage"

download_file \
    "https://www.ncert.nic.in/textbook/pdf/hemh116.pdf" \
    "${BASE_DIR}/english/mensuration/ncert_class10_mensuration.pdf" \
    "NCERT Class 10 - Mensuration"

echo "=== Downloads Complete ==="
log "=== Downloads Complete ==="

# Summary
echo ""
echo "=== DOWNLOAD SUMMARY ==="
find "${BASE_DIR}/english" -name "*.pdf" -exec ls -lh {} \; | awk '{print $9, "-", $5}' | sort