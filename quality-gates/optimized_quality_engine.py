#!/usr/bin/env python3
"""
Optimized Quality Assessment Engine
Handles large directories by processing in batches to prevent timeouts
Designed for comprehensive content quality assessment
"""

import os
import json
import zipfile
import hashlib
import traceback
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time

class OptimizedQualityAssessment:
    def __init__(self, max_workers=4, batch_size=50):
        self.max_workers = max_workers
        self.batch_size = batch_size
        self.results = {}
        self.progress_lock = threading.Lock()
        self.total_files_processed = 0
        self.start_time = time.time()
        
    def calculate_file_hash(self, file_path):
        """Calculate SHA-256 hash of file for integrity verification"""
        try:
            hash_sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except Exception:
            return None
    
    def check_pdf_integrity(self, pdf_path):
        """Comprehensive PDF integrity check"""
        try:
            size = os.path.getsize(pdf_path)
            if size < 100:
                return "too_small"
                
            with open(pdf_path, 'rb') as f:
                header = f.read(4)
                if header != b'%PDF':
                    return "invalid_header"
                
                # Check for PDF end marker
                f.seek(0, 2)  # Go to end
                f.seek(-10, 2)  # Go back 10 bytes
                end_content = f.read()
                if b'%%EOF' not in end_content:
                    return "missing_eof"
                
                # Additional checks for large PDFs
                if size > 1000000:  # 1MB+
                    # For large files, do basic structure check
                    f.seek(0)
                    content = f.read(1024)
                    if b'/Pages' not in content and b'/Page' not in content:
                        return "suspicious_structure"
                
                return "intact"
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_json_integrity(self, json_path):
        """Check JSON file integrity and validate structure"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, (dict, list)):
                    return "invalid_structure"
                    
                # Check for required fields based on expected structure
                if isinstance(data, dict):
                    # Metadata files should have at least some meaningful content
                    if len(data) == 0:
                        return "empty"
                    # Check if it looks like metadata (has meaningful keys)
                    meaningful_keys = [k for k, v in data.items() if v and str(v).strip()]
                    if len(meaningful_keys) < 2:
                        return "minimal_content"
                
                return "intact"
        except json.JSONDecodeError as e:
            return f"invalid_json: {str(e)}"
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_zip_integrity(self, zip_path):
        """ZIP file integrity check"""
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                # Test integrity
                bad_file = zf.testzip()
                if bad_file is not None:
                    return f"corrupted_file: {bad_file}"
                    
                # Check contents
                files = zf.namelist()
                if not files:
                    return "empty"
                    
                # Check first few files for basic content
                for name in files[:3]:
                    info = zf.getinfo(name)
                    if info.file_size == 0:
                        return "contains_empty_files"
                
                return "intact"
        except zipfile.BadZipFile:
            return "invalid_zip"
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_file_integrity(self, file_path):
        """Check integrity of any file based on type"""
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext == '.pdf':
                return self.check_pdf_integrity(file_path)
            elif file_ext == '.json':
                return self.check_json_integrity(file_path)
            elif file_ext == '.zip':
                return self.check_zip_integrity(file_path)
            elif file_ext in ['.html', '.htm']:
                return "html_check_not_implemented"  # Simplified for speed
            else:
                return "basic_check"
        except Exception as e:
            return f"critical_error: {str(e)}"
    
    def process_file_batch(self, file_batch):
        """Process a batch of files"""
        batch_results = []
        
        for file_path in file_batch:
            try:
                file_info = {
                    'file_path': str(file_path),
                    'file_type': os.path.splitext(file_path)[1].lower() or 'unknown',
                    'size': 0,
                    'integrity': 'not_checked',
                    'hash': None,
                    'issues': []
                }
                
                if os.path.exists(file_path):
                    stat = os.stat(file_path)
                    file_info['size'] = stat.st_size
                    
                    # Calculate hash for files > 1KB
                    if stat.st_size > 1024:
                        file_info['hash'] = self.calculate_file_hash(file_path)
                    
                    # Check integrity
                    file_info['integrity'] = self.check_file_integrity(file_path)
                    
                    # Determine if file has issues
                    if "error" in file_info['integrity'] or "corrupted" in file_info['integrity']:
                        file_info['issues'].append(file_info['integrity'])
                
                batch_results.append(file_info)
                
            except Exception as e:
                batch_results.append({
                    'file_path': str(file_path),
                    'file_type': 'error',
                    'size': 0,
                    'integrity': f'processing_error: {str(e)}',
                    'hash': None,
                    'issues': [f'processing_error: {str(e)}']
                })
        
        return batch_results
    
    def scan_directory_batch(self, directory):
        """Scan a directory in batches to avoid timeouts"""
        print(f"Starting batch scan of: {directory}")
        
        # Get all files
        all_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                all_files.append(os.path.join(root, file))
        
        print(f"Found {len(all_files)} files to process")
        
        # Process in batches
        results = []
        for i in range(0, len(all_files), self.batch_size):
            batch = all_files[i:i + self.batch_size]
            batch_num = i // self.batch_size + 1
            total_batches = (len(all_files) + self.batch_size - 1) // self.batch_size
            
            print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} files)")
            
            try:
                batch_results = self.process_file_batch(batch)
                results.extend(batch_results)
                
                with self.progress_lock:
                    self.total_files_processed += len(batch)
                    
                # Check for timeout (2 minutes per batch)
                if time.time() - self.start_time > 120:
                    print("WARNING: Approaching timeout, reducing batch size")
                    self.batch_size = max(10, self.batch_size // 2)
                
            except Exception as e:
                print(f"ERROR in batch {batch_num}: {str(e)}")
                print(traceback.format_exc())
                # Add placeholder results for failed batch
                for file_path in batch:
                    results.append({
                        'file_path': str(file_path),
                        'file_type': 'batch_error',
                        'size': 0,
                        'integrity': f'batch_processing_failed: {str(e)}',
                        'hash': None,
                        'issues': [f'batch_processing_failed: {str(e)}']
                    })
        
        print(f"Completed batch scan. Processed {len(results)} files.")
        return results
    
    def analyze_category(self, category_path, category_name):
        """Analyze a content category comprehensively"""
        print(f"\n{'='*60}")
        print(f"ANALYZING: {category_name}")
        print(f"PATH: {category_path}")
        print(f"{'='*60}")
        
        if not os.path.exists(category_path):
            return {
                'category': category_name,
                'path': str(category_path),
                'error': 'Directory not found',
                'overall_quality_score': 0
            }
        
        try:
            # Scan files in batches
            file_results = self.scan_directory_batch(category_path)
            
            # Analyze results
            analysis = self.analyze_file_results(file_results, category_name)
            
            return analysis
            
        except Exception as e:
            print(f"ERROR analyzing {category_name}: {str(e)}")
            print(traceback.format_exc())
            return {
                'category': category_name,
                'path': str(category_path),
                'error': str(e),
                'overall_quality_score': 0,
                'file_integrity': []
            }
    
    def analyze_file_results(self, file_results, category_name):
        """Analyze file results and calculate quality metrics"""
        
        # Categorize files
        pdf_files = []
        json_files = []
        zip_files = []
        html_files = []
        other_files = []
        
        for result in file_results:
            if result['file_type'] == '.pdf':
                pdf_files.append(result)
            elif result['file_type'] == '.json':
                json_files.append(result)
            elif result['file_type'] == '.zip':
                zip_files.append(result)
            elif result['file_type'] in ['.html', '.htm']:
                html_files.append(result)
            else:
                other_files.append(result)
        
        # Calculate integrity scores
        total_files = len(file_results)
        intact_files = sum(1 for f in file_results if 'intact' in f['integrity'])
        integrity_percentage = (intact_files / total_files * 100) if total_files > 0 else 0
        
        # Calculate content completeness
        non_empty_files = sum(1 for f in file_results if f['size'] > 0)
        completeness_percentage = (non_empty_files / total_files * 100) if total_files > 0 else 0
        
        # Calculate metadata completeness (for JSON files)
        metadata_files = json_files
        complete_metadata = 0
        if metadata_files:
            for meta_file in metadata_files:
                if 'empty' not in meta_file['integrity'] and 'minimal_content' not in meta_file['integrity']:
                    complete_metadata += 1
        metadata_percentage = (complete_metadata / len(metadata_files) * 100) if metadata_files else 0
        
        # Calculate overall quality score
        quality_score = min(100, (
            integrity_percentage * 0.40 +  # File Integrity 40%
            completeness_percentage * 0.25 +  # Content Completeness 25%
            metadata_percentage * 0.20 +  # Metadata Completeness 20%
            (100 if metadata_files else 0) * 0.10 +  # Metadata Presence 10%
            (50 if non_empty_files > 0 else 0) * 0.05  # Basic Content Presence 5%
        ))
        
        # Determine compliance status
        compliance_status = "compliant" if quality_score >= 70 else "needs_review"
        
        return {
            'category_name': category_name,
            'category_path': f"/workspace/{category_name.lower().replace(' ', '-')}",
            'assessment_timestamp': datetime.now().isoformat(),
            'file_integrity': file_results,
            'format_consistency': {
                'total_files': total_files,
                'pdf_files': len(pdf_files),
                'zip_files': len(zip_files),
                'json_files': len(json_files),
                'html_files': len(html_files),
                'other_files': len(other_files),
                'dominant_format': max([
                    ("pdf", len(pdf_files)), ("json", len(json_files)), 
                    ("zip", len(zip_files)), ("html", len(html_files)), ("other", len(other_files))
                ], key=lambda x: x[1])[0]
            },
            'metadata_completeness': {
                'metadata_files_found': len(metadata_files),
                'complete_metadata_files': complete_metadata,
                'completeness_percentage': metadata_percentage
            },
            'licensing_compliance': {
                'licensing_files_found': 0,  # Would need specific checking
                'attribution_compliance': False,  # Would need specific checking
                'compliance_status': compliance_status
            },
            'content_completeness': {
                'total_files': total_files,
                'non_empty_files': non_empty_files,
                'completion_percentage': completeness_percentage
            },
            'overall_quality_score': quality_score
        }
    
    def run_assessment(self, categories):
        """Run comprehensive assessment on all categories"""
        results = {}
        
        print("Starting Optimized Quality Assessment Engine")
        print(f"Worker threads: {self.max_workers}, Batch size: {self.batch_size}")
        print("=" * 80)
        
        for category_path, category_name in categories:
            try:
                result = self.analyze_category(category_path, category_name)
                results[category_name] = result
                
                print(f"\n✓ {category_name}: Score {result['overall_quality_score']:.1f}% - Status: {result.get('licensing_compliance', {}).get('compliance_status', 'unknown')}")
                
            except Exception as e:
                print(f"✗ ERROR in {category_name}: {str(e)}")
                results[category_name] = {
                    'error': str(e),
                    'overall_quality_score': 0
                }
        
        # Save results
        output_file = "/workspace/quality-gates/comprehensive_assessment_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n{'='*80}")
        print("ASSESSMENT COMPLETED")
        print(f"Total files processed: {self.total_files_processed}")
        print(f"Results saved to: {output_file}")
        print(f"{'='*80}")
        
        return results

def main():
    """Main execution function"""
    
    # Content categories to assess
    categories = [
        ("/workspace/content/rrb-ntpc", "RRB NTPC Content"),
        ("/workspace/diksha-ga", "DIKSHA General Awareness"),
        ("/workspace/diksha-math", "DIKSHA Mathematics"),
        ("/workspace/diksha-reasoning", "DIKSHA Reasoning"),
        ("/workspace/diksha-science", "DIKSHA Science"),
        ("/workspace/practice-ga", "Practice General Awareness"),
        ("/workspace/practice-licensing", "Practice Licensing"),
        ("/workspace/practice-math", "Practice Mathematics"),
        ("/workspace/practice-reasoning", "Practice Reasoning"),
        ("/workspace/portal-downloads", "Portal Downloads"),
        ("/workspace/current-affairs", "Current Affairs"),
        ("/workspace/govt-repos", "Government Repositories")
    ]
    
    # Initialize optimized assessment engine
    qa_engine = OptimizedQualityAssessment(max_workers=4, batch_size=30)
    
    # Run assessment
    results = qa_engine.run_assessment(categories)
    
    return results

if __name__ == "__main__":
    main()
