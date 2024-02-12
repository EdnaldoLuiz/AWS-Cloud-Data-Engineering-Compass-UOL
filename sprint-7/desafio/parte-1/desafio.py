import boto3
import os
from datetime import datetime

def upload_file_to_s3(
    aws_access_key_id,
    aws_secret_access_key,
    bucket_name,
    raw_zone,
    local_data,
    data_format,
    data_specification,
    source_file_name,
    local_file_path,
):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    data_processing_date = datetime.now().strftime("%Y/%m/%d")

    s3_destination_path = f"{bucket_name}/{raw_zone}/{local_data}/{data_format}/{data_specification}/{data_processing_date}/{source_file_name}"

    s3.upload_file(local_file_path, bucket_name, s3_destination_path)

if __name__ == "__main__":
    upload_file_to_s3(
        aws_access_key_id="AKIAWTDBM3C7SP5BWREY",
        aws_secret_access_key="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",
        bucket_name="desafios-etl",
        raw_zone="Raw",
        local_data="Local",
        data_format="CSV",
        data_specification="Series",
        source_file_name="series.csv",
        local_file_path="csv/series.csv",
    )

    upload_file_to_s3(
        aws_access_key_id="AKIAWTDBM3C7SP5BWREY",
        aws_secret_access_key="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",
        bucket_name="desafios-etl",
        raw_zone="Raw",
        local_data="Local",
        data_format="CSV",
        data_specification="Movies",
        source_file_name="movies.csv",
        local_file_path="csv/movies.csv",
    )

    print("Os arquivos foram carregados para o S3 com sucesso.")
