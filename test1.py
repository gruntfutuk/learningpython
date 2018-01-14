# from urllib.request import urlopen
import urllib2
from bs4 import BeautifulSoup
import re
article="Kevin_Bacon"
url="http://en.wikipedia.org/wiki/"+article
#html=urlopen(url)
html=urllib2.urlopen(url)
soup=BeautifulSoup(html,"html.parser")
for all in soup.findAll("a"):
    if 'href' in all.attrs:
        l=all.attrs['href']
        print(l)
