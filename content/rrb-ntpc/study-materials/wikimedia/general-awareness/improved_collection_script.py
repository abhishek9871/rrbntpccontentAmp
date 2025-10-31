#!/usr/bin/env python3
"""
Improved Wikipedia General Awareness Content Collection Script
Fixed image handling, rate limiting, and error recovery.
"""

import os
import json
import requests
import time
import hashlib
import re
from datetime import datetime
from urllib.parse import urljoin, urlparse, quote
from bs4 import BeautifulSoup
import logging

class ImprovedWikipediaCollector:
    def __init__(self, base_dir, delay_between_requests=2):
        self.base_dir = base_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RRB-NTPC-Study-Materials-Collector/2.0 (Educational Research Purpose)',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9'
        })
        self.delay = delay_between_requests
        self.logger = self._setup_logging()
        
        # Rate limiting
        self.last_request_time = 0
        
    def _setup_logging(self):
        """Setup logging for debugging"""
        logger = logging.getLogger('WikipediaCollector')
        logger.setLevel(logging.INFO)
        
        # File handler
        log_file = os.path.join(self.base_dir, 'logs', 'collection.log')
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def _rate_limit(self):
        """Implement rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.delay:
            sleep_time = self.delay - time_since_last
            self.logger.info(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def get_article_content(self, title, language='en'):
        """Get full article content including images"""
        self._rate_limit()
        api_url = f"https://{language}.wikipedia.org/w/api.php"
        
        # First get basic info
        info = self.get_article_info(title, language)
        if not info:
            return None, None
        
        params = {
            'action': 'parse',
            'page': title,
            'prop': 'text|images|links|categories|sections|revid|displaytitle',
            'format': 'json',
            'formatversion': 2,
            'disablepp': True,
            'origin': '*'
        }
        
        try:
            self.logger.info(f"Fetching content for: {title}")
            response = self.session.get(api_url, params=params, timeout=60)
            
            # Handle rate limiting
            if response.status_code == 429:
                self.logger.warning(f"Rate limited for {title}, waiting 60 seconds")
                time.sleep(60)
                return self.get_article_content(title, language)
            
            response.raise_for_status()
            data = response.json()
            
            if 'error' in data:
                raise Exception(f"API Error: {data['error']['info']}")
            
            if 'parse' not in data:
                raise Exception("No parse data in response")
                
            return info, data['parse']
        except Exception as e:
            self.logger.error(f"Error fetching {title}: {e}")
            return None, None
    
    def get_article_info(self, title, language='en'):
        """Get article metadata and revision information"""
        self._rate_limit()
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
            self.logger.info(f"Getting info for: {title}")
            response = self.session.get(api_url, params=params, timeout=30)
            
            # Handle rate limiting
            if response.status_code == 429:
                self.logger.warning(f"Rate limited for info on {title}, waiting 60 seconds")
                time.sleep(60)
                return self.get_article_info(title, language)
            
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
            self.logger.error(f"Error getting info for {title}: {e}")
            return None
    
    def get_image_url(self, image_name):
        """Get full URL for an image"""
        # Clean up the image name
        image_name = image_name.replace(' ', '_')
        
        # Try different Wikimedia Commons URL patterns
        base_urls = [
            'https://commons.wikimedia.org/wiki/File:',
            'https://en.wikipedia.org/wiki/File:',
            'https://upload.wikimedia.org/wikipedia/commons/'
        ]
        
        # For now, return the commons file URL which should work for most images
        return f'https://commons.wikimedia.org/wiki/File:{quote(image_name)}'
    
    def download_image(self, image_info, image_dir):
        """Download image file with proper error handling"""
        try:
            # Handle both string and dict formats
            if isinstance(image_info, str):
                image_name = image_info
                image_title = image_info
            else:
                image_name = image_info.get('title', 'image')
                image_title = image_info.get('title', 'image')
            
            # Get actual image URL from Wikipedia images API
            self._rate_limit()
            api_url = "https://en.wikipedia.org/w/api.php"
            
            params = {
                'action': 'query',
                'titles': image_name,
                'prop': 'imageinfo',
                'iiprop': 'url|size',
                'format': 'json',
                'formatversion': 2,
                'origin': '*'
            }
            
            response = self.session.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if ('query' in data and 'pages' in data['query'] and 
                len(data['query']['pages']) > 0 and 
                'imageinfo' in data['query']['pages'][0] and
                len(data['query']['pages'][0]['imageinfo']) > 0):
                
                image_url = data['query']['pages'][0]['imageinfo'][0].get('url')
                if image_url:
                    self.logger.info(f"Downloading image: {image_name} from {image_url}")
                    
                    # Download the image
                    img_response = self.session.get(image_url, timeout=60)
                    img_response.raise_for_status()
                    
                    # Determine file extension
                    content_type = img_response.headers.get('content-type', '')
                    if 'image/jpeg' in content_type or '.jpg' in image_url:
                        ext = '.jpg'
                    elif 'image/png' in content_type or '.png' in image_url:
                        ext = '.png'
                    elif 'image/gif' in content_type or '.gif' in image_url:
                        ext = '.gif'
                    elif 'image/svg+xml' in content_type or '.svg' in image_url:
                        ext = '.svg'
                    else:
                        ext = '.jpg'  # Default
                    
                    # Create safe filename
                    safe_name = re.sub(r'[^\w\s-]', '', image_name.replace('File:', '').replace(' ', '_'))
                    filename = f"{safe_name}{ext}"
                    filepath = os.path.join(image_dir, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    
                    self.logger.info(f"Successfully downloaded: {filename}")
                    return filename
            
            self.logger.warning(f"Could not get URL for image: {image_name}")
            return None
            
        except Exception as e:
            self.logger.error(f"Error downloading image {image_info}: {e}")
            return None
    
    def collect_article(self, title, category_dir):
        """Collect complete article with HTML, images, and metadata"""
        self.logger.info(f"Starting collection: {title} -> {category_dir}")
        
        # Create category directory
        category_path = os.path.join(self.base_dir, category_dir)
        os.makedirs(category_path, exist_ok=True)
        
        # Get article info and content
        info, parse_data = self.get_article_content(title)
        if not info or not parse_data:
            self.logger.error(f"Failed to get content for {title}")
            return False
        
        # Create article directory
        article_name = re.sub(r'[^\w\s-]', '', title.replace(' ', '_'))
        article_dir = os.path.join(category_path, article_name)
        images_dir = os.path.join(article_dir, 'images')
        os.makedirs(article_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
        
        # Save HTML content
        html_content = parse_data.get('text', '')
        if not html_content:
            self.logger.error(f"No HTML content for {title}")
            return False
        
        # Add attribution header
        attribution_html = f"""<!-- Wikipedia Article: {title} -->
<!-- Revision ID: {info['lastrevid']} -->
<!-- Timestamp: {info['timestamp']} -->
<!-- Source: {info['fullurl']} -->
<!-- License: CC BY-SA 3.0 -->
<!-- Attribution: This work is based on Wikipedia content, licensed under CC BY-SA 3.0 -->
<!-- Contributors: Wikipedia/Wikibooks contributors -->
<!-- Collection Date: {datetime.now().isoformat()} -->

"""
        
        html_filepath = os.path.join(article_dir, f"{article_name}.html")
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(attribution_html)
            f.write(html_content)
        
        # Download images
        images = parse_data.get('images', [])
        downloaded_images = []
        
        self.logger.info(f"Processing {len(images)} images for {title}")
        
        for i, image_info in enumerate(images):
            # Limit to first 20 images to avoid overwhelming the server
            if i >= 20:
                self.logger.info(f"Skipping remaining images (limit reached): {title}")
                break
                
            downloaded = self.download_image(image_info, images_dir)
            if downloaded:
                downloaded_images.append(downloaded)
            
            # Additional rate limiting for image downloads
            time.sleep(1)
        
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
        
        self.logger.info(f"✓ Collected {title} - {len(downloaded_images)} images")
        return True
    
    def collect_batch(self, articles_list, category_dir, max_articles=None):
        """Collect multiple articles in batch with progress tracking"""
        total_articles = len(articles_list)
        if max_articles:
            articles_list = articles_list[:max_articles]
            total_articles = max_articles
        
        success_count = 0
        failed_count = 0
        failed_articles = []
        
        self.logger.info(f"Starting batch collection: {total_articles} articles from {category_dir}")
        
        for i, (title, description) in enumerate(articles_list, 1):
            self.logger.info(f"[{i}/{total_articles}] Processing: {title}")
            
            try:
                if self.collect_article(title, category_dir):
                    success_count += 1
                else:
                    failed_count += 1
                    failed_articles.append(title)
                    
                # Progress update every 5 articles
                if i % 5 == 0:
                    self.logger.info(f"Progress: {success_count} successful, {failed_count} failed")
                    
            except Exception as e:
                self.logger.error(f"Failed to process {title}: {e}")
                failed_count += 1
                failed_articles.append(title)
            
            # Rate limiting between articles
            time.sleep(self.delay)
        
        # Final summary
        self.logger.info(f"\\nBatch Complete: {success_count}/{total_articles} successful, {failed_count} failed")
        if failed_articles:
            self.logger.info(f"Failed articles: {', '.join(failed_articles)}")
        
        return success_count, failed_articles

# Test the improved script
if __name__ == "__main__":
    base_directory = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    collector = ImprovedWikipediaCollector(base_directory, delay_between_requests=3)
    
    # Test with a few articles
    test_articles = [
        ("Bal Gangadhar Tilak", "Indian nationalist leader"),
        ("Lala Lajpat Rai", "Punjabi freedom fighter"),
        ("Bhagat Singh", "Revolutionary freedom fighter"),
        ("List of major rivers of India", "Major Indian rivers")
    ]
    
    print("Testing improved Wikipedia article collection...")
    collector.collect_batch(test_articles, "test_improved_collection")
