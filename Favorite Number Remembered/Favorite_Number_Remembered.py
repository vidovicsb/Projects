from pathlib import Path
import json

path = Path('favorite_num.json')

def get_new_fn(path):
    """Get a new favorite number if one does not already exist"""
    num = int(input("What is your favorite number? "))
    contents = json.dumps(num)
    path.write_text(contents)
    return num

def get_fn(path):
    """Get favorite number if one is available"""
    if path.exists():
        contents = path.read_text()
        num = json.loads(contents)
        return num
    
    else:
        return None

def favorite_number():
    fave_num = get_fn(path)
    
    if fave_num:
        print(f"Your favorite number is {fave_num}.")
    
    else:
        fave_num = get_new_fn(path)
        print(f"I will remember that your favorite number is {fave_num}.")
        

favorite_number()
