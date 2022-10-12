###########################################################
# Project : task 6
# Authors :  squad_Ask
###########################################################

#imports
import cv2
import numpy as np

#variables
XvaluesBlue = []
YvaluesBlue = []
XvaluesGreen = []
YvaluesGreen = []
isBlue = False
isGreen = False

#callback fn (Sama & Mazen)
def mouseClick(event,x,y,flags,parameters) :
    global XvaluesBlue
    global YvaluesBlue
    global XvaluesGreen
    global YvaluesGreen
    global finalImage
    global outputImage
    global isBlue
    global isGreen
    counterBlue = 0 
    counterGreen = 0

    if event == cv2.EVENT_LBUTTONDOWN :
        isBlue = True
        XvaluesBlue.append(x)
        YvaluesBlue.append(y)
    if event ==cv2.EVENT_LBUTTONUP :
        isBlue = False
        outputImage = finalImage.copy()
        XvaluesBlue.append(x)
        YvaluesBlue.append(y)
        while(counterBlue < len(XvaluesBlue)) :
            cv2.rectangle(outputImage,(XvaluesBlue[counterBlue],YvaluesBlue[counterBlue]),(XvaluesBlue[counterBlue+1],YvaluesBlue[counterBlue+1]),(255,0,0),2)
            counterBlue += 2
        while(counterGreen < len(XvaluesGreen)) :
            cv2.rectangle(outputImage,(XvaluesGreen[counterGreen],YvaluesGreen[counterGreen]),(XvaluesGreen[counterGreen+1],YvaluesGreen[counterGreen+1]),(0,255,0),2)
            counterGreen += 2
    if event == cv2.EVENT_RBUTTONDOWN :
        isGreen = True
        XvaluesGreen.append(x)
        YvaluesGreen.append(y)
    if event ==cv2.EVENT_RBUTTONUP :
        isGreen = False
        outputImage = finalImage.copy()
        XvaluesGreen.append(x)
        YvaluesGreen.append(y)
        while(counterBlue < len(XvaluesBlue)) :
            cv2.rectangle(outputImage,(XvaluesBlue[counterBlue],YvaluesBlue[counterBlue]),(XvaluesBlue[counterBlue+1],YvaluesBlue[counterBlue+1]),(255,0,0),2)
            counterBlue += 2
        while(counterGreen < len(XvaluesGreen)) :
            cv2.rectangle(outputImage,(XvaluesGreen[counterGreen],YvaluesGreen[counterGreen]),(XvaluesGreen[counterGreen+1],YvaluesGreen[counterGreen+1]),(0,255,0),2)
            counterGreen += 2
    if  event == cv2.EVENT_MOUSEMOVE :
        if isBlue :
            outputImage = finalImage.copy()
            cv2.rectangle(outputImage,(XvaluesBlue[-1],YvaluesBlue[-1]),(x,y),(255,0,0),2)
            while(counterBlue < len(XvaluesBlue)-1) :
                cv2.rectangle(outputImage,(XvaluesBlue[counterBlue],YvaluesBlue[counterBlue]),(XvaluesBlue[counterBlue+1],YvaluesBlue[counterBlue+1]),(255,0,0),2)
                counterBlue += 2
            while(counterGreen < len(XvaluesGreen)-1) :
                cv2.rectangle(outputImage,(XvaluesGreen[counterGreen],YvaluesGreen[counterGreen]),(XvaluesGreen[counterGreen+1],YvaluesGreen[counterGreen+1]),(0,255,0),2)
                counterGreen += 2  
        if isGreen :
            outputImage = finalImage.copy()
            cv2.rectangle(outputImage,(XvaluesGreen[-1],YvaluesGreen[-1]),(x,y),(0,255,0),2)
            while(counterBlue < len(XvaluesBlue)-1) :
                cv2.rectangle(outputImage,(XvaluesBlue[counterBlue],YvaluesBlue[counterBlue]),(XvaluesBlue[counterBlue+1],YvaluesBlue[counterBlue+1]),(255,0,0),2)
                counterBlue += 2
            while(counterGreen < len(XvaluesGreen)-1) :
                cv2.rectangle(outputImage,(XvaluesGreen[counterGreen],YvaluesGreen[counterGreen]),(XvaluesGreen[counterGreen+1],YvaluesGreen[counterGreen+1]),(0,255,0),2)
                counterGreen += 2       

#main image formation (mohamed)
finalImage=np.zeros((600, 1000 , 3), dtype="uint8")
Real=cv2.imread("Resources/coral3.jpg")
Real=cv2.resize(Real,(400,260))
Changed=cv2.imread("Resources/coral4.jpg")
Changed=cv2.resize(Changed,(500,500))
#add images on the outputImageput image
finalImage[20:280,550:950]= Real
finalImage[20:520,10:510] = Changed
#write on the image
cv2.putText(finalImage,"Simple Left click and drag : add a Blue rectangle",(550,350),cv2.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
cv2.putText(finalImage,"Simple Right click and drag : add a Green rectangle",(550,400),cv2.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
cv2.putText(finalImage,"Press 'd' to clear the screen",(550,450),cv2.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
cv2.putText(finalImage,"Press 'q' to quit",(550,500),cv2.FONT_HERSHEY_SIMPLEX,0.45,(255,255,255),1)
outputImage = finalImage.copy()

cv2.imshow('Task 6',outputImage)
cv2.setMouseCallback('Task 6',mouseClick)

#main loop (Sama & Mazen)
while True:
    cv2.imshow('Task 6',outputImage)
    key = cv2.waitKey(20)
    if key == ord('q') :
        cv2.destroyAllWindows()
        break
    if key == ord('d') :
        outputImage = finalImage.copy()
        XvaluesBlue.clear()
        YvaluesBlue.clear()
        XvaluesGreen.clear()
        YvaluesGreen.clear()