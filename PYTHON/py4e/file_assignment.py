fh = open(input("Enter a file name: "))
count = 0;
total = 0;
for lines in fh:
    if not lines.startswith('X-DSPAM-Confidence:') :
        continue
    count = count + 1
    total = total + float(lines[lines.find(': ')+2:len(lines)].rstrip())
print('Average spam confidence:', total / count)
