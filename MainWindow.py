from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from AddPatient import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Antenatal Clinic Booking System")

        #Lables
        self.title_label = QLabel("Booking System")

        #Buttons
        self.add_button = QPushButton("Add Appointment")
        self.manage_button = QPushButton("Manage Appointment")
        self.view_button = QPushButton("View Appointments")
        
        #Layout
        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.add_button)
        self.main_layout.addWidget(self.manage_button)
        self.main_layout.addWidget(self.view_button)


        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
