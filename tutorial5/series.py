def generate_series(n):
    series = [1]
    num = 1
    for i in range(2, n+1):
        num += i
        series.append(num)
    return series

n = int(input("Enter the number of terms: "))
print("Generated series:", generate_series(n))
