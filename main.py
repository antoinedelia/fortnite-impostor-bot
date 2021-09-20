from PIL import ImageGrab
import pyautogui
from python_imagesearch.imagesearch import imagesearch
from pytesseract import pytesseract
import time

PATH_IMAGE = "./images/"
total_xp = 0


def get_xp_collected() -> int:
    image = ImageGrab.grab(bbox=(1314, 1009, 1505, 1065))
    xp = pytesseract.image_to_string(image)
    if "," in xp:
        xp = xp.replace(",", "").replace(" XP", "")
        return int(xp)
    return 0


def launch_game():
    # This needs to be changed to fit your screen size
    # Point the cursor to the Play button and run `pyautogui.position()` to get X and Y coordinates
    pyautogui.click(2361, 1022)


def hold_e():
    global total_xp
    xp = 0
    for _ in range(0, 10):
        try:
            xp = get_xp_collected()
        except Exception:
            pass
        if xp:
            break
        time.sleep(0.5)

    if not xp:
        print("Could not get the XP won for this round.")
    else:
        total_xp += xp
        print(f"XP collected this round: {xp}")
        print(f"Total XP collected this session: {total_xp}")

    pyautogui.keyDown('e')
    time.sleep(3)
    pyautogui.keyUp('e')


def hold_f():
    pyautogui.keyDown('f')
    time.sleep(3)
    pyautogui.keyUp('f')


def press_esc():
    pyautogui.press('esc')


print("Running the script")

while(True):
    if imagesearch(PATH_IMAGE + "in_lobby.png")[0] != -1:
        print("In lobby, starting the game.")
        launch_game()
    elif imagesearch(PATH_IMAGE + "agent_win.png")[0] != -1:
        print("Agents won. Exiting to the main menu.")
        hold_e()
    elif imagesearch(PATH_IMAGE + "impostor_win.png")[0] != -1:
        print("Impostors won. Exiting to the main menu.")
        hold_e()
    elif imagesearch(PATH_IMAGE + "rewards.png")[0] != -1:
        print("Collecting rewards.")
        press_esc()
    elif imagesearch(PATH_IMAGE + "voting.png")[0] != -1:
        print("Voting time. Skipping.")
        hold_f()

    time.sleep(1)
