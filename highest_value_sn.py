i =1
num = int(input(f'#{i} - Enter a number: '))
j = num
while i <= 10:
    num = int(input(f'#{i} - Enter a number: '))
    if num > j:
        j = num
        k = i
    i += 1
print(f"#{k}'s value is the highest entered.") 