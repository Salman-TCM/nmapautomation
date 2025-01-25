import subprocess
import os
from datetime import datetime

def run_nmap_scan(target, scan_type):

    try:
        if scan_type == "1":
            print(f"[*] Running a basic port scan on {target}...")
            command = ["nmap", "-sS", target]
            scan_name = "basic_port_scan"
        elif scan_type == "2":
            print(f"[*] Running a service version scan on {target}...")
            command = ["nmap", "-sV", target]
            scan_name = "service_version_scan"
        elif scan_type == "3":
            print(f"[*] Running an OS detection scan on {target}...")
            command = ["nmap", "-O", target]
            scan_name = "os_detection_scan"
        elif scan_type == "4":
            print(f"[*] Running an aggressive scan on {target}...")
            command = ["nmap", "-A", target]
            scan_name = "aggressive_scan"
        elif scan_type == "5":
            print(f"[*] Scanning all ports on {target}...")
            command = ["nmap", "-p-", target]
            scan_name = "all_ports_scan"
        elif scan_type == "6":
            print(f"[*] Running a fast service version scan (-sV -T5 -p-) on {target}...")
            command = ["nmap", "-sV", "-T5", "-p-", target]
            scan_name = "fast_service_version_scan"
        elif scan_type == "7":
            print(f"[*] Running a high-speed scan (--min-rate 10000 -p-) on {target}...")
            command = ["nmap", "--min-rate", "10000", "-p-", target]
            scan_name = "high_speed_scan"
        elif scan_type == "8":
            print(f"[*] Running a script scan for specified ports on {target}...")
            ports = ",".join([
                "21", "22", "23", "25", "53", "67", "68", "69", "80", "443",
                "110", "111", "143", "161", "139", "445", "1433", "1978",
                "2049", "3306", "3389", "5900", "5985", "5986"
            ])
            command = ["nmap", "-sC", "-vv", f"-p{ports}", target]
            scan_name = "script_scan_specific_ports"
        elif scan_type == "9":
            print(f"[*] Running a Professional scan (-sC -sV -vv -p-) on {target}...")
            command = ["nmap", "-sC", "-sV", "-vv", "-p-", target]
            scan_name = "Professional Scan"
        else:
            print("[!] Invalid scan type selected. Exiting.")
            return
        result = subprocess.run(command, capture_output=True, text=True)
        report = os.path.join(os.getcwd(), 'report')
        if not os.path.exists(report):
            os.makedirs(report)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{target}_{scan_name}_{timestamp}.txt"
        file_path = os.path.join(report, filename)
        

        with open(file_path, "w") as file:
            file.write(result.stdout)

        print("\n[+] Scan Results:\n")
        print(result.stdout)
        print(f"\n[+] Scan results saved to: {file_path}")

    except Exception as e:
        print(f"[!] An error occurred: {e}")


def main():
    print("=== Nmap Automation Script ===")
    print("Select the type of scan you want to perform:")
    print("1. Basic Port Scan (-sS)")
    print("2. Service Version Scan (-sV)")
    print("3. OS Detection Scan (-O)")
    print("4. Aggressive Scan (-A)")
    print("5. Scan All Ports (-p-)")
    print("6. Fast Service Version Scan (-sV -T5 -p-)")
    print("7. High-Speed Scan (--min-rate 10000 -p-)")
    print("8. Script Scan for Common Ports (-sC -vv -p21,22,23,25,53,67,68,69,80,443,110,111,143,161,139,445,1433,1978,2049,3306,3389,5900,5985,5986)")
    print("9. Professional Scan (-sC -sV -vv -p-)\n")

    scan_type = input("Enter the scan type (1-9): ").strip()
    target = input("Enter the target IP or domain: ").strip()

    if target:
        run_nmap_scan(target, scan_type)
    else:
        print("[!] No target specified. Exiting.")

if __name__ == "__main__":
    main()
