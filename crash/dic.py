def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""

    person = {
        'first'.title(): first_name.title(), 'last'.title(): last_name.title()
        }
    if age:
        person['age'] = age
    return person

musician = build_person('ammar', 'alim', age=44)
print(musician)