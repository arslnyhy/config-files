import os
from pathlib import Path

# XML template
xml_template = '''<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply message-id="{message_id}"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <data>
        Hello from {platform}!
    </data>
</rpc-reply>
'''

def get_platforms():
    """Dynamically get platforms by listing directories in configs folder"""
    base_dir = Path('configs')
    
    # Create base configs directory if it doesn't exist
    base_dir.mkdir(exist_ok=True)
    
    # Get all directories in configs folder
    platforms = [d.name for d in base_dir.iterdir() if d.is_dir()]
    return platforms

def create_netconf_files():
    base_dir = Path('configs')
    platforms = get_platforms()
    
    if not platforms:
        print("No platform directories found in configs folder!")
        return
    
    print(f"Found platforms: {', '.join(platforms)}")
    
    for platform in platforms:
        # Create templates/netconf directory
        netconf_dir = base_dir / platform / 'netconf'
        netconf_dir.mkdir(exist_ok=True, parents=True)
        
        # Create get-config.xml file
        config_file = netconf_dir / 'get-config.xml'
        
        # Write the XML content, only formatting the platform name
        with open(config_file, 'w') as f:
            # Include message_id in the dict to keep it as a literal string
            f.write(xml_template.format_map({
                'platform': platform,
                'message_id': '{message_id}'
            }))
        
        print(f"Created: {config_file}")

if __name__ == "__main__":
    create_netconf_files()