# Write a Python program to demonstrate handling multiple exceptions

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1/num2
    print(f"Result: {result}")

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except Exception as e:
     print(f"An unexpected error occurred: {e}")