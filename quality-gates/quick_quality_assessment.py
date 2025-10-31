import os
import json
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime

def check_pdf_integrity(pdf_path):
    """Basic PDF integrity check"""
    try:
        size = os.path.getsize(pdf_path)
        if size < 100:
            return "corrupted_too_small"
            
        with open(pdf_path, 'rb') as f:
            header = f.read(4)
            if header != b'%PDF':
                return "corrupted_header"
                
        return "intact"
    except Exception as e:
        return f"error: {str(e)}"

def check_zip_integrity(zip_path):
    """ZIP file integrity check"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            test_result = zf.testzip()
            if test_result is not None:
                return "corrupted"
            if len(zf.namelist()) == 0:
                return "empty"
        return "intact"
    except Exception as e:
        return f"error: {str(e)}"

def check_json_integrity(json_path):
    """JSON integrity check"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return "intact"
    except Exception as e:
        return f"error: {str(e)}"

def assess_category_quickly(category_path, category_name):
    """Quick quality assessment for a category"""
    print(f"Quick assessment: {category_name}")
    
    result = {
        "category": category_name,
        "path": str(category_path),
        "timestamp": datetime.now().isoformat(),
        "total_files": 0,
        "files_by_type": {},
        "integrity_issues": [],
        "compliance_status": "unknown"
    }
    
    if not os.path.exists(category_path):
        result["compliance_status"] = "not_found"
        return result
    
    # Quick file scan
    files = []
    for root, dirs, filenames in os.walk(category_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    
    result["total_files"] = len(files)
    
    # Count by type and check integrity sample
    file_types = {}
    integrity_checked = 0
    
    for file_path in files[:50]:  # Limit to first 50 files for speed
        file_ext = os.path.splitext(file_path)[1].lower()
        file_types[file_ext] = file_types.get(file_ext, 0) + 1
        
        # Check integrity for samples
        if file_ext == ".pdf" and integrity_checked < 10:
            status = check_pdf_integrity(file_path)
            if "error" in status or "corrupted" in status:
                result["integrity_issues"].append(f"PDF: {file_path} - {status}")
            integrity_checked += 1
        elif file_ext == ".zip" and integrity_checked < 5:
            status = check_zip_integrity(file_path)
            if "error" in status or "corrupted" in status:
                result["integrity_issues"].append(f"ZIP: {file_path} - {status}")
            integrity_checked += 1
        elif file_ext == ".json" and integrity_checked < 5:
            status = check_json_integrity(file_path)
            if "error" in status or "corrupted" in status:
                result["integrity_issues"].append(f"JSON: {file_path} - {status}")
            integrity_checked += 1
    
    result["files_by_type"] = file_types
    
    # Determine compliance status
    if result["integrity_issues"]:
        result["compliance_status"] = "has_issues"
    else:
        result["compliance_status"] = "passed_basic_checks"
    
    return result

def main():
    """Main quick assessment"""
    categories = [
        ("/workspace/content/rrb-ntpc", "RRB NTPC"),
        ("/workspace/diksha-ga", "DIKSHA GA"),
        ("/workspace/diksha-math", "DIKSHA Math"),
        ("/workspace/diksha-reasoning", "DIKSHA Reasoning"),
        ("/workspace/diksha-science", "DIKSHA Science"),
        ("/workspace/practice-ga", "Practice GA"),
        ("/workspace/practice-licensing", "Practice Licensing"),
        ("/workspace/practice-math", "Practice Math"),
        ("/workspace/practice-reasoning", "Practice Reasoning"),
        ("/workspace/portal-downloads", "Portal Downloads")
    ]
    
    results = {}
    
    for category_path, category_name in categories:
        try:
            result = assess_category_quickly(category_path, category_name)
            results[category_name] = result
            print(f"✓ {category_name}: {result['total_files']} files, Status: {result['compliance_status']}")
        except Exception as e:
            print(f"✗ Error in {category_name}: {str(e)}")
            results[category_name] = {"error": str(e)}
    
    # Save quick results
    with open("/workspace/quality-gates/quick_quality_assessment.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\nQuick assessment completed!")
    return results

if __name__ == "__main__":
    results = main()