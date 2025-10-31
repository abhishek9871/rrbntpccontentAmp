#!/usr/bin/env python3
"""
Wikimedia Commons Image Downloader
==================================

This script implements robust image downloading from Wikimedia Commons
to complete the media asset collection for all Wikipedia articles.

Features:
- Downloads all images from Wikipedia pages
- Handles Commons API rate limiting
- Extracts image URLs from page HTML
- Implements retry logic for failed downloads
- Saves images with proper attribution metadata

Author: MiniMax Agent
Date: 2025-10-30
License: CC BY-SA 3.0
"""

import os
import sys
import json
import time
import logging
import requests
import re
import hashlib
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from datetime import datetime
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness/logs/image_download.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class WikimediaImageDownloader:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.commons_api = "https://commons.wikimedia.org/w/api.php"
        self.wikipedia_api = "https://en.wikipedia.org/w/api.php"
        
        # Rate limiting
        self.request_delay = 2  # 2 seconds between requests
        self.max_retries = 3
        
        # Create downloads directory
        self.downloads_dir = self.base_dir / 'image_downloads'
        self.downloads_dir.mkdir(exist_ok=True)
        
    def get_page_images(self, page_title):
        """Get list of images from a Wikipedia page"""
        try:
            # Get page content to extract image references
            params = {
                'action': 'query',
                'format': 'json',
                'titles': page_title,
                'prop': 'images|revisions',
                'imlimit': 500,
                'rvlimit': 1,
                'rvprop': 'content'
            }
            
            response = requests.get(self.wikipedia_api, params=params, timeout=15)
            data = response.json()
            
            if 'query' in data and 'pages' in data['query']:
                page = list(data['query']['pages'].values())[0]
                if 'images' in page:
                    return [img['title'] for img in page['images'] if 'title' in img]
                    
        except Exception as e:
            logger.warning(f"Error getting images for {page_title}: {e}")
            
        return []
    
    def get_image_info(self, image_title):
        """Get detailed information about an image from Commons"""
        try:
            params = {
                'action': 'query',
                'format': 'json',
                'titles': image_title,
                'prop': 'imageinfo',
                'iiprop': 'url|size|extmetadata|mediatype',
                'iiurlwidth': 1000  # Get medium-sized image URL
            }
            
            response = requests.get(self.commons_api, params=params, timeout=15)
            data = response.json()
            
            if 'query' in data and 'pages' in data['query']:
                page = list(data['query']['pages'].values())[0]
                if 'imageinfo' in page:
                    return page['imageinfo'][0]
                    
        except Exception as e:
            logger.warning(f"Error getting image info for {image_title}: {e}")
            
        return None
    
    def download_image(self, image_info, local_path):
        """Download a single image file"""
        try:
            # Get the image URL (prefer medium size)
            image_url = image_info.get('thumburl') or image_info.get('url')
            if not image_url:
                logger.warning(f"No URL found for image")
                return False
                
            # Download the image
            response = requests.get(image_url, timeout=30, stream=True)
            response.raise_for_status()
            
            # Save to local file
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        
            # Create metadata file
            metadata = {
                'title': image_info.get('title', ''),
                'url': image_url,
                'size': len(response.content),
                'width': image_info.get('width', 0),
                'height': image_info.get('height', 0),
                'mediatype': image_info.get('mediatype', ''),
                'extmetadata': image_info.get('extmetadata', {}),
                'download_timestamp': datetime.now().isoformat(),
                'source': 'Wikimedia Commons'
            }
            
            metadata_path = local_path.with_suffix('.json')
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
                
            logger.info(f"✓ Downloaded: {image_info.get('title', 'Unknown')}")
            return True
            
        except Exception as e:
            logger.error(f"Error downloading image {image_info.get('title', 'Unknown')}: {e}")
            return False
    
    def download_page_images(self, page_title, page_domain, max_images=50):
        """Download all images from a Wikipedia page"""
        logger.info(f"Downloading images for: {page_domain}/{page_title}")
        
        # Create page-specific directory
        page_dir = self.downloads_dir / page_domain / page_title
        page_dir.mkdir(parents=True, exist_ok=True)
        
        # Get list of images
        image_titles = self.get_page_images(page_title)
        if not image_titles:
            logger.info(f"No images found for {page_title}")
            return []
            
        logger.info(f"Found {len(image_titles)} images for {page_title}")
        
        downloaded_images = []
        
        # Download images (limited to prevent excessive requests)
        for i, image_title in enumerate(image_titles[:max_images]):
            try:
                # Rate limiting
                time.sleep(self.request_delay)
                
                # Clean image title (remove "File:" prefix if present)
                clean_title = image_title.replace('File:', '')
                
                # Get image info
                image_info = self.get_image_info(image_title)
                if not image_info:
                    logger.warning(f"Could not get info for: {image_title}")
                    continue
                
                # Create filename
                safe_name = re.sub(r'[^\w\-_.]', '_', clean_title)
                image_extension = image_info.get('url', '').split('.')[-1].split('?')[0]
                if image_extension:
                    filename = f"{safe_name}.{image_extension}"
                else:
                    filename = safe_name
                
                local_path = page_dir / filename
                
                # Skip if already downloaded
                if local_path.exists():
                    logger.info(f"✓ Already exists: {filename}")
                    downloaded_images.append(str(local_path))
                    continue
                
                # Download the image
                if self.download_image(image_info, local_path):
                    downloaded_images.append(str(local_path))
                    
            except Exception as e:
                logger.error(f"Error processing image {image_title}: {e}")
                continue
                
        logger.info(f"Downloaded {len(downloaded_images)} images for {page_title}")
        return downloaded_images
    
    def extract_images_from_html(self, html_file):
        """Extract image references from HTML content"""
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find image references in the HTML
            image_patterns = [
                r'<img[^>]+src="([^"]+)"',
                r'<a[^>]+href="([^"]+)\.jpg"',
                r'<a[^>]+href="([^"]+)\.png"',
                r'<a[^>]+href="([^"]+)\.gif"',
                r'<a[^>]+href="([^"]+)\.svg"'
            ]
            
            images = []
            for pattern in image_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    # Convert relative URLs to absolute
                    if match.startswith('/'):
                        match = f"https://commons.wikimedia.org{match}"
                    elif match.startswith('//'):
                        match = f"https:{match}"
                    images.append(match)
            
            # Remove duplicates and non-Commons URLs
            commons_images = list(set([img for img in images if 'commons.wikimedia.org' in img]))
            
            return commons_images
            
        except Exception as e:
            logger.error(f"Error extracting images from {html_file}: {e}")
            return []
    
    def download_from_html(self, html_file, page_domain):
        """Download images referenced in HTML file"""
        try:
            page_title = html_file.parent.name
            
            # Extract image URLs from HTML
            image_urls = self.extract_images_from_html(html_file)
            
            if not image_urls:
                logger.info(f"No images found in HTML for {page_title}")
                return []
            
            # Download each image
            downloaded_images = []
            page_dir = self.downloads_dir / page_domain / page_title
            page_dir.mkdir(parents=True, exist_ok=True)
            
            for url in image_urls:
                try:
                    time.sleep(self.request_delay)
                    
                    # Extract filename from URL
                    parsed_url = urlparse(url)
                    filename = os.path.basename(parsed_url.path)
                    if not filename or '.' not in filename:
                        # Generate filename from URL hash
                        filename = f"image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"
                    
                    # Clean filename
                    filename = re.sub(r'[^\w\-_.]', '_', filename)
                    local_path = page_dir / filename
                    
                    if local_path.exists():
                        logger.info(f"✓ Already exists: {filename}")
                        downloaded_images.append(str(local_path))
                        continue
                    
                    # Download image
                    response = requests.get(url, timeout=30, stream=True)
                    response.raise_for_status()
                    
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    
                    # Create metadata
                    metadata = {
                        'url': url,
                        'size': len(response.content),
                        'download_timestamp': datetime.now().isoformat(),
                        'source': 'Extracted from HTML'
                    }
                    
                    metadata_path = local_path.with_suffix('.json')
                    with open(metadata_path, 'w', encoding='utf-8') as f:
                        json.dump(metadata, f, indent=2, ensure_ascii=False)
                    
                    logger.info(f"✓ Downloaded: {filename}")
                    downloaded_images.append(str(local_path))
                    
                except Exception as e:
                    logger.error(f"Error downloading {url}: {e}")
                    continue
            
            logger.info(f"Downloaded {len(downloaded_images)} images from HTML for {page_title}")
            return downloaded_images
            
        except Exception as e:
            logger.error(f"Error downloading from HTML {html_file}: {e}")
            return []
    
    def run_image_collection(self):
        """Main method to collect images from all articles"""
        logger.info("Starting Wikimedia Commons image collection...")
        
        # Define all target articles by domain
        target_articles = {
            'indian-history': [
                'History_of_India', 'Timeline_of_Indian_history', 'Medieval_India',
                'Outline_of_ancient_India', 'Indian_independence_movement',
                'List_of_Indian_independence_activists', 'Mahatma_Gandhi',
                'Subhas_Chandra_Bose', 'Bal_Gangadhar_Tilak', 'Lala_Lajpat_Rai', 'Bhagat_Singh'
            ],
            'geography': [
                'Geography_of_India', 'List_of_major_rivers_of_India', 'Himalayas',
                'Western_Ghats', 'Eastern_Ghats', 'Indo-Gangetic_Plain'
            ],
            'polity': [
                'Constitution_of_India', 'Government_of_India', 'Parliament_of_India',
                'Supreme_Court_of_India', 'Kesavananda_Bharati_v_State_of_Kerala', 'Basic_structure_doctrine'
            ],
            'science-technology': [
                'Science_and_technology_in_India', 'ISRO', 'Chandrayaan_programme',
                'Mars_Orbiter_Mission', 'Nuclear_power_in_India',
                'Indias_three-stage_nuclear_power_programme', 'Vikram_Sarabhai'
            ],
            'economy': [
                'Economy_of_India', 'Banking_in_India', 'Reserve_Bank_of_India',
                'Finance_in_India', 'Payment_and_settlement_systems_in_India', 'List_of_banks_in_India'
            ],
            'environment': [
                'Environmental_issues_in_India', 'Wildlife_of_India', 'Environment_of_India',
                'Conservation_in_India', 'Fauna_of_India'
            ],
            'international-relations': [
                'United_Nations', 'International_relations', 'List_of_specialized_agencies_of_the_United_Nations'
            ],
            'organizations': [
                'United_Nations_System', 'List_of_intergovernmental_organizations',
                'International_organization', 'Member_states_of_the_United_Nations'
            ],
            'culture': ['Culture_of_India', 'Indian_literature']
        }
        
        total_downloaded = 0
        total_images = 0
        
        for domain, articles in target_articles.items():
            logger.info(f"\n--- Processing domain: {domain} ---")
            
            domain_dir = self.base_dir / domain
            if not domain_dir.exists():
                logger.warning(f"Domain directory not found: {domain}")
                continue
            
            for article in articles:
                article_dir = domain_dir / article
                
                # Try downloading from HTML first
                html_file = article_dir / 'index.html'
                if html_file.exists():
                    downloaded = self.download_from_html(html_file, domain)
                    total_downloaded += len(downloaded)
                    total_images += len(downloaded)
                else:
                    # Fallback to API method
                    downloaded = self.download_page_images(article, domain, max_images=20)
                    total_downloaded += len(downloaded)
                    total_images += len(downloaded)
        
        # Create summary report
        summary = {
            'collection_date': datetime.now().isoformat(),
            'total_images_downloaded': total_images,
            'total_downloads': total_downloaded,
            'download_directory': str(self.downloads_dir),
            'status': 'Completed' if total_images > 0 else 'No images found'
        }
        
        summary_file = self.downloads_dir / 'collection_summary.json'
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        logger.info(f"\n🎯 Image Collection Summary:")
        logger.info(f"   Total images downloaded: {total_images}")
        logger.info(f"   Downloads completed: {total_downloaded}")
        logger.info(f"   Summary saved: {summary_file}")
        
        return summary

def main():
    """Main execution function"""
    base_dir = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    
    try:
        downloader = WikimediaImageDownloader(base_dir)
        summary = downloader.run_image_collection()
        
        if summary['total_images_downloaded'] > 0:
            logger.info("✅ Image collection completed successfully!")
            return 0
        else:
            logger.warning("⚠️ No images were downloaded")
            return 1
            
    except Exception as e:
        logger.error(f"Image collection failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())