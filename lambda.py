def a(l1, _func):
    print(l1)
    for i in range(len(l1)):
        l1[i] = _func(l1[i])
    print (l1)

a([1,2,3,4,5], lambda x: x**2 )