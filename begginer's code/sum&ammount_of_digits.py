#Get a number, and show the number of digits and the sum of the digits.
num = int(input('Enter a number: '))
j = 0
k = 0
while 0 < num:
    j += 1
    k += num%10
    num //= 10
print (f' The number has {j} digit(s), and the sum is: {k}')