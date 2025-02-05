from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday (mmddyyyy): ")
if birthday in pi_string:
    print("Your birthday is in pi.")
else:
    print("Your birthday is not in pi.")
