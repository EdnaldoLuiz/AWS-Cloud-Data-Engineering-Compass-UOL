# Exercício 2

## Pergunta

É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

## Resolução

Sim, é possível reutilizar containers parados no Docker. Isso pode ser feito com o seguinte comando:

```docker
docker start <ID ou nome_do_conteiner>
```

## Meu exemplo

Por exemplo, no exercício anterior eu utilizei o seguinte comando para reutilizar meu container:

```docker
docker start carguru-ex1
```

Porem como estamos falando de um container de script sem processamento contínuo no caso do carguru.py (carguru-ex1), o contêiner terminará assim que o script for concluído.
