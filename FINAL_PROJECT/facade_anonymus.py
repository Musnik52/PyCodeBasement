from facade_base import FacadeBase
from users import Users
from login_token import LoginToken
from facade_customer import CustomerFacade
from facade_administrator import AdministratorFacade
from facade_airline import AirlineFacade
from error_user_not_found import UsernameNotFound
from error_unauthorized_user_id import UnauthorizedUserID
from error_user_exists import UserAlreadyExists
from error_invalid_password import InvalidPassword

class AnonymusFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def login(self, username, password):
        user = self.repo.get_by_column_value(Users, Users.username, username)
        if not self.repo.get_by_column_value(Users, Users.username, username): raise UsernameNotFound
        elif not self.repo.get_by_column_value(Users, Users.password, password): raise InvalidPassword
        else:
            if user[0].user_role == 1: return AdministratorFacade(self.repo, LoginToken(id=user[0].administrators.id, name=user[0].administrators.first_name, role='Administrator'))
            elif user[0].user_role == 2: return AirlineFacade(self.repo, LoginToken(id=user[0].airline_companies.id, name=user[0].airline_companies.name, role='Airline'))
            elif user[0].user_role == 3: return CustomerFacade(self.repo, LoginToken(id=user[0].customers.id, name=user[0].customers.first_name, role='Customer'))
            else: print('Invalid user-role assigned!')

    def add_customer(self, customer, user):
        if self.repo.get_by_id(Users, customer.user_id) != None: raise UserAlreadyExists
        elif user.user_role == 3: 
            super().create_user(user)
            self.repo.add(customer)
        else: raise UnauthorizedUserID

    def __str__(self):
        return f'{super().__init__}'