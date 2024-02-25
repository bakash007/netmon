from scapy.all import sniff, IP, TCP, UDP
import socket

last_packet = None

def get_domain_name(ip):
    try:
        domain_name, _, _ = socket.gethostbyaddr(ip)
        return domain_name
    except socket.herror:
        return None


def packet_callback(packet):
    global last_packet

    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst

        current_packet = {src_ip,dst_ip}

        src_domain = get_domain_name(src_ip)
        dst_domain = get_domain_name(dst_ip)

        if current_packet != last_packet:
            print(f"Source IP: {src_ip}->{src_domain}, Destination IP: {dst_ip}->{dst_domain}")
            last_packet = current_packet

        
def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback,store=0, count =100) #count currently set to 100 for demonstration purposes

start_sniffing("Wi-Fi")
