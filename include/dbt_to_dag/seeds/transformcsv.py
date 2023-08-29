import csv
from pathlib import Path as path

pathToWrite = ('Path')
pathToRead = ('Path')

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
        