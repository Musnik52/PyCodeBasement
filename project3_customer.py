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
