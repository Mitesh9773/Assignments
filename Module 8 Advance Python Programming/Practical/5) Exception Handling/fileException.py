# Write a Python program to handle file exceptions and use the finally block for closing
# the file

try:
    file_name = input("Enter the file name: ")
    f = open(file_name,"r")
    content = f.read()
    print("File content:\n", content)

except FileNotFoundError:
    print("The file is not found.")

except PermissionError:
    print("You don't have permission to read this file.")

except Exception as e:
    print(f"Unexcepted error occours: {e}")

finally:
    try:
        f.close()
        print("File closed successfully.")
    except NameError:
        print("No file was opened.")