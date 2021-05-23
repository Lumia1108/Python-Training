while True:
    n =  input()
    if n != '0 0':
        a, b = map(int, n.split())
        print(a+b)
    else:
        break