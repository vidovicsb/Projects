from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("The following tickets win the prize:\n")
for i in range(0,4):
    winner = choice(list)
    list.pop(list.index(winner))
    print(winner)
    
print("\n")
print(list)
