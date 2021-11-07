def isDictKeysAlpha(di):
    for k in di:
        if not str(k).isalpha(): return False
    return True

def popByValue(d, v):
    deleted = [[i, d[i]] for i in d if str(v) == str(d[i])]
    for j in deleted: d.pop(j[0])
    return deleted

def compareDict(d1, d2):
    return d1 == d2 

def newDict(l1, l2):
    if (len(l1) != len(l2)) or len(l1) != len(set(l1)) or len(l2) != len(set(l2)):
        return None
    ndi={l1[i]: l2[i] for i in range(len(l1))}
    return ndi

di1 = {'k1': 1, 'k2': 'b', 'k3': 'c2', 'k4': 1}
di2 = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
di3 = {1: 'a', 2: 'b', 3:'c', 4: 'a'}
print(isDictKeysAlpha(di1))
print(isDictKeysAlpha(di2))
print(isDictKeysAlpha(di3))
print('='*50)
print(popByValue(di1,v = input('Enter a value: ')))
print(di1)
print(popByValue(di2,v = input('Enter a value: ')))
print(di2)
print(popByValue(di3,v = input('Enter a value: ')))
print(di3)
print('='*50)
di4 = {'k1': 1, 'k2': 'b', 'k3': 'c2', 'k4': 1}
print(compareDict(di1, di4))
print(compareDict(di1, di2))
print('='*50)
list1 = ['a1', 'a2', 'a3', 'a4']
list2 = [12,13,14,15]
list3 = ['b1', 'b2']
list4 = [2,2,3,4]
print(newDict(list1, list2))
print(newDict(list1, list4))
print(newDict(list3, list2))