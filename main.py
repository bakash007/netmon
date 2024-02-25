import psutil

def list_network_interfaces():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == "Wi-Fi" or interface == "Ethernet":
            for addr in addrs:
                if "." in addr.address:                       #because only IPv4 addresses are seperated by ".". I know its whack but gotta roll with it
                    print(f"Interface: {interface}")
                    print(f"  Address: {addr.address}")

def get_wifi_interface():
    for interface, addrs in psutil.net_if_addrs().items():
        if "Wi-Fi" in interface:
            return interface
    return None

if __name__ == "__main__":
    list_network_interfaces()
    
    interface_name = get_wifi_interface()

    if interface_name is not None:
        print(f"Wi-Fi interface found: {interface_name}")
    else:
        print("Error: Wi-Fi interface not found.")

