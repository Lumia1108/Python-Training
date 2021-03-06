import re

#pattern = r'life'
#script = 'life'

#print(re.match(pattern, script))
#print(re.match(pattern, script).group())

def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')

refinder(r'life', 'life is good')
refinder(r'life', 'Hello, World!')
refinder(r'is', 'life is good')