time = input().split()
hour = int(time[0])
minute = int(time[1])
if(minute>=45):
    minute -= 45
    print(hour, minute)
else:
    if(hour > 0):
        hour -= 1
        #minute = 60 - (45 - minute)
        minute += 15
        print(hour, minute)
    else:
        hour = 23
        minute += 15
        print(hour, minute)