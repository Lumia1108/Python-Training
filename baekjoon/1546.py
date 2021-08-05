N = int(input())
gradeReal = list(map(int, input().split()))
M = max(gradeReal)
gradeNew = 0
for i in gradeReal:
    gradeNew += (i / M * 100)

print(gradeNew / N)