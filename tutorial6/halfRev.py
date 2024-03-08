def reverse_half_string(s):
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    return first_half[::-1] + second_half[::-1]

input_string = input("Enter a string with even length: ")
if len(input_string) % 2 == 0:
    reversed_string = reverse_half_string(input_string)
    print("Reversed halves:", reversed_string)
else:
    print("The length of the string is not even.")
