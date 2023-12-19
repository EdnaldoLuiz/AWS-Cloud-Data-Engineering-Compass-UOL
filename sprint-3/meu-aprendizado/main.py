import pandas as pd
from sqlalchemy import create_engine

def read_csv_file(file_path='actors.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return None

engine = create_engine('mysql+pymysql://root:06022003@localhost/py')

read_csv_file().to_sql('atores', con=engine, if_exists='replace', index=False)