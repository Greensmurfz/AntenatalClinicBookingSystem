from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class ViewDetails(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setMinimumHeight(600)
        self.setMinimumWidth(1035)
        self.setWindowTitle("View/Edit Patient Details")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Booking System.db")
        self.db.open()

        self.table_view = QTableView()
        self.submit_changes_button = QPushButton("Submit Changes")

        self.layout = QGridLayout()
        self.layout.addWidget(self.table_view,0,0,1,3)
        self.layout.addWidget(self.submit_changes_button,1,1)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        
        self.setCentralWidget(self.widget)

        self.create_table_model()

        self.submit_changes_button.clicked.connect(self.update_details)    

    def create_table_model(self):
        self.model = QSqlTableModel()
        self.model.setTable("Patient_Details")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.table_view.setModel(self.model)
        self.table_view.model().select()

    def update_details(self):
        self.model.submitAll()

    def create_query_model(self):
        query = QSqlQuery()
        query.prepare("SELECT * FROM Patient Details WHERE NHSNumber == ?")
        query.addBindValue(4)
        query.exec_()

        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.table_view.setModel(self.model)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = ViewDetails()
    window.show()
    window.raise_()
    application.exec_()



