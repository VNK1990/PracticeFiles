fh = open('romeo.txt')#open(input('Enter File Name: '))
final_list = list()
for line in fh:
    #print(line.rstrip())
    for char in line.split():
        if char in final_list:
            continue
        final_list.append(char);
final_list.sort()
print(final_list)
