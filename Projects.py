import requests
from bs4 import BeautifulSoup


def crawler():
        url = 'https://innovate.mygov.in/sih2018-search'
        source_code = requests.get(url)
        text = source_code.text
        soup = BeautifulSoup(text, "html.parser")
		''' Prints names and links: '''
        for i in soup.findAll('div', {'class': 'head-part'}):
                tss=i.find('div', {'class':'desc-info'})
                h=i.div.string
                print(h)
                a=tss.get_text()
                a=str(a)
                print(a)
                b=a[172:175]
                print(b)
                b=int(b)
                print(b)
                '''  if(b<=100):
                   link = i.a.get('href')
                   title = i.a.string
                   print(title, link) '''
                
crawler()