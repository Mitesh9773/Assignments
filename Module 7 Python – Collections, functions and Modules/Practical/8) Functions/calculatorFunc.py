# Write a Python program to create a calculator using functions.
def display():
    print("\n--- Simple Calculator ---")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit\n")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero."
    else:
        return a / b

while True:
    display()
    choice = int(input("Enter your choice (1 to 5): "))

    if choice == 5:
        print("Exiting calculator.")
        break

    if choice < 1 or choice > 5:
        print("Please enter a number between 1 and 5.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", addition(num1, num2))
    elif choice == 2:
        print("Result:", subtraction(num1, num2))
    elif choice == 3:
        print("Result:", multiplication(num1, num2))
    elif choice == 4:
        print("Result:", division(num1, num2))