import cv2 
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import PyQt5.QtGui as QtGui
import sys
from multiprocessing import Process, connection

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("Task3Gui.ui", self)
		self.Camera1 = self.findChild(QLabel, "camera1Label")
        self.Camera2 = self.findChild(QLabel, "camera2Label")
		self.show()

	def convertPixmap(self,frame):
        height, width, channel = frame.shape()
        bytesPerLine = 3* width
        qtImage = QtGui.QImage(frame.data,width,height, bytesPerLine,QImage.Format_RGB888).rgbSwapped()
		pixMap = QtGui.QPixmap(qtImage)
		return pixMap

    def takeCameraInput(self) :
        capture = cv2.VideoCapture("http://192.168.0.5:4747/video")
        check, frame = capture.read()
        return frame

    def ApplyMapToLabel(self, pixMap) :
        self.Camera1.setPixmap(pixMap)
        self.Camera2.setPixmap(pixMap)

    def camera1Init (self):
        address = ("localhost", 1000)
        listener = Listener(address,authkey=b'secret password')
        self.connect1 = listener.accept()

    def camera2Init (self):
        address2 = ("localhost", 2000)
        listener2 = Listener(address,authkey=b'secret password')
        self.connect2 = listener2.accept()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
    CameraInputProcess = Process(UI.takeCameraInput,(UI.self))
    pixConvertProcess = Process(UI.convertPixmap,)



