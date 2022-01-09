from facade_base import FacadeBase
from db_config import local_session
from db_repo import DbRepo
from customers import Customers
from airline_companies import AirlineCompanies
from administrators import Administrators
from flights import Flights

repo = DbRepo(local_session)

class AdministratorFacade(FacadeBase):

    def __init__(self):
        super().__init__(repo)

    def get_all_customers(self):
        print(repo.get_all(Customers))

    def add_airline(self, airline):
        repo.add(airline)

    def add_customer(self, customer):
        repo.add(customer)

    def add_administrator(self, administrator):
        repo.add(administrator)    

    def remove_administrator(self, administrator):
        repo.delete_by_id(Administrators, Administrators.id, administrator.id)

    def remove_airline(self, airline):
        repo.delete_by_id(AirlineCompanies, AirlineCompanies.id, airline.id)

    def remove_customer(self, customer):
        repo.delete_by_id(Customers, Customers.id, customer.id)

    def update_flight(self, flight):
        repo.update_by_id(Flights, Flights.id, flight.id, flight)

    def __str__(self):
        return f'{super().__init__}'
