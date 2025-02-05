pet1 = {'name': 'max', 'kind': 'dog', 'owner': 'simon'}
pet2 = {'name': 'cirmos', 'kind': 'cat', 'owner': 'matt'}
pet3 = {'name': 'scout', 'kind': 'dog', 'owner': 'piper'}
pet4 = {'name': 'birdie', 'kind': 'bird', 'owner': 'sam'}
pet5 = {'name': 'puff', 'kind': 'dog', 'owner': 'leila'}
pet6 = {'name': 'sissy', 'kind': 'snake', 'owner': 'alex'}

pets = [pet1, pet2, pet3, pet4, pet5, pet6]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")
