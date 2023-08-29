import csv
from pathlib import Path as path

pathToWrite = ('D:/DataAnalysis/DBT_Snowflake_SQL_Airflow_Integration/include/dbt_to_dag/seeds/')
pathToRead = ('D:/DataAnalysis/DBT_Snowflake_SQL_Airflow_Integration/include/dbt_to_dag/seeds/dataset')

with open(f'{pathToRead}/transactions.csv', 'r', encoding="utf8") as inf, open(f'{pathToWrite}/transformed.csv', 'w',encoding="utf8") as of:

    r = csv.reader(inf, delimiter=',')
    w = csv.writer(of, delimiter=',')

    for line in inf:
        of.write(','.join(list(map(str.strip, line.split(',')))) + '\n')
    # for line in r:
    #     for l in line:
    #         line = line[:8000:]
    #         trim = (field.strip(" ") for field in line)
    #         w.writerow(trim)
        


# st = "abcdefghijklmnopqrstuvwxyz"
# print(st[:3:])
        