from PyQt5.QtCore import * 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import * 

import sys 
  
  
class Window(QMainWindow): 
  
  
    def __init__(self): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("Python") 
  
        #self.setWindowOpacity(0.1) #Adds transparency
  
  
        # setting  the geometry of window 
        self.setGeometry(60, 60, 600, 400) 
  
        # creating a label widget 
        self.label_1 = QLabel(self) 

        self.pixmap = QPixmap("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas.png")
        self.label_1.setPixmap(self.pixmap)

        # moving position 
        
  
        self.label_1.adjustSize() 
  
        # show all the widgets 
        self.show() 
  
        def paintEvent(self, event=None):
            painter = QPainter(self)

            painter.setOpacity(0.7)
            painter.setBrush(Qt.white)
            painter.setPen(QPen(Qt.white))   
            painter.drawRect(self.rect())


# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 