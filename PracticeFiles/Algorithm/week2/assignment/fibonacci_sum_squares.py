# Uses python3
from sys import stdin


def calc_fib_fast(n):
    curr_num = 1
    prev_num = 0

    if n <= 1:
        return n

    for _ in range(n - 1):
        prev_num, curr_num = curr_num, prev_num + curr_num
    return curr_num % 10


def fibonacci_sum_squares_fast(n):
    f_n = calc_fib_fast(n % 60)
    f_n_1 = calc_fib_fast((n + 1) % 60)
    return (f_n * f_n_1) % 10


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


if __name__ == '__main__':
    # n = int(input('Enter num: '))
    n = int(stdin.read())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares_fast(n))
