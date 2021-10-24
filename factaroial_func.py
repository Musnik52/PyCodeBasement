def fac(num):
    k = i = 1
    while i < num:
        k *= (i+1)
        i += 1
    return k

x = int(input("Enter a number: "))
print(f"{fac(x)} is {x}'s factorial ")