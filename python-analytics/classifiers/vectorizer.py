from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle
from pathlib import Path

path = Path('D:\DataAnalysis\DBT_Snowflake_SQL_Airflow_Integration\python-analytics')
stop = pickle.load(open(
		os.path.join(
				f'{path}\pkl_objects',
				'stopwords.pkl'
			), 'rb'
	))

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) \
                   + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
                         preprocessor=None,
                         tokenizer=tokenizer)