
def gcd(a, b):
    if b <= 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(a=5535, b=15534535))

