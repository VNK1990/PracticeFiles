import urllib.request, urllib.parse, urllib.error
import json

uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1402762.json')

data = uh.read().decode()
js = json.loads(data)
ls = js['comments']
total = 0
for l in ls:
    total = total + int(l['count'])
print(total)
