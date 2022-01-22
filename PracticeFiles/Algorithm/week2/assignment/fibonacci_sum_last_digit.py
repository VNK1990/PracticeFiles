# Uses python3
import sys


def get_pattern_length(n, m):
    if n <= 1:
        return n
    v_count = 1
    previous = 0
    current = 1
    list1 = []
    for _ in range(n - 1):
        previous, current = current, previous + current
        if previous % m == 0 and current % m == 1 and v_count > 2:
            v_count = v_count

            print(list1)
            print(sum(list1))
            return v_count
        else:
            list1.append(current % m)
            v_count += 1

    return 0


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    _sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current
        print(current, _sum % 10)

    return _sum % 10


if __name__ == '__main__':
    #print(get_pattern_length(100, 10))
   # input = input('Enter Num: ')#sys.stdin.read()
    #n = int(input)
    for c in range(30):
       print('NUM: ', fibonacci_sum_naive(c))
