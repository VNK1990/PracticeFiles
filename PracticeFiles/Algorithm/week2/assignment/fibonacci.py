# Uses python3

def calc_fib_fast(n):
    curr_num = 1
    prev_num = 0

    if n <= 1:
        return n

    for _ in range(n-1):
        prev_num, curr_num = curr_num, prev_num + curr_num
    return curr_num


def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


n = int(input())
#print(calc_fib(n))
print(calc_fib_fast(n))
