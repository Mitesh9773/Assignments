# Write a Python program to update a value at a particular key in a
# dictionary.

student = {
    "name": "Mitesh",
    "age": 20,
    "course": "Python Backend"
}

student['name'] = "Bhargav"

for key, value in student.items():
    print(f"{key} : {value}")