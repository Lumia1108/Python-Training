import requests

# Download image file
url = 'https://www.hanyang.ac.kr/html-repositories/images/custom/introduction/img_hy0104_0301.jpg'
data = requests.get(url).content
with open('hanyang.jpg', 'wb') as f:
    f.write(data)
    f.close()