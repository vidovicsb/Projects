def city_country(city, country, population=0):
    if population:
        return f"{city.title()}, {country.title()} - population {str(population)}"
    else:
        return f"{city.title()}, {country.title()}"

