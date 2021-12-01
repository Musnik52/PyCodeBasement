from employee import Employee

class Worker(Employee):
    def __init__(self, id, name, address, age, b_year, daily_h, rate_h):
        super().__init__(id, name, address, age, b_year)
        self.daily_h = daily_h
        self.rate_h = rate_h
    
    def calc_sal_worker(self):
        super().calc_salary(self.daily_h, self.rate_h)

    def __str__(self):
        return super().__str__() + f' Daily Hours: {self.daily_h}, Hourly Rate: {self.rate_h}'
