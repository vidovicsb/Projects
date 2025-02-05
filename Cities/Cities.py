cities = {
    'budapest': {
        'country': 'hungary',
        'population': '2 million',
        'fact': 'lots of assholes',
        },
        
    'new york': {
        'country': 'usa',
        'population': '8 million',
        'fact': 'lots of buildings',
        },
        
    'los angeles': {
        'country': 'usa',
        'population': '4 million',
        'fact': 'lot of homeless',
        },
    }

for city, data in cities.items():
    print(f"City: {city.title()}")
    for key, value in data.items():
        print(f"\t {key.title()}: {value.title()}")
    print("\n")


