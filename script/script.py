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

f = codecs.open('monica.txt', 'w', encoding='utf-8')
f.write(monica)
f.close()


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

# 특정 단어의 예문만 모아 파일로 저장하기
## 대사만 모으기
f = codecs.open('friends101.txt', 'r', encoding='utf-8')
sentences = f.readlines()
script2 = []
for item in sentences:
    if re.match(r'[A-Z][a-z]+:', item):
        script2.append(item)
        print(item)

## would가 들어간 문장만 모으기
would = []
for i in script2:
    if re.search('would', i):
        would.append(i)
        print(i)

f = codecs.open('would.txt', 'w', encoding='utf-8')
f.writelines(would)
f.close()