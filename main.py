import time
import sys
import pyautogui

def help():
    print("usage:")
    print(f"  autoclicker CLICK_INTERVAL START_DELAY NUMBER_OF_CLICKS")
    exit(1)

if len(sys.argv) != 4:
    help()

click_interval = float(sys.argv[1])
start_delay = float(sys.argv[2])
number_of_clicks = int(sys.argv[3])
abort_offset = 10

print(f"Starting in {start_delay} second.")
time.sleep(start_delay)

start_pos = pyautogui.position()

for i in range(number_of_clicks):
    pyautogui.click()
    time.sleep(click_interval)
    pos = pyautogui.position()
    offset = abs(pos[0] - start_pos[0]) + abs(pos[1] - start_pos[1])
    if offset > abort_offset:
        print(f"Mouse position changed by {offset}, abort offset is {abort_offset}. Stopping autoclicker.")
        break
