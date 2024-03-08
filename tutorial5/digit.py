def digit(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

num = int(input("Enter a number: "))
if digit(num):
    print("All digits are even:", num)
else:
    print("Not all digits are even.")

digit(2468)