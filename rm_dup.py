import os
import hashlib

def calculate_file_hash(file_path):
    """Calculate the SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicate_files(directory):
    """Remove duplicate files in the given directory."""
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        return

    seen_hashes = {}
    duplicates_removed = 0

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)

            if file_hash in seen_hashes:
                print(f"Duplicate found: {file_path} (Duplicate of {seen_hashes[file_hash]})")
                os.remove(file_path)
                duplicates_removed += 1
            else:
                seen_hashes[file_hash] = file_path

    print(f"Duplicates removed: {duplicates_removed}")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to check for duplicates: ").strip()
    remove_duplicate_files(target_directory)
