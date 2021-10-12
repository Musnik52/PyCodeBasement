p = []
k = 2
while k <= 101:
    i = 2
    while k%i != 0: i += 1
    if i == k: p.append(i)
    k += 1
print(p)