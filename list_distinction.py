'''
a = "i wake up at 6:00 am"
l = [a[i] for i in range(len(a)) if a[i].isalpha()]
n = [a[i] for i in range(len(a)) if a[i].isdigit()]
print(l, n)

p = [5.9,0.9,-9.2,11.1]
m = [int(p[i]) for i in range(len(p))]
print(m)

nums = [[1,2,6],[7,8,9],[100,5,2]]
ma = [max(nums[i]) for i in range(len(nums))]
mi = [min(nums[i]) for i in range(len(nums))]
print(ma, mi)

import statistics
print(statistics.mean([1,2,3]))
_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
print([_prices[i] if _prices[i] > 0 else 0 for i in range(len(_prices))])

k = ['hello','','python','world','full stack','a']
h = [len(k[i]) if len(k[i]) > 3 else (-1) for i in range(len(k))]
print(h)

print([[j for j in range(i)] for i in range(1,6)])
m = [[1,2,3],[4,5,6],[7,8,9]]
mp = [i for j in m for i in j]
print(mp)
'''
print([[j for j in range(i, 10)] for i in range(3)])