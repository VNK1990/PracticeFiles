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


def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n

    length = get_pattern_length(n, 10)
    # print('Pattern : ', length)

    new_m = m
    new_n = n

    if length != 0:
        new_m = m % length
        new_n = n % length
    # print(new_m, new_n)
    if new_m > new_n:
        new_n = new_n + length
    # print(new_m, new_n)
    return fibonacci_partial_sum_naive(new_m, new_n)


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # print('Slow: ',fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
