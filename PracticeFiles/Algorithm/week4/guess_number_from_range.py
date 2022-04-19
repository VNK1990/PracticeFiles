import math


def guess_number(low, high, qs):
    num = 0
    if qs == 0:
        return
    l_or_u = input('Enter L or U: ')
    if l_or_u == 'L':
        print('Lower: ', math.floor(low + ((high - low) / 2)))
        num = guess_number(low, math.floor(low + ((high - low) / 2)), qs=qs - 1)
        return num
    elif l_or_u == 'U':
        print('Upper: ', math.ceil(low + ((high - low) / 2)))
        num = guess_number(math.ceil(low + ((high - low) / 2)), high, qs=qs - 1)
        print(num)
        return num


if __name__ == '__main__':
    guess_number(low=1, high=127, qs=7)
