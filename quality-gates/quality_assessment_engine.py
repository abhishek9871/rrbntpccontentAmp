import os
import hashlib
import json
import csv
import re
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime
import mimetypes

class QualityAssessment:
    def __init__(self):
        self.results = {}
        self.issues = []
        self.compliance_scores = {}
        
    def check_file_integrity(self, file_path, file_type="unknown"):
        """Check if file is corrupted or incomplete"""
        result = {
            "file_path": str(file_path),
            "file_type": file_type,
            "exists": False,
            "size": 0,
            "integrity": "unknown",
            "issues": []
        }
        
        if not os.path.exists(file_path):
            result["issues"].append("File does not exist")
            return result
            
        result["exists"] = True
        result["size"] = os.path.getsize(file_path)
        
        # Check file type specific integrity
        if file_type == "pdf":
            result["integrity"] = self.check_pdf_integrity(file_path)
        elif file_type == "zip":
            result["integrity"] = self.check_zip_integrity(file_path)
        elif file_type == "json":
            result["integrity"] = self.check_json_integrity(file_path)
        elif file_type == "html":
            result["integrity"] = self.check_html_integrity(file_path)
        else:
            result["integrity"] = "basic_check"
            
        return result
        
    def check_pdf_integrity(self, pdf_path):
        """Check PDF integrity using various methods"""
        try:
            # Check file size - PDFs should be reasonable size
            size = os.path.getsize(pdf_path)
            if size < 100:  # Less than 100 bytes is suspicious
                return "corrupted"
                
            # Try to read PDF header
            with open(pdf_path, 'rb') as f:
                header = f.read(4)
                if header != b'%PDF':
                    return "corrupted"
                    
            # Try using pdfplumber if available for deeper inspection
            try:
                import pdfplumber
                with pdfplumber.open(pdf_path) as pdf:
                    pages = len(pdf.pages)
                    if pages == 0:
                        return "corrupted"
                    # Check for minimal content on pages
                    for page in pdf.pages[:3]:  # Check first 3 pages
                        text = page.extract_text()
                        if text and len(text.strip()) < 50:
                            return "incomplete"
                return "intact"
            except ImportError:
                # Fallback to basic check
                return "basic_intact"
                
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_zip_integrity(self, zip_path):
        """Check ZIP file integrity"""
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                # Test the ZIP file
                test_result = zf.testzip()
                if test_result is not None:
                    return "corrupted"
                    
                # Check if ZIP contains files
                if len(zf.namelist()) == 0:
                    return "empty"
                    
            return "intact"
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_json_integrity(self, json_path):
        """Check JSON file integrity"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) or isinstance(data, list):
                    return "intact"
                else:
                    return "invalid_structure"
        except json.JSONDecodeError as e:
            return f"invalid_json: {str(e)}"
        except Exception as e:
            return f"error: {str(e)}"
    
    def check_html_integrity(self, html_path):
        """Check HTML file integrity"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content.strip()) < 100:
                    return "too_small"
                    
                # Check for basic HTML structure
                if '<html' not in content.lower() and '<!doctype' not in content.lower():
                    return "no_html_structure"
                    
            return "intact"
        except Exception as e:
            return f"error: {str(e)}"
    
    def assess_content_category(self, category_path, category_name):
        """Assess quality for a content category"""
        print(f"Assessing {category_name}...")
        
        category_result = {
            "category_name": category_name,
            "category_path": str(category_path),
            "assessment_timestamp": datetime.now().isoformat(),
            "file_integrity": [],
            "format_consistency": {},
            "metadata_completeness": {},
            "licensing_compliance": {},
            "content_completeness": {}
        }
        
        # Get all files in category
        files = []
        for root, dirs, filenames in os.walk(category_path):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        
        # File Integrity Checks
        pdf_count = 0
        zip_count = 0
        json_count = 0
        html_count = 0
        other_count = 0
        
        for file_path in files:
            file_ext = os.path.splitext(file_path)[1].lower()
            file_type = "other"
            
            if file_ext == ".pdf":
                file_type = "pdf"
                pdf_count += 1
            elif file_ext == ".zip":
                file_type = "zip"
                zip_count += 1
            elif file_ext == ".json":
                file_type = "json"
                json_count += 1
            elif file_ext in [".html", ".htm"]:
                file_type = "html"
                html_count += 1
            else:
                other_count += 1
                
            integrity_result = self.check_file_integrity(file_path, file_type)
            category_result["file_integrity"].append(integrity_result)
        
        # Format Consistency Assessment
        category_result["format_consistency"] = {
            "total_files": len(files),
            "pdf_files": pdf_count,
            "zip_files": zip_count,
            "json_files": json_count,
            "html_files": html_count,
            "other_files": other_count,
            "dominant_format": max([
                ("pdf", pdf_count), ("zip", zip_count), 
                ("json", json_count), ("html", html_count), ("other", other_count)
            ], key=lambda x: x[1])[0]
        }
        
        # Metadata Completeness Assessment
        metadata_files = [f for f in files if f.endswith('.json')]
        if metadata_files:
            complete_metadata = 0
            for meta_file in metadata_files:
                try:
                    with open(meta_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and len(data) > 0:
                            complete_metadata += 1
                except:
                    pass
            
            category_result["metadata_completeness"] = {
                "metadata_files_found": len(metadata_files),
                "complete_metadata_files": complete_metadata,
                "completeness_percentage": (complete_metadata / len(metadata_files)) * 100 if metadata_files else 0
            }
        
        # Content Completeness Assessment
        category_result["content_completeness"] = self.assess_content_completeness(files)
        
        # Licensing Compliance Assessment  
        category_result["licensing_compliance"] = self.assess_licensing_compliance(category_path, files)
        
        return category_result
    
    def assess_content_completeness(self, files):
        """Assess content completeness across files"""
        completeness_result = {
            "total_files": len(files),
            "non_empty_files": 0,
            "files_with_content": 0,
            "completion_percentage": 0
        }
        
        for file_path in files:
            try:
                if file_path.endswith('.pdf'):
                    # Basic PDF completeness check
                    size = os.path.getsize(file_path)
                    if size > 100:  # Minimum reasonable size
                        completeness_result["non_empty_files"] += 1
                        completeness_result["files_with_content"] += 1
                elif file_path.endswith('.json'):
                    # Check JSON files for content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if data and len(str(data).strip()) > 10:
                            completeness_result["files_with_content"] += 1
                            completeness_result["non_empty_files"] += 1
                elif file_path.endswith(('.html', '.htm', '.md', '.txt')):
                    # Check text-based files for content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        if len(content) > 50:
                            completeness_result["non_empty_files"] += 1
                            completeness_result["files_with_content"] += 1
            except:
                pass
        
        if completeness_result["total_files"] > 0:
            completeness_result["completion_percentage"] = (
                completeness_result["files_with_content"] / completeness_result["total_files"]
            ) * 100
        
        return completeness_result
    
    def assess_licensing_compliance(self, category_path, files):
        """Assess licensing compliance"""
        # Look for licensing files
        licensing_files = [
            "LICENSE", "license", "LICENSE.txt", "license.txt",
            "COPYING", "COPYING.txt", "README.md", "README"
        ]
        
        licensing_found = []
        for file_path in files:
            filename = os.path.basename(file_path).lower()
            for lic_file in licensing_files:
                if lic_file.lower() in filename:
                    licensing_found.append(file_path)
        
        # Check if attribution requirements are met
        attribution_compliant = False
        if licensing_found:
            attribution_compliant = True  # Assuming presence means compliance
        
        return {
            "licensing_files_found": len(licensing_found),
            "licensing_files": licensing_found,
            "attribution_compliance": attribution_compliant,
            "compliance_status": "compliant" if licensing_found else "needs_review"
        }
    
    def calculate_quality_score(self, category_result):
        """Calculate overall quality score for a category"""
        score = 0
        
        # File Integrity Score (40%)
        if category_result["file_integrity"]:
            intact_files = sum(1 for f in category_result["file_integrity"] if "intact" in f["integrity"])
            integrity_percentage = (intact_files / len(category_result["file_integrity"])) * 100
            score += integrity_percentage * 0.4
        
        # Content Completeness Score (25%)
        if "completion_percentage" in category_result["content_completeness"]:
            score += category_result["content_completeness"]["completion_percentage"] * 0.25
        
        # Metadata Completeness Score (20%)
        if "completeness_percentage" in category_result["metadata_completeness"]:
            score += category_result["metadata_completeness"]["completeness_percentage"] * 0.20
        
        # Licensing Compliance Score (15%)
        if category_result["licensing_compliance"]["compliance_status"] == "compliant":
            score += 15
        elif category_result["licensing_compliance"]["attribution_compliance"]:
            score += 10
        
        return min(score, 100)  # Cap at 100

def main():
    """Main quality assessment execution"""
    qa = QualityAssessment()
    
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
    
    results = {}
    
    for category_path, category_name in categories:
        if os.path.exists(category_path):
            try:
                result = qa.assess_content_category(category_path, category_name)
                quality_score = qa.calculate_quality_score(result)
                result["overall_quality_score"] = quality_score
                results[category_name] = result
                print(f"✓ Completed assessment for {category_name} - Score: {quality_score:.1f}%")
            except Exception as e:
                print(f"✗ Error assessing {category_name}: {str(e)}")
                results[category_name] = {
                    "error": str(e),
                    "overall_quality_score": 0
                }
        else:
            print(f"✗ Category not found: {category_path}")
    
    return results

if __name__ == "__main__":
    results = main()
    
    # Save results
    with open("/workspace/quality-gates/quality_assessment_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\nQuality assessment completed. Results saved to quality_assessment_results.json")