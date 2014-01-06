from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import*
import sqlite3

import sys

class AddPatient(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Patient Details")
        
        #Labels
        self.first_name = QLabel("First Name")
        self.last_name = QLabel("Last Name")
        self.house_no = QLabel("House Number")
        self.street = QLabel("Street")
        self.post_code = QLabel("Post Code")
        self.telephone = QLabel("Telephone")
        self.nhs = QLabel("NHS Number")
        self.dob = QLabel("Date of Birth")
        self.weeks_pregnant = QLabel("Weeks Pregnant")
        self.hospital_number = QLabel("Hospital Number")
    
        #Buttons
        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear All")
        #Lines
        self.first_name_line = QLineEdit()
        self.last_name_line = QLineEdit()
        self.street_line = QLineEdit()
        self.house_no_line = QLineEdit()
        self.post_code_line = QLineEdit()
        self.telephone_line = QLineEdit()
        self.nhs_line = QLineEdit()
        self.nhs_line.setPlaceholderText("000-000-0000")
        self.dob_line = QLineEdit()
        self.dob_line.setPlaceholderText("YYYY/MM/DD")
        self.weeks_pregnant_line = QLineEdit()
        self.hospital_number_line = QLineEdit()

        #Layout
        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.first_name,0,0) 
        self.main_layout.addWidget(self.first_name_line,0,1)
        self.main_layout.addWidget(self.last_name,1,0)
        self.main_layout.addWidget(self.last_name_line,1,1)
        self.main_layout.addWidget(self.nhs,2,0)
        self.main_layout.addWidget(self.nhs_line,2,1)
        self.main_layout.addWidget(self.dob,3,0)
        self.main_layout.addWidget(self.dob_line,3,1)
        self.main_layout.addWidget(self.weeks_pregnant,4,0)
        self.main_layout.addWidget(self.weeks_pregnant_line,4,1)
        self.main_layout.addWidget(self.hospital_number,5,0)
        self.main_layout.addWidget(self.hospital_number_line,5,1)
        self.main_layout.addWidget(self.telephone,6,0)
        self.main_layout.addWidget(self.telephone_line,6,1)
        self.main_layout.addWidget(self.house_no,0,2)
        self.main_layout.addWidget(self.house_no_line,0,3)
        self.main_layout.addWidget(self.street,1,2)
        self.main_layout.addWidget(self.street_line,1,3)
        self.main_layout.addWidget(self.post_code,2,2)
        self.main_layout.addWidget(self.post_code_line,2,3)
        self.main_layout.addWidget(self.clear_button)
        self.main_layout.addWidget(self.submit_button)

        
        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

        self.clear_button.clicked.connect(self.clear_clicked)
        self.submit_button.clicked.connect(self.submit_data)
      

    def clear_clicked(self):
        self.first_name_line.clear()
        self.last_name_line.clear()
        self.street_line.clear()
        self.house_no_line.clear()
        self.post_code_line.clear()
        self.nhs_line.clear()
        self.telephone_line.clear()
        self.dob_line.clear()
        self.weeks_pregnant_line.clear()
        self.hospital_number_line.clear()

    def submit_data(self):
        values = (self.nhs_line.text(),
                  self.first_name_line.text(),
                  self.last_name_line.text(),
                  self.house_no_line.text(),
                  self.street_line.text(),
                  self.post_code_line.text(),
                  self.telephone_line.text(),
                  self.dob_line.text(),
                  self.weeks_pregnant_line.text(),
                  self.hospital_number_line.text(),)
        with sqlite3.connect("Booking System.db") as db:
            cursor = db.cursor()
            sql = """insert into Patient_Details
                     (NHSNumber,
                     FirstName,
                     LastName,
                     HouseNumber,
                     Street,
                     Postcode,
                     PhoneNumber,
                     DateOfBirth,
                     WeeksPregnant,
                     HospitalNumber)
                     values(?,?,?,?,?,?,?,?,?,?)"""
            cursor.execute(sql,values)
            db.commit()
        self.first_name_line.clear()
        self.last_name_line.clear()
        self.street_line.clear()
        self.house_no_line.clear()
        self.post_code_line.clear()
        self.nhs_line.clear()
        self.telephone_line.clear()
        self.dob_line.clear()
        self.weeks_pregnant_line.clear()
        self.hospital_number_line.clear()
            
           
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = AddPatient()
    window.show()
    window.raise_()
    application.exec_()
