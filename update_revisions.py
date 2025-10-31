#!/usr/bin/env python3
"""
Update environmental science HTML files with proper revision IDs and metadata
"""

import re
import os

# Revision data for environmental science topics
revision_data = {
    'environmental_science.html': {
        'revision_id': '1314325017',
        'timestamp': '2025-09-30T20:43:11Z',
        'parent_revision': '1313607560',
        'editor': '69.172.158.232 (Anonymous)',
        'editor_id': '0'
    },
    'ecosystem.html': {
        'revision_id': '1313967029',
        'timestamp': '2025-09-29T01:34:27Z',
        'parent_revision': '1309683107',
        'editor': 'Monkbot',
        'editor_id': '20483999'
    },
    'pollution.html': {
        'revision_id': '1317950916',
        'timestamp': '2025-10-21T00:49:56Z',
        'parent_revision': '1314786565',
        'editor': 'Omnipaedista',
        'editor_id': '8524693'
    },
    'biodiversity.html': {
        'revision_id': '1317660757',
        'timestamp': '2025-10-19T08:43:21Z',
        'parent_revision': '1315886073',
        'editor': 'Vycl1994',
        'editor_id': '19014806'
    }
}

def update_html_file(filepath, file_data):
    """Update HTML file with revision information"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the revision ID section
        old_revision_section = '''        <div style="margin: 10px 0;">
            <strong>Revision ID:</strong> To be documented from Wikimedia dumps
        </div>'''
        
        new_revision_section = f'''        <div style="margin: 10px 0;">
            <strong>Revision ID:</strong> {file_data['revision_id']} (Timestamp: {file_data['timestamp']})
        </div>
        
        <div style="margin: 10px 0;">
            <strong>Parent Revision:</strong> {file_data['parent_revision']}
        </div>
        
        <div style="margin: 10px 0;">
            <strong>Editor:</strong> {file_data['editor']} (User ID: {file_data['editor_id']})
        </div>'''
        
        content = content.replace(old_revision_section, new_revision_section)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

def main():
    base_path = '/workspace/wikimedia-reasoning/content/rrb-ntpc/study-materials/wikimedia/science/environmental-science/'
    
    updated_count = 0
    for filename, data in revision_data.items():
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            if update_html_file(filepath, data):
                updated_count += 1
        else:
            print(f"⚠️  File not found: {filepath}")
    
    print(f"\n🎯 Successfully updated {updated_count} files with revision IDs")

if __name__ == '__main__':
    main()
