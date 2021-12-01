import sqlite3
from project3_customer import Customer

conn = sqlite3.connect('C:\git\pyCodeBasement\SQL\customer.db')
print('connection to db opened')
cur = conn.execute('SELECT*FROM customer')

def print_all_customers(cur):
    cur.execute('SELECT*FROM customer')
    for row in cur: print(Customer(row[0], row[1], row[2], row[3], row[4]))

def insert_customer(cur, customer):
    cur.execute(f'INSERT INTO customer VALUES ({customer.id}, "{customer.fname}", "{customer.lname}", "{customer.address}", {customer.mobile})')

def delete_customer(cur, id):
    cur.execute(f"DELETE FROM customer WHERE id = {id}")

def get_all_customers (cur):
    cur.execute('SELECT*FROM customer')
    return [f'{row[1]} {row[2]}' for row in cur]

def get_customers_by_id (cur, id):
    cur.execute(f'SELECT*FROM customer WHERE id = {id}')
    return [f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}' for row in cur]

def update_customer(cur, id, customer):
    cur.execute(f"UPDATE customer SET VALUES ({customer.id}, '{customer.fname}', '{customer.lname}', '{customer.address}', {customer.mobile}) WHERE id = {id}")

'''
moris = Customer(3,'moris', 'musnik', 'rashi 31', 1234321)
alon = Customer(4,'alon', 'musnik', 'rashi 15', 9876789)
insert_customer(cur, moris)
print_all_customers(cur)
delete_customer(cur, 3)
'''