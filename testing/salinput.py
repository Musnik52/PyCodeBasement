class SalaryInputs():
    def get_salary(self, amount):
        # if the amount is not float raise valueError
        # hint: float(amount)
        # if amount > 100_000 raise TooHigherError
        # if amount < 10_000 raise TooLowerError
        # else return amount * 2
        amount = int(input("Enter salary: "))
        if not 10000 > amount:
            raise TooLowerError(amount)
        elif  100000 < amount:
            raise TooHigherError (amount)
        return amount
