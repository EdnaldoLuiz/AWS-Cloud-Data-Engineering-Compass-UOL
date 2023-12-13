import datetime

nome = input("Digite seu nome: ")
idade_atual = int(input("Digite sua idade atual: "))

ano_atual = datetime.datetime.now().year
ano_completar_100 = ano_atual + (100 - idade_atual)

print(ano_completar_100)