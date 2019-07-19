from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from PIL import ImageOps,ImageGrab
import pyautogui,time
import cv2
from  numpy import *
class Cordinates():
    replayBtn =(340,390)
    dinasaur = (171,395)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0)
    pyautogui.keyUp('space')

def imageGrab():
    global check
    global x
    global y
    global z
    global count
    box = (Cordinates.dinasaur[0]+x,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+y,Cordinates.dinasaur[1]+z)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    if(count>40):
        x=x+5
        y=y+5
        count=0
    return a

def main():
    global count
    restartGame()
    while True:
        a=imageGrab()
        if(a.sum()!=1247 ) :
            print(a)
            count = count+1
            pressSpace()
check=0
x=50
y=90
z=25
count = 0
main()