#!/usr/bin/env python3
"""
Download key educational images using direct Wikimedia Commons URLs
"""

import requests
import os

def download_image_direct(url, filename, alt_text):
    """Download image directly from Wikimedia Commons"""
    try:
        print(f"⬇️ Downloading: {filename}")
        
        headers = {
            'User-Agent': 'Educational-Content-Creator/1.0 (Educational use)',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        filepath = os.path.join('/workspace/wikimedia-reasoning/content/rrb-ntpc/study-materials/wikimedia/science/images/environmental-science', filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")
        return False

def main():
    print("🎯 Downloading key educational images for Environmental Science...")
    
    # Key educational images with direct Wikimedia Commons URLs
    key_images = [
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Smog_in_New_Delhi.jpg/800px-Smog_in_New_Delhi.jpg',
            'filename': 'environmental_issues_air_pollution_delhi.jpg',
            'alt': 'Air pollution and smog in New Delhi showing severe air quality'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Great_Pacific_Garbage_Patch.jpg/800px-Great_Pacific_Garbage_Patch.jpg',
            'filename': 'pollution_plastic_ocean.jpg',
            'alt': 'Great Pacific Garbage Patch showing plastic pollution in oceans'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Deforestation_in_Brazil.jpg/800px-Deforestation_in_Brazil.jpg',
            'filename': 'environmental_issues_deforestation_brazil.jpg',
            'alt': 'Deforestation in Brazilian Amazon rainforest'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Earth_Eastern_Hemisphere.jpg/600px-Earth_Eastern_Hemisphere.jpg',
            'filename': 'ecosystem_global_earth.jpg',
            'alt': 'Earth Eastern Hemisphere showing global ecosystem'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Biodiversity_Of_One_Square_Meter_Of_Tropical_Rainforest.jpg/600px-Biodiversity_Of_One_Square_Meter_Of_Tropical_Rainforest.jpg',
            'filename': 'biodiversity_tropical_rainforest.jpg',
            'alt': 'Biodiversity in one square meter of tropical rainforest'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Fukushima_Daiichi_Nuclear_Disaster_1.jpg/800px-Fukushima_Daiichi_Nuclear_Disaster_1.jpg',
            'filename': 'environmental_issues_nuclear_disaster.jpg',
            'alt': 'Fukushima nuclear disaster showing environmental contamination'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/East_Scotia_Ridge_-_Plos_Biol_04.jpg/250px-East_Scotia_Ridge_-_Plos_Biol_04.jpg',
            'filename': 'ecosystem_underwater_ridge.jpg',
            'alt': 'Deep sea hydrothermal vents showing marine ecosystem'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Nitrogen_Cycle.jpg/450px-Nitrogen_Cycle.jpg',
            'filename': 'ecosystem_nitrogen_cycle.jpg',
            'alt': 'Nitrogen cycle diagram showing biogeochemical cycling'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Oil_Spill_Fisherman_2.jpg/250px-Oil_Spill_Fisherman_2.jpg',
            'filename': 'pollution_oil_spill_fisherman.jpg',
            'alt': 'Fisherman affected by oil spill showing pollution impact'
        },
        {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Fungi_of_Saskatchewan.JPG/250px-Fungi_of_Saskatchewan.JPG',
            'filename': 'biodiversity_fungi_saskatchewan.jpg',
            'alt': 'Fungi in Saskatchewan showing biodiversity of decomposers'
        }
    ]
    
    downloaded_count = 0
    
    for image_info in key_images:
        if download_image_direct(image_info['url'], image_info['filename'], image_info['alt']):
            downloaded_count += 1
    
    print(f"\n🎉 Successfully downloaded {downloaded_count} key educational images")
    
    # Create image inventory
    inventory_path = '/workspace/wikimedia-reasoning/content/rrb-ntpc/study-materials/wikimedia/science/images/environmental-science/key_educational_images_inventory.json'
    with open(inventory_path, 'w') as f:
        import json
        json.dump(key_images, f, indent=2)
    
    print(f"📊 Image inventory saved to: {inventory_path}")
    return downloaded_count

if __name__ == '__main__':
    main()
