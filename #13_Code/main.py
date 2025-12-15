"""
Educational Purpose Only ⚠️
This script demonstrates how brute-force attacks work
using a HARD-CODED password.
Do NOT use this on real accounts or systems.
"""
import time

# Simulated correct password (hardcoded)
correct_password = "1234"

# Possible password attempts
attempts = ["0000", "1111", "2222", "1234", "4321"]

print("Starting brute-force simulation...\n")

for password in attempts:
    print(f"Trying password: {password}")
    time.sleep(1)  # delay to simulate real attempts

    if password == correct_password:
        print("\n✅ Password cracked successfully!")
        print(f"Correct Password: {password}")
        break
else:
    print("\n❌ Password not found")
