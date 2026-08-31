class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

    def vehicle_type(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def vehicle_type(self):
        print("This is a car.")

    def display_car_info(self):
        self.display_info()
        print("Number of doors:", self.doors)
my_car = Car("Toyota", "Corolla", 4)
my_car.display_car_info()
my_car.vehicle_type()
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))