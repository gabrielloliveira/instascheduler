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
        self._conn = Connector.connection
        self._cursor = self._conn.cursor()  

    def search_user(self, email, password):
        result = self._cursor.execute("""
        SELECT * FROM user WHERE email=? and password=?
        """, (email, password))

        return result.fetchone()

    def close(self):
        self._conn.close()
