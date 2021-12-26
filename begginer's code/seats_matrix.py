def display_seats(x):
    for k in range(len(x)):
        for l in range(len(x[k])):
            print(x[k][l], end=" ")
        print(" ")

def noseats(a,b):
    ns = []
    for i in range(b):
        nsrow =[]
        for j in range(a):
            nsrow.append('XX')
        ns.append(nsrow)
    return ns

row = int(input('Enter number of rows: '))
col = int(input('Enter number of columns: '))
seats = []
for i in range(col):
    seatsrow =[]
    for j in range(row):
        seatsrow.append(f'{i+1}{j+1}')
    seats.append(seatsrow)
display_seats(seats)
while True:
    if seats == noseats(row,col):
        print("We're full. Goodbye")
        break
    ticket = input('Enter 2 digits XY - X for row and Y for column: ')
    if ticket in seats[int(ticket)//10-1][int(ticket)%10-1]:
        print('Available!')
        seats[int(ticket)//10-1][int(ticket)%10-1] = "XX"
        display_seats(seats)
    else:
        print('Unavailable. Please choose again.')
        continue