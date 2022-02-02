from db_repo import DbRepo
from db_config import local_session, create_all_entities
from facade_anonymus import AnonymusFacade

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
repo.create_all_sp("C:\git\pyCodeBasement\FINAL_PROJECT\sp_file.sql")
print('DONE')
