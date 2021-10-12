np = 0
while True:
    p = i = 0
    num = int(input('Enter a number. A prime number will end the program: '))
    while i <= num:
        i += 1
        if num%i == 0: p += 1
    if p == 2: break
    np += 1
print(f'{np} numbers entered were not prime-numbers.')