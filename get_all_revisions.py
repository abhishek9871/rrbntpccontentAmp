#!/usr/bin/env python3
"""
Get revision IDs for all Wikipedia pages using requests library
"""

import requests
import json
import time

def get_revision_info(title):
    """Get revision information for a Wikipedia page"""
    try:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'prop': 'revisions',
            'titles': title,
            'rvlimit': 1,
            'rvprop': 'ids|timestamp|comment|user|userid'
        }
        
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        pages = data.get('query', {}).get('pages', {})
        if pages:
            page = list(pages.values())[0]
            if 'revisions' in page:
                revision = page['revisions'][0]
                return {
                    'title': page['title'],
                    'revision_id': revision['revid'],
                    'timestamp': revision['timestamp'],
                    'user': revision['user'],
                    'userid': revision['userid'],
                    'comment': revision.get('comment', '')
                }
        
        return None
        
    except Exception as e:
        print(f"Error getting revision for {title}: {e}")
        return None

def main():
    print("🔍 Getting revision information for all science topics...")
    
    # Lists of all topics
    physics_topics = [
        'Physics', 'Energy', 'Electromagnetism', 'Gravitation', 'Sound'
    ]
    
    chemistry_topics = [
        'Chemistry', 'Chemical bond', 'Periodic table', 'Acid', 'Atom'
    ]
    
    biology_topics = [
        'Biology', 'Human body', 'Cell (biology)', 'Taxonomy (biology)', 'Genetics'
    ]
    
    environmental_topics = [
        'Environmental issues', 'Environmental science', 'Ecosystem', 'Pollution', 'Biodiversity'
    ]
    
    all_topics = {
        'physics': physics_topics,
        'chemistry': chemistry_topics, 
        'biology': biology_topics,
        'environmental_science': environmental_topics
    }
    
    all_revisions = {}
    
    for subject, topics in all_topics.items():
        print(f"\n📚 Processing {subject.upper()}...")
        subject_revisions = {}
        
        for topic in topics:
            print(f"  ⏳ Getting revision for: {topic}")
            revision_info = get_revision_info(topic)
            
            if revision_info:
                subject_revisions[topic] = revision_info
                print(f"    ✅ {topic}: Rev ID {revision_info['revision_id']}")
            else:
                print(f"    ❌ Failed to get revision for: {topic}")
            
            # Rate limiting - wait between requests
            time.sleep(2)
        
        all_revisions[subject] = subject_revisions
    
    # Save all revisions to JSON file
    with open('/workspace/wikimedia-reasoning/all_revisions_complete.json', 'w') as f:
        json.dump(all_revisions, f, indent=2)
    
    print(f"\n🎉 Complete revision data saved to: all_revisions_complete.json")
    
    # Print summary
    total_count = sum(len(revisions) for revisions in all_revisions.values())
    print(f"📊 Total revision IDs retrieved: {total_count}")
    
    return all_revisions

if __name__ == '__main__':
    main()
