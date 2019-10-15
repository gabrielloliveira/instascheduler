from connector import Connector
from datetime import datetime
import socket, threading
import socket
import pickle
import os


# con, cliente = serv_socket.accept()

def login(received):
    email = received['email']
    password = received['password']
    conn = Connector()
    result = conn.search_user(email, password)
    return result

def signup(received):
    email = received['email']
    password = received['password']
    conn = Connector()
    result = conn.add_user(email, password)
    return result

def add_insta(received):
    username = received['username']
    password = received['password']
    user = received['user']
    conn = Connector()
    result = conn.add_insta(username, password, user)
    return result


def schedule_posting(received):
    user = received['user']
    img = received['img']
    subtitle = received['subtitle']
    location = received['location']
    instagram = received['instagram']
    date = received['date']

    date_image = f'{datetime.now().year}-' + f'{datetime.now().month}-' + f'{datetime.now().day}'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, f"uploads/{date_image}-{user}-{nome}")

    # Salvando a imagem na pasta upload com o nome padrão : yyyy-mm-dd-email-name.jpeg
    with open((img_path), 'wb') as f:
        f.write(dados)
        f.close()

    conn = Connector()
    result = conn.add_schedule(img_path, subtitle, location, instagram, date, user)
    return result
    
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):

        data = b''
        
        while True:
            packet = self.csocket.recv(6144) 
            data += packet
            try:
                received = pickle.loads(data)
                break
            except:
                pass
            
        received = pickle.loads(data)

        func = received['func']
        result = eval(f'{func}')(received)
        message = {
            'status': 'success' if result is not None else 'error'
        }
        print(message)
        self.csocket.send(pickle.dumps(message))
        self.csocket.close()

if __name__ == '__main__':
    addr = ("localhost", 7000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(10)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()