# Webcam Access Detector - Educational Purpose Only
# pip install opencv-python psutil

import cv2, psutil, time
from datetime import datetime

SUSPICIOUS_PROCS = ["chrome", "firefox", "msedge", "zoom", "teams", "skype",
                    "discord", "obs64", "obs", "camera", "webcam", "python"]

def is_camera_free(index=0, timeout=2):
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  
    t0 = time.time()
    ok = False
    while time.time() - t0 < timeout:
        if cap.isOpened():
            ok, _ = cap.read()
            break
        time.sleep(0.1)
    if cap.isOpened():
        cap.release()
    return ok  

def find_suspicious_processes():
    found = []
    for p in psutil.process_iter(['pid','name','exe']):
        try:
            name = (p.info['name'] or "").lower()
            exe  = (p.info['exe'] or "")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        for s in SUSPICIOUS_PROCS:
            if s in name or s in exe.lower():
                found.append((p.info['pid'], p.info['name'], exe))
                break
    return found

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== Webcam Access Detector — {now} ===")
    free = is_camera_free()
    if free:
        print("[OK] Webcam opened successfully — no other obvious process locking it.")
    else:
        print("[ALERT] Webcam could NOT be opened — it may be in use by another app!")
        suspects = find_suspicious_processes()
        if suspects:
            print("\nPossible processes that might be using the camera (pid, name, path):")
            for pid, name, exe in suspects:
                print(f"{pid}\t{name}\t{exe}")
        else:
            print("No common camera-using processes found. (Run as Administrator for deeper checks.)")
    # Also append to a log for records
    with open("webcam_access_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} - camera_free={free} - suspects={len(suspects) if not free else 0}\n")
