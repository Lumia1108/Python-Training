import numpy as np
a = np.array([[2, 3], [5, 2]])

# 배열 원소 값 출력
print(a[1][0])

# 배열 크기 알아내기
b = np.array([2, 3, 4, 5, 6])
print(b.shape)
c = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(c.shape)
d = np.array([[[1, 2], [2, 3]], [[3, 4], [4, 5]]])
print(d.shape)

# 배열의 원소 유형 확인하기
print(d.dtype)

# 배열 유형 바꾸기
data = np.array([2, 3])
print(data.dtype) #int32
data = data.astype('float64')
print(data.dtype) # float64

# 넘파이의 다양한 함수 사용해보기
## 0으로 이뤄진 배열 만들기
data2 = np.zeros((2, 10))
print(data2)
## 1로 이뤄진 배열 만들기
data3 = np.ones((2, 10))
print(data3)
## 연속형 정수 생성하기
data4 = np.arange(2, 10)
print(data4)
## 행과 열을 바꾸기
data5 = np.ones((2, 3))
print(data5)
print(np.transpose(data5))

# 배열의 사칙 연산
arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])
## 배열의 덧셈
print(arr1 + arr2)
## 배열의 뺄셈
print(arr2 - arr1)
## 배열의 곱셈
print(arr1 * arr2)
## 배열의 나눗셈
print(arr1 / arr2)

# 크기가 서로 다른 배열끼리 더하기
arr3 = np.array([100, 200, 300])
print(arr1 + arr3)
arr4 = np.array([[9], [3]])
print(arr1 + arr4)

# 인덱싱과 슬라이싱 연습하기
arr5 = np.arange(10)
print(arr5[:5])
print(arr5[:-3])
print(arr1[1, 2])
print(arr1[:, 2])