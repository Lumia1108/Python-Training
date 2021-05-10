year = int(input())
if((year % 4) == 0 and not((year % 100) == 0)):
    print(1)
    exit()
if((year % 400) == 0):
    print(1)
    exit()
print(0)