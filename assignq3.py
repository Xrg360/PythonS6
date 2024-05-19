def slice_string(string):
    odd_indices = string[1::2]
    even_indices = string[::2]
    return odd_indices, even_indices

def replace_spaces(string):
    if ' ' in string:
        return string.replace(' ', '')
    else:
        return '$' + string + '$'

def main():
    string = input("Enter a string: ")

    while True:
        print("\nMenu:")
        print("1. Slice the string to two separate strings")
        print("2. Replace all the spaces in the string")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            odd_indices, even_indices = slice_string(string)
            print("Odd indices string:", odd_indices)
            print("Even indices string:", even_indices)
        elif choice == '2':
            new_string = replace_spaces(string)
            print("Modified string:", new_string)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()