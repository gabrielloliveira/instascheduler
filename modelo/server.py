import struct 
import time
import pickle
import socket, threading

# host = "127.0.0.1"
# porta = 6124
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((host, porta))
# sock.listen(5)
# conn, addr = sock.accept()


# sock.listen(5)

def post(msg):
    nome = msg['nome']
    dados = msg['dados']
    with open(('arquivos_recebidos/'+nome), 'wb') as f:
        f.write(dados)
        f.close()


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexao: ", clientAddress)

    def run(self):
        data = b''
        while True:
            packet = self.csocket.recv(4096)
            if not packet: break
            data += packet
        msg = pickle.loads(data)
        func = msg['func']
        result = eval(f'{func}')(msg)
        print('data')
        self.csocket.close()


if __name__ == '__main__':
    addr = ("localhost", 6124)
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



        # data = b''
        # while True:
        #     packet = conn.recv(1)
        #     if not packet: break
        #     data += packet
        #     print(packet)

        # msg = pickle.loads(data)
        # print(data)
        # conn.close()

# with open('recebido.jpeg', 'wb') as f:
    # msg = pickle.loads(conn.recv(15284800) )
    # f.write(msg['msg'])
    # f.close()








# while True:
#     novo_sock, cliente = sock.accept()
#     with novo_sock:  # Caso haja uma nova conexão
#         ouvir = novo_sock.recv(2182760)  # Colocamos nosso novo objeto socket para ouvir
#         if ouvir != b"":  # Se houver uma mensagem...
#             """
#             Aqui usaremos os dados enviados na mensagem para criar nosso serielizador.

#             Com ele criado poderemos desempacotar os dados assim que recebermos.
#             Veja no cliente mais abaixo qual a primeira mensagem enviada.
#             """
#             mensagem, nome, dados = ouvir.decode().split(":")
#             serializar = struct.Struct("{}s {}s".format(len(nome.split()[0]), int(dados.split()[0])))
#             novo_sock.send("Pode enviar!".encode())  # Enviaremos uma mensagem para o cliente enviar os dados.
#             dados = novo_sock.recv(2182760)  # Agora iremos esperar por eles.
#             nome, arquivo = serializar.unpack(dados)  # Vamos desempacotar os dados
#             """
#             Agora enviamos uma mensagem dizendo que o arquivo foi recebido.

#             E iremos salva-lo no novo diretório criado.
#             """
#             novo_sock.send("Os dados do arquivo {} foram enviados.".format(nome.decode()).encode())
#             with open("arquivos_recebidos/{}".format(nome.decode()), 'wb') as novo_arquivo:
#                 novo_arquivo.write(arquivo)
#                 print("Arquivo {} salvo em arquivos_recebidos.".format(nome.decode()))

