from user_modules import User

class Admin(User):
    """Child class of User class called Admin, with special privileges."""

    def __init__(self, first_name, last_name, age, hometown, sport, hobby, login_attempts):
        super().__init__(first_name, last_name, age, hometown, sport, hobby, login_attempts)
        self.privileges = Privileges()
        
 

class Privileges:
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can grant privileges']

    def show_privileges(self):
        print("The admin has the following privileges: \n")
        for privilege in self.privileges:
            print(f"{privilege.title()}")
        print("\n")
