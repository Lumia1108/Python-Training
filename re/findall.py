import re

#print(re.findall(r'\d', '1234 is one two three four'))

def getYearFromText(txt):
    result = re.findall(r'\d+?년', txt)
    return result

text = "2002년에 태어났습니다. 2002년에는 월드컵이 있었습니다. 지금은 2021년입니다."

print(getYearFromText(text))