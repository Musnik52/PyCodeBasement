from facade_base import FacadeBase
from customers import Customers
from airline_companies import AirlineCompanies
from administrators import Administrators
from flights import Flights

class AdministratorFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def get_all_customers(self):
        return self.repo.get_all(Customers)

    def add_administrator(self, administrator):
        self.repo.add(administrator)
    
    def add_all_administrators(self, admin_list):
        self.repo.add_all(admin_list)

    def remove_administrator(self, administrator):
        self.repo.delete_by_id(Administrators, Administrators.id, administrator.id)

    def remove_airline(self, airline):
        self.repo.delete_by_id(AirlineCompanies, AirlineCompanies.id, airline.id)

    def remove_customer(self, customer):
        self.repo.delete_by_id(Customers, Customers.id, customer.id)

    def __str__(self):
        return f'{super().__init__}'
