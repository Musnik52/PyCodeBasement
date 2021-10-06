num = int(input('Enter a number: '))
h = i = 1
while i <= num:
    l = []
    while h <= num:
        l.append(h)
        h += 1
    print(l)
    i += 1
    h = i
while i > 0:
    k = []
    while num > 0:
         k.append(num)
         num -= 1
    print(k)
    i -= 1
    num = i