from bs4 import BeautifulSoup
import requests

r=requests.get(url='http://huaban.com/')
note=r.content
soup=BeautifulSoup(note)
title=soup.find_all('a')
