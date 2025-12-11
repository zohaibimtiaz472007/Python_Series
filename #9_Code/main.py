import os

# Suspicious keywords (educational purposes)
SUSPICIOUS = ["keylogger", "stealer", "rat", "token", "grabber", "spy", "malware"]

def scan_directory(path):
    print(f"\n[+] Scanning: {path}")
    found = False

    for root, dirs, files in os.walk(path):
        for file in files:
            lower_name = file.lower()
            for word in SUSPICIOUS:
                if word in lower_name:
                    found = True
                    print(f"[!] Suspicious file found: {os.path.join(root, file)}")
    
    if not found:
        print("[-] No suspicious files found.")

if __name__ == "__main__":
    # Scan common folders
    folders = [
        os.path.expanduser("~\\Downloads"),
        os.path.expanduser("~\\Documents"),
        os.path.expanduser("~\\AppData\\Local"),
        os.path.expanduser("~\\AppData\\Roaming")
    ]

    print("=== Hidden Malware Detector (Educational Purpose Only) ===")

    for folder in folders:
        if os.path.exists(folder):
            scan_directory(folder)
