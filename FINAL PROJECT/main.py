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
repo.add_all([  UserRoles(role_name='administrator'),
                UserRoles(role_name='airline company'), 
                UserRoles(role_name='customer')])
anonymus_facade.create_user([   Users(username='lior420', password='lior1999', email='lior@jb.com', user_role=1), 
                                Users(username='boris52', password='boris1992', email='boris@jb.com', user_role=2)])
admin_facade.add_airline([      AirlineCompanies(name='bazooka air', country_id=1, user_id=1), 
                                AirlineCompanies(name='sky high', country_id=2, user_id=2)])
admin_facade.add_administrator([Administrators(first_name='lior', last_name='musnik', user_id=2),
                                Administrators(first_name='boris', last_name='musnikov', user_id=1)]) 
customer_facade.add_customer([  Customers(first_name='shachar', last_name='harush', address='rashi 31', phone_number='0507897765', credit_card_number='13323432', user_id=1), 
                                Customers(first_name='max', last_name='gendalev', address='amsterdam 32', phone_number='0523452231', credit_card_number='13245678', user_id=2)])
airline_facade.add_flight([     Flights(airline_company_id=1, origin_country_id=1, desitnation_country_id=2, departure_time=datetime.now(), landing_time=datetime(2022, 10, 4, 14, 29, 1), remaining_tickets=3),
                                Flights(airline_company_id=2, origin_country_id=2, desitnation_country_id=1, departure_time=datetime.now(), landing_time=datetime(2022, 12, 4, 23, 29, 1), remaining_tickets=432)])
customer_facade.add_ticket(     Tickets(flight_id=1, customer_id=1))
customer_facade.add_ticket(     Tickets(flight_id=2, customer_id=2))
