# Very Slow Algo
def get_fib_num(n):
    if n <= 1:
        return n
    else:
        return get_fib_num(n-1) + get_fib_num(n-2)


# Vey Fast
def get_fib_num_fast(n):
    list1 = []
    if 1 <= n:
        list1.append(0)
    if 2 <= n:
        list1.append(1)
    if n > 2:
        for i in range(2, n):
            list1.append(list1[i-1] + list1[i-2])
    return list1


if __name__ == '__main__':
    print('test')
    print(get_fib_num(15))
    print(get_fib_num_fast(15))
