import json

with open('person.json', 'r') as arquivo_json:
    dados_json = json.load(arquivo_json)

    print(dados_json)
