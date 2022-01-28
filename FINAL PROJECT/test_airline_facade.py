import pytest
import datetime
from db_config import local_session
from db_repo import DbRepo
from facade_airline import AirlineFacade
from facade_administrator import AdministratorFacade
from facade_anonymus import AnonymusFacade
from facade_customer import CustomerFacade
from flights import Flights
from airline_companies import AirlineCompanies
from main import main
from error_invalid_time import InvalidTime
from error_invalid_location import InvalidLocation
from error_invalid_remaining_tickets import InvalidRemainingTickets
from error_airline_not_found import AirlineNotFound
from error_no_more_tickets import NoMoreTicketsLeft
from error_flight_not_found import FlightNotFound

repo = DbRepo(local_session)
admin_facade = AdministratorFacade(repo)
airline_facade = AirlineFacade (repo)
anonymus_facade = AnonymusFacade(repo)
customer_facade = CustomerFacade(repo)

@pytest.fixture(scope='session')
def dao_connection():
    return airline_facade

@pytest.fixture(scope='function', autouse=True)
def dao_init_before_each_test():
    main()

def test_get_flights_by_airline(dao_connection):
    assert dao_connection.get_flights_by_airline(2) == repo.get_by_column_value(Flights, Flights.airline_company_id, 2)

def test_not_get_flights_by_airline(dao_connection):
    with pytest.raises(AirlineNotFound):
        dao_connection.get_flights_by_airline(3)

def test_add_flight(dao_connection):
    flight = Flights(airline_company_id=2, origin_country_id=1, destination_country_id=2, departure_time=datetime(2022, 1, 4, 10, 10, 10), landing_time=datetime(2022, 1, 24, 10, 29, 1), remaining_tickets=44)
    airline_facade.add_flight(flight)
    assert repo.get_by_id(Flights, 3) != None

def test_not_add_flight(dao_connection):
    with pytest.raises(InvalidTime):
        flight = Flights(airline_company_id=2, origin_country_id=1, destination_country_id=2, departure_time=datetime(2023, 1, 4, 10, 10, 10), landing_time=datetime(2022, 1, 24, 10, 29, 1), remaining_tickets=44)
        dao_connection.add_flight(flight)
    with pytest.raises(InvalidRemainingTickets):
        flight = Flights(airline_company_id=2, origin_country_id=1, destination_country_id=2, departure_time=datetime(2022, 1, 4, 10, 10, 10), landing_time=datetime(2022, 1, 24, 10, 29, 1), remaining_tickets=-44)
        dao_connection.add_flight(flight)
    with pytest.raises(InvalidLocation):
        flight = Flights(airline_company_id=2, origin_country_id=1, destination_country_id=1, departure_time=datetime(2022, 1, 4, 10, 10, 10), landing_time=datetime(2022, 1, 24, 10, 29, 1), remaining_tickets=44)
        dao_connection.add_flight(flight)

def test_update_airline(dao_connection):
    airline_update = {'name':'Up Yours LTD'}
    dao_connection.update_airline(airline_update, 1)
    assert repo.get_by_column_value(AirlineCompanies, AirlineCompanies.name, 'Up Yours LTD') != None

def test_not_update_airline(dao_connection):
    with pytest.raises(AirlineNotFound):
        airline_update = {'name':'Up Yours LTD'}
        dao_connection.update_airline(airline_update, 33)

def test_update_flight(dao_connection):
    flight_update = {'remaining_tickets':12332}
    dao_connection.update_flight(flight_update, 1)
    assert repo.get_by_column_value(Flights, Flights.remaining_tickets, 12332) != None

def test_not_update_flight(dao_connection):
    with pytest.raises(NoMoreTicketsLeft):
        dao_connection.update_flight({'remaining_tickets':-2}, 1)
    with pytest.raises(FlightNotFound):
        dao_connection.update_flight({'remaining_tickets':22}, 33)