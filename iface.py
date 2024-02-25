import psutil

''' I experimented with formating some colors for the output
    \033[0m - white
    \033[92m - green
    \033[93m - yellow
    \033[96m - cyan
'''
def list_network_interfaces():
    for interface, addrs in psutil.net_if_addrs().items():
        #if interface == "Wi-Fi":
        for addr in addrs:
            if "." in addr.address: #Because only IPv4 addresses are seperated by ".". I know its whack but gotta roll with it
                print(f"\033[0mInterface: \033[96m{interface}")
                print(f"  \033[0mAddress: \033[93m{addr.address}")
                print()

def get_interface():
    for interface, addrs in psutil.net_if_addrs().items():
        if "Wi-Fi" in interface:
            return interface
    return None

list_network_interfaces()

interface_name = get_interface()

if interface_name is not None:
    print(f"\033[92mwi-Fi interface found: {interface_name}")
else:
    print("Error: Interface was not found.")
