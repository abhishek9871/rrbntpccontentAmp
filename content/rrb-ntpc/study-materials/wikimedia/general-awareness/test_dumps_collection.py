#!/usr/bin/env python3
"""
Wikipedia Dumps Test Collection Script
====================================

This script implements a test batch of Wikipedia dumps collection
to verify the approach works before scaling up.

Test approach:
1. Download small XML dump files
2. Extract 3 test articles
3. Convert to HTML
4. Test image downloading

Author: MiniMax Agent
Date: 2025-10-30
"""

import os
import sys
import json
import time
import logging
import requests
import bz2
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote
import re
from datetime import datetime
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness/logs/test_dumps_collection.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class TestDumpsCollection:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.dumps_dir = self.base_dir / 'wikipedia_dumps'
        self.temp_dir = self.base_dir / 'temp'
        self.logs_dir = self.base_dir / 'logs'
        
        # Create necessary directories
        for dir_path in [self.dumps_dir, self.temp_dir, self.logs_dir]:
            dir_path.mkdir(exist_ok=True)
            
        # Test batch - small set of articles
        self.test_articles = [
            'Mahatma_Gandhi',
            'Geography_of_India', 
            'Constitution_of_India'
        ]
        
        logger.info(f"Test articles: {self.test_articles}")
        
    def download_small_dump(self):
        """Download a small test dump file"""
        logger.info("Starting small dump download...")
        
        # Use the multistream version for selective extraction
        dump_url = "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream.xml.bz2"
        local_path = self.dumps_dir / 'enwiki-latest-pages-articles-multistream.xml.bz2'
        
        if local_path.exists():
            logger.info("Dump file already exists, skipping download")
            return True
            
        try:
            logger.info(f"Downloading from: {dump_url}")
            
            # Stream download with progress
            response = requests.get(dump_url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            if downloaded % (10 * 1024 * 1024) == 0:  # Every 10MB
                                logger.info(f"Download progress: {progress:.1f}% ({downloaded / (1024*1024):.1f} MB)")
                            
                            # For testing, stop after 50MB
                            if downloaded > 50 * 1024 * 1024:
                                logger.info("Reached 50MB limit for testing")
                                break
            
            logger.info(f"Downloaded {downloaded / (1024*1024):.1f} MB")
            return True
            
        except Exception as e:
            logger.error(f"Error downloading dump: {e}")
            return False
    
    def extract_test_articles(self):
        """Extract specific test articles from dump"""
        logger.info("Extracting test articles from dump...")
        
        dump_path = self.dumps_dir / 'enwiki-latest-pages-articles-multistream.xml.bz2'
        if not dump_path.exists():
            logger.error("Dump file not found")
            return {}
            
        extracted_articles = {}
        
        try:
            with bz2.open(dump_path, 'rt', encoding='utf-8') as f:
                current_article = None
                current_content = []
                current_metadata = {}
                found_count = 0
                
                for line_num, line in enumerate(f):
                    # Log progress every 1000 lines
                    if line_num % 1000 == 0:
                        logger.info(f"Processed {line_num} lines, found {found_count} target articles")
                    
                    # Check for article start
                    if '<page>' in line:
                        current_article = {}
                        current_content = []
                        current_metadata = {}
                        
                    # Extract page title
                    elif '<title>' in line and current_article is not None:
                        title_match = re.search(r'<title>(.*?)</title>', line)
                        if title_match:
                            current_metadata['title'] = title_match.group(1)
                            
                    # Extract page ID
                    elif '<id>' in line and 'page_id' not in current_metadata:
                        id_match = re.search(r'<id>(.*?)</id>', line)
                        if id_match and current_article is not None:
                            current_metadata['page_id'] = id_match.group(1)
                            
                    # Extract revision data
                    elif '<timestamp>' in line and current_article is not None:
                        ts_match = re.search(r'<timestamp>(.*?)</timestamp>', line)
                        if ts_match:
                            current_metadata['timestamp'] = ts_match.group(1)
                            
                    elif '<text' in line and current_article is not None:
                        # Extract wikitext content
                        text_match = re.search(r'<text.*?>(.*)', line, re.DOTALL)
                        if text_match:
                            current_content.append(text_match.group(1))
                        else:
                            content_start = line.split('>', 1)[-1] if '>' in line else ''
                            current_content.append(content_start)
                            
                    elif '</page>' in line and current_article is not None:
                        # End of article, process if it's a target article
                        article_title = current_metadata.get('title', '')
                        
                        if article_title in self.test_articles:
                            logger.info(f"✅ Found target article: {article_title}")
                            
                            # Join all content
                            wikitext = ''.join(current_content)
                            
                            # Calculate content hash for verification
                            content_hash = hashlib.md5(wikitext.encode('utf-8')).hexdigest()
                            
                            extracted_articles[article_title] = {
                                'title': article_title,
                                'page_id': current_metadata.get('page_id'),
                                'timestamp': current_metadata.get('timestamp'),
                                'wikitext': wikitext,
                                'content_hash': content_hash,
                                'source': 'Wikipedia Dump',
                                'line_count': line_num
                            }
                            
                            found_count += 1
                            logger.info(f"Extracted {article_title} (hash: {content_hash[:8]}...)")
                            
                            # Stop if we found all test articles
                            if found_count >= len(self.test_articles):
                                logger.info("Found all test articles, stopping extraction")
                                break
                    
                    # Stop early for testing
                    if line_num > 100000:  # Process first 100k lines for testing
                        logger.info("Reached line limit for testing")
                        break
        
        except Exception as e:
            logger.error(f"Error extracting articles: {e}")
            return {}
            
        logger.info(f"Successfully extracted {len(extracted_articles)} articles")
        return extracted_articles
    
    def wikitext_to_html(self, wikitext, title):
        """Convert wikitext to HTML with better formatting"""
        logger.info(f"Converting {title} from wikitext to HTML...")
        
        try:
            html_content = wikitext
            
            # Remove table of contents and other unwanted elements
            html_content = re.sub(r'__NOTOC__|__TOC__|__FORCETOC__', '', html_content)
            html_content = re.sub(r'__NOEDITSECTION__|__NEWSECTIONLINK__', '', html_content)
            
            # Convert headers
            html_content = re.sub(r'^==== (.+?) ====$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'^=== (.+?) ===$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'^== (.+?) ==$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'^= (.+?) =$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
            
            # Convert bold and italic
            html_content = re.sub(r"'''(.+?)'''", r'<strong>\1</strong>', html_content)
            html_content = re.sub(r"''(.+?)''", r'<em>\1</em>', html_content)
            
            # Convert external links
            html_content = re.sub(r'\[http[^\s\]]+\s+([^\]]+)\]', r'<a href="\1" target="_blank">\2</a>', html_content)
            html_content = re.sub(r'\[http[^\s\]]+\]', r'<a href="\1" target="_blank">\1</a>', html_content)
            
            # Convert internal links
            html_content = re.sub(r'\[\[([^\|]+)\]\]', r'<a href="#">\1</a>', html_content)
            html_content = re.sub(r'\[\[([^\|]+)\|([^\]]+)\]\]', r'<a href="#">\2</a>', html_content)
            
            # Convert lists
            html_content = re.sub(r'^\* (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html_content, flags=re.DOTALL)
            
            # Convert lists with numbers
            html_content = re.sub(r'^# (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
            html_content = re.sub(r'(<li>.*?</li>)', r'<ol>\1</ol>', html_content, flags=re.DOTALL)
            
            # Convert paragraphs
            paragraphs = html_content.split('\n\n')
            html_paragraphs = []
            for para in paragraphs:
                para = para.strip()
                if para and not para.startswith('<') and para != '':
                    html_paragraphs.append(f'<p>{para}</p>')
                elif para:
                    html_paragraphs.append(para)
            
            html_content = '\n\n'.join(html_paragraphs)
            
            # Extract images from wikitext for later download
            images = re.findall(r'\[\[File:([^\|]+)\|', wikitext)
            images.extend(re.findall(r'\[\[Image:([^\|]+)\|', wikitext))
            
            # Wrap in full HTML document
            full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Wikipedia</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #333; border-bottom: 2px solid #ddd; padding-bottom: 10px; }}
        h2 {{ color: #555; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
        h3 {{ color: #777; }}
        h4 {{ color: #999; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        ul, ol {{ margin: 15px 0; padding-left: 30px; }}
        li {{ margin-bottom: 8px; }}
        strong {{ color: #333; }}
        em {{ color: #666; }}
        .attribution {{ background: #f8f9fa; border: 1px solid #a2d9ce; padding: 20px; margin-top: 40px; border-radius: 5px; }}
        .license {{ color: #666; font-style: italic; }}
        .metadata {{ background: #e9ecef; padding: 15px; margin: 20px 0; border-radius: 3px; }}
    </style>
</head>
<body>
    <article>
        <h1>{title.replace('_', ' ')}</h1>
        {html_content}
    </article>
    
    <div class="attribution">
        <h3>Attribution & Licensing</h3>
        <div class="metadata">
            <p><strong>Title:</strong> {title.replace('_', ' ')}</p>
            <p><strong>Source:</strong> <a href="https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" target="_blank">Wikipedia - {title.replace('_', ' ')}</a></p>
            <p><strong>License:</strong> <span class="license">CC BY-SA 3.0</span> - Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply.</p>
            <p><strong>Collection Method:</strong> Wikipedia dumps-based extraction</p>
            <p><strong>Capture Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
        </div>
        <hr>
        <p><em>This content is part of the RRB NTPC General Awareness study materials. All content is used in accordance with Creative Commons licensing terms for educational purposes. Images and other media are subject to their individual licenses.</em></p>
        
        {f'<div class="metadata"><p><strong>Images Referenced:</strong> {", ".join(images[:5])}{"..." if len(images) > 5 else ""}</p></div>' if images else ''}
    </div>
</body>
</html>"""
            
            return full_html, images
            
        except Exception as e:
            logger.error(f"Error converting wikitext to HTML for {title}: {e}")
            error_html = f"""<!DOCTYPE html>
<html><body>
    <h1>{title.replace('_', ' ')}</h1>
    <p>Error converting content: {e}</p>
    <p>This article was processed from Wikipedia dumps but encountered a conversion error.</p>
</body></html>"""
            return error_html, []
    
    def download_wikimedia_commons_images(self, images, article_title):
        """Download images from Wikimedia Commons"""
        logger.info(f"Downloading images for {article_title}: {len(images)} images")
        
        downloaded_images = []
        
        # Create images directory
        article_dir = self.base_dir
        images_dir = article_dir / article_title / 'images'
        images_dir.mkdir(parents=True, exist_ok=True)
        
        for image_name in images[:5]:  # Limit to first 5 images
            try:
                # Get Commons API info
                image_name_clean = image_name.strip().replace(' ', '_')
                commons_api_url = "https://commons.wikimedia.org/w/api.php"
                
                params = {
                    'action': 'query',
                    'format': 'json',
                    'titles': f'File:{image_name_clean}',
                    'prop': 'imageinfo',
                    'iiprop': 'url|size',
                    'iiurlwidth': 800
                }
                
                response = requests.get(commons_api_url, params=params, timeout=10)
                data = response.json()
                
                if 'query' in data and 'pages' in data['query']:
                    page = list(data['query']['pages'].values())[0]
                    
                    if 'imageinfo' in page:
                        image_info = page['imageinfo'][0]
                        
                        if 'thumburl' in image_info:
                            image_url = image_info['thumburl']
                            original_url = image_info.get('url', image_url)
                            
                            # Download thumbnail
                            img_response = requests.get(image_url, timeout=10)
                            img_response.raise_for_status()
                            
                            # Save image
                            image_filename = f"{image_name_clean}.jpg"
                            image_path = images_dir / image_filename
                            
                            with open(image_path, 'wb') as f:
                                f.write(img_response.content)
                            
                            downloaded_images.append({
                                'filename': image_filename,
                                'local_path': str(image_path.relative_to(self.base_dir)),
                                'original_url': original_url,
                                'thumb_url': image_url,
                                'size': len(img_response.content)
                            })
                            
                            logger.info(f"✅ Downloaded: {image_filename}")
                        
            except Exception as e:
                logger.warning(f"Failed to download image {image_name}: {e}")
                
        return downloaded_images
    
    def save_article(self, article_title, html_content, images, metadata):
        """Save article to directory structure"""
        logger.info(f"Saving article: {article_title}")
        
        # Determine domain based on article title
        domain_map = {
            'Mahatma_Gandhi': 'indian-history',
            'Geography_of_India': 'geography',
            'Constitution_of_India': 'polity'
        }
        
        domain = domain_map.get(article_title, 'test_collection')
        
        # Save to correct domain
        domain_dir = self.base_dir / domain
        article_dir = domain_dir / article_title
        
        # Update metadata
        metadata.update({
            'title': article_title.replace('_', ' '),
            'domain': domain,
            'images_downloaded': len(images),
            'collection_method': 'wikipedia_dumps_test',
            'capture_timestamp': datetime.now().isoformat()
        })
        
        try:
            # Ensure directory exists
            article_dir.mkdir(parents=True, exist_ok=True)
            
            # Save HTML
            html_path = article_dir / 'index.html'
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Save metadata
            metadata_path = article_dir / 'metadata.json'
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            # Save image info
            if images:
                images_info = article_dir / 'images' / 'images_info.json'
                images_info.parent.mkdir(exist_ok=True)
                with open(images_info, 'w', encoding='utf-8') as f:
                    json.dump(images, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Saved to: {domain_dir.relative_to(self.base_dir) / article_title}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save article {article_title}: {e}")
            return False
    
    def run_test_collection(self):
        """Run the complete test collection process"""
        logger.info("🚀 Starting Wikipedia dumps test collection...")
        
        success_count = 0
        
        # Step 1: Download dump
        logger.info("Step 1: Downloading Wikipedia dump...")
        if not self.download_small_dump():
            logger.error("Failed to download dump")
            return False
        
        # Step 2: Extract articles
        logger.info("Step 2: Extracting test articles...")
        extracted_articles = self.extract_test_articles()
        
        if not extracted_articles:
            logger.error("No articles extracted")
            return False
        
        # Step 3: Process each article
        logger.info("Step 3: Processing extracted articles...")
        for article_title, article_data in extracted_articles.items():
            logger.info(f"Processing: {article_title}")
            
            try:
                # Convert to HTML
                html_content, images = self.wikitext_to_html(
                    article_data['wikitext'], 
                    article_title
                )
                
                # Download images
                downloaded_images = self.download_wikimedia_commons_images(
                    images, article_title
                )
                
                # Save article
                if self.save_article(article_title, html_content, downloaded_images, article_data):
                    success_count += 1
                    logger.info(f"✅ Successfully processed: {article_title}")
                else:
                    logger.error(f"❌ Failed to save: {article_title}")
                
                # Small delay
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"Error processing {article_title}: {e}")
        
        logger.info(f"🎯 Test collection completed: {success_count}/{len(extracted_articles)} articles successful")
        return success_count > 0

def main():
    """Main execution"""
    base_dir = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    
    try:
        test_collection = TestDumpsCollection(base_dir)
        success = test_collection.run_test_collection()
        
        if success:
            logger.info("🎉 Test dumps collection completed successfully!")
            return 0
        else:
            logger.error("❌ Test collection failed")
            return 1
            
    except Exception as e:
        logger.error(f"Collection failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())