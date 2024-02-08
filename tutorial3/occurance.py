#count the occurace of a particular letter in a string
str = input("Enter the string: ")
ch = input("Enter the character: ")
count = 0
for i in str:
    if i == ch:
        count += 1
print("The character",ch,"occurs",count,"times")
