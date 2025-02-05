class Car:
    """Car class with attributes and methods"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def read_mileage(self):
        """Tells us the miles on the vehicle"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def get_descriptive_name(self):
        """Returns the name of the vehicle in a neat format"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        """Updates the odometer to 'mileage' value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer.")
            
    def increment_odometer(self, miles):
        """Increments odometer by 'miles' value"""
        self.odometer_reading += miles
        

class ElectricCar(Car):
    """Child class of the class Car"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        

class Battery:
    """Making a separate class for the battery, which is then called in the electric car class."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size} kWh battery.")
        
    def get_range(self):
        """Get the range of the battery of a full charge, depending on the size of the battery."""
        if self.battery_size == 40:
            range = 150
            print(f"This car has a {range} mile range on a full charge.")
      
        elif self.battery_size == 65:
            range = 225
            print(f"This car has a {range} mile range on a full charge.")
            
    def set_battery_size(self, size):
        """Set a different size of battery for the car."""
        self.battery_size = size
                

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.set_battery_size(65)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
                                 


