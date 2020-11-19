from PyQt5.QtWidgets import QMainWindow, QApplication, QSizeGrip, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5"
        self.top = 100
        self.left = 100
        self.width = 1920
        self.height = 1080

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vbox = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)

        self.setLayout(vbox)
        

        self.show()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())