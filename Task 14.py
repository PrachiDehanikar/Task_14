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

def moviename(mr):
    return mr.find('a').find('h3').text

def movieyear(mr):
    movieyr_spans = mr.nextSibling.find_all('span')[0:2] 
    return[span.get_text() for span in movieyr_spans]

def movierating(mr):
   rating_div = mr.find_all('div',attrs ={'class' :"sc-e2dbc1a3-0 jeHPdh sc-b189961a-2 bglYHz cli-ratings-container"})
   if rating_div:
        spans = rating_div.find_all('span')
        return [span.get_text() for span in spans]  
   else:
        return []

# allmovies = [(movierating(mr),moviename(mr),movieyear(mr)) for mr in table]

# print(allmovies)


allmovies = []
for mr in table:
    rating = movierating(mr)
    name = moviename(mr)
    year, runtime = movieyear(mr)
    allmovies.append((rating, name, year, runtime))

for movie in allmovies:
    print(f"Rating: {movie[0]}, Name: {movie[1]}, Year: {movie[2]}, Runtime: {movie[3]}")





