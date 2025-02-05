class User:
    
    def __init__(self, first_name, last_name, age, hometown, sport, hobby):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.hometown = hometown
        self.sport = sport
        self.hobby = hobby
        
    def describe_user(self, adjective):
        print(f"This user is {self.first.title()} {self.last.title()}, a {self.age}-year-old from {self.hometown.title()}.")
        print(f"He/She plays {self.sport} and likes to {self.hobby} in their free time.")
        print(f"{self.first.title()} is {adjective}.")
        
    def greet_user(self):
        print(f"Hello there, {self.first.title()}!")
        

person1 = User('mary', 'jones', '20', 'new york', 'hockey', 'play the guitar')

person1.describe_user('kind')
person1.greet_user()