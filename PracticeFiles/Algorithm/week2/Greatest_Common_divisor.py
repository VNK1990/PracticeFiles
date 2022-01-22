# Slow Algorithm
def greatest_common_divisor_slow(a, b):
    greatest = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            greatest = i
    return greatest


def greatest_common_divisor_fast(a, b, c):
    if b != 0:
        remainder = a % b
        c = greatest_common_divisor_fast(b, remainder, c)
    if b != 0 and a % b == 0:
        return b

    return c


if __name__ == '__main__':
    print(greatest_common_divisor_slow(46464646, 2121))
    print(greatest_common_divisor_fast(46464646, 2121, 0))
