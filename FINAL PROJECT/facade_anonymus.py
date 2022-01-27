from facade_base import FacadeBase
from users import Users
from login_token import LoginToken
from facade_customer import CustomerFacade
from facade_administrator import AdministratorFacade
from airline_companies import AirlineCompanies
from error_user_not_found import UsernameNotFound
from error_unauthorized_user_id import UnauthorizedUserID
from error_user_exists import UserAlreadyExists
from error_invalid_password import InvalidPassword

class AnonymusFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def login(self, username, password):
        user = self.repo.get_by_column_value(Users, Users.username, username)
        if user.username != username:
            raise UsernameNotFound
        if user.password == password:
            token = LoginToken(user)
            if user.user_role == 1: return (AdministratorFacade(), token)
            elif user.user_role == 2: return (AirlineCompanies(), token)
            elif user.user_role == 3: return (CustomerFacade(), token)
            else: print('Invalid user role!')
        else: raise InvalidPassword

    def add_customer(self, customer, user):
        if self.repo.get_by_id(Users, customer.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 3: 
            super().create_user(user)
            self.repo.add(customer)
        else: raise UnauthorizedUserID
        #try-Catch inc!

    def __str__(self):
        return f'{super().__init__}'