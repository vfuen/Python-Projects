from car import Car
from electric_car import Battery, Electric_car





tesla00 = Electric_car("tesla", "model 3", 2019, "black")
print(tesla00.get_car())
tesla00.battery.charge_time()
tesla00.update_rim_size(18)
tesla00.rim_size()
tesla00.battery_range(75)

print("\n")


car01 = Car("Mazda", 3, 2020, "blue")
car01.color = "pearlescent blue"
print(car01.get_car())
#Changed the parameter of the value rims to 20.
car01.rims = 16
car01.update_rim_size(12)
car01.rim_size()

print("\n")


car02 = Car("Ford", "GT 40", 2017, "Silver")
print(car02.get_car())
car02.increment_miles(100)
car02.car_miles()
car02.update_miles(22_50)
car02.car_miles()
car02.increment_miles(100)
car02.car_miles()
car02.update_miles(22_50)

print("\n")

















class Sayain:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def food(self):
        print(f"{self.name} is eating.")

    def fight(self):
        print(f"Now {self.name} is fighting.")


sayain1 = Sayain("Goku", 40)
sayain2 = Sayain ("Vegeta", 42)
print(f"His name is {sayain1.name}.")
print(f"His name is {sayain2.name}.")

print(f"{sayain1.name} is {sayain1.age} years old.")
print(f"{sayain2.name} is {sayain2.age} years old.")

sayain1.food()
sayain2.food()
print(f"{sayain2.name} is done eating")
print(f"{sayain1.name} finished eating.")
sayain1.fight()
sayain2.fight()
print(f"{sayain2.name} saw {sayain1.name}.")
print(f"{sayain2.name} fights {sayain1.name}.")
