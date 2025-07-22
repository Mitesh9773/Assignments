# Example 5: Write a Python program to find greater and less than a number using
# if_else.

numA = input("Enter a Number A: ")
numB = input("Enter a Number B: ")
numC = input("Enter a Number C: ")

if(numA > numB):
    if(numA > numC):
        print(numA, "is greater than both", numB, "and", numC)
    else:
        print(numA, "is greater than", numB, "but less than", numC)
else:
    if(numB > numC):
        print(numB, "is greater than both", numA, "and", numC)
    else:
        print(numB, "is grater than", numA, "but less than", numC)
