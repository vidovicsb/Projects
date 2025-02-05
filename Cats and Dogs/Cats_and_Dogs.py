from pathlib import Path

def read_files(filename):
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {filename} is not found")
    else:
        print(contents)
              

print("These are the cat names: ")
read_files('cats.txt')

print("\nThese are the dog names: ")
read_files('dogs.txt')

print("\nThese are the dino names: ")
read_files('dinos.txt')
