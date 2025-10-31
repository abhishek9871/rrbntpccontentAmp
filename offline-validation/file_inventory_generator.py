#!/usr/bin/env python3
"""
Offline Validation File Inventory Generator
Generates comprehensive inventory of all content files and selects 10% samples for validation
"""

import os
import json
import random
from collections import defaultdict
from pathlib import Path
import csv

def generate_file_inventory():
    """Generate complete file inventory organized by category"""
    
    # Define content directories
    content_dirs = {
        'previous_papers': '/workspace/content/rrb-ntpc/previous-papers',
        'study_materials_diksha': '/workspace/diksha-ga',
        'study_materials_wikimedia': '/workspace/content/rrb-ntpc/study-materials/wikimedia',
        'practice_sets': '/workspace/practice-ga',
        'current_affairs': '/workspace/current-affairs',
        'metadata_files': '/workspace/metadata'
    }
    
    inventory = {
        'total_files': 0,
        'categories': {},
        'sample_files': {},
        'file_types': defaultdict(int)
    }
    
    # Generate inventory for each category
    for category, directory in content_dirs.items():
        print(f"Processing {category}: {directory}")
        
        if not os.path.exists(directory):
            print(f"Warning: Directory {directory} does not exist")
            continue
            
        category_files = []
        
        # Walk through directory and collect files
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                
                # Get file extension
                ext = os.path.splitext(file)[1].lower()
                
                # Get file size
                try:
                    size = os.path.getsize(file_path)
                except OSError:
                    size = 0
                
                file_info = {
                    'path': file_path,
                    'relative_path': rel_path,
                    'name': file,
                    'extension': ext,
                    'size': size,
                    'category': category
                }
                
                category_files.append(file_info)
                inventory['file_types'][ext] += 1
        
        inventory['categories'][category] = {
            'directory': directory,
            'total_files': len(category_files),
            'files': category_files
        }
        
        inventory['total_files'] += len(category_files)
        
        # Calculate 10% sample
        sample_size = max(1, len(category_files) // 10)
        if len(category_files) > 0:
            sample_files = random.sample(category_files, min(sample_size, len(category_files)))
            inventory['sample_files'][category] = sample_files
        
        print(f"  Found {len(category_files)} files, sample: {len(sample_files) if 'sample_files' in locals() else 0}")
    
    return inventory

def save_inventory(inventory, output_file):
    """Save inventory to JSON file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

def save_sample_csv(inventory, output_file):
    """Save sample files to CSV for easy review"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'File Name', 'Relative Path', 'Extension', 'Size (bytes)', 'Type'])
        
        for category, sample_files in inventory['sample_files'].items():
            for file_info in sample_files:
                writer.writerow([
                    category,
                    file_info['name'],
                    file_info['relative_path'],
                    file_info['extension'],
                    file_info['size'],
                    'Sample'
                ])

def print_summary(inventory):
    """Print inventory summary"""
    print("\n" + "="*60)
    print("FILE INVENTORY SUMMARY")
    print("="*60)
    
    print(f"Total Files: {inventory['total_files']}")
    print(f"\nCategories:")
    
    for category, data in inventory['categories'].items():
        sample_count = len(inventory['sample_files'].get(category, []))
        print(f"  {category}: {data['total_files']} files (sample: {sample_count})")
    
    print(f"\nFile Types Distribution:")
    for ext, count in sorted(inventory['file_types'].items()):
        print(f"  {ext or 'no extension'}: {count} files")
    
    total_sample = sum(len(samples) for samples in inventory['sample_files'].values())
    print(f"\nTotal Sample Files: {total_sample}")
    print(f"Sample Percentage: {(total_sample/inventory['total_files']*100):.1f}%")

if __name__ == "__main__":
    print("Generating file inventory for offline validation...")
    
    # Set random seed for reproducible sampling
    random.seed(42)
    
    # Generate inventory
    inventory = generate_file_inventory()
    
    # Save results
    inventory_file = '/workspace/offline-validation/sample_inventory.json'
    csv_file = '/workspace/offline-validation/sample_files.csv'
    
    save_inventory(inventory, inventory_file)
    save_sample_csv(inventory, csv_file)
    
    # Print summary
    print_summary(inventory)
    
    print(f"\nInventory saved to: {inventory_file}")
    print(f"Sample CSV saved to: {csv_file}")
