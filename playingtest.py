import pyautogui as p
import time

time.sleep(5)
location = p.locateOnScreen('playingpixel.png')
print(location)