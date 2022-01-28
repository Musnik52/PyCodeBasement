from db_config import local_session, create_all_entities
from db_repo import DbRepo
from datetime import datetime
from countries import Countries
from flights import Flights
from tickets import Tickets
from airline_companies import AirlineCompanies
from customers import Customers
from users import Users
from user_roles import UserRoles
from administrators import Administrators 
from facade_administrator import AdministratorFacade   
from facade_airline import AirlineFacade
from facade_anonymus import AnonymusFacade
from facade_customer import CustomerFacade

def main():
    #defining
    repo = DbRepo(local_session)
    admin_facade = AdministratorFacade(repo)
    airline_facade = AirlineFacade (repo)
    anonymus_facade = AnonymusFacade(repo)
    customer_facade = CustomerFacade(repo)

    #deletion of existing tables
    repo.delete_table('countries')
    repo.delete_table('flights')
    repo.delete_table('tickets')
    repo.delete_table('airline_companies')
    repo.delete_table('administrators')
    repo.delete_table('customers')
    repo.delete_table('users')
    repo.delete_table('user_roles')

    create_all_entities()

    #insert data - initial
    repo.add_all([  Countries(name='israel'), 
                    Countries(name='russia')])
    repo.add_all([                  UserRoles(role_name='administrator'),
                                    UserRoles(role_name='airline company'), 
                                    UserRoles(role_name='customer')])
    admin_facade.add_airline(       AirlineCompanies(name='bazooka air', country_id=1, user_id=1), 
                                    Users(username='b0r1s', password='boris1992', email='boris@jb.com', user_role=2)) 
    admin_facade.add_airline(       AirlineCompanies(name='sky high', country_id=2, user_id=2), 
                                    Users(username='m4x1m', password='2themax', email='max@jb.com', user_role=2))
    admin_facade.add_administrator( Administrators(first_name='lior', last_name='musnik', user_id=3), 
                                    Users(username='l10r', password='lior1999', email='lior@jb.com', user_role=1))
    admin_facade.add_administrator( Administrators(first_name='shachar', last_name='harush', user_id=4), 
                                    Users(username='sh4ch4r', password='18031991', email='shachar@jb.com', user_role=1)) 
    anonymus_facade.add_customer(   Customers(first_name='kosta', last_name='makarkov', address='rashi 31', phone_number='0507897765', credit_card_number='13323432', user_id=5), 
                                    Users(username='k0st4', password='1kosta1', email='kosta@jb.com', user_role=3)) 
    anonymus_facade.add_customer(   Customers(first_name='emil', last_name='tayeb', address='amsterdam 32', phone_number='0523452231', credit_card_number='13245678', user_id=6), 
                                    Users(username='3m1l', password='e0m1i2l', email='emil@jb.com', user_role=3))
    airline_facade.add_flight(      Flights(airline_company_id=1, origin_country_id=1, destination_country_id=2, departure_time=datetime(2022, 1, 1, 10, 10, 10), landing_time=datetime(2022, 1, 24, 10, 29, 1), remaining_tickets=3))
    airline_facade.add_flight(      Flights(airline_company_id=2, origin_country_id=2, destination_country_id=1, departure_time=datetime(2022, 3, 18, 10, 12, 10), landing_time=datetime(2022, 12, 4, 23, 29, 1), remaining_tickets=432))
    customer_facade.add_ticket(     Tickets(flight_id=1, customer_id=1))
    customer_facade.add_ticket(     Tickets(flight_id=2, customer_id=2))
    airline_facade.update_flight(   {'remaining_tickets': 0}, 4)

main()
print('DONE')