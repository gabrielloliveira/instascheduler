from connector import Connector
from datetime import datetime
import socket, threading
import socket
import pickle
import os
import time
from datetime import datetime


# con, cliente = serv_socket.accept()

def send_api(received, img_path):
    import requests
    import json

    url = "http://localhost:3000/api/"

    files = {
        'img': open(img_path, 'rb'),
    }

    parms = {
        'subtitle': received['subtitle'],
        'location': 'ufpi',
        'filtro': 'maven',
        'instagram': received['instagram'][1:]
    }

    response = requests.post(url, data=parms, files=files)

    if response.status_code == 200:
        return 'success'
    else:
        return 'Não foi possível cadastrar a imagem.'

def thread_function1(received):
    # pass
    mydatetime = datetime.strptime(received[-1], "%Y-%m-%d %H:%M:%S")
    string = str((mydatetime-datetime.now()).total_seconds())
    seg = string.split('.')[0]
    print("to esperando aqui")
    time.sleep(int(seg))
    print("Fui")
    conn = Connector()
    insta = conn.instagram( received[-3])
    dicionario = { 
        'subtitle': received[2],
        'instagram': insta[1]
    }
    path = received[1]
    send_api(dicionario, (path))


def scheduler():
    conn = Connector()
    schedulerListReturn = conn.scheduler()
    schedulerList = []

    # print(schedulerList)
    for i in schedulerListReturn:
        lista = i[-1]

    mydatetime = datetime.strptime(lista, "%Y-%m-%d %H:%M:%S")

    if mydatetime > datetime.now():
        x = threading.Thread(target=thread_function1, args=(schedulerListReturn[-1],))
        x.start()
        return "success"
    return 'Horario invalido'
    

def login(received):
    email = received['email']
    password = received['password']
    conn = Connector()
    result = conn.search_user(email, password)
    return result['message']

def signup(received):
    email = received['email']
    password = received['password']
    conn = Connector()
    result = conn.add_user(email, password)
    return result['message']

def add_insta(received):
    username = received['username']
    password = received['password']
    user = received['user']
    conn = Connector()
    result = conn.add_insta(username, password, user)
    return result['message']


def schedule_posting(received):
    user = received['user']
    img = received['img']
    binary_image = received['binary_image']
    subtitle = received['subtitle']
    location = received['location']
    instagram = received['instagram']
    date = received['date']

    date_image = f'{datetime.now().year}-' + f'{datetime.now().month}-' + f'{datetime.now().day}'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, f"uploads/{date_image}-{user}-{img}")

    if date < datetime.now():
        return 'Horario invalido'

    conn = Connector()
    result = conn.add_schedule(img_path, subtitle, location, instagram, date, user)
    if result['status'] != None:
        # Salvando a imagem na pasta upload com o nome padrão : yyyy-mm-dd-email-name.jpeg
        with open((img_path), 'wb') as f:
            f.write(binary_image)
            f.close()
        scheduler()
        time.sleep(1)
        return 'success'
        # return send_api(received, img_path)

    return result['message']


def get_last_two_schedules(received):
    """Function to connect to the database and get the last two scheduled posts
    from a user.

    Args:
        received: a dictionary containing the variables passed in the connection.
    """
    conn = Connector()
    result = conn.get_last_two_schedules(received['email'])
    if result['status'] == "ok":
        image_1 = b''
        image_2 = b''

        with open(result['schedules'][0][1], 'rb') as arq:
            image_1 = arq.read()
            arq.close()

        with open(result['schedules'][1][1], 'rb') as arq:
            image_2 = arq.read()
            arq.close()

        data = {
            'status': "send_image",
            'image_1': image_1, 
            'image_2': image_2, 
        }

        return data

    return result['status']
    

def instagram_user(received):
    user = received['user']
    conn = Connector()
    result = conn.instagram_user(user)
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
            'status': result
        }
        print(message)
        self.csocket.send(pickle.dumps(message))
        self.csocket.close()

if __name__ == '__main__':
    addr = ("", 7000)
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