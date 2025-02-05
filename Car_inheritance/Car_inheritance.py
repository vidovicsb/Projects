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
        self.battery_size = 40
        
    def describe_battery(self):
        """Describes the battery of the electric vehicle"""
        print(f"This car has a {self.battery_size} kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
