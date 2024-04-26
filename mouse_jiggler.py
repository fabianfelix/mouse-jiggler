import pyautogui, time

def jiggler():
    counter = 0
    while True:
        posX, posY = pyautogui.position()
        newX = posX + 5
        newY = posY + 5

        pyautogui.moveTo(newX, newY)
        pyautogui.moveTo(posX, posY)
        counter += 1

        if counter == 5:
            time.sleep(5)
            counter = 0

jiggler()
