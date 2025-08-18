# Write a Python program to create a class and access its properties using an object

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("BMW", "M5", 2020)

print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Year :", my_car.year)