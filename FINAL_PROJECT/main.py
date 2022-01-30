from db_config import local_session, create_all_entities
from db_repo import DbRepo
from facade_anonymus import AnonymusFacade
from datetime import datetime

#defining
repo = DbRepo(local_session)

anonymus_facade = AnonymusFacade(repo)
admin_facade = anonymus_facade.login('l10r', 'lior1999')
airline_facade = anonymus_facade.login('m4x1m', '2themax')
customer_facade = anonymus_facade.login('3m1l', 'e0m1i2l')

#db_refresh
repo.delete_all_tables()
create_all_entities()
repo.reset_db()
print('DONE')

print(admin_facade.get_flights_by_parameters(1,3,datetime(2022, 1, 1, 10, 10, 10)))