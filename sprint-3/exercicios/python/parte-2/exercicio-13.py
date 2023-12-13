def my_map(lista, funcao):
    return [funcao(elemento) for elemento in lista]

def potencia_de_2(numero):
    return numero ** 2

lista_de_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista_de_entrada, potencia_de_2)

print(resultado)
