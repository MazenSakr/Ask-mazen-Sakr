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
Image1 = cv2.imread("Resources/coral3.jpg")
Image2 = cv2.imread("Resources/coral4.jpg")
rectangleColor = (0,0,0)

#callback fn
def mouseClick(event,x,y,flags,parameters) :
    global Xvalues
    global Yvalues
    global finalImage
    global outputImage
    if event == cv2.EVENT_LBUTTONDOWN :
        
        XvaluesBlue.append(x)
        YvaluesBlue.append(y)
    if event ==cv2.EVENT_LBUTTONUP :
        outputImage = finalImage
        cv2.rectangle(finalImage,(Xvalues[-1],Yvalues[-1]),(x,y),rectangleColor,2)
        XvaluesBlue.append(x)
        YvaluesBlue.append(y)
        rectangleColor = (0,0,0)
    if event == cv2.EVENT_RBUTTONDOWN :
        rectangleColor = (0,255,0)
        Xvalues.append(x)
        Yvalues.append(y)
    if event ==cv2.EVENT_RBUTTONUP :
        Xvalues.append(x)
        Yvalues.append(y)
        rectangleColor = (0,0,0)
    if  event == cv2.EVENT_MOUSEMOVE :
        outputImage = finalImage
        cv2.rectangle(finalImage,(Xvalues[-1],Yvalues[-1]),(x,y),rectangleColor,2)
       

#main loop







def rectangle_shape(event,x,y,flag,par):
    global draw, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ix,iy = x,y
    #elif event == cv2.EVENT_MOUSEMOVE:
        #if draw == True:
            #cv2.rectangle(image_window,(ix,iy),(x,y),(255,0,0),2)
    elif event == cv2.EVENT_LBUTTONUP:
        draw= False
        cv2.rectangle(image_window,(ix,iy),(x,y),(255,0,0),2)

    elif event == cv2.EVENT_RBUTTONDOWN:
        draw = True
        ix, iy = x, y

    elif event == cv2.EVENT_RBUTTONUP:
        draw= False
        cv2.rectangle(image_window,(ix,iy),(x,y),(0,255,0),2)


image_window= np.zeros((1024,1024,3),np.uint8)
cv2.namedWindow(winname='image window')
cv2.setMouseCallback('image window',rectangle_shape)

while True:
    cv2.imshow('image window',image_window)
    if cv2.waitKey(1) & 0xFF == 'q':
        break