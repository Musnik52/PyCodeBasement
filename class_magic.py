import shelve

class BankAccount():
    def __init__(self, acc_id = 0, owner_name = "", balance = 0):
        self.acc_id = acc_id
        self.owner_name = owner_name
        self.balance = balance

    def __eq__(self, other):
        if type(other) == int or type(other) == float: return self.balance == other
        if type(self) != type(other): return False
        return self.balance == other.balance

    def __ne__(self, other):
        return not self.__eq__

    def __add__(self, other):
        if type(other) == int or type(other) == float: return self.balance + other
        if type(self) != type(other): return self.balance
        return self.balance + other.balance

    def __sub__(self, other):
        if type(other) == int or type(other) == float: return self.balance - other
        if type(self) != type(other): return self.balance
        return self.balance - other.balance

    def __mul__(self, other):
        if type(other) == int or type(other) == float: return self.balance * other
        if type(self) != type(other): return self.balance
        return self.balance * other.balance

    def __gt__(self, other):
        if type(other) == int or type(other) == float: return self.balance > other
        if type(self) != type(other): return False
        return self.balance > other.balance

    def __repr__(self):
        return f'BankAccount: {self.acc_id, self.owner_name, self.balance}'
    
    def __str__(self):
        return f'Account: {self.acc_id}\nOwner: {self.owner_name}\nBalance: {self.balance}'

acc1 = BankAccount(1, 'Boris', 10000000)
acc2 = BankAccount(2, 'Shachar', 78)
acc3 = BankAccount(3, 'Lior', 12345678901)
acc4 = BankAccount(4, 'Mosh', 78)
list1 = [acc1, acc2, acc3, acc4]
print(f'__str__: {acc1}')
print(f'__repr__: {list1}')
print(acc1, ">", acc2, ":", acc1 > acc2)
print(acc1, "==", acc4, ':', acc1 == acc4)
print(acc1, '==', acc2, ':', acc1 == acc2)
print(acc1, '+', acc3, ':',acc1 + acc3)
print(acc3, '-', acc1, ':',acc3 - acc1)
print(acc1, '*', acc2, ':',acc1 * acc2)
she = shelve.open('accounts.db')
she['1'] = acc1.__dict__ 
she['2'] = acc2.__dict__ 
she['3'] = acc3.__dict__ 
she['4'] = acc1.__dict__ 
print([she[f'{i}'] for i in she ])
she.close()