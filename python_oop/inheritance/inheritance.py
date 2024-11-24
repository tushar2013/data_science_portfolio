#!/home/neo/anaconda3/bin/python

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  # Call the parent class's constructor
        self.num_doors = num_doors

    def car_info(self):
        print(f"Car Info -> Brand: {self.brand}, Model: {self.model}, Doors: {self.num_doors}")

# Example Usage
my_car = Car("Toyota", "Corolla", 4)
my_car.display_info()  # From Vehicle class
my_car.car_info()      # From Car class

