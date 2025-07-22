# Write a Python program to apply the map() function to square a list of numbers.

numbers = [1, 2, 3, 4, 5]

square_num = list(map(lambda x: x ** 2, numbers))

print("Squared numbers:", square_num)