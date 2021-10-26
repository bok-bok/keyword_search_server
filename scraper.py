import json
from bs4 import BeautifulSoup 
import requests
import re 
from urllib import parse


header_info = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


  

  

def get_links(keyword):
    
    url = f'https://search.hani.co.kr/Search?command=query&keyword={parse.quote(keyword)}&media=news&sort=d&period=month&pageseq=0'
    soup = urlToSoup(url)

    newsLink = [] 
    selectLinksFromSoup(soup, newsLink)
    
    return newsLink



def urlToSoup(url):
  req = requests.get(url, headers=header_info)
  body = req.text
  soup = BeautifulSoup(body, 'html.parser')
  return soup

def selectLinksFromSoup(soup, newsLink):
  
  titles = soup.select('ul.search-result-list a')[:5]
  for _title in titles:
      link = _title.get('href')
      if link[:5] != 'https':
          link = 'https:' + link
      newsLink.append(link)
  





def get_contents_from_links(links):
    contents = ' '.join(list(map(get_contents_from_link,links)))
    return contents


def get_contents_from_link(link):
    soup = urlToSoup(link)
    texts = selectTextsFromSoup(soup)
    print('link',link)
    return texts
    
def selectTextsFromSoup(soup):
  texts = soup.select('div.text')[0].get_text()
  texts = re.sub(r'\s+', ' ', texts)
  return texts

    
def get_contents_from_keyword(keyword = '중국'):
    links = get_links(keyword)
    contents = get_contents_from_links(links)
    return contents 




  
  






