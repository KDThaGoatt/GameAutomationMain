import pyautogui as p
import time

hp = 0
atk = 0
df = 0

def upgrades():
    global hp, atk, df
    points = True
    print('running upgrades')
    while points == True:
        try:
            p.locateOnScreen("upgradeend.png")
            print("looking if points zero")
            points = False
            print("points are zero")
            playbutton = p.locateOnScreen('playbutton.png', confidence=0.95) #search to see if upgrade points are zero and click play if they are
            playbuttonpoint = p.center(playbutton)
            p.click(playbuttonpoint)
            print("clicking play")
            mainscreen()
        except Exception as e:
            points = True
            print(e)


        if hp + atk + df == 0 or hp + atk + df == 3:
            p.click(x=205, y=585) #upgrading HP
            hp = 1 - hp
            print("hp upgraded")
        elif (hp == 1 and atk == 0) or (hp == 0 and atk == 1):
            p.click(x=350, y=585) #upgrading attack
            atk = 1 - atk
            print("atk upgraded")
        else:
            p.click(x=490, y=585) #upgrading defense
            df = 1 - df
            print("df upgraded")

def mainscreen():
    mainscrPoints = False
    mainscrActive = False

    while True:
        time.sleep(0.2)
        try:
            location = p.locateOnScreen('healthbar.png')
            print(f"game playing, healthbar located at {location}")
            mainscrActive = False
            # Checks to see if color of background when playing is on the screen
        except:
            mainscrActive = True
            print('location not found')
            #If play background cant be located then it is on the main screen
        while mainscrActive == True:
            time.sleep(0.1)
            try:
                print('looking for 0 points')
                p.locateOnScreen('0points.png') #Check if the points are zero
                mainscrPoints = False
                print('points 0')
            except Exception as e:
                mainscrPoints = True
                print(str(e))
                
            if mainscrPoints == True:
                time.sleep(0.5)
                try:
                    upgradelocation = p.locateOnScreen('upgradebutton.png', confidence=0.9)
                    upgradecenter = p.center(upgradelocation)
                    p.click(upgradecenter)
                    print("upgrade clicked")
                    upgrades()
                    break
                except:
                    print("couldnt find upgrade button")
            else:
                time.sleep(0.5)
                tryagainlocation = p.locateOnScreen('tryagainbutton.png', confidence=0.9)
                tryagaincenter = p.center(tryagainlocation)
                p.click(tryagaincenter)
                print("try again clicked")
                break
        
def main():
    while True:
        mainscreen()

time.sleep(3)
p.moveTo(10,10,2)#Giving you time to set up your screen
main()