# python3
import sys


def compute_min_refills(distance, tank, stops, start):
    next_stop = -1
    count = 0
    # No re-fuel required and return the count
    if distance - start <= tank:
        return count

    for i in range(len(stops)):
        if stops[i] - start <= tank and stops[i] >= start:
            next_stop = stops[i]
        else:
            del stops[0:i]
            break

    if next_stop != -1:
        start = next_stop
        count = 1
        result = compute_min_refills(distance, tank, stops, start)
        if result >= 0:
            if result != 0:
                count += 1
            return count
        else:
            count = -1
            return count
    else:
        count = -1
        return count

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, _, *stops = map(int, input('Enter details: ').split())
    print(compute_min_refills(d, m, stops, start=0))
