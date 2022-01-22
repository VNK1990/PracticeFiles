name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dict_hr = dict()
for line in handle:
    if not 'From' in line.split():
        continue
    hr = line.rstrip().split()[5].split(':')[0]
    dict_hr[hr] = dict_hr.get(hr,0) + 1

list_hr = list()
for k,v in dict_hr.items():
    tuple_hr = (k,v)
    list_hr.append(tuple_hr)
sorted_list = sorted(list_hr,reverse = False)

for k , v in sorted_list:
    print(k,v)
