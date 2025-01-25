# Nmap Automation Script

## Overview
This Python script automates various types of Nmap scans, making it easier for security analysts and network administrators to assess the security and performance of their systems. The results are neatly saved in a `report` folder for future reference.

## Features
- Supports multiple Nmap scan types:
  - **Basic Scan:** `nmap -T4 -F`
  - **Service and Version Detection:** `nmap -sV -T5 -p-`
  - **High-Speed Scan:** `nmap --min-rate 10000 -p-`
  - **Common Ports Script Scan:** `nmap -sC -vv -p21,22,25,110,443,587,3306`
  - **Comprehensive Scan:** `nmap -sC -sV -vv -p-`
- Predefined scan for common ports:
  - FTP, SSH, Telnet, HTTP, HTTPS, SMTP, and more.
- Saves scan results in plain text format in a `report` folder for easy access.
- User-friendly menu for selecting the scan type.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Salman-TCM/nmapautomation.git
   cd nmapautomation
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script:**
   ```bash
   python scan.py
   ```

2. **Select a scan type from the menu:**
   Enter the number corresponding to the scan type you want to execute.

3. **View the results:**
   Scan results are saved in the `report` folder with filenames indicating the scan type and timestamp.

## Requirements
- Python 3.12 or later
- Dependencies (installed via `requirements.txt`):
  - `python-nmap`
  - `requests`
  - `numpy`

## Example Output

After running a scan, the result file in the `report` folder looks like this:

```
Scan Type: Service and Version Detection
Target: 192.168.1.1
Date: 2025-01-25 12:30:45

Open Ports:
- Port 21 (FTP)
- Port 22 (SSH)
- Port 80 (HTTP)

Detailed Results:
- Port 21: FTP service running (vsftpd 3.0.3)
- Port 22: OpenSSH 7.9p1 Debian
- Port 80: Apache 2.4.41
```

## Supported Scan Types
1. **Basic Scan:** Quickly scans common ports.
2. **Service and Version Detection:** Detects running services and versions on all ports.
3. **High-Speed Scan:** Prioritizes scan speed for large networks.
4. **Common Ports Script Scan:** Runs scripts against frequently used ports like FTP, SSH, HTTP, and more.
5. **Comprehensive Scan:** Thoroughly scans all ports with service and script detection.
6. **Custom Ports Scan:** Focuses on user-specified ports.

### Predefined Common Ports
| Port  | Service             |
|-------|---------------------|
| 21    | FTP                 |
| 22    | SSH                 |
| 23    | Telnet              |
| 25    | SMTP (mail)         |
| 53    | DNS (UDP)           |
| 67, 68| DHCP (UDP)          |
| 69    | TFTP (UDP)          |
| 80    | HTTP                |
| 443   | HTTPS               |
| 110   | POP3 (mail)         |
| 111   | ONC RPC             |
| 139, 445 | SMB              |
| 1433  | MSSQL               |
| 1978  | WiFi Mouse          |
| 2049  | NFS                 |
| 3306  | MySQL               |
| 3389  | RDP                 |
| 5900  | VNC                 |
| 5985  | WinRM HTTP          |
| 5986  | WinRM HTTPS         |

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Make sure to follow the coding standards and document your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This tool is intended for authorized testing and educational purposes only. Unauthorized use on networks without permission is illegal.

---
Enjoy automated network scanning with this powerful script!
