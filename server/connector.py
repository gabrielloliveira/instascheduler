from hash import hash_password, verify_password
from datetime import datetime
import sqlite3
import os

class Connector():
    connection = None
    def __new__(cls):
        if Connector.connection is None:
            Connector.__instance = object.__new__(cls)
            
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "db.sqlite3")
            
            Connector.connection = sqlite3.connect(db_path, timeout=10)
            Connector.__instance._conn = Connector.connection
            Connector.__instance._cursor = Connector.__instance._conn.cursor()

        return Connector.__instance
            
    def __init__(self):
        self._conn = None
        self._cursor = None
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self._db_path = os.path.join(BASE_DIR, "db.sqlite3")

    def connect_db(self):
        self._conn = sqlite3.connect(self._db_path, timeout=10)
        self._cursor = self._conn.cursor()

    def return_password(self, data):
        if data:
            result = data[0]
            return result[2]
        
    def search_user(self, email, password):
        self.connect_db()

        try:
            with self._conn:
                result = self._cursor.execute("""
                SELECT * FROM user WHERE email=?
                """, (email,))
                stored_password = self.return_password(result.fetchall())
                if stored_password is not None and verify_password(stored_password, password):
                    data = {
                        'status': 'ok',
                        'message': "success",
                    }

                    return data

                data = {
                    'status': None,
                    'message': "Cliente não encontrado",
                }

                return data
            
            data = {
                'status': None,
                'message': "Não foi possível estabelecer uma conexão com o servidor",
            }

            return data

        finally:
            self._conn.close()

    def add_user(self, email, password):
        self.connect_db()

        try:
            with self._conn:
                result = self._cursor.execute("""
                SELECT * FROM user WHERE email=?
                """, (email,))

                if result.fetchone() is None:
                    new_password = hash_password(password)

                    self._cursor.execute("""
                    INSERT INTO user (email, password) values (?, ?)
                    """, (email, new_password,))

                    self._conn.commit()

                    data = {
                        'status': 'ok',
                        'message': "success",
                    }

                    return data


                data = {
                    'status': None,
                    'message': "Esse email já existe.",
                }

                return data

            data = {
                'status': None,
                'message': "Não foi possível estabelecer uma conexão com o servidor",
            }

            return data


        finally:
            self._conn.close()

    def add_insta(self, username, password, email):
        self.connect_db()

        try:
            with self._conn:

                instagram = self._cursor.execute("""
                SELECT * FROM instagram WHERE username=?
                """, (username,))
                
                instagram = instagram.fetchall()

                user = self._cursor.execute("""
                SELECT * FROM user WHERE email=?
                """, (email,))

                user = user.fetchone()

                if not instagram and user is not None:
                    self._cursor.execute("""
                    INSERT INTO instagram (username, password, user) values (?, ?, ?)
                    """, (username, password, user[0],))

                    self._conn.commit()

                    data = {
                        'status': 'ok',
                        'message': "success",
                    }

                    return data


                data = {
                    'status': None,
                    'message': "Esse usuário já foi cadastrado",
                }

                return data

            data = {
                'status': None,
                'message': "Não foi possível estabeler uma conexão com o servidor",
            }

            return data

        finally:
            self._conn.close()

    def add_schedule(self, img_path, subtitle, location, username, date, email):
        self.connect_db()

        try:
            with self._conn:
                user = self._cursor.execute("""
                SELECT * FROM user where email=?
                """, (email,))

                user = user.fetchone()

                if user is None:
                    data = {
                        'status': None,
                        'message': "Não é possível realizar cadastro. Realize login com uma conta ativa",
                    }
                    return data
                
                instagram = self._cursor.execute("""
                SELECT * FROM instagram WHERE username=? and user=?
                """, (username, user[0],))
                
                instagram = instagram.fetchone()

                if instagram is None:
                    data = {
                        'status': None,
                        'message': "Impossível encontrar Instagram informado",
                    }
                    return data

                date_now = str(datetime.now())

                self._cursor.execute("""
                INSERT INTO scheduler (image, subtitle, location, account, created, date_scheduler) 
                values (?, ?, ?, ?, ?, ?)
                """, (img_path, subtitle, location, instagram[0], date_now, date,))

                self._conn.commit()

                
                data = {
                    'status': 'ok',
                    'message': "sucess",
                }
                return data

            data = {
                'status': 'ok',
                'message': "Não foi possivel estabeler uma conexão com o servidores",
            }
            return data

        finally:
            self._conn.close()
   
    def scheduler(self):
        self.connect_db()

        try:
            with self._conn:
                result = self._cursor.execute("""SELECT * FROM scheduler """)
            return result.fetchall()

        finally:
            self._conn.close()

    def instagram(self, id1):
        self.connect_db()

        try:
            with self._conn:
                result = self._cursor.execute("""
                SELECT * FROM instagram WHERE id=?
                """, (id1,))
            return result.fetchall()

        finally:
            self._conn.close()

    def close(self):
        self._conn.close()
