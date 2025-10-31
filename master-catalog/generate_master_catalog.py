#!/usr/bin/env python3
"""
Master Catalog Generator
Generates comprehensive catalog.csv and catalog.jsonl combining all content metadata
from RRB NTPC exam preparation materials including:
- DIKSHA content (GA, Math, Reasoning, Science)
- Bilingual organized content
- Practice sets
- Current affairs
- Portal downloads
- Wikimedia content
- Deduped content
"""

import json
import csv
import os
import hashlib
from pathlib import Path
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MasterCatalogGenerator:
    def __init__(self, workspace_dir="/workspace"):
        self.workspace = Path(workspace_dir)
        self.catalog_entries = []
        self.processed_files = set()
        
        # Initialize master catalog fields
        self.master_fields = [
            'title', 'year', 'stage', 'sections', 'topic_tags', 'language', 
            'source_url', 'source_domain', 'license', 'attribution_text',
            'expected_format', 'intended_path', 'checksum_sha256',
            'filesize_bytes', 'retrieved_at', 'verification_notes'
        ]
        
    def calculate_sha256(self, file_path):
        """Calculate SHA256 checksum of a file"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            logger.error(f"Error calculating SHA256 for {file_path}: {e}")
            return "error_calculating_checksum"
    
    def get_file_size(self, file_path):
        """Get file size in bytes"""
        try:
            return os.path.getsize(file_path)
        except Exception as e:
            logger.error(f"Error getting size for {file_path}: {e}")
            return 0
    
    def determine_format(self, filename):
        """Determine file format from extension"""
        ext = Path(filename).suffix.lower()
        format_map = {
            '.pdf': 'PDF',
            '.json': 'JSON',
            '.txt': 'Text',
            '.html': 'HTML',
            '.zip': 'Archive',
            '.jpg': 'Image',
            '.png': 'Image',
            '.gif': 'Image',
            '.svg': 'Image',
            '.md': 'Markdown',
            '.csv': 'CSV'
        }
        return format_map.get(ext, 'Other')
    
    def extract_domain(self, url):
        """Extract domain from URL"""
        if not url:
            return "local_file"
        try:
            from urllib.parse import urlparse
            return urlparse(url).netloc
        except:
            return "unknown_domain"
    
    def process_diksha_content(self):
        """Process DIKSHA content from various directories"""
        logger.info("Processing DIKSHA content...")
        
        # DIKSHA General Awareness
        diksha_ga_files = [
            (self.workspace / "diksha-ga", "diksha-ga"),
            (self.workspace / "diksha-math", "diksha-math"),
            (self.workspace / "diksha-reasoning", "diksha-reasoning"),
            (self.workspace / "diksha-science", "diksha-science")
        ]
        
        for dir_path, source_type in diksha_ga_files:
            if not dir_path.exists():
                continue
                
            for file_path in dir_path.rglob("*"):
                if file_path.is_file() and file_path.suffix in ['.pdf', '.json', '.zip', '.md', '.txt']:
                    entry = self.create_catalog_entry(file_path, "DIKSHA Platform")
                    
                    # Add DIKSHA-specific metadata
                    if "diksha-ga" in str(file_path):
                        entry['topic_tags'] = "general_awareness,history,geography,polity,economy,science"
                        entry['stage'] = "CBSE_VI-XII"
                    elif "diksha-math" in str(file_path):
                        entry['topic_tags'] = "mathematics,algebra,geometry,trigonometry,statistics"
                        entry['stage'] = "CBSE_VIII-X"
                    elif "diksha-reasoning" in str(file_path):
                        entry['topic_tags'] = "logical_reasoning,verbal_reasoning,non_verbal_reasoning"
                        entry['stage'] = "competitive_exam"
                    elif "diksha-science" in str(file_path):
                        entry['topic_tags'] = "general_science,physics,chemistry,biology"
                        entry['stage'] = "CBSE_IX-XII"
                    
                    entry['source_url'] = "https://diksha.gov.in/"
                    entry['source_domain'] = "diksha.gov.in"
                    entry['license'] = "CC BY 4.0"
                    entry['attribution_text'] = "DIKSHA Platform Team, NCERT, Ministry of Education, Government of India"
                    entry['verification_notes'] = "Official DIKSHA platform content"
                    
                    self.catalog_entries.append(entry)
    
    def process_bilingual_content(self):
        """Process bilingual organized content"""
        logger.info("Processing bilingual organized content...")
        
        bilingual_path = self.workspace / "bilingual-org"
        if not bilingual_path.exists():
            return
            
        for file_path in bilingual_path.rglob("*.pdf"):
            if file_path.is_file():
                entry = self.create_catalog_entry(file_path, "Bilingual Organization")
                
                # Extract language from path
                path_parts = file_path.parts
                if "language/en" in path_parts:
                    entry['language'] = "English"
                elif "language/hi" in path_parts:
                    entry['language'] = "Hindi"
                else:
                    entry['language'] = "Unknown"
                
                # Determine content type from path
                if "study-materials" in path_parts:
                    entry['sections'] = "study_materials"
                elif "practice-sets" in path_parts:
                    entry['sections'] = "practice_sets"
                elif "previous-papers" in path_parts:
                    entry['sections'] = "previous_papers"
                
                self.catalog_entries.append(entry)
    
    def process_practice_sets(self):
        """Process practice sets"""
        logger.info("Processing practice sets...")
        
        practice_dirs = [
            (self.workspace / "practice-math", "math_practice"),
            (self.workspace / "practice-reasoning", "reasoning_practice"),
            (self.workspace / "practice-ga", "ga_practice")
        ]
        
        for dir_path, content_type in practice_dirs:
            if not dir_path.exists():
                continue
                
            for file_path in dir_path.rglob("*"):
                if file_path.is_file() and file_path.suffix in ['.pdf', '.json', '.md', '.txt']:
                    entry = self.create_catalog_entry(file_path, "Practice Sets")
                    entry['sections'] = "practice_sets"
                    
                    # Add content type specific metadata
                    if "math" in str(file_path):
                        entry['topic_tags'] = "mathematics,practice_questions"
                    elif "reasoning" in str(file_path):
                        entry['topic_tags'] = "logical_reasoning,practice_questions"
                    elif "ga" in str(file_path):
                        entry['topic_tags'] = "general_awareness,practice_questions"
                    
                    self.catalog_entries.append(entry)
    
    def process_current_affairs(self):
        """Process current affairs content"""
        logger.info("Processing current affairs...")
        
        ca_path = self.workspace / "current-affairs"
        if not ca_path.exists():
            return
            
        for year_dir in ca_path.iterdir():
            if year_dir.is_dir() and year_dir.name.isdigit():
                for file_path in year_dir.rglob("*"):
                    if file_path.is_file():
                        entry = self.create_catalog_entry(file_path, "Current Affairs")
                        entry['year'] = year_dir.name
                        entry['sections'] = "current_affairs"
                        entry['topic_tags'] = "current_affairs,government_documents"
                        entry['verification_notes'] = f"Current affairs materials from {year_dir.name}"
                        
                        self.catalog_entries.append(entry)
    
    def process_portal_downloads(self):
        """Process portal downloads"""
        logger.info("Processing portal downloads...")
        
        portal_path = self.workspace / "portal-downloads"
        if not portal_path.exists():
            return
            
        for file_path in portal_path.rglob("*"):
            if file_path.is_file() and file_path.suffix in ['.pdf', '.json']:
                entry = self.create_catalog_entry(file_path, "RRB Portal")
                entry['sections'] = "official_documents"
                entry['topic_tags'] = "rrb_notifications,examination_materials"
                entry['verification_notes'] = "Official RRB portal content"
                
                # Extract domain from RRB portal URLs if available
                entry['source_domain'] = "rrb*.gov.in"
                
                self.catalog_entries.append(entry)
    
    def process_downloads(self):
        """Process general downloads"""
        logger.info("Processing general downloads...")
        
        downloads_path = self.workspace / "downloads"
        if not downloads_path.exists():
            return
            
        for file_path in downloads_path.rglob("*.pdf"):
            if file_path.is_file():
                entry = self.create_catalog_entry(file_path, "General Downloads")
                entry['sections'] = "study_materials"
                entry['verification_notes'] = "Downloaded study materials"
                
                self.catalog_entries.append(entry)
    
    def process_dedup_content(self):
        """Process deduplication checksums"""
        logger.info("Processing dedup content...")
        
        dedup_path = self.workspace / "dedup"
        checksums_file = dedup_path / "checksums" / "sha256sums.csv"
        
        if checksums_file.exists():
            with open(checksums_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Find corresponding entry in catalog and update checksum
                    file_path = row.get('file_path', '')
                    checksum = row.get('sha256_checksum', '')
                    
                    for entry in self.catalog_entries:
                        if entry.get('intended_path') == file_path:
                            entry['checksum_sha256'] = checksum
                            entry['verification_notes'] += f" | Deduplication: {row.get('dedup_decision', '')}"
                            break
    
    def process_govt_repos(self):
        """Process government repository catalogs"""
        logger.info("Processing government repositories...")
        
        govt_repos_path = self.workspace / "govt-repos"
        catalog_file = govt_repos_path / "government_rrb_ntpc_sources_catalog.csv"
        
        if catalog_file.exists():
            with open(catalog_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entry = {
                        'title': row.get('Portal_Name', 'Government Portal'),
                        'year': '',
                        'stage': 'RRB NTPC',
                        'sections': 'government_portals',
                        'topic_tags': 'rrb_examination,government_source',
                        'language': row.get('Bilingual_Availability', 'English,Hindi'),
                        'source_url': row.get('Source_URL', ''),
                        'source_domain': self.extract_domain(row.get('Source_URL', '')),
                        'license': 'Government Official',
                        'attribution_text': row.get('Government_Authority', ''),
                        'expected_format': 'Web Portal',
                        'intended_path': f"govt-repos/{row.get('Portal_Name', '').replace(' ', '_')}",
                        'checksum_sha256': '',
                        'filesize_bytes': 0,
                        'retrieved_at': datetime.now().isoformat(),
                        'verification_notes': f"Government authority verification: {row.get('Notes', '')}"
                    }
                    self.catalog_entries.append(entry)
    
    def create_catalog_entry(self, file_path, content_type):
        """Create a catalog entry for a file"""
        try:
            relative_path = file_path.relative_to(self.workspace)
            checksum = self.calculate_sha256(file_path)
            file_size = self.get_file_size(file_path)
            
            return {
                'title': file_path.stem,
                'year': self.extract_year_from_path(file_path),
                'stage': 'Competitive Exam',
                'sections': content_type.lower().replace(' ', '_'),
                'topic_tags': self.extract_topics_from_path(file_path),
                'language': self.detect_language(file_path),
                'source_url': '',
                'source_domain': 'local_file',
                'license': self.extract_license(file_path),
                'attribution_text': '',
                'expected_format': self.determine_format(file_path.name),
                'intended_path': str(relative_path),
                'checksum_sha256': checksum,
                'filesize_bytes': file_size,
                'retrieved_at': datetime.now().isoformat(),
                'verification_notes': f"Content type: {content_type}"
            }
        except Exception as e:
            logger.error(f"Error creating entry for {file_path}: {e}")
            return {
                'title': str(file_path),
                'year': '',
                'stage': '',
                'sections': '',
                'topic_tags': '',
                'language': '',
                'source_url': '',
                'source_domain': '',
                'license': '',
                'attribution_text': '',
                'expected_format': '',
                'intended_path': str(file_path),
                'checksum_sha256': '',
                'filesize_bytes': 0,
                'retrieved_at': datetime.now().isoformat(),
                'verification_notes': f"Error processing file: {e}"
            }
    
    def extract_year_from_path(self, file_path):
        """Extract year from file path"""
        path_str = str(file_path)
        import re
        year_match = re.search(r'(20\d{2})', path_str)
        return year_match.group(1) if year_match else ''
    
    def extract_topics_from_path(self, file_path):
        """Extract topic tags from file path"""
        path_str = str(file_path).lower()
        topic_map = {
            'math': 'mathematics',
            'algebra': 'algebra',
            'geometry': 'geometry',
            'reasoning': 'logical_reasoning',
            'history': 'indian_history',
            'geography': 'geography',
            'polity': 'polity',
            'economy': 'economics',
            'science': 'general_science',
            'physics': 'physics',
            'chemistry': 'chemistry',
            'biology': 'biology',
            'current': 'current_affairs'
        }
        
        found_topics = []
        for key, topic in topic_map.items():
            if key in path_str:
                found_topics.append(topic)
        
        return ','.join(found_topics) if found_topics else 'general'
    
    def detect_language(self, file_path):
        """Detect language from file path"""
        path_str = str(file_path).lower()
        if '/hi/' in path_str or '-hi-' in path_str or '_hi_' in path_str:
            return 'Hindi'
        elif '/en/' in path_str or '-en-' in path_str or '_en_' in path_str:
            return 'English'
        else:
            return 'Unknown'
    
    def extract_license(self, file_path):
        """Extract license information"""
        # Check if this is a known DIKSHA file
        if 'diksha' in str(file_path).lower():
            return 'CC BY 4.0'
        # Check licensing directory
        license_file = self.workspace / "licensing" / "diksha_license_register.csv"
        if license_file.exists():
            with open(license_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('content_title', '').lower() in str(file_path).lower():
                        return row.get('license_type', '')
        return 'Unknown'
    
    def generate_catalog(self):
        """Generate the master catalog by processing all sources"""
        logger.info("Starting master catalog generation...")
        
        # Process all content types
        self.process_diksha_content()
        self.process_bilingual_content()
        self.process_practice_sets()
        self.process_current_affairs()
        self.process_portal_downloads()
        self.process_downloads()
        self.process_dedup_content()
        self.process_govt_repos()
        
        # Remove duplicates based on intended_path
        unique_entries = {}
        for entry in self.catalog_entries:
            path = entry['intended_path']
            if path not in unique_entries:
                unique_entries[path] = entry
        
        self.catalog_entries = list(unique_entries.values())
        
        logger.info(f"Generated catalog with {len(self.catalog_entries)} entries")
        
    def save_csv(self, output_path):
        """Save catalog as CSV"""
        logger.info(f"Saving CSV to {output_path}")
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            if self.catalog_entries:
                writer = csv.DictWriter(f, fieldnames=self.master_fields)
                writer.writeheader()
                writer.writerows(self.catalog_entries)
        
        logger.info(f"CSV saved successfully with {len(self.catalog_entries)} entries")
    
    def save_jsonl(self, output_path):
        """Save catalog as JSONL"""
        logger.info(f"Saving JSONL to {output_path}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for entry in self.catalog_entries:
                json.dump(entry, f, ensure_ascii=False)
                f.write('\n')
        
        logger.info(f"JSONL saved successfully with {len(self.catalog_entries)} entries")
    
    def generate_statistics(self):
        """Generate catalog statistics"""
        stats = {
            'total_entries': len(self.catalog_entries),
            'format_distribution': {},
            'language_distribution': {},
            'content_type_distribution': {},
            'license_distribution': {}
        }
        
        for entry in self.catalog_entries:
            # Format distribution
            fmt = entry.get('expected_format', 'Unknown')
            stats['format_distribution'][fmt] = stats['format_distribution'].get(fmt, 0) + 1
            
            # Language distribution
            lang = entry.get('language', 'Unknown')
            stats['language_distribution'][lang] = stats['language_distribution'].get(lang, 0) + 1
            
            # Content type distribution
            content_type = entry.get('sections', 'Unknown')
            stats['content_type_distribution'][content_type] = stats['content_type_distribution'].get(content_type, 0) + 1
            
            # License distribution
            license_type = entry.get('license', 'Unknown')
            stats['license_distribution'][license_type] = stats['license_distribution'].get(license_type, 0) + 1
        
        return stats

def main():
    """Main function to generate master catalog"""
    generator = MasterCatalogGenerator()
    
    # Generate catalog
    generator.generate_catalog()
    
    # Create output directory
    output_dir = Path("/workspace/master-catalog")
    output_dir.mkdir(exist_ok=True)
    
    # Save CSV and JSONL
    csv_path = output_dir / "catalog.csv"
    jsonl_path = output_dir / "catalog.jsonl"
    
    generator.save_csv(csv_path)
    generator.save_jsonl(jsonl_path)
    
    # Generate and save statistics
    stats = generator.generate_statistics()
    stats_path = output_dir / "catalog_statistics.json"
    
    with open(stats_path, 'w') as f:
        json.dump(stats, f, indent=2)
    
    print(f"Master catalog generated successfully!")
    print(f"CSV: {csv_path}")
    print(f"JSONL: {jsonl_path}")
    print(f"Statistics: {stats_path}")
    print(f"Total entries: {stats['total_entries']}")
    
    return {
        'csv_path': str(csv_path),
        'jsonl_path': str(jsonl_path),
        'stats_path': str(stats_path),
        'total_entries': stats['total_entries'],
        'statistics': stats
    }

if __name__ == "__main__":
    result = main()
    print(f"Catalog generation completed: {result['total_entries']} entries processed")