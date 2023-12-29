# Exercício 1

## Pergunta

Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada.

Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.

## Resolução

### Criação da imagem

```docker
docker build -t carguru-ex1 .
```

### Executar o container

> Obs: usei o parametro --rm para ele ser excluido após a execução

```docker
docker run --rm carguru-ex1
```
