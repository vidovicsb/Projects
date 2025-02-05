from name_function import get_formatted_name

def test_no_middle_name():
    formatted = get_formatted_name('barnabas', 'vidovics')
    assert formatted == 'Barnabas Vidovics'
    
def test_is_middle_name():
    formatted = get_formatted_name('barnabas', 'vidovics', 'laszlo')
    assert formatted == 'Barnabas Laszlo Vidovics'
