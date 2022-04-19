import math
def guess_a_num(nlist, count, qs):

    if count == qs :
        print(nlist)
        exit()

    print("Number is : ", nlist[math.ceil(len(nlist)/2)-1])
    action = input("Enter Range: ")
    if action == 'L':
        nlist = nlist[0:math.ceil(len(nlist)/2)-1]
        #print('count: ',count,' List: ', nlist)
        count = count + 1
        guess_a_num(nlist, count, qs)
    elif action == 'U':
        nlist = nlist[math.ceil(len(nlist) / 2):len(nlist)]
        #print('count: ', count, ' List: ', nlist)
        count = count + 1
        guess_a_num(nlist, count, qs)


if __name__ == '__main__':
    num_list = []
    for c in range(1,127):
        num_list.append(c)
    guess_a_num(num_list, count = 1, qs = 7)