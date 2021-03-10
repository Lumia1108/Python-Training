import os, csv
path = os.getcwd()
os.chdir(path+'\\csv')

def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(f)
    result = []
    for i in reader:
        result.append(i)
    f.close()
    return result

print(opencsv('a.csv'))