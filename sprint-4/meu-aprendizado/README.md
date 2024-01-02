# Meu Aprendizado

Essa Sprint foi cheia de aprendizados, então ainda estou melhorando minhas anotações e logo estarei fazendo projetos com esses aprendizados e colocarei aqui.

## Índice

- [Python Funcional](#python)
- [Docker](#Docker)
- [Estatística](#estatistica)

## Python Funcional

O paradigma funcional em Python oferece uma abordagem diferente para resolver problemas, enfatizando a imutabilidade e a expressividade do código.

### Funções de Ordem Superior

Funções que aceitam outras funções como argumentos ou as retornam como resultados. Facilitam a composição de código.

```python
def aplicar_funcao(func, valor):
    return func(valor)

dobro = lambda x: x * 2
resultado = aplicar_funcao(dobro, 5)
print(resultado)  # Saída: 10
```

### Expressões Lambda

Funções anônimas e de única linha. Úteis para situações em que uma função completa não é necessária.

```python
quadrado = lambda x: x ** 2
print(quadrado(4))  # Saída: 16
```

### Decorators

Funções que modificam o comportamento de outras funções. Útil para reutilização de código.


```python
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da chamada da função")
        resultado = func(*args, **kwargs)
        print("Depois da chamada da função")
        return resultado
    return wrapper

@decorador
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
# Saída:
# Antes da chamada da função
# Olá, João!
# Depois da chamada da função
```

### Map

A função map aplica uma função a cada elemento de uma coleção, retornando um iterador.

# Exemplo: Dobrar cada elemento de uma lista

```python
numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
print(list(dobro))  # Saída: [2, 4, 6, 8, 10]
```

### Reduce

A função reduce realiza a redução de uma coleção a um único valor, aplicando uma função cumulativa aos elementos.

### Exemplo: Somar todos os elementos de uma lista

```python
numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15
```

### Filter

A função filter filtra elementos de uma coleção com base em uma função de teste.

### Exemplo: Filtrar apenas números pares

```python
numeros = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4]
```

## Docker

O Docker é uma plataforma que simplifica o desenvolvimento, implementação e execução de aplicações usando contêineres. Contêineres permitem empacotar uma aplicação e suas dependências em um ambiente isolado, garantindo consistência em diferentes ambientes.

### Dockerfile

O Dockerfile é um script que contém instruções para construir uma imagem Docker. Ele define o ambiente de execução da aplicação.

###  Exemplo de Dockerfile para uma aplicação Python

```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### Docker Compose

O Docker Compose simplifica a orquestração de vários contêineres. Ele usa um arquivo YAML para configurar os serviços, redes e volumes.

### Exemplo de docker-compose.yml

```yml
version: '3'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
  app:
    build:
      context: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:latest
```

### Volumes e Persistência de Dados

Volumes no Docker permitem persistir dados entre execuções de contêineres. Eles são essenciais para armazenamento de dados que sobrevivem à vida do contêiner.

###  Comando de exemplo para criar um volume

```docker
docker run -v /path/no/host:/caminho/no/contêiner ...
```

### Redes no Docker

As redes no Docker facilitam a comunicação entre contêineres. Por padrão, o Docker cria uma rede para cada aplicação.

### Comandos de exemplo para criar e usar uma rede

```docker
docker network create minha-rede
docker run --network=minha-rede ...
```

### Principais Comandos do Docker

Alguns comandos essenciais do Docker para interagir com contêineres:

- `docker build`: Construir uma imagem Docker.
- `docker run`: Executar um contêiner.
- `docker ps`: Listar contêineres em execução.
- `docker stop`: Parar um contêiner.
- `docker-compose up`: Iniciar serviços definidos no Docker Compose.


## Estatística

Este repositório contém informações e conceitos relacionados à estatística descritiva. Abaixo estão as principais seções:

### Dados, Informação e Conhecimento

Dados são a matéria-prima. Informação é a organização significativa desses dados. Conhecimento é a compreensão profunda e aplicação da informação.

<img src="https://www.researchgate.net/publication/330893006/figure/fig2/AS:723130851024897@1549419238833/Figura-2-Dados-informacao-e-conhecimento-Davenport-e-Prusak-1998a-p-18.ppm"  width=100%>

### Gráficos Estatísticos

> Obs: Recomendação do Seaborn e Matplotlib para criação de gráficos.

1. **Gráfico de Barras:**
   - Ideal para variáveis qualitativas.
   - Composto por retângulos horizontais.

<p align=center><b>Exemplo</b></p>

<img src="https://www.infoenem.com.br/wp-content/uploads/2020/04/graficobarras.png"  width=100%>


3. **Gráficos de Setores ou Pizza:**
   - Divide um círculo proporcionalmente às frequências.
   - Indicado para comparação com o total.

<p align=center><b>Exemplo</b></p>

<img src="https://4.bp.blogspot.com/-XXGjTRGw8qY/Uc2uzb-UyvI/AAAAAAAAUcQ/T_V3cG6nFHE/s557/Sem+t%C3%ADtulo.jpg"  width=100%>

4. **Gráfico de Linhas:**
   - Adequado para séries temporais.

<p align=center><b>Exemplo</b></p>

<img src="https://escolaeducacao.com.br/wp-content/uploads/2020/03/grafico-linhas.png"  width=100%>

5. **Histogramas:**
   - Representa a distribuição de frequência.
   - Limites no eixo horizontal.

<p align=center><b>Exemplo</b></p>

<img src="https://codersdaily.in/media/uploads/admin/2022/07/09/image-20220709124038-1.png"  width=100%>

## Medidas Estatísticas

1. **Medidas de Tendência Central:**
   - Resumo de dados populacionais (parâmetros) ou amostrais (estatísticas).

<p align=center><b>Exemplo</b></p>

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXY49G5SiFLPM19KNjWwmDK95iPJMpaScT2A&usqp=CAU"  width=100%>


### Média:
- **Definição:** A média é uma medida de tendência central que representa o valor médio de um conjunto de dados.
- **Cálculo:** Soma de todos os valores dividida pelo número de observações.
- **Características:**
  - Sensível a valores extremos (outliers).
  - Calculada mais facilmente e frequentemente usada.

### Moda:
- **Definição:** A moda é o valor que ocorre com maior frequência em um conjunto de dados.
- **Cálculo:** Determinar o valor com a maior frequência.
- **Características:**
  - Pode haver mais de uma moda (dados bimodais ou multimodais).
  - Pode ser aplicada a dados qualitativos ou quantitativos.

### Mediana:
- **Definição:** A mediana é o valor que está no centro de um conjunto de dados ordenado.
- **Cálculo:** Arranjar os dados em ordem crescente e encontrar o valor no meio.
- **Características:**
  - Menos sensível a valores extremos.
  - Útil em distribuições assimétricas.

<p align=center><b>Exemplo</b></p>

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVJs1eJOmis68P3qKSH_4quT8p1feqOOtUiQ&usqp=CAU"  width=100%>

### Estatísticas Descritivas

- **Medidas de Assimetria:**
   - Simétrica (As=0)
   - Assimétrica Negativa (As>0)
   - Assimétrica Positiva (As<0)

   <p align=center><b>Exemplo</b></p>

<img src="https://th.bing.com/th/id/R.2e4acbd44a783135a1777dbb2cf210a1?rik=bnaNmBnIRgUCZw&pid=ImgRaw&r=0&sres=1&sresct=1"  width=100%>

- **Medidas de Curtose:**
   - Quantifica a dispersão e achatamento.
   - Classificação: Leptocúrtica, Mesocúrtica, Platicúrtica.

   <p align=center><b>Exemplo</b></p>

<img src="https://4.bp.blogspot.com/-CeSKUrvUsq4/W-3iepg3IEI/AAAAAAAAFFw/Dh79KCpgcGUk_Ra2WnxhArUJ7t4b1L21QCLcBGAs/s1600/curtose.JPG" width=100%>

- **Boxplot:**
   - Representação gráfica da distribuição estatística.

   <p align=center><b>Exemplo</b></p>

<img src="https://static.wixstatic.com/media/d8f2a2_13ae00396b764d80b0fef53986739ffd~mv2.png/v1/fill/w_550,h_503,al_c/d8f2a2_13ae00396b764d80b0fef53986739ffd~mv2.png" width=100%>