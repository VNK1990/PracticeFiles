def is_breakable(amount):
    for i in range(1,amount):
        for j in range(1,amount):
            if i * 5 + j *7 > amount:
                break
            if i * 5 + j *7 == amount:
                return True
    return False

def not_divisible_amount(amount,values):
    assert(amount >= 10)
    #get the list of values can be distributed by 5 and 7
    if amount == 1007:
        return values
    if amount % 5 == 0 or amount % 7 == 0 or amount % 12 == 0 or is_breakable(amount):
        not_divisible_amount(amount + 1,values)
        return values
    else:
        values.append(amount)
        not_divisible_amount(amount + 1, values)
        return values

if __name__ == '__main__':
    print(not_divisible_amount(amount = 10, values = []))
