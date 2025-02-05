from random import choice, randint

my_list = []
for i in range(1, 16):
    my_list.append(i)

my_choice = randint(1, 15)
print(f"Your number is: {my_choice}\n")

winner = 0
counter = 1
while winner != my_choice:
    winner = choice(my_list)
    if winner == my_choice:
        print(f"\nYou won. Winning number is: {my_choice}")
        print(f"The number of attempts it took: {counter}")
        break
    print(f"{counter}: {winner}")
    counter += 1


