# Write a Python program to update a value in a dictionary

student = {
    "name": "Mitesh",
    "age": 20,
    "course": "Python Backend"
}

student["name"] = "Pavan"
student["age"] = 20
student["course"] = "Python Fullstack"

for key,value in student.items():
    print(f"{key}: {value}")