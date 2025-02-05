person1 = {'first_name': 'stan', 'last_name': 'de mey', 'age': '23', 'city': 'newport beach'}
person2 = {'first_name': 'konstantinos', 'last_name': 'koulouris', 'age': '24', 'city': 'newport beach'}
person3 = {'first_name': 'kyle', 'last_name': 'cenicola', 'age': '24', 'city': 'newport beach'}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")
