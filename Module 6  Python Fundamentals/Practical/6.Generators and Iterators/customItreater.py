# Write a Python program that uses a custom iterator to iterate over a list of integers

def custom_iterator(int_list):
    for num in int_list:
        yield num

# Example usage
numbers = [10, 20, 30, 40, 50]
iterator = custom_iterator(numbers)

print("Iterating over the list using generator function:")
for num in iterator:
    print(num) 