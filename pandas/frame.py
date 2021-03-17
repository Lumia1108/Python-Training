import pandas as pd
data = {
    'name': ['Mark', 'Jane', 'Chris', 'Ryan'],
    'age': [33, 32, 44, 42],
    'score': [91.3, 83.4, 77.5, 87.7]
}

df = pd.DataFrame(data)
print(df)

# 판다스 데이터프레임 간단한 연산 연습
print(df.sum())
print(df.mean())

# 데이터 선택하기
print(df.age)

