import re

fh = open('regex_sum_1402757.txt')
total = 0;
for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) > 0:
        for val in y:
            total = total + int(val)
print(total)
