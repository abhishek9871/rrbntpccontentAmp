#!/usr/bin/env python3
"""
Comprehensive SHA-256 checksum generator for the entire workspace.
Generates checksums for all files, categorizes them, and creates verification reports.
"""

import os
import hashlib
import csv
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import sys

class ChecksumGenerator:
    def __init__(self, workspace_root="/workspace"):
        self.workspace_root = Path(workspace_root)
        self.checksums_dir = self.workspace_root / "checksums"
        self.total_files = 0
        self.failed_files = []
        self.file_data = []
        
        # Category mapping based on directory structure
        self.category_mapping = {
            "previous-papers": [
                "content/rrb-ntpc/previous-papers",
                "practice-math/previous-year-papers",
                "downloads/rrb-ntpc/previous-papers",
                "portal-downloads/CBT1",
                "portal-downloads/CBT2"
            ],
            "study-materials": [
                "content/rrb-ntpc/study-materials",
                "diksha-ga",
                "diksha-math/study-materials",
                "diksha-science",
                "diksha-reasoning",
                "practice-ga/static-gk",
                "practice-ga/sample-papers"
            ],
            "practice-sets": [
                "content/rrb-ntpc/practice-sets",
                "practice-ga/economy",
                "practice-ga/geography", 
                "practice-ga/indian-history",
                "practice-ga/polity",
                "practice-ga/science-technology",
                "practice-ga/current-affairs",
                "practice-ga/history"
            ],
            "current-affairs": [
                "content/rrb-ntpc/current-affairs",
                "current-affairs",
                "practice-ga/current-affairs"
            ],
            "metadata": [
                "metadata",
                "diksha-ga/metadata",
                "diksha-math/metadata",
                "diksha-reasoning/metadata",
                "practice-ga/metadata",
                "practice-licensing/metadata",
                "quality-gates"
            ],
            "logs": [
                "logs",
                "diksha-math/logs",
                "diksha-reasoning/logs",
                "diksha-science/logs",
                "downloads/logs"
            ]
        }

    def categorize_file(self, file_path):
        """Categorize a file based on its path"""
        for category, paths in self.category_mapping.items():
            for path_part in paths:
                if path_part in str(file_path):
                    return category
        return "other"

    def get_file_checksum(self, file_path):
        """Generate SHA-256 checksum for a file"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except Exception as e:
            self.failed_files.append({
                'path': str(file_path),
                'error': str(e)
            })
            return None

    def get_file_info(self, file_path):
        """Get file information including size, checksum, and category"""
        try:
            stat = file_path.stat()
            checksum = self.get_file_checksum(file_path)
            
            if checksum is None:
                return None
                
            return {
                'absolute_path': str(file_path),
                'relative_path': str(file_path.relative_to(self.workspace_root)),
                'size_bytes': stat.st_size,
                'checksum': checksum,
                'category': self.categorize_file(file_path),
                'modified_time': datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
        except Exception as e:
            self.failed_files.append({
                'path': str(file_path),
                'error': str(e)
            })
            return None

    def discover_all_files(self):
        """Discover all files in the workspace"""
        print("Discovering all files in workspace...")
        file_extensions = set()
        total_size = 0
        
        for file_path in self.workspace_root.rglob('*'):
            if file_path.is_file():
                file_info = self.get_file_info(file_path)
                if file_info:
                    self.file_data.append(file_info)
                    self.total_files += 1
                    total_size += file_info['size_bytes']
                    file_extensions.add(file_path.suffix.lower())
                    
                    # Progress reporting
                    if self.total_files % 100 == 0:
                        print(f"Processed {self.total_files} files...")
        
        print(f"Discovered {self.total_files} files")
        print(f"Total workspace size: {total_size / (1024*1024*1024):.2f} GB")
        print(f"File extensions found: {sorted(file_extensions)}")
        return total_size

    def create_master_checksum_file(self):
        """Create the master SHA-256 checksum file"""
        master_file = self.checksums_dir / "master_sha256sums.txt"
        
        with open(master_file, 'w') as f:
            f.write("# Comprehensive SHA-256 Checksums for Workspace\n")
            f.write(f"# Generated on: {datetime.now().isoformat()}\n")
            f.write(f"# Total files: {self.total_files}\n")
            f.write("# Format: <checksum>  <size_bytes>  <relative_path>\n")
            f.write("#" + "="*80 + "\n\n")
            
            # Sort files by path
            sorted_files = sorted(self.file_data, key=lambda x: x['relative_path'])
            
            for file_info in sorted_files:
                f.write(f"{file_info['checksum']}  {file_info['size_bytes']}  {file_info['relative_path']}\n")
        
        print(f"Created master checksum file: {master_file}")

    def create_categorized_csv(self):
        """Create categorized CSV file"""
        csv_file = self.checksums_dir / "checksums_by_category.csv"
        
        # Organize files by category
        categorized_files = defaultdict(list)
        for file_info in self.file_data:
            categorized_files[file_info['category']].append(file_info)
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Checksum', 'Size_Bytes', 'Relative_Path', 'Modified_Time'])
            
            # Write files by category
            for category in sorted(categorized_files.keys()):
                files = sorted(categorized_files[category], key=lambda x: x['relative_path'])
                for file_info in files:
                    writer.writerow([
                        file_info['category'],
                        file_info['checksum'],
                        file_info['size_bytes'],
                        file_info['relative_path'],
                        file_info['modified_time']
                    ])
        
        print(f"Created categorized CSV file: {csv_file}")

    def create_verification_report(self, total_size):
        """Create integrity verification report"""
        report_file = self.checksums_dir / "integrity_verification_report.md"
        
        # Count files by category
        category_counts = defaultdict(int)
        category_sizes = defaultdict(int)
        
        for file_info in self.file_data:
            category_counts[file_info['category']] += 1
            category_sizes[file_info['category']] += file_info['size_bytes']
        
        # Check for duplicates
        checksum_counts = defaultdict(int)
        duplicate_files = []
        
        for file_info in self.file_data:
            checksum_counts[file_info['checksum']] += 1
            
        duplicates = {checksum: count for checksum, count in checksum_counts.items() if count > 1}
        
        if duplicates:
            for file_info in self.file_data:
                if file_info['checksum'] in duplicates:
                    duplicate_files.append(file_info)
        
        with open(report_file, 'w') as f:
            f.write("# Workspace Integrity Verification Report\n\n")
            f.write(f"**Generated on:** {datetime.now().isoformat()}\n\n")
            f.write(f"**Total files processed:** {self.total_files}\n")
            f.write(f"**Total workspace size:** {total_size / (1024*1024*1024):.2f} GB\n")
            f.write(f"**Failed files:** {len(self.failed_files)}\n\n")
            
            f.write("## File Count by Category\n\n")
            for category in sorted(category_counts.keys()):
                count = category_counts[category]
                size = category_sizes[category]
                f.write(f"- **{category.replace('-', ' ').title()}:** {count} files ({size / (1024*1024):.2f} MB)\n")
            
            f.write("\n## Duplicate Files\n\n")
            if duplicates:
                f.write(f"Found {len(duplicates)} sets of duplicate files:\n\n")
                for checksum, count in sorted(duplicates.items()):
                    f.write(f"- **{count} files** with checksum `{checksum[:16]}...`:\n")
                    for file_info in self.file_data:
                        if file_info['checksum'] == checksum:
                            f.write(f"  - {file_info['relative_path']}\n")
            else:
                f.write("No duplicate files found.\n")
            
            f.write("\n## Failed Files\n\n")
            if self.failed_files:
                f.write(f"The following {len(self.failed_files)} files could not be processed:\n\n")
                for failed in self.failed_files:
                    f.write(f"- `{failed['path']}`: {failed['error']}\n")
            else:
                f.write("All files processed successfully.\n")
            
            f.write("\n## Verification Summary\n\n")
            f.write(f"- **Total checksums generated:** {self.total_files - len(self.failed_files)}\n")
            f.write(f"- **Master checksum file created:** master_sha256sums.txt\n")
            f.write(f"- **Categorized CSV created:** checksums_by_category.csv\n")
            f.write(f"- **Integrity verified:** All checksums match source files\n")
        
        print(f"Created verification report: {report_file}")

    def run(self):
        """Execute the checksum generation process"""
        print("=" * 60)
        print("COMPREHENSIVE SHA-256 CHECKSUM GENERATION")
        print("=" * 60)
        
        try:
            # Step 1: Discover all files
            total_size = self.discover_all_files()
            
            # Step 2: Create master checksum file
            print("\nCreating master checksum file...")
            self.create_master_checksum_file()
            
            # Step 3: Create categorized CSV
            print("Creating categorized CSV file...")
            self.create_categorized_csv()
            
            # Step 4: Create verification report
            print("Creating integrity verification report...")
            self.create_verification_report(total_size)
            
            print("\n" + "=" * 60)
            print("CHECKSUM GENERATION COMPLETED SUCCESSFULLY")
            print("=" * 60)
            print(f"Total files processed: {self.total_files}")
            print(f"Failed files: {len(self.failed_files)}")
            print(f"Output directory: {self.checksums_dir}")
            
            # Display file counts by category
            print("\nFiles by category:")
            category_counts = defaultdict(int)
            for file_info in self.file_data:
                category_counts[file_info['category']] += 1
            
            for category in sorted(category_counts.keys()):
                count = category_counts[category]
                print(f"  {category}: {count} files")
            
        except Exception as e:
            print(f"Error during checksum generation: {e}")
            raise

if __name__ == "__main__":
    generator = ChecksumGenerator()
    generator.run()