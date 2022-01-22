#Exit Procedure
def is_exit(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1 or arr[i][j] == 2:
                count = count + 1
    if count == 6:
        return True
    return False

#Check Condition
def check_condition(arr,r,c):
    if not r - 1 < 0:
        print('First row then no bottom checks required')
        if arr[r][c] == arr[r-1][c]:
            return True

    if not c - 1 < 0:
        print('First column then no left checks required')
    if not r + 1 > len(arr):
        print('Last Row then no top check required')
    if not c + 1 > len(arr):
        print('Last column then no right check required')
    #left check
    #right check
    #top check
    #bottom check
    #left-bottom diagonal check
    #left-top diagonal check
    #right-top diagonal check
    #right-bottom diagonal check

    return False

#Extend
def extend(arr,n):
    #Exit Condition
    if is_exit(arr):
        print(arr)
        exit()
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j])

if __name__ == '__main__':
    perm = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    extend(perm , n = 9)
