from pathlib import Path
path = Path("guest_book.txt")

guest_names = ""

while True:
    name = input("Guest name: ")
    guest_names += f"{name}\n"
    
    if name == "":
        break
    
path.write_text(guest_names)
    

