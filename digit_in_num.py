x = int(input('Enter a number: '))
dig = int(input('Enter a single digit: '))
k = x
while k%dig != 0:
    k -= 1
print(f'{dig} is in {x} exactly {int(k/dig)} times.')