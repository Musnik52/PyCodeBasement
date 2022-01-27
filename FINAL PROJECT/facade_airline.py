from facade_base import FacadeBase
from airline_companies import AirlineCompanies
from flights import Flights
from login_token import LoginToken
from error_no_more_tickets import NoMoreTicketsLeft
from error_airline_not_found import AirlineNotFound
from error_flight_not_found import FlightNotFound
from error_invalid_time import InvalidTime
from error_invalid_location import InvalidLocation
from error_invalid_token import InvalidToken

class AirlineFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def get_flights_by_airline(self, airline, token):
        if not isinstance(token, LoginToken):
            raise InvalidToken
            # token.user.user_role == 1
        if self.repo.get_by_id(AirlineCompanies, airline) == None: raise AirlineNotFound
        else: return self.repo.get_by_column_value(Flights, Flights.airline_company_id, airline)

    def add_flight(self, flight):
        if flight.departure_time > flight.landing_time: raise InvalidTime
        elif flight.origin_country_id == flight.destination_country_id: raise InvalidLocation
        else: self.repo.add(flight)
        #try-Catch inc!
        #neg. number of tickets

    def update_airline(self, airline):
        airline_id = int(input('Please enter the airline ID number: ')) #no input
        if super().get_airline_by_id(airline_id) == None: raise AirlineNotFound
        else: self.repo.update_by_id(AirlineCompanies, AirlineCompanies.id, airline_id, airline)

    def update_flight(self, flight):
        if flight['remaining_tickets'] < 0: raise NoMoreTicketsLeft
        else:
            flight_id = int(input('Please enter the flight ID: '))
            if super().get_flight_by_id(flight_id) == None: raise FlightNotFound 
            else: 
                self.repo.update_by_id(Flights, Flights.id, flight_id, flight) #flight must be dictionary
                print(f'{flight["remaining_tickets"]} remaining ticket(s) on flight #{flight_id}')

    def __str__(self):
        return f'{super().__init__}'
