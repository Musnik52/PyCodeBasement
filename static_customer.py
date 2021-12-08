from datetime import datetime

class Customer():

    current_id = 0
    last_cus_cre_ti = None

    def __init__(self, fname, lname):
        Customer.current_id += 1
        self.id = Customer.current_id
        self.fname = fname
        self.lname = lname
        Customer.last_cus_cre_ti = datetime.now()

    @staticmethod
    def last_created():
        return Customer.last_cus_cre_ti

    @staticmethod
    def reset_id():
        Customer.current_id = 0

    @staticmethod
    def get_current_id():
        return Customer.current_id

    def __repr__(self):
        return f'Customer: ({self.fname}, {self.lname})'
    
    def __str__(self):
        return f'Customer: ID:{self.id} First Name: {self.fname}, Last Name: {self.lname}'   

boris = Customer('Boris', 'Musnikov')
lior = Customer('Lior', 'Musnikov')

print(boris)
print(lior)