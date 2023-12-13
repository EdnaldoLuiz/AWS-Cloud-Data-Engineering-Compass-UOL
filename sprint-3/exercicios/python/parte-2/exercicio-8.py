palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    palavra = palavra.lower() 
    palavra_invertida = palavra[::-1]  

    if palavra == palavra_invertida:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
