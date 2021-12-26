def invokeme(l1, _func):
    print(l1)
    for i in range(len(l1)):
        l1[i] = _func(l1[i])
    print (l1)

def invokeme_zugi_ezugi(l1, func1, func2):
    for i in range(len(l1)):
        if l1[i]%2==0: l1[i] = func1(l1[i])
        else: l1[i] = func2(l1[i])
    print (l1)

#invokeme([1,2,3,4,5], lambda x: x**2 )
invokeme_zugi_ezugi([1,2,3,4,5], lambda x: x*2, lambda x: x**0)