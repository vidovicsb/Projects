from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break
k = 1
j = 1

for i in range(height - 1, -1, -1):
    print(" " * i, end="")
    print("#" * k, end="")
    print("  ", end="")
    print("#" * j, end="")
    k += 1
    j += 1
    print()


