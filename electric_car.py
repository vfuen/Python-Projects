from car import Electric_car, Battery
#can also use 'import car' with dot notation after the module name

tesla01 = Electric_car("tesla", "model 3", 2020, "gold")
print(tesla01.get_car())
tesla01.battery.charge_time()
tesla01.update_rim_size(18)
tesla01.rim_size()
tesla01.battery_range()
tesla01.switch_battery_size(100)
tesla01.battery_range()
tesla01.switch_battery_size(33)
print("\n")