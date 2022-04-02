##########################################
## src: github.com/neek8044/TextSpammer ##
##########################################

# Imports
from colorama import Fore, Style
import time
from os import system

system('cls')
# Configuring colorama
F = Fore
SR = Style.RESET_ALL

# Trying to import pyauto gui library. If an ImportError
# occured, it will install the library via pip.
try:
    import pyautogui
except ImportError:  # Installs library if an error occures.
    print(f"{F.LIGHTRED_EX}[!] Error while importing pyautogui library.")
    print(f"{F.GREEN}[+] Installing library via pip...{SR}")
    system('pip install pyautogui')

    try:
        import pyautogui # Tries again after installation
    except ImportError:
        print(f"{F.LIGHTRED_EX}[!] Error while importing pyautogui library.")
        print(f"{F.RED}[+] Updating library via pip...{SR}")
        system('pip install --upgrade pyautogui')

# Initialization
version = '22.04.02'
gui = pyautogui
done = 0
errors = 0

# Wait function using the time library
def wait(s):
    time.sleep(s)

##################################################

print(f"{F.LIGHTMAGENTA_EX}Text Spammer - Version " + version)

while True:
    print("")

    # Asks what phrase to spam and for how many times
    text = input(f"{F.YELLOW}[?] Phrase to spam: {SR}")
    cycles = input(f"{F.YELLOW}[?] How many times: {SR}")
    cycles = int(cycles)

    # Delay before running so the user can click on a textbox
    print(f"{F.CYAN}[i] You are given 10 seconds to click on a text field.{SR}")
    wait(5)
    print(f"{F.CYAN}[i] 5 seconds left...{SR}")
    wait(5)

    # While given cycles are more than how many are done, continue.
    while cycles > done:
        try:
            gui.typewrite(text)
            gui.press("enter")
            print(f"{F.GREEN}[*] Success!")
            done = done + 1
        except Exception:
            print(f"{F.RED}[!] Error occured. Trying again...{SR}")
            done = done - 1
            errors = errors + 1

            # If errors are more than cycles given * 2, stop running.
            if errors > cycles * 2:
                done = cycles # Sets done = cycles in order to stop the while loop
                print(f"{F.LIGHTRED_EX}[x] Critical error: too many tries. Script automatically stopped.")

    print(f"{F.CYAN}[i] Task completed.")
