def sum_even_numbers(n):
    return sum(x for x in range(1, n+1) if x % 2 == 0)

N = int(input("Enter a number: "))
print("Sum of even numbers between 1 and", N, "is:", sum_even_numbers(N))
