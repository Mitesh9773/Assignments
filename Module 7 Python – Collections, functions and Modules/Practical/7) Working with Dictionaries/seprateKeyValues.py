# rite a Python program to separate keys and values from a dictionary using
# keys() and values() methods

student = {
    "name": "Mitesh",
    "age": 20,
    "course": "Python Backend"
}

for key, value in student.items():
    print(f"{key} : {value}")