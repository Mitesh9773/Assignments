# Write a Python program to write multiple strings into a file

file = open("example.txt","w")

lines = ["Hello, this is line 1.\n",
    "Python file handling is easy!\n",
    "This is the third line.\n"]

file.writelines(lines)

file.close()

print("Strings written successfully.")