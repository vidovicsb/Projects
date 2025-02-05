from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
print("\n")

lines = contents.splitlines()
lines_list = []

for line in lines:
    lines_list.append(line)
    
for line in lines_list:
    print(f"\t{line}")
