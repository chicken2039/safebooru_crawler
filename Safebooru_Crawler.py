import requests
import re
from bs4 import BeautifulSoup
import urllib.request


def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://safebooru.org/index.php?page=post&s=list&tags=hibiki_%28kantai_collection%29&pid=' + str(
            (page - 1) * 40)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        href = "http://safebooru.org/index.php?page=post&s=list&tags=hibiki_%28kantai_collection%29&pid=" + str(
            (page - 1) * 40)
        print (href)
        for link in soup.findAll(id=re.compile('s\d+')):
            pic = link.a['href']
            url_pic = "http://safebooru.org/" + pic
            print (url_pic)

            source_code_pic = requests.get(url_pic)
            pic_text = source_code_pic.text
            pic_soup = BeautifulSoup(pic_text, 'lxml')
            for pic_soup_2 in pic_soup.findAll(href=re.compile('\/\/safebooru.org\/\/images\/\d+\/\w+.(png|jpg|jpeg)')):
                pic_2 = 'http:'+pic_soup_2['href']
                name=pic_2[-25:]
                urllib.request.urlretrieve(pic_2,name)

        page += 1

spider(2)