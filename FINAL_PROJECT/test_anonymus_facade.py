import pytest
from db_config import local_session
from db_repo import DbRepo
from facade_anonymus import AnonymusFacade
from customers import Customers
from users import Users
from error_user_exists import UserAlreadyExists
from error_short_password import PasswordTooShort
from error_unauthorized_user_id import UnauthorizedUserID
from error_user_not_found import UsernameNotFound
from error_invalid_password import InvalidPassword
from error_invalid_input import InvalidInput

repo = DbRepo(local_session)
anonymus_facade = AnonymusFacade(repo)

@pytest.fixture(scope='session')
def anonymus_facade_object():
    an_facade = anonymus_facade
    return an_facade

@pytest.fixture(scope='function', autouse=True)
def anonymus_facade_clean():
    repo.reset_db()

def test_login(anonymus_facade_object):
    assert anonymus_facade_object.login('b0r1s', 'boris1992') != None

def test_not_login(anonymus_facade_object):
    with pytest.raises(InvalidInput):
        anonymus_facade_object.login('we6682', 87)
    with pytest.raises(InvalidInput):
        anonymus_facade_object.login(533, 'boris1992')
    with pytest.raises(UsernameNotFound):
        anonymus_facade_object.login('we6682', 'boris1992')
    with pytest.raises(InvalidPassword):
        anonymus_facade_object.login('b0r1s', 'we562')

def test_add_customer(anonymus_facade_object):
    expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=8)
    expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
    anonymus_facade_object.add_customer(expected_customer, expected_user)
    assert repo.get_by_column_value(Customers, Customers.first_name, 'testkosta') != None
    assert repo.get_by_column_value(Users, Users.username, 'testk0st4') != None

def test_not_add_customer(anonymus_facade_object):
    with pytest.raises(InvalidInput):
        expected_customer = "Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=3)"
        expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
        anonymus_facade_object.add_customer(expected_customer, expected_user)
    with pytest.raises(InvalidInput):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=3)
        expected_user = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=3)
        anonymus_facade_object.add_customer(expected_customer, expected_user)
    with pytest.raises(UserAlreadyExists):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=3)
        expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=3)
        anonymus_facade_object.add_customer(expected_customer, expected_user)
    with pytest.raises(PasswordTooShort):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=8)
        expected_user = Users(username='testk0st4', password='123', email='testkosta@jb.com', user_role=3)
        anonymus_facade_object.add_customer(expected_customer, expected_user)
    with pytest.raises(UnauthorizedUserID):
        expected_customer = Customers(first_name='testkosta', last_name='testmakarkov', address='testrashi 31', phone_number='test0507897765', credit_card_number='test13323432', user_id=8)
        expected_user = Users(username='testk0st4', password='test1kosta1', email='testkosta@jb.com', user_role=1)
        anonymus_facade_object.add_customer(expected_customer, expected_user)