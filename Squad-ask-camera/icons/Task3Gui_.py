from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QWidget ,QPushButton,QDialog
from PyQt5 import uic,QtCore
from PyQt5.QtCore import QTimer ,QDateTime
from PyQt5.QtGui import QPixmap,QKeyEvent,QImage
from PyQt5.Qt import Qt
import sys
import cv2
sec =0
min=0
hour=0

timerOn= False
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        #load the ui file
        uic.loadUi("Squad ask camera\icons\Task3Gui.ui",self)
        #define our widgets
        self.setWindowTitle("Squad Ask ROV")
        self.downLabel = self.findChild( QLabel ,"downLabel")
        self.upLabel = self.findChild( QLabel ,"upLabel")
        self.rotateCWred = self.findChild( QLabel ,"rotateCWred")
        self.rotateCCWred = self.findChild( QLabel ,"rotateCCWred")
        self.leftLabel = self.findChild( QLabel ,"leftLabel")
        self.rightLabel= self.findChild( QLabel ,"rightLabel")
        self.frontLabel= self.findChild( QLabel ,"frontLabel")
        self.backLabel= self.findChild( QLabel ,"backLabel")
        self.vgribberlabel = self.findChild(QLabel,"closedVgribber")
        self.hgribberlabel = self.findChild(QLabel,"closedHgribber")

        self.timerstartbutton = self.findChild(QPushButton,"startButton")
        self.timerstartbutton.clicked.connect(self.start_timer)
        self.timerendbutton = self.findChild(QPushButton,"endButton")
        self.timerendbutton.clicked.connect(self.stop_timer)
        self.timerresetbutton = self.findChild(QPushButton,"resetButton")
        self.timerresetbutton.clicked.connect(self.reset_timer)
        self.timerLabel=self.findChild(QLabel,"timerLabel")
        self.timerLabel.setText("0:0:0")

        self.autunomusButton=self.findChild(QPushButton,"autunomusButton")
        self.depthholdButton=self.findChild(QPushButton,"depthholdButton")
        self.stabilizeButton=self.findChild(QPushButton,"stabilizeButton")
        self.manualButton=self.findChild(QPushButton,"manualButton")
        self.curentmodeLabel= self.findChild( QLabel ,"curentmodeLabel")
        self.autunomusButton.clicked.connect(self.currentMoodAuto)
        self.depthholdButton.clicked.connect(self.currentMoodDepth)
        self.stabilizeButton.clicked.connect(self.currentMoodStable)
        self.manualButton.clicked.connect(self.currentMoodManual)

        self.imgLabel=self.findChild(QLabel,"camera1Label")
        self.imgLabel2=self.findChild(QLabel,"camera2Label")
        self.image = None

        #timer initialization
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        #********************************
        self.setFocus()
        #show the app
        self.show()

    def startWebcam(self) :
        self.capture = cv2.VideoCapture('http://192.168.0.6:4747/video')
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(5)
    def updateFrame(self) :
        ret,self.image = self.capture.read()
        self.image = cv2.flip(self.image,1)
        self.displayImage(self.image,1)
    def displayImage(self,img,window = 1) :
        self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        outImage = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        if window == 1 :
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)
            self.imgLabel2.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel2.setScaledContents(True)       
    def currentMoodAuto(self):
        self.curentmodeLabel.setText("Current Mode: Autonmous")

    def currentMoodDepth(self):
        self.curentmodeLabel.setText("Current Mode: Depth Hold")

    def currentMoodStable(self):
        self.curentmodeLabel.setText("Current Mode: Stabilize")

    def currentMoodManual(self):
        self.curentmodeLabel.setText("Current Mode: Manual")

    #timer functions*****************   
    def showTime(self) :
    
        global sec , min ,hour
        if timerOn :      
            sec+=1
            if sec ==60 :
                min+=1
                sec=0
            if min == 60:
                hour+=1
                min=0    
            text = str(hour)+":"+str(min)+":"+str(sec)
            self.timerLabel.setText(text)
    def start_timer(self):
        global timerOn
        timerOn=True 

    def reset_timer(self) :
        global TimerOn,sec,min,hour 
        TimerOn=False
        sec=0
        min=0
        hour=0
        self.timerLabel.setText("0:0:0")
    def stop_timer(self):
        global timerOn
        timerOn=False

    #take key press    
    def keyPressEvent(self, event):
        self.setFocus()
        if event.key()== Qt.Key_Right:
            pixmap = QPixmap('right-arrow.png')
            self.rightLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Left:
            pixmap = QPixmap('left-arrow.png')
            self.leftLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Up:
            pixmap = QPixmap('frwrd-arrow.png')
            self.frontLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Down:
            pixmap = QPixmap('bckwrd-arrow.png')
            self.backLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_9:
            pixmap = QPixmap('cw.png')
            self.rotateCWred.setPixmap(pixmap)
        elif event.key()== Qt.Key_0:
            pixmap = QPixmap('ccw.png')
            self.rotateCCWred .setPixmap(pixmap)
        elif event.key()== Qt.Key_U:
            pixmap = QPixmap('upward-arrow.png')
            self.upLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_D:
            pixmap = QPixmap('downward-arrow.png')
            self.downLabel.setPixmap(pixmap)
        elif event.key() == Qt.Key_V :
            pixmap = QPixmap('grapper-open.png')
            self.vgribberlabel.setPixmap(pixmap)
        elif event.key() == Qt.Key_H :
            pixmap = QPixmap('grapper-open-horizontal.png')
            self.hgribberlabel.setPixmap(pixmap)    


    #take key release
    def keyReleaseEvent(self, event) :
        self.setFocus()
        if event.key() == Qt.Key_Up :
            pixmap=QPixmap('frwrd-arrowred.png')
            self.frontLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Left:
            pixmap = QPixmap('left-arrowred.png')
            self.leftLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Right :
            pixmap = QPixmap('right-arrowred.png')
            self.rightLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_Down:
            pixmap = QPixmap('bckwrd-arrowred.png')
            self.backLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_9:
            pixmap = QPixmap('cwred.png')
            self.rotateCWred.setPixmap(pixmap)
        elif event.key()== Qt.Key_0:
            pixmap = QPixmap('ccwred.png')
            self.rotateCCWred .setPixmap(pixmap)
        elif event.key()== Qt.Key_U:
            pixmap = QPixmap('upward-arrowred.png')
            self.upLabel.setPixmap(pixmap)
        elif event.key()== Qt.Key_D:
            pixmap = QPixmap('downward-arrowred.png')
            self.downLabel.setPixmap(pixmap)   
        elif event.key() == Qt.Key_V :
            pixmap = QPixmap('grapper-close.png')
            self.vgribberlabel.setPixmap(pixmap)
        elif event.key() == Qt.Key_H :
            pixmap = QPixmap('grapper-close-horizontalpng.png')
            self.hgribberlabel.setPixmap(pixmap)         
        
                
app =QApplication(sys.argv)
UIWindow = UI()
UIWindow.startWebcam()
UIWindow.show()
sys.exit(app.exec_())