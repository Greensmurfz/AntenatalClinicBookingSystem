from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import*

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Appointment System")
        
        self.menu_bar = QMenuBar()
        self.add_menu = self.menu_bar.addMenu("Add")
        self.add_menu.addAction("Add Patient")

        self.browse_menu = self.menu_bar.addMenu("Browse")

        
        
        self.setMenuBar(self.menu_bar)

            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

