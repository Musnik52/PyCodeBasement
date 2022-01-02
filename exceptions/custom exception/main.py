class OutOfSalmonException(Exception):
    def __init__(self, order_name, message="No Salmon! Order canceled."):
        self.message = message
        self.order_name = order_name
        super().__init__(self.message)

    def __str__(self):
        return f'SalaryNotInRangeError: {self.message}'

class Waiter:
    def __init__(self, name, kitchen_sup):
        self.name = name
        self.kitchen_sup = kitchen_sup

    def get_order(self, order_name):
        print(f'Waiter {self.name} passing order of {order_name} to kitchen_sup')
        self.kitchen_sup.proccess_order(order_name)

try:
    salary = get_salary()
except OutOfSalmonException as e:
    print(e)
    print(f'you entered {e.salary} which is illegal')