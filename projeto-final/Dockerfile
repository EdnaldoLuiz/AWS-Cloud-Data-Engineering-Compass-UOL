FROM python:3.9

COPY . .

WORKDIR /

RUN pip install boto3

CMD ["python", "./layers/upload_csv_s3.py"]