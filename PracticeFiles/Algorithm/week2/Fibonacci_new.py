# slow
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# fast
def fibonacci_fast(n):
    num_list = []
    for num in range(0, n):
        if num <= 1:
            num_list.append(num)
        else:
            num_list.append(num_list[num-1] + num_list[num-2])
    return num_list


if __name__ == '__main__':
    print('Slow: ', fibonacci(n=15))
    print('Fast: ', fibonacci_fast(n=15))
