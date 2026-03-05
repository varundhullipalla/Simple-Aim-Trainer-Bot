import time
import pyautogui
while True:
    try:
        res = pyautogui.locateCenterOnScreen("Target.png", confidence=0.7)
        if res:
            print("Found at:", res)
            pyautogui.click(res)
        else:
            print("Not found")

    except pyautogui.ImageNotFoundException:
        print("Image not found this frame")


