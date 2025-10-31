#!/usr/bin/env python3
"""
Verification script to spot-check generated checksums for accuracy.
"""

import hashlib
import csv
from pathlib import Path
import sys

def verify_checksum(file_path, expected_checksum):
    """Verify a file's SHA-256 checksum"""
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest() == expected_checksum
    except Exception as e:
        print(f"Error verifying {file_path}: {e}")
        return False

def spot_check_checksums():
    """Perform spot checks on generated checksums"""
    print("Performing spot verification of generated checksums...")
    
    # Read the master checksums file
    master_file = Path("/workspace/checksums/master_sha256sums.txt")
    
    if not master_file.exists():
        print("ERROR: Master checksums file not found!")
        return False
    
    # Sample some checksums to verify
    checked_files = 0
    verified_files = 0
    workspace_root = Path("/workspace")
    
    with open(master_file, 'r') as f:
        lines = f.readlines()
        
        # Skip comments and empty lines
        data_lines = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
        
        # Check every 50th file to get a good sample
        sample_lines = data_lines[::50]  # Every 50th file
        
        for line in sample_lines:
            parts = line.split()
            if len(parts) >= 3:
                checksum = parts[0]
                size = parts[1]
                relative_path = ' '.join(parts[2:])  # Handle paths with spaces
                
                # Get absolute path
                file_path = workspace_root / relative_path
                
                if file_path.exists():
                    checked_files += 1
                    if verify_checksum(file_path, checksum):
                        verified_files += 1
                        print(f"✓ VERIFIED: {relative_path}")
                    else:
                        print(f"✗ FAILED: {relative_path}")
                        print(f"  Expected: {checksum}")
                        # Calculate actual checksum for debugging
                        try:
                            sha256_hash = hashlib.sha256()
                            with open(file_path, "rb") as f:
                                for chunk in iter(lambda: f.read(4096), b""):
                                    sha256_hash.update(chunk)
                            print(f"  Actual:   {sha256_hash.hexdigest()}")
                        except Exception as e:
                            print(f"  Error calculating actual: {e}")
                else:
                    print(f"⚠ FILE NOT FOUND: {relative_path}")
    
    print(f"\nVerification Summary:")
    print(f"Files checked: {checked_files}")
    print(f"Files verified: {verified_files}")
    print(f"Success rate: {(verified_files/checked_files*100):.1f}%" if checked_files > 0 else "No files checked")
    
    return verified_files == checked_files and checked_files > 0

if __name__ == "__main__":
    success = spot_check_checksums()
    if success:
        print("\n✓ All spot checks PASSED!")
        sys.exit(0)
    else:
        print("\n✗ Some spot checks FAILED!")
        sys.exit(1)