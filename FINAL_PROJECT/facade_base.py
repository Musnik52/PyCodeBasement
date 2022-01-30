from abc import ABC, abstractmethod
from datetime import datetime
from flights import Flights
from users import Users
from airline_companies import AirlineCompanies
from countries import Countries
from error_short_password import PasswordTooShort
from error_airline_not_found import AirlineNotFound
from error_flight_not_found import FlightNotFound
from error_invalid_input import InvalidInput
from error_invalid_country import InvalidCountry

class FacadeBase(ABC):

    @abstractmethod
    def __init__(self, repo):
        self.repo = repo

    def get_all_flights(self):
        return self.repo.get_all(Flights)

    def get_flight_by_id(self, id):
        if not isinstance(id, int): raise InvalidInput('Input must be an integer!')
        elif self.repo.get_by_id(Flights, id) == None: raise FlightNotFound
        else: return self.repo.get_by_id(Flights, id)

    def get_flights_by_parameters(self, origin_country_id, destination_country_id, date):
        if not isinstance(origin_country_id, int): raise InvalidInput('Input must be an integer!')
        elif not isinstance(destination_country_id, int): raise InvalidInput('Input must be an integer!')
        elif not isinstance(date, datetime): raise InvalidInput('Input must be a datetime object!')
        elif self.repo.get_by_condition(Flights, lambda query: query.filter(Flights.origin_country_id == origin_country_id, Flights.destination_country_id == destination_country_id, Flights.departure_time == date)) == []: raise FlightNotFound
        else: return self.repo.get_by_condition(Flights, lambda query: query.filter(Flights.origin_country_id == origin_country_id, Flights.destination_country_id == destination_country_id, Flights.departure_time == date))

    def get_all_airlines(self):
        return self.repo.get_all(AirlineCompanies)

    def get_airline_by_id(self, id):
        if not isinstance(id, int): raise InvalidInput('Input must be an integer!')
        elif self.repo.get_by_id(AirlineCompanies, id) == None: raise AirlineNotFound
        else: return self.repo.get_by_id(AirlineCompanies, id)

    def get_all_countries(self):
        return self.repo.get_all(Countries)

    def get_country_by_id(self, id):
        if not isinstance(id, int): raise InvalidInput('Input must be an integer!')
        elif self.repo.get_by_id(Countries, id) == None: raise InvalidCountry
        else: return self.repo.get_by_id(Countries, id)

    def create_user(self, user):
        if not isinstance(user, Users): raise InvalidInput('Input must be a "Users" object!')
        elif len(user.password) < 6: raise PasswordTooShort
        else: self.repo.add(user)

    def __str__(self):
        return f'REPOSITORY: {self.repo}'