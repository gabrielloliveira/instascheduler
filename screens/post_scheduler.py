# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'post_scheduler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from client.session import Session
from datetime import datetime
import socket
import pickle

addr = (('localhost', 7000))

class Ui_Post_scheduler(object):
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(101, 151, 76, 22))
        self.label_3.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_3.setObjectName("label_3")
        self.scheduler_button = QtWidgets.QPushButton(self.centralwidget)
        self.scheduler_button.setGeometry(QtCore.QRect(260, 400, 301, 32))
        self.scheduler_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scheduler_button.setStyleSheet("background-color: #3897f0;\n"
"color: white;\n"
"border-color: #3897f0;\n"
"border-radius: 16px;")
        self.scheduler_button.setObjectName("scheduler_button")
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(101, 101, 42, 22))
        self.label_4.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_4.setObjectName("label_4")
        self.button_upload = QtWidgets.QPushButton(self.centralwidget)
        self.button_upload.setGeometry(QtCore.QRect(224, 101, 421, 36))
        self.button_upload.setStyleSheet("background-color:#8334ac ;\n"
"color: white;\n"
"border-color: #8334ac;\n"
"border-radius: 16px;\n"
"padding: 10px;")
        self.button_upload.setObjectName("button_upload")
        self.subtitle_field = QtWidgets.QTextEdit(self.centralwidget)
        self.subtitle_field.setGeometry(QtCore.QRect(224, 151, 421, 140))
        self.subtitle_field.setObjectName("subtitle_field")
        self.location_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.location_checkBox.setGeometry(QtCore.QRect(222, 298, 179, 20))
        self.location_checkBox.setObjectName("location_checkBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(101, 324, 86, 22))
        self.label_5.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.instagram_field = QtWidgets.QLineEdit(self.centralwidget)
        self.instagram_field.setGeometry(QtCore.QRect(224, 324, 421, 24))
        self.instagram_field.setObjectName("instagram_field")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(101, 356, 109, 22))
        self.label_6.setStyleSheet("font-size: 18px;\n"
"color: #404244;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.date_scheduler_field = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.date_scheduler_field.setGeometry(QtCore.QRect(224, 356, 421, 24))
        self.date_scheduler_field.setObjectName("date_scheduler_field")
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
        self.layoutWidget.raise_()
        self.columnView.raise_()
        self.columnView_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.scheduler_button.raise_()
        self.label_4.raise_()
        self.button_upload.raise_()
        self.subtitle_field.raise_()
        self.location_checkBox.raise_()
        self.label_5.raise_()
        self.instagram_field.raise_()
        self.label_6.raise_()
        self.date_scheduler_field.raise_()
        self.line.raise_()
        self.home_button.raise_()
        self.logout_button.raise_()
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
        self.label.setText(_translate("MainWindow", "Agendar Publicação"))
        self.label_3.setText(_translate("MainWindow", "Legenda:"))
        self.scheduler_button.setText(_translate("MainWindow", "Agendar"))
        self.label_2.setText(_translate("MainWindow", "Foto:"))
        self.pushButton_2.setText(_translate("MainWindow", "Upload"))
        self.label_4.setText(_translate("MainWindow", "Foto:"))
        self.button_upload.setText(_translate("MainWindow", "Upload"))
        self.location_checkBox.setText(_translate("MainWindow", "Compartilhar Lozalização"))
        self.label_5.setText(_translate("MainWindow", "Instagram:"))
        self.instagram_field.setText(_translate("MainWindow", "@"))
        self.label_6.setText(_translate("MainWindow", "Data do post:"))
        self.home_button.setText(_translate("MainWindow", "Voltar"))
        self.logout_button.setText(_translate("MainWindow", "Sair"))

    def add(self, path):
        session = Session('name')
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        subtitle = self.subtitle_field.toPlainText()
        instagram = self.instagram_field.text()
        date_str = self.date_scheduler_field.text()  
        _translate = QtCore.QCoreApplication.translate
        self.instagram_field.setText(_translate("MainWindow", "@"))
        self.subtitle_field.setText(_translate("MainWindow", ""))


        try:
            date = datetime.strptime(date_str, "%d/%m/%y %H:%M") 
        except :
            date = datetime.strptime(date_str, "%d/%m/%Y %H:%M") 
        
        client_socket.connect(addr)

        with open(path, 'rb') as arq:
            binary_image = arq.read()
            arq.close()
        
        img = path.split('/')[-1]
        message = {
            'func': 'schedule_posting',
            'img': img,
            'binary_image': binary_image,
            'subtitle': subtitle,
            'location': 'location',
            'instagram': instagram,
            'date': date,
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

