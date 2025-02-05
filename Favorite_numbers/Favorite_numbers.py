fave_numbers = {'stan': [2, 8, 6], 'kostas': [3, 5, 1], 'kyle': [4, 8, 6]}

for key, value in fave_numbers.items():
    print(f"{key.title()}'s favorite numbers are: ")
    list = []
    for num in value:
        list.append(num)
        
    print(*list, sep=', ')
    print("\n")
