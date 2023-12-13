def soma_string_numeros(string_numeros):
    numeros = [int(numero) for numero in string_numeros.split(',')]

    soma = sum(numeros)
    print(soma)

soma_string_numeros("1,3,4,6,10,76")
