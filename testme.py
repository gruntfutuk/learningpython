import sys

from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'admin' and
            self.textPass.text() == 'admin'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Try Again')

class Sign_Up(QWidget):
    def __init__(self, parent=None):
        super(Sign_Up, self).__init__(parent)

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(['DriverID', 'Full Name', 'Age', 'Phone','Time in', 'Time out'])
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        self.lblDriverID = QLabel("DriverID:")
        self.txtDriverID = QLineEdit()
        self.txtDriverID.setPlaceholderText("DriverID")

        self.lblFullName = QLabel("Full Name:")
        self.txtFullName = QLineEdit()
        self.txtFullName.setPlaceholderText("Full Name")

        self.lbAge = QLabel("Age:")
        self.txtAge = QLineEdit()
        self.txtAge.setPlaceholderText("Age")

        self.lblPhone = QLabel("Phone:")
        self.txtPhone = QLineEdit()
        self.txtPhone.setPlaceholderText("Phone")

        self.lblTimein = QLabel("Time in:")
        self.txtTimein = QLineEdit()
        self.txtTimein.setPlaceholderText("Time in")

        self.lblTimeout = QLabel("Time out:")
        self.txtTimeout = QLineEdit()
        self.txtTimeout.setPlaceholderText("Time out")

        grid = QGridLayout()
        grid.addWidget(self.lblDriverID, 0, 0)
        grid.addWidget(self.txtDriverID, 0, 1)
        grid.addWidget(self.lblFullName, 1, 0)
        grid.addWidget(self.txtFullName, 1, 1)
        grid.addWidget(self.lbAge, 2, 0)
        grid.addWidget(self.txtAge, 2, 1)
        grid.addWidget(self.lblPhone, 3,0)
        grid.addWidget(self.txtPhone, 3, 1)
        grid.addWidget(self.lblTimein, 4,0)
        grid.addWidget(self.txtTimein, 4, 1)
        grid.addWidget(self.lblTimeout, 5,0)
        grid.addWidget(self.txtTimeout, 5, 1)

        btnLoad = QPushButton('Load Data')
        btnLoad.clicked.connect(self.loadData)

        btnInsert = QPushButton('Add')
        btnInsert.clicked.connect(self.insertData)

        btnRemove = QPushButton('Delete')
        btnRemove.clicked.connect(self.removeData)

        hbx = QHBoxLayout()
        hbx.addWidget(btnLoad)
        hbx.addWidget(btnInsert)
        hbx.addWidget(btnRemove)

        vbx = QVBoxLayout()
        vbx.addLayout(grid)
        vbx.addLayout(hbx)
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(self.table)

        self.setWindowTitle("YellowDot Transport Inc.")
        self.resize(500, 500)
        self.setLayout(vbx)

    def loadData(self, event):
        index = 0
        query = QSqlQuery()
        query.exec_("select * from person")

        while query.next():
            driverID = query.value(0)
            fullname = query.value(1)
            age = query.value(2)
            phone = query.value(3)
            time_in = query.value(4)
            time_out = query.value(5)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(driverID)))
            self.table.setItem(index, 1, QTableWidgetItem(fullname))
            self.table.setItem(index, 2, QTableWidgetItem(age))
            self.table.setItem(index, 3, QTableWidgetItem(phone))
            self.table.setItem(index, 4, QTableWidgetItem(time_in))
            self.table.setItem(index, 5, QTableWidgetItem(time_out))

            index += 1

    def insertData(self, event):
        driver_ID = int(self.txtDriverID.text())
        full_name = self.txtFullName.text()
        age = self.txtAge.text()
        phone= self.txtPhone.text()
        time_in= self.txtTimeIn.text()
        time_out= self.txtTimeOut.text()

        query = QSqlQuery()
        query.exec_("insert into person values({0}, '{1}', '{2}', '{3}','{4}','{5}')".format(driver_ID, full_name, age, phone, time_in, time_out))

    def removeData(self, event):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        DriverID = self.table.selectedItems()[0]
        query = QSqlQuery()
        query.exec_("delete from person where id = " + DriverID.text())

        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex())

    def db_connect(self, filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
            "Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read the Qt SQL "
            "driver documentation for information how to build it.\n\n"
            "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True

    def db_fillupform(self):
        query = QSqlQuery()
        query.exec_("create table person(id int primary key, "
        "fullname varchar(20), age varchar(20), phone varchar(11), timein varchar(10), timeout varchar(10))")
        query.exec_("insert into person values(101, 'Cagnaan, John Albert B', '19', 09991835096,'7:30','4:00')")
        query.exec_("insert into person values(102, 'Cepe, Vince Paul', '19', 09999150854,'7:30','4:00')")
        query.exec_("insert into person values(103, 'Resquid, Macky', '19', 09999988701,'7:30','4:00')")
        query.exec_("insert into person values(104, 'Resquid, Macky', '19', 09999988702,'7:30','4:00')")
        query.exec_("insert into person values(105, 'Resquid, Macky', '19', 09999988703,'7:30','4:00')")

    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app = QApplication(sys.argv)
    ejm = Sign_Up()
    ejm.init('datafile', 'QSQLITE')
    ejm.show()
    login = Login()


