##############################
## src: neek8044/TextSpammer
####

import time
import pyautogui

gui = pyautogui
done = 0
errors = 0

while True:
    print("")
    text = input("[?] What to spam: ")
    cycles = input("[?] How many times: ")
    fcycles = int(cycles)
    print("[i] You are given 10 seconds to click on a text field.")
    time.sleep(5)
    print("[i] 5 seconds left...")
    time.sleep(5)

    while fcycles > done:
        try:
            gui.typewrite(text)
            gui.press("enter")
            print("[*] Success!")
            done = done + 1
        except:
            print("[!] Error occured. Trying again...")
            done = done - 1
            errors = errors + 1

    print(f"[i] Task completed successfully with {errors} errors")