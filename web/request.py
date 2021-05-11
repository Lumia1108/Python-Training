import requests as r

# GET
url = 'https://www.brookings.edu/search/'
html = r.get(url, params={'key1': 'value1', 'key2': 'value2'})
print(html.url)

# POST
url = 'http://benhong.cafe24.com/php/api/Post.php'
html = r.post(url, data={'name': 'hahaha'})
print(html.url)
print(html.text)