def isHan(n):
    if n < 100:
        return True
    if n == 1000:
        return False
    n = str(n)
    if (int(n[0]) + int(n[2])) == (int(n[1]) * 2):
        return True
    
    return False

N = int(input())
count = 0

for i in range(1, N+1):
    if isHan(i):
        count += 1

print(count)