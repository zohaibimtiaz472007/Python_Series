from pynput import mouse
from datetime import datetime

log_file = "mouse_logs.txt"

def on_click(x, y, button, pressed):
    if pressed:
        with open(log_file, "a") as f:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{time}] Button: {button} | Position: ({x}, {y})\n")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
