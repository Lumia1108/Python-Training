import pandas as pd
import re, os
path = os.getcwd()
os.chdir(path + '\\pandas')
df = pd.read_csv('apt.csv', encoding='utf-8-sig')

# 면적이 130m^2이 넘는 것만 출력하기
print(df[df.면적 > 130])
print(df.가격[df.면적 > 130])

# 면적이 130m^2이 넘고 가격은 2억원 미만인 것만 출력하기
print(df['가격'][(df['면적']>130) & (df['가격']<20000)])

# 원하는 자료만 살펴보기
print(df.loc[:10, ['아파트', '가격']])
print(df.loc[:, ['아파트', '가격']][df.가격 > 40000])

# 새로운 값 추가하기
df['단가'] = df.가격 / df.면적
print(df.loc[:10, ('가격', '면적', '단가')])

# 데이터 정렬하기
print(df.sort_values(by = '가격').loc[:, ('가격', '지역')]) # 오름차순으로 정렬하기
print(df.sort_values(by = '가격', ascending = False).loc[:, ('가격', '지역')]) # 내림차순으로 정렬하기

print(df[df.가격 > 40000].sort_values(by = '가격').loc[:, ('가격', '면적', '지역')])

# 문자열 다루기
print(df.지역.str.find('강릉'))
print(df[df.지역.str.find('강릉') > -1])