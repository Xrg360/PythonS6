import sys

# Get the command-line arguments
arguments = sys.argv

# Check if there are two arguments provided
if len(arguments) == 3:
    # Get the two numbers from the arguments
    num1 = int(arguments[1])
    num2 = int(arguments[2])

    # Perform addition
    result = num1 + num2

    # Print the result
    print("The sum is:", result)
else:
    print("Please provide two numbers as command-line arguments.")