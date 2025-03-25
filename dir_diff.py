import os
import hashlib

def calculate_file_hash(file_path):
    """Calculate the SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_files_with_hashes(directory):
    """Get all files in a directory with their relative paths and hashes."""
    files_with_hashes = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, directory)
            file_hash = calculate_file_hash(file_path)
            files_with_hashes[relative_path] = file_hash
    return files_with_hashes

def remove_uncommon_files(dir1, dir2):
    """Remove files that are not common between two directories."""
    dir1_files = get_files_with_hashes(dir1)
    dir2_files = get_files_with_hashes(dir2)

    common_files = {
        file for file in dir1_files
        if file in dir2_files and dir1_files[file] == dir2_files[file]
    }

    for file in dir1_files:
        if file not in common_files:
            os.remove(os.path.join(dir1, file))
            print(f"Removed from Directory 1: {file}")

    for file in dir2_files:
        if file not in common_files:
            os.remove(os.path.join(dir2, file))
            print(f"Removed from Directory 2: {file}")

    print("\nCleanup complete. Only common files remain.")

if __name__ == "__main__":
    dir1 = input("Enter the path of the first directory: ").strip()
    dir2 = input("Enter the path of the second directory: ").strip()

    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        print("One or both of the provided paths are not valid directories.")
    else:
        remove_uncommon_files(dir1, dir2)
