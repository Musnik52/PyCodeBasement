import pytest
import datetime
import time
from db_config import local_session
from db_repo import DbRepo
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
from error_invalid_time import InvalidTime
from error_invalid_location import InvalidLocation
from error_invalid_remaining_tickets import InvalidRemainingTickets
from error_user_exists import UserAlreadyExists
from error_short_password import PasswordTooShort
from error_unauthorized_user_id import UnauthorizedUserID
from error_admin_not_found import AdminNotFound
from error_airline_not_found import AirlineNotFound
from error_no_more_tickets import NoMoreTicketsLeft
from error_flight_not_found import FlightNotFound
from error_customer_not_found import CustomerNotFound

repo = DbRepo(local_session)
admin_facade = AdministratorFacade(repo)
airline_facade = AirlineFacade (repo)
anonymus_facade = AnonymusFacade(repo)
customer_facade = CustomerFacade(repo)

@pytest.fixture(scope='session')
def dao_connection():
    return customer_facade

@pytest.fixture(scope='function', autouse=True)
def dao_init_before_each_test():
    main()

def test_update_customer(dao_connection):
    dao_connection.update_customer({'first_name': 'Samuel'}, 1) 
    assert repo.get_by_column_value(Customers, Customers.first_name, 'Samuel') != None

