num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
k = 1
d1 = [1]
d2 = [1]
d3 = [1]
while k < max(num1, num2):
    k += 1
    if num1%k == 0: d1.append(k)
    if num2%k == 0: d2.append(k)
    if num1%k == num2%k == 0: d3.append(k)
print (f"{num1}'s deviders are: {d1}.\n{num2}'s deviders are: {d2}.\nThe highest common devider is: {max(d3)}")