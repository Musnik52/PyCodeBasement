from facade_base import FacadeBase
from users import Users
from facade_customer import CustomerFacade
from facade_administrator import AdministratorFacade
from airline_companies import AirlineCompanies
from error_user_not_found import UsernameNotFound

class AnonymusFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def login(self, username, password):
        user = self.repo.get_by_column_value(Users, Users.username, username)
        if user.username != username:
            raise UsernameNotFound
        if user.password == password:
            if user.user_role == 1: return AdministratorFacade()
            elif user.user_role == 2: return AirlineCompanies()
            elif user.user_role == 3: return CustomerFacade()
            else: print('Invalid user - role') 

    def create_user(self, user):
        self.repo.add_all(user) #user must be list

    def __str__(self):
        return f'{super().__init__}'