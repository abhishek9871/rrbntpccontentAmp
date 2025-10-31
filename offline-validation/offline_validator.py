#!/usr/bin/env python3
"""
Offline Validation Tester
Tests sampled files for offline accessibility, readability, and rendering
"""

import os
import json
import csv
import mimetypes
import subprocess
from pathlib import Path
import re
from urllib.parse import urlparse
import hashlib
import time

class OfflineValidator:
    def __init__(self, sample_inventory_file):
        self.results = []
        self.sample_inventory_file = sample_inventory_file
        self.load_sample_inventory()
        
    def load_sample_inventory(self):
        """Load the sample inventory from JSON file"""
        with open(self.sample_inventory_file, 'r', encoding='utf-8') as f:
            self.inventory = json.load(f)
    
    def check_file_accessibility(self, file_path):
        """Check if file is accessible and readable"""
        result = {
            'accessible': False,
            'readable': False,
            'size': 0,
            'permissions': 'unknown',
            'checksum': None,
            'error': None
        }
        
        try:
            # Check if file exists and is accessible
            if os.path.exists(file_path):
                result['accessible'] = True
                result['size'] = os.path.getsize(file_path)
                result['permissions'] = oct(os.stat(file_path).st_mode)[-3:]
                
                # Try to read the file (basic accessibility check)
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read(1024)  # Read first 1KB
                        result['readable'] = True
                        
                        # Generate checksum
                        f.seek(0)
                        hasher = hashlib.sha256()
                        while chunk := f.read(8192):
                            hasher.update(chunk)
                        result['checksum'] = hasher.hexdigest()
                        
                except Exception as e:
                    result['error'] = f"Read error: {str(e)}"
            else:
                result['error'] = "File does not exist"
                
        except Exception as e:
            result['error'] = f"Access error: {str(e)}"
            
        return result
    
    def test_pdf_readability(self, file_path):
        """Test PDF file readability"""
        result = {
            'valid_pdf': False,
            'page_count': 0,
            'text_extractable': False,
            'embedded_images': False,
            'links_functional': False,
            'error': None
        }
        
        try:
            # Check if file starts with PDF magic bytes
            with open(file_path, 'rb') as f:
                header = f.read(4)
                if header.startswith(b'%PDF'):
                    result['valid_pdf'] = True
                    
                    # Try to extract basic PDF info using python libraries
                    try:
                        import PyPDF2
                        with open(file_path, 'rb') as pdf_file:
                            pdf_reader = PyPDF2.PdfReader(pdf_file)
                            result['page_count'] = len(pdf_reader.pages)
                            
                            # Test text extraction
                            try:
                                text = pdf_reader.pages[0].extract_text()
                                result['text_extractable'] = len(text.strip()) > 0
                            except:
                                result['text_extractable'] = False
                                
                    except ImportError:
                        # Fallback: basic PDF structure check
                        with open(file_path, 'rb') as f:
                            content = f.read().decode('latin-1', errors='ignore')
                            # Look for PDF objects and pages
                            if '/Type /Page' in content:
                                page_matches = re.findall(r'/Type /Page', content)
                                result['page_count'] = len(page_matches)
                                result['valid_pdf'] = True
                            if '/XObject' in content and '/Image' in content:
                                result['embedded_images'] = True
                                
                else:
                    result['error'] = "Invalid PDF header"
                    
        except Exception as e:
            result['error'] = f"PDF test error: {str(e)}"
            
        return result
    
    def test_html_rendering(self, file_path):
        """Test HTML file rendering"""
        result = {
            'valid_html': False,
            'has_doctype': False,
            'has_head': False,
            'has_body': False,
            'linked_resources': [],
            'inline_resources': [],
            'has_css': False,
            'has_js': False,
            'error': None
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Basic HTML structure check
            content_lower = content.lower()
            result['valid_html'] = '<html' in content_lower or '<!doctype' in content_lower
            result['has_doctype'] = '<!doctype' in content_lower or 'doctype' in content_lower
            result['has_head'] = '<head' in content_lower
            result['has_body'] = '<body' in content_lower
            
            # Check for CSS and JS
            result['has_css'] = any(tag in content_lower for tag in ['<style', '<link', '.css'])
            result['has_js'] = any(tag in content_lower for tag in ['<script', 'javascript:', 'function'])
            
            # Extract linked resources (src and href attributes)
            src_pattern = r'src=["\']([^"\']+)["\']'
            href_pattern = r'href=["\']([^"\']+)["\']'
            
            src_matches = re.findall(src_pattern, content)
            href_matches = re.findall(href_pattern, content)
            
            result['linked_resources'] = list(set(src_matches + href_matches))
            
            # Check if linked resources are local (relative paths)
            local_resources = []
            external_resources = []
            
            for resource in result['linked_resources']:
                if resource.startswith(('http://', 'https://', '//')):
                    external_resources.append(resource)
                else:
                    local_resources.append(resource)
            
            result['inline_resources'] = local_resources
            result['external_resources'] = external_resources
            
        except Exception as e:
            result['error'] = f"HTML test error: {str(e)}"
            
        return result
    
    def test_image_display(self, file_path):
        """Test image file display"""
        result = {
            'valid_image': False,
            'image_type': 'unknown',
            'dimensions': None,
            'has_transparency': False,
            'file_corrupted': False,
            'error': None
        }
        
        try:
            # Check file extension and MIME type
            ext = os.path.splitext(file_path)[1].lower()
            mime_type, _ = mimetypes.guess_type(file_path)
            
            image_types = {
                '.jpg': 'JPEG',
                '.jpeg': 'JPEG', 
                '.png': 'PNG',
                '.gif': 'GIF',
                '.bmp': 'BMP',
                '.tiff': 'TIFF',
                '.svg': 'SVG'
            }
            
            if ext in image_types:
                result['image_type'] = image_types[ext]
                
                # Basic image validation by checking file headers
                with open(file_path, 'rb') as f:
                    header = f.read(16)
                    
                if ext in ['.jpg', '.jpeg'] and header.startswith(b'\xff\xd8\xff'):
                    result['valid_image'] = True
                elif ext == '.png' and header.startswith(b'\x89PNG\r\n\x1a\n'):
                    result['valid_image'] = True
                elif ext == '.gif' and header.startswith(b'GIF87a', b'GIF89a'):
                    result['valid_image'] = True
                elif ext == '.bmp' and header.startswith(b'BM'):
                    result['valid_image'] = True
                elif ext == '.svg' and 'svg' in open(file_path, 'r').read(100).lower():
                    result['valid_image'] = True
                else:
                    result['file_corrupted'] = True
                    
        except Exception as e:
            result['error'] = f"Image test error: {str(e)}"
            
        return result
    
    def test_metadata_parsing(self, file_path):
        """Test metadata file parsing (JSON, CSV, MD)"""
        result = {
            'valid_format': False,
            'parsed_successfully': False,
            'structure_valid': False,
            'data_integrity': False,
            'encoding_issues': False,
            'error': None
        }
        
        ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if ext == '.json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    result['valid_format'] = True
                    result['parsed_successfully'] = True
                    result['structure_valid'] = isinstance(data, (dict, list))
                    result['data_integrity'] = len(str(data)) > 0
                    
            elif ext == '.csv':
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    rows = list(reader)
                    result['valid_format'] = True
                    result['parsed_successfully'] = len(rows) > 0
                    result['structure_valid'] = len(rows) > 0 and all(len(row) > 0 for row in rows[:5])
                    result['data_integrity'] = len(rows) > 1
                    
            elif ext == '.md':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    result['valid_format'] = True
                    result['parsed_successfully'] = len(content) > 0
                    result['structure_valid'] = '#' in content or '*' in content or '-' in content
                    result['data_integrity'] = len(content.strip()) > 10
                    
        except UnicodeDecodeError:
            result['encoding_issues'] = True
            result['error'] = "Encoding issues detected"
        except Exception as e:
            result['error'] = f"Metadata parsing error: {str(e)}"
            
        return result
    
    def validate_sample_file(self, sample_file):
        """Validate a single sample file"""
        file_path = sample_file['path']
        category = sample_file['category']
        file_name = sample_file['name']
        extension = sample_file['extension']
        
        print(f"Testing: {file_name} ({category})")
        
        # Basic file accessibility
        accessibility_result = self.check_file_accessibility(file_path)
        
        # File-specific testing
        file_specific_result = {}
        
        if extension == '.pdf':
            file_specific_result = self.test_pdf_readability(file_path)
        elif extension == '.html':
            file_specific_result = self.test_html_rendering(file_path)
        elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']:
            file_specific_result = self.test_image_display(file_path)
        elif extension in ['.json', '.csv', '.md']:
            file_specific_result = self.test_metadata_parsing(file_path)
        else:
            file_specific_result = {'note': f'File type {extension} not specifically tested'}
        
        # Compile comprehensive result
        validation_result = {
            'file_name': file_name,
            'category': category,
            'file_path': file_path,
            'relative_path': sample_file['relative_path'],
            'extension': extension,
            'size': accessibility_result['size'],
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'accessibility': accessibility_result,
            'file_specific': file_specific_result,
            'overall_status': self.determine_overall_status(accessibility_result, file_specific_result)
        }
        
        self.results.append(validation_result)
        return validation_result
    
    def determine_overall_status(self, accessibility, file_specific):
        """Determine overall validation status"""
        if not accessibility['accessible']:
            return 'FAILED'
        if not accessibility['readable']:
            return 'FAILED'
        
        # Check file-specific validation
        if file_specific.get('valid_pdf', True) and file_specific.get('valid_html', True):
            if file_specific.get('parsed_successfully', True):
                return 'PASSED'
        
        # Special cases
        if 'error' in file_specific and file_specific['error'] is None:
            return 'PASSED'
            
        return 'WARNING'
    
    def validate_all_samples(self):
        """Validate all sample files"""
        print("Starting offline validation of sample files...")
        print("=" * 60)
        
        for category, sample_files in self.inventory['sample_files'].items():
            print(f"\nValidating category: {category}")
            print("-" * 40)
            
            for sample_file in sample_files:
                self.validate_sample_file(sample_file)
        
        return self.results
    
    def save_results(self, output_file):
        """Save validation results to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
    
    def generate_summary(self):
        """Generate validation summary"""
        total_files = len(self.results)
        passed = sum(1 for r in self.results if r['overall_status'] == 'PASSED')
        failed = sum(1 for r in self.results if r['overall_status'] == 'FAILED')
        warnings = sum(1 for r in self.results if r['overall_status'] == 'WARNING')
        
        summary = {
            'total_files_tested': total_files,
            'passed': passed,
            'failed': failed,
            'warnings': warnings,
            'pass_rate': (passed / total_files * 100) if total_files > 0 else 0,
            'categories': {}
        }
        
        # Category breakdown
        for category in set(r['category'] for r in self.results):
            category_files = [r for r in self.results if r['category'] == category]
            cat_passed = sum(1 for r in category_files if r['overall_status'] == 'PASSED')
            cat_total = len(category_files)
            
            summary['categories'][category] = {
                'total': cat_total,
                'passed': cat_passed,
                'pass_rate': (cat_passed / cat_total * 100) if cat_total > 0 else 0
            }
        
        return summary

if __name__ == "__main__":
    print("Starting Offline Validation Process...")
    
    validator = OfflineValidator('/workspace/offline-validation/sample_inventory.json')
    
    # Validate all samples
    results = validator.validate_all_samples()
    
    # Save results
    results_file = '/workspace/offline-validation/validation_results.json'
    validator.save_results(results_file)
    
    # Generate and display summary
    summary = validator.generate_summary()
    
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Total Files Tested: {summary['total_files_tested']}")
    print(f"Passed: {summary['passed']} ({summary['pass_rate']:.1f}%)")
    print(f"Failed: {summary['failed']}")
    print(f"Warnings: {summary['warnings']}")
    
    print("\nCategory Breakdown:")
    for category, stats in summary['categories'].items():
        print(f"  {category}: {stats['passed']}/{stats['total']} ({stats['pass_rate']:.1f}%)")
    
    print(f"\nDetailed results saved to: {results_file}")
