import matplotlib.pyplot as plt
x = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x) #기본형
plt.show()
plt.plot(x, color='r') # 색 변경
plt.show()
plt.plot(x, 'or') # 그래프 모양 점선으로 바꾸기
plt.show()

# 그래프 이름과 그래프 축 정하기
y = list(range(1, 9))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib practice')
plt.show()
