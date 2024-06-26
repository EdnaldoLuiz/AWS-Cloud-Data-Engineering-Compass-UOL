import requests
import pandas as pd

from IPython.display import display

api_key = "e4f6fca45b95d5b6b44904d806c9fe0d"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()

filmes = []

for movie in data["results"]:
    df = pd.DataFrame(
        {
            "Titulo": [movie["title"]],
            "Data de lançamento": [movie["release_date"]],
            "Visão geral": [movie["overview"]],
            "Votos": [movie["vote_count"]],
            "Média de votos:": [movie["vote_average"]],
        }
    )
    filmes.append(df)

df_final = pd.concat(filmes)
display(df_final)