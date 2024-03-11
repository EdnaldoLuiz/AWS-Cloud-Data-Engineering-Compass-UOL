import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import lit, col, lower, regexp_replace
from pyspark.ml.feature import Imputer
from pyspark.sql.types import IntegerType, FloatType

# Inicializando o GlueContext e a sessão Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Caminho de entrada e saída
input_path = "s3://desafios-etl/Raw/Local/CSV/Movies/2024/02/17/movies.csv"
output_path = "s3://desafios-etl/Trusted"

# Lendo os dados CSV da Raw Zone
movies_csv_df = (
    spark.read.format("csv")
    .option("header", "true")
    .option("delimiter", "|")
    .option("mode", 'PERMISSIVE')
    .load(input_path)
)

# Limpeza dos dados
movies_csv_df = movies_csv_df.dropDuplicates()
movies_csv_df = movies_csv_df.na.drop()

# Converter colunas para o tipo correto
movies_csv_df = movies_csv_df.withColumn("anoLancamento", col("anoLancamento").cast(IntegerType()))
movies_csv_df = movies_csv_df.withColumn("tempoMinutos", col("tempoMinutos").cast(IntegerType()))
movies_csv_df = movies_csv_df.withColumn("notaMedia", col("notaMedia").cast(FloatType()))
movies_csv_df = movies_csv_df.withColumn("numeroVotos", col("numeroVotos").cast(IntegerType()))

# Remover caracteres especiais e converter para minúsculas
movies_csv_df = movies_csv_df.withColumn("tituloPincipal", lower(regexp_replace(col("tituloPincipal"), "[^a-zA-Z0-9\s]", "")))
movies_csv_df = movies_csv_df.withColumn("tituloOriginal", lower(regexp_replace(col("tituloOriginal"), "[^a-zA-Z0-9\s]", "")))

# Escrevendo os dados CSV transformados na Trusted Zone no formato PARQUET
movies_csv_df.write.parquet(output_path)