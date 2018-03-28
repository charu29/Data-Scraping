import requests
from bs4 import BeautifulSoup
import re
from bs4 import NavigableString


def crawler():
        url = 'https://innovate.mygov.in/sih2018-search'
        source_code = requests.get(url)
        text = source_code.text
        soup = BeautifulSoup(text, "html.parser")
        
        nos = []
        for div in soup.find_all(string=re.compile("Total Submissions")):
                txt = str(div)
                no = ""
                for i, c in enumerate(txt):
                        if i == 41 or i == 42 or i == 43:
                                no = no + c
                nos.append(int(no))

        href = []
        titles = []
        for div in soup.find_all("div", class_="title"):
                href.append(div.a.get('href'))
                titles.append(div.a.get_text())

        for i in range(len(titles)):
                if nos[i] < 10:
                     print(nos[i], ":" + titles[i] + ":" + href[i])
                

crawler()