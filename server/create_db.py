import sqlite3

# conectando...
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# criando a tabela (user)
cursor.execute("""
CREATE TABLE user (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(2000) NOT NULL UNIQUE,
    password VARCHAR(2000) NOT NULL
);
""")
print("Criando a tabela user ... OK")

# criando a tabela (instagram)
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

# criando a tabela (scheduler)
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

# desconectando...
conn.close()
