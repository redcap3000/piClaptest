from sense_hat import SenseHat
import time
import subprocess
import sys

# Configuration constants
DURATION = 2
OUTPUT_FILE = "clap_capture.wav"
COUNTDOWN_START = 5

# Initialize the hardware
sense = SenseHat()

def clear_display():
    # Clears all LEDs
    sense.clear()

def show_waiting_state():
    # Shows a red question mark to indicate standby
    sense.show_letter("?", text_colour=[255, 0, 0])

def run_countdown():
    # Performs the numerical countdown on the LED matrix
    for i in range(COUNTDOWN_START, 0, -1):
        sense.show_letter(str(i), text_colour=[255, 255, 255])
        time.sleep(1)

def main():
    clear_display()
    show_waiting_state()
    print("------------------------------------------")
    print("SENSE HAT CLAP TEST: STANDBY")
    print("[Action] Press the Joystick Click to Start")
    print("------------------------------------------")

    while True:
        event = sense.stick.wait_for_event()
        while event is not None:
            # Check for joystick click activation
            print(event)
            if event.action == "pressed" and event.direction == "middle":
                print("\n[!] Trigger Detected! Starting Countdown...")
                run_countdown()
                print("*** !!! CLAP NOW !!! ***")

                cmd = [
                    "arecord",
                    "-d", str(DURATION),
                    "-f", "cd",
                    "-t", "wav",
                    "-r", "44100",
                    "-c", "1",
                    OUTPUT_FILE
                ]

                try:
                    subprocess.run(cmd, check=True)
                    print("------------------------------------------")
                    print("SUCCESS: Audio file created.")
                    sense.show_letter("!", text_colour=[0, 255, 0])
                    time.sleep(3)
                    clear_display()
                    sys.exit(0)
                except Exception:
                    print("Error: Recording failed")
                    sense.show_letter("X", text_colour=[255, 0, 0])

                time.sleep(3)
                clear_display()
                show_waiting_state()
                print("\n[!] Ready for next test. Press Joystick again.")
            elif event.action == "release":
                if event.name != "middle":
                    print("Input ignored. Use Click only.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTest terminated by user.")
        sense.clear()
        sys.exit(0)
