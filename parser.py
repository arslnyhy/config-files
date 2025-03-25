import json
import glob
import os
from openpyxl import Workbook

# Define the path to the directory containing all subdirectories with JSON files
base_directory_path = '/home/user/cvelistV5/cves/2021'
output_excel = '/home/user/cve-vendors/cisco_2021.xlsx'

# Create a new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Cisco CVEs"

# Define the headers for the Excel file
headers = ['cve_id', 'cve_name', 'vendor', 'product', 'versions', 'device_name', 'device_ipaddress', 'os_version', 'url']
ws.append(headers)

# Use glob to find all JSON files in any subdirectory under the base path
found_files = glob.glob(os.path.join(base_directory_path, "*", "*.json"))

# Check if any files were found
if not found_files:
    print("No JSON files found in the specified directory structure.")
else:
    print(f"Found {len(found_files)} JSON files.")

# Iterate over the files found
for filepath in found_files:
    print(f"Processing file: {filepath}")  # Debug print to show each file path
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            
            # Check if 'Cisco' is listed as a vendor in the affected section
            affected_products = data.get("containers", {}).get("cna", {}).get("affected", [])
            for product in affected_products:
                if product.get("vendor") == "Cisco":
                    # Extract the URL if available
                    references = data.get("containers", {}).get("cna", {}).get("references", [])
                    url = references[0].get("url") if references else ""  # Get the first URL if present
                    
                    # Extract fields to write to Excel
                    row_data = [
                        data.get("cveMetadata", {}).get("cveId"),  # cve_id
                        data.get("containers", {}).get("cna", {}).get("title"),  # cve_name
                        product.get("vendor"),  # vendor
                        product.get("product"),  # product
                        ', '.join([ver.get("version") for ver in product.get("versions", [])]),  # versions
                        "",  # device_name placeholder
                        "",  # device_ipaddress placeholder
                        "",  # os_version placeholder
                        url  # url field
                    ]
                    
                    # Append the row to the sheet
                    ws.append(row_data)
                    print(f"Added CVE: {row_data[0]} with URL: {url}")  # Debug print to confirm CVE is added
                    break  # Stop further checks if Cisco is found
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {filepath}")
    except Exception as e:
        print(f"Unexpected error with file {filepath}: {e}")

# Save the workbook to a file if any files were processed
if found_files:
    wb.save(output_excel)
    print(f"Filtered Cisco CVEs have been written to {output_excel}")
