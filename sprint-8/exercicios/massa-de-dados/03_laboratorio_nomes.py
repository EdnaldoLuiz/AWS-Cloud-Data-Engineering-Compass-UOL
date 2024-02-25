# Passo 1: Instalar a biblioteca names

# Passo 2: Importar as bibliotecas random, time, os e names
import random
import time
import os
import names

# Passo 3: Definir os parâmetros para a geração do dataset
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Passo 4: Gerar os nomes aleatórios
aux = []

for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
dados = []

for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Passo 5: Gerar um txt contendo todos os nomes
with open("nomes_aleatorios.txt", "w") as arquivo:
    arquivo.write("\n".join(dados))

print("Arquivo gerado com sucesso!")