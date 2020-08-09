import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for day nd night
    
    for i in range(350, 430):
        for j in range(300, 400):
            if data[i, j] < 100:
                for i in range(325, 405):
                    for j in range(400, 470):
                        if data[i, j] > 100:
                            hit("up")
                            return
            else:
                for i in range(325, 405):
                    for j in range(400, 470):
                        if data[i, j] < 100:
                            hit("up")
                            return
            return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(340, 420):
            for j in range(400, 470):
                data[i, j] = 0
        
        # Draw the rectangle for checking its a day or night
        for i in range(240, 270):
            for j in range(550, 560):
                data[i, j] = 171

        image.show()
        break
        '''
