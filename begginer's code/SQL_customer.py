import sqlite3

class Customer:
    def __init__(self, id, fname, lname, address, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile
    
    def __repr__(self):
        return f'Customer: {self.id, self.fname, self.lname, self.address, self.mobile}'

    def __str__(self):
        return str(self.__dict__)

conn = sqlite3.connect('C:\git\pyCodeBasement\SQL\customer.db')
print('connection to db opened')
cur = conn.execute('SELECT*FROM customer')

def insert_customer(cur, table, id, fname, lname, address, mobile):
    cur.execute(f'INSERT INTO {table} VALUES ({id}, "{fname}","{lname}", "{address}", {mobile})')


def delete_customer(cur, table, id):
    cur.execute(f"DELETE FROM {table} WHERE id = {id}")

def update_customer(cur, table, id, address, mobile):
    cur.execute(f"UPDATE {table} SET address = {address} WHERE id = {id}")
    cur.execute(f"UPDATE {table} SET mobile = {mobile} WHERE id = {id}")

def print_all_customers(cur):
    cur.execute('SELECT*FROM customer')
    print([row for row in cur])

#insert_customer(cur, "customer", 3, 'Ana', 'Musnikov', 'Makor 12', 507859986)
#update_customer(cur, "customer", 3, 'Eilat 2', 86424431)
print_all_customers(cur)
#delete_customer(cur, "customer", 3)

print('connection to db closed')

conn.commit()
conn.close()