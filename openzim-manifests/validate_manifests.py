#!/usr/bin/env python3
"""
OpenZIM Build Manifest Validator
Validates YAML and JSON manifest files for structure and compliance
"""

import yaml
import json
import os
import sys
from typing import Dict, List, Any

def validate_manifest_file(file_path: str) -> Dict[str, Any]:
    """Validate a single manifest file"""
    result = {
        'file': file_path,
        'valid': True,
        'errors': [],
        'warnings': [],
        'info': []
    }
    
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine format and parse
        if file_path.endswith('.yml') or file_path.endswith('.yaml'):
            try:
                manifest = yaml.safe_load(content)
                result['info'].append('Successfully parsed as YAML')
            except yaml.YAMLError as e:
                result['valid'] = False
                result['errors'].append(f'YAML parsing error: {e}')
                return result
        elif file_path.endswith('.json'):
            try:
                manifest = json.loads(content)
                result['info'].append('Successfully parsed as JSON')
            except json.JSONDecodeError as e:
                result['valid'] = False
                result['errors'].append(f'JSON parsing error: {e}')
                return result
        else:
            result['valid'] = False
            result['errors'].append('Unknown file format - must be .yml, .yaml, or .json')
            return result
        
        # Validate required fields
        required_fields = [
            'bundle_id', 'version', 'created_date', 'description', 'target_audience',
            'bundle_config', 'content_sources', 'licensing_compliance', 'build_config'
        ]
        
        for field in required_fields:
            if field not in manifest:
                result['valid'] = False
                result['errors'].append(f'Missing required field: {field}')
        
        # Validate bundle configuration
        if 'bundle_config' in manifest:
            config = manifest['bundle_config']
            required_config = ['language_support', 'total_content_size', 'compression_level']
            for field in required_config:
                if field not in config:
                    result['valid'] = False
                    result['errors'].append(f'Missing bundle_config.{field}')
        
        # Validate content sources
        if 'content_sources' in manifest:
            sources = manifest['content_sources']
            if not isinstance(sources, dict) or len(sources) == 0:
                result['valid'] = False
                result['errors'].append('content_sources must be a non-empty dictionary')
            else:
                for source_name, source_config in sources.items():
                    if not isinstance(source_config, dict):
                        result['valid'] = False
                        result['errors'].append(f'content_sources.{source_name} must be a dictionary')
                    elif 'source_path' not in source_config:
                        result['valid'] = False
                        result['errors'].append(f'content_sources.{source_name} missing source_path')
        
        # Validate licensing compliance
        if 'licensing_compliance' in manifest:
            licensing = manifest['licensing_compliance']
            if not isinstance(licensing, dict):
                result['valid'] = False
                result['errors'].append('licensing_compliance must be a dictionary')
            else:
                for license_type, license_info in licensing.items():
                    if not isinstance(license_info, list):
                        result['warnings'].append(f'licensing_compliance.{license_type} should be a list')
        
        # Add general info
        if 'bundle_id' in manifest:
            result['info'].append(f'Bundle ID: {manifest["bundle_id"]}')
        if 'version' in manifest:
            result['info'].append(f'Version: {manifest["version"]}')
            
    except Exception as e:
        result['valid'] = False
        result['errors'].append(f'Unexpected error: {e}')
    
    return result

def validate_all_manifests(directory: str) -> Dict[str, Any]:
    """Validate all manifest files in directory"""
    results = {
        'directory': directory,
        'total_files': 0,
        'valid_files': 0,
        'invalid_files': 0,
        'warnings_count': 0,
        'results': []
    }
    
    if not os.path.exists(directory):
        results['error'] = f'Directory {directory} does not exist'
        return results
    
    # Find manifest files
    manifest_files = []
    for file in os.listdir(directory):
        if file.endswith(('.yml', '.yaml', '.json')) and not file.startswith('README'):
            manifest_files.append(os.path.join(directory, file))
    
    results['total_files'] = len(manifest_files)
    
    if results['total_files'] == 0:
        results['error'] = 'No manifest files found'
        return results
    
    # Validate each file
    for file_path in manifest_files:
        result = validate_manifest_file(file_path)
        results['results'].append(result)
        
        if result['valid']:
            results['valid_files'] += 1
        else:
            results['invalid_files'] += 1
            
        results['warnings_count'] += len(result['warnings'])
    
    return results

def print_results(results: Dict[str, Any]):
    """Print validation results"""
    print(f"\n{'='*60}")
    print(f"OpenZIM Build Manifest Validation Results")
    print(f"{'='*60}")
    print(f"Directory: {results['directory']}")
    print(f"Total files: {results['total_files']}")
    print(f"Valid files: {results['valid_files']}")
    print(f"Invalid files: {results['invalid_files']}")
    print(f"Warnings: {results['warnings_count']}")
    
    if 'error' in results:
        print(f"\nERROR: {results['error']}")
        return
    
    for result in results['results']:
        print(f"\n{'-'*40}")
        print(f"File: {os.path.basename(result['file'])}")
        print(f"Valid: {'✓' if result['valid'] else '✗'}")
        
        if result['errors']:
            print(f"Errors ({len(result['errors'])}):")
            for error in result['errors']:
                print(f"  • {error}")
        
        if result['warnings']:
            print(f"Warnings ({len(result['warnings'])}):")
            for warning in result['warnings']:
                print(f"  • {warning}")
        
        if result['info']:
            print(f"Info:")
            for info in result['info']:
                print(f"  • {info}")

def main():
    """Main validation function"""
    if len(sys.argv) != 2:
        print("Usage: python validate_manifests.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    results = validate_all_manifests(directory)
    print_results(results)
    
    # Exit with error code if any files are invalid
    if results['invalid_files'] > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()