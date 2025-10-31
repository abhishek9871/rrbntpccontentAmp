#!/usr/bin/env python3
"""
Complete Revision ID Documentation for All Subjects
Retrieves revision IDs for Physics, Chemistry, Biology with proper rate limiting
"""

import requests
import json
import time
from pathlib import Path

# All remaining topics that need revision IDs
TARGET_TOPICS = [
    # Physics (5 topics)
    {"title": "Physics", "subject": "physics"},
    {"title": "Energy", "subject": "physics"},  
    {"title": "Electromagnetism", "subject": "physics"},
    {"title": "Gravitation", "subject": "physics"},
    {"title": "Sound", "subject": "physics"},
    
    # Chemistry (5 topics)
    {"title": "Chemistry", "subject": "chemistry"},
    {"title": "Chemical bond", "subject": "chemistry"},
    {"title": "Periodic table", "subject": "chemistry"},
    {"title": "Acid", "subject": "chemistry"},
    {"title": "Atom", "subject": "chemistry"},
    
    # Biology (5 topics)
    {"title": "Biology", "subject": "biology"},
    {"title": "Human body", "subject": "biology"},
    {"title": "Cell (biology)", "subject": "biology"},
    {"title": "Taxonomy (biology)", "subject": "biology"},
    {"title": "Genetics", "subject": "biology"}
]

# Topics that already have revision IDs (Environmental Science)
COMPLETED_TOPICS = [
    {"title": "Environmental issues", "revision_id": "1310975708", "timestamp": "2025-09-12T16:58:26Z"},
    {"title": "Environmental science", "revision_id": "1314325017", "timestamp": "2025-09-17T18:17:57Z"},
    {"title": "Ecosystem", "revision_id": "1313967029", "timestamp": "2025-09-16T09:54:30Z"},
    {"title": "Pollution", "revision_id": "1317950916", "timestamp": "2025-10-23T15:22:41Z"},
    {"title": "Biodiversity", "revision_id": "1317660757", "timestamp": "2025-10-20T12:45:33Z"}
]

def get_revision_id(title):
    """Get revision ID for a Wikipedia page with rate limiting"""
    try:
        # Wikipedia API endpoint for latest revision
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'format': 'json',
            'prop': 'revisions',
            'titles': title,
            'rvlimit': 1,
            'rvprop': 'ids|timestamp|comment|user|userid',
            'rvdir': 'older',  # Get latest revision (oldest in this case)
            'formatversion': 2
        }
        
        print(f"Getting revision for: {title}")
        response = requests.get(url, params=params, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if 'query' in data and 'pages' in data['query']:
                page = data['query']['pages'][0]
                if 'revisions' in page and len(page['revisions']) > 0:
                    revision = page['revisions'][0]
                    return {
                        "title": title,
                        "revision_id": revision['revid'],
                        "timestamp": revision['timestamp'],
                        "user": revision.get('user', 'Unknown'),
                        "parent_id": revision.get('parentid', 'N/A'),
                        "comment": revision.get('comment', 'N/A')
                    }
                else:
                    print(f"No revisions found for {title}")
                    return None
            else:
                print(f"Invalid response format for {title}")
                return None
        else:
            print(f"HTTP {response.status_code} for {title}")
            return None
            
    except Exception as e:
        print(f"Error getting revision for {title}: {str(e)}")
        return None

def main():
    """Get revision IDs for all remaining topics"""
    print("=" * 60)
    print("COMPLETING REVISION ID DOCUMENTATION FOR ALL SUBJECTS")
    print("=" * 60)
    
    all_results = []
    
    # Add already completed Environmental Science topics
    for topic in COMPLETED_TOPICS:
        result = {
            "title": topic["title"],
            "revision_id": topic["revision_id"],
            "timestamp": topic["timestamp"],
            "user": "Recorded earlier",
            "subject": "environmental-science",
            "status": "completed"
        }
        all_results.append(result)
        print(f"✓ {topic['title']} (Environmental Science) - {topic['revision_id']}")
    
    # Get revision IDs for remaining topics
    for i, topic in enumerate(TARGET_TOPICS):
        print(f"\n--- {i+1}/{len(TARGET_TOPICS)}: {topic['title']} ({topic['subject']}) ---")
        
        result = get_revision_id(topic['title'])
        
        if result:
            result['subject'] = topic['subject']
            result['status'] = 'retrieved'
            all_results.append(result)
            print(f"✓ Retrieved: {result['revision_id']} ({result['timestamp']})")
        else:
            print(f"✗ Failed to retrieve revision ID for {topic['title']}")
            result = {
                "title": topic['title'],
                "revision_id": "FAILED",
                "timestamp": "N/A",
                "user": "N/A",
                "subject": topic['subject'],
                "status": "failed"
            }
            all_results.append(result)
        
        # Rate limiting: wait 2-3 seconds between requests
        if i < len(TARGET_TOPICS) - 1:  # Don't wait after last request
            time.sleep(3)
            print("   Waiting 3 seconds to avoid rate limiting...")
    
    # Save all results to file
    output_file = "/workspace/wikimedia-reasoning/all_revision_ids_complete.json"
    with open(output_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n" + "=" * 60)
    print("REVISION ID RETRIEVAL COMPLETED")
    print("=" * 60)
    print(f"Total topics processed: {len(all_results)}")
    print(f"Successful retrievals: {len([r for r in all_results if r['status'] == 'retrieved'])}")
    print(f"Already completed: {len([r for r in all_results if r['status'] == 'completed'])}")
    print(f"Failed: {len([r for r in all_results if r['status'] == 'failed'])}")
    print(f"Results saved to: {output_file}")
    
    # Summary by subject
    print("\nSUMMARY BY SUBJECT:")
    subjects = ['physics', 'chemistry', 'biology', 'environmental-science']
    for subject in subjects:
        subject_results = [r for r in all_results if r['subject'] == subject]
        completed = len([r for r in subject_results if r['status'] in ['retrieved', 'completed']])
        total = len(subject_results)
        print(f"  {subject.capitalize()}: {completed}/{total} completed")

if __name__ == "__main__":
    main()