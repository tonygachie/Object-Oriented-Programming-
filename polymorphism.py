# Base class
class Vehicle:
    def move(self):
        # generic move, to be overridden
        print("The vehicle is moving.")

# Subclass Car
class Car(Vehicle):
    def move(self):
        print(" The car is driving on the road.")

# Subclass Plane
class Plane(Vehicle):
    def move(self):
        print(" The plane is flying in the sky.")

# Subclass Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")

# Subclass Bike
class Bike(Vehicle):
    def move(self):
        print(" The bike is pedaling forward.")

# Test polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
