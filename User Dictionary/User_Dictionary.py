from pathlib import Path
import json

path = Path('user_dict.json')


def get_new_info():
    """Returns user_info dictionary"""
    user_info = {}
    first_name = input("What is your first name? ").title()
    user_info['First name'] = first_name
    last_name = input("What is your last name? ").title()
    user_info['Last name'] = last_name
    age = input("What is your age? ")
    user_info['Age'] = age
    hobby = input("What is your hobby? ")
    user_info['Hobby'] = hobby
    return user_info

def print_input(user_info):
    print("We will rememeber the following:")
    for key,value in user_info.items():
        print(f"{key}: {value}")

def info_to_file(path):
    contents = get_new_info()
    dictionary = contents.copy()
    content = json.dumps(contents)
    path.write_text(content)
    return dictionary

def get_info(path):
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def information(path):
    """Prints out information about the user if it's the same user. If not, gets new user's information"""
    if get_info(path):
        user_info = get_info(path)
        assume_first = user_info['First name']
        given_first = input("What is your first name? ").title()
        if assume_first == given_first:
            print("These are the things we know:")
            for key, value in user_info.items():
                print(f"{key}: {value}")
        else:
            print("We need to set up a new profile for you.\n")
            print_input(info_to_file(path))
    else:
        print_input(info_to_file(path))        
        


information(path)
