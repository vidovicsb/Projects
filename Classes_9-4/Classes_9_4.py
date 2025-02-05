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
        

restaurant = Restaurant('olympus', 'greek')

print(f"The number of people served is {restaurant.number_served}.")
restaurant.number_served = 20
print(f"The number of people served is {restaurant.number_served}.")
restaurant.set_number_served(30)
print(f"The number of people served is {restaurant.number_served}.")
restaurant.increment_number_served(20)
print(f"The number of people served is {restaurant.number_served}.")



