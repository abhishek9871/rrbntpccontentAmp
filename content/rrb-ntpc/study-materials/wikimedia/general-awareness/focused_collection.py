#!/usr/bin/env python3
"""
Focused Wikipedia Content Collection - Text Priority
Collects core articles efficiently without image complexity.
"""

import os
import json
import requests
import time
import hashlib
import re
from datetime import datetime
from urllib.parse import quote

class FocusedWikipediaCollector:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RRB-NTPC-Study-Materials-Collector/3.0 (Educational Research Purpose)'
        })
        self.last_request_time = 0
        
    def _rate_limit(self):
        """Implement rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < 2:  # 2 second minimum between requests
            time.sleep(2 - time_since_last)
        
        self.last_request_time = time.time()
    
    def collect_article_text(self, title, category_dir):
        """Collect article text content only"""
        self._rate_limit()
        
        # Get article info
        info = self.get_article_info(title)
        if not info:
            print(f"Failed to get info for {title}")
            return False
        
        # Create directories
        category_path = os.path.join(self.base_dir, category_dir)
        os.makedirs(category_path, exist_ok=True)
        
        article_name = re.sub(r'[^\w\s-]', '', title.replace(' ', '_'))
        article_dir = os.path.join(category_path, article_name)
        os.makedirs(article_dir, exist_ok=True)
        
        # Get article content via Simple API
        try:
            print(f"Collecting: {title}")
            
            # Use Wikipedia's simple API for text extraction
            api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
            
            response = self.session.get(api_url, timeout=30)
            response.raise_for_status()
            summary_data = response.json()
            
            # Get full page content via MediaWiki API
            api_url = "https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'parse',
                'page': title,
                'prop': 'text|sections',
                'format': 'json',
                'formatversion': 2,
                'origin': '*'
            }
            
            response = self.session.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if 'error' in data or 'parse' not in data:
                print(f"Error parsing {title}")
                return False
            
            html_content = data['parse'].get('text', '')
            
            # Create HTML file with attribution
            attribution = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        .attribution {{ background: #f0f0f0; padding: 10px; margin-bottom: 20px; border-radius: 5px; font-size: 0.9em; }}
        .content {{ background: white; padding: 20px; border: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="attribution">
        <strong>Source:</strong> <a href="{info['fullurl']}" target="_blank">{title}</a><br>
        <strong>Revision ID:</strong> {info['lastrevid']}<br>
        <strong>Timestamp:</strong> {info['timestamp']}<br>
        <strong>License:</strong> CC BY-SA 3.0<br>
        <strong>Attribution:</strong> This work is based on Wikipedia content, licensed under CC BY-SA 3.0<br>
        <strong>Contributors:</strong> Wikipedia/Wikibooks contributors<br>
        <strong>Collected:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
    <div class="content">
        {html_content}
    </div>
    <script>
        // Add basic interactivity
        document.addEventListener('DOMContentLoaded', function() {{
            const links = document.querySelectorAll('a[href^="/wiki/"]');
            links.forEach(link => {{
                link.href = link.href.replace('/wiki/', 'https://en.wikipedia.org/wiki/');
                link.target = '_blank';
            }});
        }});
    </script>
</body>
</html>"""
            
            # Save HTML file
            html_filepath = os.path.join(article_dir, f"{article_name}.html")
            with open(html_filepath, 'w', encoding='utf-8') as f:
                f.write(attribution)
            
            # Create metadata
            metadata = {
                'title': title,
                'original_url': info['fullurl'],
                'pageid': info['pageid'],
                'revision_id': info['lastrevid'],
                'timestamp': info['timestamp'],
                'language': 'en',
                'category': category_dir,
                'collected_date': datetime.now().isoformat(),
                'license': 'CC BY-SA 3.0',
                'attribution': 'This work is based on Wikipedia content, licensed under CC BY-SA 3.0. Contributors: Wikipedia/Wikibooks contributors.',
                'files': {
                    'html': f"{article_name}.html"
                },
                'images_count': 0,
                'file_hash': hashlib.md5(html_content.encode()).hexdigest()[:8]
            }
            
            # Save metadata
            metadata_filepath = os.path.join(article_dir, 'metadata.json')
            with open(metadata_filepath, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Successfully collected {title}")
            return True
            
        except Exception as e:
            print(f"Error collecting {title}: {e}")
            return False
    
    def get_article_info(self, title):
        """Get basic article info"""
        self._rate_limit()
        
        try:
            api_url = f"https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'titles': title,
                'prop': 'info|revisions',
                'inprop': 'url',
                'rvlimit': 1,
                'rvprop': 'timestamp|ids',
                'format': 'json',
                'formatversion': 2,
                'origin': '*'
            }
            
            response = self.session.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if 'query' in data and 'pages' in data['query']:
                page = data['query']['pages'][0]
                if 'revisions' in page:
                    revision = page['revisions'][0]
                    return {
                        'pageid': page.get('pageid'),
                        'title': page.get('title'),
                        'fullurl': page.get('fullurl'),
                        'lastrevid': revision.get('revid'),
                        'timestamp': revision.get('timestamp')
                    }
            return None
        except Exception as e:
            print(f"Error getting info for {title}: {e}")
            return None

def get_priority_articles():
    """Get priority articles for systematic collection"""
    return {
        'indian-history': [
            ("History of India", "Complete history overview"),
            ("Timeline of Indian history", "Chronological timeline"),
            ("Medieval India", "Medieval period"),
            ("Outline of ancient India", "Ancient India"),
            ("Indian independence movement", "Freedom struggle"),
            ("List of Indian independence activists", "Freedom fighters"),
            ("Bal Gangadhar Tilak", "Indian nationalist"),
            ("Lala Lajpat Rai", "Freedom fighter"),
            ("Bhagat Singh", "Revolutionary")
        ],
        'geography': [
            ("Geography of India", "Physical geography"),
            ("List of major rivers of India", "Major rivers"),
            ("Himalayas", "Mountain range"),
            ("Western Ghats", "Western mountains"),
            ("Eastern Ghats", "Eastern mountains"),
            ("Indo-Gangetic Plain", "Fertile plain")
        ],
        'polity': [
            ("Constitution of India", "Supreme law"),
            ("Parliament of India", "Legislative body"),
            ("Supreme Court of India", "Highest court"),
            ("Government of India", "Executive branch"),
            ("Kesavananda Bharati v. State of Kerala", "Constitutional case")
        ],
        'science-technology': [
            ("Science and technology in India", "S&T overview"),
            ("ISRO", "Space agency"),
            ("Chandrayaan programme", "Lunar mission"),
            ("Mars Orbiter Mission", "Mars mission"),
            ("Nuclear power in India", "Nuclear energy"),
            ("India's three-stage nuclear power programme", "Nuclear strategy")
        ],
        'economy': [
            ("Economy of India", "Economic overview"),
            ("Banking in India", "Banking system"),
            ("Reserve Bank of India", "Central bank"),
            ("Finance in India", "Financial system")
        ],
        'environment': [
            ("Environmental issues in India", "Environment challenges"),
            ("Wildlife of India", "Biodiversity"),
            ("Environment of India", "Environmental overview"),
            ("Conservation in India", "Conservation efforts")
        ]
    }

def main():
    """Main collection function"""
    base_directory = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    collector = FocusedWikipediaCollector(base_directory)
    
    articles = get_priority_articles()
    
    total_categories = len(articles)
    total_articles = sum(len(category_articles) for category_articles in articles.values())
    
    print(f"Starting focused collection: {total_articles} articles across {total_categories} categories")
    print("=" * 60)
    
    successful_collections = []
    failed_collections = []
    
    category_count = 0
    for category_dir, category_articles in articles.items():
        category_count += 1
        print(f"\\n[{category_count}/{total_categories}] COLLECTING: {category_dir.upper()}")
        print("-" * 40)
        
        for i, (title, description) in enumerate(category_articles, 1):
            print(f"  [{i}/{len(category_articles)}] {title}")
            
            try:
                if collector.collect_article_text(title, category_dir):
                    successful_collections.append((title, category_dir))
                else:
                    failed_collections.append((title, category_dir))
            except Exception as e:
                print(f"    ❌ Error: {e}")
                failed_collections.append((title, category_dir))
            
            # Small delay between articles
            time.sleep(1)
        
        print(f"\\n✓ {category_dir} category completed")
        time.sleep(2)
    
    # Final summary
    print("\\n" + "=" * 60)
    print("🏁 FOCUSED COLLECTION COMPLETE!")
    print(f"✅ Successful: {len(successful_collections)}/{total_articles}")
    print(f"❌ Failed: {len(failed_collections)}/{total_articles}")
    print(f"📊 Success Rate: {(len(successful_collections)/total_articles)*100:.1f}%")
    
    if failed_collections:
        print("\\n❌ Failed articles:")
        for title, category in failed_collections:
            print(f"   - {title} ({category})")
    
    print("=" * 60)
    
    return successful_collections, failed_collections

if __name__ == "__main__":
    main()
