import re

print(re.search(r'life', 'life is good').group())
print(re.search(r'is', 'life is good').group())

print(re.search(r'\d', '1 is one').group())
print(re.search(r'\d{4}', '1234 is one two three four'))