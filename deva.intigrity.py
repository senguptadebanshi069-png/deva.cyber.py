import hashlib
import os

def calculate_sha256(file_path):
    """Calculates the SHA-256 hash value of a given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def monitor_file():
    print("--- Devanix Cyber: File Integrity Checker ---")
    target_file = input("Enter the filename or path to monitor (e.g., test.txt): ")
    
    if not os.path.exists(target_file):
        print(" Error: File not found. Please create the file first.")
        return

    original_hash = calculate_sha256(target_file)
    print(f"\n Baseline Fingerprint Generated (Original SHA-256 Hash):")
    print(f" {original_hash}")
    print("\n[System is now monitoring the file...]")
    
    input("\nGo to your system, modify and save the file, then press Enter here to verify...")
    
    current_hash = calculate_sha256(target_file)
    print(f"\n Current Fingerprint (Current SHA-256 Hash):")
    print(f" {current_hash}")
    
    if original_hash == current_hash:
        print("\n Green Signal: File integrity is intact. No unauthorized modifications detected.")
    else:
        print("\n ALERT: File integrity has been compromised! The content was modified.")

if __name__ == "__main__":
    monitor_file()
