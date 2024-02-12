import pandas as pd

arquivo = 'sprint-7\\exercicios\\python\\actors.csv'

df = pd.read_csv(arquivo)

df.rename(columns={
    'Number of Movies': 'numero_de_filmes',
    'numero_1_filme': '#1 Movie'
}, inplace=True)

media_por_filme = df['Total Gross'] / df['numero_de_filmes']

atores_atrizes_maior_media = df[media_por_filme == media_por_filme.max()]


nome_ator_atriz_maior_media = atores_atrizes_maior_media['Actor'].to_string(index=False)

print("O ator/atriz com a maior média por filme é", nome_ator_atriz_maior_media)