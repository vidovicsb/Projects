from pathlib import Path

name = input("What is your name? ")
path = Path("guest.txt")
path.write_text(f"The person's name is: {name}")
