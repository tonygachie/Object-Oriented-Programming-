# Parent class: Car
class Car:
    def __init__(self, brand, model, year, color):
        # Attributes (encapsulation with underscore to indicate 'private')
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0  # starts at rest

    # Methods
    def accelerate(self, increment):
        self._speed += increment
        print(f"{self._brand} {self._model} accelerated to {self._speed} km/h.")

    def brake(self, decrement):
        self._speed = max(0, self._speed - decrement)
        print(f"{self._brand} {self._model} slowed to {self._speed} km/h.")

    def honk(self):
        print(f"{self._brand} {self._model} says: Beep beep!")

    # Getter (to safely access private attribute)
    def get_speed(self):
        return self._speed


# Child class: ElectricCar (Inheritance + Polymorphism)
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        # Call parent constructor
        super().__init__(brand, model, year, color)
        self._battery_capacity = battery_capacity  # in kWh
        self._battery_level = 100  # percentage

    # Override (polymorphism: different behavior than parent class)
    def honk(self):
        print(f"{self._brand} {self._model} says: Silent beep... ")

    # Extra method specific to ElectricCar
    def charge(self):
        self._battery_level = 100
        print(f"{self._brand} {self._model} is fully charged.")


# Example usage
car1 = Car("Toyota", "Corolla", 2020, "Blue")
car1.accelerate(30)
car1.honk()
car1.brake(10)

print("----")

tesla = ElectricCar("Tesla", "Model S", 2023, "Red", 100)
tesla.accelerate(50)
tesla.honk()          # polymorphism in action
tesla.charge()
