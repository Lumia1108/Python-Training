N = int(input())
arr = []

for i in range(N):
    arr.append(input())
score = []
for i, value in enumerate(arr):
    score.append(0)
    continuous = 1
    for j in value:
        if j == 'O':
            score[i] += continuous
            continuous += 1
        else:
            continuous = 1

for i in score:
    print(i)