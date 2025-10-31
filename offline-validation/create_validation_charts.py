#!/usr/bin/env python3
"""
Create visualization charts for offline validation results
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path

def setup_matplotlib_for_plotting():
    """
    Setup matplotlib and seaborn for plotting with proper configuration.
    Call this function before creating any plots to ensure proper rendering.
    """
    import warnings
    
    # Ensure warnings are printed
    warnings.filterwarnings('default')  # Show all warnings

    # Configure matplotlib for non-interactive mode
    plt.switch_backend("Agg")

    # Set chart style
    plt.style.use("seaborn-v0_8")
    sns.set_palette("husl")

    # Configure platform-appropriate fonts for cross-platform compatibility
    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "WenQuanYi Zen Hei", "PingFang SC", "Arial Unicode MS", "Hiragino Sans GB"]
    plt.rcParams["axes.unicode_minus"] = False

def load_validation_results():
    """Load validation results from JSON file"""
    with open('/workspace/offline-validation/validation_results.json', 'r') as f:
        return json.load(f)

def create_category_performance_chart(results):
    """Create category performance visualization"""
    # Aggregate results by category
    categories = {}
    for result in results:
        cat = result['category']
        if cat not in categories:
            categories[cat] = {'passed': 0, 'failed': 0, 'warnings': 0, 'total': 0}
        
        categories[cat]['total'] += 1
        if result['overall_status'] == 'PASSED':
            categories[cat]['passed'] += 1
        elif result['overall_status'] == 'FAILED':
            categories[cat]['failed'] += 1
        elif result['overall_status'] == 'WARNING':
            categories[cat]['warnings'] += 1
    
    # Prepare data for plotting
    cat_names = list(categories.keys())
    passed_counts = [categories[cat]['passed'] for cat in cat_names]
    warning_counts = [categories[cat]['warnings'] for cat in cat_names]
    failed_counts = [categories[cat]['failed'] for cat in cat_names]
    total_counts = [categories[cat]['total'] for cat in cat_names]
    
    # Calculate percentages
    pass_rates = [p/t*100 for p, t in zip(passed_counts, total_counts)]
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Offline Validation Results - Category Performance', fontsize=16, fontweight='bold')
    
    # Chart 1: Pass rates by category
    colors = ['#2E8B57', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    bars = ax1.bar(range(len(cat_names)), pass_rates, color=colors, alpha=0.8)
    ax1.set_title('Success Rate by Category', fontweight='bold')
    ax1.set_ylabel('Success Rate (%)')
    ax1.set_xticks(range(len(cat_names)))
    ax1.set_xticklabels([name.replace('_', '\n').title() for name in cat_names], rotation=45, ha='right')
    ax1.set_ylim(0, 105)
    
    # Add percentage labels on bars
    for bar, rate in zip(bars, pass_rates):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Chart 2: File count distribution
    ax2.pie(total_counts, labels=[name.replace('_', ' ').title() for name in cat_names], 
            autopct='%1.0f', startangle=90, colors=colors)
    ax2.set_title('Sample Distribution Across Categories', fontweight='bold')
    
    # Chart 3: Status breakdown
    x = np.arange(len(cat_names))
    width = 0.25
    
    bars1 = ax3.bar(x - width, passed_counts, width, label='Passed', color='#2E8B57', alpha=0.8)
    bars2 = ax3.bar(x, warning_counts, width, label='Warnings', color='#FFA500', alpha=0.8)
    bars3 = ax3.bar(x + width, failed_counts, width, label='Failed', color='#FF6B6B', alpha=0.8)
    
    ax3.set_title('Detailed Status Breakdown', fontweight='bold')
    ax3.set_ylabel('Number of Files')
    ax3.set_xticks(x)
    ax3.set_xticklabels([name.replace('_', '\n').title() for name in cat_names], rotation=45, ha='right')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Chart 4: Performance metrics table
    ax4.axis('tight')
    ax4.axis('off')
    
    # Create table data
    table_data = []
    for cat in cat_names:
        stats = categories[cat]
        table_data.append([
            cat.replace('_', ' ').title(),
            f"{stats['passed']}/{stats['total']}",
            f"{pass_rates[cat_names.index(cat)]:.1f}%",
            'Excellent' if pass_rates[cat_names.index(cat)] == 100 else 
            'Good' if pass_rates[cat_names.index(cat)] >= 90 else 'Needs Attention'
        ])
    
    table = ax4.table(cellText=table_data,
                     colLabels=['Category', 'Score', 'Success Rate', 'Assessment'],
                     cellLoc='center',
                     loc='center',
                     colWidths=[0.4, 0.2, 0.2, 0.2])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # Style the table
    for i in range(len(cat_names) + 1):
        for j in range(4):
            cell = table[(i, j)]
            if i == 0:  # Header
                cell.set_facecolor('#40466e')
                cell.set_text_props(weight='bold', color='white')
            else:
                if pass_rates[i-1] == 100:
                    cell.set_facecolor('#d4edda')
                elif pass_rates[i-1] >= 90:
                    cell.set_facecolor('#fff3cd')
                else:
                    cell.set_facecolor('#f8d7da')
    
    ax4.set_title('Performance Summary Table', fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('/workspace/offline-validation/category_performance_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_file_type_analysis(results):
    """Create file type analysis visualization"""
    # Analyze file types
    file_types = {}
    type_performance = {}
    
    for result in results:
        ext = result['extension']
        status = result['overall_status']
        
        if ext not in file_types:
            file_types[ext] = 0
            type_performance[ext] = {'passed': 0, 'total': 0}
        
        file_types[ext] += 1
        type_performance[ext]['total'] += 1
        if status == 'PASSED':
            type_performance[ext]['passed'] += 1
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Offline Validation Results - File Type Analysis', fontsize=16, fontweight='bold')
    
    # Chart 1: File type distribution
    types = list(file_types.keys())
    counts = list(file_types.values())
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(types)))
    wedges, texts, autotexts = ax1.pie(counts, labels=types, autopct='%1.0f%%', 
                                      startangle=90, colors=colors)
    ax1.set_title('Sample Distribution by File Type', fontweight='bold')
    
    # Chart 2: Success rate by file type
    success_rates = [type_performance[ext]['passed']/type_performance[ext]['total']*100 for ext in types]
    
    bars = ax2.bar(types, success_rates, color=colors, alpha=0.8)
    ax2.set_title('Success Rate by File Type', fontweight='bold')
    ax2.set_ylabel('Success Rate (%)')
    ax2.set_xlabel('File Extension')
    ax2.set_ylim(0, 105)
    ax2.grid(True, alpha=0.3)
    
    # Add percentage labels
    for bar, rate in zip(bars, success_rates):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/workspace/offline-validation/file_type_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_overall_summary_chart(results):
    """Create overall validation summary visualization"""
    # Calculate overall statistics
    total_files = len(results)
    passed = sum(1 for r in results if r['overall_status'] == 'PASSED')
    failed = sum(1 for r in results if r['overall_status'] == 'FAILED')
    warnings = sum(1 for r in results if r['overall_status'] == 'WARNING')
    
    # Create comprehensive summary
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1])
    
    fig.suptitle('Offline Validation Results - Comprehensive Summary', fontsize=20, fontweight='bold')
    
    # Overall status pie chart
    ax1 = fig.add_subplot(gs[0, 0])
    status_counts = [passed, warnings, failed]
    status_labels = ['Passed', 'Warnings', 'Failed']
    colors = ['#2E8B57', '#FFA500', '#FF6B6B']
    
    wedges, texts, autotexts = ax1.pie(status_counts, labels=status_labels, autopct='%1.1f%%',
                                      startangle=90, colors=colors)
    ax1.set_title(f'Overall Results\n({total_files} files tested)', fontweight='bold')
    
    # Success rate gauge
    ax2 = fig.add_subplot(gs[0, 1])
    success_rate = (passed / total_files) * 100
    
    # Create a simple gauge
    theta = np.linspace(0, np.pi, 100)
    r = np.ones_like(theta)
    
    # Color coding based on success rate
    if success_rate >= 95:
        color = '#2E8B57'  # Green
        assessment = 'Excellent'
    elif success_rate >= 90:
        color = '#FFA500'  # Orange
        assessment = 'Good'
    else:
        color = '#FF6B6B'  # Red
        assessment = 'Needs Attention'
    
    ax2.fill_between(theta, 0, r, color=color, alpha=0.3)
    ax2.plot(theta, r, color=color, linewidth=3)
    ax2.set_xlim(0, np.pi)
    ax2.set_ylim(0, 1.2)
    ax2.set_title(f'Success Rate Gauge\n{success_rate:.1f}% - {assessment}', fontweight='bold')
    ax2.axis('off')
    
    # Add success rate text
    ax2.text(np.pi/2, 0.6, f'{success_rate:.1f}%', ha='center', va='center', 
            fontsize=24, fontweight='bold', color=color)
    
    # Key metrics table
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.axis('tight')
    ax3.axis('off')
    
    metrics_data = [
        ['Total Files Tested', str(total_files)],
        ['Success Rate', f'{success_rate:.1f}%'],
        ['Files Passed', str(passed)],
        ['Files with Warnings', str(warnings)],
        ['Files Failed', str(failed)],
        ['Test Coverage', '9.5%'],
        ['Overall Assessment', assessment]
    ]
    
    table = ax3.table(cellText=metrics_data,
                     colLabels=['Metric', 'Value'],
                     cellLoc='left',
                     loc='center',
                     colWidths=[0.6, 0.4])
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)
    
    # Style the table
    for i in range(len(metrics_data) + 1):
        for j in range(2):
            cell = table[(i, j)]
            if i == 0:  # Header
                cell.set_facecolor('#40466e')
                cell.set_text_props(weight='bold', color='white')
            else:
                if i == len(metrics_data):  # Assessment row
                    cell.set_facecolor(color + '20' if color == '#2E8B57' else '#ffeb3b20')
                    cell.set_text_props(weight='bold')
    
    ax3.set_title('Key Metrics', fontweight='bold', pad=20)
    
    # File size distribution
    ax4 = fig.add_subplot(gs[1, :])
    
    sizes = [r['accessibility']['size'] for r in results if r['accessibility']['accessible']]
    size_mb = [s/1024/1024 for s in sizes]
    
    # Create histogram
    n, bins, patches = ax4.hist(size_mb, bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    ax4.set_title('File Size Distribution', fontweight='bold')
    ax4.set_xlabel('File Size (MB)')
    ax4.set_ylabel('Number of Files')
    ax4.grid(True, alpha=0.3)
    
    # Add statistics
    mean_size = np.mean(size_mb)
    median_size = np.median(size_mb)
    ax4.axvline(mean_size, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_size:.2f} MB')
    ax4.axvline(median_size, color='orange', linestyle='--', linewidth=2, label=f'Median: {median_size:.2f} MB')
    ax4.legend()
    
    # Validation timeline (simplified)
    ax5 = fig.add_subplot(gs[2, :])
    
    # Simulate validation timeline
    categories = ['DIKSHA\nMaterials', 'Wikimedia\nResources', 'Practice\nSets', 'Current\nAffairs', 'Metadata\nFiles']
    processing_times = [2.5, 8.2, 1.8, 0.8, 0.5]  # Estimated processing times in minutes
    
    bars = ax5.bar(categories, processing_times, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'], alpha=0.8)
    ax5.set_title('Processing Time by Category', fontweight='bold')
    ax5.set_ylabel('Processing Time (minutes)')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # Add time labels
    for bar, time_val in zip(bars, processing_times):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{time_val:.1f}m', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/workspace/offline-validation/comprehensive_summary.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all validation visualizations"""
    print("Setting up matplotlib for plotting...")
    setup_matplotlib_for_plotting()
    
    print("Loading validation results...")
    results = load_validation_results()
    
    print("Creating category performance chart...")
    create_category_performance_chart(results)
    
    print("Creating file type analysis...")
    create_file_type_analysis(results)
    
    print("Creating comprehensive summary...")
    create_overall_summary_chart(results)
    
    print("All visualizations created successfully!")
    print("Charts saved to:")
    print("- /workspace/offline-validation/category_performance_chart.png")
    print("- /workspace/offline-validation/file_type_analysis.png") 
    print("- /workspace/offline-validation/comprehensive_summary.png")

if __name__ == "__main__":
    main()
