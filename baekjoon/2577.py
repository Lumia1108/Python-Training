A = int(input())
B = int(input())
C = int(input())
product = str(A * B * C)
arr = []
for i in range(10):
    arr.append(0)

for i in product:
    arr[int(i)] += 1

for i in arr:
    print(i)