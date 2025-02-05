from random import choice, randint

colors = ['green', 'blue', 'yellow', 'red', 'black', 'white', 'brown', 'grey', 'pink']
speeds = ['slow', 'medium', 'fast']

aliens = []

for alien in range(0, 31):
    new_alien = {'color': choice(colors), 'points': randint(1, 5), 'speed': choice(speeds)}
    aliens.append(new_alien)
    
for i, member in enumerate(aliens):
    print(f"{i}: {member}")

