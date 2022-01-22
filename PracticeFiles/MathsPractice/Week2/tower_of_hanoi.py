def hanoi(n,s,d,a):
    if n == 0 :
        return
    hanoi(n-1,s,a,d)
    print('Move the disk: ',n,'From ',s, d)
    hanoi(n-1,a,d,s)
if __name__ == '__main__':
    m = 6
    hanoi(m, 'A', 'C', 'B')
