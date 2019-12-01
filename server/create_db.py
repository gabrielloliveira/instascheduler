import sqlite3

"""Script to create database structure."""

# connection...
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# creating the user table
cursor.execute("""
CREATE TABLE user (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(2000) NOT NULL UNIQUE,
    password VARCHAR(2000) NOT NULL
);
""")
print("Criando a tabela user ... OK")

# creating the instagram table
cursor.execute("""
CREATE TABLE instagram (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(2000) NOT NULL UNIQUE,
    password VARCHAR(2000) NOT NULL,
    user INTEGER NOT NULL,
    FOREIGN KEY(user) REFERENCES user(id)
);
""")
print("Criando a tabela instagram ... OK")

# creating the scheduler table
cursor.execute("""
CREATE TABLE scheduler (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    image VARCHAR(2000) NOT NULL,
    subtitle VARCHAR(2000),
    location VARCHAR(2000),
    account INTEGER NOT NULL,
    created DATE NOT NULL,
    date_scheduler DATE NOT NULL,
    FOREIGN KEY(account) REFERENCES instagram(id)
);
""")
print("Criando a tabela scheduler ... OK")

print('BD criado com sucesso.')

# closing the database connection...
conn.close()
