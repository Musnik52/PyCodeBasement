name = input('Enter your first & last names only: ')
while len(name.split()) != 2:
    name = input('Enter your first & last names only: ')
print(f'First name: {name.split()[0]}\nLast name: {name.split()[1]}')