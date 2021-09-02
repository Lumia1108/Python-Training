alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
S = input().upper()
num = {}
for i in alphabet:
    num[i] = S.count(i)

answer = 'A'
duplication = False

for i in num:
    if (num[i] == num[answer]) and (i != answer):
        duplication = True
    if num[i] > num[answer]:
        answer = i
        duplication = False

if duplication:
    print('?')
else:
    print(answer)