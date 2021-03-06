# File Input and Output (with codecs)

import os, codecs
path = os.getcwd()
os.chdir(path + '\\file')
path = os.getcwd()


f = codecs.open('한글.txt', 'w', 'utf-8')
f.write("안녕하십니까")
f.close()
f = codecs.open('한글.txt', 'r', 'utf-8')
print(f.read())
f.close()