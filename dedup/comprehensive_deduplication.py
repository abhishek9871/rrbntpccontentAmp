#!/usr/bin/env python3
"""
Comprehensive Deduplication System for Educational Content
Implements SHA-256 checksum-based deduplication with source priority rules
"""

import os
import hashlib
import csv
import json
import logging
import difflib
import re
import mimetypes
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple, Optional

class ContentDeduplicator:
    def __init__(self):
        self.setup_logging()
        self.setup_directories()
        self.initialize_data_structures()
        self.define_source_priorities()
        
    def setup_logging(self):
        """Setup comprehensive logging system"""
        log_dir = Path("/workspace/dedup/logs")
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / 'de-dup.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("=== DEDUPLICATION SYSTEM INITIALIZED ===")
        
    def setup_directories(self):
        """Setup and verify directory structure"""
        self.content_directories = [
            "/workspace/content/rrb-ntpc",
            "/workspace/diksha-math",
            "/workspace/diksha-reasoning", 
            "/workspace/diksha-science",
            "/workspace/diksha-ga",
            "/workspace/wikimedia-math",
            "/workspace/wikimedia-reasoning"
        ]
        
        self.checksums_dir = Path("/workspace/dedup/checksums")
        self.checksums_dir.mkdir(exist_ok=True)
        
        self.logger.info(f"Content directories to process: {len(self.content_directories)}")
        
    def initialize_data_structures(self):
        """Initialize data structures for deduplication"""
        self.file_data = []
        self.checksum_map = defaultdict(list)
        self.filename_similarity_map = defaultdict(list)
        self.source_stats = defaultdict(int)
        self.dedup_stats = {
            'total_files': 0,
            'exact_duplicates': 0,
            'near_duplicates': 0,
            'kept_files': 0,
            'removed_files': 0,
            'sources': defaultdict(int)
        }
        
    def define_source_priorities(self):
        """Define source priority hierarchy"""
        self.source_priorities = {
            # Level 1: Official RRB Sources (Highest Priority)
            'rrb': {
                'keywords': ['rrb', 'railway', 'cen-05', 'ntpc', 'railway_board'],
                'priority_score': 100,
                'priority_level': 'Official RRB'
            },
            
            # Level 2: Government OER Sources (Medium-High Priority)
            'gov_oer': {
                'keywords': ['diksha', 'oer', 'ncert', 'gov', 'government', ' ministry', ' ncert'],
                'priority_score': 80,
                'priority_level': 'Government OER'
            },
            
            # Level 3: Credible Educational Portals (Lower Priority)
            'credible_portals': {
                'keywords': ['adda247', 'practicemock', 'testbook', 'meritnotes', 'yct', 
                           'cracku', 'freshersnow', 'instamojo', 'jagranjosh', 'oliveboard',
                           'ssb', 'quiz', 'practice', 'study', 'guide'],
                'priority_score': 60,
                'priority_level': 'Credible Portal'
            },
            
            # Level 4: Wikimedia/Open Source (Lowest Priority)
            'wikimedia': {
                'keywords': ['wikimedia', 'wikipedia', 'wikibooks', 'wikimedia'],
                'priority_score': 40,
                'priority_level': 'Open Source'
            }
        }
        
        self.logger.info(f"Source priority hierarchy defined with {len(self.source_priorities)} levels")
        
    def classify_source_priority(self, file_path: str, directory: str) -> Dict:
        """Classify source priority based on directory and filename"""
        path_lower = file_path.lower()
        dir_lower = directory.lower()
        
        for source_type, config in self.source_priorities.items():
            for keyword in config['keywords']:
                if keyword in path_lower or keyword in dir_lower:
                    return {
                        'source_type': source_type,
                        'priority_score': config['priority_score'],
                        'priority_level': config['priority_level']
                    }
                    
        # Default classification for unclassified sources
        return {
            'source_type': 'unclassified',
            'priority_score': 50,
            'priority_level': 'Unclassified'
        }
        
    def get_file_type(self, file_path: str) -> str:
        """Determine file type from extension and mime type"""
        mime_type, _ = mimetypes.guess_type(file_path)
        
        if mime_type:
            if mime_type.startswith('image/'):
                return 'image'
            elif mime_type == 'application/pdf':
                return 'pdf'
            elif mime_type.startswith('text/'):
                return 'text'
            elif mime_type.startswith('application/json'):
                return 'json'
                
        # Fallback to extension
        ext = Path(file_path).suffix.lower()
        if ext in ['.pdf']:
            return 'pdf'
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']:
            return 'image'
        elif ext in ['.txt', '.md']:
            return 'text'
        elif ext in ['.json', '.xml']:
            return 'data'
        else:
            return 'other'
            
    def generate_sha256(self, file_path: str) -> str:
        """Generate SHA-256 checksum for a file"""
        try:
            with open(file_path, 'rb') as f:
                hash_sha256 = hashlib.sha256()
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
                return hash_sha256.hexdigest()
        except Exception as e:
            self.logger.error(f"Error generating SHA256 for {file_path}: {e}")
            return ""
            
    def extract_text_content(self, file_path: str) -> str:
        """Extract text content for similarity analysis"""
        try:
            file_type = self.get_file_type(file_path)
            
            if file_type == 'text':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()
            elif file_type == 'json':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    data = json.load(f)
                    return str(data)
            else:
                # For now, return filename only for non-text files
                return file_path
                
        except Exception as e:
            self.logger.debug(f"Could not extract text from {file_path}: {e}")
            return ""
            
    def normalize_filename(self, filename: str) -> str:
        """Normalize filename for pattern matching"""
        # Remove file extensions
        name = Path(filename).stem
        
        # Convert to lowercase and replace special characters
        name = re.sub(r'[_\-]+', ' ', name.lower())
        name = re.sub(r'[^\w\s]', '', name)
        
        # Remove common stop words and numbers
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        words = [word for word in name.split() if word not in stop_words and not word.isdigit()]
        
        return ' '.join(words)
        
    def calculate_similarity(self, content1: str, content2: str, name1: str, name2: str) -> float:
        """Calculate content and filename similarity"""
        # Content similarity (if available)
        content_sim = 0.0
        if content1 and content2 and content1 != content1:  # Check if not same content
            content_sim = difflib.SequenceMatcher(None, content1, content2).ratio()
            
        # Filename similarity
        norm_name1 = self.normalize_filename(name1)
        norm_name2 = self.normalize_filename(name2)
        name_sim = difflib.SequenceMatcher(None, norm_name1, norm_name2).ratio()
        
        # Combined similarity (weighted average)
        combined_sim = (content_sim * 0.3 + name_sim * 0.7) if content_sim > 0 else name_sim
        
        return combined_sim
        
    def scan_all_directories(self):
        """Scan all content directories for files"""
        self.logger.info("=== STARTING DIRECTORY SCAN ===")
        
        for directory in self.content_directories:
            if not os.path.exists(directory):
                self.logger.warning(f"Directory not found: {directory}")
                continue
                
            self.logger.info(f"Scanning directory: {directory}")
            
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # Skip very small files (less than 100 bytes - likely metadata)
                    try:
                        file_size = os.path.getsize(file_path)
                        if file_size < 100:
                            continue
                    except OSError:
                        continue
                        
                    # Generate SHA-256 checksum
                    checksum = self.generate_sha256(file_path)
                    if not checksum:
                        continue
                        
                    # Classify source
                    source_info = self.classify_source_priority(file_path, directory)
                    
                    # Get file type
                    file_type = self.get_file_type(file_path)
                    
                    # Extract content for similarity analysis
                    content = self.extract_text_content(file_path)
                    
                    file_info = {
                        'file_path': file_path,
                        'checksum': checksum,
                        'file_size': file_size,
                        'directory': directory,
                        'source_info': source_info,
                        'file_type': file_type,
                        'content': content,
                        'filename': file
                    }
                    
                    self.file_data.append(file_info)
                    self.checksum_map[checksum].append(file_info)
                    self.dedup_stats['total_files'] += 1
                    self.dedup_stats['sources'][source_info['source_type']] += 1
                    
        self.logger.info(f"=== DIRECTORY SCAN COMPLETE ===")
        self.logger.info(f"Total files processed: {self.dedup_stats['total_files']}")
        self.logger.info(f"Source distribution: {dict(self.dedup_stats['sources'])}")
        
    def detect_exact_duplicates(self):
        """Detect exact duplicates based on SHA-256"""
        self.logger.info("=== DETECTING EXACT DUPLICATES ===")
        
        for checksum, files in self.checksum_map.items():
            if len(files) > 1:
                self.dedup_stats['exact_duplicates'] += len(files) - 1
                
                # Sort by priority (highest first)
                files.sort(key=lambda x: x['source_info']['priority_score'], reverse=True)
                
                # Keep highest priority, mark others for removal
                for i in range(1, len(files)):
                    files[i]['dedup_decision'] = 'drop'
                    files[i]['dedup_rationale'] = f"Exact duplicate of {files[0]['file_path']} (same SHA-256, lower priority)"
                    
                files[0]['dedup_decision'] = 'keep'
                files[0]['dedup_rationale'] = 'Kept as highest priority version'
                
                self.logger.info(f"Exact duplicate group: {len(files)} files with SHA-256 {checksum[:16]}...")
                for i, file_info in enumerate(files):
                    decision = "KEEP" if i == 0 else "DROP"
                    self.logger.info(f"  {decision}: {file_info['file_path']} ({file_info['source_info']['priority_level']})")
                    
    def detect_near_duplicates(self):
        """Detect near duplicates based on content similarity and naming patterns"""
        self.logger.info("=== DETECTING NEAR DUPLICATES ===")
        
        # Group files by file type and approximate size range for efficiency
        grouped_files = defaultdict(list)
        
        for file_info in self.file_data:
            if file_info.get('dedup_decision') == 'drop':
                continue
                
            # Group by file type
            grouped_files[file_info['file_type']].append(file_info)
            
        similarity_threshold = 0.85
        
        for file_type, files in grouped_files.items():
            if len(files) < 2:
                continue
                
            self.logger.info(f"Analyzing near duplicates for type: {file_type}")
            
            # Compare all pairs within file type
            for i in range(len(files)):
                if files[i].get('dedup_decision') == 'drop':
                    continue
                    
                for j in range(i + 1, len(files)):
                    if files[j].get('dedup_decision') == 'drop':
                        continue
                        
                    sim = self.calculate_similarity(
                        files[i]['content'], files[j]['content'],
                        files[i]['filename'], files[j]['filename']
                    )
                    
                    if sim >= similarity_threshold:
                        self.dedup_stats['near_duplicates'] += 1
                        
                        # Compare priorities to decide which to keep
                        file1_priority = files[i]['source_info']['priority_score']
                        file2_priority = files[j]['source_info']['priority_score']
                        
                        if file1_priority > file2_priority:
                            keep_file, drop_file = files[i], files[j]
                        elif file2_priority > file1_priority:
                            keep_file, drop_file = files[j], files[i]
                        else:
                            # Same priority, keep larger file
                            if files[i]['file_size'] >= files[j]['file_size']:
                                keep_file, drop_file = files[i], files[j]
                            else:
                                keep_file, drop_file = files[j], files[i]
                                
                        drop_file['dedup_decision'] = 'drop'
                        drop_file['dedup_rationale'] = f"Near duplicate of {keep_file['file_path']} (similarity: {sim:.2f}, lower priority)"
                        keep_file['dedup_decision'] = keep_file.get('dedup_decision', 'keep')
                        
                        self.logger.info(f"Near duplicate detected (similarity: {sim:.2f})")
                        self.logger.info(f"  KEEP: {keep_file['file_path']} ({keep_file['source_info']['priority_level']})")
                        self.logger.info(f"  DROP: {drop_file['file_path']} ({drop_file['source_info']['priority_level']})")
                        
    def apply_deduplication_rules(self):
        """Apply deduplication rules and make final decisions"""
        self.logger.info("=== APPLYING DEDUPLICATION RULES ===")
        
        # Mark files without explicit decisions
        for file_info in self.file_data:
            if 'dedup_decision' not in file_info:
                file_info['dedup_decision'] = 'keep'
                file_info['dedup_rationale'] = 'Unique file - no duplicates found'
                
        # Count final decisions
        keep_count = sum(1 for f in self.file_data if f['dedup_decision'] == 'keep')
        drop_count = sum(1 for f in self.file_data if f['dedup_decision'] == 'drop')
        
        self.dedup_stats['kept_files'] = keep_count
        self.dedup_stats['removed_files'] = drop_count
        
        self.logger.info(f"Deduplication complete:")
        self.logger.info(f"  Files kept: {keep_count}")
        self.logger.info(f"  Files removed: {drop_count}")
        self.logger.info(f"  Duplicates removed: {self.dedup_stats['exact_duplicates'] + self.dedup_stats['near_duplicates']}")
        
    def generate_outputs(self):
        """Generate required output files"""
        self.logger.info("=== GENERATING OUTPUT FILES ===")
        
        # Generate CSV output
        csv_path = self.checksums_dir / "sha256sums.csv"
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'file_path', 'sha256_checksum', 'file_size_bytes', 
                'file_size_mb', 'source_priority', 'priority_score',
                'dedup_decision', 'dedup_rationale', 'file_type'
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for file_info in self.file_data:
                row = {
                    'file_path': file_info['file_path'],
                    'sha256_checksum': file_info['checksum'],
                    'file_size_bytes': file_info['file_size'],
                    'file_size_mb': round(file_info['file_size'] / (1024*1024), 2),
                    'source_priority': file_info['source_info']['priority_level'],
                    'priority_score': file_info['source_info']['priority_score'],
                    'dedup_decision': file_info.get('dedup_decision', 'keep'),
                    'dedup_rationale': file_info.get('dedup_rationale', 'Unique file'),
                    'file_type': file_info['file_type']
                }
                writer.writerow(row)
                
        self.logger.info(f"Generated CSV output: {csv_path}")
        
        # Generate summary report
        self.generate_summary_report()
        
    def generate_summary_report(self):
        """Generate deduplication summary report"""
        report_path = self.checksums_dir / "deduplication_summary.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("COMPREHENSIVE DEDUPLICATION SUMMARY REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("STATISTICS:\n")
            f.write(f"Total files processed: {self.dedup_stats['total_files']}\n")
            f.write(f"Files kept: {self.dedup_stats['kept_files']}\n")
            f.write(f"Files removed: {self.dedup_stats['removed_files']}\n")
            f.write(f"Exact duplicates removed: {self.dedup_stats['exact_duplicates']}\n")
            f.write(f"Near duplicates removed: {self.dedup_stats['near_duplicates']}\n")
            f.write(f"Total duplicates removed: {self.dedup_stats['exact_duplicates'] + self.dedup_stats['near_duplicates']}\n\n")
            
            f.write("SOURCE PRIORITY DISTRIBUTION:\n")
            for source_type, count in self.dedup_stats['sources'].items():
                priority_name = self.source_priorities.get(source_type, {}).get('priority_level', source_type)
                f.write(f"  {priority_name}: {count} files\n")
                
            f.write(f"\nDEDUPLICATION RATE: {(self.dedup_stats['removed_files'] / self.dedup_stats['total_files'] * 100):.1f}%\n")
            
        self.logger.info(f"Generated summary report: {report_path}")
        
    def run_deduplication(self):
        """Execute the complete deduplication workflow"""
        start_time = datetime.now()
        self.logger.info(f"Starting deduplication at {start_time}")
        
        try:
            # Phase 1: Scan directories
            self.scan_all_directories()
            
            # Phase 2: Detect exact duplicates
            self.detect_exact_duplicates()
            
            # Phase 3: Detect near duplicates  
            self.detect_near_duplicates()
            
            # Phase 4: Apply rules and finalize decisions
            self.apply_deduplication_rules()
            
            # Phase 5: Generate outputs
            self.generate_outputs()
            
            end_time = datetime.now()
            duration = end_time - start_time
            
            self.logger.info(f"=== DEDUPLICATION COMPLETE ===")
            self.logger.info(f"Duration: {duration}")
            self.logger.info(f"Results: {self.dedup_stats['kept_files']} kept, {self.dedup_stats['removed_files']} removed")
            
        except Exception as e:
            self.logger.error(f"Error during deduplication: {e}")
            raise

def main():
    """Main execution function"""
    deduplicator = ContentDeduplicator()
    deduplicator.run_deduplication()

if __name__ == "__main__":
    main()