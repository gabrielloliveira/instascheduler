from connector import Connector
import socket
import pickle

addr = ("localhost", 7000)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10) 

con, cliente = serv_socket.accept()

def login(received):
    email = received['email']
    password = received['password']
    conn = Connector()
    result = conn.search_user(email, password)
    conn.close()
    return result

while(True):
    received = pickle.loads(con.recv(1024))
    func = received['func']
    try:
        result = eval(f'{func}')(received)
        message = {
            'status': 'success' if result is not None else 'error'
        }
        con.send(pickle.dumps(message))

    except:
        serv_socket.close()

serv_socket.close()
