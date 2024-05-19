    # 1.Write a program to count the number of palindrome words in a text file

filename = "text.txt"
with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    count = 0
    for word in words:
        if word == word[::-1]:
            count += 1
    print(f"Number of palindrome words in the file: {count}")
    