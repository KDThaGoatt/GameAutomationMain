import pyautogui as p
import time

while True:
    try:
        time.sleep(0.5)
        p.locateOnScreen('upgradeend.png')
        print("found")
    except Exception as e:
        print(e)
