# Passando para refined apenas os dados vindos do CSV que são do genero do genero Comedy e/ou Animation
# e também apenas as linhas que não apresentão valores nulos \N
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col
from pyspark.sql.functions import array_contains, split

# Inicializando o GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# Lendo os dados da tabela criada pelo crawler
dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="glue-lab", table_name="trusted"
)

# Convertendo o DynamicFrame para um DataFrame
dataframe = dynamic_frame.toDF()

# Dividindo a coluna de gênero em uma lista
dataframe = dataframe.withColumn("genero", split(col("genero"), ","))

# Filtrando os filmes de gênero Comedy e Animation
dataframe = dataframe.filter(
    array_contains(col("genero"), "Comedy") | array_contains(col("genero"), "Animation")
)

# Removendo as linhas com valores nulos
dataframe = dataframe.filter(col("generoArtista") != "\\N")
dataframe = dataframe.filter(col("personagem") != "\\N")
dataframe = dataframe.filter(col("nomeArtista") != "\\N")
dataframe = dataframe.filter(col("anoNascimento") != "\\N")
dataframe = dataframe.filter(col("anoFalecimento") != "\\N")
dataframe = dataframe.filter(col("profissao") != "\\N")
dataframe = dataframe.filter(col("titulosMaisConhecidos") != "\\N")

# Criando as tabelas de dimensões e a tabela de fatos
dim_filme = dataframe.select("id", "title")
dim_ator_principal = dataframe.select("id", "main_actor")
dim_diretor = dataframe.select("id", "director")
dim_data_lancamento = dataframe.select("id", "release_date")
dim_orcamento = dataframe.select("id", "budget")
dim_receita = dataframe.select("id", "revenue")
fato_votacao_filme = dataframe.select("id", "vote_average", "vote_count")

# Caminho do S3
s3_path = "s3://desafios-etl/Refined/"

# Escrevendo os dados nas tabelas correspondentes na camada Refined
dim_filme.write.parquet(s3_path + "CSVdim_filme")
dim_ator_principal.write.parquet(s3_path + "CSVdim_ator_principal")
dim_diretor.write.parquet(s3_path + "CSVdim_diretor")
dim_data_lancamento.write.parquet(s3_path + "CSVdim_data_lancamento")
dim_orcamento.write.parquet(s3_path + "CSVdim_orcamento")
dim_receita.write.parquet(s3_path + "CSVdim_receita")
fato_votacao_filme.write.parquet(s3_path + "CSVfato_votacao_filme")