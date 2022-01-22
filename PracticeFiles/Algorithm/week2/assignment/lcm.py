# Uses python3
import sys

def get_gcd(a, b):
    if b <= 0:
        return a
    else:
        return get_gcd(b, a % b)


def lcm_fast(a, b):
    return int((a * b) / get_gcd(a, b))


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))
