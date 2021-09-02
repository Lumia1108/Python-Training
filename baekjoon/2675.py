T = int(input())

for i in range(T):
    RS = input().split()
    R = int(RS[0])
    S = RS[1]
    P = ''
    for i in S:
        P += (i * R)
    print(P)