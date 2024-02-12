import pandas as pd

caminho_arquivo = 'sprint-7\\exercicios\\python\\actors.csv'
df = pd.read_csv(caminho_arquivo)

media_numero_filmes = df['Number of Movies'].mean()

print(f'A média do número de filmes é {media_numero_filmes:.2f}')