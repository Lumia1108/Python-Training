import os, csv, re
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


data = opencsv('seoul.csv')
k = []

for item in data:
    k.append([])
    for i in item:
        try:
            k[data.index(item)].append(float(re.sub(',', '', i)))
        except:
            k[data.index(item)].append(i)

print(k)