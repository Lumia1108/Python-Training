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

from scipy import stats

male = df.income[df.sex == 'm']
female = df.income[df.sex == 'f']

ttest_result = stats.ttest_ind(male, female)

if ttest_result[1] > 0.05:
    print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
else:
    print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])