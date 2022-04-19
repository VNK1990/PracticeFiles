# python3
import sys


def remove_list_elements(stops, r_list):
    new_list = []
    for stop in stops:
        if stop not in r_list:
            new_list.append(stop)
    stops = new_list
    return stops


def compute_min_refills(distance, tank, stops):
    start_point = 0
    r_list = []
    count = 0

    #exit case
    if distance - start_point <= tank:
        return 0

    # Get the stops till far stop
    for stop in stops:
        if stop - start_point <= tank:
            r_list.append(stop)
        else:
            break

    if len(r_list) <= 0:
        return -1
    else:
        start_point = max(r_list)
        stops = remove_list_elements(stops, r_list)
        stops = [stop - start_point for stop in stops]
        distance = distance - start_point
        count = compute_min_refills(distance, tank, stops)
        if count == -1:
            return -1
        else:
            count += 1
            return count

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
