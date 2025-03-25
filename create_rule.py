import os
import argparse

cve_names = [
    "CVE-2025-20172",
    "CVE-2025-20174",
    "CVE-2025-20176",
]

def create_cve_files(dry_run=False):
    destination_folder = "/home/user/cveasy/rules/cisco/2025/ios"
    total_files = len(cve_names)
    created_files = 0

    if dry_run:
        print(f"Total files to be created: {total_files}")
        print(f"Destination: {destination_folder}")
        for cve in cve_names:
            filename = f"{cve.lower().replace('-', '')}.py"
    else:
        os.makedirs(destination_folder, exist_ok=True)
        for cve in cve_names:
            filename = f"{cve.lower().replace('-', '')}.py"
            file_path = os.path.join(destination_folder, filename)
            
            with open(file_path, 'w') as f:
                f.write(f'# Placeholder for CVE script\n')
            created_files += 1
        print(f"Created {created_files} files in {destination_folder}")

def main():
    parser = argparse.ArgumentParser(description='Create CVE files')
    parser.add_argument('--dry-run', action='store_true', 
                      help='Show what would be created without actually creating files')
    args = parser.parse_args()

    create_cve_files(dry_run=args.dry_run)

if __name__ == "__main__":
    main() 