#!/usr/bin/env python3
"""
Content Organization Script for RRB-NTPC Bilingual Organization
Copies and organizes content based on language analysis
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Set
import csv

class BilingualContentOrganizer:
    def __init__(self):
        self.analysis_file = '/workspace/bilingual-org/content_analysis_results.json'
        self.target_base = '/workspace/bilingual-org/content/rrb-ntpc/language'
        self.organization_log = []
        self.org_map_data = []
        
    def load_analysis_results(self) -> List[Dict]:
        """Load content analysis results"""
        with open(self.analysis_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_target_path(self, item: Dict) -> Path:
        """Calculate target path for an item"""
        language = item['language']
        category = item['category']
        source_name = Path(item['source_path']).name
        
        # Map categories to target structure
        category_map = {
            'study-materials': 'study-materials',
            'practice-sets': 'practice-sets',
            'current-affairs': 'current-affairs',
            'previous-papers': 'previous-papers',
            'mixed': 'study-materials'  # Default mixed content to study materials
        }
        
        target_category = category_map.get(category, 'study-materials')
        
        # For 'both' language, create duplicates in both languages
        if language == 'both':
            return None  # Will be handled specially
            
        # Build target path
        target_path = Path(self.target_base) / language / target_category / source_name
        
        return target_path
    
    def ensure_target_directory(self, target_path: Path):
        """Ensure target directory exists"""
        target_path.parent.mkdir(parents=True, exist_ok=True)
    
    def copy_content(self, source_file: Path, target_path: Path) -> bool:
        """Copy content to target location"""
        try:
            if not source_file.exists():
                self.organization_log.append(f"Source file not found: {source_file}")
                return False
            
            self.ensure_target_directory(target_path)
            
            # Copy file
            shutil.copy2(source_file, target_path)
            
            self.organization_log.append(f"✓ Copied: {source_file} -> {target_path}")
            return True
            
        except Exception as e:
            self.organization_log.append(f"✗ Failed to copy {source_file}: {str(e)}")
            return False
    
    def create_symlink(self, source_file: Path, target_path: Path) -> bool:
        """Create symbolic link instead of copy"""
        try:
            if not source_file.exists():
                self.organization_log.append(f"Source file not found for symlink: {source_file}")
                return False
                
            self.ensure_target_directory(target_path)
            
            # Remove existing file/directory if it exists
            if target_path.exists():
                if target_path.is_file():
                    target_path.unlink()
                elif target_path.is_dir():
                    shutil.rmtree(target_path)
            
            # Create symlink
            target_path.symlink_to(source_file)
            
            self.organization_log.append(f"🔗 Symlinked: {source_file} -> {target_path}")
            return True
            
        except Exception as e:
            self.organization_log.append(f"✗ Failed to symlink {source_file}: {str(e)}")
            return False
    
    def add_to_org_map(self, item: Dict, target_path: Path, operation: str):
        """Add entry to organization map CSV data"""
        org_entry = {
            'original_path': str(Path(item['source_path']) / item['relative_path']),
            'filename': item['filename'],
            'language': item['language'],
            'category': item['category'],
            'source': item['source_path'],
            'target_path': str(target_path),
            'operation': operation,
            'file_type': item['file_type'],
            'size_bytes': item['size_bytes'],
            'confidence': item['confidence'],
            'detection_method': item['detection_method']
        }
        self.org_map_data.append(org_entry)
    
    def handle_bilingual_content(self, item: Dict, source_file: Path, base_target_path: Path):
        """Handle content available in both languages"""
        # For bilingual content, create copies in both language directories
        for lang in ['en', 'hi']:
            target_path = base_target_path.parent.parent / lang / base_target_path.name / base_target_path.name / item['filename']
            if self.copy_content(source_file, target_path):
                self.add_to_org_map(item, target_path, 'copy_bilingual')
    
    def organize_content(self, use_symlinks: bool = False):
        """Main organization function"""
        print("🔄 Starting content organization...")
        
        results = self.load_analysis_results()
        
        # Group items by language and filter for valid items
        organized_count = 0
        skipped_count = 0
        error_count = 0
        
        for item in results:
            # Skip items with invalid languages or very small files
            if item['language'] not in ['en', 'hi', 'both'] or item['size_bytes'] < 1024:
                skipped_count += 1
                continue
                
            source_file = Path(item['source_path']) / item['relative_path']
            target_path = self.get_target_path(item)
            
            if target_path is None:  # Bilingual content
                self.handle_bilingual_content(item, source_file, target_path)
                organized_count += 1
                continue
                
            # Copy or symlink content
            success = False
            if use_symlinks:
                success = self.create_symlink(source_file, target_path)
                operation = 'symlink'
            else:
                success = self.copy_content(source_file, target_path)
                operation = 'copy'
            
            if success:
                self.add_to_org_map(item, target_path, operation)
                organized_count += 1
            else:
                error_count += 1
        
        print(f"\n📊 Organization Summary:")
        print(f"  ✓ Organized: {organized_count} items")
        print(f"  ⏭️  Skipped: {skipped_count} items")
        print(f"  ✗ Errors: {error_count} items")
        
        return organized_count, skipped_count, error_count
    
    def create_organization_map_csv(self):
        """Create the required organization map CSV file"""
        csv_file = '/workspace/bilingual-org/organization_map.csv'
        
        if not self.org_map_data:
            print("⚠️  No data for organization map")
            return
            
        fieldnames = [
            'original_path', 'filename', 'language', 'category', 'source',
            'target_path', 'operation', 'file_type', 'size_bytes',
            'confidence', 'detection_method'
        ]
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.org_map_data)
        
        print(f"📋 Organization map created: {csv_file}")
        return csv_file
    
    def update_metadata_files(self):
        """Create/update metadata files with language codes"""
        metadata_dir = Path(self.target_base) / 'metadata'
        metadata_dir.mkdir(exist_ok=True)
        
        # Create language inventory
        inventory = {
            'generated_at': '2025-10-31T02:46:41Z',
            'total_organized_items': len(self.org_map_data),
            'languages': {
                'en': [item for item in self.org_map_data if item['language'] == 'en'],
                'hi': [item for item in self.org_map_data if item['language'] == 'hi'],
                'both': [item for item in self.org_map_data if item['language'] == 'both']
            },
            'categories': {}
        }
        
        # Group by categories
        for item in self.org_map_data:
            category = item['category']
            if category not in inventory['categories']:
                inventory['categories'][category] = []
            inventory['categories'][category].append(item)
        
        # Save inventory
        inventory_file = metadata_dir / 'language_inventory.json'
        with open(inventory_file, 'w', encoding='utf-8') as f:
            json.dump(inventory, f, indent=2, ensure_ascii=False)
        
        # Create summary README
        readme_content = f"""# RRB-NTPC Bilingual Content Organization

## Overview
This directory contains RRB-NTPC study materials organized by language availability.

## Structure
```
/content/rrb-ntpc/language/
├── en/
│   ├── previous-papers/     # English previous papers
│   ├── study-materials/     # English study materials
│   ├── practice-sets/       # English practice sets
│   └── current-affairs/     # English current affairs
└── hi/
    ├── previous-papers/     # Hindi previous papers
    ├── study-materials/     # Hindi study materials
    ├── practice-sets/       # Hindi practice sets
    └── current-affairs/     # Hindi current affairs
```

## Organization Statistics
- **Total organized items**: {len(self.org_map_data)}
- **English content**: {len([item for item in self.org_map_data if item['language'] == 'en'])}
- **Hindi content**: {len([item for item in self.org_map_data if item['language'] == 'hi'])}
- **Bilingual content**: {len([item for item in self.org_map_data if item['language'] == 'both'])}

## Language Detection
Content has been analyzed for language availability using multiple methods:
- Directory structure patterns
- Filename patterns
- Content analysis
- Metadata examination
- Source-based inference

## Files
- `organization_map.csv`: Complete mapping of original to organized files
- `language_inventory.json`: Structured inventory of all organized content
- `content_analysis_results.json`: Detailed analysis results
- `analysis_statistics.json`: Summary statistics

Generated: 2025-10-31T02:46:41Z
"""
        
        readme_file = metadata_dir / 'README.md'
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"📝 Metadata files updated in: {metadata_dir}")
        
        return inventory_file, readme_file
    
    def save_organization_log(self):
        """Save the organization log"""
        log_file = '/workspace/bilingual-org/organization_log.txt'
        
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("RRB-NTPC Bilingual Organization Log\\n")
            f.write("=" * 50 + "\\n\\n")
            for entry in self.organization_log:
                f.write(entry + "\\n")
        
        print(f"📜 Organization log saved: {log_file}")

def main():
    organizer = BilingualContentOrganizer()
    
    # Run organization (using copy instead of symlinks for better compatibility)
    organized, skipped, errors = organizer.organize_content(use_symlinks=False)
    
    # Create organization map CSV
    organizer.create_organization_map_csv()
    
    # Update metadata files
    organizer.update_metadata_files()
    
    # Save organization log
    organizer.save_organization_log()
    
    print(f"\\n✅ Organization complete!")
    print(f"   Organized: {organized} items")
    print(f"   Skipped: {skipped} items") 
    print(f"   Errors: {errors} items")
    print(f"\\n📁 Output directory: {organizer.target_base}")
    
    return True

if __name__ == "__main__":
    main()
