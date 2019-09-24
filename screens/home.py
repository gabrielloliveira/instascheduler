# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 741, 421))
        self.tableWidget.setStyleSheet("background-color: white;\n"
"border: 1px solid #f7f7f7;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(650, 50, 110, 32))
        self.logout_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_button.setStyleSheet("background-color: #ff3860;\n"
"color: white;\n"
"border-color: #ff3860;\n"
"border-radius: 14px;")
        self.logout_button.setObjectName("logout_button")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(40, 50, 110, 32))
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 14px;")
        self.home_button.setObjectName("home_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 191, 31))
        self.label_2.setStyleSheet("font-size: 24px;\n"
"color: #404244;\n"
"")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 80, 741, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 130, 110, 32))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 14px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 811, 481))
        self.columnView.setStyleSheet("background-color: #fcfcfc;")
        self.columnView.setObjectName("columnView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(51, 180, 350, 250))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("static/img/350x250.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(407, 180, 350, 250))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("static/img/350x250.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 130, 110, 32))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 14px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 430, 64, 17))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 430, 64, 17))
        self.label_5.setObjectName("label_5")
        self.columnView.raise_()
        self.tableWidget.raise_()
        self.logout_button.raise_()
        self.home_button.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()
        self.label_5.raise_()
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
        self.logout_button.setText(_translate("MainWindow", "Sair"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "InstaScheduler"))
        self.pushButton_3.setText(_translate("MainWindow", "Agendar Post"))
        self.pushButton_4.setText(_translate("MainWindow", "Adicionar Insta"))
        self.label.setText(_translate("MainWindow", "Status"))
        self.label_5.setText(_translate("MainWindow", "Status"))

# import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

