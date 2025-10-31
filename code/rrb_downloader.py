#!/usr/bin/env python3
"""
RRB NTPC Document Downloader
Downloads official RRB documents and question papers with proper organization and metadata.
"""

import os
import json
import hashlib
import requests
import time
from datetime import datetime
from urllib.parse import urlparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RRBDownloader:
    def __init__(self, base_dir="/workspace/downloads"):
        self.base_dir = base_dir
        self.log_file = os.path.join(base_dir, "logs", "downloads.log")
        self.ensure_directories()
        
    def ensure_directories(self):
        """Create necessary directories"""
        os.makedirs(os.path.join(self.base_dir, "rrb-ntpc", "previous-papers", "CBT1"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "rrb-ntpc", "previous-papers", "CBT2"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "logs"), exist_ok=True)
        
    def calculate_checksum(self, filepath):
        """Calculate SHA256 checksum of file"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def get_file_size(self, filepath):
        """Get file size in bytes"""
        return os.path.getsize(filepath)
    
    def download_file(self, url, output_path, max_retries=3):
        """Download file with retries and progress tracking"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Downloading {url} (attempt {attempt + 1})")
                
                response = requests.get(url, headers=headers, stream=True, timeout=60)
                response.raise_for_status()
                
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                progress = (downloaded / total_size) * 100
                                print(f"\rProgress: {progress:.1f}%", end="", flush=True)
                
                print()  # New line after progress
                logger.info(f"Downloaded successfully: {output_path}")
                return True
                
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(5)  # Wait before retry
                else:
                    logger.error(f"All download attempts failed for {url}")
                    return False
        
        return False
    
    def create_metadata(self, filepath, metadata):
        """Create metadata JSON file"""
        if os.path.exists(filepath):
            checksum = self.calculate_checksum(filepath)
            filesize = self.get_file_size(filepath)
            
            metadata.update({
                'checksum_sha256': checksum,
                'filesize_bytes': filesize,
                'retrieved_at': datetime.now().isoformat(),
                'verification_notes': 'Downloaded from official RRB source'
            })
            
            metadata_path = filepath + '.json'
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Metadata created: {metadata_path}")
        else:
            logger.error(f"File not found for metadata creation: {filepath}")
    
    def parse_filename(self, filename):
        """Parse filename to extract components"""
        # Expected format: <category>__<year>__<stage>__<subject_or_topic>__<language>__<source-domain>.<ext>
        parts = filename.split('__')
        if len(parts) >= 6:
            return {
                'category': parts[0],
                'year': parts[1],
                'stage': parts[2],
                'topic': parts[3],
                'language': parts[4],
                'domain': parts[5].split('.')[0],  # Remove file extension
                'ext': filename.split('.')[-1]
            }
        return None
    
    def download_direct_pdfs(self):
        """Download directly accessible PDFs from the catalog"""
        downloads = [
            {
                'url': 'https://rrbsecunderabad.gov.in/CEN05-2024-CBT1-to-CBT2-Results-CEN-05-2024-NTPC-Graduate.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT2/2024/results__2024__CBT1toCBT2__ntpc-graduate__en__rrbsecunderabad.gov.pdf',
                'metadata': {
                    'title': 'CEN 05/2024 CBT1 to CBT2 Results NTPC Graduate',
                    'year': '2024',
                    'stage': 'CBT1 to CBT2',
                    'sections': 'Results',
                    'topic_tags': ['NTPC', 'Graduate', 'Results'],
                    'language': 'en',
                    'source_url': 'https://rrbsecunderabad.gov.in/CEN05-2024-CBT1-to-CBT2-Results-CEN-05-2024-NTPC-Graduate.pdf',
                    'source_domain': 'rrbsecunderabad.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Secunderabad'
                }
            },
            {
                'url': 'https://rrbchennai.gov.in/CEN-03-2015-shortlisted-18candidates-2nd-stage-examination.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT2/2015/shortlist__2015__CBT2__cen-03-2015__en__rrbchennai.gov.pdf',
                'metadata': {
                    'title': 'CEN 03/2015 Shortlisted Candidates for 2nd Stage Examination',
                    'year': '2015',
                    'stage': 'CBT2',
                    'sections': 'Shortlist',
                    'topic_tags': ['Shortlist', 'CBT2', 'CEN-03-2015'],
                    'language': 'en',
                    'source_url': 'https://rrbchennai.gov.in/CEN-03-2015-shortlisted-18candidates-2nd-stage-examination.pdf',
                    'source_domain': 'rrbchennai.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Chennai'
                }
            },
            {
                'url': 'https://rrbsecunderabad.gov.in/CEN-01-2019-NTPC-CBT1-Result-Level-5.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT1/2019/results__2019__CBT1__ntpc-level-5__en__rrbsecunderabad.gov.pdf',
                'metadata': {
                    'title': 'CEN 01/2019 NTPC CBT1 Result Level 5',
                    'year': '2019',
                    'stage': 'CBT1',
                    'sections': 'Results',
                    'topic_tags': ['NTPC', 'Level 5', 'Results', 'CEN-01-2019'],
                    'language': 'en',
                    'source_url': 'https://rrbsecunderabad.gov.in/CEN-01-2019-NTPC-CBT1-Result-Level-5.pdf',
                    'source_domain': 'rrbsecunderabad.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Secunderabad'
                }
            },
            {
                'url': 'https://rrbchennai.gov.in/CEN-05-2024-NB-Candidates-shortlisted-for-CBT-2.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT2/2024/shortlist__2024__CBT2__cen-05-2024__en__rrbchennai.gov.pdf',
                'metadata': {
                    'title': 'CEN 05/2024 Non-Backlog Candidates shortlisted for CBT2',
                    'year': '2024',
                    'stage': 'CBT2',
                    'sections': 'Shortlist',
                    'topic_tags': ['Shortlist', 'CBT2', 'Non-Backlog', 'CEN-05-2024'],
                    'language': 'en',
                    'source_url': 'https://rrbchennai.gov.in/CEN-05-2024-NB-Candidates-shortlisted-for-CBT-2.pdf',
                    'source_domain': 'rrbchennai.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Chennai'
                }
            }
        ]
        
        successful_downloads = []
        failed_downloads = []
        
        for download in downloads:
            try:
                if self.download_file(download['url'], download['output_path']):
                    self.create_metadata(download['output_path'], download['metadata'])
                    successful_downloads.append(download['output_path'])
                else:
                    failed_downloads.append(download['url'])
            except Exception as e:
                logger.error(f"Error processing download {download['url']}: {str(e)}")
                failed_downloads.append(download['url'])
        
        # Log summary
        with open(self.log_file, 'a') as f:
            f.write(f"\n=== Download Summary ===\n")
            f.write(f"Time: {datetime.now().isoformat()}\n")
            f.write(f"Successful: {len(successful_downloads)}\n")
            f.write(f"Failed: {len(failed_downloads)}\n")
            f.write(f"Total attempted: {len(downloads)}\n")
            
            if successful_downloads:
                f.write("Successful downloads:\n")
                for download in successful_downloads:
                    f.write(f"  - {download}\n")
            
            if failed_downloads:
                f.write("Failed downloads:\n")
                for download in failed_downloads:
                    f.write(f"  - {download}\n")
        
        return successful_downloads, failed_downloads

if __name__ == "__main__":
    downloader = RRBDownloader()
    successful, failed = downloader.download_direct_pdfs()
    print(f"Download complete. Successful: {len(successful)}, Failed: {len(failed)}")
