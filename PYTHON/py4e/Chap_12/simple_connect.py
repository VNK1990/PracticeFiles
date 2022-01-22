import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
count = 1

def url_call(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    total = 0
    tags = soup('a')
    return tags

url = 'http://py4e-data.dr-chuck.net/known_by_Meledy.html'
for c in range(8):
    #print('------Count-------',c)
    count = 1
    print(url)
    tags = url_call(url)
    for tag in tags:
        if count == 18:
            url = tag.get('href', None)
            break
        count = count + 1
