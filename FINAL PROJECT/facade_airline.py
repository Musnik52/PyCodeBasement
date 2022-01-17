from facade_base import FacadeBase
from db_config import local_session, create_all_entities
from db_repo import DbRepo
from airline_companies import AirlineCompanies
from flights import Flights

repo = DbRepo(local_session)

class AirlineFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def get_flights_by_airline(self, airline):
        return self.repo.get_by_column_value(Flights, Flights.airline_company_id, airline.id)

    def update_airline(self, airline):
        self.repo.update_by_id(AirlineCompanies, AirlineCompanies.id, airline.id, airline)

    def update_flight(self, flight):
        self.repo.update_by_id(Flights, Flights.id, flight.id, flight)

    def __str__(self):
        return f'{super().__init__}'
