from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
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

        self.screen_sigup = Ui_Signup()
        self.screen_sigup.setupUi(self.stack1)

        self.screen_home = Ui_Home()
        self.screen_home.setupUi(self.stack2)

        self.acreen_add_insta = Ui_Add_insta()
        self.acreen_add_insta.setupUi(self.stack3)

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
        self.setupUi(self)

        self.screen_login.login_button.clicked.connect(self.login)
        # self.screen_login.link_signup.clicked.connect(self.signup)

        # self.tela_inicio.botao_criar_conta.clicked.connect(self.openCriarConta)

        # self.tela_cadastro.botao_salvar.clicked.connect(self.criarConta)
        # self.tela_cadastro.toolButton.clicked.connect(self.voltarInicio)

        # self.tela_principal.cadastrar_novo_livro.clicked.connect(self.openCadastrarLivro)
        # self.tela_principal.ver_acervo.clicked.connect(self.openAcervoLivro)
        # self.tela_principal.sair.clicked.connect(self.voltarInicio)

        # self.tela_cadastro_livro.botao_salvar_livro.clicked.connect(self.cadastrarLivro)
        # self.tela_cadastro_livro.buttonVoltar.clicked.connect(self.voltarPrincipal)

        # self.tela_acervo.sair.clicked.connect(self.entrar)


    def login(self):
        try:
            self.screen_login.login()
            self.QtStack.setCurrentIndex(2)
        except:
            QtWidgets.QMessageBox.about(None, self, "Cliente não encontrado")

    def signup(self):
        self.QtStack.setCurrentIndex(1)

    # def entrar(self):
    #     self.QtStack.setCurrentIndex(2)

    # def openCriarConta(self):
    #     self.QtStack.setCurrentIndex(1)

    # def voltarInicio(self):
    #     self.QtStack.setCurrentIndex(0)

    # def criarConta(self):
    #     self.QtStack.setCurrentIndex(0)

    # def openCadastrarLivro(self):
    #     self.QtStack.setCurrentIndex(3)

    # def openAcervoLivro(self):
    #     self.QtStack.setCurrentIndex(4)

    # def voltarPrincipal(self):
    #     self.QtStack.setCurrentIndex(2)

    # def cadastrarLivro(self):
    #     self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())