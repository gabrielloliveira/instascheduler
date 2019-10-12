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
    conn.close()
    return result

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):
        while(True):
            data = b""
            while True:
                # print('eii1')
                packet = self.csocket.recv(4096)
                if not packet: break
                data += packet
                break
                # print('eii')

            
            try:
                # print('disgraca1')
                data_arr = pickle.loads(data)  
                # print('disgraca')
            except EOFError:
                continue  
            received = data_arr 
            print('deu certo', data_arr)
            # received = pickle.loads(self.csocket.recv())
            func = received['func']
            try:
                # result = eval(f'{func}')(received)
                message = {
                    'status': 'success' 
                    # 'status': 'success' if result is not None else 'error'
                }
                # self.csocket.send(pickle.dumps(message))
                self.csocket.send(message.encode())

            except:
                self.csocket.close()
            break
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
