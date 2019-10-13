import sqlite3
import os

class Connector():
    connection = None
    def __new__(cls):
        if Connector.connection is None:
            Connector.__instance = object.__new__(cls)
            
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "db.sqlite3")
            
            Connector.connection = sqlite3.connect(db_path)
            Connector.__instance._conn = Connector.connection
            Connector.__instance._cursor = Connector.__instance._conn.cursor()

        return Connector.__instance
            
    def __init__(self):
        self._conn = None
        self._cursor = None
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self._db_path = os.path.join(BASE_DIR, "db.sqlite3")

    def connect_db(self):
        self._conn = sqlite3.connect(self._db_path)
        self._cursor = self._conn.cursor()

    def search_user(self, email, password):
        self.connect_db()

        try:
            with self._conn:
                result = self._cursor.execute("""
                SELECT * FROM user WHERE email=? and password=?
                """, (email, password))

                return result.fetchone()

            return None

        finally:
            self._conn.close()

    def close(self):
        self._conn.close()
