from pyspark import SparkContext, SparkConf
from awsglue.context import GlueContext
from pyspark.sql import DataFrame
from pyspark.sql.functions import lit

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Lendo o primeiro arquivo json da Raw Zone para obter o esquema
file_path = "desafios-etl/Raw/tmdb/json/2024/02/24/filmes__01.json"
full_file_path = f"s3://{file_path}"
first_df = spark.read.json(full_file_path)

# DataFrame vazio para armazenar todos os dados
all_data_df = spark.createDataFrame([], first_df.schema)

# Lendo todos os arquivos json da Raw Zone
for i in range(1, 6):
    file_path = f"desafios-etl/Raw/tmdb/json/2024/02/24/filmes__0{i}.json"
    full_file_path = f"s3://{file_path}"
    movies_json_df = spark.read.json(full_file_path)

    # Extraindo a data do caminho do arquivo
    date = "-".join(file_path.split("/")[4:7])

    # Adicionando a coluna 'dt' ao DataFrame
    movies_json_df = movies_json_df.withColumn("dt", lit(date))

    # Adicionando os dados ao DataFrame geral
    all_data_df = all_data_df.unionByName(movies_json_df, allowMissingColumns=True)

# Escrevendo os dados JSON transformados na Trusted Zone no formato PARQUET
all_data_df = all_data_df.persist()  # Adicione esta linha
all_data_df.write.partitionBy("dt").parquet(
    f"s3://desafios-etl/Trusted/"
)