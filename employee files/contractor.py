from employee import Employee

class Contractor(Employee):
    def __init__(self, id, name, address, age, b_year, proj_num, rate_p):
        super().__init__(id, name, address, age, b_year)
        self.proj_num = proj_num
        self.rate_p = rate_p
    
    def calc_sal_contractor(self):
        super().calc_salary(self.proj_num, self.rate_p)

    def __str__(self):
        return super().__str__() + f' Daily Hours: {self.proj_num}, Hourly Rate: {self.rate_p}'
