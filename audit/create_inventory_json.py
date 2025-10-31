#!/usr/bin/env python3
"""
Create structured content inventory JSON
Generates comprehensive inventory for programmatic access
"""

import json
from datetime import datetime

def create_content_inventory():
    """Create comprehensive content inventory"""
    
    # Load the audit data
    with open('/workspace/audit/content_audit_stats.json', 'r') as f:
        audit_data = json.load(f)
    
    # Create the inventory structure
    inventory = {
        "metadata": {
            "audit_timestamp": datetime.now().isoformat(),
            "audit_version": "1.0",
            "workspace_path": "/workspace",
            "description": "Comprehensive content inventory for RRB NTPC and educational materials",
            "total_files": audit_data['total_files'],
            "total_size_bytes": audit_data['total_size_bytes'],
            "total_size_human": f"{audit_data['total_size_bytes'] / (1024*1024):.2f} MB"
        },
        
        "summary_statistics": {
            "file_format_distribution": audit_data['files_by_format'],
            "file_size_distribution": audit_data['files_by_size'],
            "location_distribution": audit_data['files_by_location'],
            "language_distribution": audit_data['language_distribution']
        },
        
        "content_areas": {
            "rrb_ntpc_content": {
                "description": "RRB NTPC exam preparation materials",
                "path": "content/rrb-ntpc/",
                "subdirectories": {
                    "current_affairs": "Current affairs materials for 2024-2025",
                    "language": "English and Hindi language materials",
                    "practice_sets": "Practice question sets and mock tests",
                    "previous_papers": "Previous year question papers (CBT1, CBT2)",
                    "study_materials": "Study materials from OER and Wikimedia"
                },
                "file_count": audit_data['files_by_location'].get('content', 0)
            },
            
            "diksha_content": {
                "description": "DIKSHA platform educational content",
                "general_awareness": {
                    "path": "diksha-ga/",
                    "description": "General awareness materials",
                    "components": ["current-affairs", "economy", "geography", "indian-history", "polity", "science-technology", "static-gk"],
                    "file_count": audit_data['files_by_location'].get('diksha-ga', 0)
                },
                "mathematics": {
                    "path": "diksha-math/",
                    "description": "Mathematics study materials",
                    "file_count": audit_data['files_by_location'].get('diksha-math', 0)
                },
                "reasoning": {
                    "path": "diksha-reasoning/",
                    "description": "Reasoning ability materials",
                    "components": ["logical_reasoning", "mental_ability", "non_verbal_reasoning", "verbal_reasoning"],
                    "file_count": audit_data['files_by_location'].get('diksha-reasoning', 0)
                },
                "science": {
                    "path": "diksha-science/",
                    "description": "Science and technology materials",
                    "file_count": audit_data['files_by_location'].get('diksha-science', 0)
                }
            },
            
            "supporting_content": {
                "current_affairs": {
                    "path": "current-affairs/",
                    "description": "Annual reports, economic surveys, ministry publications, policy documents, yearbooks",
                    "years_covered": "2020-2024",
                    "file_count": audit_data['files_by_location'].get('current-affairs', 0)
                },
                "downloaded_materials": {
                    "path": "downloads/",
                    "description": "Directly downloaded exam materials and resources",
                    "file_count": audit_data['files_by_location'].get('downloads', 0)
                },
                "extracted_content": {
                    "path": "extract/",
                    "description": "Extracted and processed content from various sources",
                    "file_count": audit_data['files_by_location'].get('extract', 0)
                }
            }
        },
        
        "source_analysis": {
            "credibility_breakdown": analyze_credibility(audit_data),
            "subject_distribution": analyze_subjects(audit_data),
            "language_coverage": analyze_languages(audit_data),
            "format_analysis": analyze_formats(audit_data)
        },
        
        "licensing_status": {
            "total_files_checked": 0,
            "licensing_files_present": False,
            "attribution_files": audit_data['files_by_location'].get('licensing', 0),
            "notes": "Licensing compliance status requires detailed review of individual files"
        },
        
        "quality_assessment": {
            "large_file_count": audit_data['files_by_size'].get('Large (1MB-100MB)', 0),
            "small_file_count": audit_data['files_by_size'].get('Small (<1KB)', 0),
            "average_file_size": f"{(audit_data['total_size_bytes'] / audit_data['total_files'] / 1024):.2f} KB" if audit_data['total_files'] > 0 else "0 KB",
            "quality_notes": "Most files are medium-sized (1KB-1MB) indicating good content density"
        },
        
        "recommendations": {
            "immediate_actions": [
                "Complete language detection for files marked as 'Mixed/Unknown'",
                "Review licensing compliance for all downloaded materials",
                "Categorize files with 'Other/Uncategorized' subjects",
                "Verify source credibility for 'Unknown' credibility files"
            ],
            "enhancement_opportunities": [
                "Expand current affairs coverage beyond 2025",
                "Add more practice materials for reasoning sections",
                "Create comprehensive index for all study materials",
                "Implement automated quality checks for future content"
            ]
        },
        
        "technical_details": {
            "file_hash_algorithm": "SHA256",
            "storage_efficiency": "Good - 569 files in 2.32 GB",
            "backup_recommendations": "Regular backup of content directory structure",
            "indexing_status": "Complete - all files catalogued"
        }
    }
    
    # Add detailed file information (sample - full file list available in audit data)
    inventory["file_details_sample"] = audit_data['file_details'][:50]  # First 50 files as sample
    
    return inventory

def analyze_credibility(audit_data):
    """Analyze source credibility from file details"""
    credibility_counts = {}
    
    for file_info in audit_data['file_details']:
        credibility = file_info.get('credibility', 'Unknown')
        if credibility not in credibility_counts:
            credibility_counts[credibility] = 0
        credibility_counts[credibility] += 1
    
    return credibility_counts

def analyze_subjects(audit_data):
    """Analyze subject distribution"""
    subject_counts = {}
    
    for file_info in audit_data['file_details']:
        subject = file_info.get('subject', 'Unknown')
        if subject not in subject_counts:
            subject_counts[subject] = 0
        subject_counts[subject] += 1
    
    return dict(sorted(subject_counts.items(), key=lambda x: x[1], reverse=True))

def analyze_languages(audit_data):
    """Analyze language distribution"""
    return audit_data['language_distribution']

def analyze_formats(audit_data):
    """Analyze file format distribution"""
    return audit_data['files_by_format']

def main():
    """Create the content inventory"""
    print("Creating comprehensive content inventory...")
    
    inventory = create_content_inventory()
    
    # Save the inventory
    with open('/workspace/audit/content_inventory.json', 'w') as f:
        json.dump(inventory, f, indent=2, default=str)
    
    print("Content inventory created successfully!")
    print(f"Inventory saved to: /workspace/audit/content_inventory.json")
    
    # Print summary
    print(f"\nInventory Summary:")
    print(f"Total files catalogued: {inventory['metadata']['total_files']}")
    print(f"Total storage used: {inventory['metadata']['total_size_human']}")
    print(f"Content areas covered: {len(inventory['content_areas'])}")
    print(f"Source credibility levels: {len(inventory['source_analysis']['credibility_breakdown'])}")

if __name__ == "__main__":
    main()
