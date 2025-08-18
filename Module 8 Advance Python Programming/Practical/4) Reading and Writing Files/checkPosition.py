# Write a Python program to check the current position of the file cursor using tell().

with open("example.txt","w") as file:
    file.write("Hello, World!")

with open ("example.txt","r") as file:
    file.read(5)

    position = file.tell()
    print(f"Current cursor position: {position}")
