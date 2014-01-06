from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import*

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Patient Details.db")
        self.db.open()
        
        self.table_view = QTableView()
        self.submit_changes_button = QPushButton("Submit")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_view)
        self.layout.addWidget(self.submit_changes_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        
        self.setCentralWidget(self.widget)
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
