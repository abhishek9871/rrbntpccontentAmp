#!/usr/bin/env python3
"""
Wikipedia Image Downloader and Preserver
Downloads and organizes images from Wikipedia pages for educational content
"""

import os
import re
import json
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

class WikipediaImageDownloader:
    def __init__(self, base_path):
        self.base_path = base_path
        self.images_dir = os.path.join(base_path, 'images')
        self.create_directories()
        
        # Wikimedia Commons base URL
        self.commons_base = 'https://commons.wikimedia.org/wiki/File:'
        
    def create_directories(self):
        """Create necessary directories for image organization"""
        directories = [
            self.images_dir,
            os.path.join(self.images_dir, 'environmental-science'),
            os.path.join(self.images_dir, 'physics'),
            os.path.join(self.images_dir, 'chemistry'),
            os.path.join(self.images_dir, 'biology')
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Created directory: {directory}")
    
    def extract_image_urls(self, page_url, page_name):
        """Extract image URLs from a Wikipedia page"""
        try:
            print(f"🔍 Extracting images from {page_name}...")
            
            # Get the page content
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; EducationalBot/1.0; +https://example.com/bot)'
            }
            response = requests.get(page_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Parse HTML and extract images
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all image elements
            images = []
            
            # Regular img tags
            for img in soup.find_all('img'):
                src = img.get('src')
                alt = img.get('alt', '')
                width = img.get('width')
                
                if src and src.startswith('/'):
                    full_url = f"https://en.wikipedia.org{src}"
                    
                    # Skip small icons and decorative images
                    if width and int(width) < 100:
                        continue
                        
                    images.append({
                        'url': full_url,
                        'alt': alt,
                        'filename': self.generate_filename(page_name, alt, src),
                        'width': width
                    })
            
            # Look for file links
            file_links = soup.find_all('a', href=re.compile(r'/wiki/File:'))
            for link in file_links:
                file_name = link.get('href', '').replace('/wiki/File:', '')
                if file_name:
                    # Try to construct Wikimedia Commons URL
                    encoded_name = file_name.replace(' ', '_')
                    commons_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded_name}"
                    alt_text = link.get('title', file_name)
                    
                    images.append({
                        'url': commons_url,
                        'alt': alt_text,
                        'filename': self.generate_filename(page_name, alt_text, encoded_name),
                        'width': None
                    })
            
            print(f"📊 Found {len(images)} images on {page_name}")
            return images
            
        except Exception as e:
            print(f"❌ Error extracting images from {page_name}: {e}")
            return []
    
    def generate_filename(self, page_name, alt_text, src):
        """Generate a safe filename for the image"""
        # Clean the filename
        if alt_text:
            filename = alt_text
        elif src:
            filename = src.split('/')[-1].split('?')[0]
        else:
            filename = f"{page_name}_image"
        
        # Remove special characters and limit length
        filename = re.sub(r'[^\w\s-]', '', filename)
        filename = re.sub(r'\s+', '_', filename)[:50]
        
        # Add extension if missing
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg')):
            filename += '.jpg'
        
        return filename
    
    def download_image(self, image_info, subject_dir):
        """Download a single image"""
        try:
            url = image_info['url']
            filename = image_info['filename']
            filepath = os.path.join(subject_dir, filename)
            
            # Skip if already downloaded
            if os.path.exists(filepath):
                print(f"⏭️  Skipping existing image: {filename}")
                return True
            
            print(f"⬇️  Downloading: {filename}")
            
            # Download the image
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; EducationalBot/1.0; +https://example.com/bot)'
            }
            response = requests.get(url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            # Save the image
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Downloaded: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Error downloading {image_info['filename']}: {e}")
            return False
    
    def process_page(self, page_url, page_name, subject):
        """Process a single Wikipedia page for image extraction and download"""
        print(f"\n{'='*60}")
        print(f"Processing: {page_name}")
        print(f"URL: {page_url}")
        print(f"Subject: {subject}")
        print(f"{'='*60}")
        
        # Extract images
        images = self.extract_image_urls(page_url, page_name)
        
        if not images:
            print(f"⚠️  No images found for {page_name}")
            return []
        
        # Create subject directory
        subject_dir = os.path.join(self.images_dir, subject)
        os.makedirs(subject_dir, exist_ok=True)
        
        # Download images
        downloaded_images = []
        for image_info in images:
            if self.download_image(image_info, subject_dir):
                downloaded_images.append({
                    'original_url': image_info['url'],
                    'local_path': os.path.join(subject, image_info['filename']),
                    'alt_text': image_info['alt'],
                    'filename': image_info['filename']
                })
            time.sleep(1)  # Rate limiting
        
        print(f"🎯 Successfully processed {page_name}: {len(downloaded_images)} images downloaded")
        return downloaded_images
    
    def download_environmental_science_images(self):
        """Download images from all environmental science pages"""
        environmental_pages = [
            {
                'url': 'https://en.wikipedia.org/wiki/Environmental_issues',
                'name': 'Environmental Issues',
                'subject': 'environmental-science'
            },
            {
                'url': 'https://en.wikipedia.org/wiki/Environmental_science',
                'name': 'Environmental Science',
                'subject': 'environmental-science'
            },
            {
                'url': 'https://en.wikipedia.org/wiki/Ecosystem',
                'name': 'Ecosystem',
                'subject': 'environmental-science'
            },
            {
                'url': 'https://en.wikipedia.org/wiki/Pollution',
                'name': 'Pollution',
                'subject': 'environmental-science'
            },
            {
                'url': 'https://en.wikipedia.org/wiki/Biodiversity',
                'name': 'Biodiversity',
                'subject': 'environmental-science'
            }
        ]
        
        all_downloaded_images = []
        
        for page_info in environmental_pages:
            downloaded = self.process_page(
                page_info['url'],
                page_info['name'],
                page_info['subject']
            )
            all_downloaded_images.extend(downloaded)
        
        # Save image inventory
        inventory_file = os.path.join(self.images_dir, 'environmental_science_images_inventory.json')
        with open(inventory_file, 'w', encoding='utf-8') as f:
            json.dump(all_downloaded_images, f, indent=2)
        
        print(f"\n🎉 Environmental Science Image Download Complete!")
        print(f"📊 Total images downloaded: {len(all_downloaded_images)}")
        print(f"📁 Inventory saved to: {inventory_file}")
        
        return all_downloaded_images

def main():
    base_path = '/workspace/wikimedia-reasoning/content/rrb-ntpc/study-materials/wikimedia/science'
    downloader = WikipediaImageDownloader(base_path)
    
    print("🚀 Starting Wikipedia Image Download for Environmental Science")
    downloaded_images = downloader.download_environmental_science_images()
    
    return downloaded_images

if __name__ == '__main__':
    main()