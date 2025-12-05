import os
import shutil
import subprocess

# Paths to clean
paths = [
    r"C:\Windows\Temp",
    r"C:\Users\%USERNAME%\AppData\Local\Temp",
    
]

def clean_path(path):
    path = os.path.expandvars(path)

    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return
    
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, ignore_errors=True)
        except:
            pass
    
    print(f"Cleaned: {path}")

# Clear Recycle Bin
def clear_recycle_bin():
    subprocess.call(["powershell", "-Command", "Clear-RecycleBin -Force"], shell=True)
    print("Recycle Bin Cleared")

# MAIN
print("Cleaning started...")
for p in paths:
    clean_path(p)

clear_recycle_bin()
print("Your PC is now clean & faster!")
