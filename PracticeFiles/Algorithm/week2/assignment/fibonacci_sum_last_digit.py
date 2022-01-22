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


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    length = get_pattern_length(n, 10)
    print(length)
    if length != 0:
        new_num = n % length
    else:
        new_num = n

    if new_num <= 1:
        return new_num

    previous = 0
    current = 1
    _sum = 1
    for _ in range(new_num - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    _sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # print(fibonacci_sum_fast(n))

    for c in range(1666):
        print('---------====', c, '=====-----------')
        if fibonacci_sum_naive(c) != fibonacci_sum_fast(c):
            print('Naive : ', fibonacci_sum_naive(c))
            print('Pattern : ', fibonacci_sum_fast(c))

# print('Naive : ', fibonacci_sum_naive(61))
# print('Pattern : ', fibonacci_sum_fast(61))
