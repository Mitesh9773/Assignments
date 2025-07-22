# Example 7: Write a Python program to calculate grades based on percentage using
# if-else ladder

marks = int(input("Enter your marks: "))

if 80 <=marks <= 100:
    print("Grade: A")
elif 60 <= marks < 80:
    print("Grade: B")
elif 40 <= marks < 60:
    print("Grade: C")
elif 0 <= marks < 40:
    print("Grade: F")
else:
    print("Invalid marks entered.")