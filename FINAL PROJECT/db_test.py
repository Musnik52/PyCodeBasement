import pytest
from db_config import local_session, create_all_entities
from db_repo import DbRepo
import time
import datetime
from facade_airline import AirlineFacade
from facade_administrator import AdministratorFacade
from facade_anonymus import AnonymusFacade
from facade_customer import CustomerFacade
from countries import Countries
from flights import Flights
from tickets import Tickets
from airline_companies import AirlineCompanies
from customers import Customers
from users import Users
from user_roles import UserRoles
from administrators import Administrators 
from main import main
from configparser import ConfigParser
from error_user_exists import UserAlreadyExists
from error_short_password import PasswordTooShort

repo = DbRepo(local_session)
admin_facade = AdministratorFacade(repo)
airline_facade = AirlineFacade (repo)
anonymus_facade = AnonymusFacade(repo)
customer_facade = CustomerFacade(repo)

@pytest.fixture(scope='session')
def dao_connection():
    return admin_facade

@pytest.fixture(scope='function', autouse=True)
def dao_init_before_each_test():
    main()

#admin_facade testing:
def test_get_all_customers(dao_connection):
    assert dao_connection.get_all_customers() != None

def test_add_administrator(dao_connection):
    expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=7)
    expected_user = Users(username='testl10r', password='testlior1999', email='testlior@jb.com', user_role=1)
    dao_connection.add_administrator(expected_admin, expected_user)
    assert repo.get_by_column_value(Administrators, Administrators.first_name, 'testlior') != None
    assert repo.get_by_column_value(Users, Users.username, 'testl10r') != None

def test_not_add_administrator(dao_connection):
    with pytest.raises(UserAlreadyExists):
        with pytest.raises(PasswordTooShort):
            expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=1)
            expected_user = Users(username='testl10r', password='123', email='testlior@jb.com', user_role=1)
            dao_connection.add_administrator(expected_admin, expected_user)


#@pytest.mark.parametrize("x,y,z", [(10, 20, 30), (40, 50, 90)])