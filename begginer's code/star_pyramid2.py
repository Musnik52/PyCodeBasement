num = int(input('Enter a base number of * for the pyramid: '))
for i in range(1,num+1,2):
    print(" "*((num-i)//2),"*"*i)
for i in range(2,num+1,2):
    print(" "*((num-i)//2),"*"*i)
for i in range(3,num+1,2):
    print(" "*((num-i)//2),"*"*i)