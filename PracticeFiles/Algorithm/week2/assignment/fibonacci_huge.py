# Uses python3
import sys


def get_pattern_length(n, m):
    if n <= 1:
        return n
    v_count = 1
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        if previous % m == 0 and current % m == 1 and v_count > 2:
            v_count = v_count
            return v_count
        else:
            v_count += 1

    return 0


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    length = get_pattern_length(n, m)
    print(length)
    if length != 0:
        new_num = n % length
    else:
        new_num = n

    if new_num <= 1:
        return new_num
    previous = 0
    current = 1

    for _ in range(new_num - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


if __name__ == '__main__':
    input = input('Enter two num ')#sys.stdin.read();
    n, m = map(int, input.split())
    print('Slow : ', get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
