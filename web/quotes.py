import requests
from bs4 import BeautifulSoup as bs

count = 0
main_url = 'http://quotes.toscrape.com'

def quote(url):
    global count
    global main_url
    if url[0:4] != 'http':
        url = main_url + url

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    data = soup.find_all('div', {'class': 'quote'})
    for i, value in enumerate(data):
        count += 1
        print(count, '번째')
        saying = value.span.text
        print(saying)
    next_page = soup.find('li', {'class': 'next'})
    if next_page != None:
        quote(next_page.a.get('href'))

quote(main_url)