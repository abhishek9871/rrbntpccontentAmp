#!/usr/bin/env python3
"""
Simplified Wikipedia Image Downloader - Focused on key educational images
"""

import os
import requests
from bs4 import BeautifulSoup
import json

class FocusedImageDownloader:
    def __init__(self):
        self.base_path = '/workspace/wikimedia-reasoning/content/rrb-ntpc/study-materials/wikimedia/science'
        self.images_dir = os.path.join(self.base_path, 'images', 'environmental-science')
        os.makedirs(self.images_dir, exist_ok=True)
        
    def get_key_image_urls(self):
        """Get URLs for the most important educational images from environmental science pages"""
        key_images = [
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Smog_in_New_Delhi.jpg/800px-Smog_in_New_Delhi.jpg',
                'filename': 'environmental_issues_air_pollution.jpg',
                'alt': 'Air pollution in Delhi showing smog',
                'description': 'Air pollution example'
            },
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Great_Pacific_Garbage_Patch.jpg/800px-Great_Pacific_Garbage_Patch.jpg',
                'filename': 'pollution_plastic_oceans.jpg',
                'alt': 'Great Pacific Garbage Patch',
                'description': 'Plastic pollution in oceans'
            },
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Deforestation_in_Brazil.jpg/800px-Deforestation_in_Brazil.jpg',
                'filename': 'environmental_issues_deforestation.jpg',
                'alt': 'Deforestation in Brazil',
                'description': 'Deforestation example'
            },
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Earth_Eastern_Hemisphere.jpg/600px-Earth_Eastern_Hemisphere.jpg',
                'filename': 'ecosystem_earth_system.jpg',
                'alt': 'Earth Eastern Hemisphere',
                'description': 'Global ecosystem view'
            },
            {
                'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Biodiversity_Of_One_Square_Meter_Of_Tropical_Rainforest.jpg/600px-Biodiversity_Of_One_Square_Meter_Of_Tropical_Rainforest.jpg',
                'filename': 'biodiversity_tropical_forest.jpg',
                'alt': 'Biodiversity in tropical rainforest',
                'description': 'Tropical rainforest biodiversity'
            }
        ]
        return key_images
    
    def download_single_image(self, image_info):
        """Download a single image with error handling"""
        try:
            print(f"⬇️  Downloading: {image_info['filename']}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; EducationalBot/1.0; +https://example.com/bot)'
            }
            
            response = requests.get(image_info['url'], headers=headers, timeout=30)
            response.raise_for_status()
            
            filepath = os.path.join(self.images_dir, image_info['filename'])
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Downloaded: {image_info['filename']}")
            return True
            
        except Exception as e:
            print(f"❌ Error downloading {image_info['filename']}: {e}")
            return False
    
    def download_key_images(self):
        """Download the most important educational images"""
        print("🎯 Starting focused image download for Environmental Science")
        
        key_images = self.get_key_image_urls()
        downloaded_images = []
        
        for image_info in key_images:
            if self.download_single_image(image_info):
                downloaded_images.append(image_info)
        
        # Save inventory
        inventory_path = os.path.join(self.images_dir, 'key_images_inventory.json')
        with open(inventory_path, 'w') as f:
            json.dump(downloaded_images, f, indent=2)
        
        print(f"\n🎉 Downloaded {len(downloaded_images)} key images")
        print(f"📁 Images saved to: {self.images_dir}")
        print(f"📊 Inventory: {inventory_path}")
        
        return downloaded_images

def main():
    downloader = FocusedImageDownloader()
    downloaded_images = downloader.download_key_images()
    
    print("\n✅ Core image preservation task completed")
    return downloaded_images

if __name__ == '__main__':
    main()