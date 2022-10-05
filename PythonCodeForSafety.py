#jupyter notbook crashes erasing all the code in it

#task 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = np.zeros((50,50,3),np.uint8)
image1[:,:] = (125,0,246)
image2 = np.zeros((50,50,3),np.uint8)
image2[:,:] = (255,23,15)
image3 = np.zeros((50,50,3),np.uint8)
image3[:,:] = (15,255,30)
image4 = np.zeros((50,50,3),np.uint8)
image4[:,:] = (35,0,12)

row1 = np.hstack((image1,image2))
row2 = np.hstack((image3,image4))
finalImage = np.vstack((row1,row2))
finalImage = cv2.cvtColor(finalImage,cv2.COLOR_BGR2RGB)

plt.imshow(finalImage)
plt.show

#task 2
import cv2
from cv2 import ROTATE_90_CLOCKWISE
from cv2 import COLOR_BGR2GRAY
from cv2 import COLOR_BGR2HSV
import numpy as np

capture = cv2.VideoCapture("http://192.168.0.5:4747/video")
frameWidth = int(capture.get(3))
frameHeight = int(capture.get(4))
frameSize = (frameWidth,frameHeight)
FPS = int(capture.get(5))

key = 'z'
lastKey = 'z'

while True :
    check, frame = capture.read()
    readkey = cv2.waitKey(20)
    if readkey != -1 :
        key = readkey
        cv2.destroyAllWindows()
    if  key == ord('q') or key == ord('Q') :
        break
    elif key == ord('r') or key == ord('R') :#rotate frame
        frame = cv2.rotate(frame,ROTATE_90_CLOCKWISE)
    elif key == ord('c') or key == ord('C') :#save frame
        cv2.imwrite("Resources/Capture.jpg",frame)   
    elif (key == ord('s') or key == ord('s')) and (lastKey != ord('s') or lastKey != ord('S')) :#start save video
        outputVideo = cv2.VideoWriter('Resources/CaptureVideo.avi', cv2.VideoWriter_fourcc('M','J','P','G'), FPS, frameSize)
    elif (key == ord('s') or key == ord('S')) and (lastKey == ord('s') or lastKey == ord('S') ) :#save video
        outputVideo.write(frame)
    elif (key != ord('s') or key != ord('S')) and (lastKey == ord('s') or lastKey == ord('S')) :#end save video
        outputVideo.release()
    elif key == ord('g') or key == ord('G') :#convert grayscale
        frame = cv2.cvtColor(frame,COLOR_BGR2GRAY)
    elif key == ord('h') or key == ord('H')  :#convertHSV
        frame = cv2.cvtColor(frame,COLOR_BGR2HSV)
    elif key == ord('x') or key == ord('X') :#show all
        rotatedFrame = cv2.rotate(frame,ROTATE_90_CLOCKWISE)
        cv2.imshow("Video2",rotatedFrame)
        imageGray = cv2.cvtColor(frame,COLOR_BGR2GRAY)
        cv2.imshow("Video3",imageGray)
        imageHSV = cv2.cvtColor(frame,COLOR_BGR2HSV)
        cv2.imshow("Video4",imageHSV)
    #show original only z case is implicit
    cv2.imshow("Video",frame)
    lastKey = key
    
capture.release()
cv2.destroyAllWindows()
