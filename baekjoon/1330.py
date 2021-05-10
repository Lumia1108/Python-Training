num = input()
nums = num.split()
A = int(nums[0])
B = int(nums[1])
if(A > B):
    print('>')
    exit()
if(A < B):
    print('<')
    exit()
if(A == B):
    print('==')
    exit()