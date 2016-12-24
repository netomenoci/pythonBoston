import requests
from bs4 import BeautifulSoup


def trade_spider (max_page):
    page = 1
    while page <= max_page :
        url = 'http://sp.olx.com.br/?o=' + str(page) + '&q=notebook'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'OLXad-list-link'}) :
            href = link.get('href')
            print(href)
        page += 1

trade_spider(1)

