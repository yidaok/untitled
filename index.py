import requests
import re

url='http://www.qiushibaike.com/'
r=requests.get(url=url)
html=r.content
