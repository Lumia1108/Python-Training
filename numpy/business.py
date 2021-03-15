import numpy as np
import numpy_financial as npf


# 자본의 현재 가치 구하기
discount = 0.05
cashflow = 100

def presentvalue(n):
    return (cashflow / ((1 + discount) ** n))

## 20년 동안 발생할 현재 가치
for i in range(20):
    print(presentvalue(i))

# 놀이공원 사업의 사업성 분석하기
# 1, 2년 차에 발생한 비용입니다.
loss = [-750, -250]
# 3년차부터 발생한 이익입니다.
profit = [100] * 18
# 총 20년 동안의 현금 흐름을 리스트로 cf에 저장합니다.
cf = loss + profit
cashflow = np.array(cf)

# 순현재가치(NPV)와 내부수익률(IRR) 구하기
npv = npf.npv(0.045, cashflow)
irr = npf.irr(cashflow)

print(npv)
print(irr)