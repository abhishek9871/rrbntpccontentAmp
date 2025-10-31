#!/usr/bin/env python3
"""
Small batch collection for validation and testing
"""

import sys
sys.path.append('/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness')
from collection_script import WikipediaCollector
import time

def collect_core_articles():
    """Collect core high-priority articles"""
    base_directory = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    collector = WikipediaCollector(base_directory)
    
    # Core articles - 15 high-priority ones
    core_articles = [
        # Indian History - Core
        ("History of India", "indian-history"),
        ("Indian independence movement", "indian-history"),
        ("Mahatma Gandhi", "indian-history"),
        ("Subhas Chandra Bose", "indian-history"),
        
        # Geography - Core
        ("Geography of India", "geography"),
        ("List of major rivers of India", "geography"),
        ("Himalayas", "geography"),
        
        # Polity - Core  
        ("Constitution of India", "polity"),
        ("Parliament of India", "polity"),
        ("Supreme Court of India", "polity"),
        
        # Science & Technology - Core
        ("Science and technology in India", "science-technology"),
        ("ISRO", "science-technology"),
        
        # Economy - Core
        ("Economy of India", "economy"),
        ("Reserve Bank of India", "economy"),
        
        # Environment - Core
        ("Environmental issues in India", "environment")
    ]
    
    print("Collecting core RRB NTPC General Awareness articles...")
    print(f"Total articles: {len(core_articles)}")
    print("=" * 50)
    
    successful = 0
    failed = 0
    
    for i, (title, category) in enumerate(core_articles, 1):
        print(f"[{i}/{len(core_articles)}] {title} -> {category}")
        
        try:
            if collector.collect_article(title, category):
                print(f"  ✅ Success")
                successful += 1
            else:
                print(f"  ❌ Failed")
                failed += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
            failed += 1
        
        # Rate limiting
        time.sleep(3)
    
    print("=" * 50)
    print(f"Core collection complete!")
    print(f"✅ Successful: {successful}/{len(core_articles)}")
    print(f"❌ Failed: {failed}/{len(core_articles)}")
    print(f"📊 Success Rate: {(successful/len(core_articles))*100:.1f}%")

if __name__ == "__main__":
    collect_core_articles()
