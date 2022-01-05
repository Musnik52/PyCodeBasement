from abc import ABC, abstractmethod
from db_config import local_session, create_all_entities
from db_repo import DbRepo
from flights import Flights
from airline_companies import AirlineCompanies
from countries import Countries

repo = DbRepo(local_session)

class FacadeBase(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def get_all_flights(self):
        print(repo.get_all(Flights))

    def get_flight_by_id(self, id):
        repo.get_by_id(Flights, id)

    def flights_by_parameters(self, origin_country_id, destination_country_id, date):
        pass

    def get_all_airlines(self):
        print(repo.get_all(AirlineCompanies))

    def get_airline_by_id(self, id):
        repo.get_by_id(AirlineCompanies, id)

    def add_customer(self, customer):
        repo.add(customer)

    def add_airline(self, airline):
        repo.add(airline)

    def get_all_countries(self):
        print(repo.get_all(Countries))

    def get_country_by_id(self, id):
        repo.get_by_id(Countries, id)

    def __str__(self):
        return f''