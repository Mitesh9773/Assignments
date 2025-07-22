# #Write a Python program that demonstrates the correct use of indentation, comments, and
# variables following PEP 8 guidelines.

# Ask the user to enter a number
user_input = input("Enter a number: ")

# Check if the input is a digit (positive integers only)
if user_input.isdigit():
    number = int(user_input)

    # Check if the number is even
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
else:
    print("Invalid input. Please enter a valid positive integer.")
