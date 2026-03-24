# Smart Network Scanner & Reporter

A Python-based automated network scanning tool built using Nmap to identify open ports, services, and generate structured reports.

---

## Features

* Port Scanning (1–1024)
* Service Detection
* Input Validation
* Error Handling
* Report Generation
* Multi-target Support (optional)

---

## Tech Stack

* Python
* Nmap
* Linux (Kali)

---

## Use Case

Used in the reconnaissance phase of penetration testing to identify open ports and running services.

---

## Disclaimer

This tool is for educational purposes only. Use it only on systems you own or have permission to test.

---

## How to Run

```bash
pip install -r requirements.txt
python scanner.py
```

---

## Sample Output

```text
Port: 80 | State: open | Service: http
Port: 22 | State: open | Service: ssh
```
