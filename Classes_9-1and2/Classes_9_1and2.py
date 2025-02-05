class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"This is {self.restaurant_name.title()}, a restaurant the serves {self.cuisine_type.title()} food.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!\n")
        

restaurant1 = Restaurant('olympus', 'greek')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('rome', 'italian')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant('budapest', 'hungarian')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

