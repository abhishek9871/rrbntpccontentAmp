#!/usr/bin/env python3
"""
License Registry Data Consolidation Script

Consolidates licensing information from DIKSHA, Wikimedia, and practice materials
into a comprehensive license register with enhanced compliance metadata.
"""

import csv
import pandas as pd
import os
from pathlib import Path

class LicenseConsolidator:
    def __init__(self):
        self.consolidated_data = []
        self.source_mapping = {
            'DIKSHA': 'https://diksha.gov.in/',
            'Wikimedia': 'https://www.wikimedia.org/',
            'Mockers': 'https://www.mockers.in/',
            'Testbook': 'https://testbook.com/',
            'Jagran Josh': 'https://www.jagranjosh.com/',
            'RRB': 'https://www.rrb.gov.in/'
        }
        self.license_categories = {
            'CC BY 4.0': {
                'attribution_required': 'Yes',
                'commercial_use_allowed': 'Yes',
                'modifications_allowed': 'Yes',
                'redistribution_permissions': 'Yes'
            },
            'CC BY-SA 3.0': {
                'attribution_required': 'Yes',
                'commercial_use_allowed': 'Yes',
                'modifications_allowed': 'Yes (Share-Alike Required)',
                'redistribution_permissions': 'Yes'
            },
            'CC BY-SA 4.0': {
                'attribution_required': 'Yes',
                'commercial_use_allowed': 'Yes',
                'modifications_allowed': 'Yes (Share-Alike Required)',
                'redistribution_permissions': 'Yes'
            },
            'All Rights Reserved': {
                'attribution_required': 'Yes',
                'commercial_use_allowed': 'No',
                'modifications_allowed': 'No',
                'redistribution_permissions': 'No (Permission Required)'
            },
            'Government Work': {
                'attribution_required': 'Yes',
                'commercial_use_allowed': 'Yes',
                'modifications_allowed': 'Yes',
                'redistribution_permissions': 'Yes (with attribution)'
            }
        }
    
    def categorize_content(self, title, source_portal, content_type=''):
        """Categorize content based on title and source"""
        title_lower = title.lower()
        
        # Educational Content Categories
        if any(word in title_lower for word in ['class', 'textbook', 'ncert', 'economics', 'geography', 'history', 'politics', 'science']):
            return 'NCERT Educational Content'
        elif any(word in title_lower for word in ['mathematics', 'algebra', 'geometry', 'statistics', 'trigonometry']):
            return 'Mathematics Education'
        elif any(word in title_lower for word in ['reasoning', 'mental ability', 'logical', 'verbal', 'non-verbal']):
            return 'Reasoning & Mental Ability'
        elif any(word in title_lower for word in ['computer', 'programming', 'web development', 'javascript', 'html']):
            return 'Computer Science & Programming'
        elif any(word in title_lower for word in ['mock', 'practice', 'sample', 'previous year', 'exam']):
            return 'Exam Practice Materials'
        elif any(word in title_lower for word in ['railway', 'rrb', 'current affairs', 'general knowledge']):
            return 'General Awareness'
        elif any(word in title_lower for word in ['platform', 'diksha', 'login', 'download', 'mobile']):
            return 'Platform Documentation'
        elif any(word in title_lower for word in ['unesco', 'framework', 'policy']):
            return 'Policy Documentation'
        else:
            return 'Educational Content'
    
    def extract_contact_info(self, source_portal, license_type):
        """Extract or generate contact information"""
        if source_portal:
            portal_lower = source_portal.lower()
            
            if 'diksha' in portal_lower or 'ncert' in portal_lower:
                return "NCERT, Ministry of Education, Government of India"
            elif 'wikimedia' in portal_lower or 'wikipedia' in portal_lower:
                return "Wikimedia Foundation"
            elif 'mockers' in portal_lower:
                return "Mockers.in Educational Platform"
            elif 'testbook' in portal_lower:
                return "Testbook Edutech Pvt Ltd"
            elif 'jagran josh' in portal_lower:
                return "Jagran Prakashan Limited"
            elif 'rrb' in portal_lower:
                return f"Railway Recruitment Board ({source_portal.split('(')[-1].split(')')[0] if '(' in source_portal else 'India'})"
            elif 'government' in portal_lower:
                return "Government of India Portal"
            else:
                return source_portal
        else:
            return "Content Publisher"
    
    def generate_compliance_notes(self, license_type, usage_restrictions, redistribution_permissions):
        """Generate detailed compliance notes"""
        notes = []
        
        if license_type == 'CC BY 4.0':
            notes.append("Attribution required: Title, Author, Source, License (TASL)")
            notes.append("Commercial use permitted with proper attribution")
            notes.append("Modifications allowed and encouraged")
            if usage_restrictions:
                notes.append(f"Usage: {usage_restrictions}")
        elif 'CC BY-SA' in license_type:
            notes.append("Attribution required: Title, Author, Source, License (TASL)")
            notes.append("Share-Alike: Derivatives must use same license")
            notes.append("Commercial use permitted with attribution and share-alike")
            if usage_restrictions:
                notes.append(f"Usage: {usage_restrictions}")
        elif license_type == 'All Rights Reserved':
            notes.append("No redistribution without written permission")
            notes.append("Personal use only - educational/commercial use prohibited")
            if usage_restrictions:
                notes.append(f"Usage: {usage_restrictions}")
        elif license_type == 'Government Work':
            notes.append("Attribution to issuing government body required")
            notes.append("Public use generally permitted")
            if usage_restrictions:
                notes.append(f"Usage: {usage_restrictions}")
        
        if redistribution_permissions:
            if 'not' in redistribution_permissions.lower():
                notes.append("Redistribution restricted")
            elif 'permission' in redistribution_permissions.lower():
                notes.append("Redistribution requires explicit permission")
            else:
                notes.append(f"Redistribution: {redistribution_permissions}")
        
        return " | ".join(notes)
    
    def process_diksha_data(self):
        """Process DIKSHA licensing data"""
        file_path = '/workspace/licensing/diksha_license_register.csv'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                content_category = self.categorize_content(
                    row['content_title'], 
                    'DIKSHA Platform'
                )
                
                license_info = self.license_categories.get(row['license_type'], {
                    'attribution_required': 'Yes',
                    'commercial_use_allowed': 'Yes',
                    'modifications_allowed': 'Yes',
                    'redistribution_permissions': 'Yes'
                })
                
                entry = {
                    'content_category': content_category,
                    'license_type': row['license_type'],
                    'attribution_required': license_info['attribution_required'],
                    'redistribution_permissions': license_info['redistribution_permissions'],
                    'commercial_use_allowed': license_info['commercial_use_allowed'],
                    'modifications_allowed': license_info['modifications_allowed'],
                    'contact_info': self.extract_contact_info('DIKSHA (NCERT)', row['license_type']),
                    'source_url': 'https://diksha.gov.in/',
                    'legal_compliance_notes': self.generate_compliance_notes(
                        row['license_type'],
                        row['usage_restrictions'],
                        row['redistribution_permissions']
                    )
                }
                self.consolidated_data.append(entry)
    
    def process_practice_materials_data(self):
        """Process practice materials licensing data"""
        file_path = '/workspace/practice-licensing/metadata/practice_materials_license_register.csv'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                content_category = self.categorize_content(
                    row['content_title'],
                    row['source_portal']
                )
                
                license_info = self.license_categories.get(row['license_type'], {
                    'attribution_required': 'Yes',
                    'commercial_use_allowed': 'Unknown',
                    'modifications_allowed': 'Unknown',
                    'redistribution_permissions': 'Unknown'
                })
                
                # Update redistribution permissions based on actual data
                if row['redistribution_permissions'].lower() == 'no redistribution permitted':
                    license_info['redistribution_permissions'] = 'No'
                elif 'permission' in row['redistribution_permissions'].lower():
                    license_info['redistribution_permissions'] = 'Permission Required'
                elif 'permitted' in row['redistribution_permissions'].lower():
                    license_info['redistribution_permissions'] = 'Yes'
                
                entry = {
                    'content_category': content_category,
                    'license_type': row['license_type'],
                    'attribution_required': license_info['attribution_required'],
                    'redistribution_permissions': license_info['redistribution_permissions'],
                    'commercial_use_allowed': license_info['commercial_use_allowed'],
                    'modifications_allowed': license_info['modifications_allowed'],
                    'contact_info': self.extract_contact_info(row['source_portal'], row['license_type']),
                    'source_url': self.extract_source_url(row['source_portal']),
                    'legal_compliance_notes': self.generate_compliance_notes(
                        row['license_type'],
                        row['usage_restrictions'],
                        row['redistribution_permissions']
                    )
                }
                self.consolidated_data.append(entry)
    
    def process_wikimedia_data(self):
        """Process Wikimedia licensing data"""
        file_path = '/workspace/wikimedia-licensing/metadata/wikimedia_license_register.csv'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                content_category = self.categorize_content(
                    row['page_title'],
                    'Wikimedia Foundation'
                )
                
                license_info = self.license_categories.get(row['license_type'], {
                    'attribution_required': 'Yes',
                    'commercial_use_allowed': 'Yes',
                    'modifications_allowed': 'Yes (Share-Alike Required)',
                    'redistribution_permissions': 'Yes'
                })
                
                # Extract specific source URL from attribution text
                attribution_text = row.get('specific_attribution_text_required', '')
                source_url = self.extract_wikimedia_url(attribution_text)
                
                entry = {
                    'content_category': content_category,
                    'license_type': row['license_type'],
                    'attribution_required': license_info['attribution_required'],
                    'redistribution_permissions': license_info['redistribution_permissions'],
                    'commercial_use_allowed': license_info['commercial_use_allowed'],
                    'modifications_allowed': license_info['modifications_allowed'],
                    'contact_info': 'Wikimedia Foundation',
                    'source_url': source_url,
                    'legal_compliance_notes': self.generate_compliance_notes(
                        row['license_type'],
                        row['share_alike_obligations'],
                        'Yes'
                    )
                }
                self.consolidated_data.append(entry)
    
    def extract_source_url(self, source_portal):
        """Extract source URL based on portal"""
        if not source_portal:
            return ''
        
        portal_lower = source_portal.lower()
        
        for portal_key, url in self.source_mapping.items():
            if portal_key.lower() in portal_lower:
                return url
        
        return ''
    
    def extract_wikimedia_url(self, attribution_text):
        """Extract URL from Wikimedia attribution text"""
        if 'https://' in attribution_text:
            import re
            urls = re.findall(r'https://[^\s\)]+', attribution_text)
            return urls[0] if urls else 'https://en.wikipedia.org/'
        return 'https://en.wikipedia.org/'
    
    def save_consolidated_data(self, output_path):
        """Save consolidated data to CSV"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            if self.consolidated_data:
                fieldnames = [
                    'content_category', 'license_type', 'attribution_required',
                    'redistribution_permissions', 'commercial_use_allowed',
                    'modifications_allowed', 'contact_info', 'source_url',
                    'legal_compliance_notes'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.consolidated_data)
        
        print(f"Consolidated {len(self.consolidated_data)} license entries to {output_path}")
    
    def generate_summary(self):
        """Generate summary statistics"""
        categories = {}
        licenses = {}
        
        for entry in self.consolidated_data:
            # Count categories
            cat = entry['content_category']
            categories[cat] = categories.get(cat, 0) + 1
            
            # Count licenses
            license_type = entry['license_type']
            licenses[license_type] = licenses.get(license_type, 0) + 1
        
        print("\n=== LICENSE REGISTRY SUMMARY ===")
        print(f"Total Entries: {len(self.consolidated_data)}")
        
        print("\nContent Categories:")
        for cat, count in sorted(categories.items()):
            print(f"  {cat}: {count}")
        
        print("\nLicense Types:")
        for license_type, count in sorted(licenses.items()):
            print(f"  {license_type}: {count}")
    
    def consolidate_all(self):
        """Main consolidation process"""
        print("Starting license data consolidation...")
        
        print("Processing DIKSHA data...")
        self.process_diksha_data()
        
        print("Processing practice materials data...")
        self.process_practice_materials_data()
        
        print("Processing Wikimedia data...")
        self.process_wikimedia_data()
        
        # Remove duplicates based on content title and license type
        seen = set()
        deduplicated_data = []
        for entry in self.consolidated_data:
            key = (entry['content_category'], entry['license_type'], entry['source_url'])
            if key not in seen:
                seen.add(key)
                deduplicated_data.append(entry)
        
        self.consolidated_data = deduplicated_data
        
        self.generate_summary()
        
        output_path = '/workspace/license-registry/metadata/license_register.csv'
        self.save_consolidated_data(output_path)
        
        return output_path

if __name__ == "__main__":
    consolidator = LicenseConsolidator()
    output_file = consolidator.consolidate_all()
    print(f"\nConsolidation complete! Output saved to: {output_file}")
