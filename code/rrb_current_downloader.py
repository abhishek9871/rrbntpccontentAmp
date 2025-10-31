#!/usr/bin/env python3
"""
RRB Current Documents Downloader
Downloads accessible PDFs from current RRB portals, especially RRB Bhopal.
"""

import os
import json
import hashlib
import requests
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CurrentRRBDownloader:
    def __init__(self):
        self.base_dir = "/workspace/downloads"
        self.log_file = os.path.join(self.base_dir, "logs", "downloads.log")
        self.ensure_directories()
        
    def ensure_directories(self):
        os.makedirs(os.path.join(self.base_dir, "rrb-ntpc", "previous-papers", "CBT1"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "rrb-ntpc", "previous-papers", "CBT2"), exist_ok=True)
        os.makedirs(os.path.join(self.base_dir, "logs"), exist_ok=True)
        
    def calculate_checksum(self, filepath):
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    def get_file_size(self, filepath):
        return os.path.getsize(filepath)
    
    def download_file(self, url, output_path, metadata, max_retries=3):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/pdf,*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Downloading: {url} (attempt {attempt + 1})")
                
                response = requests.get(url, headers=headers, stream=True, timeout=120)
                response.raise_for_status()
                
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0 and downloaded % 100000 == 0:  # Log every 100KB
                                progress = (downloaded / total_size) * 100
                                print(f"\rProgress: {progress:.1f}% ({downloaded}/{total_size} bytes)", end="", flush=True)
                
                print()  # New line
                
                # Verify download
                if os.path.exists(output_path):
                    filesize = self.get_file_size(output_path)
                    if filesize > 1000:  # At least 1KB
                        self.create_metadata(output_path, metadata)
                        logger.info(f"Successfully downloaded: {output_path}")
                        return True
                    else:
                        logger.error(f"Downloaded file too small: {filesize} bytes")
                        os.remove(output_path)
                else:
                    logger.error(f"File not created: {output_path}")
                    
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(10)  # Wait before retry
        
        logger.error(f"All download attempts failed for {url}")
        return False
    
    def create_metadata(self, filepath, metadata):
        if os.path.exists(filepath):
            checksum = self.calculate_checksum(filepath)
            filesize = self.get_file_size(filepath)
            
            metadata.update({
                'checksum_sha256': checksum,
                'filesize_bytes': filesize,
                'retrieved_at': datetime.now().isoformat(),
                'verification_notes': 'Downloaded from active RRB official portal'
            })
            
            metadata_path = filepath + '.json'
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Metadata created: {metadata_path}")
        else:
            logger.error(f"File not found for metadata: {filepath}")

    def download_bhopal_documents(self):
        """Download PDFs from RRB Bhopal that are accessible"""
        downloads = [
            {
                'url': 'https://rrbbhopal.gov.in/Beware.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT1/2025/notice__2025__CBT__railway-recruitment-warning__en__rrbbhopal.gov.pdf',
                'metadata': {
                    'title': 'Railway Recruitment Exam Warning',
                    'year': '2025',
                    'stage': 'CBT',
                    'sections': 'Notice',
                    'topic_tags': ['Warning', 'Railway Recruitment', 'Exam'],
                    'language': 'en',
                    'source_url': 'https://rrbbhopal.gov.in/Beware.pdf',
                    'source_domain': 'rrbbhopal.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Bhopal'
                }
            },
            {
                'url': 'https://rrbbhopal.gov.in/Normalization FAQ.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT1/2025/faq__2025__CBT__normalization__en__rrbbhopal.gov.pdf',
                'metadata': {
                    'title': 'Normalization FAQ',
                    'year': '2025',
                    'stage': 'CBT',
                    'sections': 'FAQ',
                    'topic_tags': ['Normalization', 'FAQ', 'Scoring'],
                    'language': 'en',
                    'source_url': 'https://rrbbhopal.gov.in/Normalization FAQ.pdf',
                    'source_domain': 'rrbbhopal.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Bhopal'
                }
            },
            {
                'url': 'https://rrbbhopal.gov.in/Notice.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT1/2025/notice__2025__CBT__email-correspondence__en__rrbbhopal.gov.pdf',
                'metadata': {
                    'title': 'E-Mail Correspondence Important Notice',
                    'year': '2025',
                    'stage': 'CBT',
                    'sections': 'Notice',
                    'topic_tags': ['Email', 'Correspondence', 'Important Notice'],
                    'language': 'en',
                    'source_url': 'https://rrbbhopal.gov.in/Notice.pdf',
                    'source_domain': 'rrbbhopal.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Bhopal'
                }
            },
            {
                'url': 'https://rrbbhopal.gov.in/CEN 5_2025_JE_DMS_CMA_ English_ 28.10.2025.pdf',
                'output_path': '/workspace/downloads/rrb-ntpc/previous-papers/CBT1/2025/cen__2025__CBT__je-dms-cma__en__rrbbhopal.gov.pdf',
                'metadata': {
                    'title': 'CEN 05/2025 - Junior Engineers, Depot Material Superintendent, Chemical & Metallurgical Assistant',
                    'year': '2025',
                    'stage': 'CBT',
                    'sections': 'CEN Notification',
                    'topic_tags': ['CEN-05-2025', 'JE', 'DMS', 'CMA', 'Graduate'],
                    'language': 'en',
                    'source_url': 'https://rrbbhopal.gov.in/CEN 5_2025_JE_DMS_CMA_ English_ 28.10.2025.pdf',
                    'source_domain': 'rrbbhopal.gov.in',
                    'license': 'Official Government Document',
                    'attribution_text': 'RRB Bhopal'
                }
            }
        ]
        
        successful_downloads = []
        failed_downloads = []
        
        for download in downloads:
            try:
                if self.download_file(download['url'], download['output_path'], download['metadata']):
                    successful_downloads.append(download['output_path'])
                else:
                    failed_downloads.append(download['url'])
            except Exception as e:
                logger.error(f"Error processing download {download['url']}: {str(e)}")
                failed_downloads.append(download['url'])
        
        # Log summary
        with open(self.log_file, 'a') as f:
            f.write(f"\n=== RRB Bhopal Download Summary ===\n")
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
    downloader = CurrentRRBDownloader()
    successful, failed = downloader.download_bhopal_documents()
    print(f"\nDownload complete. Successful: {len(successful)}, Failed: {len(failed)}")
