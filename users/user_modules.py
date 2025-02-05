class User:
    """Creating a User class to store specific attributes about users."""

    def __init__(self, first_name, last_name, age, hometown, sport, hobby, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown
        self.sport = sport
        self.hobby = hobby
        self.login_attempts = login_attempts
        
    def describe_user(self, adjective):
        """This method describes the user"""
        print(f"This user is {self.first.title()} {self.last.title()}, a {self.age}-year-old from {self.hometown.title()}.")
        print(f"He/She plays {self.sport} and likes to {self.hobby} in their free time.")
        print(f"{self.first.title()} is {adjective}.")
        
    def greet_user(self):
        print(f"Hello there, {self.first.title()}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

