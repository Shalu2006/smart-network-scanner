import nmap
import shutil
from utils import validate_target, save_report

def check_nmap():
    """
    Check if Nmap is installed on the system.
    """
    if not shutil.which("nmap"):
        print("[!] Nmap is not installed. Please install it first.")
        return False
    return True


def scan_target(target, ports="1-1024"):
    """
    Scans a target for open ports and services using Nmap.
    """
    scanner = nmap.PortScanner()

    try:
        print(f"\n[+] Scanning Target: {target}")

        # -sS: SYN scan, -sV: service detection
        scanner.scan(target, ports, arguments='-sS -sV')

        if not scanner.all_hosts():
            print("[!] No hosts found.")
            return None

        results = []

        for host in scanner.all_hosts():
            print(f"\nHost: {host}")
            print(f"State: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"Protocol: {proto}")

                ports_list = sorted(scanner[host][proto].keys())

                for port in ports_list:
                    port_data = scanner[host][proto][port]

                    state = port_data.get('state', 'unknown')
                    service = port_data.get('name', 'unknown')

                    result = f"Port: {port} | State: {state} | Service: {service}"
                    print(result)
                    results.append(result)

        return results

    except Exception as e:
        print(f"[!] Error scanning {target}: {e}")
        return None


def main():
    print("=== Smart Network Scanner ===")

    if not check_nmap():
        return

    target = input("Enter target IP or domain: ").strip()

    if not validate_target(target):
        print("[!] Invalid IP/Domain. Please try again.")
        return

    ports = input("Enter port range (default 1-1024): ").strip()
    if not ports:
        ports = "1-1024"

    results = scan_target(target, ports)

    if results:
        save_report(target, results)
        print("\n[+] Scan completed and report saved.")
    else:
        print("[!] No results to save.")


if __name__ == "__main__":
    main()
