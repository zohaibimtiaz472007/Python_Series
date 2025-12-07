import pyautogui
from datetime import datetime
import time
import os

folder_name = "screenshots"
os.makedirs(folder_name, exist_ok=True)

while True:
    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{folder_name}/screenshot_{time_now}.png")
    time.sleep(10) 
    