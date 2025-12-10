# EDUCATIONAL PURPOSE ONLY
# Automatically saves copied text from clipboard to a file

import pyperclip
import time
from datetime import datetime

last_text = ""

print("Clipboard auto saver is running...")

while True:
    try:
        text = pyperclip.paste()

        if text != last_text and text.strip() != "":
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open("clipboard_logs.txt", "a", encoding="utf-8") as f:
                f.write(f"[{time_now}] {text}\n")

            print("New text saved from clipboard ✅")
            last_text = text

        time.sleep(2)  

    except KeyboardInterrupt:
        print("Stopped")
        break
