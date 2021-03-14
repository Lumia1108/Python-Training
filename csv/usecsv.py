import csv, os, re
def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

def writecsv(filename, the_list):
    f = open(filename, 'w', encoding='utf-8-sig')
    writer = csv.writer(f, delimiter=',')
    writer.writerows(the_list)
    f.close()

# only 2*2 list
def switchtonum(the_list):
    for i in the_list:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return the_list