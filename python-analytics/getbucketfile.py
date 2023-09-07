import csv
from io import StringIO
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('daniel_online_retail')
blob = bucket.blob('raw/imdb.csv')
blob.download_as_string()
blob.decode('utf8')

blob = StringIO(blob)
names = csv.reader(blob)
for name in names:
    print(f'Review {name[0]}')

    
