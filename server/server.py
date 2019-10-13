from connector import Connector
import socket, threading
import socket
import pickle


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
    
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):
        # while(True): //juguei q n é necessario ficar em loop devido a conecção q é fechada 
        try:
            received = pickle.loads(self.csocket.recv(6144))
            print(received)
        except:
            pass
        func = received['func']
        # try:
        result = eval(f'{func}')(received)
        message = {
            'status': 'success' if result is not None else 'error'
        }
        print(message)
        self.csocket.send(pickle.dumps(message))

        # except:
        self.csocket.close()

        # self.csocket.close()

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