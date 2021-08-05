C = int(input())
grades = []
for i in range(C):
    grades.append(list(map(int, input().split())))

for i in grades:
    average = sum(i[1:]) / i[0]
    ratio = 0
    for j in i[1:]:
        if j > average:
            ratio += 1
    print(('%.3f' % (round((ratio / i[0]) * 100, 3))) + '%')