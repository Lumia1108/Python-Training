n = int(input())
arr = input().split()
for i, value in enumerate(arr):
    arr[i] = int(value)
print(min(arr[:n]), max(arr[:n]))