from pathlib import Path
import re

path = Path('D:\DataAnalysis\DBT_Snowflake_SQL_Airflow_Integration\python-analytics')

# def test():
#     with open(f'{path}/movie.csv', 'r', encoding='utf8') as csv:
#         next(csv)
#         for line in csv:
#             label = int(line[-2])
#             yield label
           
# gen_object = test()

# print(type(gen_object))

# for i in gen_object:

#    print(i)

with open(f'{path}/movie.csv', 'r', encoding='utf-8') as text:
    for line in text:
        allemots = []
        emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', line.lower())
        if emoticons in text:
            allemots.append(emoticons)
            print(allemots)