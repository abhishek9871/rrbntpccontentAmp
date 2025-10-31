#!/usr/bin/env python3
"""
Visualization Generator for Content Audit
Creates charts and graphs for the comprehensive audit report
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from collections import Counter
import warnings

def setup_matplotlib_for_plotting():
    """
    Setup matplotlib and seaborn for plotting with proper configuration.
    Call this function before creating any plots to ensure proper rendering.
    """
    warnings.filterwarnings('default')  # Show all warnings

    # Configure matplotlib for non-interactive mode
    plt.switch_backend("Agg")

    # Set chart style
    plt.style.use("seaborn-v0_8")
    sns.set_palette("husl")

    # Configure platform-appropriate fonts for cross-platform compatibility
    # Must be set after style.use, otherwise will be overridden by style configuration
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

def load_audit_data():
    """Load the audit data from JSON file"""
    with open('/workspace/audit/content_audit_stats.json', 'r') as f:
        return json.load(f)

def create_format_distribution_chart(data):
    """Create pie chart for file format distribution"""
    setup_matplotlib_for_plotting()
    
    formats = data['files_by_format']
    counts = list(formats.values())
    labels = list(formats.keys())
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create pie chart
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%', 
                                      colors=colors, startangle=90)
    
    # Improve text readability
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('File Format Distribution', fontsize=16, fontweight='bold', pad=20)
    
    # Add legend
    ax.legend(wedges, [f'{label}: {count}' for label, count in zip(labels, counts)],
              title="Formats",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('/workspace/audit/file_format_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_size_distribution_chart(data):
    """Create bar chart for file size distribution"""
    setup_matplotlib_for_plotting()
    
    sizes = data['files_by_size']
    categories = list(sizes.keys())
    counts = list(sizes.values())
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars = ax.bar(categories, counts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    ax.set_title('File Size Distribution', fontsize=16, fontweight='bold')
    ax.set_ylabel('Number of Files', fontsize=12)
    ax.set_xlabel('Size Category', fontsize=12)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('/workspace/audit/file_size_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_location_distribution_chart(data):
    """Create horizontal bar chart for location distribution"""
    setup_matplotlib_for_plotting()
    
    locations = data['files_by_location']
    # Sort by count for better visualization
    sorted_locations = dict(sorted(locations.items(), key=lambda x: x[1], reverse=True))
    
    categories = list(sorted_locations.keys())
    counts = list(sorted_locations.values())
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    bars = ax.barh(categories, counts, color=plt.cm.viridis(np.linspace(0, 1, len(categories))))
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'{int(width)}',
                ha='left', va='center', fontweight='bold')
    
    ax.set_title('Content Distribution by Location', fontsize=16, fontweight='bold')
    ax.set_xlabel('Number of Files', fontsize=12)
    ax.set_ylabel('Content Area', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('/workspace/audit/location_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_language_distribution_chart(data):
    """Create pie chart for language distribution"""
    setup_matplotlib_for_plotting()
    
    languages = data['language_distribution']
    counts = list(languages.values())
    labels = list(languages.keys())
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(labels)))
    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%', 
                                      colors=colors, startangle=90)
    
    # Improve text readability
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Language Distribution', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/workspace/audit/language_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_credibility_distribution_chart(data):
    """Create pie chart for source credibility distribution"""
    setup_matplotlib_for_plotting()
    
    # Count credibility levels
    credibility_counts = Counter()
    for credibility_list in data['source_credibility'].values():
        for item in credibility_list:
            credibility_counts['High'] += 1 if 'High' in str(item) else 0
            credibility_counts['Medium'] += 1 if 'Medium' in str(item) else 0
            credibility_counts['Unknown'] += 1 if 'Unknown' in str(item) else 0
    
    # Handle case where credibility is stored differently
    if sum(credibility_counts.values()) == 0:
        # Fallback to simplified categorization
        all_files = data['file_details']
        credibility_counts = Counter([file_info.get('credibility', 'Unknown') for file_info in all_files])
    
    labels = list(credibility_counts.keys())
    counts = list(credibility_counts.values())
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#2E8B57', '#FFD700', '#CD5C5C']  # Green, Gold, Red
    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%', 
                                      colors=colors, startangle=90)
    
    # Improve text readability
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title('Source Credibility Distribution', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/workspace/audit/credibility_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_comprehensive_dashboard(data):
    """Create a comprehensive dashboard with multiple charts"""
    setup_matplotlib_for_plotting()
    
    fig = plt.figure(figsize=(20, 24))
    
    # 1. File Format Distribution (Top Left)
    ax1 = plt.subplot(3, 2, 1)
    formats = data['files_by_format']
    counts = list(formats.values())
    labels = list(formats.keys())
    colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
    ax1.pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('File Format Distribution', fontsize=14, fontweight='bold')
    
    # 2. File Size Distribution (Top Right)
    ax2 = plt.subplot(3, 2, 2)
    sizes = data['files_by_size']
    categories = list(sizes.keys())
    counts = list(sizes.values())
    bars = ax2.bar(categories, counts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    ax2.set_title('File Size Distribution', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Number of Files')
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    
    # 3. Location Distribution (Middle Left)
    ax3 = plt.subplot(3, 2, 3)
    locations = data['files_by_location']
    sorted_locations = dict(sorted(locations.items(), key=lambda x: x[1], reverse=True))
    categories = list(sorted_locations.keys())[:8]  # Top 8
    counts = list(sorted_locations.values())[:8]
    ax3.barh(categories, counts, color=plt.cm.viridis(np.linspace(0, 1, len(categories))))
    ax3.set_title('Top 8 Content Areas', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Number of Files')
    
    # 4. Language Distribution (Middle Right)
    ax4 = plt.subplot(3, 2, 4)
    languages = data['language_distribution']
    counts = list(languages.values())
    labels = list(languages.keys())
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(labels)))
    ax4.pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax4.set_title('Language Distribution', fontsize=14, fontweight='bold')
    
    # 5. Subject Distribution (Bottom Left)
    ax5 = plt.subplot(3, 2, 5)
    # Count subjects from file details
    subjects = Counter([file_info.get('subject', 'Unknown') for file_info in data['file_details']])
    top_subjects = dict(subjects.most_common(6))
    categories = list(top_subjects.keys())
    counts = list(top_subjects.values())
    ax5.bar(categories, counts, color=plt.cm.tab10(np.linspace(0, 1, len(categories))))
    ax5.set_title('Top 6 Subjects', fontsize=14, fontweight='bold')
    ax5.set_ylabel('Number of Files')
    plt.setp(ax5.get_xticklabels(), rotation=45, ha='right')
    
    # 6. Summary Statistics (Bottom Right)
    ax6 = plt.subplot(3, 2, 6)
    ax6.axis('off')
    
    # Calculate summary stats
    total_size_mb = data['total_size_bytes'] / (1024 * 1024)
    avg_file_size = total_size_mb / data['total_files'] if data['total_files'] > 0 else 0
    
    summary_text = f"""AUDIT SUMMARY
    
Total Files: {data['total_files']:,}
Total Size: {total_size_mb:.2f} MB
Average File Size: {avg_file_size:.2f} KB

Top Format: {max(formats, key=formats.get)} ({formats[max(formats, key=formats.get)]} files)
Top Location: {max(locations, key=locations.get)} ({locations[max(locations, key=locations.get)]} files)
Most Common Size: Medium (1KB-1MB) - {sizes['Medium (1KB-1MB)']} files"""
    
    ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('/workspace/audit/comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Main function to generate all visualizations"""
    print("Loading audit data...")
    data = load_audit_data()
    
    print("Creating visualizations...")
    
    # Create individual charts
    create_format_distribution_chart(data)
    create_size_distribution_chart(data)
    create_location_distribution_chart(data)
    create_language_distribution_chart(data)
    create_credibility_distribution_chart(data)
    
    # Create comprehensive dashboard
    create_comprehensive_dashboard(data)
    
    print("All visualizations created successfully!")
    print("Charts saved in /workspace/audit/")

if __name__ == "__main__":
    main()
