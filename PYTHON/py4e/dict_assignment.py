name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
sender_dict = dict()
for line in handle:
    if 'From' not in line.split():
        continue
    #print(line.split()[1])
    sender_dict[line.split()[1]] = sender_dict.get(line.split()[1],0) + 1

maxcount = None
maxsender = None
for sender,count in sender_dict.items():
    if maxsender is None or maxcount < count:
        maxsender = sender
        maxcount = count
print(maxsender , maxcount)
