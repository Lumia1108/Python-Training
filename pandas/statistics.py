import os, re
import pandas as pd

# 기초통계량 살펴보기
path = os.getcwd()
os.chdir(path + '\\pandas')
df = pd.read_csv('survey.csv')

print(df.head())

# 평균과 합 구하기
print(df.mean())
print(df.income.mean())
print(df.income.sum())

# 중앙값 구하기
print(df.income.median())

# 기초통계량 요약해서 출력하기
print(df.describe())
print(df.income.describe())

# 기초통계량 분석하기
## 빈도 분석하기
print(df.sex.value_counts())

## 두 집단 평균 구하기
print(df.groupby(df.sex).mean())