import pyautogui as p
import time

mainscrPoints = True
hp = 0
atk = 0
df = 0

def upgrades():
    global hp, atk, df
    points = True
    while points:
        try:
            p.locateOnScreen("upgradeend.png")
            p.click(x=710, y=740) #search to see if upgrade points are zero and click play if they are
            points = False
        except:
            points = True


        if hp + atk + df == 0 or hp + atk + df == 3:
            p.click(x=545, y=545) #upgrading HP
            hp = 1 - hp
        elif (hp == 1 and atk == 0) or (hp == 0 and atk == 1):
            p.click(x=710, y=545) #upgrading attack
            atk = 1 - atk
        else:
            p.click(x=885, y=545) #upgrading defense
            df = 1 - df

def mainscreen():
    global mainscrPoints
    mainscrActive = True
    while True:
        try:
            p.locateOnScreen("playingpixel.png", confidence=0.8)
            mainscrActive = False
            # Checks to see if color of background when playing is on the screen
        except:
            mainscrActive = True
        while mainscrActive:
            try:
                p.locateOnScreen("0points.png") #Check if the points are zero
                mainscrPoints = False
            except:
                mainscrPoints = True

        if mainscrPoints:
            p.click(x=715, y=560) #Click upgrade button
            upgrades()
        else:
            p.click(x=715, y=415) #Click try again button
            break
        
def main():
    while True:
        mainscreen()

time.sleep(5) #Giving you time to set up your screen
mainscreen()