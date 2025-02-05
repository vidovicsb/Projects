from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

py_string = ''
for line in contents.splitlines():
    py_string += f"\n{line}"
    
print(py_string.lstrip().replace('Python', 'C'))