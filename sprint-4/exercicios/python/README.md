# Exercícios Python

## Exercício 1

Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:

- **map**
- **filter**
- **sorted**
- **sum**

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

-  lista dos 5 maiores números pares em ordem decrescente;
- a soma destes valores.

## Resolução

```python
with open('number.txt', 'r') as f:
    lines = f.readlines()

pares = list(filter(lambda x: x % 2 == 0, map(int, lines)))

top_5 = sorted(pares, reverse=True)[:5]

soma = sum(top_5)

print(top_5)
print(soma)
```

---

## Exercício 2

Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:

- **len**
- **filter**
- **lamba**

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

## Resolução

```python
def conta_vogais(texto: str) -> int:
    vogais = list(filter(lambda x: x.lower() in 'aeiou', texto))
    return len(vogais)
```

---

## Exercício 3

A função _calcula_saldo_ recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função por exemplo.

    lancamentos = [
        (200,'D'),
        (300,'C'),
        (100,'C')
    ]

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final **200**.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

- **reduce** (_módulo functools_)
- **map**

## Resolução

```python
from functools import reduce

def calcula_saldo(lancamentos):
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    saldo = reduce(lambda a, b: a + b, valores)
    return saldo
```

---

## Exercício 4

A função _calcular_valor_maximo_ deve receber dois parâmetros, chamados de _operadores_ e _operandos_. Em _operadores_, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

**Veja o exemplo:**

- Entrada

> operadores = ['+','-','*','/','+']

> operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

- Aplicar as operações aos pares de operandos

> [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

- Obter o maior dos valores

> 12

Na resolução da atividade você deverá aplicar as seguintes funções:

- **max**
- **zip**
- **map**

## Resolução

```python
def calcular_valor_maximo(operadores, operandos) -> float:

    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
    }

    valores = map(lambda x: operacoes[x[0]](*x[1]), zip(operadores, operandos))
    return max(valores)
```

---

## Exercício 5

Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

- Nome do estudante
- Três maiores notas, em ordem decrescente
- Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

**_Nome: <nome estudante'> Notas: [n1, n2, n3] Média: <média>_**

**Exemplo:**

_Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67_

_Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33_

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

- **round**
- **map**
- **sorted**

## Resolução

```python
import csv

with open('estudantes.csv', 'r') as f:
    reader = csv.reader(f)
    data = sorted(list(reader), key=lambda x: x[0])

for row in data:
    nome = row[0]
    notas = list(map(float, row[1:]))

    top_3_notas = sorted(notas, reverse=True)[:3]

    media = round(sum(top_3_notas) / 3, 2)

    formatted_notas = [int(nota) if nota.is_integer() else round(nota, 1) for nota in top_3_notas]

    formatted_media = f'{media}'

    print(f"Nome: {nome} Notas: {formatted_notas} Média: {formatted_media}")
```