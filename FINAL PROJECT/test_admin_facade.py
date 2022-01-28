import pytest
from db_config import local_session
from db_repo import DbRepo
from facade_airline import AirlineFacade
from facade_administrator import AdministratorFacade
from facade_anonymus import AnonymusFacade
from facade_customer import CustomerFacade
from airline_companies import AirlineCompanies
from customers import Customers
from users import Users
from administrators import Administrators 
from main import main
from error_user_exists import UserAlreadyExists
from error_short_password import PasswordTooShort
from error_unauthorized_user_id import UnauthorizedUserID
from error_admin_not_found import AdminNotFound
from error_airline_not_found import AirlineNotFound
from error_customer_not_found import CustomerNotFound

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

def test_get_all_customers(dao_connection):
    assert dao_connection.get_all_customers() == repo.get_all(Customers)

def test_add_administrator(dao_connection):
    expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=7)
    expected_user = Users(username='testl10r', password='testlior1999', email='testlior@jb.com', user_role=1)
    dao_connection.add_administrator(expected_admin, expected_user)
    assert repo.get_by_column_value(Administrators, Administrators.first_name, 'testlior') != None
    assert repo.get_by_column_value(Users, Users.username, 'testl10r') != None

def test_not_add_administrator(dao_connection):
    with pytest.raises(UserAlreadyExists):
        expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=3)
        expected_user = Users(username='testl10r', password='1234545678', email='testlior@jb.com', user_role=1)
        dao_connection.add_administrator(expected_admin, expected_user)
    with pytest.raises(PasswordTooShort):
        expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=7)
        expected_user = Users(username='testl10r', password='12', email='testlior@jb.com', user_role=1)
        dao_connection.add_administrator(expected_admin, expected_user)
    with pytest.raises(UnauthorizedUserID):
        expected_admin = Administrators(first_name='testlior', last_name='testmusnik', user_id=7)
        expected_user = Users(username='testl10r', password='121223', email='testlior@jb.com', user_role=3)
        dao_connection.add_administrator(expected_admin, expected_user)

def test_add_airline(dao_connection):
    expected_airline = AirlineCompanies(name='testbazooka air', country_id=1, user_id=7)
    expected_user = Users(username='testb0r1s', password='boris1992', email='testboris@jb.com', user_role=2)
    dao_connection.add_airline(expected_airline, expected_user)
    assert repo.get_by_column_value(AirlineCompanies, AirlineCompanies.name, 'testbazooka air') != None
    assert repo.get_by_column_value(Users, Users.username, 'testb0r1s') != None

def test_not_add_airline(dao_connection):
    with pytest.raises(UserAlreadyExists):
        expected_airline = AirlineCompanies(name='testbazooka air', country_id=1, user_id=2)
        expected_user = Users(username='testb0r1s', password='boris1992', email='testboris@jb.com', user_role=2)
        dao_connection.add_airline(expected_airline, expected_user)
    with pytest.raises(PasswordTooShort):
        expected_airline = AirlineCompanies(name='testbazooka air', country_id=1, user_id=7)
        expected_user = Users(username='testb0r1s', password='12', email='testboris@jb.com', user_role=2)
        dao_connection.add_airline(expected_airline, expected_user)
    with pytest.raises(UnauthorizedUserID):
        expected_airline = AirlineCompanies(name='testbazooka air', country_id=1, user_id=7)
        expected_user = Users(username='testb0r1s', password='133232', email='testboris@jb.com', user_role=1)
        dao_connection.add_airline(expected_airline, expected_user)

def test_add_customer(dao_connection):
    expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=7)
    expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
    dao_connection.add_customer(expected_customer, expected_user)
    assert repo.get_by_column_value(Customers, Customers.first_name, 'testkosta') != None
    assert repo.get_by_column_value(Users, Users.username, 'testk0st4') != None

def test_not_add_customer(dao_connection):
    with pytest.raises(UserAlreadyExists):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=3)
        expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
        dao_connection.add_customer(expected_customer, expected_user)
    with pytest.raises(PasswordTooShort):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=7)
        expected_user = Users(username='testk0st4', password='123', email='testkosta@jb.com', user_role=3)
        dao_connection.add_customer(expected_customer, expected_user)
    with pytest.raises(UnauthorizedUserID):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=7)
        expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=1)
        dao_connection.add_customer(expected_customer, expected_user)
    
def test_remove_administrator(dao_connection):
    dao_connection.remove_administrator(1)
    assert repo.get_by_id(Administrators, 1) == None
    assert repo.get_by_id(Users, 3) == None

def test_not_remove_administrator(dao_connection):
    with pytest.raises(AdminNotFound):
        dao_connection.remove_administrator(3)

def test_remove_airline(dao_connection):
    expected_airline = AirlineCompanies(name='testbazooka air', country_id=1, user_id=7)
    expected_user = Users(username='testb0r1s', password='boris1992', email='testboris@jb.com', user_role=2)
    dao_connection.add_airline(expected_airline, expected_user)
    dao_connection.remove_airline(3)
    assert repo.get_by_id(AirlineCompanies, 3) == None
    assert repo.get_by_id(Users, 7) == None

def test_not_remove_airline(dao_connection):
    with pytest.raises(AirlineNotFound):
        dao_connection.remove_airline(3)

def test_remove_customer(dao_connection):
    expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=7)
    expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
    dao_connection.add_customer(expected_customer, expected_user)
    dao_connection.remove_customer(3)
    assert repo.get_by_id(Customers, 3) == None
    assert repo.get_by_id(Users, 7) == None

def test_not_remove_customer(dao_connection):
    with pytest.raises(CustomerNotFound):
        dao_connection.remove_customer(3)