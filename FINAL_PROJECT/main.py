from db_files.db_repo import DbRepo
from db_files.db_config import local_session, config
from facades.facade_anonymus import AnonymusFacade
from tables.flights import Flights
from tables.tickets import Tickets 
from datetime import datetime

# defining
repo = DbRepo(local_session)
anonymus_facade = AnonymusFacade(repo, config)
admin_facade = anonymus_facade.login('l10r', 'lior1999')
airline_facade = anonymus_facade.login('m4x1m', '2themax')
customer_facade = anonymus_facade.login('3m1l', 'e0m1i2l')

# db_refresh
repo.reset_db()
some_flight = Flights(id=222, airline_company_id=2, origin_country_id=31, destination_country_id=2, departure_time=datetime(2025, 1, 1, 10, 10, 10), landing_time=datetime(2026, 1, 24, 10, 29, 1), remaining_tickets=3)
# some_ticket = Tickets(flight_id=222, customer_id=2)
repo.add(some_flight)
print("#"*55)
me = repo.get_by_id("flights", 222)
print(me)
# print(some_ticket.data_for_web())
print('DONE')
