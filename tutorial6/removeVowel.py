def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

input_string = input("Enter a string: ")
print("String with vowels removed:", remove_vowels(input_string))
