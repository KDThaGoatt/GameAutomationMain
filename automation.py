import pyautogui as p
import time
import keyboard

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
            p.click(x=350, y=750) #search to see if upgrade points are zero and click play if they are
            points = False
            mainscreen()
        except:
            points = True


        if hp + atk + df == 0 or hp + atk + df == 3:
            p.click(x=205, y=585) #upgrading HP
            hp = 1 - hp
        elif (hp == 1 and atk == 0) or (hp == 0 and atk == 1):
            p.click(x=350, y=585) #upgrading attack
            atk = 1 - atk
        else:
            p.click(x=490, y=585) #upgrading defense
            df = 1 - df

def mainscreen():
    global mainscrPoints
    mainscrActive = True
    while True:
        time.sleep(0.2)
        print("test")
        try:
            location = p.locateOnScreen('playingpixel.png')
            print("test2")
            print(location)
            mainscrActive = False
            # Checks to see if color of background when playing is on the screen
        except:
            mainscrActive = True
            print('locoation not found')
            #If play background cant be located then it is on the main screen
        while mainscrActive:
            try:
                p.locateOnScreen('0points.png') #Check if the points are zero
                mainscrPoints = False
                print('points 0')
            except:
                mainscrPoints = True
                

        if mainscrPoints:
            p.click(x=345, y=600) #Click upgrade button
            upgrades()
        else:
            p.click(x=345, y=475) #Click try again button
            break
        
def main():
    while True:
        mainscreen()

time.sleep(3)
p.moveTo(10,10,2)#Giving you time to set up your screen
main()