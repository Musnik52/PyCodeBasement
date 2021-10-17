a = int(input('Enter a begining number: '))
b = int(input('Enter destination number: '))
t = (a-b)/abs(a-b) 
for i in range(a,b-t,-t):
    print(i)