# File Input and Output
import os
path = os.getcwd()
os.chdir(path + '\\file')
path = os.getcwd()
#print(path)

f = open('1.txt', 'w')
f.write('abc')
f.close()
f = open('1.txt', 'r')
print(f.read())
f.close()

f = open('1.txt', 'a')
f.write('defg')
f.close()
f = open('1.txt', 'r')
print(f.read())
f.close()