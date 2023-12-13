primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (primeiro_nome, sobre_nome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f'{indice} - {primeiro_nome} {sobre_nome} está com {idade} anos')
