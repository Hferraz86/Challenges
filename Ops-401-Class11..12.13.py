#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

#!/usr/bin/env python3

import subprocess
import ipaddress

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

def scan_ports(ip_address):
    """
    Scan ports on a given IP address.
    For demonstration, this function prints the scan results.
    """
    # Replace with your port scanning logic using Scapy or another library
    print(f"Scanning ports on {ip_address}...")

def main():
    # Ask user for target network address in CIDR notation
    target_cidr = input("Enter the target network address in CIDR notation (e.g., 192.168.1.0/24): ").strip()

    try:
        # Generate list of IP addresses in the specified network
        network = ipaddress.ip_network(target_cidr)
    except ValueError as e:
        print(f"Invalid network address: {e}")
        return

    # Perform ping and port scan for each IP in the network
    for ip in network.hosts():
        ip_address = str(ip)
        print(f"Pinging {ip_address}...")
        if ping_host(ip_address):
            print(f"{ip_address} is reachable.")
            # Perform port scan if host is reachable
            scan_ports(ip_address)
        else:
            print(f"{ip_address} is down or unresponsive.")
            print(f"Skipping port scan for {ip_address} since the host is unresponsive.")

if __name__ == "__main__":
    main()
