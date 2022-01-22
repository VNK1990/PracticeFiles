def extend(fac, n):
    if n >= 1 :
        fac = fac * n
        n = n - 1
        extend(fac,n)
    else:
        print(fac)
        exit()
if  __name__ == "__main__":
    extend(fac = 1, n = 6)
