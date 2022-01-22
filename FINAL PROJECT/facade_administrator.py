from facade_base import FacadeBase
from customers import Customers
from airline_companies import AirlineCompanies
from administrators import Administrators
from error_airline_not_found import AirlineNotFound
from error_admin_not_found import AdminNotFound
from error_customer_not_found import CustomerNotFound

class AdministratorFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def get_all_customers(self):
        return self.repo.get_all(Customers)

    def add_administrator(self, administrator):
        self.repo.add_all(administrator) #administrator must be list

    def add_airline(self, airline):
        self.repo.add_all(airline) #airline must be list
    
    def remove_administrator(self, administrator):
        if self.repo.get_by_id(AdministratorFacade, administrator) == None: raise AdminNotFound
        else: self.repo.delete_by_id(Administrators, Administrators.id, administrator)

    def remove_airline(self, airline):
        if self.repo.get_by_id(AirlineCompanies, airline) == None: raise AirlineNotFound
        else: self.repo.delete_by_id(AirlineCompanies, AirlineCompanies.id, airline)

    def remove_customer(self, customer):
        if self.repo.get_by_id(Customers, customer) == None: raise CustomerNotFound
        else: self.repo.delete_by_id(Customers, Customers.id, customer)

    def __str__(self):
        return f'{super().__init__}'
