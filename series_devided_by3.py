n = int(input('Enter a number:'))
total = 0
for i in range(1,n+1):
     if i%3==0:
        print(i)
        total += i
print(f'The total is: {total}')