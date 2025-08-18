# Write a Python program to demonstrate the use of local and
# global variables in a class.

x = 10  #global variable 

class demo:
    def show_variables(self):
        #Local Vaiable
        y = 20
        print(f"Global Variable is: {x}")
        print(f"Local Variable is: {y}")

obj = demo()
obj.show_variables()

print(f"Outside global variable: {x}")