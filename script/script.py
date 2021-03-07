import os, re, codecs

path = os.getcwd()
os.chdir(path+'\\script')

f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
f.close()

# 특정 인물의 대사만 모으기
Line = re.findall(r'Monica:.+', script101)
monica = ""

for item in Line:
    print(item)
    monica += (item + '\n')
'''
f = codecs.open('monica.txt', 'w', encoding='utf-8')
f.write(monica)
f.close()
'''

# 등장인물 리스트 만들기
characters = re.findall(r'[A-Z][a-z]+:', script101)
characters = set(characters)
characters2 = []
for item in characters:
    result = re.sub(':', '', item)
    characters2.append(result)

# 지문만 출력하기
script = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)
for item in script:
    print(item)

