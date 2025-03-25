import random
import ipaddress

def generate_routes(num_routes=200000):
    # Protocol definitions
    protocols = {
        'O': '[110/2] via',
        'B': '[200/0] via',
        'D': '[90/2] via',
        'S': '[1/0] via',
        'R': '[120/1] via',
        'E1': '[110/3] via',
        'E2': '[110/1] via',
        'N1': '[110/2] via',
        'N2': '[110/2] via'
    }
    
    # Common next-hop interfaces
    interfaces = [
        'GigabitEthernet1',
        'GigabitEthernet2',
        'GigabitEthernet3',
        'TenGigabitEthernet1',
        'FastEthernet0/0',
        'FastEthernet0/1'
    ]
    
    routes = []
    used_networks = set()  # To avoid duplicate networks
    
    for _ in range(num_routes):
        # Generate random network (avoiding RFC1918 for variety)
        while True:
            first_octet = random.randint(1, 223)
            if first_octet not in [10, 172, 192]:  # Avoid private ranges
                network = f"{first_octet}.{random.randint(0, 255)}.{random.randint(0, 255)}.0"
                mask = random.randint(24, 30)  # Common subnet masks
                network_with_mask = f"{network}/{mask}"
                
                if network_with_mask not in used_networks:
                    used_networks.add(network_with_mask)
                    break
        
        # Generate random next-hop IP
        next_hop = f"10.10.{random.randint(1, 254)}.{random.randint(1, 254)}"
        
        # Select random protocol and its metric
        protocol = random.choice(list(protocols.keys()))
        metric_info = protocols[protocol]
        
        # Select random interface
        interface = random.choice(interfaces)
        
        # Create route entry
        route = f"{protocol}     {network_with_mask} {metric_info} {next_hop}, {interface}"
        routes.append(route)
    
    return routes

def main():
    # Generate routes
    new_routes = generate_routes()
    
    # Read existing file
    template_file = "/home/user/mockit/configs/cisco_ios/templates/show ip route.txt"
    try:
        with open(template_file, 'r') as f:
            existing_content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {template_file}")
        return
    
    # Find the position to insert new routes (after the header)
    header_end = existing_content.find("Gateway of last resort")
    if header_end == -1:
        print("Error: Could not find appropriate position to insert routes")
        return
    
    # Split content and get just the header
    header = existing_content[:header_end]
    
    # Create new content with just the header and new routes
    new_content = header + "\n".join(new_routes)
    
    # Write to a new file
    output_file = "/home/user/mockit/configs/cisco_ios/templates/show ip route.txt"
    with open(output_file, 'w') as f:
        f.write(new_content)
    
    print(f"Successfully generated {len(new_routes)} new routes")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    main() 