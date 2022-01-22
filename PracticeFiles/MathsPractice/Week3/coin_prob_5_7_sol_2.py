def is_breakable(amount):
    for i in range(0,amount):
        for j in range(0,amount):
            if i * 5 + j *7 > amount:
                break
            if i * 5 + j *7 == amount:
                return True
    return False

def get_list(amount, values):
    if len(values) == 5:
        print(values[0] - 1)
        return values[0] - 1

    if is_breakable(amount):
        values.append(amount)
        get_list(amount + 1, values)
    else:
        values = []
        get_list(amount + 1, values)

if __name__ == '__main__':
    get_list(amount = 10, values = [])