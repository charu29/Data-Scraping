import requests
from bs4 import BeautifulSoup


def crawler():
        url = 'https://innovate.mygov.in/sih2018-search'
        source_code = requests.get(url)
        text = source_code.text
        soup = BeautifulSoup(text, "html.parser")
        for i in soup.findAll('div', {'class': 'head-part'}):
                ts = i.next_sibling.div.get_text()
                link = i.div.a.get('href')
                title = i.div.a.string
                print(title, link)

crawler()