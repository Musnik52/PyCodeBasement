a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
p = 1
while b>0:
    m=0
    t=a
    while t>0:
        m += p
        t -= 1
    p = m
    b -= 1
print(p)