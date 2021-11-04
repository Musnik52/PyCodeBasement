def doesKeyExist (d, k):
    return k in d.keys()

def tryAdd(d,k,v):
    if k in d.keys(): return False
    d[k] = v
    return True

def tryDelete(d,k):
    if k in d.keys(): return d.pop(k) 
    return None

def cityPop(c,k):
    if k not in c: return 'Input non-existing'
    return c[k]   

def cityName(c,v):
    if v not in c: return 'Input non-existing'
    return c[:v]

d = {'k1': 0, 'k2': 1, 'k3': 'a'}
#print(doesKeyExist(d, k= input('Enter Keyword: ')))
#print(tryAdd(d, k= input('Enter Keyword: '), v = input('Enter value: ')))
#print(tryDelete(d,k= input('Enter Keyword: ')))
c = {'telaviv': 200, 'london': 200, 'paris': 321, 'tokyo': 4}
print(c.fromkeys(london))
#print(cityPop(c, k = input('Enter a city: ')))
#print(cityName(c, v = input('Enter a population number: ')))