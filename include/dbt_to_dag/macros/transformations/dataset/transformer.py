import csv
from pathlib import Path as path
import pandas as pd

pathToRead = ('D:/DataAnalysis/DBT_Snowflake_SQL_Airflow_Integration/include/dbt_to_dag/macros/transformations/dataset')
pathToWrite = ('D:/DataAnalysis/DBT_Snowflake_SQL_Airflow_Integration/include/dbt_to_dag/seeds')


# Read the CSV file
df = pd.read_csv(f'{pathToRead}/IMDB_dataset.csv')

# Trim the 'sentiment' column to <= 8000 characters
df['review'] = df['review'].str[:7900]

# Save the modified data to a new CSV file
df.to_csv(f'{pathToWrite}/imdb.csv', index=False)
        