import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
print("Hypotenuse of the triangle is:", hypotenuse(a, b))
