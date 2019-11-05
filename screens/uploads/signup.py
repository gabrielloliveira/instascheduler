# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Signup(object):
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
        self.label.setGeometry(QtCore.QRect(250, 70, 291, 31))
        self.label.setStyleSheet("font-size: 24px;\n"
"color: #404244;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 140, 60, 16))
        self.label_2.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_2.setObjectName("label_2")
        self.email_field = QtWidgets.QLineEdit(self.centralwidget)
        self.email_field.setGeometry(QtCore.QRect(250, 170, 301, 21))
        self.email_field.setObjectName("email_field")
        self.password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.password_field.setGeometry(QtCore.QRect(250, 240, 301, 21))
        self.password_field.setText("")
        self.password_field.setObjectName("password_field")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 210, 60, 16))
        self.label_3.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_3.setObjectName("label_3")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(252, 330, 301, 32))
        self.signup_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_button.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 16px;")
        self.signup_button.setObjectName("signup_button")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(140, 20, 521, 421))
        self.columnView_2.setStyleSheet("background-color: white;\n"
"border: 1px solid #f7f7f7;")
        self.columnView_2.setObjectName("columnView_2")
        self.link_login = QtWidgets.QLabel(self.centralwidget)
        self.link_login.setGeometry(QtCore.QRect(310, 280, 201, 20))
        self.link_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.link_login.setStyleSheet("font-size:14px;\n"
"color: #3897F0;\n"
"text-decoration: underline;")
        self.link_login.setAlignment(QtCore.Qt.AlignCenter)
        self.link_login.setObjectName("link_login")
        self.columnView.raise_()
        self.columnView_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.email_field.raise_()
        self.password_field.raise_()
        self.label_3.raise_()
        self.signup_button.raise_()
        self.link_login.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.label.setText(_translate("MainWindow", "InstaScheduler - Cadastro"))
        self.label_2.setText(_translate("MainWindow", "E-mail:"))
        self.label_3.setText(_translate("MainWindow", "Senha:"))
        self.signup_button.setText(_translate("MainWindow", "Cadastrar"))
        self.link_login.setText(_translate("MainWindow", "Já tem uma conta? Faça login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

