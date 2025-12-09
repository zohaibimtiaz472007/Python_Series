# EDUCATIONAL PURPOSE ONLY

import subprocess
import time

def get_connected_devices():
    result = subprocess.check_output("arp -a", shell=True).decode(errors="ignore")
    devices = set()

    for line in result.split("\n"):
        if "-" in line:
            parts = line.split()
            if len(parts) >= 2:
                ip = parts[0]
                mac = parts[1]
                devices.add((ip, mac))
    return devices


print("Monitoring WiFi for new devices...\n")

known_devices = get_connected_devices()

while True:
    time.sleep(10)  # check every 10 seconds
    current_devices = get_connected_devices()

    new_devices = current_devices - known_devices

    for device in new_devices:
        print(f"⚠️ New device connected -> IP: {device[0]} | MAC: {device[1]}")

    known_devices = current_devices
