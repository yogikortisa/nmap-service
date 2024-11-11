import nmap3
nmap = nmap3.Nmap()

def scan_ip(ip_address):
    results = nmap.scan_top_ports(ip_address, args="-sT")
    return results