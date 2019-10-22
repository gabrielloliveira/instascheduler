# InstaScheduler

## Requisitos

- Python >= 3.6
- PyQt5

## Modo de usar

- Execute o script para a criação do banco de dados com: ```python server/create_db.py```

- Depois execute o servidor. ```python server/server.py```

- Logo após, abre outra aba no terminal e execute o arquivo ```main.py``` na raiz do projeto.

## O que havia na iteração passada

- Na iteração passada foi feita a exibição de todas as telas funcionando no modo de single-thread, a única funcionalidade que estava funcionando era a de login no sistema.

- Foi utilizado um banco dados que continha usuário e senha padrão de acesso, previamente cadastrado.

## O que mudou

- Esta interação conta com a implementação de multithread com cliente e servidor, para possibilitar a conexão de vários usuários ao mesmo tempo.

- Os dados estão sendo salvos e consultados no banco de dados. Funcionalidades que utilizam alguma propriedade do bd: cadastrar usuário, fazer login, agendar postagem e adicionar instagram.

- Também contém o upload de imagem (no caso da funcionalidade de agendar post). A imagem é salva numa pasta chamada chamada **uploads** que fica dentro da pasta **server**.

## Para iteração futuras

- Conectar com a API do instagram (API Graph do Facebook).

- Mandar a localização do cliente para o servidor.

- Transformar todos os inputs que pegam as senhas com as devidas seguranças. (ao invés de aparecer a senha, propriamente ditas, mostrar com os pontinhos * * * * *).

- Melhorar as respostas do server para uma melhor experiência com o usuário. Por exemplo, caso não tenha dado certo o login com o email e senha informado, o sistema apenas exibe "não foi possível realizar o login". Mas não se sabe qual foi o verdadeiro motivo. O servidor está fora? email ou senha incorretos?

- Criar alguma espécie de *jobs* que ficam verificando se existe postagens pendentes para enviar para a API do instagram. Caso exista, ele manda a requisção.
