fh = open('mbox-short.txt')
count = 0;
for line in fh:
    if 'From' not in line.split():
        continue
    print(line.rstrip().split()[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
