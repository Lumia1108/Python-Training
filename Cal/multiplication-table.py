# 9*9 multiplication table
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = ""
for num in numbers:
    for i in numbers:
        result += "%d " % (num * i)
    result += "\n"

print(result)