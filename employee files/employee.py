from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, id, name, address, age, b_year):
        self.id = id
        self.name = name
        self.address = address
        self.age = age
        self.b_year = b_year

    def calc_salary(self, units, rate):
        print (f'The salary for {self.name} is: {units * rate}')

    def get_age(self):
        print(f'The age is: {2021 - int(self.b_year)}')
    
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Address: {self.address}, Age: {self.age}, Birth Year: {self.b_year}'