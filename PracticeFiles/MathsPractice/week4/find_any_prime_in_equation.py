def is_prime_num(value):
    count = 0
    for i in range(2, value):
        if value % i == 0:
            print('Divided by :', i)
            return True
    return False


def get_equation(c):
    value = c * c + c + 41
    if is_prime_num(value):
        print(c, '      ', value)


if __name__ == '__main__':
    for j in range(1, 41):
        get_equation(j)
