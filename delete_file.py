import os

# List of file paths to delete
files_to_delete = [
    "cve/tests/juniper/cve202421595.yaml",
    "cve/tests/juniper/cve202439521.yaml",
    "cve/tests/juniper/cve202439522.yaml",
    "cve/tests/juniper/cve202439523.yaml",
    "cve/tests/juniper/cve202439524.yaml",
    # "cve/tests/juniper/cve202439557.yaml",
    # "cve/tests/juniper/cve202439558.yaml",
    # "cve/tests/juniper/cve202439560.yaml",
    # "cve/tests/juniper/cve202439561.yaml",
    "cve/tests/juniper/cve202440405.yaml",
    "cve/tests/juniper/cve202440406.yaml",
    "cve/tests/juniper/cve202440407.yaml",
    "cve/tests/juniper/cve202440408.yaml",
    "cve/tests/juniper/cve202440409.yaml",
    "cve/tests/juniper/cve202440410.yaml",
    "cve/tests/juniper/cve202447489.yaml",
    "cve/tests/juniper/cve202447490.yaml",
    "cve/tests/juniper/cve202447491.yaml",
    "cve/tests/juniper/cve202447493.yaml",
    "cve/tests/juniper/cve202447496.yaml",
    "cve/tests/juniper/cve202447497.yaml",
    "cve/tests/juniper/cve202447505.yaml",
    "cve/tests/juniper/cve202447508.yaml",
    "cve/tests/juniper/cve202447509.yaml"
]

# Deleting each file if it exists
for file_path in files_to_delete:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
