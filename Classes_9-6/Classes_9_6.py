class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"This is {self.restaurant_name.title()}, a restaurant the serves {self.cuisine_type.title()} food.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!\n")
        
    def set_number_served(self, people):
        self.number_served = people
        
    def increment_number_served(self, people):
        self.number_served += people
        

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'cookies and cream', 'coconut']
        
    def display_flavors(self):
        print("We have the following flavors:\n")
        for flavor in self.flavors:
            print(f"{flavor.title()}")
            

stand = IceCreamStand('Creamer', 'ice cream')

stand.display_flavors()
