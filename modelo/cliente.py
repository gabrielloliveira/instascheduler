import struct
import socket
import pickle
arquivo = 'img.jpeg'
host = '127.0.0.1'
porta = 6124
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria nosso objeto socket
sock.connect((host, porta))

with open(arquivo, 'rb') as arq:
    dados_arquivo = arq.read()
    arq.close()

msg = {
    'func':'post',
    'nome':arquivo,
    'dados':dados_arquivo
}

sock.send(pickle.dumps(msg))

sock.close()
    # dados_upload = serializar.pack(*[arquivo.encode(), dados_arquivo])
    # serializar = struct.Struct("{}s {}s".format(len(arquivo), len(dados_arquivo)))


# with open(arquivo, 'rb') as arq:
#     dados_arquivo = arq.read()
#     serializar = struct.Struct("{}s {}s".format(len(arquivo), len(dados_arquivo)))
#     dados_upload = serializar.pack(*[arquivo.encode(), dados_arquivo])

# sock.send("Enviarei um arquivo chamado: {} contendo: {} bytes".format(
#     arquivo, len(dados_arquivo)).encode())  # Enviamos a mensagem com o nome e tamanho do arquivo.
# ouvir = sock.recv(2182760)  # Aguardamos uma mensagem de confirmação do servidor.
# if ouvir.decode() == "Pode enviar!":
#     sock.send(dados_upload)  # Enviamos os dados empacotados.
#     resposta = sock.recv(2182760)  # Aguardamos a confirmação de que os dados foram enviados.
#     print(resposta.decode())
