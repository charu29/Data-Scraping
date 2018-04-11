import requests
from bs4 import BeautifulSoup
import re
from bs4 import NavigableString

def ProjectSelector():
    url = 'https://innovate.mygov.in/sih2018-search/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    nos =[]
    for div in soup.find_all(string = re.compile("Total Submissions")):

       txt = str(div)
       no=""
       for i,c in enumerate(txt):
           if i==41 or i==42 or i==43:
                no = no + c
       nos.append(int(no))
    print(nos)

    href = []
    titles = []
    for div in soup.find_all("div", class_="title"):
        href.append(div.a.get('href'))
        titles.append(div.a.get_text())

    for i in range(len(titles)):
        if(nos[i]<10):
            print(nos[i],":"+titles[i]+":"+href[i])

#def surrounded_by_strings(tag):
#    return (isinstance(tag.next_element, NavigableString))
ProjectSelector()