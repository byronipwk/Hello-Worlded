# -*- coding: utf-8 -*-
from urllib.parse import urljoin
import requests

pages = requests.get('http://www.macaodaily.com/html/2019-09/16/node_3.htm')


#取得所有版面的相對url
page_link_list = pages.xpath('//div[2]//a[contains(@id,"pageLink")]').re('node_[0-9]{2}.htm')

#生成所有版面的絕對url
for page_link in page_link_list:
    new_page_link = urljoin('http://www.macaodaily.com/html/2019-09/16/', page_link)
    new_page_links_list = new_page_links_list.add(new_page_link)

#取得一版所有報道的相對url
news_list = response.xpath('//div[2]//a[contains(@href,"content")]').re('content_[0-9]{7}.htm')

#生成所有報道的絕對url
for news_link in news_list:
    new_news_link = urljoin('http://www.macaodaily.com/html/2019-09/16/', news_link)
    new_news_link_list = new_news_link_list.add(new_news_link)
