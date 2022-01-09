from error_sal_too_high import *
from error_sal_too_low import *

class SalaryInputs():
    def get_salary(self, amount):
        # if the amount is not float raise valueError
        # hint: float(amount)
        # if amount > 100_000 raise TooHigherError
        # if amount < 10_000 raise TooLowerError
        # else return amount * 2
        if type(amount) != float:
            raise ValueError('Salary must be a float!')
        if 10000 > amount:
            raise TooLowError(amount)
        elif 100000 < amount:
            raise TooHighError(amount)
        else: return amount * 2

