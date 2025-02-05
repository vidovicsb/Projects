class User:
    
    def __init__(self, first_name, last_name, age, hometown, sport, hobby, login_attempts):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.hometown = hometown
        self.sport = sport
        self.hobby = hobby
        self.login_attempts = login_attempts
        
    def describe_user(self, adjective):
        print(f"This user is {self.first.title()} {self.last.title()}, a {self.age}-year-old from {self.hometown.title()}.")
        print(f"He/She plays {self.sport} and likes to {self.hobby} in their free time.")
        print(f"{self.first.title()} is {adjective}.")
        
    def greet_user(self):
        print(f"Hello there, {self.first.title()}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

person1 = User('mary', 'jones', '20', 'new york', 'hockey', 'play the guitar', 3)

person1.describe_user('kind')
person1.greet_user()
      
print(f"This person has had {person1.login_attempts} login attempts.")
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
print(f"This person has had {person1.login_attempts} login attempts.")
person1.reset_login_attempts()
print(f"This person has had {person1.login_attempts} login attempts.")



