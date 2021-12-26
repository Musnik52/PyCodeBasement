import random

a = [random.randint(1,100) for i in range(10)]
print(a)

_list1 = [1,-5,-100,2,0,3,4]
x = [_list1[l] for l in range(len(_list1)) if _list1[l]>=0 ]
print (x)

_list2 = ['hello','of','python','world','best']
s =[_list2[l][0].upper() for l in range(len(_list2)) if len(_list2[l])>2]
print(s)

c =[_list2[l][::-1] for l in range(len(_list2))]
print(c)

def primer(x):
    if x < 2: return False
    for i in range(2,x):
        if x%i == 0: return False
    return True

_list3 = [1,2,5,8,17,19,29]
b = [(_list3[i],primer(_list3[i])) for i in range(len(_list3))]
print(b)
