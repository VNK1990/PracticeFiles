def change(amount):
    assert(amount >= 8)
    if amount == 8:
        return [5,3]
    if amount == 9:
        return [3,3,3]
    if amount == 10:
        return [5,5]
    coins = change(amount - 3)
    coins.append(3)
    return coins

if __name__ == '__main__':
   coins = change(amount = 11)
   print(len(coins), coins)