#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

#!/usr/bin/env python3

import subprocess
import ipaddress
from scapy.all import *

def ping_host(ip_address):
    """
    Ping a given IP address and return True if it responds, False otherwise.
    """
    try:
        # Ping with a timeout of 2 seconds (-W 2)
        result = subprocess.run(['ping', '-c', '1', '-W', '2', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if result.returncode == 0:
            return True
        else:
            return False
    except subprocess.TimeoutExpired:
        return False
    except Exception as e:
        print(f"Error pinging {ip_address}: {str(e)}")
        return False

def scan_ports(ip_address, port_range):
    """
    Scan ports on a given IP address.
    """
    open_ports = []
    for port in port_range:
        # Send SYN packet
        syn_packet = IP(dst=ip_address) / TCP(dport=port, flags='S')
        response = sr1(syn_packet, timeout=1, verbose=0)

        if response:
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK
                    open_ports.append(port)
                    # Send RST packet to close the open connection
                    rst_packet = IP(dst=ip_address) / TCP(dport=port, flags='R')
                    send(rst_packet, verbose=0)
                elif response[TCP].flags == 0x14:  # RST-ACK
                    pass  # Port is closed
            elif response.haslayer(ICMP):
                if int(response[ICMP].type) == 3 and int(response[ICMP].code) in [1, 2, 3, 9, 10, 13]:
                    print(f"Port {port} is filtered.")
        else:
            print(f"Port {port} is filtered or silently dropped.")

    return open_ports

def main():
    # Ask user for target network address in CIDR notation
    target_cidr = input("Enter the target network address in CIDR notation (e.g., 192.168.1.0/24): ").strip()

    try:
        # Generate list of IP addresses in the specified network
        network = ipaddress.ip_network(target_cidr)
    except ValueError as e:
        print(f"Invalid network address: {e}")
        return

    # Define the range of ports to scan
    port_range = range(20, 1025)  # Adjust the port range as needed

    # Perform ping and port scan for each IP in the network
    for ip in network.hosts():
        ip_address = str(ip)
        print(f"Pinging {ip_address}...")
        if ping_host(ip_address):
            print(f"{ip_address} is reachable.")
            # Perform port scan if host is reachable
            open_ports = scan_ports(ip_address, port_range)
            if open_ports:
                print(f"Open ports on {ip_address}: {open_ports}")
            else:
                print(f"No open ports found on {ip_address}.")
        else:
            print(f"{ip_address} is down or unresponsive.")
            print(f"Skipping port scan for {ip_address} since the host is unresponsive.")

if __name__ == "__main__":
    main()
