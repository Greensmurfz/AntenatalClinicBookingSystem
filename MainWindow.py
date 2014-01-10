from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from AddPatient import *
from ViewPatientDetails import *


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(600)
        self.setMinimumWidth(1035)
        self.setWindowTitle("Antenatal Clinic Booking System")

        #Lables
        self.title_label = QLabel("""<center><font size="6">Booking System</font>""")
        self.blank = QLabel("")

        #Buttons
        self.add_button = QPushButton("Add Appointment")
        self.patient_button = QPushButton("View/Edit Patient Details")
        self.appointment_button = QPushButton("View/Edit Appointments")
        
        #Layout
        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.blank,4,0)
        self.main_layout.addWidget(self.blank,4,1)
        self.main_layout.addWidget(self.title_label,4,1)
        self.main_layout.addWidget(self.blank,0,2)
        self.main_layout.addWidget(self.blank,1,2)
        self.main_layout.addWidget(self.blank,2,2)
        self.main_layout.addWidget(self.add_button,3,2)
        self.main_layout.addWidget(self.patient_button,4,2)
        self.main_layout.addWidget(self.appointment_button,5,2)
        self.main_layout.addWidget(self.blank,6,2)
        self.main_layout.addWidget(self.blank,7,2)
        self.main_layout.addWidget(self.blank,8,2)
        self.main_layout.addWidget(self.blank,4,3)


        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.add_button.clicked.connect(self.add_patient)
        self.patient_button.clicked.connect(self.edit_patient_details)

        

        

    def add_patient(self):
        self.add_patient = AddPatient()
        self.setCentralWidget(self.add_patient)

    def edit_patient_details(self):
        self.edit_patient_details = ViewDetails()
        self.setCentralWidget(self.edit_patient_details)
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
