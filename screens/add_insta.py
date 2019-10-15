# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_insta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.session import Session
import socket
import pickle
import struct

addr = (('localhost', 7000))

class Ui_Add_insta(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(-5, -19, 811, 481))
        self.columnView.setStyleSheet("background-color: #fcfcfc;")
        self.columnView.setObjectName("columnView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(270, 50, 271, 31))
        self.label.setStyleSheet("font-size: 24px;\n"
"color: #404244;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(260, 400, 301, 32))
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_button.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 16px;")
        self.add_button.setObjectName("add_button")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(30, 20, 741, 421))
        self.columnView_2.setStyleSheet("background-color: white;\n"
"border: 1px solid #f7f7f7;")
        self.columnView_2.setObjectName("columnView_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 140, 278, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("background-color: #5c4aca;\n"
"color: white;\n"
"border-color: #5c4aca;\n"
"border-radius: 16px;\n"
"padding: 10px;\n"
"width: 200px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(101, 140, 86, 22))
        self.label_5.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_field.setGeometry(QtCore.QRect(224, 140, 421, 24))
        self.username_field.setObjectName("username_field")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 80, 741, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(40, 50, 110, 32))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 14px;")
        self.home_button.setObjectName("home_button")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(650, 50, 110, 32))
        self.logout_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_button.setStyleSheet("background-color: #ff3860;\n"
"color: white;\n"
"border-color: #ff3860;\n"
"border-radius: 14px;")
        self.logout_button.setObjectName("logout_button")
        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(223, 176, 421, 24))
        self.password_field.setText("")
        self.password_field.setObjectName("password_field")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 176, 86, 22))
        self.label_6.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.layoutWidget.raise_()
        self.columnView.raise_()
        self.columnView_2.raise_()
        self.label.raise_()
        self.add_button.raise_()
        self.label_5.raise_()
        self.username_field.raise_()
        self.line.raise_()
        self.home_button.raise_()
        self.logout_button.raise_()
        self.password_field.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Adicionar Conta"))
        self.add_button.setText(_translate("MainWindow", "Adicionar"))
        self.label_2.setText(_translate("MainWindow", "Foto:"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload"))
        self.label_5.setText(_translate("MainWindow", "Instagram:"))
        self.username_field.setText(_translate("MainWindow", "@"))
        self.home_button.setText(_translate("MainWindow", "Voltar"))
        self.logout_button.setText(_translate("MainWindow", "Sair"))
        self.label_6.setText(_translate("MainWindow", "Senha"))

    def add(self):
        session = Session('name')
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        username = self.username_field.text()   
        password = self.password_field.text()

        # try:
        client_socket.connect(addr)
        
        message = {
            'func': 'add_insta',
            'username': username,
            'password': password,
            'user': session.user,
        }
        
        while(True):
            client_socket.send(pickle.dumps(message))
            response = pickle.loads(client_socket.recv(6144))
            client_socket.close()
            print(response)
            res = 1
            if response['status'] != 'success':
                res = 0

            return res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

