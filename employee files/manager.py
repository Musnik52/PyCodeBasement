from employee import Employee

class Manager(Employee):
    def __init__(self, id, name, address, age, b_year, empl_num, rate_e):
        super().__init__(id, name, address, age, b_year)
        self.empl_num = empl_num
        self.rate_e = rate_e
    
    def calc_sal_manager(self):
        super().calc_salary(self.empl_num, self.rate_e)
    
    def __str__(self):
        return super().__str__() + f' Number of Employees: {self.empl_num}, Rate per Employee: {self.rate_e}'