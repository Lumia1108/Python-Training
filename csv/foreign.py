# 외국인 비율 계산해서 파일로 저장
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
def writecsv(filename, obj):
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    csvobject = csv.writer(f, delimiter=',')
    csvobject.writerows(obj)
    f.close()


data = opencsv('seoul.csv')
k = []
for item in data:
    k.append([])
    for i in item:
        try:
            k[data.index(item)].append(float(re.sub(',', '', i)))
        except:
            k[data.index(item)].append(i)
new = [['구', '전체', '내국인', '외국인', '외국인 비율(%)']]
for i in k:
    foreign = 0
    try:
        foreign = round((i[3] / i[1]) * 100, 1)
        i.append(foreign)
        print(i[0], foreign)
        new.append(i)
    except:
        pass
print(new)
writecsv('seoul3.csv', new)