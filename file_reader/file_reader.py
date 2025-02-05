from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

print(contents)
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line
    
print(pi_string)
print(len(pi_string))

print(1+float(pi_string))
