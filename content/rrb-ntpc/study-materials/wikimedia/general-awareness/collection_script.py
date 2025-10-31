#!/usr/bin/env python3
"""
Wikimedia General Awareness Content Collection Script
Collects Wikipedia articles with full HTML, assets, and metadata for RRB NTPC study materials.
"""

import os
import json
import requests
import time
import hashlib
from datetime import datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

class WikipediaCollector:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RRB-NTPC-Study-Materials-Collector/1.0 (Research Purpose)'
        })
        
    def get_article_html(self, title, language='en'):
        """Get Wikipedia article HTML using MediaWiki API"""
        api_url = f"https://{language}.wikipedia.org/w/api.php"
        
        params = {
            'action': 'parse',
            'page': title,
            'prop': 'text|images|parsetree|categories|sections|links',
            'format': 'json',
            'formatversion': 2,
            'disablepp': True,
            'origin': '*'
        }
        
        try:
            response = self.session.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if 'error' in data:
                raise Exception(f"API Error: {data['error']['info']}")
            
            if 'parse' not in data:
                raise Exception("No parse data in response")
                
            return data['parse']
        except Exception as e:
            print(f"Error fetching {title}: {e}")
            return None
    
    def get_article_info(self, title, language='en'):
        """Get article metadata and revision information"""
        api_url = f"https://{language}.wikipedia.org/w/api.php"
        
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
        
        try:
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
    
    def download_image(self, image_url, image_dir, image_name):
        """Download image file"""
        try:
            response = self.session.get(image_url, timeout=30)
            response.raise_for_status()
            
            # Determine file extension from content-type or URL
            content_type = response.headers.get('content-type', '')
            if 'image/jpeg' in content_type or '.jpg' in image_url:
                ext = '.jpg'
            elif 'image/png' in content_type or '.png' in image_url:
                ext = '.png'
            elif 'image/gif' in content_type or '.gif' in image_url:
                ext = '.gif'
            elif 'image/svg+xml' in content_type or '.svg' in image_url:
                ext = '.svg'
            else:
                ext = os.path.splitext(image_url)[1]
                if not ext:
                    ext = '.bin'  # fallback
            
            filename = f"{image_name}{ext}"
            filepath = os.path.join(image_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            return filename
        except Exception as e:
            print(f"Error downloading image {image_url}: {e}")
            return None
    
    def collect_article(self, title, category_dir):
        """Collect complete article with HTML, images, and metadata"""
        print(f"Collecting: {title}")
        
        # Create category directory
        category_path = os.path.join(self.base_dir, category_dir)
        os.makedirs(category_path, exist_ok=True)
        
        # Get article info
        info = self.get_article_info(title)
        if not info:
            print(f"Failed to get info for {title}")
            return False
        
        # Get article content
        parse_data = self.get_article_html(title)
        if not parse_data:
            print(f"Failed to get content for {title}")
            return False
        
        # Create directories
        article_name = re.sub(r'[^\w\s-]', '', title.replace(' ', '_'))
        article_dir = os.path.join(category_path, article_name)
        images_dir = os.path.join(article_dir, 'images')
        os.makedirs(article_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
        
        # Save HTML content
        html_content = parse_data.get('text', '')
        html_filepath = os.path.join(article_dir, f"{article_name}.html")
        
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(f"<!-- Wikipedia Article: {title} -->\n")
            f.write(f"<!-- Revision ID: {info['lastrevid']} -->\n")
            f.write(f"<!-- Timestamp: {info['timestamp']} -->\n")
            f.write(f"<!-- Source: {info['fullurl']} -->\n")
            f.write(f"<!-- License: CC BY-SA 3.0 -->\n")
            f.write(f"<!-- Attribution: This work is based on Wikipedia content, licensed under CC BY-SA 3.0 -->\n")
            f.write(f"<!-- Contributors: Wikipedia/Wikibooks contributors -->\n")
            f.write(html_content)
        
        # Download images
        images = parse_data.get('images', [])
        downloaded_images = []
        
        for i, image_info in enumerate(images):
            # Handle both string and dict formats
            if isinstance(image_info, str):
                image_url = image_info
                image_title = f"image_{i}"
            else:
                image_url = image_info.get('url', '')
                image_title = image_info.get('title', f'image_{i}')
            
            if image_url:
                # Convert URL to thumbnail if available
                if 'thumb/' in image_url:
                    image_name = f"img_{i:03d}_{image_title.replace(' ', '_')}"
                else:
                    image_name = f"img_{i:03d}_{image_title.replace(' ', '_')}"
                
                downloaded = self.download_image(image_url, images_dir, image_name)
                if downloaded:
                    downloaded_images.append(downloaded)
        
        # Create metadata file
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
                'html': f"{article_name}.html",
                'images': downloaded_images
            },
            'images_count': len(downloaded_images),
            'file_hash': hashlib.md5(html_content.encode()).hexdigest()[:8]
        }
        
        metadata_filepath = os.path.join(article_dir, 'metadata.json')
        with open(metadata_filepath, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Collected {title} - {len(downloaded_images)} images")
        return True
    
    def collect_batch(self, articles_list, category_dir):
        """Collect multiple articles in batch"""
        success_count = 0
        total_count = len(articles_list)
        
        for i, (title, description) in enumerate(articles_list, 1):
            print(f"[{i}/{total_count}] Collecting: {title}")
            
            if self.collect_article(title, category_dir):
                success_count += 1
            
            # Rate limiting
            time.sleep(2)
        
        print(f"\\nBatch Complete: {success_count}/{total_count} articles collected successfully")
        return success_count

# Example usage and test collection
if __name__ == "__main__":
    base_directory = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    collector = WikipediaCollector(base_directory)
    
    # Test with a few sample articles
    test_articles = [
        ("Constitution of India", "Primary source for Indian Constitution"),
        ("Mahatma Gandhi", "Indian independence leader"),
        ("Geography of India", "Physical and geographical overview"),
        ("ISRO", "Indian space program")
    ]
    
    print("Testing Wikipedia article collection...")
    collector.collect_batch(test_articles, "test_collection")
