def fibonacci(n):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

n = int(input("Enter a number: "))
print("Fibonacci series up to", n, "is:", fibonacci(n))
