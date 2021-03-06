# File Input and Output (with)
import os
path = os.getcwd()
os.chdir(path + '\\file')
path = os.getcwd()

with open('2.txt', 'w') as f:
    f.write('Hello')
    f.close()
with open('2.txt', 'r') as f:
    print(f.read())
    f.close()