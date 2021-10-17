num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = num2
for i in range(1, num1):
    num3 += num2
    print(i)
    print (num3)
print (num3)