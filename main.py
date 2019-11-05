from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem, QFileDialog
from screens.login import Ui_Login
from screens.signup import Ui_Signup
from screens.home import Ui_Home
from screens.add_insta import Ui_Add_insta
from screens.post_scheduler import Ui_Post_scheduler
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot
from client.session import Session

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.screen_login = Ui_Login()
        self.screen_login.setupUi(self.stack0)

        self.screen_signup = Ui_Signup()
        self.screen_signup.setupUi(self.stack1)

        self.screen_home = Ui_Home()
        self.screen_home.setupUi(self.stack2)

        self.screen_add_insta = Ui_Add_insta()
        self.screen_add_insta.setupUi(self.stack3)

        self.screen_post_scheduler = Ui_Post_scheduler()
        self.screen_post_scheduler.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.upload_path = None
        self.setupUi(self)

        self.screen_login.login_button.clicked.connect(self.login)
        self.screen_login.link_signup.clicked.connect(self.signup)

        self.screen_signup.signup_button.clicked.connect(self.add_user)
        self.screen_signup.link_login.clicked.connect(self.screensLogin)

        self.screen_home.home_button.clicked.connect(self.home)
        self.screen_home.logout_button.clicked.connect(self.logout)
        self.screen_home.pushButton_4.clicked.connect(self.add_insta)
        self.screen_home.pushButton_3.clicked.connect(self.post_scheduler)

        self.screen_add_insta.home_button.clicked.connect(self.come_back)
        self.screen_add_insta.logout_button.clicked.connect(self.logout)
        self.screen_add_insta.add_button.clicked.connect(self.add_insta_clicked)

        self.screen_post_scheduler.home_button.clicked.connect(self.come_back)
        self.screen_post_scheduler.logout_button.clicked.connect(self.logout)
        self.screen_post_scheduler.button_upload.clicked.connect(self.upload)
        self.screen_post_scheduler.scheduler_button.clicked.connect(self.scheduler)

    def login(self):
        try:
            response = self.screen_login.login()
            if response == "success":
                session = Session(self.screen_login.email_field.text())
                session.set_data(self.screen_login.email_field.text())
                self.QtStack.setCurrentIndex(2)
            else:
                QtWidgets.QMessageBox.about(None, "Login", response)
        except:
            QtWidgets.QMessageBox.about(None, "Login", "Não foi possivel estabeler uma conexão com o servidor")

    def screensLogin(self):
        self.QtStack.setCurrentIndex(0)
    
    def add_user(self):
        try:
            response = self.screen_signup.signup()
            if response == "success":
                self.QtStack.setCurrentIndex(0)
            else:
                QtWidgets.QMessageBox.about(None, "Cadastro", response)
        except:
            QtWidgets.QMessageBox.about(None, "Cadastro", "Não foi possivel estabeler uma conexão com o servidor")

    def add_insta_clicked(self):
        try:
            response = self.screen_add_insta.add()
            if response == "success":
                QtWidgets.QMessageBox.about(None, "Adicionar Instagram", "Instagram gravado com sucesso!")
                self.QtStack.setCurrentIndex(2)
            else:
                QtWidgets.QMessageBox.about(None, "Adicionar Instagram", response)
        except:
            QtWidgets.QMessageBox.about(None, "Adicionar Instagram", "Não foi possivel estabeler uma conexão com o servidor")
    
    def signup(self):
        self.QtStack.setCurrentIndex(1) 
    
    def home(self):
        self.QtStack.setCurrentIndex(2) 

    def logout(self):
        self.QtStack.setCurrentIndex(0) 

    def add_insta(self):
        self.QtStack.setCurrentIndex(3) 

    def post_scheduler(self):
        self.QtStack.setCurrentIndex(4) 

    def come_back(self):
        self.QtStack.setCurrentIndex(2) 

    def add(self):
        pass
    
    def upload(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.upload_path = path
            

    def scheduler(self):
        response = self.screen_post_scheduler.add(self.upload_path)
        try:
            if response == "success":
                QtWidgets.QMessageBox.about(None, "Agendar Postagem", "Agendamento gravada com sucesso!")
                self.QtStack.setCurrentIndex(2)
            else:
                QtWidgets.QMessageBox.about(None, "Agendar Postagem", response)
        except:
            QtWidgets.QMessageBox.about(None, "Agendar Postagem", "Não foi possivel estabeler uma conexão com o servidor")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
