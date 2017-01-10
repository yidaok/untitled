import requests
from bs4 import BeautifulSoup

url = "http://weibo.com/p/1008084b518bb3f640edbe038bff149451836c/emceercd?from=page_huati_rcd_more"
data = {
    "cookie":""
}

#Pl_Third_App__45 > div > div > div.WB_feed.WB_feed_v3.WB_feed_v4 > div:nth-child(1) > div.WB_feed_detail.clearfix > div.WB_detail > div.WB_text.W_f14 > a:nth-child(2)