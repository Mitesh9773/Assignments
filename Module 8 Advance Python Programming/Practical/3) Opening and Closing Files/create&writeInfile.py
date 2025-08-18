# Write a Python program to open a file in write mode, write some text, and then close it.

file = open("example.txt","w")

file.write("Hello, This is a test file.\n")

file.close()

print("File written successfully.")