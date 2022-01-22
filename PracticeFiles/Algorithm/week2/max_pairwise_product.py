def max_pairwise_product(numbers):
    max_num1 = 0
    max_num2 = 0
    for first in numbers:
       if max_num1 <= first:
           max_num2 = max_num1
           max_num1 = first
       elif max_num2 < first:
           max_num2 = first


    #print('First: ' + str(max_num1)  + ' Second: '+ str(max_num2))
    return max_num1 * max_num2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

