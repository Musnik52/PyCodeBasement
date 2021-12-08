import sqlite3
from customer import Customer
from customer_data_access import CustomerDataAccess

conn = sqlite3.connect('C:\git\pyCodeBasement\SQL\customer.db')
print('connection to db opened')
cur = conn.execute('SELECT*FROM customer')
c1 = CustomerDataAccess('C:\git\pyCodeBasement\SQL\customer.db')

while True:
    inp = input('Enter Your Choice:\n1. Get all customers\n2. Get customer by id\n3. Insert customer\n4. Delete customer\n5. Update customer\n6. Exit\n')
    if inp == '1': print(c1.print_all_customers())
    if inp == '2': print(c1.get_customers_by_id(id=input('Enter ID: ')))
    if inp == '3': 
        n_cust = Customer(id=int(input('ID:')),fname=input('First Name: '), lname=input('Last Name: '), address=input('Address: '), mobile=input('Mobile: '))
        print(c1.insert_customer(n_cust))
    if inp == '4': print(c1.delete_customer(id = input('ID: ')))
    if inp == '5': 
        inp_id = input('Insert the current ID to be Update: ')
        if not c1.check_if_in(int(inp_id)): print("ID does't exist.")
        else:
            u_cust = Customer(id=input('ID:'),fname=input('First Name: '), lname=input('Last Name: '), address=input('Address: '), mobile=input('Mobile: '))
            print(c1.update_customer(inp_id, u_cust))
    if inp == '6': break
    else: continue
