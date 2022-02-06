##############################
## src: neek8044/TextSpammer
####

# Imports
from colorama import Fore, Style
import time
import pyautogui

# Initialization
version = '0.2'
gui = pyautogui
done = 0
errors = 0

F = Fore
SR = Style.RESET_ALL

# Startline
print("")
print(f"{F.LIGHTMAGENTA_EX}Text Spammer - Version: " + version)

while True:
    print("")

    # User inputs
    text = input(f"{F.YELLOW}[?] What to spam: {SR}")
    cycles = input(f"{F.YELLOW}[?] How many times: {SR}")
    fcycles = int(cycles)

    # Delay before running
    print(f"{F.CYAN}[i] You are given 10 seconds to click on a text field.{SR}")
    time.sleep(5)
    print(f"{F.CYAN}[i] 5 seconds left...{SR}")
    time.sleep(5)

    # While given cycles are more than how many are done, continue.
    while fcycles > done:
        try:
            gui.typewrite(text)
            gui.press("enter")
            print(f"{F.LIGHTGREEN_EX}[*] Success!")
            done = done + 1
        except:
            print(f"{F.RED}[!] Error occured. Trying again...{SR}")
            done = done - 1
            errors = errors + 1

            # If errors are more than cycles given * 2, stop running.
            if errors > fcycles * 2:
                done = fcycles # Sets done = cycles in order to stop the while loop
                print(f"{F.LIGHTRED_EX}[x] Critical error: too many tries. Script automatically stopped.")

    print(f"{F.CYAN}[i] Task completed.")