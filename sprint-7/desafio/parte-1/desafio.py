import boto3
import os
from datetime import datetime

def get_s3_client(aws_access_key_id, aws_secret_access_key, aws_session_token):
    return boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
    )

def get_s3_destination_path(raw_zone, local_data, data_format, data_specification, source_file_name):
    data_processing_date = datetime.now().strftime("%Y/%m/%d")
    return f"{raw_zone}/{local_data}/{data_format}/{data_specification}/{data_processing_date}/{source_file_name}"

def upload_file_to_s3(s3, local_file_path, bucket_name, s3_destination_path):
    s3.upload_file(local_file_path, bucket_name, s3_destination_path)

if __name__ == "__main__":
    aws_access_key_id="ASIAWTDBM3C7R73O4DRL"
    aws_secret_access_key="aB8LgXC0rGm3LIW8kdUqHmZKKCIZpeSVhV4WSmvR"
    aws_session_token="IQoJb3JpZ2luX2VjEAAaCXVzLWVhc3QtMSJHMEUCICwH4iXRxroCRGbfWTfYz0SH1OsiOmXabPlwHq6zw32bAiEA9iGWPuwJgYfaTka0nVN1sU3X7bR4ONz6++gWVsdYhkYqpgMI2P//////////ARAAGgw0NTMzMjMzMTUzOTEiDMlyaFJyTLF8H6u7Jyr6AvH6YPlJYWDg8kAaATr0BaqUOnWXEiMMdIYfisyJpZ6GgpLj/HTmhDu5Bo3Ri4ha07g+taIBJDYAoiTP3oNQE1EFOy7WHjAyvYLgRQl6qXoT2zp1G4PQ8TyNW+v7babRvYw9n5V1V1NAtPFWnm3jc8EeduV2JudM/DWWgNphdZwWnyr/KKg5sam3JX53y2L7U+3QmRFztKscXMKbmGjRGQxuW8dSdI/mFLUeG3NTODgoqDQbUpzyX2LbwUkItJpavWM7Um2u9h+5auFC6gG/iPAmzG+er/TSZYbbuBHUhsSApAP9lDOP/aPuptn6JxwDEC9T8pecchYogdVQ8j8PRZ0HgPuxrNfwAFTzj/Dw78qr4iDyez+sNoSlq0qgZvuzjeu8iIvf1jWc/lQf1dTBKBi9rXrvjPEK+XVTkgMGmrI040koVfjL/mDhyu06esXmkvYqqRXXoVtM74FseUcgE9vJuQvtJfZASPm6LR85dDylYDS5tsx+Js/LwDCCnMOuBjqmAcIWizIK1fb07Zfax/DkMJ/rjDzuNThsEVQrthSO4zxdAIbN2EE1laJ0y+fJAUCAzN9rTVSbw8dxapikNAhV+3YVw/Qbf06XLCuGK10+TevunVIfVSmdrrDdQ7XRwRgM69ykza5QSB/IyVzZfxnA3J23oLTPTzc3wYN27XVE+IFmct5QJktmlT2ZGu53xfVFlrAwP22d90jG2vrpIXucXQk5+JTFfnE="
    bucket_name="desafios-etl"
    raw_zone="Raw"
    local_data="Local"
    data_format="CSV"

    s3 = get_s3_client(aws_access_key_id, aws_secret_access_key, aws_session_token)

    upload_data = [
        {"data_specification": "Series", "source_file_name": "series.csv", "local_file_path": "series.csv"},
        {"data_specification": "Movies", "source_file_name": "movies.csv", "local_file_path": "movies.csv"}
    ]

    for data in upload_data:
        s3_destination_path = get_s3_destination_path(raw_zone, local_data, data_format, data["data_specification"], data["source_file_name"])
        upload_file_to_s3(s3, data["local_file_path"], bucket_name, s3_destination_path)

    print("Os arquivos foram carregados para o S3 com sucesso.")