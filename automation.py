import pyautogui as p
import time

hp = 0
atk = 0
df = 0
mainscrPoints = True

def upgrades():
    p.click(x=715, y=560)
    points = True
    while points == True:
        try:
            p.locateOnScreen("upgradeend.png")
            p.click(x=710, y=740) #search to see if upgrade points are zero and click play if they are
            points = False
        except:
            points = True
        if hp + atk + df == 0 or hp + atk + df == 3:
            p.click(x=545, y=545) #upgrading HP
            if hp == 0:
                hp = 1
            else:
                hp = 0
        elif hp == 1 and atk == 0 or hp == 0 and atk == 1:
            p.click(x=710, y=545) #upgrading attack
            if atk == 0:
                atk = 1
            else:
                atk = 0
        else:
            p.click(x=885, y=545) #upgrading defense
            if df ==0:
                df = 1
            else:
                df = 0

def mainscreen():
    try:
        p.locateOnScreen("0points.png")
        mainscrPoints = True
    except:
        mainscrPoints = False

    if mainscrPoints == True:
        