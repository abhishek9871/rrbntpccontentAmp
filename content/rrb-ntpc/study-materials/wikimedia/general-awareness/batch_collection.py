#!/usr/bin/env python3
"""
RRB NTPC General Awareness - Batch Collection Script
Systematically collects all identified Wikipedia articles for the syllabus.
"""

import os
import sys
import time
import json
from datetime import datetime

# Import our collection script
sys.path.append('/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness')
from collection_script import WikipediaCollector

def load_collection_list():
    """Load the comprehensive article collection list"""
    articles_list = {
        'indian-history': [
            ("History of India", "Complete history of the Indian subcontinent"),
            ("Timeline of Indian history", "Chronological timeline of Indian events"),
            ("Medieval India", "Medieval period of Indian history"),
            ("Outline of ancient India", "Ancient Indian civilizations and dynasties"),
            ("Middle kingdoms of India", "Post-classical period kingdoms"),
            ("Indian independence movement", "Freedom struggle against British rule"),
            ("List of Indian independence activists", "Comprehensive list of freedom fighters"),
            ("Mahatma Gandhi", "Leader of Indian independence movement"),
            ("Subhas Chandra Bose", "Indian nationalist leader"),
            ("Bal Gangadhar Tilak", "Indian nationalist and independence activist"),
            ("Lala Lajpat Rai", "Punjabi freedom fighter"),
            ("Bhagat Singh", "Revolutionary freedom fighter")
        ],
        'geography': [
            ("Geography of India", "Physical and geographical overview of India"),
            ("List of major rivers of India", "Major rivers flowing through India"),
            ("Himalayas", "Mountain range in northern India"),
            ("Western Ghats", "Mountain range along western coast"),
            ("Eastern Ghats", "Mountain range along eastern coast"),
            ("Indo-Gangetic Plain", "Fertile plain in northern India"),
            ("Indian subcontinent", "Geographical region of South Asia"),
            ("Geography of South India", "Geographic features of southern India")
        ],
        'polity': [
            ("Constitution of India", "Supreme law of India"),
            ("Parliament of India", "Legislative body of India"),
            ("Supreme Court of India", "Highest judicial authority"),
            ("Government of India", "Executive branch of Indian government"),
            ("Kesavananda Bharati v. State of Kerala", "Landmark constitutional case"),
            ("Basic structure doctrine", "Constitutional law doctrine")
        ],
        'science-technology': [
            ("Science and technology in India", "Scientific developments in India"),
            ("ISRO", "Indian Space Research Organisation"),
            ("Department of Space", "Government department for space affairs"),
            ("Chandrayaan programme", "Indian lunar exploration program"),
            ("Mars Orbiter Mission", "India's first interplanetary mission"),
            ("Nuclear power in India", "Nuclear energy program in India"),
            ("India's three-stage nuclear power programme", "Nuclear energy strategy"),
            ("Vikram Sarabhai", "Father of Indian space program")
        ],
        'economy': [
            ("Economy of India", "Economic overview of India"),
            ("Banking in India", "Banking system in India"),
            ("Reserve Bank of India", "Central bank of India"),
            ("Finance in India", "Financial system overview"),
            ("List of banks in India", "Banking institutions in India")
        ],
        'environment': [
            ("Environmental issues in India", "Major environmental challenges"),
            ("Wildlife of India", "Fauna and flora of India"),
            ("Environment of India", "Environmental overview"),
            ("Conservation in India", "Conservation efforts and policies"),
            ("Fauna of India", "Animal diversity of India")
        ],
        'culture': [
            ("Culture of India", "Cultural heritage of India"),
            ("Indian literature", "Literary traditions of India")
        ],
        'international-relations': [
            ("United Nations", "International organization"),
            ("International relations", "Study of international politics"),
            ("Member states of the United Nations", "UN member countries")
        ],
        'organizations': [
            ("List of specialized agencies of the United Nations", "UN specialized agencies"),
            ("United Nations System", "UN organizational structure"),
            ("International organization", "Types and functions of international organizations")
        ]
    }
    
    return articles_list

def batch_collect_articles():
    """Systematically collect all articles"""
    base_directory = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    collector = WikipediaCollector(base_directory)
    
    articles_list = load_collection_list()
    
    # Summary tracking
    total_categories = len(articles_list)
    total_articles = sum(len(articles) for articles in articles_list.values())
    collection_summary = {
        'collection_started': datetime.now().isoformat(),
        'total_categories': total_categories,
        'total_articles_planned': total_articles,
        'successful_collections': [],
        'failed_collections': [],
        'category_summaries': {}
    }
    
    print(f"Starting systematic collection of {total_articles} articles across {total_categories} categories...")
    print("=" * 60)
    
    category_count = 0
    for category_dir, articles in articles_list.items():
        category_count += 1
        category_success = 0
        category_total = len(articles)
        
        print(f"\\n[{category_count}/{total_categories}] COLLECTING CATEGORY: {category_dir.upper()}")
        print(f"Articles in this category: {category_total}")
        print("-" * 40)
        
        for i, (title, description) in enumerate(articles, 1):
            print(f"  [{i}/{category_total}] {title}")
            
            try:
                if collector.collect_article(title, category_dir):
                    collection_summary['successful_collections'].append({
                        'title': title,
                        'category': category_dir,
                        'description': description,
                        'timestamp': datetime.now().isoformat()
                    })
                    category_success += 1
                else:
                    collection_summary['failed_collections'].append({
                        'title': title,
                        'category': category_dir,
                        'description': description,
                        'error': 'Collection failed',
                        'timestamp': datetime.now().isoformat()
                    })
                
                # Rate limiting between articles
                time.sleep(3)
                
            except Exception as e:
                print(f"    ❌ Error collecting {title}: {e}")
                collection_summary['failed_collections'].append({
                    'title': title,
                    'category': category_dir,
                    'description': description,
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
        
        # Category summary
        collection_summary['category_summaries'][category_dir] = {
            'total': category_total,
            'successful': category_success,
            'failed': category_total - category_success,
            'success_rate': f"{(category_success/category_total)*100:.1f}%"
        }
        
        print(f"\\n📊 {category_dir.upper()} Summary: {category_success}/{category_total} successful ({(category_success/category_total)*100:.1f}%)")
        
        # Pause between categories
        time.sleep(5)
    
    # Final summary
    collection_summary['collection_completed'] = datetime.now().isoformat()
    collection_summary['total_successful'] = len(collection_summary['successful_collections'])
    collection_summary['total_failed'] = len(collection_summary['failed_collections'])
    collection_summary['overall_success_rate'] = f"{(collection_summary['total_successful']/total_articles)*100:.1f}%"
    
    # Save collection summary
    summary_path = os.path.join(base_directory, 'metadata', 'collection_summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(collection_summary, f, indent=2, ensure_ascii=False)
    
    print("\\n" + "=" * 60)
    print("🏁 COLLECTION COMPLETE!")
    print(f"✅ Successful: {collection_summary['total_successful']}/{total_articles}")
    print(f"❌ Failed: {collection_summary['total_failed']}/{total_articles}")
    print(f"📈 Success Rate: {collection_summary['overall_success_rate']}")
    print(f"💾 Summary saved: {summary_path}")
    print("=" * 60)
    
    return collection_summary

if __name__ == "__main__":
    summary = batch_collect_articles()
