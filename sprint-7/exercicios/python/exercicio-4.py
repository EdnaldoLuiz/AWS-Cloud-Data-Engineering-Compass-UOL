import pandas as pd

caminho_arquivo = 'sprint-7\\exercicios\\python\\actors.csv'

dados = pd.read_csv(caminho_arquivo)

count_valor = dados['#1 Movie'].value_counts()

for i, (filme, qtd) in enumerate(count_valor.items(), start=1):
    print(f'{i}- O filme {filme} aparece {qtd} vez(es) no dataset')