import requests
from bs4 import BeautifulSoup


def trade_spider (max_page):
    page = 1
    linksDell = open('links.txt', 'w')
    while page <= max_page :
        url = 'http://sp.olx.com.br/?o=' + str(page) + '&q=notebook'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        # prints the link  of the product
        for link in soup.findAll('a', {'class': 'OLXad-list-link'}) :
            title = link.get('title')
            href = link.get('href')
            if (str(title)).lower().find('dell') != -1:
                linksDell.write(title + ' ' + href + '\n')
                print(title + '\n')
        page += 10

trade_spider(1)

