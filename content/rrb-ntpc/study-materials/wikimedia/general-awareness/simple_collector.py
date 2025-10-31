#!/usr/bin/env python3
"""
Simple manual Wikipedia content collection
Manual approach for reliable collection
"""

import os
import json
import re
from datetime import datetime
import hashlib

def create_article_page(title, category):
    """Create a basic article placeholder with proper structure"""
    
    # Create directory structure
    base_dir = "/workspace/content/rrb-ntpc/study-materials/wikimedia/general-awareness"
    category_dir = os.path.join(base_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    
    article_name = re.sub(r'[^\w\s-]', '', title.replace(' ', '_'))
    article_dir = os.path.join(category_dir, article_name)
    os.makedirs(article_dir, exist_ok=True)
    
    # Create HTML content with placeholder
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px; 
            line-height: 1.6; 
            background-color: #f9f9f9;
        }}
        .header {{ 
            background: #0066cc; 
            color: white; 
            padding: 20px; 
            border-radius: 8px 8px 0 0; 
            margin-bottom: 0;
        }}
        .attribution {{ 
            background: #f0f0f0; 
            padding: 15px; 
            margin-bottom: 20px; 
            border-radius: 0 0 8px 8px; 
            font-size: 0.9em; 
        }}
        .content {{ 
            background: white; 
            padding: 30px; 
            border: 1px solid #ddd; 
            border-radius: 8px;
            min-height: 400px;
        }}
        .status {{ 
            background: #fff3cd; 
            border: 1px solid #ffeaa7; 
            color: #856404; 
            padding: 15px; 
            border-radius: 5px; 
            margin-bottom: 20px;
        }}
        .links a {{ 
            display: block; 
            padding: 10px; 
            margin: 5px 0; 
            background: #e9ecef; 
            text-decoration: none; 
            border-radius: 4px;
        }}
        .links a:hover {{ 
            background: #dee2e6; 
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>General Awareness - RRB NTPC Study Materials</p>
    </div>
    
    <div class="status">
        <strong>📋 Status:</strong> Content placeholder created - To be populated with actual Wikipedia content<br>
        <strong>📚 Category:</strong> {category.replace('-', ' ').title()}<br>
        <strong>🎯 Target:</strong> RRB NTPC General Awareness
    </div>
    
    <div class="attribution">
        <h3>📜 Attribution and Licensing</h3>
        <strong>Source:</strong> Wikipedia - <a href="https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" target="_blank" rel="noopener">{title}</a><br>
        <strong>License:</strong> CC BY-SA 3.0<br>
        <strong>Attribution:</strong> This work is based on Wikipedia content, licensed under CC BY-SA 3.0<br>
        <strong>Contributors:</strong> Wikipedia/Wikibooks contributors<br>
        <strong>Collection Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
        <strong>Status:</strong> Placeholder - Manual collection needed
    </div>
    
    <div class="content">
        <h2>📖 Content Overview</h2>
        <p>This page is a placeholder for comprehensive content about <strong>{title}</strong> as covered in the RRB NTPC General Awareness section.</p>
        
        <h3>🎯 Key Topics to Cover:</h3>
        <ul>
            <li>Historical context and significance</li>
            <li>Important dates and events</li>
            <li>Key personalities and contributions</li>
            <li>Current relevance and connections</li>
            <li>Exam-oriented facts and figures</li>
        </ul>
        
        <h3>🔗 Related Resources:</h3>
        <div class="links">
            <a href="https://en.wikipedia.org/wiki/{title.replace(' ', '_')}" target="_blank" rel="noopener">
                📖 Full Wikipedia Article
            </a>
            <a href="https://en.wikipedia.org/wiki/Special:Search/{title.replace(' ', '_')}" target="_blank" rel="noopener">
                🔍 Related Articles on Wikipedia
            </a>
        </div>
        
        <h3>📝 Notes:</h3>
        <p><em>This placeholder structure provides the framework for Wikipedia content that will be populated manually. The actual Wikipedia articles provide comprehensive coverage of:</em></p>
        <ul>
            <li><strong>Historical Background:</strong> Detailed timeline and context</li>
            <li><strong>Key Features:</strong> Important characteristics and significance</li>
            <li><strong>Current Status:</strong> Recent developments and present state</li>
            <li><strong>Exam Relevance:</strong> Connection to RRB NTPC syllabus</li>
        </ul>
    </div>
    
    <script>
        // Add basic interactivity
        document.addEventListener('DOMContentLoaded', function() {{
            console.log('Wikipedia content placeholder loaded: {title}');
            
            // Add click tracking
            const links = document.querySelectorAll('a[href*="wikipedia.org"]');
            links.forEach(link => {{
                link.addEventListener('click', function(e) {{
                    console.log('Wikipedia link clicked:', this.href);
                }});
            }});
        }});
    </script>
</body>
</html>"""
    
    # Save HTML file
    html_filepath = os.path.join(article_dir, f"{article_name}.html")
    with open(html_filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Create metadata
    metadata = {
        'title': title,
        'original_url': f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
        'pageid': 'placeholder',
        'revision_id': 'pending',
        'timestamp': datetime.now().isoformat(),
        'language': 'en',
        'category': category,
        'collected_date': datetime.now().isoformat(),
        'license': 'CC BY-SA 3.0',
        'attribution': 'This work is based on Wikipedia content, licensed under CC BY-SA 3.0. Contributors: Wikipedia/Wikibooks contributors.',
        'files': {
            'html': f"{article_name}.html"
        },
        'images_count': 0,
        'file_hash': hashlib.md5(html_content.encode()).hexdigest()[:8],
        'status': 'placeholder_created',
        'notes': 'Manual placeholder created for systematic Wikipedia content extraction'
    }
    
    # Save metadata
    metadata_filepath = os.path.join(article_dir, 'metadata.json')
    with open(metadata_filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    return article_name

def main():
    """Create collection framework"""
    print("Creating comprehensive Wikipedia collection framework...")
    
    # Priority articles for RRB NTPC GA
    priority_articles = {
        'indian-history': [
            ("History of India", "Complete history overview"),
            ("Timeline of Indian history", "Chronological timeline"),
            ("Medieval India", "Medieval period"),
            ("Outline of ancient India", "Ancient India"),
            ("Indian independence movement", "Freedom struggle"),
            ("List of Indian independence activists", "Freedom fighters"),
            ("Mahatma Gandhi", "Freedom movement leader"),
            ("Subhas Chandra Bose", "Freedom fighter"),
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
            ("Kesavananda Bharati v. State of Kerala", "Constitutional case"),
            ("Basic structure doctrine", "Constitutional law")
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
        ],
        'international-relations': [
            ("United Nations", "International organization"),
            ("International relations", "International politics"),
            ("List of specialized agencies of the United Nations", "UN agencies")
        ],
        'organizations': [
            ("List of intergovernmental organizations", "Global organizations"),
            ("United Nations System", "UN structure")
        ]
    }
    
    total_categories = len(priority_articles)
    total_articles = sum(len(category_articles) for category_articles in priority_articles.values())
    
    print(f"Creating framework for {total_articles} articles across {total_categories} categories")
    print("=" * 60)
    
    created_count = 0
    
    for category, articles in priority_articles.items():
        print(f"\\nCreating: {category.upper()}")
        
        for i, (title, description) in enumerate(articles, 1):
            try:
                article_name = create_article_page(title, category)
                print(f"  [{i}/{len(articles)}] ✓ {title}")
                created_count += 1
            except Exception as e:
                print(f"  [{i}/{len(articles)}] ❌ {title}: {e}")
        
        print(f"✓ {category} category completed")
    
    print("\\n" + "=" * 60)
    print("🏁 FRAMEWORK CREATION COMPLETE!")
    print(f"✅ Articles created: {created_count}/{total_articles}")
    print(f"📊 Success Rate: {(created_count/total_articles)*100:.1f}%")
    print("\\n📁 Structure: /content/rrb-ntpc/study-materials/wikimedia/general-awareness/")
    print("=" * 60)
    
    return created_count

if __name__ == "__main__":
    main()
