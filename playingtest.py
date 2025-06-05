import pyautogui as p
import time

time.sleep(2)
location = p.locateOnScreen('healthbar.png')
print(location)