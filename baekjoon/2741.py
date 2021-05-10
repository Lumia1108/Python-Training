import sys
N = int(input())
for i in range(N):
    sys.stdout.writelines(str(i + 1))
    sys.stdout.writelines('\n')