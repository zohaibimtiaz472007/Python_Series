

# EDUCATIONAL PURPOSE ONLY

from pynput import mouse
import pyautogui
from datetime import datetime
import os


folder = "click_screenshots"
os.makedirs(folder, exist_ok=True)

def on_click(x, y, button, pressed):
    if pressed:
        time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"{folder}/screenshot_{time_now}.png")
        print(f"Screenshot captured at ({x}, {y})")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
 