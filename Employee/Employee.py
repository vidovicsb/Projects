class Employee:
    
    def __init__(self, first, last, annual):
        """Employee with first name, last name, and annual salary in $ amount"""
        self.first = first
        self.last = last
        self.annual = annual
        
    def give_raise(self, amount=5000):
        """Adds amount to annual salary, by default $5,000"""
        self.annual += amount
