from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class AddAppointment(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Appointment")

        self.calendar = QCalendarWidget()
        self.time_select = QComboBox()
        

        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.calendar,0,0)
        self.main_layout.addWidget(self.time_select,0,1)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        

      
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddAppointment()
    window.show()
    window.raise_()
    application.exec_()
