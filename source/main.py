##########################################
## src: github.com/neek8044/TextSpammer ##
##########################################

# Imports
from colorama import Fore
import time
from os import system
import pip

system('cls')
# Configuring colorama
F = Fore
R = Fore.RESET

# Trying to import pyautogui library
try:
    import pyautogui
except ImportError:
    print(f"{F.LIGHTRED_EX}[!] Error while importing pyautogui library.")
    print(f"{F.GREEN}[+] Installing library via pip...{R}")
    pip.main(['install', 'pyautogui'])
    import pyautogui

# Initialization
__version__ = '22.04.02'
gui = pyautogui
done = 0
errors = 0

# Wait function using the time library
def wait(s):
    time.sleep(s)

##################################################

print(f"{F.LIGHTMAGENTA_EX}Text Spammer - Version " + __version__)

while True:
    print("")

    # Asks what phrase to spam and for how many times
    text = input(f"{F.YELLOW}[/] Text to spam: {R}")
    repeats = input(f"{F.YELLOW}[/] Repeats: {R}")
    repeats = int(repeats)

    # Delay before running so the user can click on a textbox
    print(f"{F.CYAN}[i] You are given 10 seconds to click on a text field.{R}")
    wait(5)
    print(f"{F.CYAN}[i] 5 seconds left...{R}")
    wait(5)

    # While given repeats are more than how many are done, continue.
    while repeats > done:
        try:
            gui.typewrite(text)
            gui.press("enter")
            print(f"{F.GREEN}[#] {done}/{repeats}")
            done = done + 1
        except Exception:
            print(f"{F.RED}[!] Error occured. Trying again...{R}")
            done = done - 1
            errors = errors + 1

            # If errors are more than repeats given * 2, stop running.
            if errors > repeats * 2:
                print(f"{F.LIGHTRED_EX}[x] Too many tries. Script automatically stopped.")
                done = repeats # stops the while loop

    print(f"{F.CYAN}[i] Task completed.")
