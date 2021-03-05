price = [23, 40, 67]
def service_price():
    service = input("서비스 종류를 입력하세요, a/b/c: ")
    result = 0
    if service == 'a':
        result = price[0]
    elif service == 'b':
        result = price[1]
    elif service == 'c':
        result = price[2]
    else:
        print("값을 제대로 입력해주세요.")
        service_price()
        return False
    valueAdded = input("부가세를 포함합니까? y/n: ")
    if valueAdded == 'y':
        result *= 1.1
    
    print(result)

service_price()
