#!/bin/bash

# Create directory structure for DIKSHA Mathematics materials
echo "Creating DIKSHA Mathematics materials directory structure..."

# Main directory structure
mkdir -p /workspace/diksha-math/study-materials/oer/mathematics/english/{number-system,ratio-proportion,time-work,simple-compound-interest,profit-loss,average-statistics,percentage,algebra,geometry,trigonometry,mensuration,time-distance}

mkdir -p /workspace/diksha-math/study-materials/oer/mathematics/hindi/{number-system,ratio-proportion,time-work,simple-compound-interest,profit-loss,average-statistics,percentage,algebra,geometry,trigonometry,mensuration,time-distance}

# Metadata and logs directories
mkdir -p /workspace/diksha-math/metadata
mkdir -p /workspace/diksha-math/logs

# Create initial log file
echo "# DIKSHA Mathematics Materials Download Log" > /workspace/diksha-math/logs/diksha-mathematics.log
echo "Started: $(date)" >> /workspace/diksha-math/logs.log
echo "" >> /workspace/diksha-math/logs/diksha-mathematics.log

echo "Directory structure created successfully!"
echo "Location: /workspace/diksha-math/"
tree /workspace/diksha-math/ 2>/dev/null || find /workspace/diksha-math/ -type d | sort