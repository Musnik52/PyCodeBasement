def name(fname='John',lname='Doe'):
    return f'{fname} {lname}'

f = input('What is your name? ')
l = input('What is your last name? ')
print(f"{name(f,l)}")