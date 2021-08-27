nlist = []
for i in range(10000+1):
    nlist.append(True)
i = 1
j = 0
def d(n):
    ns = str(n)
    result = n
    for i in ns:
        result += int(i)
    return result

while i <= 10000:
    if nlist[i] == True:
        j = d(i)
        while j <= 10000:
            nlist[j] = False
            j = d(j)
    i += 1

k = 1
while k <= 10000:
    if nlist[k]:
        print(k)
    k += 1