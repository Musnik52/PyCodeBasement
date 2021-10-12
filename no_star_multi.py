num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = num2
while num1 > 1:
    num2 += num3
    num1 -= 1
print(num2)