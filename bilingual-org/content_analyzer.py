#!/usr/bin/env python3
"""
Content Language Analyzer for RRB-NTPC Bilingual Organization
Analyzes files to determine language availability (English, Hindi, or Both)
"""

import os
import json
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Set, Tuple

class ContentLanguageAnalyzer:
    def __init__(self):
        self.analysis_results = []
        self.language_patterns = {
            'english': [
                r'.*_en\b', r'\benglish\b', r'\beng\b', r'\ben\b',
                r'class\d+-english', r'class\d+-eng'
            ],
            'hindi': [
                r'.*_hi\b', r'\bhindi\b', r'\bhin\b', r'class\d+-hindi',
                r'class\d+-hin', r'\bhindi\.zip\b'
            ],
            'both': [
                r'.*_bilingual\b', r'\bbilingual\b', r'\bboth\b'
            ]
        }
        
        # Extensions that typically contain text content
        self.text_extensions = {'.pdf', '.txt', '.md', '.json', '.html', '.htm'}
        
    def is_text_file(self, file_path: Path) -> bool:
        """Check if file is likely to contain readable text"""
        return file_path.suffix.lower() in self.text_extensions
    
    def detect_language_from_name(self, file_path: Path) -> str:
        """Detect language from filename patterns"""
        name_lower = file_path.name.lower()
        
        # Check for English indicators
        for pattern in self.language_patterns['english']:
            if re.search(pattern, name_lower, re.IGNORECASE):
                return 'en'
                
        # Check for Hindi indicators
        for pattern in self.language_patterns['hindi']:
            if re.search(pattern, name_lower, re.IGNORECASE):
                return 'hi'
                
        # Check for bilingual indicators
        for pattern in self.language_patterns['both']:
            if re.search(pattern, name_lower, re.IGNORECASE):
                return 'both'
        
        return 'unknown'
    
    def detect_language_from_path(self, path_parts: List[str]) -> str:
        """Detect language from directory path"""
        path_str = '/'.join(path_parts).lower()
        
        if '/english/' in path_str or '/eng/' in path_str:
            return 'en'
        elif '/hindi/' in path_str or '/hin/' in path_str:
            return 'hi'
        elif '/bilingual/' in path_str:
            return 'both'
            
        return 'unknown'
    
    def analyze_file_content(self, file_path: Path) -> str:
        """Basic content analysis for language detection"""
        if not self.is_text_file(file_path):
            return 'unknown'
            
        try:
            # For small files, try to read and analyze content
            if file_path.stat().st_size < 1024 * 100:  # 100KB limit
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(1000)  # Read first 1000 chars
                    
                    # Count Devanagari vs Latin characters
                    devanagari_count = len(re.findall(r'[\u0900-\u097F]', content))
                    latin_count = len(re.findall(r'[a-zA-Z]', content))
                    
                    if devanagari_count > latin_count * 0.1:
                        return 'hi'
                    elif latin_count > 0:
                        return 'en'
        except Exception:
            pass
            
        return 'unknown'
    
    def analyze_metadata_files(self, source_dir: Path) -> Dict[str, str]:
        """Analyze metadata files for language information"""
        language_map = {}
        
        # Look for common metadata files
        metadata_patterns = [
            'metadata.json', 'content_inventory.json', 'final_comprehensive_inventory.json',
            'comprehensive_metadata.json', 'sources_catalog.json', 'collection_metadata.json'
        ]
        
        for pattern in metadata_patterns:
            metadata_file = source_dir / pattern
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                        # Extract language information if available
                        if isinstance(data, dict):
                            for key, value in data.items():
                                if isinstance(value, str) and any(lang in value.lower() for lang in ['english', 'hindi', 'eng', 'hin']):
                                    language_map[key] = value
                except Exception:
                    continue
                    
        return language_map
    
    def analyze_directory(self, source_dir: Path, category: str, source_path: str) -> List[Dict]:
        """Analyze a directory for content and language"""
        results = []
        
        # First check metadata for language hints
        metadata_languages = self.analyze_metadata_files(source_dir)
        
        for root, dirs, files in os.walk(source_dir):
            current_path = Path(root)
            path_parts = current_path.parts
            
            # Skip hidden directories and logs
            if any(part.startswith('.') or part in ['logs', 'temp', 'cache'] for part in path_parts):
                continue
                
            for file in files:
                if file.startswith('.') or file.endswith('.log'):
                    continue
                    
                file_path = current_path / file
                
                # Basic file info
                file_info = {
                    'source_path': source_path,
                    'category': category,
                    'relative_path': str(file_path.relative_to(source_dir)) if file_path.is_relative_to(source_dir) else str(file_path),
                    'filename': file,
                    'file_type': file_path.suffix.lower(),
                    'size_bytes': file_path.stat().st_size,
                    'language': 'unknown',
                    'confidence': 'low',
                    'detection_method': 'none'
                }
                
                # Language detection methods (priority order)
                # 1. Check parent directory names
                lang_from_path = self.detect_language_from_path(path_parts)
                if lang_from_path != 'unknown':
                    file_info['language'] = lang_from_path
                    file_info['confidence'] = 'high'
                    file_info['detection_method'] = 'path'
                
                # 2. Check filename patterns
                elif self.is_text_file(file_path):
                    lang_from_name = self.detect_language_from_name(file_path)
                    if lang_from_name != 'unknown':
                        file_info['language'] = lang_from_name
                        file_info['confidence'] = 'medium'
                        file_info['detection_method'] = 'filename'
                    
                    # 3. Check content
                    else:
                        lang_from_content = self.analyze_file_content(file_path)
                        if lang_from_content != 'unknown':
                            file_info['language'] = lang_from_content
                            file_info['confidence'] = 'medium'
                            file_info['detection_method'] = 'content'
                
                # 4. Check metadata
                file_key = file_info['relative_path']
                if file_key in metadata_languages:
                    metadata_lang = metadata_languages[file_key].lower()
                    if 'english' in metadata_lang:
                        file_info['language'] = 'en'
                    elif 'hindi' in metadata_lang:
                        file_info['language'] = 'hi'
                    file_info['confidence'] = 'high'
                    file_info['detection_method'] = 'metadata'
                
                # 5. Default fallback based on common patterns
                if file_info['language'] == 'unknown':
                    # Educational materials are often in English unless specified
                    if any(keyword in file.lower() for keyword in ['ncert', 'cbse', 'sample', 'guide', 'practice']):
                        file_info['language'] = 'en'
                    elif any(keyword in file.lower() for keyword in ['guide', 'hindi']):
                        file_info['language'] = 'hi'
                    file_info['confidence'] = 'low'
                    file_info['detection_method'] = 'default'
                
                # Skip very small files that are likely not content
                if file_info['size_bytes'] < 1024:
                    continue
                    
                results.append(file_info)
        
        return results

def main():
    analyzer = ContentLanguageAnalyzer()
    
    # Define source directories and their categories
    sources = {
        '/workspace/diksha-math/study-materials/oer/mathematics': 'study-materials',
        '/workspace/diksha-reasoning': 'study-materials',
        '/workspace/diksha-science': 'study-materials',
        '/workspace/diksha-ga': 'study-materials',
        '/workspace/wikimedia-math': 'study-materials',
        '/workspace/wikimedia-general_science': 'study-materials',
        '/workspace/wikimedia-general_awareness': 'study-materials',
        '/workspace/practice-math': 'practice-sets',
        '/workspace/practice-reasoning': 'practice-sets',
        '/workspace/practice-ga': 'practice-sets',
        '/workspace/current-affairs': 'current-affairs',
        '/workspace/portal-downloads': 'previous-papers',
        '/workspace/downloads/rrb-ntpc': 'previous-papers',
        '/workspace/downloads': 'mixed'
    }
    
    all_results = []
    
    print("🔍 Starting comprehensive content analysis...")
    
    for source_path, category in sources.items():
        source_dir = Path(source_path)
        if source_dir.exists():
            print(f"📁 Analyzing: {source_path}")
            results = analyzer.analyze_directory(source_dir, category, source_path)
            all_results.extend(results)
            print(f"   Found {len(results)} files")
        else:
            print(f"⚠️  Directory not found: {source_path}")
    
    # Save detailed analysis
    output_file = '/workspace/bilingual-org/content_analysis_results.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    # Generate summary statistics
    stats = {
        'total_files': len(all_results),
        'by_language': {},
        'by_category': {},
        'by_source': {},
        'by_confidence': {}
    }
    
    for result in all_results:
        lang = result['language']
        category = result['category']
        source = result['source_path']
        confidence = result['confidence']
        
        stats['by_language'][lang] = stats['by_language'].get(lang, 0) + 1
        stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
        stats['by_source'][source] = stats['by_source'].get(source, 0) + 1
        stats['by_confidence'][confidence] = stats['by_confidence'].get(confidence, 0) + 1
    
    # Save statistics
    stats_file = '/workspace/bilingual-org/analysis_statistics.json'
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 Analysis Complete!")
    print(f"Total files analyzed: {len(all_results)}")
    print(f"Results saved to: {output_file}")
    print(f"Statistics saved to: {stats_file}")
    
    return all_results

if __name__ == "__main__":
    main()
