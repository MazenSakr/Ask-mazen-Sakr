import sys 

import cv2 
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.uic import loadUi

class Application (QMainWindow) :
    def __init__(self) :
        super(Application,self).__init__()
        loadUi('Squad ask camera\icons\Task3Gui.ui',self)
        self.imgLabel1=self.findChild(QLabel,"camera1Label")
        self.imgLabel2=self.findChild(QLabel,"camera2Label")
        self.image = None
        self.startWebcam()
        

    def startWebcam(self) :
        self.capture = cv2.VideoCapture("http://192.168.0.6:4747/video")
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,640)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(5)
    
    def updateFrame(self) :
        ret,self.image = self.capture.read()
        self.image = cv2.flip(self.image,1)
        self.displayImage(1)

    def displayImage(self,window = 1) :
        self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        if window == 1 : 
            self.imgLabel1.setPixmap(QPixmap.fromImage(qImg))
            self.imgLabel1.setScaledContents(True)
            self.imgLabel2.setPixmap(QPixmap.fromImage(qImg))
            self.imgLabel2.setScaledContents(True)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())