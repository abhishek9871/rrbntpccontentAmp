#!/usr/bin/env python3
"""
Quick revision ID getter for individual topics
"""

import requests
import json

def get_single_revision(title):
    """Get revision info for a single title"""
    try:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'prop': 'revisions',
            'titles': title,
            'rvlimit': 1,
            'rvprop': 'ids|timestamp|user'
        }
        
        response = requests.get(url, params=params, timeout=10)
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
                    'user': revision['user']
                }
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    return None

# Test with physics topics
physics_topics = ['Physics', 'Energy']

print("Testing physics topics...")
for topic in physics_topics:
    result = get_single_revision(topic)
    if result:
        print(f"✅ {topic}: {result['revision_id']} at {result['timestamp']}")
    else:
        print(f"❌ Failed: {topic}")
