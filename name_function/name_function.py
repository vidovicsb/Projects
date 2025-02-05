def get_formatted_name(first, last, middle=''):
    """Returns a neatly formatted name"""
    if middle == '':
        full_name = f"{first} {last}"
    elif middle != '':
        full_name = f"{first} {middle} {last}"
    return full_name.title()


