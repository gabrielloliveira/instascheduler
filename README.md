# InstaScheduler

## Requisitos

- Python >= 3.6

## Modo de usar

- Execute o script para a criação do banco de dados com: ```python server/create_db.py```

- Depois execute o servidor. ```python server/server.py```

- Logo após, abre outra aba no terminal e execute o arquivo ```main.py``` na raiz do projeto.

## O que havia na iteração passada

- Na iteração passada foi mostrado todas as telas e funcionando para somente um usuário, o cadastro usuários não estava disponível.
- Foi utilizado banco dados para guardar um login de acesso 
- Fois mostrado funcionando como cliente servidor, com um usuário utilizando por vez(mono thread)

## O que mudou

- Essa interação conta com multithread no servidor para utilização de vários usuários ao mesmo tempo
- Utiliza o banco de dados para cadastrar usuário,fazer login, agendar postagem, adcionar instagram e validar dados.
- Faz upload de de forma fácil 
- Excluindo a localização o código que executa a função cliente manda todas as informações para o servidor, inclusive imagens.

## Para iteração futuras
- Conectar a api do instagram.
- Mandar a localização do cliente para o servidor.

