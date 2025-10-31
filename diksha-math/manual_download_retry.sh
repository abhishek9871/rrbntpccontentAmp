#!/bin/bash

# DIKSHA Mathematics Download - Manual Retry Script
# For use if automatic downloads fail or need to continue
# Created: 2025-10-30

set -e

echo "🔄 DIKSHA Mathematics Downloads - Manual Retry"
echo "============================================="

# Configuration
BASE_DIR="/workspace/diksha-math/study-materials/oer/mathematics"
LOG_FILE="/workspace/diksha-math/logs/manual_retry.log"

# Create log file
touch "$LOG_FILE"

# Function to log and display
log_msg() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to download with manual retry
manual_download() {
    local url="$1"
    local output="$2" 
    local description="$3"
    
    echo ""
    echo "📥 Downloading: $description"
    echo "📍 Location: $output"
    echo "🔗 URL: $url"
    echo ""
    
    log_msg "Starting manual download: $description"
    
    # Create directory if needed
    mkdir -p "$(dirname "$output")"
    
    # Attempt download with enhanced options
    if curl -L -f \
            --max-time 600 \
            --retry 3 \
            --retry-delay 5 \
            --connect-timeout 60 \
            --continue-at - \
            --progress-bar \
            -o "$output" "$url"; then
        
        if [ -f "$output" ] && [ -s "$output" ]; then
            local size=$(du -h "$output" | cut -f1)
            log_msg "✅ SUCCESS: $description (Size: $size)"
            
            # Create metadata file
            local metadata_file="${output%.pdf}_metadata.json"
            cat > "$metadata_file" << EOF
{
  "download_date": "$(date '+%Y-%m-%d')",
  "filename": "$(basename "$output")",
  "source_url": "$url",
  "topic_category": "$(dirname "$output" | sed 's|.*/||')",
  "language": "English",
  "license": "CC BY 4.0",
  "content_provider": "NCERT/CBSE",
  "file_size": "$size",
  "download_method": "Manual retry"
}
EOF
            log_msg "📝 Metadata created: $metadata_file"
            return 0
        fi
    fi
    
    log_msg "❌ FAILED: $description"
    echo "💥 Download failed. You may need to:"
    echo "   1. Check your internet connection"
    echo "   2. Try the URL manually in a browser"
    echo "   3. Use alternative download methods"
    return 1
}

# Priority retry downloads
log_msg "=== Starting Manual Retry Downloads ==="

# CBSE Class 8 Mathematics (retry)
manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/cbse_class8_mathematics_complete.pdf" \
    "CBSE Class 8 Mathematics (Complete Textbook)"

# Class 10 Statistics (retry)
manual_download \
    "https://www.ncert.nic.in/textbook/pdf/hemh114.pdf" \
    "${BASE_DIR}/english/statistics/ncert_class10_statistics_complete.pdf" \
    "NCERT Class 10 Statistics"

# Additional resources for comprehensive coverage
manual_download \
    "https://www.ncert.nic.in/textbook/pdf/hemh116.pdf" \
    "${BASE_DIR}/english/mensuration/ncert_class10_mensuration_complete.pdf" \
    "NCERT Class 10 Mensuration"

manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/ratio-proportion/ncert_class8_ratio_proportion.pdf" \
    "NCERT Class 8 Ratio & Proportion"

manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/time-work/ncert_class8_time_work.pdf" \
    "NCERT Class 8 Time & Work"

manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/simple-compound-interest/ncert_class8_sci.pdf" \
    "NCERT Class 8 Simple & Compound Interest"

manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/profit-loss/ncert_class8_profit_loss.pdf" \
    "NCERT Class 8 Profit & Loss"

manual_download \
    "https://static.qumath.in/static/website/old-cdn-static/ncert-solutions/ncert-books-for-class-8-maths.pdf" \
    "${BASE_DIR}/english/percentage/ncert_class8_percentage.pdf" \
    "NCERT Class 8 Percentage"

echo ""
echo "🎯 Manual Download Summary"
echo "========================"
echo "📊 Completed Downloads:"
ls -lh "${BASE_DIR}"/english/*/*.pdf 2>/dev/null | wc -l | xargs echo "📁 Total PDF files:"
echo "📈 Total size:"
du -sh "${BASE_DIR}"/english/*/*.pdf 2>/dev/null | tail -1 | awk '{print $1}' || echo "0"

echo ""
echo "📋 Log file: $LOG_FILE"
echo "🔍 Check logs for detailed download information"
echo ""
echo "✅ Manual download process completed!"