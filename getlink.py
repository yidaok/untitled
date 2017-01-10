
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import requests
from bs4 import BeautifulSoup
import codecs
import re

url='https://www.douban.com/note/168932131/'
html=requests.get(url).content
links=re.findall(r'href=["\'](%s.*?)["\']',html)
table=[]
for i in links:
    table.append(i)
fb=codecs.open('get','wb',encoding='utf-8')
fb.write('{movie}\n'.format(movie='\n'.join(table)))
fb.close()
