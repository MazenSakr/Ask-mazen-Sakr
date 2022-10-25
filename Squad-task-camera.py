import cv2 
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("image.ui", self)

		# Define our widgets
		self.button = self.findChild(QPushButton, "pushButton")
		self.Camera1 = self.findChild(QLabel, "label")
        self.Camera2 = self.findChild(QLabel, "label")
		# Click The Dropdown Box
		self.button.clicked.connect(self.clicker)
						
		# Show The App
		self.show()

	def clicker(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\gui\\images", "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")

		# Open The Image
		if fname:
			self.pixmap = QPixmap(fname[0])
			# Add Pic to label
			self.label.setPixmap(self.pixmap)

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
