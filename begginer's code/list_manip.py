x = [8,1000,-3,2,5]
print('Sum: ',sum(x))
print('Max: ',max(x))
print('Min: ',min(x))
print('Average: ',sum(x)/len(x))
x.sort()
print('sorted: ', x)
print('Duplicated 5 times: ',x*5)
y = x
y.remove(x[0])
print(x)
z =[]
for i in range(len(x)):
    if x[i] < (sum(x)/len(x)): z.append(x[i])
print(z)