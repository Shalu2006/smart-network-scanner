import re
import os
import socket

def validate_target(target):
    """
    Validates if the input is a valid IP address or domain name.
    """
    # Check for valid IP
    try:
        socket.inet_aton(target)
        return True
    except socket.error:
        pass

    # Check for valid domain
    domain_pattern = r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(domain_pattern, target):
        return True

    return False


def sanitize_filename(name):
    """
    Removes invalid characters from filename.
    """
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def save_report(target, results):
    """
    Saves scan results into a file with proper error handling.
    """
    try:
        os.makedirs("report", exist_ok=True)

        safe_target = sanitize_filename(target)
        file_path = f"report/{safe_target}_report.txt"

        with open(file_path, "w") as file:
            file.write(f"Scan Report for {target}\n")
            file.write("=" * 40 + "\n")

            for line in results:
                file.write(line + "\n")

        print(f"[+] Report saved: {file_path}")

    except Exception as e:
        print(f"[!] Error saving report: {e}")
