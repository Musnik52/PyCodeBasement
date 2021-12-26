def getInRange(mi, ma):
    while True:
        num = int(input('Enter a number. if it is within the designated range, the program ends: '))
        if  mi <= num <= ma:
            return num

h = int(input("Enter the upper limit: "))
l = int(input("Enter the lower limit: "))
while l>=h:
    l = int(input("Enter the CORRECT lower limit: "))
print(f'The number {getInRange(l,h)} was in range')