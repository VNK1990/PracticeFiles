def fibonacci(fib, n):
    if n <= 0:
        return

    for i in range(len(fib),n+1):
        fib.append(fib[i-1] + fib[i-2])

if __name__ == '__main__':
   fib1 = [0, 1]
   fibonacci(fib1,n = 100)
   print(fib1[100])