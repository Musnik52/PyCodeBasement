import sqlite3
from customer import Customer

class CustomerDataAccess:

    def __init__(self, db_path):
        conn = sqlite3.connect(db_path)
        self.db_path = db_path
        self.cur = conn.cursor()
    
    def check_if_in(self, inp):
        self.cur.execute('SELECT*FROM customer')
        l = [row[0] for row in self.cur]
        return inp in l

    def print_all_customers(self):
        self.cur.execute('SELECT*FROM customer')
        for row in self.cur: print(Customer(row[0], row[1], row[2], row[3], row[4]))

    def insert_customer(self, customer):
        if self.check_if_in(int(customer.id)): return "ID already exists."
        self.cur.execute(f'INSERT INTO customer VALUES ({customer.id}, "{customer.fname}", "{customer.lname}", "{customer.address}", {customer.mobile})')
        return f'Customer {customer.fname} {customer.lname} - ADDED'

    def delete_customer(self, id):
        if not self.check_if_in(int(id)): return "ID does't exist."
        self.cur.execute(f"DELETE FROM customer WHERE id = {id}")
        return f'Customer with the ID: {id} - DELETED.'

    def get_all_customers (self):
        self.cur.execute('SELECT*FROM customer')
        return [f'{row[1]} {row[2]}' for row in self.cur]

    def get_customers_by_id (self, id):
        if not self.check_if_in(int(id)): return "ID does't exist."
        else:
            self.cur.execute(f'SELECT*FROM customer WHERE id = {id}')
            return [f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}' for row in self.cur] 

    def update_customer(self, id, customer):
        self.cur.execute(f"UPDATE customer SET id = {customer.id} WHERE id = {id} ")
        self.cur.execute(f"UPDATE customer SET fname = '{customer.fname}' WHERE id = {id} ")
        self.cur.execute(f"UPDATE customer SET lname = '{customer.lname}' WHERE id = {id} ")
        self.cur.execute(f"UPDATE customer SET address = '{customer.address}' WHERE id = {id} ")
        self.cur.execute(f"UPDATE customer SET mobile = {customer.mobile} WHERE id = {id} ")
        return f'Customer {customer.fname} {customer.lname} - UPDATED'

    def __repr__(self):
        return f'CustomerDataAccess({self.db_path})'

    def __str__(self):
        return f'CustomerDataAccess: db_path: {self.db_path}'


