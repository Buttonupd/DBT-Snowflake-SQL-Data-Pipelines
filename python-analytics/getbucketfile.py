# Google cloud sdk

import csv
from io import StringIO
from google.cloud import storage
from pathlib import Path
from decouple import config

path = Path('D:\DataAnalysis\DBT_Snowflake_SQL_Airflow_Integration\python-analytics')

def download_to_path():

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(config('bucket'))
    blob = bucket.blob(config('blob'))
    blob = blob.download_as_string()
    blob = blob.decode('utf-8')

    blob = StringIO(blob)
    names = csv.reader(blob)
    
    with open(f'{path}/movie.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([name for name in names])
        return
    
download_to_path()


