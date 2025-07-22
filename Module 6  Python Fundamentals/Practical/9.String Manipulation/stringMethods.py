# Write a Python program that manipulates and prints strings using various string methods.

text = "  hello, Python World!  "

#print Orignal string
print("Oringnal string:", repr(text))

# 1. Trailing Spaces
print("Stripped String:", text.strip())

# 2. Convert to uppercase
print("Uppercase String:", text.upper())

# 3. Convert to lowercase
print("Lowercase String:", text.lower())

# 4. Capitalize the first character
print("Capitalized:", text.strip().capitalize())

# 5. Title case (capitalize each word)
print("Capitalize each word :", text.title())

# 6. Replace 'Python' with 'Java'
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# 7. Count occurrences of 'o'
print("Count occurrences of 'o':", text.count('o'))

#8. Find the index of 'World'
print("Find the index of 'World':", text.find('World'))

# 9. Check if string starts with 'hello'
print("Starts with 'hello':", text.strip().startswith("hello"))

# 10. Check if string ends with '!'
print("Ends with '!':", text.strip().endswith("!"))