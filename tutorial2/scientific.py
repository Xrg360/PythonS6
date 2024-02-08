#python pgm to implement calculator to perform a few scientific operations like abs,ceil,floor,sin,cos,tan,log,sqrt,x^y,log2,log10
import math
a = int(input("Enter the first number: "))

print("The value of a is: ", a)
print("The absolute value of a is: ", abs(a))
print("The ceil value of a is: ", math.ceil(a)) 
print("The floor value of a is: ", math.floor(a))
print("The sin value of a is: ", math.sin(a))
print("The cos value of a is: ", math.cos(a))
print("The tan value of a is: ", math.tan(a))
print("The log value of a is: ", math.log(a))
print("The square root value of a is: ", math.sqrt(a))
b = int(input("Enter the second number: "))
print("The value of a^b is: ", math.pow(a,b))
print("The log2 value of a is: ", math.log2(a))
print("The log10 value of a is: ", math.log10(a))
