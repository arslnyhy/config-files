from ncclient import manager
from lxml import etree

# Define the BGP filter using the correct Cisco IOS XE namespace
bgp_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <bgp/>
        </router>
    </native>
</filter>
"""

# Connect to the device
with manager.connect(
    host='localhost',
    port=830,
    username='test',
    password='test',
    hostkey_verify=False
) as m:
    
    # Get the running configuration with the BGP filter
    running_config = m.get_config('running', filter=bgp_filter)
    
    # Parse the XML response and print the BGP section
    print(etree.tostring(running_config.data, pretty_print=True).decode())
