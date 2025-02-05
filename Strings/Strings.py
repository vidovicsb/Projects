from car import Car, ElectricCar


my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf2: ElectricCar = ElectricCar('honda', 'civic hybrid', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
print(my_leaf2.get_descriptive_name())
my_leaf2.describe_battery()
print(my_leaf.make)
my_newCar = Car('toyota', 'prius', 2012)
print(my_newCar.get_descriptive_name())

