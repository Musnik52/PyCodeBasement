num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = min (num1, num2)
while True:
    if num1%i == num2%i == 0:
        break
    i -= 1
print(i, " is the highest divider.")
