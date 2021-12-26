import sqlite3

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

conn = sqlite3.connect('C:\git\pyCodeBasement\SQL\\1test.db')
print('connection to db opened')
cur = conn.execute('SELECT*FROM COMPANY')
_emp = []
for row in cur: print(Employee(row[0], row[1], row[2], row[3], row[4]))
#    _emp.append(e)
#print(_emp)