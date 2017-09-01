#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup

ZhilianHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',\
                 }
ZhilianSearchValues = {'jl':'北京', 'kw':'Python', 'sm':'0', 'p':'1', 'source':'0'}
ZhilianSearchData = urllib.urlencode(ZhilianSearchValues)


ZhilianUrl = "http://sou.zhaopin.com/jobs/searchresult.ashx"
request = urllib2.Request(ZhilianUrl + '?' + ZhilianSearchData, headers = ZhilianHeader)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response, "lxml")
#print soup.name
#print soup.a
#for sibling in soup.
#print soup.body.find_all(name = 'frmMain')
for child in soup.body.children:
    print type(child)
    break

for child in soup.body.descendants:
    print type(child)
    if [] != child.find_all(class_ = 'newlist_main'):
        print child