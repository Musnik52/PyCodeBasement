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
from error_invalid_token import InvalidToken

class AdministratorFacade(FacadeBase):

    def __init__(self, repo, login_token):
        super().__init__(repo)
        self.login_token = login_token

    def get_all_customers(self):
        if self.login_token.role != 'Administrator': raise InvalidToken
        return self.repo.get_all(Customers)

    def add_administrator(self, administrator, user):
        if self.login_token.role != 'Administrator': raise InvalidToken
        if self.repo.get_by_id(Users, administrator.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 1: 
            super().create_user(user)
            self.repo.add(administrator)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def add_airline(self, airline, user):
        if self.login_token.role != 'Administrator': raise InvalidToken
        if self.repo.get_by_id(Users, airline.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 2: 
            super().create_user(user)
            self.repo.add(airline)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def add_customer(self, customer, user):
        if self.login_token.role != 'Administrator': raise InvalidToken
        if self.repo.get_by_id(Users, customer.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 3: 
            super().create_user(user)
            self.repo.add(customer)
        else: raise UnauthorizedUserID
    
    def remove_administrator(self, administrator):
        if self.login_token.role != 'Administrator': raise InvalidToken
        admin = self.repo.get_by_id(Administrators, administrator)
        if admin == None: raise AdminNotFound
        else: 
            admin_user_id = admin.user_id
            self.repo.delete_by_id(Administrators, Administrators.id, administrator)
            self.repo.delete_by_id(Users, Users.id, admin_user_id)

    def remove_airline(self, airline):
        if self.login_token.role != 'Administrator': raise InvalidToken
        airline1 = self.repo.get_by_id(AirlineCompanies, airline)
        if airline1 == None: raise AirlineNotFound
        else: 
            airline_user_id = airline1.user_id
            self.repo.delete_by_id(AirlineCompanies, AirlineCompanies.id, airline)
            self.repo.delete_by_id(Users, Users.id, airline_user_id)

    def remove_customer(self, customer):
        if self.login_token.role != 'Administrator': raise InvalidToken
        customer1 = self.repo.get_by_id(Customers, customer)
        if customer1 == None: raise CustomerNotFound
        else: 
            customer1_user_id = customer1.user_id
            self.repo.delete_by_id(Customers, Customers.id, customer)
            self.repo.delete_by_id(Users, Users.id, customer1_user_id)

    def __str__(self):
        return f'{super().__init__}'
