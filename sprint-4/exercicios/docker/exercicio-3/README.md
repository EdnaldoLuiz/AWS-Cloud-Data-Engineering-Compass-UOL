# Exercício 3

## Pergunta

Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.

- Criar novo script Python que implementa o algoritmo a seguir:

    1. Receber uma string via input

    2. Gerar o hash  da string por meio do algoritmo SHA-1

    3. Imprimir o hash em tela, utilizando o método hexdigest

    4. Retornar ao passo 1


- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente
- Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento
- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.

## Resolução

- Link da imagem Docker no meu Dockerhub [aqui](https://hub.docker.com/repository/docker/ednaldoluiz/mascarar-dados/general)

- Script Python

```python
import hashlib

while True:
    input_string = input("Digite uma string para mascarar (ou 'sair' para sair): ")

    if input_string.lower() == 'sair':
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    print(f"Hash SHA-1 da string '{input_string}': {sha1_hash}")
```

- Dockerfile

```dockerfile
FROM python:3.9

COPY mascarar_dados.py /app/mascarar_dados.py

WORKDIR /app

CMD ["python", "mascarar_dados.py"]
```

### Comandos utilizados

Para criar a imagem

```docker
docker build -t mascarar-dados .
```
Para Executar o container em modo interativo e excluir ele após o término

```docker
docker run -it --rm mascarar-dados
```

