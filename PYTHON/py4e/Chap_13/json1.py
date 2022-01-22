import json

data = '''
[{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}]'''

info = json.loads(data)
print(type(info))
print(info)
print('Name:',info[0].get("name"))
print('Number:',info[0].get('phone').get('number'))
