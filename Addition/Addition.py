from pathlib import Path

print("Type in 2 numbers, and I'll add them together.")
print("To quit, press 'q'")

while True:
    
    num1 = input("Number 1: ")
    if num1 == 'q':
        break
    num2 = input("Number 2: ")
    if num2 == 'q':
        break
    
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("You can only add numbers.")
    else:
        print(answer)

