import requests as rq 

from bs4 import BeautifulSoup

import re

from bs4 import NavigableString

IMBurl= 'https://www.imdb.com/chart/top/'

qheader = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'
}

Iresponse = rq.get(url = IMBurl, headers=qheader)

bsoup = BeautifulSoup(Iresponse.content,'html.parser')

table = bsoup.find_all('div', attrs={'class':"ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 bnSrml cli-title"}) 

# print(table[0].find('a').find('h3').text)

def moviename(mn):
    return mn.find('a').find('h3').text

def movieyear(my):
    return my.nextSibling.find('span').getText()

def movierating(mr):
   return mr.find('span')
    

allmovies = [movierating(mr) for mr in table]

print(allmovies)





