# Uses python3
import sys


def get_optimal_value(capacity, weights, values, per_weight_value):
    value = 0.
    if capacity == 0 or len(weights) == 0:
        return value
    else:
        index = per_weight_value.index(max(per_weight_value))
        if capacity >= weights[index]:
            value = values[index]
            capacity -= weights[index]
            per_weight_value.pop(index)
            weights.pop(index)
            values.pop(index)
        else:
            value = capacity * per_weight_value[index]
            capacity = 0

    return value + get_optimal_value(capacity, weights, values, per_weight_value)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input('Enter values: ').split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # n = 3
    # capacity = 100
    # values = [60, 100, 120]
    # weights = [20, 50, 30]

    per_weight_value = []
    for i in range(n):
        per_weight_value.append(values[i] / weights[i])

    # print('n', n)
    # print('capacity', capacity)
    # print('values', values)
    # print('weights', weights)
    # print('per_weight_value', per_weight_value)

    opt_value = get_optimal_value(capacity, weights, values, per_weight_value)
    print("{:.4f}".format(opt_value))
