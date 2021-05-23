n = input()
cycle = 0
newn = n

while newn != n or cycle == 0:
    cycle += 1
    if newn == '0':
        break
    if len(newn) == 1:
        newn = '0' + newn
    newn = str(int(newn[-1] + str(int(newn[0]) + int(newn[1]))[-1]))
print(cycle)