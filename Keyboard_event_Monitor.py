# ============================================================
# EDUCATIONAL KEYBOARD EVENT MONITOR
# ============================================================
# Purpose   : Demonstrates keyboard event handling in Python
#             as part of a cybersecurity internship exercise.
# Usage     : Run manually. Press ESC to stop.
# Legal     : For use only on your own devices with your own consent.
#             Unauthorized use on other people's systems is illegal.
#
# ============================================================

from pynput import keyboard
from datetime import datetime
import os

EVENT_LOG_FILE = "keyboard_events.txt"
STOP_KEY = keyboard.Key.esc

event_count = 0


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_to_file(text):
    with open(EVENT_LOG_FILE, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def on_key_press(key):
    global event_count

    timestamp = get_timestamp()

    event_message = f"[{timestamp}] Keyboard press event detected"

    print(event_message)
    log_to_file(event_message)

    event_count += 1

    if key == STOP_KEY:
        stop_message = (
            f"[{timestamp}] Stop event detected. "
            f"Total events recorded: {event_count}"
        )

        print(stop_message)
        log_to_file(stop_message)

        return False


def on_key_release(key):
    timestamp = get_timestamp()

    event_message = f"[{timestamp}] Keyboard release event detected"

    log_to_file(event_message)


def main():

    print("=" * 50)
    print("EDUCATIONAL KEYBOARD EVENT MONITOR")
    print("=" * 50)

    print(f"Recording events to: {os.path.abspath(EVENT_LOG_FILE)}")
    print("Press 'ESC' to stop monitoring.")

    session_start = (
        f"\n{'=' * 50}\n"
        f"Session started at: {get_timestamp()}\n"
        f"{'=' * 50}"
    )

    log_to_file(session_start)

    print("Monitor is running... Keyboard events will be recorded.")

    with keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release
    ) as listener:

        listener.join()


    print(f"\nEvents saved to: {os.path.abspath(EVENT_LOG_FILE)}")
    print(f"Total events recorded: {event_count}")


if __name__ == "__main__":
    main()
