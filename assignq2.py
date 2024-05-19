#2.Write Python program to check for the presence of a key in the dictionary and find the sum of all values in the dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
if key in my_dict:
    print(f"The key '{key}' is present in the dictionary.")
else:
    print(f"The key '{key}' is not present in the dictionary.")

# Find the sum of all values in the dictionary
sum_values = sum(my_dict.values())
print(f"The sum of all values in the dictionary is: {sum_values}")