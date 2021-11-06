class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles = 1
        self.rims = 16

    def get_car(self):
        whole_description = f"{self.year} {self.color} {self.make} {self.model} "
        return whole_description.title()

    def update_rim_size(self, new_size):
            if new_size >= self.rims:
                self.rims = new_size
            if new_size > 22:
                print("Largest rim size 22 inches.")
            if new_size < 16:
               print("Smallest rim size is 16 in.")

    def rim_size(self):
        print(f"Comes in {self.rims}-inch rims.")



    def car_miles(self):
        print(f"Car mileage is {self.miles}")

    def update_miles(self, mileage):
        if mileage >= self.miles:
            self.miles = mileage
        else:
            print("This car cannot go down in mileage."
                  f"\nCar mileage is currently {self.miles}.")

    def increment_miles(self, mileage):
        self.miles += mileage



class Battery:

    def __init__(self,  max_charge=120):
        self.battery_charge = max_charge
    #If I decide to move the method battery_range back too Battery.
        # self.battery_size = size
    def charge_time(self):
        print(f"Full charge in {self.battery_charge} minutes.")


class Electric_car(Car):

    def __init__(self, make, model, year, color):

        super().__init__(make, model, year, color)
        self.battery = Battery()
        self.battery_size = 75



    def fill_gas_tank(self):
        print("Tesla's doesnt use gas!")

    def battery_range(self):

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go around {range} miles on a full charge.")

    def switch_battery_size(self, option_battery):
        if option_battery >= self.battery_size:
            self.battery_size = option_battery
        if option_battery == 75:
            range = 260
        if option_battery == 100:
            range = 320
        else:
            print(f"{option_battery} not a battery size.")