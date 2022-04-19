# Uses python3
import sys


def get_change_optimal(m, list1):
    cnt = 0
    if m == 0:
        return cnt
    else:
        a = max(list1)
        if len(list1) != 0 and m >= a:
            cnt = m // a
            m -= ((m // a) * a)
            list1.remove(a)
        else:
            list1.remove(a)

        cnt += get_change_optimal(m, list1)
    return cnt


def get_change(m):
    num = 0
    if m >= 10:
        a = m // 10
        m = m - (a * 10)
        num += a

    if m >= 5:
        b = m // 5
        m -= (b * 5)
        num += b

    if m >= 1:
        c = m // 1
        m -= (c * 1)
        num += c

    return num


if __name__ == '__main__':
    # m = int(input('Enter value: '))
    m = int(sys.stdin.read())
    # print(get_change(m))
    list1 = [1, 5, 10]
    print(get_change_optimal(m, list1))

