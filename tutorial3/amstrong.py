#print all the armstrong numbers between 1 and 1000
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for i in range(lower,upper+1):
    n = i
    s = 0
    while n > 0:
        r = n % 10
        s = s + r ** 3
        n = n // 10
    if i == s:
        print(i)