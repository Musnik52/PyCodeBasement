from facade_base import FacadeBase
from customers import Customers
from users import Users
from airline_companies import AirlineCompanies
from administrators import Administrators
from error_airline_not_found import AirlineNotFound
from error_admin_not_found import AdminNotFound
from error_customer_not_found import CustomerNotFound
from error_unauthorized_user_id import UnauthorizedUserID
from error_user_exists import UserAlreadyExists

class AdministratorFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def get_all_customers(self):
        return self.repo.get_all(Customers)

    def add_administrator(self, administrator, user):
        if self.repo.get_by_id(Users, administrator.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 1: 
            super().create_user(user)
            self.repo.add(administrator)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def add_airline(self, airline, user):
        if self.repo.get_by_id(Users, airline.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 2: 
            super().create_user(user)
            self.repo.add(airline)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def add_customer(self, customer, user):
        if self.repo.get_by_id(Users, customer.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 3: 
            super().create_user(user)
            self.repo.add(customer)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def add_user_roles(self, user_roles):
        self.repo.add_all(user_roles)
        #redundant
    
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
