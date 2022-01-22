import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

xml = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1402761.xml')
out = ''
for line in xml:
    #if out is None:
        #out = line.decode().strip()
        out = out + line.decode().strip()
#print(out)
tree = ET.fromstring(out)

lst = tree.findall('comments/comment')
#print('User count:', len(lst))
total = 0
for item in lst :
    total = total + int(item.find('count').text)
print(total)
