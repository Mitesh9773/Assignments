# Example: 9) Write a Python program to print every alternate character from the
# string starting from index 1.

def printString(name):
    for i in name[1::2]:
        print(i)

firstName = "Mitesh"
printString(firstName)
