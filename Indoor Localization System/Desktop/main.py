from PyQt5 import QtWidgets, QtCore ,QtGui
from Desktop import Ui_MainWindow
import sys
import numpy as np
import pyqtgraph as pg
from firebase import firebase

 

class MovingObject(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(QtCore.Qt.blue)
    def posision(self, x,y):
        self.setPos(QtCore.QPointF(x, y))
 

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                       
        
        self.X = 0       
        self.Y = 0          
        self.firebase = firebase.FirebaseApplication('https://esp-project-d8500.firebaseio.com/', None)
        self.scene = QtWidgets.QGraphicsScene()
        pix = QtGui.QPixmap("E:\\4th year\\Electronics\\Task2\\mapV2H.jpg")
        item = QtWidgets.QGraphicsPixmapItem(pix)
        self.ui.graphicsView_3.setScene(self.scene)
        self.scene.addItem(item)
        self.moveObject = MovingObject(self.X , self.Y , 20)
        self.scene.addItem(self.moveObject)
        # self.GetNewXYValue()
        self.update_XY()
     
   
    def update_XY(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.GetNewXYValue)
        self.timer.start(1000)

    def GetNewXYValue(self):
        Value  = self.firebase.get('https://esp-project-d8500.firebaseio.com/', '')  
        self.X =   Value["Top"] 
        self.Y = - Value["Left"] +280
        self.map()
                                                                 
        
    def map(self):
        
        # self.X = self.GetNewXYValue("Left")     
        # self.Y = -self.GetNewXYValue("Top") +520
        self.moveObject.posision(self.X,self.Y)
        
        




       

   

        
   
        
    
    


    

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == "__main__":
    main()





