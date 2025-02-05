from random import randint

class Die:
    
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        return randint(1, self.sides)
    


six_sides = Die()
print(f"10 random rolls with a {six_sides.sides}-sided die:\n")
for i in range(0, 10):
    print(f"{i+1}: {six_sides.roll_die()}")
    
print("\n")    
ten_sides = Die(10)
print(f"10 random rolls with a {ten_sides.sides}-sided die:\n")
for i in range(0, 10):
    print(f"{i+1}: {ten_sides.roll_die()}")

print("\n")
twenty_sides= Die(20)
print(f"10 random rolls with a {twenty_sides.sides}-sided die:\n")
for i in range(0, 10):
    print(f"{i+1}: {twenty_sides.roll_die()}")