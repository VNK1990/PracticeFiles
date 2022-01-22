smallest = None
largest = None

while True:
    in_num = input('Enter a Number: ')
    if in_num == 'done':
       break
    try:
        num = int(in_num)
    except:
        print('Invalid input')
        continue

    else :
       if smallest is None :
           smallest = num
       elif smallest > num :
           smallest = num
       if largest is None :
           largest = num
       elif largest < num :
           largest = num

print('Maximum is',largest)
print('Minimum is',smallest)
