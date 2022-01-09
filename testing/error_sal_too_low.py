class TooLowError(Exception):
    def __init__(self, salary, message="Salary Too Low!"):
        self.message = message
        self.salary = salary
        super().__init__(self.message)

    def __str__(self):
        return f'SalaryNotInRangeError: {self.message}'
