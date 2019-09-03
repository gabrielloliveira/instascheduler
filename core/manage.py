import os
from datetime import datetime

from create_user import CreateUser
from instagram import Instagram
from sheduler import Scheduler
from login import Login
from bd import Bd

def menuInitial(db):
    while(True):
        print(''' 
        |*******************|
        |1-Fazer login      |
        |2-Cadastrar        |
        *********************
        ''')
        op = int(input("opcao: "))
        os.system("clear")
        if op == 1:
            boolean = False
            while( boolean == False):
                email = input("email: ")
                password = input("Password: ")
                login = Login()
                login.email = email
                login.password = password
                boolean = login.data_verification(db)
            return boolean
        elif op == 2:
            register = CreateUser()
            email = input("email: ")
            password = input("Password: ")
            register.email = email
            register.password = password
            db.accounts = register.registering()

def menuSecondary(db,accountLogin):
    while(True):
        print(''' 
        |**********************|
        |1-Cadastrar publicação|
        |2-Sair                |
        ************************
        ''')
        op = int(input("opcao: "))
        os.system("clear")
        if op == 1:
            scheduler = Scheduler()
            scheduler.image = input("Caminho da publicacao: ") 
            scheduler.subtitle = input("Subtitle da publicaco: ")
            scheduler.location = input("Locazação da publicaco: ")
            '''----------------------------------------------------'''
            account = Instagram()
            account.username = input("Nome conta que será publicado: ")
            account.password = input("senha conta que será publicado: ")
            account.user = accountLogin
            '''----------------------------------------------------'''
            scheduler.account = account
            scheduler.created = datetime.today()
            scheduler.date_scheduler = input("Data para ser publicado a foto(dd/mm/YY HH:MM): ")
            db.publication = scheduler

        if op == 2:
            data = db.publication[0].date_scheduler
            exe = "python3 mandaremail.py Sua publicacao será feita as "+str(data) +"&"
            os.system(exe)
            #print("Sua publicacao será feita")
            return False


if __name__ == "__main__":
    db = Bd()
    accounts = menuInitial(db)
    menuSecondary(db,accounts)
    
