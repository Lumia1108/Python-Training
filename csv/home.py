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

def strtonum(item):
    for i in item:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return item

apt = strtonum(opencsv('home_price.csv'))
writecsv('home_price.csv', apt)

# 시군구 단지명 거래금액(만원) 출력
for i in apt[:6]:
    print(i[0], i[4], i[-5])

apt_list = []
#강원도에 120m^2 이상 3억원 이하 아파트 검색하기
for i in apt:
    try:
        if re.match('강원', i[0]) and i[5] >= 120 and i[-5] < 30000:
            print(i[0], i[4], i[-5])
            apt_list.append([i[0], i[4], i[-5]])
    except:
        pass

writecsv('apt_list.csv', apt_list)