#!/usr/bin/env python3
"""
Comprehensive Content Audit Analyzer
Analyzes all content across workspace directories for audit purposes
"""

import os
import json
import csv
import hashlib
from pathlib import Path
from collections import defaultdict
import mimetypes
from datetime import datetime

class ContentAuditor:
    def __init__(self, workspace_path="/workspace"):
        self.workspace_path = Path(workspace_path)
        self.content_stats = {
            'total_files': 0,
            'total_size_bytes': 0,
            'files_by_format': defaultdict(int),
            'files_by_size': defaultdict(int),
            'files_by_location': defaultdict(int),
            'content_categories': defaultdict(list),
            'language_distribution': defaultdict(int),
            'source_credibility': defaultdict(list),
            'file_details': []
        }
        
        # Content area mappings
        self.content_areas = {
            'rrb-ntpc': 'Railway Recruitment Board - Non-Technical Popular Categories',
            'diksha-ga': 'DIKSHA General Awareness',
            'diksha-math': 'DIKSHA Mathematics',
            'diksha-reasoning': 'DIKSHA Reasoning',
            'diksha-science': 'DIKSHA Science',
            'current-affairs': 'Current Affairs',
            'downloads': 'Downloaded Materials',
            'extract': 'Extracted Content',
            'browser/extracted_content': 'Browser Extracted Content'
        }
        
        # Subject mappings
        self.subject_mappings = {
            'current-affairs': ['Current Affairs', 'News', 'Events'],
            'language': ['Language Learning', 'English', 'Hindi'],
            'practice-sets': ['Practice Materials', 'Tests', 'Exercises'],
            'previous-papers': ['Previous Papers', 'Exam Materials', 'Sample Papers'],
            'study-materials': ['Study Materials', 'Educational Resources'],
            'economy': ['Economics', 'Financial Studies'],
            'geography': ['Geography', 'Earth Sciences'],
            'indian-history': ['History', 'Indian History'],
            'polity': ['Political Science', 'Constitution', 'Governance'],
            'science-technology': ['Science', 'Technology', 'NCERT'],
            'static-gk': ['General Knowledge', 'Static GK'],
            'logical_reasoning': ['Reasoning', 'Logical Thinking'],
            'mental_ability': ['Mental Ability', 'Aptitude'],
            'non_verbal_reasoning': ['Non-Verbal Reasoning'],
            'verbal_reasoning': ['Verbal Reasoning']
        }

    def get_file_hash(self, file_path):
        """Generate SHA256 hash for file"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except:
            return "N/A"

    def analyze_file(self, file_path):
        """Analyze individual file"""
        try:
            stat = file_path.stat()
            file_size = stat.st_size
            file_ext = file_path.suffix.lower()
            file_name = file_path.name
            relative_path = file_path.relative_to(self.workspace_path)
            
            # Detect language from filename or path
            language = self.detect_language(file_name, relative_path)
            
            # Detect subject category
            subject = self.detect_subject(relative_path)
            
            # Detect content type
            content_type = self.detect_content_type(file_ext, file_name)
            
            # Determine source credibility
            credibility = self.assess_credibility(relative_path, file_name)
            
            file_info = {
                'file_path': str(relative_path),
                'absolute_path': str(file_path),
                'size_bytes': file_size,
                'size_human': self.format_size(file_size),
                'extension': file_ext,
                'content_type': content_type,
                'language': language,
                'subject': subject,
                'credibility': credibility,
                'hash': self.get_file_hash(file_path),
                'modified_time': datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
            
            return file_info
            
        except Exception as e:
            return {
                'file_path': str(file_path.relative_to(self.workspace_path)),
                'error': str(e),
                'size_bytes': 0,
                'size_human': '0 B'
            }

    def detect_language(self, file_name, file_path):
        """Detect language from filename or path"""
        path_str = str(file_path).lower()
        
        if '/hi/' in path_str or '_hi_' in file_name.lower():
            return 'Hindi'
        elif '/en/' in path_str or '_en_' in file_name.lower():
            return 'English'
        elif 'hindi' in path_str or 'हिंदी' in path_str:
            return 'Hindi'
        elif 'english' in path_str:
            return 'English'
        else:
            # Default inference based on content
            if any(keyword in path_str for keyword in ['ncert', 'class', 'chapters']):
                return 'English'  # Most NCERT content is in English
            return 'Mixed/Unknown'

    def detect_subject(self, file_path):
        """Detect subject category"""
        path_str = str(file_path).lower()
        
        # Direct subject mapping
        for key, subjects in self.subject_mappings.items():
            if key in path_str:
                return subjects[0]
        
        # Additional mapping
        if 'history' in path_str:
            return 'History'
        elif 'geography' in path_str:
            return 'Geography'
        elif 'economy' in path_str or 'economics' in path_str:
            return 'Economics'
        elif 'science' in path_str:
            return 'Science'
        elif 'math' in path_str:
            return 'Mathematics'
        elif 'reasoning' in path_str:
            return 'Reasoning'
        elif 'gk' in path_str or 'general' in path_str:
            return 'General Knowledge'
        elif 'polity' in path_str or 'constitution' in path_str:
            return 'Political Science'
        elif 'current' in path_str and 'affair' in path_str:
            return 'Current Affairs'
        
        return 'Other/Uncategorized'

    def detect_content_type(self, file_ext, file_name):
        """Detect content type based on extension and name"""
        if file_ext == '.pdf':
            return 'PDF Document'
        elif file_ext == '.json':
            return 'JSON Data'
        elif file_ext == '.md':
            return 'Markdown Document'
        elif file_ext == '.csv':
            return 'CSV Data'
        elif file_ext == '.txt':
            return 'Text Document'
        elif file_ext == '.zip':
            return 'Archive'
        elif file_ext == '.html':
            return 'HTML Page'
        elif file_ext in ['.png', '.jpg', '.jpeg', '.gif']:
            return 'Image'
        elif file_ext in ['.py', '.sh', '.js']:
            return 'Code'
        else:
            return 'Other'

    def assess_credibility(self, file_path, file_name):
        """Assess source credibility"""
        path_str = str(file_path).lower()
        
        # High credibility sources
        if any(source in path_str for source in [
            'ncert', 'govt', 'government', 'official', 
            'diksha', 'nroer', 'drishti', 'wikipedia'
        ]):
            return 'High'
        
        # Medium credibility sources
        elif any(source in path_str for source in [
            'ibps', 'ssc', 'mock', 'practice', 'guide'
        ]):
            return 'Medium'
        
        # Lower credibility or unclear
        else:
            return 'Unknown'

    def format_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"

    def scan_directory(self, directory_path):
        """Recursively scan directory for files"""
        files_found = []
        
        try:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = Path(root) / file
                    if file_path.is_file():
                        file_info = self.analyze_file(file_path)
                        files_found.append(file_info)
        except Exception as e:
            print(f"Error scanning {directory_path}: {e}")
        
        return files_found

    def run_audit(self):
        """Run complete audit"""
        print("Starting comprehensive content audit...")
        
        # Define content directories to scan
        content_directories = [
            'content/rrb-ntpc',
            'diksha-ga',
            'diksha-math', 
            'diksha-reasoning',
            'diksha-science',
            'current-affairs',
            'downloads',
            'extract',
            'browser/extracted_content',
            'docs',
            'licensing',
            'logs'
        ]
        
        all_files = []
        
        # Scan each content directory
        for content_dir in content_directories:
            full_path = self.workspace_path / content_dir
            if full_path.exists():
                print(f"Scanning {content_dir}...")
                files = self.scan_directory(full_path)
                all_files.extend(files)
                print(f"Found {len(files)} files in {content_dir}")
            else:
                print(f"Directory {content_dir} not found")
        
        # Process collected files
        self.process_files(all_files)
        
        return self.content_stats

    def process_files(self, files):
        """Process and categorize all files"""
        self.content_stats['total_files'] = len(files)
        
        for file_info in files:
            if 'error' in file_info:
                continue
                
            self.content_stats['file_details'].append(file_info)
            
            # Update counters
            self.content_stats['total_size_bytes'] += file_info['size_bytes']
            
            # By format
            self.content_stats['files_by_format'][file_info['content_type']] += 1
            
            # By size category
            if file_info['size_bytes'] < 1024:
                size_cat = 'Small (<1KB)'
            elif file_info['size_bytes'] < 1024 * 1024:
                size_cat = 'Medium (1KB-1MB)'
            elif file_info['size_bytes'] < 100 * 1024 * 1024:
                size_cat = 'Large (1MB-100MB)'
            else:
                size_cat = 'Very Large (>100MB)'
            self.content_stats['files_by_size'][size_cat] += 1
            
            # By location
            location = self.extract_location_category(file_info['file_path'])
            self.content_stats['files_by_location'][location] += 1
            
            # Language distribution
            self.content_stats['language_distribution'][file_info['language']] += 1
            
            # Source credibility
            self.content_stats['source_credibility'][file_info['credibility']].append(file_info['subject'])
            
            # Content categories
            category_key = self.extract_content_category(file_info['file_path'])
            self.content_stats['content_categories'][category_key].append(file_info)

    def extract_location_category(self, file_path):
        """Extract location category from file path"""
        path_parts = file_path.split('/')
        if len(path_parts) >= 2:
            return path_parts[0]
        return 'Other'

    def extract_content_category(self, file_path):
        """Extract content category from file path"""
        path_parts = file_path.split('/')
        if len(path_parts) >= 3:
            return path_parts[2]
        elif len(path_parts) >= 2:
            return path_parts[1]
        return 'Other'

if __name__ == "__main__":
    auditor = ContentAuditor()
    stats = auditor.run_audit()
    
    # Save results
    with open('/workspace/audit/content_audit_stats.json', 'w') as f:
        json.dump(stats, f, indent=2, default=str)
    
    print(f"\nAudit Complete!")
    print(f"Total files found: {stats['total_files']}")
    print(f"Total size: {auditor.format_size(stats['total_size_bytes'])}")