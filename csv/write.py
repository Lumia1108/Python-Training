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

def writecsv(filename, obj):
    f = open(filename, 'w', encoding='utf-8', newline='')
    csvobject = csv.writer(f, delimiter=',')
    csvobject.writerows(obj)
    f.close()

a = [['구','전체','내국인','외국인'],
['관악구',519864,502089,17775],
['강남구',547602,542498,5104],
['송파구',686181,679247,6934],
['강동구',428547,424235,4312]]
writecsv('seoul.csv', a)