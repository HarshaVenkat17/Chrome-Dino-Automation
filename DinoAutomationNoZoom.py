import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide1(data):
    """# Draw the rectangle for birds
    for i in range(310,350):
        for j in range(310,402):
            if data[i, j] < 100:
                hit("down")
                return 1"""
    for i in range(450, 576):#380/390
        for j in range(230,265):#402
            if data[i, j] < 100:
                hit("up")
                return 
    return

def isCollide2(data):
    """# Draw the rectangle for birds
    for i in range(310,350):
        for j in range(310,402):
            if data[i, j] < 100:
                hit("down")
                return 1"""
    for i in range(450, 600):#380/390
        for j in range(230,265):#402
            if data[i, j] > 100:
                hit("up")
                return 
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        for i in range(1150,1170):
            for j in range(500,520):#(310,402):
                if data[i, j]>100:
                    isCollide1(data)
                    break
                else:
                    isCollide2(data)
                    break
            break
                
        
        #print(asarray(image))
        """
        # Draw the rectangle for cactus
        for i in range(450, 510):
            for j in range(230, 265):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(1150,1170):
            for j in range(500,520):#(310,402):
                data[i, j] = 171

        image.show()
        break"""
      
