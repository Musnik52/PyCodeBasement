def numtype(num):
    return 'even' if num%2 == 0 else "odd"

x = int(input('Enter a number: '))
print(f"it's {numtype(x)}")