from city_functions import city_country

def test_city_country():
    output = city_country('budapest', 'hungary')
    assert output == 'Budapest, Hungary'
    
def test_city_country_population():
    output = city_country('budapest', 'hungary', 10000000)
    assert output == 'Budapest, Hungary - population 10000000'
